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

    # exhibits
    exh = sub.add_parser("exhibits", help="Generate highlighted exhibit images from report citations")
    exh.add_argument("--report", type=str, help="Path to landscape report (default: latest)")
    exh.add_argument("--pdf", action="store_true", help="Also build a PDF with exhibits as appendix pages")

    # classify
    classify = sub.add_parser("classify", help="Classify documents/pages into topic categories")
    classify.add_argument("--pages", action="store_true", help="Also classify individual pages")
    classify.add_argument("--force", action="store_true", help="Re-classify even if topics exist")
    classify.add_argument("--min-matches", type=int, default=2, help="Min keyword hits per topic (default: 2)")

    # render
    rend = sub.add_parser("render", help="Render PDF pages as images")
    rend.add_argument("--doc-id", type=int, help="Render a specific document ID")

    # status
    sub.add_parser("status", help="Show collection status for all boards")

    # run
    sub.add_parser("run", help="Run full pipeline (bootstrap -> discover -> collect -> extract)")

    # pipeline
    pipe = sub.add_parser("pipeline", help="Run the automated intelligence pipeline")
    pipe.add_argument("--boards", type=str, help="Comma-separated board codes (e.g., TX_MD,FL_MD)")
    pipe.add_argument("--skip-report", action="store_true", help="Collection + extraction only, skip prompt prep")
    pipe.add_argument("--finalize", action="store_true", help="Mark a run as complete")
    pipe.add_argument("--run-id", type=int, help="Pipeline run ID (for --finalize and --ingest-topics)")
    pipe.add_argument("--digest-path", type=str, help="Path to digest file (for --finalize)")
    pipe.add_argument("--report-path", type=str, help="Path to report file (for --finalize)")
    pipe.add_argument("--ingest-topics", action="store_true", help="Ingest topic tags from JSON")
    pipe.add_argument("--status", action="store_true", help="Show recent pipeline runs")
    pipe.add_argument("--rebuild-fts", action="store_true", help="Rebuild the FTS5 search index")

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

    elif args.command == "classify":
        await handle_classify(args)

    elif args.command == "render":
        await handle_render(args)

    elif args.command == "summarize":
        await handle_summarize(args)

    elif args.command == "exhibits":
        await handle_exhibits(args)

    elif args.command == "status":
        await show_status()

    elif args.command == "pipeline":
        await handle_pipeline(args)

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


async def handle_classify(args):
    """Classify documents and optionally pages into topic categories."""
    from app.database import init_db
    from app.pipeline.classifier import classify_all_documents, classify_all_pages

    await init_db()

    print("=== Document Classification ===")
    result = await classify_all_documents(
        force=args.force,
        min_matches=args.min_matches,
    )

    if args.pages:
        print("\n=== Page-Level Classification ===")
        page_result = await classify_all_pages(
            force=args.force,
            min_matches=max(1, args.min_matches - 1),  # lower threshold for pages
        )

    # Rebuild FTS after classification
    from app.pipeline.fts import rebuild_fts_index
    print("\n=== Rebuilding FTS Index ===")
    await rebuild_fts_index()
    print("Done.")


async def handle_render(args):
    """Render PDF document pages as images."""
    from app.database import init_db
    from app.pipeline.renderer import render_document_pages, render_all_new_pages

    await init_db()

    if args.doc_id:
        print(f"Rendering document {args.doc_id}...")
        result = await render_document_pages(args.doc_id)
        print(f"Result: {result}")
    else:
        print("Rendering all unrendered documents...")
        result = await render_all_new_pages()
        print(f"Result: {result}")


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


