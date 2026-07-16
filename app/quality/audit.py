"""Standing provenance audit — re-verify every stored fact against stored text.

Frank's V2 ruling (docs/plans/2026-07-16-boardpulse-validation-decisions.md):
a monthly re-check that the database still supports itself. For each of the
four fact tables this verifies, per row:

  * the stored quote is STILL a verbatim (whitespace-normalized) substring of
    the meeting's stored document text — the same reference frame the ingest
    gate used, re-checked after the fact so re-extraction, document changes,
    or bugs can't silently break provenance;
  * the row is linked to a document;
  * (disciplinary only, legacy tally rows) whether a count >= 2 is visible in
    its own quote — the gap the itemized facts-v2 contract closes. This
    metric retires as the backfill replaces tally rows with per-case rows.

Output: a scorecard dict, persisted to data/reports/facts_audit.json so the
/ops page and the dashboard artifact can render the latest result. Read-only
against the DB (stdlib sqlite3, mode=ro), same pattern as reports/brief.py.
"""
from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from app.config import REPORTS_DIR
from app.quality.gates import _ws, count_visible

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = PROJECT_ROOT / "boardpulse.db"
AUDIT_PATH = REPORTS_DIR / "facts_audit.json"

FACT_TABLES = ("disciplinary_actions", "policy_actions",
               "legislation_mentions", "emerging_topics")


def _connect_ro(db_path: Optional[Path] = None) -> sqlite3.Connection:
    path = Path(db_path) if db_path else DB_PATH
    con = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


# The bulk-entry visibility rule now lives in gates (the ingest gate
# enforces it for facts-v2); the audit re-checks stored rows with the same
# definition. Kept under the old name for callers/tests.
_count_visible = count_visible


def audit_facts(db_path: Optional[Path] = None,
                write: bool = True) -> dict:
    """Run the provenance audit over all four fact tables.

    Returns the scorecard dict; when ``write`` is True also persists it to
    data/reports/facts_audit.json.
    """
    con = _connect_ro(db_path)
    try:
        cur = con.cursor()
        total_boards = cur.execute(
            "SELECT count(*) FROM boards").fetchone()[0]

        # Meeting-level concatenated text — the gate's reference frame.
        texts: dict[int, str] = {}

        def meeting_text(mid: int) -> str:
            if mid not in texts:
                docs = cur.execute(
                    "SELECT content_text FROM meeting_documents "
                    "WHERE meeting_id = ? AND content_text IS NOT NULL",
                    (mid,)).fetchall()
                texts[mid] = _ws(" ".join(d["content_text"] for d in docs))
            return texts[mid]

        per_table: dict[str, dict] = {}
        for table in FACT_TABLES:
            if table == "emerging_topics":
                # emerging_topics has no meeting-scoped uniqueness issues and
                # anchors on board_id; still joined through meeting_id.
                rows = cur.execute(
                    "SELECT t.id, t.meeting_id, t.document_id, t.quote, "
                    "       b.code AS board_code "
                    "FROM emerging_topics t "
                    "JOIN meetings m ON m.id = t.meeting_id "
                    "JOIN boards b ON b.id = m.board_id").fetchall()
            else:
                rows = cur.execute(
                    f"SELECT t.id, t.meeting_id, t.document_id, t.quote, "
                    f"       b.code AS board_code "
                    f"FROM {table} t "
                    f"JOIN meetings m ON m.id = t.meeting_id "
                    f"JOIN boards b ON b.id = m.board_id").fetchall()

            quoted = verified = doc_linked = 0
            mismatch_ids: list[int] = []
            boards: set[str] = set()
            for r in rows:
                boards.add(r["board_code"])
                if r["document_id"] is not None:
                    doc_linked += 1
                q = _ws(r["quote"])
                if not q:
                    continue
                quoted += 1
                if q in meeting_text(r["meeting_id"]):
                    verified += 1
                else:
                    mismatch_ids.append(r["id"])

            per_table[table] = {
                "rows": len(rows),
                "quoted": quoted,
                "quote_verified": verified,
                "quote_mismatch_ids": mismatch_ids[:50],
                "doc_linked": doc_linked,
                "boards_contributing": len(boards),
            }

        # Disciplinary legacy-tally check: counts >= 2 not visible in quote.
        disc = cur.execute(
            "SELECT id, action_count, quote FROM disciplinary_actions "
            "WHERE action_count >= 2").fetchall()
        unseen = sum(
            1 for r in disc
            if not _count_visible(r["action_count"], _ws(r["quote"]).lower()))
        per_table["disciplinary_actions"]["multi_count_rows"] = len(disc)
        per_table["disciplinary_actions"]["count_not_in_quote"] = unseen
    finally:
        con.close()

    total_rows = sum(t["rows"] for t in per_table.values())
    total_quoted = sum(t["quoted"] for t in per_table.values())
    total_verified = sum(t["quote_verified"] for t in per_table.values())

    scorecard = {
        "generated_at": datetime.now(timezone.utc).isoformat(
            timespec="seconds"),
        "total_boards": total_boards,
        "overall": {
            "rows": total_rows,
            "quoted": total_quoted,
            "quote_verified": total_verified,
            "quote_verified_pct": round(
                100 * total_verified / total_quoted, 1) if total_quoted else None,
        },
        "tables": per_table,
    }

    if write:
        AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
        AUDIT_PATH.write_text(json.dumps(scorecard, indent=2),
                              encoding="utf-8")
    return scorecard


def latest_audit() -> Optional[dict]:
    """The most recent persisted scorecard, or None."""
    if not AUDIT_PATH.exists():
        return None
    try:
        return json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def print_scorecard(scorecard: dict) -> None:
    """ASCII scorecard for the console (cp1252-safe)."""
    o = scorecard["overall"]
    print(f"PROVENANCE AUDIT  {scorecard['generated_at']}")
    print(f"  facts: {o['rows']:,}  quoted: {o['quoted']:,}  "
          f"quote-verified: {o['quote_verified']:,}"
          + (f" ({o['quote_verified_pct']}%)"
             if o["quote_verified_pct"] is not None else ""))
    for table, t in scorecard["tables"].items():
        line = (f"  {table}: rows={t['rows']:,} "
                f"verified={t['quote_verified']:,}/{t['quoted']:,} "
                f"doc-linked={t['doc_linked']:,} "
                f"boards={t['boards_contributing']}/{scorecard['total_boards']}")
        if "multi_count_rows" in t:
            line += (f" | legacy multi-counts={t['multi_count_rows']:,} "
                     f"count-not-in-quote={t['count_not_in_quote']:,}")
        print(line)
        if t["quote_mismatch_ids"]:
            print(f"    MISMATCHED quote row ids: {t['quote_mismatch_ids']}")
