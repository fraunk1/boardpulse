"""Ingest AI-generated topic tags from JSON into the database."""
import json
from pathlib import Path

from sqlalchemy import select

import app.database as db
from app.models import Meeting, MeetingDocument


async def ingest_topics_from_file(topics_path: Path) -> dict:
    """Read a topics JSON file and store tags on MeetingDocument + rollup to Meeting.

    The JSON format is: {"document_id": ["tag1", "tag2"], ...}

    Returns a summary dict with counts.
    """
    data = json.loads(topics_path.read_text(encoding="utf-8"))

    documents_tagged = 0
    meetings_to_rollup: set[int] = set()

    for doc_id_str, tags in data.items():
        doc_id = int(doc_id_str)
        async with db.async_session() as session:
            doc = await session.get(MeetingDocument, doc_id)
            if not doc:
                print(f"  Warning: document {doc_id} not found, skipping")
                continue
            doc.topics = tags
            meetings_to_rollup.add(doc.meeting_id)
            await session.commit()
            documents_tagged += 1

    meetings_rolled = 0
    for meeting_id in meetings_to_rollup:
        async with db.async_session() as session:
            docs = (await session.execute(
                select(MeetingDocument)
                .where(MeetingDocument.meeting_id == meeting_id)
                .where(MeetingDocument.topics.isnot(None))
            )).scalars().all()

            all_topics: set[str] = set()
            for doc in docs:
                tags = doc.topics if isinstance(doc.topics, list) else json.loads(doc.topics or "[]")
                all_topics.update(tags)

            meeting = await session.get(Meeting, meeting_id)
            if meeting:
                meeting.topics = sorted(all_topics)
                await session.commit()
                meetings_rolled += 1

    print(f"  Tagged {documents_tagged} documents, rolled up {meetings_rolled} meetings")
    return {"documents_tagged": documents_tagged, "meetings_rolled_up": meetings_rolled}
