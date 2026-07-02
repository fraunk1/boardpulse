#!/usr/bin/env python3
"""Data-quality audit across the whole boardpulse DB.

Defect classes checked (all deterministic, no LLM):
  A. date-mismatch docs — the document's own filename parses to a date more
     than 7 days from its meeting's date (my collector prefixes dest names
     with the meeting date, so the prefix is stripped before parsing)
  B. boilerplate docs — the same source_url registered on 3+ meetings of a
     board (static templates / sidebar links glued onto many meetings)
  C. cross-board contamination — meeting/doc names carrying another
     profession's keywords (acupuncture on a medical board, etc.)
  D. empty meetings ratio per board (meetings with zero documents)
  E. docs with no extractable text per board
  F. summary-citation integrity — dates cited in each board's summary file
     that don't exist as meetings in the DB

Output: per-class findings + a per-board severity table.
"""
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import date, datetime

from app.config import DB_PATH as DB, REPORTS_DIR as REPORTS
from app.scraper.collector import parse_date

OTHER_PROFESSIONS = [
    "acupunctur", "respiratory", "pharmac", "nursing", "massage",
    "podiatr", "chiropract", "dental", "veterinar", "optometr",
    "athletic train", "psycholog", "social work", "counselor",
    "cosmetol", "funeral", "midwif", "dietit", "occupational therap",
    "physical therap", "speech", "audiolog", "genetic counsel",
    "naturopath", "hearing aid", "emergency medical",  # EMS = known VT quirk
]

DATE_PREFIX = re.compile(r"^\d{4}-\d{2}-\d{2}_")


