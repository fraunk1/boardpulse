"""Test database models and relationships."""
import pytest
from datetime import date, datetime

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import database as db
from app.models import Board, Meeting, MeetingDocument


@pytest.fixture(autouse=True)
async def setup_db(tmp_path):
    """Initialize a fresh in-memory DB for each test."""
    await db.init_db(url="sqlite+aiosqlite://")
    yield


@pytest.mark.asyncio
async def test_create_board():
    async with db.async_session() as session:
        board = Board(
            state="CA",
            code="CA_MD",
            name="Medical Board of California",
            board_type="combined",
            homepage="https://www.mbc.ca.gov",
            discovery_status="pending",
        )
        session.add(board)
        await session.commit()
        await session.refresh(board)
        assert board.id is not None
        assert board.code == "CA_MD"


@pytest.mark.asyncio
async def test_board_code_unique():
    async with db.async_session() as session:
        b1 = Board(state="CA", code="CA_MD", name="Board 1", board_type="combined",
                    homepage="https://example.com", discovery_status="pending")
        session.add(b1)
        await session.commit()

    from sqlalchemy.exc import IntegrityError
    with pytest.raises(IntegrityError):
        async with db.async_session() as session:
            b2 = Board(state="CA", code="CA_MD", name="Board 2", board_type="combined",
                        homepage="https://example2.com", discovery_status="pending")
            session.add(b2)
            await session.commit()


@pytest.mark.asyncio
async def test_meeting_belongs_to_board():
    async with db.async_session() as session:
        board = Board(state="OH", code="OH_MD", name="Ohio Board",
                      board_type="combined", homepage="https://med.ohio.gov",
                      discovery_status="found")
        session.add(board)
        await session.commit()
        await session.refresh(board)

        meeting = Meeting(
            board_id=board.id,
            meeting_date=date(2026, 1, 15),
            title="January Board Meeting",
            meeting_type="regular",
            source_url="https://med.ohio.gov/meetings/jan2026",
        )
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)
        assert meeting.board_id == board.id


@pytest.mark.asyncio
async def test_meeting_document_belongs_to_meeting():
    async with db.async_session() as session:
        board = Board(state="TX", code="TX_MD", name="Texas Board",
                      board_type="combined", homepage="https://tmb.state.tx.us",
                      discovery_status="found")
        session.add(board)
        await session.commit()
        await session.refresh(board)

        meeting = Meeting(board_id=board.id, meeting_date=date(2026, 2, 10),
                          title="February Meeting", meeting_type="regular",
                          source_url="https://tmb.state.tx.us/meetings")
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)

        doc = MeetingDocument(
            meeting_id=meeting.id,
            doc_type="minutes",
            filename="feb2026_minutes.pdf",
            file_path="data/documents/TX_MD/feb2026_minutes.pdf",
            source_url="https://tmb.state.tx.us/docs/feb2026.pdf",
        )
        session.add(doc)
        await session.commit()
        await session.refresh(doc)
        assert doc.meeting_id == meeting.id
        assert doc.doc_type == "minutes"
