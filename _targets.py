#!/usr/bin/env python3
"""Emit _targets.md — boards still missing minutes docs (for URL research)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent / "boardpulse.db"
OUT = Path(__file__).resolve().parent / "_targets.md"
con = sqlite3.connect(DB)
rows = con.execute(
    """
    SELECT b.code, b.name, b.homepage, b.discovery_status,
           CASE WHEN b.minutes_url IS NULL THEN '' ELSE b.minutes_url END,
           COUNT(DISTINCT m.id), COUNT(d.id)
    FROM boards b
    LEFT JOIN meetings m ON m.board_id = b.id
    LEFT JOIN meeting_documents d ON d.meeting_id = m.id
    GROUP BY b.id ORDER BY b.code
    """
).fetchall()

lines = [
    "# boardpulse coverage targets",
    "",
    "Boards with **no minutes documents collected** (docs=0). Find the page where "
    "each board posts DOWNLOADABLE meeting minutes/agendas (PDF/DOCX), verify it "
    "has dated document links, and return the best URL.",
    "",
    "| code | board | homepage | current_url (bad/empty) | mtgs | docs |",
    "|---|---|---|---|---|---|",
]
n = 0
for code, name, home, status, url, mtgs, docs in rows:
    if docs > 0:
        continue
    n += 1
    lines.append(f"| {code} | {name} | {home} | {url or '(none)'} | {mtgs} | {docs} |")
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {OUT.name} with {n} target boards (docs=0)")
