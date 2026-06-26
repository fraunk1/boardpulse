#!/usr/bin/env python3
"""Logged pipeline runner for background rebuild stages.

cli.py does not configure logging, so the per-board progress emitted by the
scraper/extractor modules is otherwise silent. This wrapper turns on INFO
logging (with timestamps) and dispatches to a single stage so background runs
produce a readable progress log.

Usage:
    python _pipeline.py discover [--force]
    python _pipeline.py collect  [--board CODE]
    python _pipeline.py extract
"""
import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
# Quiet the noisy transport libraries
for noisy in ("httpx", "httpcore", "asyncio", "playwright"):
    logging.getLogger(noisy).setLevel(logging.WARNING)


async def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "discover"
    force = "--force" in sys.argv
    board = None
    if "--board" in sys.argv:
        board = sys.argv[sys.argv.index("--board") + 1]

    if stage == "discover":
        from app.scraper.discoverer import discover_all
        await discover_all(board_code=board, force=force)
    elif stage == "collect":
        from app.scraper.collector import collect_all
        await collect_all(board_code=board)
    elif stage == "extract":
        from app.extractor.extract import extract_all
        await extract_all()
    else:
        print(f"Unknown stage: {stage}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
