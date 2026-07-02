#!/usr/bin/env python3
"""Validate *_summary.md files against the two-layer contract.

For each file (or the codes given as args): parse with the production
parser, then compare its meeting-block dates against the board's actual
window meetings that have extracted text.

    python _validate_summaries.py            # all files
    python _validate_summaries.py HI_MD VA_MD
"""
import sqlite3
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
DB = ROOT / "boardpulse.db"
REPORTS = ROOT / "data" / "reports"

from app.extractor.summarizer import parse_board_summary_file  # noqa: E402


def main():
    codes = sys.argv[1:]
    con = sqlite3.connect(DB)
    cutoff = (date.today() - timedelta(days=365)).isoformat()

    files = sorted(REPORTS.glob("*_summary.md"))
    if codes:
        files = [f for f in files
                 if f.stem.replace("_summary", "") in codes]

    bad = 0
    for f in files:
        code = f.stem.replace("_summary", "")
        _topics, rollup, sections = parse_board_summary_file(
            f.read_text(encoding="utf-8"))

        text_dates = {r[0] for r in con.execute("""
            SELECT DISTINCT m.meeting_date FROM meetings m
            JOIN boards b ON b.id = m.board_id
            JOIN meeting_documents d ON d.meeting_id = m.id
            WHERE b.code = ? AND m.meeting_date >= ?
              AND d.content_text IS NOT NULL AND d.content_text != ''
        """, (code, cutoff)).fetchall()}

        ghosts = sorted(set(sections) - text_dates)
        missing = sorted(text_dates - set(sections))
        legacy = not sections
        rollup_words = len(rollup.split())

        status = "OK"
        if legacy:
            status = "LEGACY"
            bad += 1
        elif ghosts:
            status = "GHOSTS"
            bad += 1
        elif rollup_words < 50:
            status = "THIN-ROLLUP"
            bad += 1

        print(f"  {code:8} {status:12} blocks={len(sections):<3} "
              f"text_meetings={len(text_dates):<3} ghosts={len(ghosts)} "
              f"missing={len(missing)} rollup={rollup_words}w")
        if ghosts:
            print(f"           ghost dates: {ghosts[:5]}")

    con.close()
    print(f"\n{len(files)} files checked, {bad} problematic")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
