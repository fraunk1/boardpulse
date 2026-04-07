"""Prepare data bundles for AI summarization and ingest results.

This module does NOT call any LLM directly for the original summarization flow.
It prepares prompt files that Claude Code subagents consume, and ingests their
output back into the database.

Flow:
    1. prepare_board_bundle() — query DB, build prompt, write to data/reports/{code}_prompt.md
    2. (external) Claude Code subagent reads prompt, writes data/reports/{code}_summary.md
    3. ingest_board_summary() — read summary file, store in meetings.summary + DB
    4. prepare_national_bundle() — collect all per-board summaries, write synthesis prompt
    5. (external) Claude Code subagent writes data/reports/YYYY-MM-DD-board-landscape.md
    6. prepare_narrative_prompts() — per-meeting narrative prompts → subagents → ingest
    7. prepare_tldr_prompts() — per-meeting TLDR prompts → subagents → ingest
    8. prepare_board_briefs() — period brief prompts → subagents → ingest
"""
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import selectinload

import app.database as db
from app.config import REPORTS_DIR
from app.models import Board, BoardBrief, Meeting, MeetingDocument
from app.extractor.prompts import (
    per_board_prompt,
    national_synthesis_prompt,
    board_brief_prompt,
    per_meeting_summary_prompt,
    per_meeting_tldr_prompt,
)


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
        minutes_url=board.minutes_url or "",
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


def _parse_summary_frontmatter(text: str) -> tuple[list[str], str]:
    """Extract YAML frontmatter topics from a summary file.

    Returns (topics_list, body_text). If no frontmatter found, returns ([], text).
    """
    import re
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not m:
        return [], text

    frontmatter = m.group(1)
    body = text[m.end():]

    # Extract topics list from YAML (simple parser — no pyyaml dependency)
    topics = []
    tm = re.search(r'topics:\s*\[([^\]]*)\]', frontmatter)
    if tm:
        raw = tm.group(1)
        topics = [t.strip().strip('"').strip("'") for t in raw.split(",") if t.strip()]

    return topics, body


