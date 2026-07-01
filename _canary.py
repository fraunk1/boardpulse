#!/usr/bin/env python3
"""Wave-3 regression canary for the collector.

Two modes:
    python _canary.py baseline   # snapshot per-board counts from the REAL db
                                 #   -> data/_verify/wave3_baseline.json
    python _canary.py            # regression check: copy the db to a scratch
                                 #   location, re-collect 5 archetype "good"
                                 #   boards against the COPY, assert counts
                                 #   did not regress vs the copy's own state.

Isolation guarantees:
- DB: the copy is made with sqlite3's backup API (WAL-safe); the module-level
  app.database.DATABASE_URL is repointed at the copy, so every internal
  init_db() call (collect_all re-inits!) hits the copy, never the real db.
- Files: collector.DOCUMENTS_DIR / SCREENSHOTS_DIR module globals are
  repointed at a scratch directory, so no real data files are touched.

Exit code 0 = green, 1 = regression or error.
"""
import asyncio
import json
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REAL_DB = ROOT / "boardpulse.db"
BASELINE = ROOT / "data" / "_verify" / "wave3_baseline.json"

# Archetype boards that work today — spans plain lists, accordion pages,
# year indexes, and CMS-hosted PDFs. These must never regress.
CANARY_BOARDS = ["OK_MD", "HI_MD", "ME_MD", "MS_MD", "AZ_MD"]

COUNT_SQL = """
    SELECT b.code,
           COUNT(DISTINCT m.id) AS mtgs,
           COUNT(d.id) AS docs,
           SUM(CASE WHEN d.content_text IS NOT NULL AND d.content_text != ''
                    THEN 1 ELSE 0 END) AS docs_text
    FROM boards b
    LEFT JOIN meetings m ON m.board_id = b.id
    LEFT JOIN meeting_documents d ON d.meeting_id = m.id
    GROUP BY b.id
"""


def counts(db_path: Path) -> dict:
    con = sqlite3.connect(db_path)
    rows = con.execute(COUNT_SQL).fetchall()
    con.close()
    return {code: {"meetings": m, "docs": d, "docs_text": dt or 0}
            for code, m, d, dt in rows}


def write_baseline():
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    snap = {
        "recorded_at": datetime.now().isoformat(timespec="seconds"),
        "boards": counts(REAL_DB),
    }
    BASELINE.write_text(json.dumps(snap, indent=2), encoding="utf-8")
    total_docs = sum(b["docs"] for b in snap["boards"].values())
    print(f"Baseline written: {len(snap['boards'])} boards, "
          f"{total_docs} docs -> {BASELINE}")


def backup_db(dest: Path):
    """WAL-safe copy of the real db."""
    src = sqlite3.connect(f"file:{REAL_DB}?mode=ro", uri=True)
    dst = sqlite3.connect(dest)
    with dst:
        src.backup(dst)
    src.close()
    dst.close()


async def run_check() -> int:
    scratch = Path(tempfile.mkdtemp(prefix="bp_canary_"))
    db_copy = scratch / "canary.db"
    backup_db(db_copy)

    # --- isolation: repoint db + file dirs BEFORE importing pipeline code ---
    import app.database as db
    db.DATABASE_URL = f"sqlite+aiosqlite:///{db_copy.as_posix()}"

    from app.scraper import collector
    scratch_docs = scratch / "documents"
    scratch_ss = scratch / "screenshots"
    collector.DOCUMENTS_DIR = scratch_docs
    collector.SCREENSHOTS_DIR = scratch_ss

    before = counts(db_copy)

    print(f"Canary run against {db_copy}")
    for code in CANARY_BOARDS:
        print(f"\n--- canary: {code} ---")
        try:
            await collector.collect_all(board_code=code)
        except Exception as exc:
            print(f"CANARY FAIL: {code} raised {exc!r}")
            return 1

    after = counts(db_copy)

    failed = False
    print(f"\n{'Board':<8} {'mtgs':>10} {'docs':>10}  result")
    for code in CANARY_BOARDS:
        b, a = before.get(code, {}), after.get(code, {})
        ok = (a.get("meetings", 0) >= b.get("meetings", 0)
              and a.get("docs", 0) >= b.get("docs", 0))
        print(f"{code:<8} {b.get('meetings',0):>4}->{a.get('meetings',0):<5} "
              f"{b.get('docs',0):>4}->{a.get('docs',0):<5}  "
              f"{'OK' if ok else 'REGRESSION'}")
        failed = failed or not ok

    shutil.rmtree(scratch, ignore_errors=True)
    print(f"\nCANARY {'FAIL' if failed else 'GREEN'}")
    return 1 if failed else 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "baseline":
        write_baseline()
        return
    sys.exit(asyncio.run(run_check()))


if __name__ == "__main__":
    main()
