"""Fixup pass for IA_MD recovery edge cases.

Fixes two issues from recover_iowa_bom_docs.py:
  1. lnks.gd shortlinks resolved to JS-redirect HTML stubs (~413B). The
     real destination URL is in the HTML body. Parse it, follow it, save.
  2. Google Docs export?format=pdf returned HTTP 410 for some docs. Try
     alternative URL forms (/export?format=html, then /pub).

Run from project root with venv:
    python3 scripts/recover_iowa_fixup.py
"""
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx
from sqlalchemy import select
from app import database as db
from app.models import Board, Meeting, MeetingDocument

USER_AGENT = "Mozilla/5.0 (compatible; boardpulse/1.0)"


def parse_lnks_destination(html: str) -> str | None:
    """Extract the real URL from a lnks.gd JS-redirect stub."""
    m = re.search(r'href="([^"]+)"\s+id="destination"', html)
    return m.group(1) if m else None


async def fix_lnks_gd_files(client: httpx.AsyncClient, doc_dir: Path) -> int:
    """Find tiny HTML files (lnks.gd JS stubs) and re-fetch their real targets."""
    fixed = 0
    for path in sorted(doc_dir.glob("*_iowa_bom_agenda.html")):
        if path.stat().st_size > 1024:
            continue  # already a real file
        try:
            html = path.read_text(encoding="utf-8")
        except Exception:
            continue
        dest_url = parse_lnks_destination(html)
        if not dest_url:
            print(f"  {path.name}: no destination found in stub, skip")
            continue
        print(f"  {path.name}: → {dest_url}")
        try:
            r = await client.get(dest_url, follow_redirects=True, timeout=60.0)
            if r.status_code != 200:
                print(f"    HTTP {r.status_code}")
                continue
            path.write_bytes(r.content)
            print(f"    ✓ {len(r.content)} bytes")
            fixed += 1
        except Exception as e:
            print(f"    ERROR: {e}")
    return fixed


async def fix_google_docs_minutes(client: httpx.AsyncClient) -> int:
    """Find IA_MD meetings whose minutes link is a docs.google.com doc but
    no MeetingDocument exists for it (export failed). Try alternative URLs."""
    await db.init_db()

    # Hardcoded — the two that 410'd in the previous run
    candidates = [
        ("2026-01-15", "1ikcaOQNrDw_QqCgP-Qcb0ak0TklsPFk4FwrliN8qZ8A"),
        ("2025-12-11", "1ERIotonn6EzNkoaR7R2ceshRZA0oz91btPXuUW3XJug"),
    ]

    fixed = 0
    async with db.async_session() as session:
        ia_board = (await session.execute(
            select(Board).where(Board.code == "IA_MD")
        )).scalar_one()

    from datetime import date as _date
    from app.config import DOCUMENTS_DIR
    doc_dir = DOCUMENTS_DIR / "IA_MD"

    for date_str, doc_id in candidates:
        meeting_date = _date.fromisoformat(date_str)
        print(f"\n[{date_str}] doc_id={doc_id}")

        # Try alternate URL formats in order of preference
        url_attempts = [
            f"https://docs.google.com/document/d/{doc_id}/export?format=html",
            f"https://docs.google.com/document/d/{doc_id}/export?format=txt",
            f"https://docs.google.com/document/d/{doc_id}/pub",
            f"https://docs.google.com/document/d/{doc_id}/preview",
        ]

        success_path = None
        for url in url_attempts:
            try:
                r = await client.get(url, follow_redirects=True, timeout=60.0)
                if r.status_code == 200 and len(r.content) > 1024:
                    ext = "html" if "html" in url or "pub" in url or "preview" in url else "txt"
                    fname = f"{date_str}_iowa_bom_minutes.{ext}"
                    success_path = doc_dir / fname
                    success_path.write_bytes(r.content)
                    print(f"    ✓ {url[-40:]}: {len(r.content)} bytes → {fname}")
                    break
                else:
                    print(f"    HTTP {r.status_code} ({len(r.content)}B): {url[-40:]}")
            except Exception as e:
                print(f"    ERROR on {url[-40:]}: {e}")

        if success_path is None:
            print(f"    All URL attempts failed")
            continue

        # Insert MeetingDocument row
        async with db.async_session() as session:
            meeting = (await session.execute(
                select(Meeting)
                .where(Meeting.board_id == ia_board.id)
                .where(Meeting.meeting_date == meeting_date)
            )).scalar_one_or_none()
            if not meeting:
                print(f"    no meeting row found for {date_str}, skip insert")
                continue
            md = MeetingDocument(
                meeting_id=meeting.id,
                doc_type="minutes",
                filename=success_path.name,
                file_path=str(success_path),
                source_url=f"https://docs.google.com/document/d/{doc_id}/edit?tab=t.0",
            )
            session.add(md)
            await session.commit()
            fixed += 1

    return fixed


async def main() -> int:
    print("=== IA_MD recovery fixup ===")
    from app.config import DOCUMENTS_DIR
    doc_dir = DOCUMENTS_DIR / "IA_MD"

    async with httpx.AsyncClient(
        headers={"User-Agent": USER_AGENT},
        follow_redirects=True,
    ) as client:
        print("\n[1] Resolving lnks.gd JS-redirect stubs")
        n_lnks = await fix_lnks_gd_files(client, doc_dir)
        print(f"    Fixed {n_lnks} lnks.gd files")

        print("\n[2] Recovering Google Docs minutes via alternative URLs")
        n_docs = await fix_google_docs_minutes(client)
        print(f"    Recovered {n_docs} Google Docs minutes")

    print("\n=== Done ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