async def ingest_board_summary(board_code: str, source: str = "subagent") -> bool:
    """Read a completed summary file and store it in the database.

    Parses YAML frontmatter for topic tags, then stores the summary text
    and topics on all meetings for that board in the collection window.

    Args:
        board_code: Board to ingest.
        source: Provenance label — 'subagent' (default) or 'ollama'.

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

    # Parse frontmatter for topics
    topics, body = _parse_summary_frontmatter(summary_text)

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

        # Store the board-level summary and topics on all meetings in the period
        for meeting in meetings:
            meeting.summary = summary_text
            meeting.summary_source = source
            if topics:
                meeting.topics = topics
        await session.commit()

    topic_str = f", topics={topics}" if topics else ""
    print(f"  Ingested summary for {board_code} ({len(meetings)} meetings updated{topic_str})")
    return True


async def ingest_all_summaries(source: str = "subagent") -> int:
    """Scan data/reports/ for *_summary.md files and ingest them all.

    Args:
        source: Provenance label — 'subagent' (default) or 'ollama'.

    Returns count of successfully ingested summaries.
    """
    await db.init_db()

    summary_files = sorted(REPORTS_DIR.glob("*_summary.md"))
    if not summary_files:
        print("No summary files found in data/reports/")
        return 0

    print(f"Found {len(summary_files)} summary files to ingest (source={source}).\n")
    success = 0
    for path in summary_files:
        # Extract board_code from filename: CA_MD_summary.md -> CA_MD
        board_code = path.stem.replace("_summary", "")
        if await ingest_board_summary(board_code, source=source):
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


# ---------------------------------------------------------------------------
# Board Briefs + TLDR Summaries (prepare prompts / ingest results)
# ---------------------------------------------------------------------------

PERIODS = [
    ("quarter", 90),
    ("half-year", 180),
    ("year", 365),
]


async def prepare_board_briefs(board_code: str | None = None, skip_existing: bool = True) -> list[Path]:
    """Prepare brief prompt files for boards.

    Writes prompt files to data/reports/{board_code}_brief_{period}.prompt.md
    for each period (quarter, half-year, year) that has meetings.

    If skip_existing=True, skips boards/periods that already have a BoardBrief
    row generated in the last 7 days.

    Returns list of prompt file paths written.
    """
    await db.init_db()

    async with db.async_session() as session:
        if board_code:
            boards = (await session.execute(
                select(Board).where(Board.code == board_code)
            )).scalars().all()
        else:
            boards = (await session.execute(
                select(Board).order_by(Board.state, Board.code)
            )).scalars().all()

    if not boards:
        print(f"No boards found{f' for {board_code}' if board_code else ''}.")
        return []

    # Pre-fetch existing briefs for skip-existing check
    existing_briefs: dict[tuple[int, str], datetime] = {}
    if skip_existing:
        async with db.async_session() as session:
            rows = (await session.execute(
                select(BoardBrief)
            )).scalars().all()
            for r in rows:
                existing_briefs[(r.board_id, r.period)] = r.generated_at

    fresh_cutoff = datetime.now(timezone.utc) - timedelta(days=7)

    prompt_paths = []
    for board in boards:
        print(f"\n{board.code} — {board.name}")

        for period_label, days in PERIODS:
            # Skip if a fresh brief already exists
            if skip_existing and (board.id, period_label) in existing_briefs:
                gen_at = existing_briefs[(board.id, period_label)]
                if gen_at and gen_at.replace(tzinfo=timezone.utc) > fresh_cutoff:
                    print(f"  {period_label}: fresh brief exists — skipped (use --force to regenerate)")
                    continue

            cutoff = date.today() - timedelta(days=days)

            async with db.async_session() as session:
                meetings = (await session.execute(
                    select(Meeting)
                    .where(Meeting.board_id == board.id)
                    .where(Meeting.meeting_date >= cutoff)
                    .order_by(Meeting.meeting_date.desc())
                )).scalars().all()

            if not meetings:
                print(f"  {period_label}: no meetings — skipped")
                continue

            meeting_data = []
            for m in meetings:
                # Get doc IDs for citation references
                async with db.async_session() as session:
                    docs = (await session.execute(
                        select(MeetingDocument)
                        .where(MeetingDocument.meeting_id == m.id)
                    )).scalars().all()

                meeting_data.append({
                    "meeting_id": m.id,
                    "meeting_date": m.meeting_date.isoformat(),
                    "title": m.title,
                    "summary": m.summary,
                    "docs": [{"doc_id": d.id, "doc_type": d.doc_type} for d in docs],
                })

            prompt = board_brief_prompt(
                board_name=board.name,
                board_code=board.code,
                state=board.state,
                period_label=period_label,
                meeting_summaries=meeting_data,
            )

            prompt_path = REPORTS_DIR / f"{board.code}_brief_{period_label}.prompt.md"
            prompt_path.write_text(prompt, encoding="utf-8")
            prompt_paths.append(prompt_path)
            print(f"  {period_label}: {len(meetings)} meetings → {prompt_path.name}")

    print(f"\nPrepared {len(prompt_paths)} brief prompts.")
    return prompt_paths


async def ingest_board_briefs(board_code: str | None = None) -> int:
    """Ingest completed brief files from data/reports/{code}_brief_{period}.md.

    Returns count of briefs ingested.
    """
    await db.init_db()

    pattern = f"{board_code}_brief_*.md" if board_code else "*_brief_*.md"
    brief_files = sorted(
        p for p in REPORTS_DIR.glob(pattern)
        if not p.name.endswith(".prompt.md")  # skip prompt files
    )

    if not brief_files:
        print(f"No brief files found in {REPORTS_DIR}/")
        return 0

    print(f"Found {len(brief_files)} brief files to ingest.\n")
    total = 0

    for path in brief_files:
        # Parse filename: MO_MD_brief_quarter.md → board_code=MO_MD, period=quarter
        stem = path.stem  # e.g., "MO_MD_brief_quarter"
        parts = stem.rsplit("_brief_", 1)
        if len(parts) != 2:
            print(f"  Skipping {path.name} — unexpected filename format")
            continue
        code, period = parts

        brief_text = path.read_text(encoding="utf-8").strip()
        if not brief_text:
            print(f"  Skipping {path.name} — empty file")
            continue

        # Look up board and count meetings in period
        period_days = dict(PERIODS).get(period)
        if not period_days:
            print(f"  Skipping {path.name} — unknown period '{period}'")
            continue

        cutoff = date.today() - timedelta(days=period_days)

        async with db.async_session() as session:
            board = (await session.execute(
                select(Board).where(Board.code == code)
            )).scalar_one_or_none()

            if not board:
                print(f"  Skipping {path.name} — board {code} not found")
                continue

            meeting_count = len((await session.execute(
                select(Meeting)
                .where(Meeting.board_id == board.id)
                .where(Meeting.meeting_date >= cutoff)
            )).scalars().all())

            # Upsert
            existing = (await session.execute(
                select(BoardBrief)
                .where(BoardBrief.board_id == board.id)
                .where(BoardBrief.period == period)
            )).scalar_one_or_none()

            if existing:
                existing.brief_text = brief_text
                existing.meetings_analyzed = meeting_count
                existing.period_start = cutoff
                existing.period_end = date.today()
                existing.generated_at = datetime.now(timezone.utc)
            else:
                session.add(BoardBrief(
                    board_id=board.id,
                    period=period,
                    brief_text=brief_text,
                    meetings_analyzed=meeting_count,
                    period_start=cutoff,
                    period_end=date.today(),
                ))

            await session.commit()

        total += 1
        print(f"  Ingested {code} {period} ({meeting_count} meetings)")

    print(f"\nIngested {total} briefs.")
    return total


async def prepare_narrative_prompts(board_code: str | None = None, skip_existing: bool = True) -> list[Path]:
    """Prepare per-meeting narrative summary prompts with page-segmented text.

    Pulls text from document_pages.text (per-page) so the LLM can cite
    specific pages in its output.

    If skip_existing=True, skips meetings that already have a summary stored.

    Writes prompt files to data/reports/narrative/{board_code}_{meeting_id}.prompt.md.

    Returns list of prompt file paths written.
    """
    from app.models import DocumentPage

    await db.init_db()

    narrative_dir = REPORTS_DIR / "narrative"
    narrative_dir.mkdir(exist_ok=True)

    async with db.async_session() as session:
        query = (
            select(Meeting)
            .join(Board)
            .options(selectinload(Meeting.documents), selectinload(Meeting.board))
        )
        if board_code:
            query = query.where(Board.code == board_code)
        query = query.order_by(Meeting.meeting_date.desc())

        meetings = (await session.execute(query)).scalars().all()

    if not meetings:
        print("No meetings found.")
        return []

    prompt_paths = []
    skipped = 0
    skipped_existing = 0
    for m in meetings:
        # Skip if summary already exists
        if skip_existing and m.summary:
            skipped_existing += 1
            continue

        # Build page-segmented text per document
        doc_sections = []
        for doc in m.documents:
            async with db.async_session() as session:
                pages = (await session.execute(
                    select(DocumentPage)
                    .where(DocumentPage.document_id == doc.id)
                    .where(DocumentPage.text.isnot(None))
                    .order_by(DocumentPage.page_number)
                )).scalars().all()

            if not pages:
                continue

            doc_sections.append({
                "doc_id": doc.id,
                "doc_type": doc.doc_type,
                "filename": doc.filename,
                "pages": [{"page_number": p.page_number, "text": p.text} for p in pages],
            })

        if not doc_sections:
            skipped += 1
            continue

        prompt = per_meeting_summary_prompt(
            board_name=m.board.name,
            meeting_date=m.meeting_date.isoformat(),
            meeting_title=m.title,
            doc_sections=doc_sections,
        )

        prompt_path = narrative_dir / f"{m.board.code}_{m.id}.prompt.md"
        prompt_path.write_text(prompt, encoding="utf-8")
        prompt_paths.append(prompt_path)

    extra = f", {skipped_existing} skipped — already exist" if skipped_existing else ""
    print(f"Prepared {len(prompt_paths)} narrative prompts ({skipped} skipped — no text{extra}).")
    print(f"Prompts written to: {narrative_dir}/")
    return prompt_paths


async def ingest_narrative_summaries(
    board_code: str | None = None,
    source: str = "subagent",
) -> int:
    """Ingest completed narrative files from data/reports/narrative/{code}_{id}.md.

    Writes to meetings.summary and tags meetings.summary_source with provenance.
    Returns count of summaries ingested.
    """
    await db.init_db()

    narrative_dir = REPORTS_DIR / "narrative"
    pattern = f"{board_code}_*.md" if board_code else "*.md"
    files = sorted(
        p for p in narrative_dir.glob(pattern)
        if not p.name.endswith(".prompt.md")
    )

    if not files:
        print(f"No narrative files found in {narrative_dir}/")
        return 0

    print(f"Found {len(files)} narrative files to ingest.\n")
    total = 0

    for path in files:
        stem = path.stem
        parts = stem.rsplit("_", 1)
        if len(parts) != 2:
            continue
        try:
            meeting_id = int(parts[1])
        except ValueError:
            continue

        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue

        async with db.async_session() as session:
            meeting = await session.get(Meeting, meeting_id)
            if meeting:
                meeting.summary = text
                meeting.summary_source = source
                await session.commit()
                total += 1

    print(f"Ingested {total} narrative summaries (source={source}).")
    return total


async def prepare_tldr_prompts(board_code: str | None = None, skip_existing: bool = True) -> list[Path]:
    """Prepare TLDR prompt files for meetings with document text.

    If skip_existing=True, skips meetings that already have a tldr stored.

    Writes prompt files to data/reports/tldr/{board_code}_{meeting_id}.prompt.md.

    Returns list of prompt file paths written.
    """
    await db.init_db()

    tldr_dir = REPORTS_DIR / "tldr"
    tldr_dir.mkdir(exist_ok=True)

    async with db.async_session() as session:
        query = (
            select(Meeting)
            .join(Board)
            .options(selectinload(Meeting.documents), selectinload(Meeting.board))
        )
        if board_code:
            query = query.where(Board.code == board_code)
        query = query.order_by(Meeting.meeting_date.desc())

        meetings = (await session.execute(query)).scalars().all()

    if not meetings:
        print("No meetings found.")
        return []

    prompt_paths = []
    skipped = 0
    skipped_existing = 0
    for m in meetings:
        if skip_existing and m.tldr:
            skipped_existing += 1
            continue
        doc_texts = [d.content_text for d in m.documents if d.content_text]
        if not doc_texts:
            skipped += 1
            continue

        prompt = per_meeting_tldr_prompt(
            board_name=m.board.name,
            meeting_date=m.meeting_date.isoformat(),
            meeting_title=m.title,
            doc_texts=doc_texts,
        )

        prompt_path = tldr_dir / f"{m.board.code}_{m.id}.prompt.md"
        prompt_path.write_text(prompt, encoding="utf-8")
        prompt_paths.append(prompt_path)

    extra = f", {skipped_existing} skipped — already exist" if skipped_existing else ""
    print(f"Prepared {len(prompt_paths)} TLDR prompts ({skipped} skipped — no text{extra}).")
    print(f"Prompts written to: {tldr_dir}/")
    return prompt_paths


async def ingest_tldr_summaries(
    board_code: str | None = None,
    source: str = "subagent",
) -> int:
    """Ingest completed TLDR files from data/reports/tldr/{code}_{id}.md.

    Writes to meetings.tldr and tags meetings.tldr_source with provenance.
    Returns count of TLDRs ingested.
    """
    await db.init_db()

    tldr_dir = REPORTS_DIR / "tldr"
    pattern = f"{board_code}_*.md" if board_code else "*.md"
    tldr_files = sorted(
        p for p in tldr_dir.glob(pattern)
        if not p.name.endswith(".prompt.md")
    )

    if not tldr_files:
        print(f"No TLDR files found in {tldr_dir}/")
        return 0

    print(f"Found {len(tldr_files)} TLDR files to ingest.\n")
    total = 0

    for path in tldr_files:
        # Parse filename: MO_MD_123.md → meeting_id=123
        stem = path.stem
        parts = stem.rsplit("_", 1)
        if len(parts) != 2:
            continue
        try:
            meeting_id = int(parts[1])
        except ValueError:
            continue

        tldr_text = path.read_text(encoding="utf-8").strip()
        if not tldr_text:
            continue

        async with db.async_session() as session:
            meeting = await session.get(Meeting, meeting_id)
            if meeting:
                meeting.tldr = tldr_text
                meeting.tldr_source = source
                await session.commit()
                total += 1

    print(f"Ingested {total} TLDRs (source={source}).")
    return total
