"""
Meeting minutes page discoverer.

Crawls board websites to find the page where meeting minutes are posted.
Uses keyword scoring to rank links by relevance, then follows the best
candidates up to max_depth levels deep.
"""

import asyncio
import logging
import re
from urllib.parse import urljoin, urlparse

from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Keyword tiers — (pattern, score)
# Patterns are matched case-insensitively against link text.
# ---------------------------------------------------------------------------

HIGH_KEYWORDS: list[tuple[re.Pattern, int]] = [
    (re.compile(r"meeting\s*minutes", re.IGNORECASE), 90),
    (re.compile(r"board\s*minutes", re.IGNORECASE), 90),
    (re.compile(r"minutes\s*of\s*meeting", re.IGNORECASE), 90),
]

MEDIUM_KEYWORDS: list[tuple[re.Pattern, int]] = [
    (re.compile(r"board\s*meeting", re.IGNORECASE), 60),
    (re.compile(r"public\s*meeting", re.IGNORECASE), 60),
    (re.compile(r"\bmeetings?\b", re.IGNORECASE), 60),
    (re.compile(r"\bagenda\b", re.IGNORECASE), 60),
    (re.compile(r"public\s*session", re.IGNORECASE), 60),
    (re.compile(r"meeting\s*notice", re.IGNORECASE), 60),
    (re.compile(r"meeting\s*schedule", re.IGNORECASE), 60),
]

LOW_KEYWORDS: list[tuple[re.Pattern, int]] = [
    (re.compile(r"\bcalendar\b", re.IGNORECASE), 20),
    (re.compile(r"\bnotices?\b", re.IGNORECASE), 20),
    (re.compile(r"\bschedule\b", re.IGNORECASE), 20),
    (re.compile(r"\bdocuments?\b", re.IGNORECASE), 20),
    (re.compile(r"\barchives?\b", re.IGNORECASE), 20),
    (re.compile(r"public\s*records?", re.IGNORECASE), 20),
]

# External / social domains to ignore
EXTERNAL_BLOCKLIST = {
    "twitter.com",
    "x.com",
    "facebook.com",
    "linkedin.com",
    "youtube.com",
    "instagram.com",
}


def _is_blocked_href(href: str) -> bool:
    """Return True if the href should be ignored (external, social, mailto, tel)."""
    href_lower = href.lower().strip()
    if href_lower.startswith(("mailto:", "tel:", "javascript:")):
        return True
    try:
        parsed = urlparse(href)
        domain = parsed.netloc.lower()
        # Strip www. prefix for matching
        if domain.startswith("www."):
            domain = domain[4:]
        if domain in EXTERNAL_BLOCKLIST:
            return True
    except Exception:
        return True
    return False


def score_link(text: str, href: str) -> int:
    """Score a link 0-100 based on how likely it leads to meeting minutes.

    Args:
        text: The visible link text.
        href: The href attribute value.

    Returns:
        Integer score 0-100. Higher means more likely to be a minutes page.
    """
    if not text or not href:
        return 0

    # Block external / social / mailto / tel links
    if _is_blocked_href(href):
        return 0

    combined = f"{text} {href}"
    best_score = 0

    # Check each tier, keep the highest match
    for pattern, points in HIGH_KEYWORDS:
        if pattern.search(text):
            best_score = max(best_score, points)

    for pattern, points in MEDIUM_KEYWORDS:
        if pattern.search(text):
            best_score = max(best_score, points)

    for pattern, points in LOW_KEYWORDS:
        if pattern.search(text):
            best_score = max(best_score, points)

    # Bonus if "minute" appears in the URL path
    try:
        path = urlparse(href).path.lower()
    except Exception:
        path = href.lower()
    if "minute" in path:
        best_score = min(best_score + 15, 100)

    return best_score


def pick_best_links(
    links: list[dict],
    base_url: str,
    threshold: int = 15,
) -> list[dict]:
    """Filter and sort links by relevance score.

    Args:
        links: List of dicts with "text" and "href" keys.
        base_url: The page URL used to resolve relative hrefs.
        threshold: Minimum score to include a link (default 15).

    Returns:
        List of link dicts (with added "score" and resolved "href"),
        sorted descending by score.
    """
    scored: list[dict] = []
    for link in links:
        text = (link.get("text") or "").strip()
        href = (link.get("href") or "").strip()
        if not href or not text:
            continue

        # Resolve relative URLs
        resolved = urljoin(base_url, href)

        s = score_link(text, resolved)
        if s >= threshold:
            scored.append({
                "text": text,
                "href": resolved,
                "score": s,
            })

    # Sort descending by score, then alphabetically by href for stability
    scored.sort(key=lambda x: (-x["score"], x["href"]))
    return scored


