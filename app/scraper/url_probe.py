"""Probe candidate document URLs for boards with no usable index page.

Some boards publish documents at guessable dated URLs but provide no index
(New Jersey agendas, Tennessee minutes after a site redesign). Given strftime
URL templates from the board's strategy, this module generates candidates
from known meeting dates (or a bounded daily grid), HEAD-checks them with
modest concurrency, downloads the hits with byte validation, and registers
Meeting/MeetingDocument rows.

Run standalone:
    python -m app.scraper.url_probe NJ_MD TN_MD MO_MD
"""
import asyncio
import logging
import sys
from datetime import date, timedelta

import httpx
from sqlalchemy import select

import app.database as db
from app.config import DOCUMENTS_DIR, USER_AGENT
from app.models import Board, Meeting, MeetingDocument
from app.scraper.collector import (
    _doc_filename,
    _infer_doc_type,
    validate_document_bytes,
)
from app.scraper.strategies import get_strategy

logger = logging.getLogger(__name__)

PROBE_CONCURRENCY = 8
WINDOW_DAYS = 730  # 24-month collection window


def candidate_urls(
    templates: tuple[str, ...] | list[str],
    dates: list[date],
) -> list[tuple[date, str]]:
    """Expand strftime *templates* over *dates* (newest first, deduped)."""
    out: list[tuple[date, str]] = []
    seen: set[str] = set()
    for d in sorted(set(dates), reverse=True):
        for t in templates:
            url = d.strftime(t)
            if url not in seen:
                seen.add(url)
                out.append((d, url))
    return out


def daily_grid(days: int = WINDOW_DAYS) -> list[date]:
    today = date.today()
    return [today - timedelta(days=i) for i in range(days)]


async def _probe_one(client: httpx.AsyncClient, url: str) -> bool:
    """HEAD-check a candidate; GET fallback for servers that reject HEAD."""
    try:
        r = await client.head(url, follow_redirects=True, timeout=15)
        if r.status_code == 200:
            ct = r.headers.get("content-type", "").lower()
            return "html" not in ct
        if r.status_code == 405:  # HEAD not allowed — let the GET decide
            return True
    except Exception:
        pass
    return False


async def probe_board(code: str) -> dict:
    """Probe one board's url_probes templates and persist validated hits."""
    stats = {"candidates": 0, "hits": 0, "docs": 0, "rejected": 0}

    strategy = get_strategy(code)
    if not strategy.url_probes:
        print(f"  [{code}] no url_probes in strategy — skipping")
        return stats

    await db.init_db()
    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == code)
        )).scalar_one_or_none()
        if not board:
            print(f"  [{code}] board not found")
            return stats
        known = [r[0] for r in await session.execute(
            select(Meeting.meeting_date).where(Meeting.board_id == board.id)
        )]

    dates = known or daily_grid()
    candidates = candidate_urls(strategy.url_probes, dates)
    stats["candidates"] = len(candidates)
    print(f"  [{code}] probing {len(candidates)} candidate URLs "
          f"({'known meeting dates' if known else 'daily grid'})")

    sem = asyncio.Semaphore(PROBE_CONCURRENCY)
    hits: list[tuple[date, str]] = []

    async with httpx.AsyncClient(
        headers={"User-Agent": USER_AGENT}, follow_redirects=True,
    ) as client:

        async def check(d: date, url: str):
            async with sem:
                if await _probe_one(client, url):
                    hits.append((d, url))

        await asyncio.gather(*(check(d, u) for d, u in candidates))
        stats["hits"] = len(hits)
        if not hits:
            print(f"  [{code}] no hits")
            return stats

        doc_dir = DOCUMENTS_DIR / code
        doc_dir.mkdir(parents=True, exist_ok=True)

        async with db.async_session() as session:
            for d, url in sorted(hits, reverse=True):
                try:
                    resp = await client.get(url, timeout=60)
                except Exception as exc:
                    logger.warning("GET failed %s: %s", url, exc)
                    continue
                if resp.status_code != 200:
                    continue
                valid, reason = validate_document_bytes(
                    resp.content, "." + url.rsplit(".", 1)[-1].lower()
                    if "." in url.rsplit("/", 1)[-1] else ".pdf",
                )
                if not valid:
                    stats["rejected"] += 1
                    logger.info("REJECT [%s] %s", reason, url)
                    continue

                meeting = (await session.execute(
                    select(Meeting).where(
                        Meeting.board_id == board.id,
                        Meeting.meeting_date == d,
                    )
                )).scalars().first()
                if meeting is None:
                    meeting = Meeting(
                        board_id=board.id,
                        meeting_date=d,
                        title=f"{board.name} — {d.strftime('%B %d, %Y')}",
                        source_url=url,
                    )
                    session.add(meeting)
                    await session.flush()

                existing = (await session.execute(
                    select(MeetingDocument).where(
                        MeetingDocument.meeting_id == meeting.id,
                        MeetingDocument.source_url == url,
                    )
                )).scalars().first()
                if existing:
                    continue

                filename = _doc_filename(url)
                dest_filename = f"{d.isoformat()}_{filename}"
                dest_path = doc_dir / dest_filename
                dest_path.write_bytes(resp.content)
                session.add(MeetingDocument(
                    meeting_id=meeting.id,
                    doc_type=_infer_doc_type(filename),
                    filename=dest_filename,
                    file_path=str(dest_path),
                    source_url=url,
                ))
                stats["docs"] += 1
                print(f"    + {dest_filename}")
            await session.commit()

    print(f"  [{code}] hits={stats['hits']} docs={stats['docs']} "
          f"rejected={stats['rejected']}")
    return stats


async def main():
    codes = sys.argv[1:]
    if not codes:
        print("usage: python -m app.scraper.url_probe CODE [CODE ...]")
        return
    for code in codes:
        await probe_board(code)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s: %(message)s",
                        datefmt="%H:%M:%S")
    asyncio.run(main())
