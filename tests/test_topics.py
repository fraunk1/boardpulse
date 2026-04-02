"""Test topic ingestion from JSON files."""
import json
import pytest
from datetime import date

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import database as db
from app.models import Board, Meeting, MeetingDocument
from app.pipeline.topics import ingest_topics_from_file


@pytest.fixture(autouse=True)
async def setup_db(tmp_path):
    await db.init_db(url="sqlite+aiosqlite://")
    yield


@pytest.mark.asyncio
async def test_ingest_topics_from_file(tmp_path):
    """Ingest topics JSON: sets MeetingDocument.topics and rolls up to Meeting.topics."""
    async with db.async_session() as session:
        board = Board(
            state="FL", code="FL_MD", name="Florida Board",
            board_type="combined", homepage="https://flboardofmedicine.gov",
            discovery_status="found",
        )
        session.add(board)
        await session.commit()
        await session.refresh(board)

        meeting = Meeting(board_id=board.id, meeting_date=date(2026, 3, 20), title="March")
        session.add(meeting)
        await session.commit()
        await session.refresh(meeting)

        doc1 = MeetingDocument(
            meeting_id=meeting.id, doc_type="agenda",
            filename="agenda.pdf", file_path="data/documents/FL_MD/agenda.pdf",
        )
        doc2 = MeetingDocument(
            meeting_id=meeting.id, doc_type="minutes",
            filename="minutes.pdf", file_path="data/documents/FL_MD/minutes.pdf",
        )
        session.add_all([doc1, doc2])
        await session.commit()
        await session.refresh(doc1)
        await session.refresh(doc2)

    # Write topics JSON
    topics_file = tmp_path / "run_1_topics.json"
    topics_data = {
        str(doc1.id): ["licensing", "telehealth"],
        str(doc2.id): ["licensing", "disciplinary", "AI"],
    }
    topics_file.write_text(json.dumps(topics_data))

    result = await ingest_topics_from_file(topics_file)
    assert result["documents_tagged"] == 2

    # Verify document-level topics
    async with db.async_session() as session:
        d1 = await session.get(MeetingDocument, doc1.id)
        d2 = await session.get(MeetingDocument, doc2.id)
        assert set(d1.topics) == {"licensing", "telehealth"}
        assert set(d2.topics) == {"licensing", "disciplinary", "AI"}

        # Verify meeting-level rollup
        m = await session.get(Meeting, meeting.id)
        assert set(m.topics) == {"licensing", "telehealth", "disciplinary", "AI"}


@pytest.mark.asyncio
async def test_ingest_topics_skips_missing_documents(tmp_path):
    """Ingestion skips document IDs that don't exist in DB."""
    topics_file = tmp_path / "run_1_topics.json"
    topics_data = {"9999": ["licensing"]}
    topics_file.write_text(json.dumps(topics_data))

    result = await ingest_topics_from_file(topics_file)
    assert result["documents_tagged"] == 0
