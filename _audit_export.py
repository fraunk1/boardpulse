#!/usr/bin/env python3
"""Export per-board audit samples for LLM content auditors.

For each given board: 3 random documents WITH extracted text (filename,
meeting date, source url, first 3500 chars of text) + board metadata →
data/_verify/audit/<CODE>.json. Auditor agents Read these files instead of
touching the DB.
"""
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "boardpulse.db"
OUT = ROOT / "data" / "_verify" / "audit"


def main():
    codes = sys.argv[1:]
    OUT.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    for code in codes:
        board = con.execute(
            "SELECT name, state FROM boards WHERE code=?", (code,)).fetchone()
        if not board:
            print(f"  {code}: not found")
            continue
        docs = con.execute("""
            SELECT d.filename, m.meeting_date, d.source_url,
                   substr(d.content_text, 1, 3500)
            FROM meeting_documents d
            JOIN meetings m ON m.id = d.meeting_id
            JOIN boards b ON b.id = m.board_id
            WHERE b.code=? AND d.content_text IS NOT NULL
              AND d.content_text != ''
            ORDER BY RANDOM() LIMIT 3
        """, (code,)).fetchall()
        payload = {
            "code": code,
            "board_name": board[0],
            "state": board[1],
            "samples": [
                {"filename": f, "meeting_date": md, "source_url": u,
                 "text_excerpt": t}
                for f, md, u, t in docs
            ],
        }
        path = OUT / f"{code}.json"
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"  {code}: {len(docs)} samples -> {path.name}")
    con.close()


if __name__ == "__main__":
    main()
