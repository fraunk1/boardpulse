#!/usr/bin/env python3
"""Apply researched minutes URLs (data/_research/g*.json) to the boards table.

Applies URLs whose format is plausibly collectable; skips calendar-only /
none-published / unknown. Prints the list of boards to re-collect.
"""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "boardpulse.db"
RES = ROOT / "data" / "_research"
APPLY_FORMATS = {"direct_pdf", "query_param_portal", "viewer", "google_drive"}

findings = {}
for f in sorted(RES.glob("g*.json")):
    try:
        for item in json.loads(f.read_text(encoding="utf-8")):
            findings[item["code"]] = item
    except Exception as e:
        print(f"  !! {f.name}: parse error {e}")

con = sqlite3.connect(DB, timeout=30)
cur = con.cursor()
applied, skipped = [], []
for code, item in sorted(findings.items()):
    url = (item.get("url") or "").strip()
    fmt = item.get("format", "unknown")
    if url and fmt in APPLY_FORMATS:
        cur.execute(
            "UPDATE boards SET minutes_url=?, discovery_status='manual' WHERE code=?",
            (url, code),
        )
        applied.append(code)
        print(f"  APPLY {code:8} [{fmt:18}] {url[:80]}")
    else:
        skipped.append((code, fmt))
con.commit()
con.close()

print(f"\nApplied {len(applied)} | Skipped {len(skipped)} | Total findings {len(findings)}")
if skipped:
    print("Skipped:", ", ".join(f"{c}({f})" for c, f in skipped))
print("\nRECOLLECT:", " ".join(applied))
