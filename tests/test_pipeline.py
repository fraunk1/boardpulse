"""Test pipeline data models."""
import pytest
from datetime import date, datetime, timezone

from app import database as db
from app.models import Board, Meeting, MeetingDocument, PipelineRun, PipelineEvent


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


from app.pipeline.delta import snapshot_board_counts, compute_delta


@pytest.mark.asyncio
async def test_snapshot_board_counts():
    """Snapshot returns {board_code: {meetings: N, documents: N}} for all boards."""
    async with db.async_session() as session:
        board = Board(
            state="OH", code="OH_MD", name="Ohio Board",
            board_type="combined", homepage="https://med.ohio.gov",
            discovery_status="found",
        )
        session.add(board)
        await session.commit()
        await session.refresh(board)

        m = Meeting(board_id=board.id, meeting_date=date(2026, 1, 15), title="Jan")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        doc = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="jan.pdf", file_path="data/documents/OH_MD/jan.pdf",
        )
        session.add(doc)
        await session.commit()

    snap = await snapshot_board_counts()
    assert "OH_MD" in snap
    assert snap["OH_MD"]["meetings"] == 1
    assert snap["OH_MD"]["documents"] == 1


@pytest.mark.asyncio
async def test_compute_delta():
    """Delta shows differences between two snapshots."""
    before = {"TX_MD": {"meetings": 5, "documents": 8}}
    after = {"TX_MD": {"meetings": 7, "documents": 11}, "FL_MD": {"meetings": 2, "documents": 3}}

    delta = compute_delta(before, after)
    assert delta["TX_MD"]["new_meetings"] == 2
    assert delta["TX_MD"]["new_documents"] == 3
    assert delta["FL_MD"]["new_meetings"] == 2
    assert delta["FL_MD"]["new_documents"] == 3


@pytest.mark.asyncio
async def test_compute_delta_no_changes():
    """Delta returns empty dict when nothing changed."""
    snap = {"TX_MD": {"meetings": 5, "documents": 8}}
    delta = compute_delta(snap, snap)
    assert delta == {}


from app.pipeline.context import generate_context_file


@pytest.mark.asyncio
async def test_generate_context_file(tmp_path):
    """Context file contains delta info and instructions."""
    async with db.async_session() as session:
        board = Board(
            state="TX", code="TX_MD", name="Texas Medical Board",
            board_type="combined", homepage="https://tmb.state.tx.us",
            discovery_status="found",
        )
        session.add(board)
        await session.commit()
        await session.refresh(board)

        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March Meeting")
        session.add(m)
        await session.commit()

    delta = {"TX_MD": {"new_meetings": 1, "new_documents": 2}}
    no_change = ["AL_MD", "CA_MD"]

    output_path = tmp_path / "run_1_context.md"
    await generate_context_file(
        run_id=1,
        delta=delta,
        no_change_boards=no_change,
        output_path=output_path,
        reports_dir=tmp_path,
    )

    content = output_path.read_text()
    assert "Pipeline Run #1" in content
    assert "TX_MD" in content
    assert "Texas Medical Board" in content
    assert "1 new meeting" in content
    assert "AL_MD" in content
    assert "Instructions" in content
