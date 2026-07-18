"""Prepare data bundles for structured-facts extraction and ingest results.

This module is the facts-v1 sibling of app.extractor.summarizer: it prepares
prompt bundle files that external Claude Code subagents consume, then ingests
their JSON output back into the four typed fact tables. It never calls an LLM.

Flow:
    1. prepare_facts_bundles() — query DB for meetings that have text but no
       facts yet, chunk them (newest-first, on meeting boundaries) into
       data/reports/facts/{code}_{NN}_facts_prompt.md via
       fact_prompts.fact_extraction_prompt, plus a .meta.json sidecar.
    2. (external) a Claude Code subagent reads a prompt, writes the sibling
       data/reports/facts/{code}_{NN}_facts.json.
    3. ingest_facts_file() — gate the JSON via app.quality.gates.check_facts
       against the DB-derived inputs, then (on pass) write the facts in ONE
       transaction: an extraction_runs provenance row, the four fact tables,
       and meetings.facts_extracted_at for every covered meeting.
    4. ingest_all_facts() — scan data/reports/facts/*_facts.json, ingest each.
    5. facts_status() — per-board coverage of text-meetings vs facts-extracted.

Ingest is deliberately SYNCHRONOUS (sqlite3): the whole write is one
transaction, the F5 confidence mutation lives on the dict check_facts()
returns via, and a single connection keeps the DELETE+INSERT atomic without
async-session bookkeeping.
"""
import hashlib
import json
import sqlite3
from datetime import date, datetime, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import selectinload

import app.database as db
from app.config import DB_PATH, REPORTS_DIR
from app.extractor.fact_prompts import (
    FACTS_MAX_PROMPT_CHARS, fact_extraction_prompt, render_meeting_section,
)
from app.models import Board, Meeting
from app.quality.gates import check_facts, normalize_summary
from app.quality.taxonomy import PROMPT_VERSION

# All facts prompt/output files live in their own subdirectory so the summary
# pipeline's *_prompt.md / *_summary.md globs never collide with them.
FACTS_DIR = REPORTS_DIR / "facts"


def _facts_dir() -> Path:
    FACTS_DIR.mkdir(parents=True, exist_ok=True)
    return FACTS_DIR


# ===========================================================================
# 1. PREPARE — async, mirrors summarizer.prepare_board_bundle
# ===========================================================================

async def _board_meetings_needing_facts(
    session, board: Board, *, force: bool,
) -> list[Meeting]:
    """Text-bearing meetings for one board that still need facts.

    A meeting qualifies when it has >=1 document with extracted text AND its
    facts_extracted_at is NULL. With force=True the column is cleared for the
    board first, so every text-bearing meeting re-qualifies.

    Unlike the 12-month summary window, facts cover ALL history: facts are a
    permanent record (emerging_topics keep the earliest date), so re-scoping
    to a rolling window would silently drop older meetings from extraction.
    """
    if force:
        for m in (await session.execute(
            select(Meeting).where(Meeting.board_id == board.id)
        )).scalars().all():
            m.facts_extracted_at = None
        await session.commit()

    meetings = (await session.execute(
        select(Meeting)
        .where(Meeting.board_id == board.id)
        .where(Meeting.facts_extracted_at.is_(None))
        .options(selectinload(Meeting.documents))
        .order_by(Meeting.meeting_date.desc())
    )).scalars().all()

    needing: list[Meeting] = []
    for m in meetings:
        if any(d.content_text for d in m.documents):
            needing.append(m)
    return needing


def _meeting_payload(meeting: Meeting) -> dict:
    """Shape one ORM meeting into the dict fact_prompts expects."""
    return {
        "meeting_date": meeting.meeting_date.isoformat(),
        "title": meeting.title,
        "documents": [
            {
                "doc_type": d.doc_type,
                "filename": d.filename,
                "content_text": d.content_text,
            }
            for d in meeting.documents
            if d.content_text
        ],
    }


def _chunk_meetings(payloads: list[dict]) -> list[list[dict]]:
    """Split newest-first meetings into chunks under FACTS_MAX_PROMPT_CHARS.

    Chunks break only on meeting boundaries. A single meeting whose rendered
    section already exceeds the budget still gets its own chunk (never split
    mid-meeting) — fact_prompts.slice_doc_text has already bounded each doc.
    """
    chunks: list[list[dict]] = []
    current: list[dict] = []
    running = 0
    for payload in payloads:
        section_len = len(render_meeting_section(payload))
        if current and running + section_len > FACTS_MAX_PROMPT_CHARS:
            chunks.append(current)
            current = []
            running = 0
        current.append(payload)
        running += section_len
    if current:
        chunks.append(current)
    return chunks


