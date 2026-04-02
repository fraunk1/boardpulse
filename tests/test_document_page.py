"""Test DocumentPage model."""
import pytest
from datetime import date, datetime, timezone

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage


@pytest.fixture(autouse=True)
async def setup_db(tmp_path):
    await db.init_db(url="sqlite+aiosqlite://")
    yield


@pytest.mark.asyncio
async def test_create_document_page():
    async with db.async_session() as session:
        board = Board(state="TX", code="TX_MD", name="Texas Board",
                      board_type="combined", homepage="https://tmb.state.tx.us",
                      discovery_status="found")
        session.add(board)
        await session.commit()
        await session.refresh(board)

        meeting = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15),
                          title="March Meeting")
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)

        doc = MeetingDocument(meeting_id=meeting.id, doc_type="minutes",
                              filename="march.pdf", file_path="data/documents/TX_MD/march.pdf")
        session.add(doc)
        await session.commit()
        await session.refresh(doc)

        page = DocumentPage(
            document_id=doc.id,
            page_number=1,
            image_path="data/pages/TX_MD/1/page_001.png",
            thumb_path="data/pages/TX_MD/1/page_001_thumb.png",
            rendered_at=datetime.now(timezone.utc),
        )
        session.add(page)
        await session.commit()
        await session.refresh(page)
        assert page.id is not None
        assert page.page_number == 1
        assert page.topics is None


@pytest.mark.asyncio
async def test_document_page_with_topics():
    async with db.async_session() as session:
        board = Board(state="FL", code="FL_MD", name="Florida Board",
                      board_type="combined", homepage="https://flboardofmedicine.gov",
                      discovery_status="found")
        session.add(board)
        await session.commit()
        await session.refresh(board)

        meeting = Meeting(board_id=board.id, meeting_date=date(2026, 3, 20),
                          title="March Meeting")
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)

        doc = MeetingDocument(meeting_id=meeting.id, doc_type="minutes",
                              filename="march.pdf", file_path="data/documents/FL_MD/march.pdf")
        session.add(doc)
        await session.commit()
        await session.refresh(doc)

        page = DocumentPage(
            document_id=doc.id, page_number=3,
            image_path="data/pages/FL_MD/1/page_003.png",
            thumb_path="data/pages/FL_MD/1/page_003_thumb.png",
            topics=["telehealth", "AI"],
            tagged_at=datetime.now(timezone.utc),
            rendered_at=datetime.now(timezone.utc),
        )
        session.add(page)
        await session.commit()
        await session.refresh(page)
        assert page.topics == ["telehealth", "AI"]
        assert page.tagged_at is not None


@pytest.mark.asyncio
async def test_document_pages_relationship():
    async with db.async_session() as session:
        board = Board(state="OH", code="OH_MD", name="Ohio Board",
                      board_type="combined", homepage="https://med.ohio.gov",
                      discovery_status="found")
        session.add(board)
        await session.commit()
        await session.refresh(board)

        meeting = Meeting(board_id=board.id, meeting_date=date(2026, 1, 15),
                          title="Jan Meeting")
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)

        doc = MeetingDocument(meeting_id=meeting.id, doc_type="minutes",
                              filename="jan.pdf", file_path="data/documents/OH_MD/jan.pdf")
        session.add(doc)
        await session.commit()
        await session.refresh(doc)

        now = datetime.now(timezone.utc)
        for i in range(1, 4):
            page = DocumentPage(
                document_id=doc.id, page_number=i,
                image_path=f"data/pages/OH_MD/{doc.id}/page_{i:03d}.png",
                thumb_path=f"data/pages/OH_MD/{doc.id}/page_{i:03d}_thumb.png",
                rendered_at=now,
            )
            session.add(page)
        await session.commit()

    from sqlalchemy import select, func
    async with db.async_session() as session:
        count = (await session.execute(
            select(func.count(DocumentPage.id))
            .where(DocumentPage.document_id == doc.id)
        )).scalar()
        assert count == 3
