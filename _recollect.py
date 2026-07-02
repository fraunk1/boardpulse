#!/usr/bin/env python3
"""Reset and re-collect the given boards.

`collect_board` skips meetings that already exist, so after fixing a board's
minutes_url OR the collector itself, a plain re-collect won't backfill docs.
This clears each board's meetings (+documents) first, then collects fresh.

Usage: python _recollect.py MT_MD WA_MD UT_MD ...
"""
import asyncio
import logging
import sqlite3
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
for n in ("httpx", "httpcore", "asyncio", "playwright"):
    logging.getLogger(n).setLevel(logging.WARNING)

DB = Path(__file__).resolve().parent / "boardpulse.db"


def reset(codes):
    con = sqlite3.connect(DB, timeout=30)
    cur = con.cursor()
    for code in codes:
        row = cur.execute("SELECT id FROM boards WHERE code=?", (code,)).fetchone()
        if not row:
            print(f"  {code}: NOT FOUND")
            continue
        bid = row[0]
        cur.execute(
            "DELETE FROM meeting_documents WHERE meeting_id IN "
            "(SELECT id FROM meetings WHERE board_id=?)", (bid,))
        cur.execute("DELETE FROM meetings WHERE board_id=?", (bid,))
        print(f"  {code}: cleared")
    con.commit()
    con.close()


async def main():
    codes = [c for c in sys.argv[1:] if not c.startswith("-")]
    if not codes:
        print("usage: _recollect.py CODE [CODE ...]")
        return
    print("Resetting:", ", ".join(codes))
    reset(codes)
    from app.scraper.collector import collect_all
    for code in codes:
        await collect_all(board_code=code)


if __name__ == "__main__":
    asyncio.run(main())
