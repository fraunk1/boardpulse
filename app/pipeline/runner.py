"""Pipeline orchestrator — manages run lifecycle, event logging, and stage execution."""
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import select

import app.database as db
from app.models import PipelineRun, PipelineEvent, Board, Meeting, MeetingDocument
from app.pipeline.delta import snapshot_board_counts, compute_delta
from app.pipeline.context import generate_context_file
from app.config import REPORTS_DIR


class PipelineRunner:
    """Orchestrates a single pipeline run."""

    def __init__(self, trigger: str = "manual"):
        self.trigger = trigger
        self.run_id: int | None = None
        self._snapshot_before: dict = {}

    async def start(self) -> int:
        """Create a PipelineRun record and return its ID."""
        await db.init_db()
        async with db.async_session() as session:
            run = PipelineRun(
                started_at=datetime.now(timezone.utc),
                status="running",
                trigger=self.trigger,
                boards_collected=0,
                new_meetings_found=0,
                new_documents_found=0,
                boards_summarized=0,
            )
            session.add(run)
            await session.commit()
            await session.refresh(run)
            self.run_id = run.id
        return self.run_id

    async def log_event(
        self,
        stage: str,
        event_type: str,
        board_code: str | None = None,
        detail: str | None = None,
    ):
        """Log a PipelineEvent for the current run."""
        async with db.async_session() as session:
            event = PipelineEvent(
                run_id=self.run_id,
                timestamp=datetime.now(timezone.utc),
                stage=stage,
                board_code=board_code,
                event_type=event_type,
                detail=detail,
            )
            session.add(event)
            await session.commit()

    async def snapshot(self):
        """Take a snapshot of current board counts (call before collection)."""
        self._snapshot_before = await snapshot_board_counts()

    async def run_collection(self, board_codes: list[str] | None = None):
        """Run the collection stage. Wraps existing collector."""
        from app.scraper.collector import collect_all

        await self.log_event(stage="collect", event_type="started")
        await self.snapshot()

        if board_codes:
            for code in board_codes:
                try:
                    await self.log_event(stage="collect", event_type="started", board_code=code)
                    await collect_all(board_code=code)
                    await self.log_event(stage="collect", event_type="completed", board_code=code)
                except Exception as e:
                    await self.log_event(
                        stage="collect", event_type="failed",
                        board_code=code, detail=str(e),
                    )
        else:
            try:
                await collect_all()
                await self.log_event(stage="collect", event_type="completed")
            except Exception as e:
                await self.log_event(
                    stage="collect", event_type="failed", detail=str(e),
                )

    async def run_extraction(self):
        """Run text extraction on new documents."""
        from app.extractor.extract import extract_all

        await self.log_event(stage="extract", event_type="started")
        try:
            await extract_all()
            await self.log_event(stage="extract", event_type="completed")
        except Exception as e:
            await self.log_event(stage="extract", event_type="failed", detail=str(e))

    async def run_rendering(self):
        """Render pages for new PDF documents."""
        from app.pipeline.renderer import render_all_new_pages

        await self.log_event(stage="render", event_type="started")
        try:
            result = await render_all_new_pages()
            await self.log_event(
                stage="render", event_type="completed",
                detail=f"{result['rendered']} pages rendered from {result['total']} documents",
            )
        except Exception as e:
            await self.log_event(stage="render", event_type="failed", detail=str(e))

    async def run_fts_rebuild(self):
        """Rebuild the FTS5 search index."""
        from app.pipeline.fts import rebuild_fts_index

        await self.log_event(stage="fts", event_type="started")
        try:
            result = await rebuild_fts_index()
            await self.log_event(
                stage="fts", event_type="completed",
                detail=f"{result['indexed']} meetings indexed",
            )
        except Exception as e:
            await self.log_event(stage="fts", event_type="failed", detail=str(e))

    async def compute_and_write_context(self) -> dict:
        """Compute delta, write context file, prepare prompts. Returns delta dict."""
        snapshot_after = await snapshot_board_counts()
        delta = compute_delta(self._snapshot_before, snapshot_after)

        all_codes = set(snapshot_after.keys())
        changed_codes = set(delta.keys())
        no_change = sorted(all_codes - changed_codes)

        context_path = REPORTS_DIR / f"run_{self.run_id}_context.md"
        await generate_context_file(
            run_id=self.run_id,
            delta=delta,
            no_change_boards=no_change,
            output_path=context_path,
            reports_dir=REPORTS_DIR,
        )
        print(f"\nPipeline context file: {context_path}")

        if delta:
            from app.extractor.summarizer import prepare_board_bundle
            for code in delta:
                try:
                    await prepare_board_bundle(code)
                except Exception as e:
                    print(f"  Warning: could not prepare prompt for {code}: {e}")

        for code in delta:
            async with db.async_session() as session:
                board = (await session.execute(
                    select(Board).where(Board.code == code)
                )).scalar_one_or_none()
                if board:
                    meetings = (await session.execute(
                        select(Meeting)
                        .where(Meeting.board_id == board.id)
                        .where(Meeting.pipeline_run_id.is_(None))
                    )).scalars().all()
                    for m in meetings:
                        m.pipeline_run_id = self.run_id
                    await session.commit()

        for code, counts in delta.items():
            await self.log_event(
                stage="collect", event_type="new_meeting", board_code=code,
                detail=f"{counts['new_meetings']} new meetings, {counts['new_documents']} new documents",
            )

        return delta

    async def finalize(
        self,
        digest_path: str | None = None,
        report_path: str | None = None,
        boards_collected: int = 0,
        new_meetings: int = 0,
        new_documents: int = 0,
        boards_summarized: int = 0,
    ):
        """Mark run as completed and record final stats."""
        async with db.async_session() as session:
            run = await session.get(PipelineRun, self.run_id)
            run.status = "completed"
            run.completed_at = datetime.now(timezone.utc)
            run.digest_path = digest_path
            run.report_path = report_path
            run.boards_collected = boards_collected
            run.new_meetings_found = new_meetings
            run.new_documents_found = new_documents
            run.boards_summarized = boards_summarized
            await session.commit()

    async def mark_failed(self, error: str):
        """Mark run as failed with error message."""
        async with db.async_session() as session:
            run = await session.get(PipelineRun, self.run_id)
            run.status = "failed"
            run.completed_at = datetime.now(timezone.utc)
            run.error_message = error
            await session.commit()
