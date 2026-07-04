"""Prepare data bundles for AI summarization and ingest results.

This module does NOT call any LLM directly. It prepares prompt files that
Claude Code subagents consume, and ingests their output back into the database.

Flow:
    1. prepare_board_bundle() — query DB, build prompt, write to data/reports/{code}_prompt.md
    2. (external) Claude Code subagent reads prompt, writes data/reports/{code}_summary.md
    3. ingest_board_summary() — normalize + gate the summary file
       (app.quality.gates.check_summary), then store it in meetings.summary
       + DB; rejected files get data/reports/{code}_summary.errors.txt
    4. prepare_national_bundle() — collect all per-board summaries, write synthesis prompt
    5. (external) Claude Code subagent writes data/reports/YYYY-MM-DD-board-landscape.md
"""
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import selectinload

import app.database as db
from app.config import REPORTS_DIR
from app.models import Board, Meeting, MeetingDocument
from app.extractor.prompts import per_board_prompt, national_synthesis_prompt
from app.quality.gates import check_summary, normalize_summary


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


# Per-meeting section delimiter in board summary files. Lenient by design:
# tolerates 2+ '=', flexible spacing, and trailing title text after the date.
_MEETING_DELIM_RE = re.compile(
    r'^\s*={2,}\s*MEETING:\s*(\d{4}-\d{2}-\d{2}).*$', re.MULTILINE)
_END_DELIM_RE = re.compile(r'^\s*={2,}\s*END\s*={2,}\s*$', re.MULTILINE)
_TOPICS_LINE_RE = re.compile(r'^\s*topics:\s*\[?([^\]\n]*)\]?\s*$',
                             re.IGNORECASE | re.MULTILINE)


def _parse_topics_value(raw: str) -> list[str]:
    return [t.strip().strip('"').strip("'")
            for t in raw.split(",") if t.strip()]


def parse_board_summary_file(
    text: str,
) -> tuple[list[str], str, dict[str, tuple[str, list[str]]]]:
    """Parse a board summary file into (board_topics, rollup, meetings).

    File layout (see prompts.per_board_prompt for the authoring contract):
      YAML frontmatter (topics union) -> 12-month board ROLLUP ->
      one "=== MEETING: YYYY-MM-DD ===" block per text-bearing meeting
      (optional "topics: [...]" first line) -> "=== END ===".

    Deliberately lenient: a mangled delimiter loses one section, never the
    file; zero delimiters = LEGACY format (whole body is the rollup,
    meetings={}) so old files degrade to board-page-only summaries.

    Returns:
        (board_topics, rollup_markdown,
         {date_str: (meeting_summary_md, meeting_topics)})
    """
    import re as _re

    board_topics, body = _parse_summary_frontmatter(text.strip())

    matches = list(_MEETING_DELIM_RE.finditer(body))
    if not matches:
        return board_topics, body.strip(), {}

    rollup = body[: matches[0].start()].strip()

    meetings: dict[str, tuple[str, list[str]]] = {}
    for i, m in enumerate(matches):
        date_str = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        section = body[start:end]
        section = _END_DELIM_RE.sub("", section).strip()

        topics: list[str] = []
        tm = _TOPICS_LINE_RE.search(section[:200])
        if tm:
            topics = _parse_topics_value(tm.group(1))
            # remove the topics line from the summary text
            section = (section[: tm.start()] + section[tm.end():]).strip()

        if date_str in meetings:
            print(f"  Warning: duplicate section for {date_str} — first wins")
            continue
        meetings[date_str] = (section, topics)

    return board_topics, rollup, meetings