async def handle_pipeline(args):
    """Handle the pipeline command and its flags."""
    from app.database import init_db
    await init_db()

    if args.status:
        await show_pipeline_status()
        return

    if args.rebuild_fts:
        from app.pipeline.fts import rebuild_fts_index
        print("Rebuilding FTS5 search index...")
        await rebuild_fts_index()
        print("Done.")
        return

    if args.ingest_topics:
        if not args.run_id:
            print("Error: --ingest-topics requires --run-id")
            sys.exit(1)
        from app.config import REPORTS_DIR
        import json as _json

        topics_file = REPORTS_DIR / f"run_{args.run_id}_topics.json"
        if not topics_file.exists():
            print(f"Error: topics file not found: {topics_file}")
            sys.exit(1)

        data = _json.loads(topics_file.read_text())
        first_value = next(iter(data.values()), None)
        is_page_level = isinstance(first_value, dict)

        if is_page_level:
            from app.pipeline.topics import ingest_page_topics_from_file
            print(f"Ingesting page-level topics from {topics_file}...")
            await ingest_page_topics_from_file(topics_file)
        else:
            from app.pipeline.topics import ingest_topics_from_file
            print(f"Ingesting document-level topics from {topics_file}...")
            await ingest_topics_from_file(topics_file)
        print("Done.")
        return

    if args.finalize:
        if not args.run_id:
            print("Error: --finalize requires --run-id")
            sys.exit(1)
        from app.pipeline.runner import PipelineRunner
        from app.models import Meeting, PipelineRun as PR
        from sqlalchemy import select, func
        import app.database as db

        async with db.async_session() as session:
            run = await session.get(PR, args.run_id)
            if not run:
                print(f"Error: run #{args.run_id} not found")
                sys.exit(1)
            boards_summarized = (await session.execute(
                select(func.count(func.distinct(Meeting.board_id)))
                .where(Meeting.pipeline_run_id == args.run_id)
                .where(Meeting.summary.isnot(None))
            )).scalar() or 0

        runner = PipelineRunner()
        runner.run_id = args.run_id
        await runner.finalize(
            digest_path=args.digest_path,
            report_path=args.report_path,
            boards_collected=run.boards_collected,
            new_meetings=run.new_meetings_found,
            new_documents=run.new_documents_found,
            boards_summarized=boards_summarized,
        )
        print(f"Pipeline run #{args.run_id} marked as completed ({boards_summarized} boards summarized).")
        return

    # Default: run the full pipeline
    from app.pipeline.runner import PipelineRunner
    import app.database as db

    board_codes = args.boards.split(",") if args.boards else None
    runner = PipelineRunner(trigger="manual")

    try:
        run_id = await runner.start()
        print(f"\n{'='*60}")
        print(f"PIPELINE RUN #{run_id}")
        print(f"{'='*60}")

        print("\n--- Stage 1: Collection ---")
        await runner.run_collection(board_codes=board_codes)

        print("\n--- Stage 2: Text Extraction ---")
        await runner.run_extraction()

        # Stage 3: Render pages
        print("\n--- Stage 3: Page Rendering ---")
        await runner.run_rendering()

        if args.skip_report:
            print("\n--- Skipping prompt preparation (--skip-report) ---")
            delta = {}
        else:
            print("\n--- Stage 4: Delta Calculation + Context File ---")
            delta = await runner.compute_and_write_context()

        # Rebuild FTS index
        print("\n--- Rebuilding FTS index ---")
        await runner.run_fts_rebuild()

        total_new_meetings = sum(d["new_meetings"] for d in delta.values())
        total_new_docs = sum(d["new_documents"] for d in delta.values())

        async with db.async_session() as session:
            from app.models import PipelineRun as PR
            run = await session.get(PR, run_id)
            run.boards_collected = len(board_codes) if board_codes else await _count_boards()
            run.new_meetings_found = total_new_meetings
            run.new_documents_found = total_new_docs
            await session.commit()

        print(f"\n{'='*60}")
        print(f"PIPELINE RUN #{run_id} — Layer 1 Complete")
        print(f"{'='*60}")
        print(f"  New meetings:  {total_new_meetings}")
        print(f"  New documents: {total_new_docs}")
        print(f"  Boards with new content: {len(delta)}")
        if delta and not args.skip_report:
            from app.config import REPORTS_DIR
            context_path = REPORTS_DIR / f"run_{run_id}_context.md"
            print(f"\n  Context file: {context_path}")
            print(f"\n  Next: Have your AI assistant read the context file and follow the instructions.")
        elif not delta:
            print("\n  No new content found. Nothing to summarize.")
            await runner.finalize()
        print()

    except Exception as e:
        await runner.mark_failed(str(e))
        print(f"\nPipeline failed: {e}")
        sys.exit(1)


async def _count_boards() -> int:
    from sqlalchemy import func, select
    import app.database as db
    from app.models import Board
    async with db.async_session() as session:
        return (await session.execute(select(func.count(Board.id)))).scalar() or 0


async def show_pipeline_status():
    from sqlalchemy import select
    import app.database as db
    from app.models import PipelineRun

    async with db.async_session() as session:
        runs = (await session.execute(
            select(PipelineRun).order_by(PipelineRun.started_at.desc()).limit(10)
        )).scalars().all()

    if not runs:
        print("No pipeline runs found.")
        return

    print(f"{'ID':<5} {'Date':<12} {'Status':<12} {'Trigger':<10} "
          f"{'Meetings':<10} {'Documents':<10} {'Summarized':<10}")
    print("-" * 80)

    for r in runs:
        date_str = r.started_at.strftime("%Y-%m-%d") if r.started_at else "—"
        print(f"{r.id:<5} {date_str:<12} {r.status:<12} {r.trigger:<10} "
              f"{r.new_meetings_found:<10} {r.new_documents_found:<10} {r.boards_summarized:<10}")


if __name__ == "__main__":
    main()
