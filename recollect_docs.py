"""Aggressive document recollector for boards with 0 document files.

Unlike the standard collector which skips existing meetings, this script:
1. Visits the board's minutes page
2. Follows sub-page links (meeting detail pages)
3. Downloads ANY PDF/document links found
4. Associates documents with existing Meeting records by date matching

Usage:
    python recollect_docs.py TX_MD
    python recollect_docs.py TX_MD FL_MD GA_MD
    python recollect_docs.py --all-missing
"""
import asyncio
import logging
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urljoin, urlparse

import httpx
from playwright.async_api import async_playwright
from sqlalchemy import select

import app.database as db
from app.models import Board, Meeting, MeetingDocument
from app.config import DOCUMENTS_DIR, USER_AGENT, SCREENSHOTS_DIR
from app.scraper.collector import parse_date, is_within_window, _infer_doc_type

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DOCUMENT_EXTENSIONS = {".pdf", ".docx", ".doc", ".xlsx", ".xls"}


def _is_doc_url(url: str) -> bool:
    """Check if URL points to a downloadable document."""
    path = urlparse(url).path.lower().split("?")[0]
    return any(path.endswith(ext) for ext in DOCUMENT_EXTENSIONS)


def _is_dynamic_download(url: str, text: str) -> bool:
    """Check if URL is a dynamic file download (no .pdf extension but serves files).

    Catches patterns like:
    - download_resource.asp?id=XXX
    - GetFile.cfm?xxx
    - /download?fileId=XXX
    - /api/documents/XXX
    """
    lower_url = urlparse(url).path.lower()
    lower_text = text.lower()
    # URL patterns that suggest a file download
    download_patterns = ["download", "getfile", "get_file", "fetch", "resource.asp",
                         "attachment", "/file/", "/files/", "document.asp", "docs.asp"]
    url_looks_like_download = any(p in lower_url for p in download_patterns)
    # Text patterns that suggest this is a minutes/agenda document
    text_looks_like_doc = any(kw in lower_text for kw in
                              ["minute", "agenda", "meeting minute", "board meeting minute",
                               "action item", "packet", "approved minute"])
    return url_looks_like_download or (text_looks_like_doc and "?" in url)


def _is_likely_meeting_page(url: str, text: str) -> bool:
    """Heuristic: is this link likely to lead to a meeting detail page with docs?"""
    combined = f"{url} {text}".lower()
    keywords = ["minute", "agenda", "meeting", "board meeting", "action item",
                "summary", "record", "proceeding", "packet", "material"]
    return any(kw in combined for kw in keywords)


async def _download_file(client: httpx.AsyncClient, url: str, dest: Path) -> bool:
    """Download a file. Returns True on success."""
    try:
        resp = await client.get(url, follow_redirects=True, timeout=60)
        if resp.status_code != 200:
            return False
        content_type = resp.headers.get("content-type", "")
        # Skip HTML pages that masquerade as documents
        if "text/html" in content_type and not dest.suffix == ".html":
            return False
        if len(resp.content) < 500:
            return False  # Too small to be a real document
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(resp.content)
        return True
    except Exception:
        return False


async def _extract_all_links(page) -> list[dict]:
    """Extract all links from the current page."""
    return await page.evaluate("""() => {
        const results = [];
        for (const a of document.querySelectorAll('a[href]')) {
            const href = a.href || '';
            const text = (a.innerText || a.textContent || '').trim().substring(0, 300);
            const parentText = (a.parentElement ? (a.parentElement.innerText || '').trim().substring(0, 300) : '');
            results.push({href, text, parentText});
        }
        return results;
    }""")


