"""Collect meeting documents from discovered board minutes pages.

Visits each board's minutes_url, takes a full-page screenshot, extracts
links, identifies meeting entries by date, and downloads associated
documents (PDFs, DOCX, etc.) for later text extraction.
"""
import asyncio
import logging
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urljoin, urlparse

import httpx
from playwright.async_api import async_playwright
from sqlalchemy import select

from app.scraper.browser_provider import launch_browser
from app.database import async_session, init_db
from app.models import Board, Meeting, MeetingDocument
from app.config import SCRAPE_DELAY_SECONDS, SCREENSHOTS_DIR, DOCUMENTS_DIR, USER_AGENT

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Date patterns — ordered most-specific first
# ---------------------------------------------------------------------------

DATE_PATTERNS = [
    # "January 15, 2026" or "Jan 15, 2026" (comma optional)
    re.compile(
        r'((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?'
        r'|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?'
        r'|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4})',
        re.IGNORECASE,
    ),
    # "2026-01-15"
    re.compile(r'(\d{4}-\d{2}-\d{2})'),
    # "01/15/2026"
    re.compile(r'(\d{1,2}/\d{1,2}/\d{4})'),
]

# File extensions we consider downloadable documents
DOCUMENT_EXTENSIONS = {".pdf", ".docx", ".doc", ".xlsx", ".xls"}

# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------


def parse_date(text: str) -> date | None:
    """Try to extract a date from *text* using known patterns.

    Returns the first successfully-parsed date, or ``None``.
    """
    for pattern in DATE_PATTERNS:
        m = pattern.search(text)
        if not m:
            continue
        raw = m.group(1).strip()
        # Try multiple strptime formats for the matched string
        for fmt in (
            "%B %d, %Y",   # January 15, 2026
            "%B %d %Y",    # January 15 2026
            "%b %d, %Y",   # Jan 15, 2026
            "%b %d %Y",    # Jan 15 2026
            "%Y-%m-%d",    # 2026-01-15
            "%m/%d/%Y",    # 01/15/2026
        ):
            try:
                return datetime.strptime(raw, fmt).date()
            except ValueError:
                continue
    return None


def is_within_window(d: date, months: int = 12) -> bool:
    """Return True if *d* is within the last *months* months from today."""
    cutoff = date.today() - timedelta(days=months * 30)
    return d >= cutoff


# ---------------------------------------------------------------------------
# Link extraction JS — runs inside the browser page
# ---------------------------------------------------------------------------

_EXTRACT_LINKS_JS = """() => {
    const docExts = ['.pdf', '.docx', '.doc', '.xlsx', '.xls'];
    const results = [];
    for (const a of document.querySelectorAll('a[href]')) {
        const href = a.href || '';
        const text = (a.innerText || a.textContent || '').trim();
        const parentText = (a.parentElement ? a.parentElement.innerText || '' : '').trim();
        const lowerHref = href.toLowerCase();
        const isDoc = docExts.some(ext => lowerHref.endsWith(ext));
        results.push({href, text, parentText, isDoc});
    }
    return results;
}"""

# ---------------------------------------------------------------------------
# Document type inference
# ---------------------------------------------------------------------------


def _infer_doc_type(filename: str) -> str:
    """Guess document type from filename keywords."""
    lower = filename.lower()
    if "agenda" in lower:
        return "agenda"
    if "notice" in lower:
        return "notice"
    if "attachment" in lower or "exhibit" in lower:
        return "attachment"
    return "minutes"


# ---------------------------------------------------------------------------
# Download helper
# ---------------------------------------------------------------------------


async def _download_file(
    client: httpx.AsyncClient,
    url: str,
    dest: Path,
) -> bool:
    """Download *url* to *dest*. Returns True on success."""
    try:
        resp = await client.get(url, follow_redirects=True, timeout=60)
        if resp.status_code != 200:
            logger.warning("HTTP %s downloading %s", resp.status_code, url)
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(resp.content)
        logger.info("Downloaded %s → %s", url, dest)
        return True
    except Exception as exc:
        logger.warning("Failed to download %s: %s", url, exc)
        return False


# ---------------------------------------------------------------------------
# collect_board — process one board
# ---------------------------------------------------------------------------