# ---------------------------------------------------------------------------
# Async discovery crawler
# ---------------------------------------------------------------------------

async def _extract_links(page) -> list[dict]:
    """Extract all <a> links from the current page."""
    return await page.evaluate("""
        () => Array.from(document.querySelectorAll('a[href]')).map(a => ({
            text: (a.innerText || a.textContent || '').trim().substring(0, 200),
            href: a.getAttribute('href') || ''
        }))
    """)


async def discover_board(board, page, max_depth: int = 2) -> str | None:
    """Crawl a board's website to find the meeting minutes page.

    Starts at the board's homepage and follows the highest-scoring links
    up to max_depth levels.

    Args:
        board: A Board model instance (needs .homepage and .code).
        page: A Playwright page object.
        max_depth: Maximum link-following depth (default 2).

    Returns:
        The URL of the best minutes page found, or None.
    """
    from app.config import SCREENSHOTS_DIR

    homepage = board.homepage
    best_url: str | None = None
    best_score = 0

    current_url = homepage

    for depth in range(max_depth + 1):
        logger.info(f"[{board.code}] depth={depth} visiting {current_url}")
        try:
            await page.goto(current_url, wait_until="domcontentloaded", timeout=30_000)
            await page.wait_for_timeout(1000)  # Let JS settle
        except Exception as e:
            logger.warning(f"[{board.code}] Failed to load {current_url}: {e}")
            break

        # Screenshot
        try:
            ss_path = SCREENSHOTS_DIR / f"{board.code}_discovery_d{depth}.png"
            await page.screenshot(path=str(ss_path), full_page=False)
            logger.info(f"[{board.code}] Screenshot saved: {ss_path.name}")
        except Exception as e:
            logger.debug(f"[{board.code}] Screenshot failed: {e}")

        # Extract and score links
        raw_links = await _extract_links(page)
        ranked = pick_best_links(raw_links, base_url=current_url)

        if ranked:
            top = ranked[0]
            logger.info(
                f"[{board.code}] Top link: \"{top['text']}\" "
                f"({top['score']}pts) -> {top['href']}"
            )
            if top["score"] > best_score:
                best_score = top["score"]
                best_url = top["href"]

            # Follow the top link if we haven't exhausted depth
            if depth < max_depth:
                current_url = top["href"]
            else:
                break
        else:
            logger.info(f"[{board.code}] No relevant links found at depth {depth}")
            break

    return best_url


async def discover_all(board_code: str | None = None, force: bool = False):
    """Run discovery for all boards (or a single board by code).

    Args:
        board_code: If provided, only discover for this board.
        force: If True, re-discover even if minutes_url is already set.
    """
    from app.database import async_session, init_db
    from app.models import Board
    from app.config import SCRAPE_DELAY_SECONDS
    from app.scraper.browser_provider import launch_browser
    from sqlalchemy import select

    await init_db()

    async with async_session() as session:
        stmt = select(Board)
        if board_code:
            stmt = stmt.where(Board.code == board_code.upper())
        if not force:
            stmt = stmt.where(Board.minutes_url.is_(None))

        result = await session.execute(stmt)
        boards = result.scalars().all()

    if not boards:
        logger.info("No boards to discover.")
        return

    logger.info(f"Discovering minutes pages for {len(boards)} board(s)...")

    async with async_playwright() as pw:
        browser, context, page = await launch_browser(pw, site_id="discoverer")

        try:
            for i, board in enumerate(boards):
                logger.info(f"\n--- [{board.code}] {board.name} ({i+1}/{len(boards)}) ---")
                minutes_url = await discover_board(board, page, max_depth=2)

                # Update the database
                async with async_session() as session:
                    async with session.begin():
                        stmt = select(Board).where(Board.id == board.id)
                        result = await session.execute(stmt)
                        db_board = result.scalar_one()
                        if minutes_url:
                            db_board.minutes_url = minutes_url
                            db_board.discovery_status = "found"
                            logger.info(f"[{board.code}] Minutes URL: {minutes_url}")
                        else:
                            db_board.discovery_status = "not_found"
                            logger.warning(f"[{board.code}] No minutes page found.")

                # Rate limit between boards
                if i < len(boards) - 1:
                    await asyncio.sleep(SCRAPE_DELAY_SECONDS)
        finally:
            await browser.close()

    logger.info("Discovery complete.")
