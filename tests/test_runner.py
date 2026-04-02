"""Test PipelineRunner lifecycle management."""
import pytest
from datetime import date, datetime, timezone

from app import database as db
from app.models import PipelineRun, PipelineEvent
from app.pipeline.runner import PipelineRunner
from sqlalchemy import select


@pytest.mark.asyncio
async def test_pipeline_runner_creates_run_record():
    runner = PipelineRunner(trigger="manual")
    run_id = await runner.start()
    assert run_id is not None

    async with db.async_session() as session:
        run = await session.get(PipelineRun, run_id)
        assert run.status == "running"
        assert run.trigger == "manual"


@pytest.mark.asyncio
async def test_pipeline_runner_log_event():
    runner = PipelineRunner(trigger="manual")
    run_id = await runner.start()
    await runner.log_event(
        stage="collect", board_code="TX_MD",
        event_type="new_meeting", detail="Found meeting 2026-03-15",
    )

    async with db.async_session() as session:
        events = (await session.execute(
            select(PipelineEvent).where(PipelineEvent.run_id == run_id)
        )).scalars().all()
        assert len(events) == 1
        assert events[0].stage == "collect"
        assert events[0].board_code == "TX_MD"


@pytest.mark.asyncio
async def test_pipeline_runner_finalize():
    runner = PipelineRunner(trigger="manual")
    run_id = await runner.start()
    await runner.finalize(
        digest_path="data/reports/run_1_digest.md",
        report_path="data/reports/2026-04-01-board-landscape.md",
        boards_collected=5, new_meetings=3, new_documents=7, boards_summarized=2,
    )

    async with db.async_session() as session:
        run = await session.get(PipelineRun, run_id)
        assert run.status == "completed"
        assert run.completed_at is not None
        assert run.digest_path == "data/reports/run_1_digest.md"
        assert run.new_meetings_found == 3


@pytest.mark.asyncio
async def test_pipeline_runner_mark_failed():
    runner = PipelineRunner(trigger="manual")
    run_id = await runner.start()
    await runner.mark_failed("Collection crashed: timeout")

    async with db.async_session() as session:
        run = await session.get(PipelineRun, run_id)
        assert run.status == "failed"
        assert "timeout" in run.error_message
