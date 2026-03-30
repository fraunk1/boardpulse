"""Bootstrap board registry by scraping the FSMB contact page."""
import asyncio
import re
import json
from datetime import datetime

from playwright.async_api import async_playwright
from sqlalchemy import select

from app.scraper.browser_provider import launch_browser
from app.database import async_session, init_db
from app.models import Board
from app.config import FSMB_CONTACT_URL, SCRAPE_DELAY_SECONDS


def infer_board_type(name: str) -> str:
    """Infer MD/DO/combined from board name."""
    name_lower = name.lower()
    if "osteopath" in name_lower and "medic" not in name_lower:
        return "DO"
    if "osteopath" in name_lower and "medic" in name_lower:
        return "combined"
    return "MD"


def make_board_code(state: str, board_type: str, index: int = 0) -> str:
    """Generate a unique board code like CA_MD, PA_DO."""
    suffix = board_type.upper()
    code = f"{state}_{suffix}"
    if index > 0:
        code += f"_{index}"
    return code


async def bootstrap(force: bool = False):
    """Scrape the FSMB contact page and populate the boards table.

    Args:
        force: If True, re-scrape even if boards already exist.
    """
    await init_db()

    # Check if boards already exist
    if not force:
        async with async_session() as session:
            result = await session.execute(select(Board).limit(1))
            if result.scalars().first():
                print("Boards already populated. Use --force to re-bootstrap.")
                return

    print(f"Bootstrapping from {FSMB_CONTACT_URL}...")

    async with async_playwright() as pw:
        browser, context, page = await launch_browser(pw, site_id="fsmb")

        await page.goto(FSMB_CONTACT_URL, wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(3)  # Let JS render

        # Extract board entries from the page
        boards_data = await page.evaluate("""() => {
            const boards = [];
            const entries = document.querySelectorAll(
                '.state-board, .board-entry, .contact-entry, ' +
                'table tr, .accordion-item, [class*="board"], ' +
                'li, .card, article'
            );

            if (entries.length === 0) {
                return JSON.stringify({fallback: true, html: document.body.innerHTML.substring(0, 50000)});
            }

            for (const entry of entries) {
                const text = entry.innerText || '';
                const links = entry.querySelectorAll('a[href]');
                const urls = Array.from(links).map(a => ({
                    text: a.innerText.trim(),
                    href: a.href,
                }));

                if (text.length > 20 && text.length < 2000) {
                    boards.push({
                        text: text.trim(),
                        urls: urls,
                    });
                }
            }
            return JSON.stringify({fallback: false, entries: boards});
        }""")

        await browser.close()

    data = json.loads(boards_data)

    if data.get("fallback"):
        print("Could not parse structured entries. Saving raw HTML for manual review.")
        from app.config import DATA_DIR
        raw_path = DATA_DIR / "fsmb_contact_raw.html"
        raw_path.write_text(data["html"])
        print(f"Raw HTML saved to {raw_path}")
        print("Please review and populate boards manually or adjust parser.")
        return

    # Parse entries into Board records
    from app.scraper._state_names import STATE_LOOKUP

    url_re = re.compile(r'https?://[^\s<>"]+')
    phone_re = re.compile(r'[\(]?\d{3}[\)]?[-.\s]?\d{3}[-.\s]?\d{4}')

    boards_to_add = []
    seen_codes = set()

    for entry in data.get("entries", []):
        text = entry.get("text", "")
        urls = entry.get("urls", [])

        if len(text) < 30:
            continue

        # Find website URL (prefer .gov or .org links)
        homepage = ""
        for u in urls:
            href = u.get("href", "")
            if any(d in href for d in [".gov", ".org", ".state.", "board"]):
                homepage = href
                break
        if not homepage and urls:
            homepage = urls[0].get("href", "")

        # Find phone
        phone_match = phone_re.search(text)
        phone = phone_match.group(0) if phone_match else None

        # Extract board name (first substantial line)
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        name = lines[0] if lines else text[:100]

        # Infer state
        state = ""
        for state_name, abbr in STATE_LOOKUP.items():
            if state_name.lower() in name.lower():
                state = abbr
                break

        if not state:
            for abbr in STATE_LOOKUP.values():
                if f".{abbr.lower()}." in homepage.lower() or f"/{abbr.lower()}/" in homepage.lower():
                    state = abbr
                    break

        if not state or not homepage:
            continue

        board_type = infer_board_type(name)
        code = make_board_code(state, board_type)

        if code in seen_codes:
            code = make_board_code(state, board_type, index=1)
        if code in seen_codes:
            continue
        seen_codes.add(code)

        address_lines = [l for l in lines[1:] if not phone_re.search(l) and "http" not in l.lower()]
        address = "\n".join(address_lines[:3]) if address_lines else None

        boards_to_add.append(Board(
            state=state,
            code=code,
            name=name,
            board_type=board_type,
            homepage=homepage,
            phone=phone,
            address=address,
            discovery_status="pending",
        ))

    # Save to database
    async with async_session() as session:
        for board in boards_to_add:
            existing = await session.execute(
                select(Board).where(Board.code == board.code)
            )
            if not existing.scalars().first():
                session.add(board)
        await session.commit()

    print(f"Bootstrapped {len(boards_to_add)} boards.")