async def prepare_facts_bundles(
    board_code: str | None = None, *, force: bool = False,
) -> list[Path]:
    """Write facts-extraction prompt chunks for boards that need them.

    Selects meetings with >=1 text-bearing document and facts_extracted_at IS
    NULL (force clears facts_extracted_at in scope first), chunks them
    newest-first on meeting boundaries, and writes each chunk to
    data/reports/facts/{code}_{NN}_facts_prompt.md with a sibling
    {code}_{NN}_facts_prompt.meta.json sidecar {covered_dates, budget_chars}.

    Returns the list of prompt files written.
    """
    await db.init_db()
    out_dir = _facts_dir()

    async with db.async_session() as session:
        if board_code:
            boards = (await session.execute(
                select(Board).where(Board.code == board_code)
            )).scalars().all()
            if not boards:
                print(f"Board {board_code} not found.")
                return []
        else:
            boards = (await session.execute(
                select(Board).order_by(Board.state, Board.code)
            )).scalars().all()

        written: list[Path] = []
        board_chunk_counts: list[tuple[str, int, int]] = []

        for board in boards:
            needing = await _board_meetings_needing_facts(
                session, board, force=force)
            if not needing:
                continue

            payloads = [_meeting_payload(m) for m in needing]
            chunks = _chunk_meetings(payloads)
            total_chunks = len(chunks)

            for idx, chunk in enumerate(chunks, start=1):
                nn = f"{idx:02d}"
                prompt_path = out_dir / f"{board.code}_{nn}_facts_prompt.md"
                out_json = f"{board.code}_{nn}_facts.json"
                chunk_note = (
                    f"**Chunk {idx} of {total_chunks}** for this board. Write "
                    f"your output ONLY as JSON to `data/reports/facts/"
                    f"{out_json}` (nothing else). Cover EXACTLY the meetings "
                    "listed below — no more, no fewer.")

                prompt = fact_extraction_prompt(
                    board={"name": board.name, "state": board.state,
                           "code": board.code},
                    meetings_payload=chunk,
                    chunk_note=chunk_note,
                )
                prompt_path.write_text(prompt, encoding="utf-8")

                covered = [m["meeting_date"] for m in chunk]
                meta = {
                    "board_code": board.code,
                    "chunk": idx,
                    "total_chunks": total_chunks,
                    "covered_dates": covered,
                    "budget_chars": FACTS_MAX_PROMPT_CHARS,
                    "prompt_chars": len(prompt),
                    "output_file": out_json,
                }
                (out_dir / f"{board.code}_{nn}_facts_prompt.meta.json"
                 ).write_text(json.dumps(meta, indent=2), encoding="utf-8")

                written.append(prompt_path)

            board_chunk_counts.append(
                (board.code, len(needing), total_chunks))

    # Report
    if not board_chunk_counts:
        scope = f" for {board_code}" if board_code else ""
        print(f"No meetings need facts extraction{scope} "
              "(all text-bearing meetings already have facts_extracted_at).")
        return []

    print(f"Prepared facts prompts in {out_dir}:\n")
    for code, n_mtgs, n_chunks in board_chunk_counts:
        print(f"  {code}: {n_mtgs} meeting(s) -> {n_chunks} chunk(s)")
    print(f"\n{len(written)} prompt file(s) across "
          f"{len(board_chunk_counts)} board(s).")
    print("\nDispatch: for each *_facts_prompt.md, run a Claude Code subagent "
          "that reads the prompt and writes the sibling *_facts.json listed "
          "in its chunk note. Then ingest with the `facts --ingest` command.")
    return written


# ===========================================================================
# INGEST helpers — sync sqlite3
# ===========================================================================

def _connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    return con


