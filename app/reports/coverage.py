#!/usr/bin/env python3
"""Quick coverage report straight from boardpulse.db (stdlib sqlite3, sync).

Usage:
    python cli.py coverage            # summary + per-board table
    python cli.py coverage --summary  # just the totals
"""
import sqlite3
import sys

from app.config import DB_PATH as DB


def main(summary: bool = False):
    con = sqlite3.connect(DB)
    cur = con.cursor()

    boards = cur.execute("SELECT COUNT(*) FROM boards").fetchone()[0]
    found = cur.execute("SELECT COUNT(*) FROM boards WHERE discovery_status='found'").fetchone()[0]
    meetings = cur.execute("SELECT COUNT(*) FROM meetings").fetchone()[0]
    docs = cur.execute("SELECT COUNT(*) FROM meeting_documents").fetchone()[0]
    docs_text = cur.execute(
        "SELECT COUNT(*) FROM meeting_documents WHERE content_text IS NOT NULL AND content_text != ''"
    ).fetchone()[0]
    mtg_summ = cur.execute(
        "SELECT COUNT(*) FROM meetings WHERE summary IS NOT NULL AND summary != ''"
    ).fetchone()[0]
    boards_with_mtgs = cur.execute(
        "SELECT COUNT(DISTINCT board_id) FROM meetings"
    ).fetchone()[0]

    print("=" * 60)
    print("BOARDPULSE COVERAGE")
    print("=" * 60)
    print(f"Boards seeded ............ {boards}")
    print(f"Boards discovery=found ... {found}")
    print(f"Boards with meetings ..... {boards_with_mtgs}")
    print(f"Meetings ................. {meetings}")
    print(f"Documents ................ {docs}")
    print(f"  with extracted text .... {docs_text}")
    print(f"Meetings with summary .... {mtg_summ}")

    if summary or "--summary" in sys.argv:
        return

    print("\nPer-board (boards with >=1 meeting):")
    print(f"  {'Code':<8} {'Meetings':>8} {'Docs':>6} {'Docs+Text':>10}")
    print("  " + "-" * 36)
    rows = cur.execute(
        """
        SELECT b.code,
               COUNT(DISTINCT m.id) AS mtgs,
               COUNT(d.id) AS docs,
               SUM(CASE WHEN d.content_text IS NOT NULL AND d.content_text != '' THEN 1 ELSE 0 END) AS docs_text
        FROM boards b
        LEFT JOIN meetings m ON m.board_id = b.id
        LEFT JOIN meeting_documents d ON d.meeting_id = m.id
        GROUP BY b.id
        HAVING mtgs > 0
        ORDER BY docs DESC, mtgs DESC
        """
    ).fetchall()
    for code, mtgs, d, dt in rows:
        print(f"  {code:<8} {mtgs:>8} {d:>6} {(dt or 0):>10}")

    con.close()


if __name__ == "__main__":
    main()
