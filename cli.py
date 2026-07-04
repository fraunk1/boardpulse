#!/usr/bin/env python3
"""boardpulse CLI — State medical board meeting minutes intelligence."""
import argparse
import asyncio
import sys


def main():
    parser = argparse.ArgumentParser(
        description="boardpulse — State medical board meeting minutes intelligence",
    )
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # seed
    sd = sub.add_parser("seed", help="Seed all 60 US state medical boards from built-in data")
    sd.add_argument("--force", action="store_true", help="Re-seed (skip existing boards)")

    # bootstrap
    bp = sub.add_parser("bootstrap", help="Scrape FSMB contact page to build board registry")
    bp.add_argument("--force", action="store_true", help="Re-bootstrap even if boards exist")

    # discover
    disc = sub.add_parser("discover", help="Discover meeting minutes pages")
    disc.add_argument("--board", type=str, help="Board code (e.g., CA_MD)")
    disc.add_argument("--force", action="store_true", help="Re-discover even if URL cached")

    # collect
    coll = sub.add_parser("collect", help="Collect minutes and screenshots")
    coll.add_argument("--board", type=str, help="Board code (e.g., CA_MD)")

    # extract
    sub.add_parser("extract", help="Extract text from collected documents")

    # summarize
    summ = sub.add_parser("summarize", help="Prepare AI summarization data bundles")
    summ.add_argument("--board", type=str, help="Board code (e.g., CA_MD) — one board only")
    summ.add_argument(
        "--ingest", action="store_true",
        help="Ingest completed summary files back into the database",
    )
    summ.add_argument(
        "--national", action="store_true",
        help="Prepare national landscape synthesis prompt (requires per-board summaries)",
    )
    summ.add_argument(
        "--force", action="store_true",
        help="Bypass the ingest quality gate (manual overrides only)",
    )

    # eval — gold-standard model eval harness
    ev = sub.add_parser("eval", help="Gold-standard eval harness (prepare|score|judge)")
    evsub = ev.add_subparsers(dest="eval_command", required=True)
    evp = evsub.add_parser("prepare", help="Freeze gold set + manifest from data/reports")
    evp.add_argument("--boards", nargs="*", default=None,
                     help="Board codes (default: 8 archetypes)")
    evs = evsub.add_parser("score", help="Score data/eval/<run_id>/ against the gold set")
    evs.add_argument("run_id")
    evs.add_argument("--model-label", default=None)
    evj = evsub.add_parser("judge", help="Emit judge_prompt.md for a qualitative pass")
    evj.add_argument("run_id")

    # refresh — the run-anytime incremental scrape (see refresh.py)
    rf = sub.add_parser(
        "refresh",
        help="Incremental re-scrape of all boards + extract + diff report",
    )
    rf.add_argument("--board", type=str, help="Single board code (e.g. TX_MD)")
    rf.add_argument("--full", action="store_true",
                    help="Reset the board first (requires --board)")
    rf.add_argument("--include-headed", action="store_true",
                    help="Also run headed-WAF boards (visible windows)")
    rf.add_argument("--prompts", action="store_true",
                    help="Emit AI-summary prompt bundles for changed boards")
    rf.add_argument("--no-extract", action="store_true",
                    help="Skip the text-extraction pass")
    rf.add_argument("--quiet", action="store_true", help="Log to file only")

    # serve
    srv = sub.add_parser("serve", help="Start the web dashboard (port 8099)")
    srv.add_argument("--host", default="0.0.0.0", help="Bind address (default: 0.0.0.0)")
    srv.add_argument("--port", type=int, default=8099, help="Port (default: 8099)")

    # exhibits
    exh = sub.add_parser("exhibits", help="Generate highlighted exhibit images from report citations")
    exh.add_argument("--report", type=str, help="Path to landscape report (default: latest)")
    exh.add_argument("--pdf", action="store_true", help="Also build a PDF with exhibits as appendix pages")

    # status
    sub.add_parser("status", help="Show collection status for all boards")

    # diagnostics (consolidated from the former root _*.py scripts)
    cov = sub.add_parser("coverage", help="Coverage report (totals + per-board)")
    cov.add_argument("--summary", action="store_true", help="Totals only")
    sub.add_parser("boards", help="Board-by-board coverage buckets + done-math")
    sub.add_parser("qa", help="Data-quality audit (date mismatches, "
                             "contamination, ghost citations)")
    led = sub.add_parser("ledger", help="Coverage ledger — mark/list "
                                        "none_published/blocked boards")
    led.add_argument("ledger_args", nargs="*",
                     help="list | none_published CODE... | blocked CODE... "
                          "| manual CODE...")

    # run
    sub.add_parser("run", help="Run full pipeline (bootstrap -> discover -> collect -> extract)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Serve is synchronous (uvicorn manages its own event loop)
    if args.command == "serve":
        from app.web.server import run_server
        run_server(host=args.host, port=args.port)
        return

    # Sync diagnostics (stdlib sqlite3 — no event loop needed)
    if args.command == "coverage":
        from app.reports.coverage import main as coverage_main
        coverage_main(summary=args.summary)
        return
    if args.command == "boards":
        from app.reports.boards import main as boards_main
        boards_main()
        return
    if args.command == "qa":
        from app.reports.qa import main as qa_main
        qa_main()
        return
    if args.command == "ledger":
        from app.reports.ledger import main as ledger_main
        ledger_main(args.ledger_args or None)
        return
    if args.command == "eval":
        from app.quality import evalharness
        if args.eval_command == "prepare":
            evalharness.prepare(args.boards or None)
        elif args.eval_command == "score":
            evalharness.score(args.run_id, args.model_label)
        elif args.eval_command == "judge":
            evalharness.judge(args.run_id)
        return

    # Refresh manages its own event loop + exit code
    if args.command == "refresh":
        import refresh as refresh_mod
        sys.exit(asyncio.run(refresh_mod.run(
            board=args.board,
            full=args.full,
            include_headed=args.include_headed,
            prompts=args.prompts,
            no_extract=args.no_extract,
            quiet=args.quiet,
        )))

    asyncio.run(dispatch(args))


async def dispatch(args):
    if args.command == "seed":
        await seed_boards(force=args.force)

    elif args.command == "bootstrap":
        from app.scraper.boards import bootstrap
        await bootstrap(force=args.force)

    elif args.command == "discover":
        from app.scraper.discoverer import discover_all
        await discover_all(board_code=args.board, force=args.force)

    elif args.command == "collect":
        from app.scraper.collector import collect_all
        await collect_all(board_code=args.board)

    elif args.command == "extract":
        from app.extractor.extract import extract_all
        await extract_all()

    elif args.command == "summarize":
        await handle_summarize(args)

    elif args.command == "exhibits":
        await handle_exhibits(args)

    elif args.command == "status":
        await show_status()

    elif args.command == "run":
        from app.scraper.boards import bootstrap
        from app.scraper.discoverer import discover_all
        from app.scraper.collector import collect_all
        from app.extractor.extract import extract_all

        print("=== Bootstrap ===")
        await bootstrap()
        print("\n=== Discover ===")
        await discover_all()
        print("\n=== Collect ===")
        await collect_all()
        print("\n=== Extract ===")
        await extract_all()
        print("\n=== Done ===")


async def seed_boards(force: bool = False):
    """Seed all US state medical boards from built-in data."""
    from app.database import init_db
    from app.models import Board
    from app.scraper.seed_data import BOARDS
    from sqlalchemy import select
    import app.database as db

    await init_db()

    added = 0
    skipped = 0

    async with db.async_session() as session:
        for board_data in BOARDS:
            existing = (await session.execute(
                select(Board).where(Board.code == board_data["code"])
            )).scalar_one_or_none()

            if existing:
                skipped += 1
                continue

            board = Board(
                state=board_data["state"],
                code=board_data["code"],
                name=board_data["name"],
                board_type=board_data["board_type"],
                homepage=board_data["homepage"],
                discovery_status="pending",
            )
            session.add(board)
            added += 1

        await session.commit()

    print(f"Seeded {added} boards ({skipped} already existed).")
    print(f"Total: {added + skipped} boards across {len(set(b['state'] for b in BOARDS))} jurisdictions.")
    print(f"\nNext: run 'python cli.py discover' to find meeting minutes pages.")


async def handle_summarize(args):
    """Handle the summarize command and its flags."""
    from app.extractor.summarizer import (
        prepare_all_bundles,
        ingest_all_summaries,
        ingest_board_summary,
        prepare_national_bundle,
    )
    from app.config import REPORTS_DIR

    if args.ingest:
        # Ingest mode: read completed summary files back into DB. The gate
        # can reject files; exit 1 tells the operator a retry pass is needed
        # (rejected boards leave data/reports/{code}_summary.errors.txt).
        if args.board:
            ok = await ingest_board_summary(
                args.board, force=getattr(args, "force", False))
            sys.exit(0 if ok else 1)
        ingested, rejected = await ingest_all_summaries()
        sys.exit(1 if rejected else 0)

    if args.national:
        # National synthesis mode: build synthesis prompt from per-board summaries
        path = await prepare_national_bundle()
        if path:
            print(f"\n{'='*60}")
            print("NATIONAL SYNTHESIS PROMPT READY")
            print(f"{'='*60}")
            print(f"Prompt file: {path}")
            print(f"\nTo generate the report, have a Claude Code subagent:")
            print(f"  1. Read: {path}")
            print(f"  2. Write output to: {REPORTS_DIR}/{{date}}-board-landscape.md")
        return

    # Default: prepare per-board data bundles
    prompt_paths = await prepare_all_bundles(board_code=args.board)

    if prompt_paths:
        print(f"\n{'='*60}")
        print("SUMMARIZATION PROMPTS READY")
        print(f"{'='*60}")
        print(f"\nPrompt files written to: {REPORTS_DIR}/")
        print(f"Files: {len(prompt_paths)}")
        print()
        for p in prompt_paths:
            board_code = p.stem.replace("_prompt", "")
            print(f"  {board_code}:")
            print(f"    Read:  {p}")
            print(f"    Write: {REPORTS_DIR}/{board_code}_summary.md")
        print()
        print("Next steps:")
        print("  1. Dispatch Claude Code subagents to process each prompt file")
        print("  2. Each subagent reads the prompt and writes the summary file")
        print("  3. Run 'python cli.py summarize --ingest' to store summaries in the DB")
        print("  4. Run 'python cli.py summarize --national' to prepare the synthesis prompt")


async def handle_exhibits(args):
    """Generate exhibit images from report citations, optionally build PDF."""
    from app.extractor.exhibits import generate_all_exhibits
    from app.config import REPORTS_DIR
    from pathlib import Path

    # Find report
    if args.report:
        report_path = Path(args.report)
    else:
        reports = sorted(REPORTS_DIR.glob("*-board-landscape.md"), reverse=True)
        if not reports:
            print("No landscape report found. Run 'summarize --national' first.")
            return
        report_path = reports[0]

    print(f"Generating exhibits from: {report_path.name}\n")
    results = generate_all_exhibits(report_path)

    if args.pdf:
        from app.extractor.exhibit_pdf import build_exhibit_report
        pdf_path = build_exhibit_report(report_path, results)
        if pdf_path:
            print(f"\nExhibit report PDF: {pdf_path}")


async def show_status():
    """Print a status table of all boards."""
    from app.database import init_db
    from app.models import Board, Meeting
    from sqlalchemy import select, func
    import app.database as db

    await init_db()

    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).order_by(Board.state, Board.code)
        )).scalars().all()

    if not boards:
        print("No boards found. Run 'bootstrap' first.")
        return

    print(f"{'Code':<10} {'State':<6} {'Discovery':<12} {'Minutes URL':<40} "
          f"{'Meetings':<10} {'Last Scraped'}")
    print("-" * 110)

    for board in boards:
        async with db.async_session() as session:
            meeting_count = (await session.execute(
                select(func.count(Meeting.id)).where(Meeting.board_id == board.id)
            )).scalar() or 0

        url_display = (board.minutes_url or "")[:37] + "..." if board.minutes_url and len(board.minutes_url) > 40 else (board.minutes_url or "—")
        scraped = board.last_scraped_at.strftime("%Y-%m-%d") if board.last_scraped_at else "—"

        print(f"{board.code:<10} {board.state:<6} {board.discovery_status:<12} "
              f"{url_display:<40} {meeting_count:<10} {scraped}")

    from collections import Counter
    status_counts = Counter(b.discovery_status for b in boards)
    summary = " | ".join(f"{k}: {v}" for k, v in sorted(status_counts.items()))
    print(f"\nTotal: {len(boards)} boards | {summary}")


if __name__ == "__main__":
    main()