async def recollect_board(board_code: str):
    """Aggressively recollect documents for a single board."""
    await db.init_db()

    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()

    if not board:
        print(f"Board {board_code} not found")
        return

    if not board.minutes_url:
        print(f"Board {board_code} has no minutes_url")
        return

    # Get existing meetings for date matching
    async with db.async_session() as session:
        meetings = (await session.execute(
            select(Meeting).where(Meeting.board_id == board.id)
        )).scalars().all()

    meeting_by_date = {m.meeting_date: m for m in meetings}
    print(f"\n{'='*60}")
    print(f"RECOLLECTING: {board_code} — {board.name}")
    print(f"Minutes URL: {board.minutes_url}")
    print(f"Existing meetings: {len(meetings)}")
    print(f"{'='*60}")

    doc_dir = DOCUMENTS_DIR / board_code
    doc_dir.mkdir(parents=True, exist_ok=True)

    stats = {"docs_downloaded": 0, "pages_visited": 0, "errors": 0, "matched": 0}
    downloaded_urls = set()

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1440, "height": 900},
        )
        page = await context.new_page()

        # Phase 1: Visit the main minutes page
        print(f"\n[Phase 1] Loading main page...")
        try:
            await page.goto(board.minutes_url, wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(3)
        except Exception as exc:
            print(f"  FAILED to load page: {exc}")
            stats["errors"] += 1
            await browser.close()
            return stats

        stats["pages_visited"] += 1

        # Try clicking year accordions/expand buttons
        try:
            current_year = date.today().year
            for year_label in [str(current_year), str(current_year - 1), str(current_year - 2)]:
                locator = page.locator(
                    "button, summary, [role='button'], a, li, div, span, h2, h3"
                ).filter(has_text=re.compile(rf"^\s*{year_label}\s*$"))
                count = await locator.count()
                for i in range(count):
                    try:
                        await locator.nth(i).click(timeout=2000)
                        await asyncio.sleep(0.5)
                    except Exception:
                        pass
                if count:
                    print(f"  Expanded {count} accordion(s) for {year_label}")
                    await asyncio.sleep(1)
        except Exception:
            pass

        # Also try "Show All" / "View All" / "Load More" type buttons
        try:
            for label in ["Show All", "View All", "Load More", "See All", "All Years", "More"]:
                btn = page.locator(f"button:has-text('{label}'), a:has-text('{label}')")
                if await btn.count() > 0:
                    await btn.first.click(timeout=3000)
                    await asyncio.sleep(2)
                    print(f"  Clicked '{label}' button")
        except Exception:
            pass

        # Extract links from main page
        main_links = await _extract_all_links(page)
        print(f"  Found {len(main_links)} links on main page")

        # Collect document URLs and sub-page URLs
        doc_urls = []  # (url, context_text)
        sub_pages = []  # (url, text) — pages likely to have doc links

        base_domain = urlparse(board.minutes_url).netloc

        for link in main_links:
            href = link["href"]
            text = link["text"]
            combined = f"{text} {link['parentText']} {href}"

            if _is_doc_url(href):
                doc_urls.append((href, combined))
            elif _is_dynamic_download(href, text):
                doc_urls.append((href, combined))
            elif _is_likely_meeting_page(href, text):
                # Only follow sub-pages on the same domain
                if urlparse(href).netloc == base_domain or not urlparse(href).netloc:
                    sub_pages.append((href, combined))

        print(f"  Direct doc links: {len(doc_urls)}")
        print(f"  Candidate sub-pages: {len(sub_pages)}")

        # Phase 2: Visit sub-pages to find more documents
        # Limit to 30 sub-pages to avoid going too deep
        sub_pages = sub_pages[:30]
        if sub_pages:
            print(f"\n[Phase 2] Visiting {len(sub_pages)} sub-pages for documents...")

        for i, (sub_url, sub_context) in enumerate(sub_pages):
            try:
                full_url = urljoin(board.minutes_url, sub_url)
                await page.goto(full_url, wait_until="domcontentloaded", timeout=20000)
                await asyncio.sleep(2)
                stats["pages_visited"] += 1

                sub_links = await _extract_all_links(page)
                found_on_page = 0
                for sl in sub_links:
                    if _is_doc_url(sl["href"]) or _is_dynamic_download(sl["href"], sl["text"]):
                        doc_urls.append((sl["href"], f"{sub_context} {sl['text']} {sl['parentText']}"))
                        found_on_page += 1

                if found_on_page:
                    print(f"  [{i+1}/{len(sub_pages)}] {full_url[:80]} — found {found_on_page} docs")
                else:
                    logger.debug(f"  [{i+1}] No docs on {full_url[:60]}")

            except Exception as exc:
                logger.debug(f"  Sub-page failed: {sub_url[:60]} — {exc}")
                stats["errors"] += 1

        await browser.close()

    print(f"\n[Phase 3] Downloading {len(doc_urls)} documents...")

    # Phase 3: Download documents and match to meetings
    async with httpx.AsyncClient(
        headers={"User-Agent": USER_AGENT},
        follow_redirects=True,
    ) as client:
        for url, context_text in doc_urls:
            full_url = urljoin(board.minutes_url, url)

            if full_url in downloaded_urls:
                continue
            downloaded_urls.add(full_url)

            # Parse date from context
            d = parse_date(context_text)
            if d is None:
                # Try parsing from URL itself
                d = parse_date(full_url)
            if d is None:
                logger.debug(f"  No date for: {full_url[:60]}")
                continue
            if not is_within_window(d, months=36):
                continue

            # Build filename — handle dynamic URLs gracefully
            parsed = urlparse(full_url)
            raw_name = Path(parsed.path).name or ""
            # Clean up query-string filenames
            if "?" in raw_name:
                raw_name = raw_name.split("?")[0]
            # If the path name isn't a useful filename (e.g., download_resource.asp),
            # generate one from the link text
            if not raw_name or not any(raw_name.lower().endswith(ext) for ext in DOCUMENT_EXTENSIONS):
                # Build a slug from link text
                slug = re.sub(r'[^\w\s-]', '', context_text[:60]).strip()
                slug = re.sub(r'[\s]+', '_', slug)
                if not slug:
                    slug = f"document_{hash(full_url) % 10000:04d}"
                raw_name = f"{slug}.pdf"
            filename = raw_name
            dest_filename = f"{d.isoformat()}_{filename}"
            dest_path = doc_dir / dest_filename

            if dest_path.exists():
                logger.debug(f"  Already exists: {dest_filename}")
                continue

            ok = await _download_file(client, full_url, dest_path)
            if not ok:
                stats["errors"] += 1
                continue

            stats["docs_downloaded"] += 1

            # Match to existing meeting or create new one
            meeting = meeting_by_date.get(d)
            if meeting:
                stats["matched"] += 1
            else:
                # Create a new meeting record
                async with db.async_session() as session:
                    meeting = Meeting(
                        board_id=board.id,
                        meeting_date=d,
                        title=f"{board.name} — {d.strftime('%B %d, %Y')}",
                        source_url=board.minutes_url,
                    )
                    session.add(meeting)
                    await session.flush()
                    meeting_by_date[d] = meeting

            # Create document record
            async with db.async_session() as session:
                existing_doc = (await session.execute(
                    select(MeetingDocument).where(
                        MeetingDocument.meeting_id == meeting.id,
                        MeetingDocument.filename == dest_filename,
                    )
                )).scalar_one_or_none()

                if not existing_doc:
                    doc = MeetingDocument(
                        meeting_id=meeting.id,
                        doc_type=_infer_doc_type(filename),
                        filename=dest_filename,
                        file_path=str(dest_path),
                        source_url=full_url,
                    )
                    session.add(doc)
                    await session.commit()

            print(f"  ✓ {dest_filename} → meeting {d}")

    # Summary
    print(f"\n{'─'*60}")
    print(f"RESULTS for {board_code}:")
    print(f"  Pages visited:       {stats['pages_visited']}")
    print(f"  Documents downloaded: {stats['docs_downloaded']}")
    print(f"  Matched to meetings: {stats['matched']}")
    print(f"  Errors:              {stats['errors']}")
    print(f"{'─'*60}")

    return stats


async def main():
    codes = []
    if "--all-missing" in sys.argv:
        # Find all boards with meetings but 0 document files
        await db.init_db()
        async with db.async_session() as session:
            from sqlalchemy import func
            boards = (await session.execute(
                select(Board).where(
                    Board.id.in_(select(Meeting.board_id).distinct())
                )
            )).scalars().all()

        for b in boards:
            doc_dir = DOCUMENTS_DIR / b.code
            file_count = len(list(doc_dir.glob("*"))) if doc_dir.exists() else 0
            if file_count == 0:
                codes.append(b.code)
        print(f"Found {len(codes)} boards with 0 documents: {', '.join(codes)}")
    else:
        codes = [c.upper() for c in sys.argv[1:] if not c.startswith("-")]

    if not codes:
        print("Usage: python recollect_docs.py BOARD_CODE [BOARD_CODE ...]")
        print("       python recollect_docs.py --all-missing")
        return

    total_stats = {"docs_downloaded": 0, "matched": 0, "errors": 0}
    for code in codes:
        try:
            stats = await recollect_board(code)
            if stats:
                total_stats["docs_downloaded"] += stats["docs_downloaded"]
                total_stats["matched"] += stats["matched"]
                total_stats["errors"] += stats["errors"]
        except Exception as exc:
            print(f"\nFATAL ERROR for {code}: {exc}")
            import traceback
            traceback.print_exc()

    if len(codes) > 1:
        print(f"\n{'='*60}")
        print(f"GRAND TOTAL: {total_stats['docs_downloaded']} documents downloaded, "
              f"{total_stats['matched']} matched, {total_stats['errors']} errors")
        print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main())
