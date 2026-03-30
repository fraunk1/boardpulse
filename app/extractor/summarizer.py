"""Prepare data bundles for AI summarization and ingest results.

This module does NOT call any LLM directly. It prepares prompt files that
Claude Code subagents consume, and ingests their output back into the database.

Flow:
    1. prepare_board_bundle() — query DB, build prompt, write to data/reports/{code}_prompt.md
    2. (external) Claude Code subagent reads prompt, writes data/reports/{code}_summary.md
    3. ingest_board_summary() — read summary file, store in meetings.summary + DB
    4. prepare_national_bundle() — collect all per-board summaries, write synthesis prompt
    5. (external) Claude Code subagent writes data/reports/YYYY-MM-DD-board-landscape.md
"""
from datetime import date, timedelta
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import selectinload

import app.database as db
from app.config import REPORTS_DIR
from app.models import Board, Meeting, MeetingDocument
from app.extractor.prompts import per_board_prompt, national_synthesis_prompt


async def prepare_board_bundle(board_code: str) -> Path | None:
    """Prepare a summary prompt file for a single board.

    Queries the database for all meetings with extracted text in the last 12 months,
    builds the prompt, and writes it to data/reports/{board_code}_prompt.md.

    Returns the path to the prompt file, or None if no data available.
    """
    await db.init_db()

    cutoff = date.today() - timedelta(days=365)

    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()

        if not board:
            print(f"Board {board_code} not found.")
            return None

        meetings = (await session.execute(
            select(Meeting)
            .where(Meeting.board_id == board.id)
            .where(Meeting.meeting_date >= cutoff)
            .options(selectinload(Meeting.documents))
            .order_by(Meeting.meeting_date.desc())
        )).scalars().all()

    if not meetings:
        print(f"No meetings found for {board_code} in the last 12 months.")
        return None

    # Check if any meeting has extracted text
    has_text = False
    meetings_data = []
    for m in meetings:
        docs_data = []
        for doc in m.documents:
            if doc.content_text:
                has_text = True
            docs_data.append({
                "doc_type": doc.doc_type,
                "filename": doc.filename,
                "content_text": doc.content_text,
            })
        meetings_data.append({
            "meeting_date": m.meeting_date.isoformat(),
            "title": m.title,
            "documents": docs_data,
        })

    if not has_text:
        print(f"No extracted text available for {board_code}. Run 'extract' first.")
        return None

    prompt = per_board_prompt(
        board_name=board.name,
        state=board.state,
        board_code=board.code,
        meetings=meetings_data,
    )

    prompt_path = REPORTS_DIR / f"{board_code}_prompt.md"
    prompt_path.write_text(prompt, encoding="utf-8")

    meeting_count = len(meetings_data)
    doc_count = sum(len(m["documents"]) for m in meetings_data)
    text_docs = sum(
        1 for m in meetings_data
        for d in m["documents"]
        if d.get("content_text")
    )
    print(f"  {board_code}: {meeting_count} meetings, {doc_count} documents "
          f"({text_docs} with text) -> {prompt_path.name}")

    return prompt_path


async def prepare_all_bundles(board_code: str | None = None) -> list[Path]:
    """Prepare summary prompt files for all boards (or one specific board).

    Returns list of prompt file paths that were written.
    """
    await db.init_db()

    if board_code:
        path = await prepare_board_bundle(board_code)
        return [path] if path else []

    # Find all boards that have meetings with extracted text
    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).order_by(Board.state, Board.code)
        )).scalars().all()

    if not boards:
        print("No boards found. Run 'bootstrap' first.")
        return []

    print(f"Preparing summary bundles for {len(boards)} boards...\n")

    prompt_paths = []
    skipped = 0
    for board in boards:
        path = await prepare_board_bundle(board.code)
        if path:
            prompt_paths.append(path)
        else:
            skipped += 1

    print(f"\nPrepared {len(prompt_paths)} prompt files, skipped {skipped} boards.")
    return prompt_paths


async def ingest_board_summary(board_code: str) -> bool:
    """Read a completed summary file and store it in the database.

    Looks for data/reports/{board_code}_summary.md, reads it, and stores
    the full text in the summary field of each meeting for that board
    (as a board-level summary, not per-meeting).

    Returns True if successful.
    """
    await db.init_db()

    summary_path = REPORTS_DIR / f"{board_code}_summary.md"
    if not summary_path.exists():
        print(f"No summary file found at {summary_path}")
        return False

    summary_text = summary_path.read_text(encoding="utf-8").strip()
    if not summary_text:
        print(f"Summary file is empty: {summary_path}")
        return False

    cutoff = date.today() - timedelta(days=365)

    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()

        if not board:
            print(f"Board {board_code} not found.")
            return False

        meetings = (await session.execute(
            select(Meeting)
            .where(Meeting.board_id == board.id)
            .where(Meeting.meeting_date >= cutoff)
        )).scalars().all()

        # Store the board-level summary on all meetings in the period
        for meeting in meetings:
            meeting.summary = summary_text
        await session.commit()

    print(f"  Ingested summary for {board_code} ({len(meetings)} meetings updated)")
    return True


async def ingest_all_summaries() -> int:
    """Scan data/reports/ for *_summary.md files and ingest them all.

    Returns count of successfully ingested summaries.
    """
    await db.init_db()

    summary_files = sorted(REPORTS_DIR.glob("*_summary.md"))
    if not summary_files:
        print("No summary files found in data/reports/")
        return 0

    print(f"Found {len(summary_files)} summary files to ingest.\n")
    success = 0
    for path in summary_files:
        # Extract board_code from filename: CA_MD_summary.md -> CA_MD
        board_code = path.stem.replace("_summary", "")
        if await ingest_board_summary(board_code):
            success += 1

    print(f"\nIngested {success}/{len(summary_files)} summaries.")
    return success


async def prepare_national_bundle() -> Path | None:
    """Prepare the national landscape synthesis prompt.

    Collects all per-board summary files from data/reports/, builds the
    synthesis prompt, and writes it to data/reports/national_synthesis_prompt.md.

    Returns the path to the prompt file, or None if insufficient data.
    """
    await db.init_db()

    summary_files = sorted(REPORTS_DIR.glob("*_summary.md"))
    if not summary_files:
        print("No per-board summary files found. Run per-board summarization first.")
        return None

    board_summaries = []
    for path in summary_files:
        board_code = path.stem.replace("_summary", "")

        # Look up board metadata
        async with db.async_session() as session:
            board = (await session.execute(
                select(Board).where(Board.code == board_code)
            )).scalar_one_or_none()

        if not board:
            print(f"  Warning: board {board_code} not found in DB, skipping")
            continue

        summary_text = path.read_text(encoding="utf-8").strip()
        if not summary_text:
            continue

        board_summaries.append({
            "board_name": board.name,
            "state": board.state,
            "board_code": board.code,
            "summary_text": summary_text,
        })

    if len(board_summaries) < 2:
        print(f"Only {len(board_summaries)} board summaries available. "
              "Need at least 2 for a meaningful national synthesis.")
        return None

    report_date = date.today()
    prompt = national_synthesis_prompt(board_summaries, report_date)

    prompt_path = REPORTS_DIR / "national_synthesis_prompt.md"
    prompt_path.write_text(prompt, encoding="utf-8")

    states = sorted(set(bs["state"] for bs in board_summaries))
    print(f"National synthesis prompt prepared: {len(board_summaries)} boards, "
          f"{len(states)} states -> {prompt_path.name}")

    return prompt_path
