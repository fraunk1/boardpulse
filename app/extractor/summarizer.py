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
import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import selectinload

import app.database as db
from app.config import REPORTS_DIR
from app.models import Board, Meeting, MeetingDocument
from app.extractor.prompts import (
    per_board_prompt, archive_bundle_prompt, national_synthesis_prompt,
)
from app.quality.gates import check_summary, normalize_summary

# The rolling summary window. Meetings inside it are the rollup's concern;
# meetings older than it belong to the archive backfill.
WINDOW_DAYS = 365

# Archive bundles live in their own subdirectory so the *_summary.md glob
# and the national synthesis never sweep them up as rollup files.
ARCHIVE_DIR = REPORTS_DIR / "archive"


def _write_prompt_sidecar(
    meta_path: Path,
    *,
    mode: str,
    covered_dates: list[str],
    target_dates: list[str],
) -> None:
    """Write the prompt-scope manifest next to a prompt file.

    The sidecar records what dates a prompt actually covered so the ingest
    (and prune) can operate against the prompt's real scope instead of a
    live-recomputed window — which drifts day to day.

    Keys:
      mode           'rollup' or 'archive'
      covered_dates  every meeting date the prompt included as CONTEXT or
                     TARGET (the universe prune is allowed to touch)
      target_dates   the subset the model is asked to emit NEW blocks for
    """
    meta_path.write_text(
        json.dumps(
            {
                "mode": mode,
                "covered_dates": sorted(covered_dates),
                "target_dates": sorted(target_dates),
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def _read_prompt_sidecar(meta_path: Path) -> dict | None:
    """Read a prompt-scope manifest, or None if it is absent/unreadable."""
    if not meta_path.exists():
        return None
    try:
        data = json.loads(meta_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    return data if isinstance(data, dict) else None


# Archive file stems are "{board_code}_{YYYY}{a|b}", e.g. "CA_MD_2024a".
# The board code itself has an underscore, so match the chunk suffix and
# strip it off the end.
_ARCHIVE_CHUNK_SUFFIX_RE = re.compile(r"_(\d{4})([a-z])$")


def _board_code_from_stem(stem: str) -> str:
    """Recover the board code from an archive file stem.

    'CA_MD_2024a' -> 'CA_MD'. A stem with no chunk suffix is returned as-is
    (so a plain board code still resolves).
    """
    return _ARCHIVE_CHUNK_SUFFIX_RE.sub("", stem)


async def prepare_board_bundle(board_code: str) -> Path | None:
    """Prepare a rollup summary prompt file for a single board.

    Queries the database for all meetings with extracted text in the last 12
    months, builds the prompt, and writes it to
    data/reports/{board_code}_prompt.md plus a {board_code}_prompt.meta.json
    scope manifest.

    Context-not-target: window meetings that already have a stored summary
    (summarized_at IS NOT NULL) are passed to the prompt as CONTEXT ONLY —
    their stored Meeting.summary grounds the rollup, but they are not asked
    to be re-emitted as MEETING blocks. Only unsummarized, text-bearing
    window meetings are TARGETS. This keeps write-once backfilled summaries
    from being re-prompted every refresh.

    Returns the path to the prompt file, or None if no data available.
    """
    await db.init_db()

    cutoff = date.today() - timedelta(days=WINDOW_DAYS)

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

    # Build prompt input. An already-summarized meeting renders as CONTEXT
    # (its stored summary); an unsummarized text-bearing meeting is a TARGET
    # (full doc text). covered_dates = every window date the prompt saw;
    # target_dates = the ones we ask the model to emit new blocks for.
    has_target_text = False
    meetings_data = []
    covered_dates: list[str] = []
    target_dates: list[str] = []
    for m in meetings:
        date_str = m.meeting_date.isoformat()
        text_docs_here = [d for d in m.documents if d.content_text]
        already = m.summarized_at is not None

        if already:
            # Context only: pass the stored summary, no raw doc text.
            meetings_data.append({
                "meeting_date": date_str,
                "title": m.title,
                "already_summarized": True,
                "stored_summary": m.summary or "",
                "documents": [],
            })
            covered_dates.append(date_str)
            continue

        docs_data = [{
            "doc_type": doc.doc_type,
            "filename": doc.filename,
            "content_text": doc.content_text,
        } for doc in m.documents]
        meetings_data.append({
            "meeting_date": date_str,
            "title": m.title,
            "documents": docs_data,
        })
        covered_dates.append(date_str)
        if text_docs_here:
            has_target_text = True
            target_dates.append(date_str)

    if not has_target_text:
        # Every text-bearing window meeting is already summarized (or none
        # carry text). Nothing new to prompt for.
        print(f"No unsummarized text meetings for {board_code}. "
              "Rollup is already current (or no extracted text).")
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
    _write_prompt_sidecar(
        REPORTS_DIR / f"{board_code}_prompt.meta.json",
        mode="rollup",
        covered_dates=covered_dates,
        target_dates=target_dates,
    )

    meeting_count = len(meetings_data)
    context_count = sum(1 for m in meetings_data if m.get("already_summarized"))
    print(f"  {board_code}: {meeting_count} window meetings "
          f"({len(target_dates)} target, {context_count} context-only) "
          f"-> {prompt_path.name}")

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


async def prepare_archive_bundles(board_code: str | None = None) -> list[Path]:
    """Prepare ARCHIVE summary prompts for meetings older than the window.

    For each board, gathers every text-bearing meeting with summarized_at IS
    NULL whose date is older than the rolling 12-month window, groups them by
    calendar year, and writes one prompt per year — split into
    {code}_{YYYY}a / {code}_{YYYY}b / ... chunks when a single year's text
    would blow the MAX_PROMPT_CHARS budget. Each prompt gets a matching
    {code}_{YYYY}{x}_prompt.meta.json sidecar (mode='archive').

    Files land in data/reports/archive/ so the rollup *_summary.md glob and
    the national synthesis never sweep them up.

    Returns the list of prompt file paths written.
    """
    from app.extractor.prompts import MAX_PROMPT_CHARS

    await db.init_db()
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    cutoff = date.today() - timedelta(days=WINDOW_DAYS)

    async with db.async_session() as session:
        board_q = select(Board).order_by(Board.state, Board.code)
        if board_code:
            board_q = select(Board).where(Board.code == board_code)
        boards = (await session.execute(board_q)).scalars().all()

    if not boards:
        print("No boards found." if not board_code
              else f"Board {board_code} not found.")
        return []

    written: list[Path] = []
    for board in boards:
        async with db.async_session() as session:
            meetings = (await session.execute(
                select(Meeting)
                .where(Meeting.board_id == board.id)
                .where(Meeting.meeting_date < cutoff)
                .where(Meeting.summarized_at.is_(None))
                .options(selectinload(Meeting.documents))
                .order_by(Meeting.meeting_date.desc())
            )).scalars().all()

        # Keep only text-bearing meetings; build per-year prompt input.
        by_year: dict[str, list[dict]] = {}
        for m in meetings:
            docs = [{
                "doc_type": d.doc_type,
                "filename": d.filename,
                "content_text": d.content_text,
            } for d in m.documents if d.content_text]
            if not docs:
                continue
            year = m.meeting_date.isoformat()[:4]
            by_year.setdefault(year, []).append({
                "meeting_date": m.meeting_date.isoformat(),
                "title": m.title,
                "documents": docs,
            })

        if not by_year:
            continue

        for year in sorted(by_year, reverse=True):
            year_meetings = by_year[year]
            # Split this year into budget-sized chunks. Chunking mirrors the
            # prompt builder's own per-section budget accounting so a chunk's
            # covered_dates exactly matches what the prompt actually includes.
            chunks = _chunk_by_budget(year_meetings, MAX_PROMPT_CHARS)
            for idx, chunk in enumerate(chunks):
                suffix = chr(ord("a") + idx)
                stem = f"{board.code}_{year}{suffix}"
                prompt = archive_bundle_prompt(
                    board_name=board.name,
                    state=board.state,
                    board_code=board.code,
                    year=year,
                    meetings=chunk,
                    minutes_url=board.minutes_url or "",
                )
                prompt_path = ARCHIVE_DIR / f"{stem}_prompt.md"
                prompt_path.write_text(prompt, encoding="utf-8")
                covered = [m["meeting_date"] for m in chunk]
                _write_prompt_sidecar(
                    ARCHIVE_DIR / f"{stem}_prompt.meta.json",
                    mode="archive",
                    covered_dates=covered,
                    target_dates=covered,  # every archive meeting is a target
                )
                written.append(prompt_path)
                print(f"  {stem}: {len(chunk)} meeting(s) -> {prompt_path.name}")

    print(f"\nPrepared {len(written)} archive prompt file(s) in "
          f"{ARCHIVE_DIR}.")
    return written


def _chunk_by_budget(
    meetings: list[dict], budget: int,
) -> list[list[dict]]:
    """Split meetings into chunks whose rendered doc text fits the budget.

    Uses the same per-section size estimate the prompt builders use (doc
    text is capped at MAX_DOC_CHARS per document), so a chunk's covered_dates
    line up with what the prompt actually renders. A single meeting that on
    its own exceeds the budget still gets its own chunk (never dropped).
    """
    from app.extractor.prompts import MAX_DOC_CHARS

    def _meeting_size(m: dict) -> int:
        total = len(m.get("meeting_date", "")) + len(m.get("title") or "")
        for d in m.get("documents", []):
            t = d.get("content_text") or ""
            total += min(len(t), MAX_DOC_CHARS) + len(d.get("filename") or "")
        return total

    chunks: list[list[dict]] = []
    current: list[dict] = []
    running = 0
    for m in meetings:
        size = _meeting_size(m)
        if current and running + size > budget:
            chunks.append(current)
            current = []
            running = 0
        current.append(m)
        running += size
    if current:
        chunks.append(current)
    return chunks


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


async def ingest_board_summary(
    board_code: str, *, force: bool = False, prune: bool = False,
) -> bool:
    """Read a completed rollup summary file, gate it, and store it.

    The file is normalized (BOM/fence/whitespace repairs) and run through
    app.quality.gates.check_summary (mode='rollup') against the board's
    12-month text dates and source text. On rejection the errors are written
    to data/reports/{code}_summary.errors.txt (one "CODE: message" line each)
    for the retry agent, and NOTHING is written to the database.

    Non-destructive by design (the 36-month history redesign):

      * The rollup goes on Board.summary; each "=== MEETING: date ===" block
        goes on ITS OWN meeting's summary/topics, matched against ALL of the
        board's meeting dates (no 365-day cutoff for matching — a block for
        an out-of-window archive date still lands on its meeting).
      * Per-meeting summaries are WRITE-ONCE: a meeting that already has a
        stored summary (summarized_at IS NOT NULL) is NEVER overwritten,
        even if a new file re-emits a block for it. This protects backfilled
        archive summaries from being clobbered by a later rollup pass.
      * NEVER clears by default. A window meeting absent from the file keeps
        whatever summary it already had.
      * prune=True clears summary/topics ONLY for dates that were in the
        prompt's covered_dates sidecar AND are absent from the file (a
        meeting the prompt SAW as a target but the model chose to drop). If
        the sidecar is missing, prune is a no-op with a warning — we refuse
        to guess the covered set from a live-recomputed window.

    Legacy files (no sections) set only the board rollup, and only with
    force=True (which skips the gate).

    Returns True if successful.
    """
    await db.init_db()

    # Archive files carry a sidecar with mode='archive'. If asked to ingest
    # a file whose sidecar says archive, delegate to the archive path.
    meta = _read_prompt_sidecar(REPORTS_DIR / f"{board_code}_prompt.meta.json")
    if meta and meta.get("mode") == "archive":
        return await ingest_archive_summary(board_code, force=force)

    summary_path = REPORTS_DIR / f"{board_code}_summary.md"
    errors_path = REPORTS_DIR / f"{board_code}_summary.errors.txt"
    if not summary_path.exists():
        print(f"No summary file found at {summary_path}")
        return False

    summary_text = normalize_summary(summary_path.read_text(encoding="utf-8"))
    if not summary_text:
        print(f"Summary file is empty: {summary_path}")
        return False

    cutoff = date.today() - timedelta(days=WINDOW_DAYS)

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

    # prune scope comes from the prompt sidecar, never a live window guess.
    prune_dates: set[str] = set()
    if prune:
        if meta and isinstance(meta.get("covered_dates"), list):
            prune_dates = set(meta["covered_dates"]) - set(sections)
        else:
            print(f"  WARNING: prune=True but no covered_dates sidecar for "
                  f"{board_code} — skipping prune (nothing cleared).")

    now = datetime.now(timezone.utc)

    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()

        if not board:
            print(f"Board {board_code} not found.")
            return False

        # Board-level 12-month rollup (always refreshed by a rollup file).
        board.summary = rollup
        board.summarized_at = now

        # Match blocks against ALL of the board's meetings — an archive-era
        # block still lands on its own meeting, not just window meetings.
        meetings = (await session.execute(
            select(Meeting).where(Meeting.board_id == board.id)
        )).scalars().all()

        matched = 0
        skipped_write_once = 0
        pruned = 0
        for meeting in meetings:
            key = meeting.meeting_date.isoformat()
            if key in sections:
                # Write-once: never overwrite an existing stored summary.
                if meeting.summarized_at is not None:
                    skipped_write_once += 1
                    continue
                section_md, section_topics = sections[key]
                meeting.summary = section_md
                meeting.topics = section_topics or None
                meeting.summarized_at = now
                matched += 1
            elif prune and key in prune_dates:
                # Only prune dates the prompt covered but the file dropped.
                meeting.summary = None
                meeting.topics = None
                meeting.summarized_at = None
                pruned += 1

        ghosts = sorted(set(sections) - {m.meeting_date.isoformat()
                                         for m in meetings})
        await session.commit()

    ghost_str = f", ghost_dates={ghosts}" if ghosts else ""
    write_once_str = (f", write-once-skipped={skipped_write_once}"
                      if skipped_write_once else "")
    prune_str = f", pruned={pruned}" if pruned else ""
    print(f"  Ingested {board_code}: rollup={len(rollup)} chars, "
          f"matched {matched} new block(s)"
          f"{write_once_str}{prune_str}"
          f"{', LEGACY format' if legacy else ''}{ghost_str}")
    return True


async def ingest_archive_summary(stem: str, *, force: bool = False) -> bool:
    """Ingest an ARCHIVE summary file (per-meeting blocks, no rollup).

    ``stem`` is the archive file stem, e.g. ``CA_MD_2024a`` (the board code
    plus a ``_{YYYY}{a,b}`` chunk suffix). The file lives at
    data/reports/archive/{stem}_summary.md with a
    data/reports/archive/{stem}_prompt.meta.json sidecar (mode='archive',
    covered_dates=[...]).

    Archive ingest:
      * NEVER touches Board.summary or Board.summarized_at — the rollup is
        the window's concern; archive files only fill in old meeting blocks.
      * Writes each block onto its OWN meeting, WRITE-ONCE (a meeting that
        already has a stored summary is left alone).
      * Runs check_summary(mode='archive') against the sidecar covered_dates.
        Never clears anything.

    Returns True if successful.
    """
    await db.init_db()

    board_code = _board_code_from_stem(stem)

    summary_path = ARCHIVE_DIR / f"{stem}_summary.md"
    errors_path = ARCHIVE_DIR / f"{stem}_summary.errors.txt"
    meta_path = ARCHIVE_DIR / f"{stem}_prompt.meta.json"
    if not summary_path.exists():
        print(f"No archive summary file found at {summary_path}")
        return False

    summary_text = normalize_summary(summary_path.read_text(encoding="utf-8"))
    if not summary_text:
        print(f"Archive summary file is empty: {summary_path}")
        return False

    meta = _read_prompt_sidecar(meta_path)
    covered = set(meta.get("covered_dates", [])) if meta else set()

    async with db.async_session() as session:
        gate_board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()
        if not gate_board:
            print(f"Board {board_code} not found (from stem '{stem}').")
            return False

        # Source text for the covered dates (for the gate's name/refusal
        # checks). Pull all of the board's meetings so out-of-window archive
        # dates are covered.
        board_meetings = (await session.execute(
            select(Meeting)
            .where(Meeting.board_id == gate_board.id)
            .options(selectinload(Meeting.documents))
        )).scalars().all()

    source_texts: dict[str, list[str]] = {}
    all_dates: set[str] = set()
    for m in board_meetings:
        key = m.meeting_date.isoformat()
        all_dates.add(key)
        texts = [d.content_text for d in m.documents if d.content_text]
        if texts:
            source_texts.setdefault(key, []).extend(texts)

    if force:
        print(f"  WARNING: force=True — SKIPPING the archive ingest gate "
              f"for {stem}.")
    else:
        result = check_summary(
            board_code,
            summary_text,
            state=gate_board.state,
            # In archive mode db_text_dates == the sidecar covered dates.
            db_text_dates=covered,
            db_all_dates=all_dates,
            source_texts_by_date={k: "\n\n".join(v)
                                  for k, v in source_texts.items()},
            minutes_url=gate_board.minutes_url,
            homepage=gate_board.homepage,
            mode="archive",
        )
        if not result.ok:
            errors_path.write_text(
                "\n".join(f"{e.code}: {e.message}" for e in result.errors)
                + "\n", encoding="utf-8")
            print(f"  REJECTED archive {stem}: {len(result.errors)} errors "
                  f"-> {errors_path}")
            return False

    errors_path.unlink(missing_ok=True)

    _board_topics, _rollup, sections = parse_board_summary_file(summary_text)

    now = datetime.now(timezone.utc)

    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()
        if not board:
            print(f"Board {board_code} not found.")
            return False

        meetings = (await session.execute(
            select(Meeting).where(Meeting.board_id == board.id)
        )).scalars().all()

        matched = 0
        skipped_write_once = 0
        for meeting in meetings:
            key = meeting.meeting_date.isoformat()
            if key in sections:
                if meeting.summarized_at is not None:
                    skipped_write_once += 1
                    continue
                section_md, section_topics = sections[key]
                meeting.summary = section_md
                meeting.topics = section_topics or None
                meeting.summarized_at = now
                matched += 1
        # Board.summary / summarized_at deliberately UNTOUCHED.

        ghosts = sorted(set(sections) - {m.meeting_date.isoformat()
                                         for m in meetings})
        await session.commit()

    ghost_str = f", ghost_dates={ghosts}" if ghosts else ""
    write_once_str = (f", write-once-skipped={skipped_write_once}"
                      if skipped_write_once else "")
    print(f"  Ingested archive {stem}: matched {matched} new block(s)"
          f"{write_once_str}{ghost_str} (Board.summary untouched)")
    return True


async def ingest_all_summaries(
    *, force: bool = False, prune: bool = False,
) -> tuple[int, list[str]]:
    """Scan data/reports/ (and archive/) for *_summary.md and ingest them.

    Rollup files in data/reports/ ingest via ingest_board_summary(); archive
    files in data/reports/archive/ ingest via ingest_archive_summary(). The
    force/prune flags apply to the rollup files (archive ingest never clears,
    so prune is meaningless there and is ignored).

    Returns (ingested_count, rejected_stems). A file lands in the rejected
    list when it fails the ingest gate (see its *_summary.errors.txt) or
    can't be ingested at all (missing board, etc.).
    """
    await db.init_db()

    summary_files = sorted(REPORTS_DIR.glob("*_summary.md"))
    # Resolve the archive dir from the current REPORTS_DIR (not the frozen
    # module constant) so tests that repoint REPORTS_DIR stay isolated.
    archive_files = sorted((REPORTS_DIR / "archive").glob("*_summary.md"))
    if not summary_files and not archive_files:
        print("No summary files found in data/reports/ or archive/")
        return 0, []

    print(f"Found {len(summary_files)} rollup + {len(archive_files)} archive "
          "summary files to ingest.\n")
    ingested = 0
    rejected: list[str] = []

    for path in summary_files:
        # Extract board_code from filename: CA_MD_summary.md -> CA_MD
        board_code = path.stem.replace("_summary", "")
        if await ingest_board_summary(board_code, force=force, prune=prune):
            ingested += 1
        else:
            rejected.append(board_code)

    for path in archive_files:
        # Extract stem: CA_MD_2024a_summary.md -> CA_MD_2024a
        stem = path.stem.replace("_summary", "")
        if await ingest_archive_summary(stem, force=force):
            ingested += 1
        else:
            rejected.append(stem)

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
