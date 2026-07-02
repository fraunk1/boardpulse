#!/usr/bin/env python3
"""boardpulse refresh — one command to re-scrape everything, any time.

    python refresh.py                 # incremental: collect all boards,
                                      #   probe pattern-URL boards, extract
                                      #   text, print what changed
    python refresh.py --board TX_MD   # one board only
    python refresh.py --full --board TX_MD   # reset that board, then collect
    python refresh.py --include-headed        # also run headed-WAF boards
                                      #   (visible Chromium windows — needs
                                      #   a desktop session; skipped by
                                      #   default so cron runs never hang)
    python refresh.py --prompts       # also emit AI-summary prompt bundles
                                      #   for boards whose documents changed

Idempotency: meetings dedupe by (board, date); documents dedupe by
source_url + filename; files are byte-validated before writing. Safe to run
repeatedly — a second consecutive run reports "no changes".

Exit codes: 0 = ok, 1 = a board's document count DECREASED (regression) or
the run crashed. Cron-safe.

Logs: console + data/logs/refresh-YYYYMMDD-HHMMSS.log
"""
import argparse
import asyncio
import logging
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from app.config import LOGS_DIR  # noqa: E402

DB = ROOT / "boardpulse.db"

SNAP_SQL = """
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


def snapshot() -> dict:
    con = sqlite3.connect(DB)
    rows = con.execute(SNAP_SQL).fetchall()
    con.close()
    return {code: {"mtgs": m, "docs": d, "docs_text": dt or 0}
            for code, m, d, dt in rows}


def setup_logging(quiet: bool) -> Path:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / f"refresh-{datetime.now():%Y%m%d-%H%M%S}.log"
    handlers = [logging.FileHandler(log_path, encoding="utf-8")]
    if not quiet:
        handlers.append(logging.StreamHandler())
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        handlers=handlers,
    )
    for noisy in ("httpx", "httpcore", "asyncio", "playwright"):
        logging.getLogger(noisy).setLevel(logging.WARNING)
    return log_path


async def run(
    board: str | None = None,
    full: bool = False,
    include_headed: bool = False,
    prompts: bool = False,
    no_extract: bool = False,
    quiet: bool = False,
) -> int:
    from app.scraper.collector import collect_all
    from app.scraper.strategies import STRATEGIES
    from app.scraper.url_probe import probe_board
    from app.extractor.extract import extract_all

    log_path = setup_logging(quiet)
    before = snapshot()

    # 1. Reset first when --full (single board only — global reset is too
    #    destructive for an unattended tool)
    if full:
        if not board:
            print("--full requires --board (global reset is not allowed here; "
                  "use _recollect.py explicitly if you really mean it)")
            return 1
        from _recollect import reset
        reset([board.upper()])

    # 2. Collect (incremental). Headed-strategy boards are skipped unless
    #    explicitly included — they pop visible Chromium windows.
    headed_codes = {code for code, s in STRATEGIES.items() if s.headed}
    exclude = set() if include_headed else headed_codes
    await collect_all(
        board_code=board.upper() if board else None,
        exclude_codes=exclude or None,
    )

    # 3. Probe pattern-URL boards (no usable index page)
    probe_codes = [code for code, s in STRATEGIES.items() if s.url_probes]
    if board:
        probe_codes = [c for c in probe_codes if c == board.upper()]
    for code in probe_codes:
        if code in exclude:
            continue
        await probe_board(code)

    # 4. Extract text from any new documents
    if not no_extract:
        await extract_all()

    # 5. Diff report
    after = snapshot()
    changed: list[str] = []
    regressed: list[str] = []
    print("\n" + "=" * 64)
    print(f"REFRESH DIFF  ({datetime.now():%Y-%m-%d %H:%M})")
    print("=" * 64)
    header = f"{'Board':<8} {'meetings':>14} {'docs':>14} {'docs+text':>14}"
    printed_header = False
    for code in sorted(after):
        b = before.get(code, {"mtgs": 0, "docs": 0, "docs_text": 0})
        a = after[code]
        if (a["mtgs"], a["docs"], a["docs_text"]) == (
                b["mtgs"], b["docs"], b["docs_text"]):
            continue
        if not printed_header:
            print(header)
            printed_header = True
        changed.append(code)
        if a["docs"] < b["docs"]:
            regressed.append(code)
        print(f"{code:<8} {b['mtgs']:>6}->{a['mtgs']:<6} "
              f"{b['docs']:>6}->{a['docs']:<6} "
              f"{b['docs_text']:>6}->{a['docs_text']:<6}")

    if not changed:
        print("no changes")
    tot_b = sum(v["docs"] for v in before.values())
    tot_a = sum(v["docs"] for v in after.values())
    print(f"\nTotals: docs {tot_b} -> {tot_a} | boards changed: {len(changed)}")
    print(f"Log: {log_path}")

    # 6. Optional: emit AI-summary prompt bundles for changed boards
    if prompts and changed:
        from app.extractor.summarizer import prepare_board_bundle
        print("\nPreparing summary prompt bundles for changed boards...")
        for code in changed:
            await prepare_board_bundle(code)

    if regressed:
        print(f"\nREGRESSION: doc count decreased for {', '.join(regressed)}")
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Re-scrape state medical board meeting documents "
                    "(incremental, idempotent, cron-safe)")
    ap.add_argument("--board", help="single board code (e.g. TX_MD)")
    ap.add_argument("--full", action="store_true",
                    help="reset the board first (requires --board)")
    ap.add_argument("--include-headed", action="store_true",
                    help="also run headed-WAF boards (visible windows)")
    ap.add_argument("--prompts", action="store_true",
                    help="emit AI-summary prompt bundles for changed boards")
    ap.add_argument("--no-extract", action="store_true",
                    help="skip the text-extraction pass")
    ap.add_argument("--quiet", action="store_true",
                    help="log to file only")
    args = ap.parse_args()
    sys.exit(asyncio.run(run(
        board=args.board,
        full=args.full,
        include_headed=args.include_headed,
        prompts=args.prompts,
        no_extract=args.no_extract,
        quiet=args.quiet,
    )))


if __name__ == "__main__":
    main()
