#!/usr/bin/env python3
"""Reset and re-collect the given boards (thin wrapper; logic lives in
app/scraper/reset.py + the collector).

Usage: python _recollect.py [--purge-files] CODE [CODE ...]
"""
import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
for n in ("httpx", "httpcore", "asyncio", "playwright"):
    logging.getLogger(n).setLevel(logging.WARNING)

from app.scraper.reset import reset  # noqa: E402  (re-export for importers)


async def main():
    codes = [c for c in sys.argv[1:] if not c.startswith("-")]
    purge = "--purge-files" in sys.argv
    if not codes:
        print("usage: _recollect.py [--purge-files] CODE [CODE ...]")
        return
    print("Resetting:", ", ".join(codes), "(purging files)" if purge else "")
    reset(codes, purge_files=purge)
    from app.scraper.collector import collect_all
    for code in codes:
        await collect_all(board_code=code)


if __name__ == "__main__":
    asyncio.run(main())
