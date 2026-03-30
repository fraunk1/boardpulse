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

    # serve
    srv = sub.add_parser("serve", help="Start the web dashboard (port 8099)")
    srv.add_argument("--host", default="0.0.0.0", help="Bind address (default: 0.0.0.0)")
    srv.add_argument("--port", type=int, default=8099, help="Port (default: 8099)")

    # status
    sub.add_parser("status", help="Show collection status for all boards")

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
        # Ingest mode: read completed summary files back into DB
        if args.board:
            await ingest_board_summary(args.board)
        else:
            await ingest_all_summaries()
        return

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

    found = sum(1 for b in boards if b.discovery_status == "found")
    failed = sum(1 for b in boards if b.discovery_status == "failed")
    pending = sum(1 for b in boards if b.discovery_status == "pending")
    print(f"\nTotal: {len(boards)} boards | Found: {found} | Failed: {failed} | Pending: {pending}")


if __name__ == "__main__":
    main()