def _canonical_hash(*parts) -> str:
    """sha256 over pipe-joined canonical fields (UNIQUE fact identity)."""
    canon = "|".join(" ".join(str(p or "").split()).lower() for p in parts)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def _gate_inputs_for_board(
    con: sqlite3.Connection, board_code: str,
) -> dict | None:
    """DB-side check_facts() inputs for one board.

    Facts cover all history (no rolling window): db_text_dates and
    source_texts_by_date span every text-bearing meeting the board has.
    Returns None when the board is missing from the DB.
    """
    row = con.execute(
        "SELECT id, state FROM boards WHERE code = ?", (board_code,)
    ).fetchone()
    if row is None:
        return None
    board_id = row[0]

    texts: dict[str, list[str]] = {}
    for d, t in con.execute(
        """SELECT m.meeting_date, d.content_text
           FROM meetings m
           JOIN meeting_documents d ON d.meeting_id = m.id
           WHERE m.board_id = ?
             AND d.content_text IS NOT NULL AND d.content_text != ''""",
        (board_id,),
    ):
        texts.setdefault(d[:10], []).append(t)

    return {
        "board_id": board_id,
        "db_text_dates": set(texts),
        "source_texts_by_date": {
            k: "\n\n".join(v) for k, v in texts.items()},
    }


def _meeting_id_by_date(
    con: sqlite3.Connection, board_id: int,
) -> dict[str, int]:
    """iso-date -> meeting_id for a board (first meeting on each date wins)."""
    out: dict[str, int] = {}
    for mid, d in con.execute(
        "SELECT id, meeting_date FROM meetings WHERE board_id = ? "
        "ORDER BY id",
        (board_id,),
    ):
        out.setdefault(d[:10], mid)
    return out


def _documents_by_filename(
    con: sqlite3.Connection, meeting_id: int,
) -> dict[str, int]:
    """filename -> document_id for one meeting."""
    return {
        fn: did
        for did, fn in con.execute(
            "SELECT id, filename FROM meeting_documents WHERE meeting_id = ?",
            (meeting_id,),
        )
    }


# ===========================================================================
# 2. INGEST ONE FILE — sync sqlite3, single transaction
# ===========================================================================

def ingest_facts_file(path, *, force: bool = False, dry_run: bool = False) -> bool:
    """Gate one *_facts.json and, on pass, write it in one transaction.

    ``dry_run=True`` runs the gate only and returns whether the file WOULD
    ingest, writing nothing to the database (used by ``facts --validate``).

    Steps:
      * board_code comes from the filename ({code}_{NN}_facts.json).
      * covered_dates come from the {code}_{NN}_facts_prompt.meta.json
        sidecar (falls back to the meeting dates found in the JSON itself).
      * check_facts() runs against the board's text-bearing dates and per-date
        source text. Pass the parsed DICT so its F5 confidence downgrade
        sticks. On failure: write {path}.errors.txt, record a failed
        extraction_runs row, write NO facts, return False.
      * On pass, in ONE transaction: insert the extraction_runs row (status
        'ingested') first; per meeting DELETE existing policy/legislation/
        disciplinary rows then INSERT fresh (fact_hash = sha256 of canonical
        fields); UPSERT emerging_topics on (board_id, topic_slug) keeping the
        earliest first_mentioned_on; set meetings.facts_extracted_at for every
        covered meeting (even zero-fact ones); update the run's counts.

    Returns True on a successful ingest.
    """
    path = Path(path)
    errors_path = Path(str(path) + ".errors.txt")

    if not path.exists():
        print(f"No facts file found at {path}")
        return False

    board_code = path.stem.replace("_facts", "")
    # strip the _NN chunk suffix if present -> board code
    if "_" in board_code:
        parts = board_code.split("_")
        if parts[-1].isdigit():
            board_code = "_".join(parts[:-1])

    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(normalize_summary(raw))
    except json.JSONDecodeError as exc:
        # Let the gate produce the retry-agent message for consistency, but
        # short-circuit here if we can't even parse enough to know the board.
        data = normalize_summary(raw)  # gate re-parses str and reports BAD_JSON
        _ = exc

    # covered_dates: sidecar first, then fall back to the JSON's own dates.
    covered_dates = _covered_dates_from_sidecar(path)
    if covered_dates is None:
        covered_dates = _covered_dates_from_data(data)

    con = _connect()
    try:
        inputs = _gate_inputs_for_board(con, board_code)
        if inputs is None:
            msg = (f"Board {board_code} not found in the database — cannot "
                   "resolve meetings for this facts file.")
            errors_path.write_text(f"NO_BOARD: {msg}\n", encoding="utf-8")
            _record_failed_run(con, None, board_code, str(path),
                               f"NO_BOARD: {msg}")
            con.commit()
            print(f"  REJECTED {path.name}: board not found -> {errors_path}")
            return False

        board_id = inputs["board_id"]

        if force:
            print(f"  WARNING: force=True — SKIPPING the facts gate for "
                  f"{path.name}. Unvalidated fact content is being written.")
            result = None
        else:
            result = check_facts(
                board_code,
                data,  # dict -> F5 confidence downgrade mutates in place
                covered_dates=covered_dates,
                db_text_dates=inputs["db_text_dates"],
                source_texts_by_date=inputs["source_texts_by_date"],
            )
            if not result.ok:
                if dry_run:
                    print(f"  WOULD REJECT {board_code} ({path.name}): "
                          f"{len(result.errors)} errors")
                    return False
                errors_path.write_text(
                    "\n".join(f"{e.code}: {e.message}"
                              for e in result.errors) + "\n",
                    encoding="utf-8")
                _record_failed_run(
                    con, board_id, board_code, str(path),
                    "\n".join(f"{e.code}: {e.message}"
                              for e in result.errors))
                con.commit()
                print(f"  REJECTED {board_code} ({path.name}): "
                      f"{len(result.errors)} errors -> {errors_path}")
                return False

        if dry_run:
            print(f"  OK {board_code} ({path.name}): would ingest.")
            return True

        # data must be a dict past the gate; if force skipped the gate and it
        # isn't, we cannot ingest.
        if not isinstance(data, dict):
            msg = ("File is not a JSON object; cannot ingest even with "
                   "force=True.")
            errors_path.write_text(f"BAD_JSON: {msg}\n", encoding="utf-8")
            _record_failed_run(con, board_id, board_code, str(path),
                               f"BAD_JSON: {msg}")
            con.commit()
            print(f"  REJECTED {board_code} ({path.name}): {msg}")
            return False

        inserted = _write_facts(
            con, board_id, board_code, str(path), data, covered_dates)
        con.commit()

        errors_path.unlink(missing_ok=True)  # clear any stale rejection
        warn_n = len(result.warnings) if result else 0
        print(f"  Ingested {board_code} ({path.name}): "
              f"{inserted} fact(s) across {len(covered_dates)} meeting(s)"
              f"{f', {warn_n} warning(s)' if warn_n else ''}.")
        return True
    finally:
        con.close()


