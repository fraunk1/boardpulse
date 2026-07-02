#!/usr/bin/env python3
"""Full board-by-board status for coverage planning (stdlib sqlite3).

Buckets every one of the 63 boards — none hidden:
  HAVE DOCS      docs > 0
  ACCOUNTED      discovery_status in (none_published, blocked) — verified
                 as publishing nothing / hard-blocked; counts toward 100%
  MTGS NO DOCS   meetings detected but no documents collected
  URL NO MTGS    a minutes_url is set but no dated meetings were found
  NO URL         never discovered (pending / not_found / failed)

Definition of done: HAVE DOCS + ACCOUNTED == total boards.
"""
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent / "boardpulse.db"

ACCOUNTED_STATUSES = ("none_published", "blocked")

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
con.close()

have_docs = [r for r in rows if r[4] > 0]
accounted = [r for r in rows if r[4] == 0 and r[1] in ACCOUNTED_STATUSES]
mtgs_no_docs = [r for r in rows
                if r[4] == 0 and r[3] > 0 and r[1] not in ACCOUNTED_STATUSES]
url_no_mtgs = [r for r in rows
               if r[4] == 0 and r[3] == 0 and r[2]
               and r[1] not in ACCOUNTED_STATUSES]
no_url = [r for r in rows
          if r[4] == 0 and r[3] == 0 and not r[2]
          and r[1] not in ACCOUNTED_STATUSES]

total = len(rows)
covered = len(have_docs) + len(accounted)

print(f"TOTAL {total} boards | have_docs={len(have_docs)} | "
      f"accounted={len(accounted)} | mtgs_no_docs={len(mtgs_no_docs)} | "
      f"url_no_mtgs={len(url_no_mtgs)} | no_url={len(no_url)}")
print(f"DONE-MATH: have_docs({len(have_docs)}) + accounted({len(accounted)}) "
      f"= {covered} / {total}"
      + ("   << 100% COVERAGE >>" if covered == total else ""))
print()

# Sanity: every board appears in exactly one bucket
bucketed = sum(map(len, (have_docs, accounted, mtgs_no_docs, url_no_mtgs, no_url)))
assert bucketed == total, f"bucket leak: {bucketed} != {total}"


def dump(label, group):
    print(f"--- {label} ({len(group)}) ---")
    for code, status, url, mtgs, docs in group:
        print(f"  {code:8} {status:14} mtgs={mtgs:<4} docs={docs:<4} {url[:80]}")
    print()


dump("HAVE DOCS", have_docs)
dump("ACCOUNTED (none_published / blocked)", accounted)
dump("MEETINGS BUT NO DOCS", mtgs_no_docs)
dump("URL SET, NO MEETINGS FOUND", url_no_mtgs)
dump("NO URL (undiscovered)", no_url)
