#!/usr/bin/env python3
"""Coverage ledger — mark boards as none_published / blocked (or back).

Usage:
    python _ledger.py none_published AR_MD KY_MD VT_DO WV_DO
    python _ledger.py blocked CO_MD KS_MD
    python _ledger.py manual CO_MD          # undo (back to collectable)
    python _ledger.py list

Statuses set on Board.discovery_status (free string, no migration). Each
change is also recorded with a date + note in coverage_ledger.json at the
repo root (committed — the audit trail for "verified publishes nothing").
"""
import json
import sqlite3
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "boardpulse.db"
LEDGER = ROOT / "coverage_ledger.json"

VALID = {"none_published", "blocked", "manual", "found"}


def load_ledger() -> dict:
    if LEDGER.exists():
        return json.loads(LEDGER.read_text(encoding="utf-8"))
    return {}


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]
    con = sqlite3.connect(DB, timeout=30)

    if cmd == "list":
        rows = con.execute(
            "SELECT code, discovery_status FROM boards "
            "WHERE discovery_status IN ('none_published','blocked') "
            "ORDER BY code").fetchall()
        ledger = load_ledger()
        for code, status in rows:
            entry = ledger.get(code, {})
            print(f"  {code:8} {status:16} verified={entry.get('date', '?')}  "
                  f"{entry.get('note', '')}")
        print(f"{len(rows)} boards accounted")
        con.close()
        return

    if cmd not in VALID:
        print(f"unknown status '{cmd}' — use one of {sorted(VALID)}")
        con.close()
        sys.exit(1)

    codes = [c.upper() for c in sys.argv[2:]]
    if not codes:
        print("no board codes given")
        con.close()
        sys.exit(1)

    ledger = load_ledger()
    for code in codes:
        cur = con.execute(
            "UPDATE boards SET discovery_status=? WHERE code=?", (cmd, code))
        if cur.rowcount == 0:
            print(f"  {code}: NOT FOUND")
            continue
        if cmd in ("none_published", "blocked"):
            ledger[code] = {"status": cmd, "date": date.today().isoformat()}
        else:
            ledger.pop(code, None)
        print(f"  {code}: -> {cmd}")
    con.commit()
    con.close()
    LEDGER.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n",
                      encoding="utf-8")
    print(f"Ledger updated: {LEDGER.name}")


if __name__ == "__main__":
    main()