async def collect_board(board: Board, page) -> dict:
    """Collect meeting minutes and documents for a single board.

    Args:
        board: Board ORM instance (must have minutes_url set).
        page: Playwright page to reuse.

    Returns:
        Stats dict with keys: meetings_found, documents_downloaded, errors.
    """
    stats = {"meetings_found": 0, "documents_downloaded": 0, "errors": 0}

    if not board.minutes_url:
        logger.info("Skipping %s — no minutes_url", board.code)
        return stats

    logger.info("Collecting %s → %s", board.code, board.minutes_url)

    # 1. Navigate to the minutes page
    try:
        await page.goto(board.minutes_url, wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(3)  # Allow JS to render
    except Exception as exc:
        logger.error("Failed to load %s: %s", board.minutes_url, exc)
        stats["errors"] += 1
        return stats

    # 2. Full-page screenshot
    ss_dir = SCREENSHOTS_DIR / board.code
    ss_dir.mkdir(parents=True, exist_ok=True)
    ss_path = ss_dir / "minutes_page.png"
    try:
        await page.screenshot(path=str(ss_path), full_page=True)
        logger.info("Screenshot saved → %s", ss_path)
    except Exception as exc:
        logger.warning("Screenshot failed for %s: %s", board.code, exc)

    # 3. Extract all links
    try:
        links = await page.evaluate(_EXTRACT_LINKS_JS)
    except Exception as exc:
        logger.error("Link extraction failed for %s: %s", board.code, exc)
        stats["errors"] += 1
        return stats

    # 4. Identify meeting entries — group links by date
    #    Each link may carry date context in its text or parent text.
    meetings_map: dict[date, list[dict]] = {}

    for link in links:
        combined_text = f"{link.get('text', '')} {link.get('parentText', '')}"
        d = parse_date(combined_text)
        if d is None:
            continue
        if not is_within_window(d):
            continue
        meetings_map.setdefault(d, []).append(link)

    if not meetings_map:
        logger.info("No dated meeting links found for %s", board.code)
        return stats

    # 5. Persist meetings and download documents
    async with async_session() as session:
        async with httpx.AsyncClient(
            headers={"User-Agent": USER_AGENT},
            follow_redirects=True,
        ) as client:
            for meeting_date in sorted(meetings_map):
                meeting_links = meetings_map[meeting_date]

                # Idempotent — skip if meeting already recorded
                existing = await session.execute(
                    select(Meeting).where(
                        Meeting.board_id == board.id,
                        Meeting.meeting_date == meeting_date,
                    )
                )
                if existing.scalars().first():
                    logger.debug(
                        "Meeting %s %s already exists — skipping",
                        board.code,
                        meeting_date,
                    )
                    continue

                # Create Meeting record
                meeting = Meeting(
                    board_id=board.id,
                    meeting_date=meeting_date,
                    title=f"{board.name} — {meeting_date.strftime('%B %d, %Y')}",
                    source_url=board.minutes_url,
                    screenshot_path=str(ss_path),
                )
                session.add(meeting)
                await session.flush()  # get meeting.id
                stats["meetings_found"] += 1

                # Download document links associated with this date
                doc_dir = DOCUMENTS_DIR / board.code
                doc_dir.mkdir(parents=True, exist_ok=True)

                for link in meeting_links:
                    href = link.get("href", "")
                    if not link.get("isDoc"):
                        continue

                    # Resolve relative URLs
                    full_url = urljoin(board.minutes_url, href)
                    parsed = urlparse(full_url)
                    filename = Path(parsed.path).name or "document"

                    # Prefix with date for uniqueness
                    safe_date = meeting_date.isoformat()
                    dest_filename = f"{safe_date}_{filename}"
                    dest_path = doc_dir / dest_filename

                    if dest_path.exists():
                        logger.debug("File already exists: %s", dest_path)
                        continue

                    ok = await _download_file(client, full_url, dest_path)
                    if ok:
                        doc = MeetingDocument(
                            meeting_id=meeting.id,
                            doc_type=_infer_doc_type(filename),
                            filename=dest_filename,
                            file_path=str(dest_path),
                            source_url=full_url,
                        )
                        session.add(doc)
                        stats["documents_downloaded"] += 1
                    else:
                        stats["errors"] += 1

            await session.commit()

    return stats


# ---------------------------------------------------------------------------
# collect_all — run collection for all (or one) board
# ---------------------------------------------------------------------------


async def collect_all(board_code: str | None = None):
    """Run document collection for discovered boards.

    Args:
        board_code: If provided, only collect for this specific board.
                    Otherwise collect for all boards with discovery_status
                    in ('found', 'manual').
    """
    await init_db()

    # Query target boards
    async with async_session() as session:
        stmt = select(Board).where(Board.minutes_url.isnot(None))
        if board_code:
            stmt = stmt.where(Board.code == board_code)
        else:
            stmt = stmt.where(Board.discovery_status.in_(("found", "manual")))
        result = await session.execute(stmt)
        boards = list(result.scalars().all())

    if not boards:
        print("No boards ready for collection.")
        return

    print(f"Collecting documents for {len(boards)} board(s)...")

    async with async_playwright() as pw:
        browser, context, page = await launch_browser(pw, site_id="collector")

        for i, board in enumerate(boards):
            if i > 0:
                await asyncio.sleep(SCRAPE_DELAY_SECONDS)

            try:
                stats = await collect_board(board, page)
                print(
                    f"  [{board.code}] meetings={stats['meetings_found']}  "
                    f"docs={stats['documents_downloaded']}  "
                    f"errors={stats['errors']}"
                )
            except Exception as exc:
                logger.error("Unexpected error collecting %s: %s", board.code, exc)
                print(f"  [{board.code}] ERROR: {exc}")
                continue

            # Update last_scraped_at
            async with async_session() as session:
                db_board = await session.get(Board, board.id)
                if db_board:
                    db_board.last_scraped_at = datetime.now()
                    await session.commit()

        await browser.close()

    print("Collection complete.")
