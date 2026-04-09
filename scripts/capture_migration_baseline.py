"""Capture pre-migration baseline counts + checksums.

Writes data/reports/migration_baseline_YYYY-MM-DD.json with row counts for
every table plus SHA-256 checksums of the summary/tldr/topics columns for
a set of canary non-RI boards. Used by the migration script to verify that
non-RI boards are bit-for-bit unchanged after the migration.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import date
from pathlib import Path

BOARDPULSE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BOARDPULSE_DIR / "boardpulse.db"
REPORT_DIR = BOARDPULSE_DIR / "data" / "reports"
RI_BOARD_ID = 48
CANARY_BOARD_CODES = ("FL_MD", "TX_MD", "AK_MD", "GA_MD")


def _canary_checksum(conn: sqlite3.Connection, board_code: str) -> str:
    """SHA-256 of concatenated (meeting_date | summary | tldr | topics) for a board."""
    rows = conn.execute(
        """
        SELECT m.meeting_date, COALESCE(m.summary, ''), COALESCE(m.tldr, ''),
               COALESCE(m.topics, '')
        FROM meetings m
        JOIN boards b ON m.board_id = b.id
        WHERE b.code = ?
        ORDER BY m.id
        """,
        (board_code,),
    ).fetchall()
    h = hashlib.sha256()
    for r in rows:
        h.update("|".join(str(x) for x in r).encode("utf-8"))
    return h.hexdigest()


def main() -> None:
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA busy_timeout = 30000")

    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        raise SystemExit(f"Pre-migration integrity check failed: {integrity}")

    counts = {
        "boards": conn.execute("SELECT COUNT(*) FROM boards").fetchone()[0],
        "meetings_total": conn.execute("SELECT COUNT(*) FROM meetings").fetchone()[0],
        "meetings_ri_md": conn.execute(
            "SELECT COUNT(*) FROM meetings WHERE board_id = ?", (RI_BOARD_ID,)
        ).fetchone()[0],
        "meeting_documents_total": conn.execute(
            "SELECT COUNT(*) FROM meeting_documents"
        ).fetchone()[0],
        "meeting_documents_ri_md": conn.execute(
            """
            SELECT COUNT(*) FROM meeting_documents md
            JOIN meetings m ON md.meeting_id = m.id
            WHERE m.board_id = ?
            """,
            (RI_BOARD_ID,),
        ).fetchone()[0],
        "document_pages": conn.execute("SELECT COUNT(*) FROM document_pages").fetchone()[0],
        "meeting_intelligence": conn.execute(
            "SELECT COUNT(*) FROM meeting_intelligence"
        ).fetchone()[0],
        "board_summaries": conn.execute("SELECT COUNT(*) FROM board_summaries").fetchone()[0],
        "ri_md_meetings_with_summary": conn.execute(
            "SELECT COUNT(*) FROM meetings WHERE board_id = ? AND summary IS NOT NULL",
            (RI_BOARD_ID,),
        ).fetchone()[0],
        "ri_md_meetings_with_docs": conn.execute(
            """
            SELECT COUNT(DISTINCT m.id)
            FROM meetings m JOIN meeting_documents md ON md.meeting_id = m.id
            WHERE m.board_id = ?
            """,
            (RI_BOARD_ID,),
        ).fetchone()[0],
    }

    per_board_counts = dict(
        conn.execute(
            """
            SELECT b.code, COUNT(m.id)
            FROM boards b LEFT JOIN meetings m ON m.board_id = b.id
            GROUP BY b.code
            """
        ).fetchall()
    )
    per_board_doc_counts = dict(
        conn.execute(
            """
            SELECT b.code, COUNT(md.id)
            FROM boards b
            LEFT JOIN meetings m ON m.board_id = b.id
            LEFT JOIN meeting_documents md ON md.meeting_id = m.id
            GROUP BY b.code
            """
        ).fetchall()
    )

    canary_checksums = {code: _canary_checksum(conn, code) for code in CANARY_BOARD_CODES}

    conn.close()

    baseline = {
        "captured_at": date.today().isoformat(),
        "db_path": str(DB_PATH),
        "integrity_check": integrity,
        "counts": counts,
        "per_board_meeting_counts": per_board_counts,
        "per_board_document_counts": per_board_doc_counts,
        "canary_checksums": canary_checksums,
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = REPORT_DIR / f"migration_baseline_{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(baseline, indent=2, sort_keys=True))
    print(f"Baseline written to {out_path}")
    print(f"Total meetings: {counts['meetings_total']}  RI_MD: {counts['meetings_ri_md']}")
    print(f"Total meeting_documents: {counts['meeting_documents_total']}")
    print(f"RI_MD meetings with docs: {counts['ri_md_meetings_with_docs']}")
    print(f"RI_MD meetings with summary: {counts['ri_md_meetings_with_summary']}")


if __name__ == "__main__":
    main()