def _covered_dates_from_sidecar(facts_path: Path) -> set[str] | None:
    """Read covered_dates from the {code}_{NN}_facts_prompt.meta.json sidecar."""
    stem = facts_path.stem.replace("_facts", "_facts_prompt")
    meta_path = facts_path.with_name(stem + ".meta.json")
    if not meta_path.exists():
        return None
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    dates = meta.get("covered_dates")
    if isinstance(dates, list):
        return {str(d) for d in dates}
    return None


def _covered_dates_from_data(data) -> set[str]:
    """Fallback: the meeting_date values present in the JSON itself."""
    if not isinstance(data, dict):
        return set()
    out: set[str] = set()
    for m in data.get("meetings", []) or []:
        if isinstance(m, dict) and isinstance(m.get("meeting_date"), str):
            out.add(m["meeting_date"])
    return out


def _record_failed_run(
    con: sqlite3.Connection, board_id, board_code: str,
    source_file: str, error: str,
) -> None:
    """Insert a status='failed' extraction_runs row (no fact writes)."""
    con.execute(
        """INSERT INTO extraction_runs
           (board_id, model, prompt_version, source_file, meetings_covered,
            facts_inserted, status, error, created_at)
           VALUES (?, ?, ?, ?, 0, 0, 'failed', ?, ?)""",
        (board_id, None, PROMPT_VERSION, source_file, error,
         datetime.now(timezone.utc).isoformat()),
    )


