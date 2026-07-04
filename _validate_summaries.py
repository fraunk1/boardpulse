#!/usr/bin/env python3
"""Validate *_summary.md files with the ingest gate (app.quality.gates).

Thin wrapper: for each file (or the codes given as args) it queries the
same DB inputs ingest_board_summary() uses, then runs check_summary() and
prints a per-board table. Exits 1 if any file fails the gate.

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

from app.quality.gates import check_summary, normalize_summary  # noqa: E402


def gate_inputs(con: sqlite3.Connection, code: str) -> dict | None:
    """Build the check_summary() keyword inputs for one board.

    Mirrors ingest_board_summary(): text dates + per-date source text are
    window-scoped (last 365 days); db_all_dates is every meeting the board
    has, any age.
    """
    row = con.execute(
        "SELECT state, minutes_url, homepage FROM boards WHERE code = ?",
        (code,)).fetchone()
    if row is None:
        return None
    state, minutes_url, homepage = row

    cutoff = (date.today() - timedelta(days=365)).isoformat()
    texts: dict[str, list[str]] = {}
    for d, t in con.execute("""
        SELECT m.meeting_date, d.content_text FROM meetings m
        JOIN boards b ON b.id = m.board_id
        JOIN meeting_documents d ON d.meeting_id = m.id
        WHERE b.code = ? AND m.meeting_date >= ?
          AND d.content_text IS NOT NULL AND d.content_text != ''
    """, (code, cutoff)):
        texts.setdefault(d[:10], []).append(t)

    all_dates = {r[0][:10] for r in con.execute("""
        SELECT DISTINCT m.meeting_date FROM meetings m
        JOIN boards b ON b.id = m.board_id
        WHERE b.code = ?
    """, (code,))}

    return dict(
        state=state,
        db_text_dates=set(texts),
        db_all_dates=all_dates,
        source_texts_by_date={k: "\n\n".join(v) for k, v in texts.items()},
        minutes_url=minutes_url,
        homepage=homepage,
    )


def main():
    codes = sys.argv[1:]
    con = sqlite3.connect(DB)

    files = sorted(REPORTS.glob("*_summary.md"))
    if codes:
        files = [f for f in files
                 if f.stem.replace("_summary", "") in codes]

    bad = 0
    for f in files:
        code = f.stem.replace("_summary", "")
        inputs = gate_inputs(con, code)
        if inputs is None:
            print(f"  {code:8} {'NO-BOARD':12} board not found in DB")
            bad += 1
            continue

        text = normalize_summary(f.read_text(encoding="utf-8"))
        result = check_summary(code, text, **inputs)

        status = "OK" if result.ok else "FAIL"
        err_codes = ",".join(sorted({e.code for e in result.errors}))
        print(f"  {code:8} {status:12} errors={len(result.errors):<3} "
              f"warnings={len(result.warnings):<3}"
              f"{'  [' + err_codes + ']' if err_codes else ''}")
        for e in result.errors:
            print(f"           {e.code}: {e.message}")
        if not result.ok:
            bad += 1

    con.close()
    print(f"\n{len(files)} files checked, {bad} problematic")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
