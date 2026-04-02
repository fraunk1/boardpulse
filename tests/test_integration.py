"""Integration test — full pipeline runner lifecycle."""
import pytest
from datetime import date, datetime, timezone

from app import database as db
from app.models import PipelineRun, PipelineEvent
from app.pipeline.runner import PipelineRunner
from sqlalchemy import select


@pytest.mark.asyncio
async def test_full_pipeline_lifecycle():
    """Integration test: start -> log events -> finalize produces correct state."""
    runner = PipelineRunner(trigger="scheduled")
    run_id = await runner.start()

    # Simulate collection events
    await runner.log_event(stage="collect", event_type="started")
    await runner.log_event(
        stage="collect", event_type="new_meeting",
        board_code="TX_MD", detail="2 new meetings",
    )
    await runner.log_event(
        stage="collect", event_type="failed",
        board_code="KS_MD", detail="403 Forbidden",
    )
    await runner.log_event(stage="extract", event_type="completed")

    # Finalize
    await runner.finalize(
        digest_path="data/reports/run_1_digest.md",
        report_path="data/reports/2026-04-01-board-landscape.md",
        boards_collected=51,
        new_meetings=2,
        new_documents=3,
        boards_summarized=1,
    )

    # Verify final state
    async with db.async_session() as session:
        run = await session.get(PipelineRun, run_id)
        assert run.status == "completed"
        assert run.trigger == "scheduled"
        assert run.new_meetings_found == 2
        assert run.new_documents_found == 3
        assert run.boards_summarized == 1
        assert run.digest_path == "data/reports/run_1_digest.md"

        events = (await session.execute(
            select(PipelineEvent)
            .where(PipelineEvent.run_id == run_id)
            .order_by(PipelineEvent.timestamp)
        )).scalars().all()
        assert len(events) == 4

        # Check that failed event is recorded
        failed = [e for e in events if e.event_type == "failed"]
        assert len(failed) == 1
        assert failed[0].board_code == "KS_MD"
        assert "403" in failed[0].detail


@pytest.mark.asyncio
async def test_pipeline_failure_lifecycle():
    """A failed pipeline records the error and sets status correctly."""
    runner = PipelineRunner(trigger="manual")
    run_id = await runner.start()

    await runner.log_event(stage="collect", event_type="started")
    await runner.mark_failed("Network timeout after 300s")

    async with db.async_session() as session:
        run = await session.get(PipelineRun, run_id)
        assert run.status == "failed"
        assert run.completed_at is not None
        assert "timeout" in run.error_message

        events = (await session.execute(
            select(PipelineEvent).where(PipelineEvent.run_id == run_id)
        )).scalars().all()
        assert len(events) == 1
