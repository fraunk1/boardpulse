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


async def snapshot() -> dict:
    """app.stats.per_board_counts() — the ONE definition of the per-board
    coverage aggregate, shared with the /ops status page. Async because run()
    already executes inside an event loop (asyncio.run here would crash)."""
    import app.database as db
    from app.stats import per_board_counts

    await db.init_db(f"sqlite+aiosqlite:///{DB}")
    return await per_board_counts()


def persist_refresh_run(started_at, finished_at, board_filter, before, after,
                        changed, regressed, log_path, exit_code) -> None:
    """Record this run + a full per-board snapshot in the DB so deltas are
    queryable (v_board_deltas) instead of living only in log files."""
    con = sqlite3.connect(DB)
    try:
        cur = con.execute(
            "INSERT INTO refresh_runs (started_at, finished_at, board_filter,"
            " boards_changed, boards_regressed, docs_before, docs_after,"
            " log_path, exit_code) VALUES (?,?,?,?,?,?,?,?,?)",
            (started_at.isoformat(sep=" ", timespec="seconds"),
             finished_at.isoformat(sep=" ", timespec="seconds"),
             board_filter, len(changed),
             ",".join(regressed) or None,
             sum(v["docs"] for v in before.values()),
             sum(v["docs"] for v in after.values()),
             str(log_path), exit_code))
        run_id = cur.lastrowid
        ids = dict(con.execute("SELECT code, id FROM boards").fetchall())
        con.executemany(
            "INSERT INTO board_snapshots (run_id, board_id, mtgs, docs,"
            " docs_text, mtgs_summarized, mtgs_facts) VALUES (?,?,?,?,?,?,?)",
            [(run_id, ids[code], v["mtgs"], v["docs"], v["docs_text"],
              v.get("mtgs_summarized", 0), v.get("mtgs_facts", 0))
             for code, v in after.items() if code in ids])
        con.commit()
    finally:
        con.close()


def rebuild_fts_index() -> None:
    """Rebuild the doc_fts full-text index via a small sync sqlite3 connection.

    Monthly cadence + ~35MB of extracted text means a full rebuild finishes
    in seconds, so there's no drift-prone incremental sync to maintain.
    """
    con = sqlite3.connect(DB)
    con.execute(
        "CREATE VIRTUAL TABLE IF NOT EXISTS doc_fts USING fts5("
        "content_text, content='meeting_documents', content_rowid='id')")
    con.execute("INSERT INTO doc_fts(doc_fts) VALUES('rebuild')")
    con.commit()
    con.close()
    print("FTS index rebuilt")


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

    started_at = datetime.now()
    log_path = setup_logging(quiet)
    before = await snapshot()

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

    # 4b. Keep the full-text search index current
    rebuild_fts_index()

    # 5. Diff report
    after = await snapshot()
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

    exit_code = 1 if regressed else 0
    persist_refresh_run(started_at, datetime.now(), board, before, after,
                        changed, regressed, log_path, exit_code)
    if regressed:
        print(f"\nREGRESSION: doc count decreased for {', '.join(regressed)}")
    return exit_code


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
