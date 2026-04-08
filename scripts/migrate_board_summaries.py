"""One-shot migration: split per-board summaries from per-meeting narratives.

Steps:
1. init_db() — creates new `board_summaries` table via Base.metadata.create_all
2. Backfill `board_summaries` from data/reports/{CODE}_summary.md files on disk
3. Reset `meetings.summary` rows whose content is a board summary stamp
   (identified by `---\ntopics:` YAML frontmatter at the start)
4. Verify counts before/after

Run from project root with venv active:
    python3 scripts/migrate_board_summaries.py
"""
import asyncio
import sys
from datetime import date, datetime, timezone
from pathlib import Path

# Add project root to path so `app` is importable when run from scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select, func, text
from app import database as db
from app.models import Board, BoardSummary, Meeting

REPORTS_DIR = Path(__file__).resolve().parent.parent / "data" / "reports"

# Marker that identifies a meeting.summary value that's actually a board summary
# stamp (YAML frontmatter starting with `---\ntopics:`).
BOARD_SUMMARY_MARKER = "---\ntopics:"


def parse_frontmatter(text: str) -> tuple[list[str], str]:
    """Extract topics list and body from YAML-frontmatter Markdown."""
    if not text.startswith("---"):
        return [], text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return [], text
    fm = parts[1]
    body = parts[2].lstrip()
    topics: list[str] = []
    for line in fm.splitlines():
        line = line.strip()
        if line.startswith("topics:"):
            # topics: ["a", "b", "c"]
            payload = line[len("topics:"):].strip()
            if payload.startswith("[") and payload.endswith("]"):
                inner = payload[1:-1]
                topics = [
                    p.strip().strip('"').strip("'")
                    for p in inner.split(",")
                    if p.strip()
                ]
    return topics, body


async def main() -> int:
    print("=== boardpulse arch fix migration ===\n")
    await db.init_db()
    print("[1] init_db() — created/verified board_summaries table")

    # Verify the table exists and integrity is ok
    async with db.engine.begin() as conn:
        result = await conn.execute(text("PRAGMA integrity_check"))
        ic = result.scalar()
        print(f"    PRAGMA integrity_check: {ic}")
        if ic != "ok":
            print("    ABORT: integrity_check failed")
            return 1

        result = await conn.execute(text(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='board_summaries'"
        ))
        if not result.scalar():
            print("    ABORT: board_summaries table not created")
            return 1
        print("    board_summaries table exists")

    # === STEP 2: Backfill board_summaries from disk ===
    print("\n[2] Backfilling board_summaries from data/reports/*_summary.md")
    summary_files = sorted(REPORTS_DIR.glob("*_summary.md"))
    print(f"    Found {len(summary_files)} summary files")

    backfilled = 0
    skipped = 0
    async with db.async_session() as session:
        # Map board codes to ids
        boards_by_code = {
            b.code: b for b in (await session.execute(select(Board))).scalars().all()
        }

        for path in summary_files:
            code = path.stem.replace("_summary", "")
            board = boards_by_code.get(code)
            if not board:
                print(f"    SKIP {code}: no matching board row")
                skipped += 1
                continue

            text_content = path.read_text(encoding="utf-8").strip()
            if not text_content:
                print(f"    SKIP {code}: empty file")
                skipped += 1
                continue

            topics, _body = parse_frontmatter(text_content)

            # Compute period from board's meetings
            meetings = (await session.execute(
                select(Meeting).where(Meeting.board_id == board.id)
            )).scalars().all()
            dates = [m.meeting_date for m in meetings if m.meeting_date]
            period_start = min(dates) if dates else None
            period_end = max(dates) if dates else None

            # Upsert: check if a row already exists for this board
            existing = (await session.execute(
                select(BoardSummary).where(BoardSummary.board_id == board.id)
            )).scalar_one_or_none()

            if existing:
                existing.summary_text = text_content
                existing.topics = topics
                existing.period_start = period_start
                existing.period_end = period_end
                existing.meetings_analyzed = len(meetings)
                existing.source = "subagent"
                existing.generated_at = datetime.now(timezone.utc)
            else:
                bs = BoardSummary(
                    board_id=board.id,
                    summary_text=text_content,
                    topics=topics,
                    period_start=period_start,
                    period_end=period_end,
                    meetings_analyzed=len(meetings),
                    source="subagent",
                    generated_at=datetime.now(timezone.utc),
                )
                session.add(bs)

            backfilled += 1

        await session.commit()

    print(f"    Backfilled {backfilled} board_summaries (skipped {skipped})")

    # === STEP 3: Reset meeting.summary rows that are board summary stamps ===
    print("\n[3] Resetting meeting.summary rows that contain board summary stamps")
    async with db.async_session() as session:
        # Count before
        total_meetings = (await session.execute(
            select(func.count(Meeting.id))
        )).scalar()
        with_summary_before = (await session.execute(
            select(func.count(Meeting.id)).where(Meeting.summary.isnot(None))
        )).scalar()
        with_board_stamp = (await session.execute(
            select(func.count(Meeting.id)).where(
                Meeting.summary.like(f"{BOARD_SUMMARY_MARKER}%")
            )
        )).scalar()
        print(f"    Before: {with_summary_before}/{total_meetings} meetings have summary")
        print(f"            {with_board_stamp} of those are board-summary stamps")

        # Reset the stamps
        result = await session.execute(text(
            "UPDATE meetings SET summary = NULL, summary_source = NULL "
            "WHERE summary LIKE :marker"
        ), {"marker": f"{BOARD_SUMMARY_MARKER}%"})
        await session.commit()
        print(f"    Reset {result.rowcount} meeting.summary fields to NULL")

        # Count after
        with_summary_after = (await session.execute(
            select(func.count(Meeting.id)).where(Meeting.summary.isnot(None))
        )).scalar()
        print(f"    After:  {with_summary_after}/{total_meetings} meetings have summary")

    # === STEP 4: Final verification ===
    print("\n[4] Final state")
    async with db.engine.begin() as conn:
        result = await conn.execute(text("PRAGMA integrity_check"))
        print(f"    PRAGMA integrity_check: {result.scalar()}")

    async with db.async_session() as session:
        bs_count = (await session.execute(
            select(func.count(BoardSummary.id))
        )).scalar()
        print(f"    board_summaries rows: {bs_count}")
        m_with_summary = (await session.execute(
            select(func.count(Meeting.id)).where(Meeting.summary.isnot(None))
        )).scalar()
        print(f"    meetings.summary populated: {m_with_summary}")
        m_with_topics = (await session.execute(
            select(func.count(Meeting.id)).where(Meeting.topics.isnot(None))
        )).scalar()
        print(f"    meetings.topics populated:  {m_with_topics}")

    print("\n=== Done ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
