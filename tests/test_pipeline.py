"""Test pipeline data models."""
import pytest
from datetime import date, datetime, timezone

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import database as db
from app.models import Board, Meeting, MeetingDocument, PipelineRun, PipelineEvent


@pytest.fixture(autouse=True)
async def setup_db(tmp_path):
    """Initialize a fresh in-memory DB for each test."""
    await db.init_db(url="sqlite+aiosqlite://")
    yield


@pytest.mark.asyncio
async def test_create_pipeline_run():
    async with db.async_session() as session:
        run = PipelineRun(
            started_at=datetime.now(timezone.utc),
            status="running",
            trigger="manual",
            boards_collected=0,
            new_meetings_found=0,
            new_documents_found=0,
            boards_summarized=0,
        )
        session.add(run)
        await session.commit()
        await session.refresh(run)
        assert run.id is not None
        assert run.status == "running"
        assert run.completed_at is None


@pytest.mark.asyncio
async def test_pipeline_event_belongs_to_run():
    async with db.async_session() as session:
        run = PipelineRun(
            started_at=datetime.now(timezone.utc),
            status="running",
            trigger="manual",
            boards_collected=0,
            new_meetings_found=0,
            new_documents_found=0,
            boards_summarized=0,
        )
        session.add(run)
        await session.commit()
        await session.refresh(run)

        event = PipelineEvent(
            run_id=run.id,
            timestamp=datetime.now(timezone.utc),
            stage="collect",
            board_code="TX_MD",
            event_type="new_meeting",
            detail="Found meeting 2026-03-15",
        )
        session.add(event)
        await session.commit()
        await session.refresh(event)
        assert event.run_id == run.id
        assert event.stage == "collect"


@pytest.mark.asyncio
async def test_meeting_pipeline_run_id():
    async with db.async_session() as session:
        board = Board(
            state="TX", code="TX_MD", name="Texas Board",
            board_type="combined", homepage="https://tmb.state.tx.us",
            discovery_status="found",
        )
        session.add(board)
        await session.commit()
        await session.refresh(board)

        run = PipelineRun(
            started_at=datetime.now(timezone.utc),
            status="running",
            trigger="manual",
            boards_collected=0,
            new_meetings_found=0,
            new_documents_found=0,
            boards_summarized=0,
        )
        session.add(run)
        await session.commit()
        await session.refresh(run)

        meeting = Meeting(
            board_id=board.id,
            meeting_date=date(2026, 3, 15),
            title="March Meeting",
            pipeline_run_id=run.id,
        )
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)
        assert meeting.pipeline_run_id == run.id


@pytest.mark.asyncio
async def test_meeting_document_topics():
    async with db.async_session() as session:
        board = Board(
            state="TX", code="TX_MD", name="Texas Board",
            board_type="combined", homepage="https://tmb.state.tx.us",
            discovery_status="found",
        )
        session.add(board)
        await session.commit()
        await session.refresh(board)

        meeting = Meeting(
            board_id=board.id,
            meeting_date=date(2026, 3, 15),
            title="March Meeting",
        )
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)

        doc = MeetingDocument(
            meeting_id=meeting.id,
            doc_type="minutes",
            filename="march_minutes.pdf",
            file_path="data/documents/TX_MD/march_minutes.pdf",
            topics=["licensing", "telehealth", "AI"],
        )
        session.add(doc)
        await session.commit()
        await session.refresh(doc)
        assert doc.topics == ["licensing", "telehealth", "AI"]
