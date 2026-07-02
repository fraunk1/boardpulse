#!/usr/bin/env python3
"""Full board-by-board status for coverage planning (stdlib sqlite3)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent / "boardpulse.db"
con = sqlite3.connect(DB)
cur = con.cursor()
rows = cur.execute(
    """
    SELECT b.code, b.discovery_status,
           CASE WHEN b.minutes_url IS NULL THEN '' ELSE b.minutes_url END AS url,
           COUNT(DISTINCT m.id) AS mtgs, COUNT(d.id) AS docs
    FROM boards b
    LEFT JOIN meetings m ON m.board_id = b.id
    LEFT JOIN meeting_documents d ON d.meeting_id = m.id
    GROUP BY b.id
    ORDER BY docs DESC, mtgs DESC, b.code
    """
).fetchall()

have_docs = [r for r in rows if r[4] > 0]
mtgs_no_docs = [r for r in rows if r[4] == 0 and r[3] > 0]
found_empty = [r for r in rows if r[4] == 0 and r[3] == 0 and r[1] == "found"]
not_found = [r for r in rows if r[1] in ("not_found", "pending", "failed")]

print(f"TOTAL {len(rows)} boards | have_docs={len(have_docs)} | "
      f"mtgs_but_no_docs={len(mtgs_no_docs)} | found_but_empty={len(found_empty)} | "
      f"not_found={len(not_found)}\n")

def dump(label, group):
    print(f"--- {label} ({len(group)}) ---")
    for code, status, url, mtgs, docs in group:
        print(f"  {code:8} {status:10} mtgs={mtgs:<3} docs={docs:<3} {url[:90]}")
    print()

dump("HAVE DOCS", have_docs)
dump("MEETINGS BUT NO DOCS (collector/url issue)", mtgs_no_docs)
dump("FOUND BUT EMPTY (bad url)", found_empty)
dump("NOT DISCOVERED (need url)", not_found)