def _write_facts(
    con: sqlite3.Connection, board_id: int, board_code: str,
    source_file: str, data: dict, covered_dates: set[str],
) -> int:
    """Write all facts from a passed file in the caller's open transaction.

    Returns the number of fact rows inserted (excludes emerging upserts that
    only refreshed an earlier date).
    """
    meetings = data.get("meetings", []) or []
    json_dates = sorted(
        m["meeting_date"] for m in meetings
        if isinstance(m, dict) and isinstance(m.get("meeting_date"), str))
    window_start = json_dates[0] if json_dates else None
    window_end = json_dates[-1] if json_dates else None

    now = datetime.now(timezone.utc).isoformat()

    # provenance row FIRST so every fact can carry its run_id
    cur = con.execute(
        """INSERT INTO extraction_runs
           (board_id, model, prompt_version, source_file, window_start,
            window_end, meetings_covered, facts_inserted, status, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, 0, 'ingested', ?)""",
        (board_id, data.get("model"), data.get("schema_version",
         PROMPT_VERSION), source_file, window_start, window_end,
         len(covered_dates), now),
    )
    run_id = cur.lastrowid

    mid_by_date = _meeting_id_by_date(con, board_id)
    inserted = 0

    def _resolve_doc(meeting_id: int, source_document, docs_cache) -> int | None:
        if not source_document:
            return None
        by_fn = docs_cache.setdefault(
            meeting_id, _documents_by_filename(con, meeting_id))
        did = by_fn.get(source_document)
        if did is None:
            print(f"    WARN: source_document '{source_document}' does not "
                  f"resolve to a document on meeting {meeting_id} "
                  f"({board_code}); storing document_id=NULL.")
        return did

    docs_cache: dict[int, dict[str, int]] = {}

    for mrec in meetings:
        if not isinstance(mrec, dict):
            continue
        d = mrec.get("meeting_date")
        meeting_id = mid_by_date.get(d)
        if meeting_id is None:
            # Covered but not resolvable — the gate would have caught a true
            # ghost; this only happens under force=True. Skip its facts.
            print(f"    WARN: meeting {d} not found for {board_code}; "
                  "skipping its facts.")
            continue

        # Replace this meeting's existing policy/legislation/disciplinary rows.
        con.execute("DELETE FROM policy_actions WHERE meeting_id = ?",
                    (meeting_id,))
        con.execute("DELETE FROM legislation_mentions WHERE meeting_id = ?",
                    (meeting_id,))
        con.execute("DELETE FROM disciplinary_actions WHERE meeting_id = ?",
                    (meeting_id,))

        # --- policy_actions ---
        for fact in mrec.get("policy_actions", []) or []:
            fh = _canonical_hash(
                "policy", fact.get("instrument"), fact.get("stage"),
                fact.get("topic"), fact.get("title"), fact.get("action_date"))
            did = _resolve_doc(meeting_id, fact.get("source_document"),
                               docs_cache)
            con.execute(
                """INSERT INTO policy_actions
                   (run_id, meeting_id, document_id, instrument, stage, topic,
                    title, description, rule_reference, action_date, quote,
                    confidence, fact_hash)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (run_id, meeting_id, did, fact.get("instrument"),
                 fact.get("stage"), fact.get("topic"), fact.get("title"),
                 fact.get("description"), fact.get("rule_reference"),
                 fact.get("action_date"), fact.get("quote"),
                 fact.get("confidence"), fh))
            inserted += 1

        # --- legislation ---
        for fact in mrec.get("legislation", []) or []:
            fh = _canonical_hash(
                "legislation", fact.get("bill_number"),
                fact.get("bill_state"))
            did = _resolve_doc(meeting_id, fact.get("source_document"),
                               docs_cache)
            con.execute(
                """INSERT INTO legislation_mentions
                   (run_id, meeting_id, document_id, bill_number, bill_state,
                    subject, topic, involvement, status_note, quote,
                    confidence, fact_hash)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                (run_id, meeting_id, did, fact.get("bill_number"),
                 fact.get("bill_state"), fact.get("subject"),
                 fact.get("topic"), fact.get("involvement"),
                 fact.get("status_note"), fact.get("quote"),
                 fact.get("confidence"), fh))
            inserted += 1

        # --- disciplinary: NOT ingested (Frank's decision 2026-07-18) ---
        # boardpulse tracks boards' topics of interest/concern, not individual
        # disciplinary cases. The DELETE above clears any stray rows; the
        # extraction may still emit a "disciplinary" array (contract unchanged),
        # but it is intentionally dropped here and never stored.

        # --- emerging_topics: UPSERT keeping earliest first_mentioned_on ---
        for fact in mrec.get("emerging_topics", []) or []:
            did = _resolve_doc(meeting_id, fact.get("source_document"),
                               docs_cache)
            slug = fact.get("topic_slug")
            existing = con.execute(
                "SELECT id, first_mentioned_on FROM emerging_topics "
                "WHERE board_id = ? AND topic_slug = ?",
                (board_id, slug)).fetchone()
            if existing is None:
                con.execute(
                    """INSERT INTO emerging_topics
                       (run_id, board_id, meeting_id, document_id, topic_slug,
                        subject, first_mentioned_on, quote, confidence)
                       VALUES (?,?,?,?,?,?,?,?,?)""",
                    (run_id, board_id, meeting_id, did, slug,
                     fact.get("subject"), d, fact.get("quote"),
                     fact.get("confidence")))
                inserted += 1
            elif d < (existing[1] or "")[:10]:
                # Earlier mention found — sharpen the timeline in place.
                con.execute(
                    """UPDATE emerging_topics
                       SET run_id = ?, meeting_id = ?, document_id = ?,
                           subject = ?, first_mentioned_on = ?, quote = ?,
                           confidence = ?
                       WHERE id = ?""",
                    (run_id, meeting_id, did, fact.get("subject"), d,
                     fact.get("quote"), fact.get("confidence"), existing[0]))
                # not counted: refreshed an existing row, not a new fact

    # Mark EVERY covered meeting as extracted — even ones with zero facts.
    for d in sorted(covered_dates):
        meeting_id = mid_by_date.get(d)
        if meeting_id is not None:
            con.execute(
                "UPDATE meetings SET facts_extracted_at = ? WHERE id = ?",
                (now, meeting_id))

    con.execute(
        "UPDATE extraction_runs SET facts_inserted = ? WHERE id = ?",
        (inserted, run_id))
    return inserted