async def ingest_board_summary(board_code: str, *, force: bool = False) -> bool:
    """Read a completed summary file, gate it, and store it in the database.

    The file is normalized (BOM/fence/whitespace repairs) and then run
    through app.quality.gates.check_summary against the board's actual
    meeting dates and source text. On rejection the errors are written to
    data/reports/{code}_summary.errors.txt (one "CODE: message" line each)
    for the retry agent, and NOTHING is written to the database.

    New contract: the file's rollup goes on Board.summary; each
    "=== MEETING: date ===" section goes on ITS OWN meeting's summary and
    topics. Window meetings absent from the file get summary/topics
    CLEARED (removes stale board-level blobs; textless meetings stay
    honestly empty). Legacy files (no sections) set only the board rollup
    — but only reach the database with force=True, which skips the gate.

    Returns True if successful.
    """
    await db.init_db()

    summary_path = REPORTS_DIR / f"{board_code}_summary.md"
    errors_path = REPORTS_DIR / f"{board_code}_summary.errors.txt"
    if not summary_path.exists():
        print(f"No summary file found at {summary_path}")
        return False

    summary_text = normalize_summary(summary_path.read_text(encoding="utf-8"))
    if not summary_text:
        print(f"Summary file is empty: {summary_path}")
        return False

    cutoff = date.today() - timedelta(days=365)

    # --- Ingest gate: gather the DB-side inputs, then run check_summary ---
    async with db.async_session() as session:
        gate_board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()
        if not gate_board:
            print(f"Board {board_code} not found.")
            return False

        window_meetings = (await session.execute(
            select(Meeting)
            .where(Meeting.board_id == gate_board.id)
            .where(Meeting.meeting_date >= cutoff)
            .options(selectinload(Meeting.documents))
        )).scalars().all()
        all_dates = (await session.execute(
            select(Meeting.meeting_date)
            .where(Meeting.board_id == gate_board.id)
        )).scalars().all()

    source_texts: dict[str, list[str]] = {}
    for m in window_meetings:
        texts = [d.content_text for d in m.documents if d.content_text]
        if texts:
            source_texts.setdefault(m.meeting_date.isoformat(), []).extend(texts)

    if force:
        print(f"  WARNING: force=True — SKIPPING the ingest gate for "
              f"{board_code}. Unvalidated summary content is being written "
              "to the database.")
    else:
        result = check_summary(
            board_code,
            summary_text,
            state=gate_board.state,
            db_text_dates=set(source_texts),
            db_all_dates={d.isoformat() for d in all_dates},
            source_texts_by_date={k: "\n\n".join(v)
                                  for k, v in source_texts.items()},
            minutes_url=gate_board.minutes_url,
            homepage=gate_board.homepage,
        )
        if not result.ok:
            errors_path.write_text(
                "\n".join(f"{e.code}: {e.message}" for e in result.errors)
                + "\n", encoding="utf-8")
            print(f"  REJECTED {board_code}: {len(result.errors)} errors "
                  f"-> {errors_path}")
            return False

    # Gate passed (or bypassed): any prior rejection record is stale.
    errors_path.unlink(missing_ok=True)

    board_topics, rollup, sections = parse_board_summary_file(summary_text)
    legacy = not sections

    now = datetime.now(timezone.utc)

    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()

        if not board:
            print(f"Board {board_code} not found.")
            return False

        # Board-level 12-month rollup
        board.summary = rollup
        board.summarized_at = now

        meetings = (await session.execute(
            select(Meeting)
            .where(Meeting.board_id == board.id)
            .where(Meeting.meeting_date >= cutoff)
        )).scalars().all()

        matched = 0
        window_dates = set()
        for meeting in meetings:
            key = meeting.meeting_date.isoformat()
            window_dates.add(key)
            if key in sections:
                section_md, section_topics = sections[key]
                meeting.summary = section_md
                meeting.topics = section_topics or None
                meeting.summarized_at = now
                matched += 1
            elif not legacy:
                # In the new contract, absence from the file means the
                # meeting has no summarizable text — clear stale blobs.
                meeting.summary = None
                meeting.topics = None
                meeting.summarized_at = None

        ghosts = sorted(set(sections) - window_dates)
        await session.commit()

    ghost_str = f", ghost_dates={ghosts}" if ghosts else ""
    print(f"  Ingested {board_code}: rollup={len(rollup)} chars, "
          f"matched {matched}/{len(meetings)} window meetings"
          f"{', LEGACY format' if legacy else ''}{ghost_str}")
    return True


async def ingest_all_summaries() -> tuple[int, list[str]]:
    """Scan data/reports/ for *_summary.md files and ingest them all.

    Returns (ingested_count, rejected_board_codes). A board lands in the
    rejected list when its file fails the ingest gate (see its
    *_summary.errors.txt) or can't be ingested at all (missing board, etc.).
    """
    await db.init_db()

    summary_files = sorted(REPORTS_DIR.glob("*_summary.md"))
    if not summary_files:
        print("No summary files found in data/reports/")
        return 0, []

    print(f"Found {len(summary_files)} summary files to ingest.\n")
    ingested = 0
    rejected: list[str] = []
    for path in summary_files:
        # Extract board_code from filename: CA_MD_summary.md -> CA_MD
        board_code = path.stem.replace("_summary", "")
        if await ingest_board_summary(board_code):
            ingested += 1
        else:
            rejected.append(board_code)

    rejected_str = f" ({', '.join(rejected)})" if rejected else ""
    print(f"\nINGEST: {ingested} ok, {len(rejected)} rejected{rejected_str}")
    return ingested, rejected


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

        # National synthesis consumes the board ROLLUP only — the
        # per-meeting sections would bloat the prompt ~10x with detail the
        # landscape report doesn't need (citations live in the rollup).
        _topics, rollup, _sections = parse_board_summary_file(summary_text)

        board_summaries.append({
            "board_name": board.name,
            "state": board.state,
            "board_code": board.code,
            "summary_text": rollup,
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
