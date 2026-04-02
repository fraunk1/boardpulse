"""Test page-level topic ingestion."""
import json
import pytest
from datetime import date, datetime, timezone

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage
from app.pipeline.topics import ingest_page_topics_from_file


@pytest.fixture
async def sample_data():
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
                              filename="march.pdf",
                              file_path="data/documents/TX_MD/march.pdf")
        session.add(doc)
        await session.commit()
        await session.refresh(doc)

        now = datetime.now(timezone.utc)
        pages = []
        for i in range(1, 4):
            p = DocumentPage(
                document_id=doc.id, page_number=i,
                image_path=f"p{i}.png", thumb_path=f"p{i}_t.png",
                rendered_at=now,
            )
            session.add(p)
            pages.append(p)
        await session.commit()
        for p in pages:
            await session.refresh(p)

    return {"board": board, "meeting": meeting, "doc": doc, "pages": pages}


@pytest.mark.asyncio
async def test_ingest_page_topics(tmp_path, sample_data):
    doc = sample_data["doc"]
    pages = sample_data["pages"]

    topics_file = tmp_path / "topics.json"
    topics_data = {
        f"document_{doc.id}": {
            "1": ["licensing"],
            "3": ["telehealth", "AI"],
        }
    }
    topics_file.write_text(json.dumps(topics_data))

    result = await ingest_page_topics_from_file(topics_file)
    assert result["pages_tagged"] == 2

    async with db.async_session() as session:
        p1 = await session.get(DocumentPage, pages[0].id)
        p2 = await session.get(DocumentPage, pages[1].id)
        p3 = await session.get(DocumentPage, pages[2].id)
        assert p1.topics == ["licensing"]
        assert p2.topics is None
        assert set(p3.topics) == {"telehealth", "AI"}

        d = await session.get(MeetingDocument, doc.id)
        assert set(d.topics) == {"licensing", "telehealth", "AI"}

        m = await session.get(Meeting, sample_data["meeting"].id)
        assert set(m.topics) == {"licensing", "telehealth", "AI"}


@pytest.mark.asyncio
async def test_ingest_page_topics_skips_unknown_docs(tmp_path):
    topics_file = tmp_path / "topics.json"
    topics_data = {"document_99999": {"1": ["licensing"]}}
    topics_file.write_text(json.dumps(topics_data))

    result = await ingest_page_topics_from_file(topics_file)
    assert result["pages_tagged"] == 0