def main():
    con = sqlite3.connect(DB)
    boards = {r[0]: r[1] for r in con.execute(
        "SELECT id, code FROM boards")}

    docs = con.execute("""
        SELECT d.id, m.board_id, m.id, m.meeting_date, d.filename,
               d.source_url,
               CASE WHEN d.content_text IS NULL THEN 'null'
                    WHEN d.content_text = '' THEN 'empty'
                    ELSE 'text' END
        FROM meeting_documents d JOIN meetings m ON m.id = d.meeting_id
    """).fetchall()

    meetings = con.execute("""
        SELECT m.board_id, m.id, m.meeting_date, m.title,
               (SELECT COUNT(*) FROM meeting_documents d
                WHERE d.meeting_id = m.id)
        FROM meetings m
    """).fetchall()

    sev = defaultdict(lambda: Counter())

    # --- A. date-mismatch docs -------------------------------------------
    print("=" * 70)
    print("A. DATE-MISMATCH DOCS (filename date vs meeting date > 7 days)")
    print("=" * 70)
    mismatches = []
    for did, bid, mid, mdate, fname, src, _t in docs:
        code = boards[bid]
        stripped = DATE_PREFIX.sub("", fname or "")
        # de-percent-encode lightly for date detection
        stripped = stripped.replace("%20", " ").replace("%26", "&")
        fdate = parse_date(stripped)
        if not fdate:
            continue
        md = datetime.strptime(mdate[:10], "%Y-%m-%d").date()
        if abs((fdate - md).days) > 7:
            mismatches.append((code, mid, mdate, stripped, fdate))
            sev[code]["date_mismatch"] += 1
    for code, mid, mdate, fname, fdate in mismatches[:25]:
        print(f"  {code:8} mtg#{mid:<5} {mdate}  doc says {fdate}  | {fname[:60]}")
    print(f"  TOTAL: {len(mismatches)}")

    # --- B. boilerplate docs ---------------------------------------------
    print("\n" + "=" * 70)
    print("B. BOILERPLATE DOCS (same source_url on 3+ meetings of a board)")
    print("=" * 70)
    by_url = defaultdict(set)
    for did, bid, mid, mdate, fname, src, _t in docs:
        if src:
            by_url[(boards[bid], src)].add(mid)
    boiler = {(c, u): ms for (c, u), ms in by_url.items() if len(ms) >= 3}
    for (code, url), ms in sorted(boiler.items(), key=lambda x: -len(x[1]))[:15]:
        print(f"  {code:8} x{len(ms):<3} {url[:80]}")
        sev[code]["boilerplate_urls"] += 1
    print(f"  TOTAL: {len(boiler)} urls "
          f"({sum(len(m) for m in boiler.values())} doc rows)")

    # --- C. cross-board contamination ------------------------------------
    print("\n" + "=" * 70)
    print("C. CROSS-BOARD CONTAMINATION (other professions in titles/files)")
    print("=" * 70)
    contam = []
    for bid, mid, mdate, title, ndocs in meetings:
        code = boards[bid]
        hay = (title or "").lower()
        for kw in OTHER_PROFESSIONS:
            if kw in hay:
                contam.append((code, mid, mdate, kw, "meeting", title))
                sev[code]["contamination"] += 1
                break
    for did, bid, mid, mdate, fname, src, _t in docs:
        code = boards[bid]
        hay = ((fname or "") + " " + (src or "")).lower().replace("%20", " ")
        for kw in OTHER_PROFESSIONS:
            if kw in hay:
                contam.append((code, mid, mdate, kw, "doc", fname))
                sev[code]["contamination"] += 1
                break
    for code, mid, mdate, kw, kind, name in contam[:25]:
        print(f"  {code:8} mtg#{mid:<5} {mdate} [{kind}:{kw}] {str(name)[:55]}")
    print(f"  TOTAL: {len(contam)}")

    # --- D/E. per-board hygiene ------------------------------------------
    print("\n" + "=" * 70)
    print("D/E. PER-BOARD: empty meetings / textless docs")
    print("=" * 70)
    per_board_m = defaultdict(lambda: [0, 0])
    for bid, mid, mdate, title, ndocs in meetings:
        per_board_m[boards[bid]][0] += 1
        if ndocs == 0:
            per_board_m[boards[bid]][1] += 1
    per_board_d = defaultdict(lambda: [0, 0])
    for did, bid, mid, mdate, fname, src, t in docs:
        per_board_d[boards[bid]][0] += 1
        if t != "text":
            per_board_d[boards[bid]][1] += 1
    for code in sorted(per_board_m):
        tm, em = per_board_m[code]
        td, ed = per_board_d.get(code, [0, 0])
        if em / max(tm, 1) > 0.5 or (td and ed / td > 0.5):
            print(f"  {code:8} meetings {tm:>3} ({em} empty)  "
                  f"docs {td:>3} ({ed} textless)")
            sev[code]["hygiene"] += 1

    # --- F. summary-citation integrity ------------------------------------
    print("\n" + "=" * 70)
    print("F. SUMMARY CITATIONS pointing at dates with no meeting in DB")
    print("=" * 70)
    date_re = re.compile(r"#(\d{4}-\d{2}-\d{2})\)")
    total_bad = 0
    mdates = defaultdict(set)
    for bid, mid, mdate, title, ndocs in meetings:
        mdates[boards[bid]].add(mdate[:10])
    for f in sorted(REPORTS.glob("*_summary.md")):
        code = f.stem.replace("_summary", "")
        cited = set(date_re.findall(f.read_text(encoding="utf-8")))
        ghost = cited - mdates.get(code, set())
        if ghost:
            print(f"  {code:8} {len(ghost)}/{len(cited)} cited dates missing: "
                  f"{sorted(ghost)[:5]}")
            sev[code]["ghost_citations"] += len(ghost)
            total_bad += len(ghost)
    print(f"  TOTAL ghost citations: {total_bad}")

    # --- severity table ----------------------------------------------------
    print("\n" + "=" * 70)
    print("SEVERITY BY BOARD (worst first)")
    print("=" * 70)
    ranked = sorted(sev.items(), key=lambda kv: -sum(kv[1].values()))
    for code, c in ranked[:20]:
        detail = "  ".join(f"{k}={v}" for k, v in c.most_common())
        print(f"  {code:8} {sum(c.values()):>4}  {detail}")

    con.close()


if __name__ == "__main__":
    main()