# ===========================================================================
# 3. INGEST ALL — scan data/reports/facts/*_facts.json
# ===========================================================================

def ingest_all_facts() -> tuple[int, list[str]]:
    """Ingest every data/reports/facts/*_facts.json file.

    Returns (ingested_count, rejected_file_names). A file lands in the
    rejected list when it fails the facts gate (see its .errors.txt) or can't
    be ingested (missing board, unparseable JSON, etc.).
    """
    out_dir = _facts_dir()
    facts_files = sorted(out_dir.glob("*_facts.json"))
    if not facts_files:
        print(f"No *_facts.json files found in {out_dir}")
        return 0, []

    print(f"Found {len(facts_files)} facts file(s) to ingest.\n")
    ingested = 0
    rejected: list[str] = []
    for path in facts_files:
        if ingest_facts_file(path):
            ingested += 1
        else:
            rejected.append(path.name)

    rejected_str = f" ({', '.join(rejected)})" if rejected else ""
    print(f"\nFACTS INGEST: {ingested} ok, "
          f"{len(rejected)} rejected{rejected_str}")
    return ingested, rejected


# ===========================================================================
# 4. STATUS — per-board coverage
# ===========================================================================

def facts_status() -> list[dict]:
    """Per-board text-bearing meetings vs facts-extracted, with coverage %.

    Returns one dict per board that has at least one text-bearing meeting,
    and prints a table. Coverage = extracted / text-bearing meetings.
    """
    con = _connect()
    try:
        rows = con.execute(
            """SELECT b.code, b.state,
                      COUNT(DISTINCT CASE
                          WHEN d.content_text IS NOT NULL AND d.content_text != ''
                          THEN m.id END) AS text_mtgs,
                      COUNT(DISTINCT CASE
                          WHEN d.content_text IS NOT NULL AND d.content_text != ''
                               AND m.facts_extracted_at IS NOT NULL
                          THEN m.id END) AS facts_mtgs
               FROM boards b
               JOIN meetings m ON m.board_id = b.id
               LEFT JOIN meeting_documents d ON d.meeting_id = m.id
               GROUP BY b.id
               HAVING text_mtgs > 0
               ORDER BY b.state, b.code""").fetchall()
    finally:
        con.close()

    out: list[dict] = []
    print(f"{'Board':10} {'Text mtgs':>10} {'Facts done':>11} "
          f"{'Coverage':>9}")
    print("-" * 44)
    tot_text = tot_facts = 0
    for code, state, text_mtgs, facts_mtgs in rows:
        pct = (facts_mtgs / text_mtgs * 100) if text_mtgs else 0.0
        tot_text += text_mtgs
        tot_facts += facts_mtgs
        out.append({
            "board_code": code, "state": state,
            "text_meetings": text_mtgs, "facts_extracted": facts_mtgs,
            "coverage_pct": round(pct, 1),
        })
        print(f"{code:10} {text_mtgs:>10} {facts_mtgs:>11} {pct:>8.1f}%")
    print("-" * 44)
    overall = (tot_facts / tot_text * 100) if tot_text else 0.0
    print(f"{'TOTAL':10} {tot_text:>10} {tot_facts:>11} {overall:>8.1f}%")
    return out
