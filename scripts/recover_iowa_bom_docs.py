"""Recover missing IA_MD documents from DIAL Board of Medicine section.

Uses the link inventory extracted via Playwright (hardcoded below — they
were live-scraped from https://dial.iowa.gov/board-meetings#ibm).

For each (date, doc_type, url) entry:
  1. If a Meeting row exists for that date + IA_MD, use it. Else create one.
  2. If a MeetingDocument with the same source_url already exists, skip.
  3. Else download the doc and insert a MeetingDocument row.

Handles:
  - docs.google.com — export as PDF via /export?format=pdf
  - drive.google.com/file/d/{ID}/view — uc?export=download&id={ID}
  - drive.google.com/drive/folders/{ID} — skip (folder, can't single-shot)
  - content.govdelivery.com/.../bulletins/{ID} — save HTML as .html stub
  - lnks.gd/... — follow redirects, then dispatch on the resolved URL
"""
import asyncio
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx
from sqlalchemy import select
from app import database as db
from app.models import Board, Meeting, MeetingDocument
from app.config import DOCUMENTS_DIR

USER_AGENT = "Mozilla/5.0 (compatible; boardpulse/1.0)"

# Link inventory live-scraped from dial.iowa.gov/board-meetings BoM section.
# Format: (meeting_date, doc_type, url, link_text)
IBM_LINKS = [
    # 2026 — agendas only via lnks.gd, no minutes posted yet
    ("2026-03-19", "agenda", "https://lnks.gd/3/3T2X-hZ", "IBM Agenda 3/19/26"),
    ("2026-02-19", "agenda", "https://lnks.gd/3/3RdpH-Z", "IBM Agenda 2/19/26"),
    ("2026-01-15", "agenda", "https://lnks.gd/3/3RH9vHr", "IBM Agenda 1/15/26"),
    ("2026-01-15", "minutes", "https://docs.google.com/document/d/1ikcaOQNrDw_QqCgP-Qcb0ak0TklsPFk4FwrliN8qZ8A/edit?tab=t.0", "IBM Minutes 1/15/26"),
    # 2025
    ("2025-12-11", "agenda", "https://lnks.gd/2/35P-3nj", "IBM Agenda 12/11/25"),
    ("2025-12-11", "minutes", "https://docs.google.com/document/d/1ERIotonn6EzNkoaR7R2ceshRZA0oz91btPXuUW3XJug/edit?tab=t.0", "IBM Minutes 12/11/25"),
    ("2025-11-13", "agenda", "https://lnks.gd/2/35_D3dR", "IBM Agenda 11/13/25"),
    ("2025-11-13", "minutes", "https://drive.google.com/drive/folders/1CKDwwXk8TBn5rUHgYkuOZETQALopndsC", "IBM Minutes 11/13/25"),
    ("2025-10-23", "agenda", "https://lnks.gd/2/33vzwq_", "IBM Agenda 10/23/25"),
    ("2025-10-23", "minutes", "https://drive.google.com/drive/folders/1CKDwwXk8TBn5rUHgYkuOZETQALopndsC", "IBM Minutes 10/23/25"),
    ("2025-09-25", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3f19a13", "IBM Agenda 9/25/25"),
    ("2025-09-25", "minutes", "https://drive.google.com/file/d/15TBbp9eaHXX9kBMSdG1NCsAt5aZMfwcB/view", "IBM Minutes 9/25/25"),
    ("2025-08-28", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3ec148f", "IBM Agenda 8/28/25"),
    ("2025-08-28", "minutes", "https://docs.google.com/document/d/1YYDsyPEjRtFwa5Z8H5cG5gipSvxO7oP_Fa2nY8g_DUo/edit?tab=t.0", "IBM Minutes 8/28/25"),
    ("2025-07-10", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3e5d93e", "IBM Agenda 7/10/25"),
    ("2025-07-10", "minutes", "https://docs.google.com/document/d/16m4HDiTiEis6JUGJuiT_LBMWYMzlmd6lYZ_QYrS4Ux4/edit?tab=t.0", "IBM Minutes 7/10/25"),
    ("2025-06-12", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3e1bb27", "IBM Agenda 6/12/25"),
    ("2025-06-12", "minutes", "https://drive.google.com/file/d/1OLdWgcgao7olzGwOX3Q0y4-_-4457Sz2/view", "IBM Minutes 6/12/25"),
    ("2025-05-15", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3dd836e", "IBM Agenda 5/15/25"),
    ("2025-05-15", "minutes", "https://drive.google.com/file/d/1FDs0DJHJt5k8F3H3rXvO7skL5KjwXTWe/view", "IBM Minutes 5/15/25"),
    ("2025-04-17", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3d905b3", "IBM Agenda 4/17/25"),
    ("2025-04-17", "minutes", "https://drive.google.com/file/d/1KsUoVpctv3XrM3DPHqp8YJ0B-Ek0fVw4/view?usp=drive_link", "IBM Minutes 4/17/25"),
    ("2025-03-20", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3d42392", "IBM Agenda 3/20/25"),
    ("2025-03-20", "minutes", "https://drive.google.com/file/d/1doUduZyij_jhvc70taXCxlPDtL-UNzBu/view?usp=drive_link", "IBM Minutes 3/20/25"),
    ("2025-02-20", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3cf4e51", "IBM Agenda 2/20/25"),
    ("2025-01-23", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3ca68d0", "IBM Agenda 1/23/25"),
    ("2025-01-23", "minutes", "https://drive.google.com/file/d/1oPbTaZbOdf1Nz59tky7tD35ag1afqS_5/view?usp=drive_link", "IBM Minutes 1/23/25"),
    # 2024
    ("2024-12-12", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3c33e09", "IBM Agenda 12/12/24"),
    ("2024-12-12", "minutes", "https://drive.google.com/file/d/1xpcTYQlUiaGmzFepyO7H3rS-t3EqcFlo/view?usp=drive_link", "IBM Minutes 12/12/24"),
    ("2024-11-14", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3bf5e85", "IBM Agenda 11/14/24"),
    ("2024-11-14", "minutes", "https://drive.google.com/file/d/19Ezj13FKSEpdK6IYuzhs19GaL6mWVkNT/view?usp=drive_link", "IBM Minutes 11/14/24"),
    ("2024-10-17", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3b99e9f", "IBM Agenda 10/17/24"),
    ("2024-10-17", "minutes", "https://drive.google.com/file/d/14hNHyEM9kVYC9mgrfX1OsrPG69hJX2ZG/view?usp=drive_link", "IBM Minutes 10/17/24"),
    ("2024-09-12", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3b31042", "IBM Agenda 9/12/24"),
    ("2024-09-12", "minutes", "https://drive.google.com/file/d/1T9nhSDXt12qg69comD4IuS8F7Jh77-X3/view?usp=drive_link", "IBM Minutes 9/12/24"),
    ("2024-08-22", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3afb6c8", "IBM Agenda 8/22/24"),
    ("2024-08-22", "minutes", "https://drive.google.com/file/d/16qYGtXSL-kjMXyBGcxGfvH-G-8DS5F7C/view?usp=drive_link", "IBM Minutes 8/22/24"),
    ("2024-07-11", "agenda", "https://content.govdelivery.com/accounts/IACIO/bulletins/3a4e6a0", "IBM Agenda 7/11/24"),
    ("2024-07-11", "minutes", "https://drive.google.com/file/d/1ngwqYJ4OxrUoKlMP_Ue9TACTyJbA1r_D/view?usp=drive_link", "IBM Minutes 7/11/24"),
]


def normalize_url(url: str, client: httpx.AsyncClient) -> tuple[str, str | None]:
    """Resolve known URL types into a downloadable form.

    Returns (download_url, file_extension) — file_extension is None if unknown.
    """
    # Google Docs → export as PDF
    m = re.match(r"https://docs\.google\.com/document/d/([^/]+)", url)
    if m:
        return (f"https://docs.google.com/document/d/{m.group(1)}/export?format=pdf", "pdf")

    # Google Drive single file → uc download
    m = re.match(r"https://drive\.google\.com/file/d/([^/]+)", url)
    if m:
        return (f"https://drive.google.com/uc?export=download&id={m.group(1)}", "pdf")

    # Drive folder — can't single-shot, skip
    if "drive.google.com/drive/folders/" in url:
        return (url, None)  # signal: not directly downloadable

    # GovDelivery bulletin — fetch the HTML
    if "content.govdelivery.com" in url:
        return (url, "html")

    # lnks.gd shortlink — let httpx follow redirects, treat as html catch-all
    if "lnks.gd" in url:
        return (url, "html")

    return (url, None)


async def download_one(
    client: httpx.AsyncClient,
    url: str,
    dest: Path,
) -> bool:
    """Stream-download a URL to dest. Returns True on success."""
    try:
        async with client.stream("GET", url, follow_redirects=True, timeout=60.0) as r:
            if r.status_code != 200:
                print(f"      HTTP {r.status_code}: {url}")
                return False
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open("wb") as f:
                async for chunk in r.aiter_bytes(chunk_size=64 * 1024):
                    f.write(chunk)
        size = dest.stat().st_size
        if size < 256:
            print(f"      Suspicious size {size}B — keeping but flag")
        print(f"      ✓ {dest.name} ({size} bytes)")
        return True
    except Exception as e:
        print(f"      ERROR: {e}")
        return False


async def main() -> int:
    print("=== IA_MD recovery from DIAL Board of Medicine section ===\n")
    await db.init_db()

    async with db.async_session() as session:
        ia_board = (await session.execute(
            select(Board).where(Board.code == "IA_MD")
        )).scalar_one()

    doc_dir = DOCUMENTS_DIR / "IA_MD"
    doc_dir.mkdir(parents=True, exist_ok=True)

    stats = {
        "links_processed": 0,
        "meetings_created": 0,
        "documents_downloaded": 0,
        "skipped_already_have": 0,
        "skipped_folder": 0,
        "errors": 0,
    }

    async with httpx.AsyncClient(
        headers={"User-Agent": USER_AGENT},
        follow_redirects=True,
    ) as client:
        for date_str, doc_type, url, link_text in IBM_LINKS:
            stats["links_processed"] += 1
            meeting_date = date.fromisoformat(date_str)
            print(f"[{date_str}] {doc_type}: {link_text}")

            # Find or create the meeting row
            async with db.async_session() as session:
                meeting = (await session.execute(
                    select(Meeting)
                    .where(Meeting.board_id == ia_board.id)
                    .where(Meeting.meeting_date == meeting_date)
                )).scalar_one_or_none()

                if not meeting:
                    meeting = Meeting(
                        board_id=ia_board.id,
                        meeting_date=meeting_date,
                        title=f"Iowa Board of Medicine — {meeting_date.strftime('%B %d, %Y')}",
                        source_url="https://dial.iowa.gov/board-meetings#ibm",
                        scraped_at=datetime.now(timezone.utc),
                    )
                    session.add(meeting)
                    await session.commit()
                    stats["meetings_created"] += 1
                    print(f"      Created meeting row id={meeting.id}")

                # Skip if a doc with the same source_url already exists for this meeting
                existing_doc = (await session.execute(
                    select(MeetingDocument)
                    .where(MeetingDocument.meeting_id == meeting.id)
                    .where(MeetingDocument.source_url == url)
                )).scalar_one_or_none()
                if existing_doc:
                    print(f"      already have doc with this url — skip")
                    stats["skipped_already_have"] += 1
                    continue

                meeting_id = meeting.id

            # Decide download URL + extension
            download_url, ext = normalize_url(url, client)
            if ext is None:
                # Folder or unknown — record as a stub document with no file
                stats["skipped_folder"] += 1
                print(f"      Drive folder — recording stub, can't single-shot")
                async with db.async_session() as session:
                    md = MeetingDocument(
                        meeting_id=meeting_id,
                        doc_type=doc_type,
                        filename=f"{date_str}_{doc_type}_FOLDER_STUB.txt",
                        file_path=str(doc_dir / f"{date_str}_{doc_type}_FOLDER_STUB.txt"),
                        source_url=url,
                        content_text=f"This entry points to a Google Drive folder: {url}\nManual download required.",
                    )
                    session.add(md)
                    await session.commit()
                # Also write the stub file so the path resolves
                (doc_dir / f"{date_str}_{doc_type}_FOLDER_STUB.txt").write_text(
                    f"Google Drive folder: {url}\n", encoding="utf-8"
                )
                continue

            filename = f"{date_str}_iowa_bom_{doc_type}.{ext}"
            dest = doc_dir / filename

            ok = await download_one(client, download_url, dest)
            if not ok:
                stats["errors"] += 1
                continue

            stats["documents_downloaded"] += 1
            async with db.async_session() as session:
                md = MeetingDocument(
                    meeting_id=meeting_id,
                    doc_type=doc_type,
                    filename=filename,
                    file_path=str(dest),
                    source_url=url,
                )
                session.add(md)
                await session.commit()

    print("\n=== Done ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
