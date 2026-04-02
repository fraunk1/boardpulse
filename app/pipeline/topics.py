"""Ingest AI-generated topic tags from JSON into the database."""
import json
from pathlib import Path

from sqlalchemy import select

import app.database as db
from app.models import Meeting, MeetingDocument, DocumentPage


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


async def ingest_page_topics_from_file(topics_path: Path) -> dict:
    """Read page-level topics JSON and store on DocumentPage + rollup.

    JSON format:
    {
        "document_42": {"1": ["licensing"], "3": ["telehealth", "AI"]},
        "document_43": {"2": ["rulemaking"]}
    }
    """
    from datetime import datetime, timezone

    data = json.loads(topics_path.read_text(encoding="utf-8"))

    pages_tagged = 0
    documents_to_rollup: set[int] = set()
    meetings_to_rollup: set[int] = set()

    for doc_key, page_map in data.items():
        try:
            doc_id = int(doc_key.replace("document_", ""))
        except ValueError:
            print(f"  Warning: invalid document key '{doc_key}', skipping")
            continue

        async with db.async_session() as session:
            doc = await session.get(MeetingDocument, doc_id)
            if not doc:
                print(f"  Warning: document {doc_id} not found, skipping")
                continue
            documents_to_rollup.add(doc_id)
            meetings_to_rollup.add(doc.meeting_id)

        now = datetime.now(timezone.utc)
        for page_num_str, tags in page_map.items():
            page_num = int(page_num_str)
            async with db.async_session() as session:
                page = (await session.execute(
                    select(DocumentPage)
                    .where(DocumentPage.document_id == doc_id)
                    .where(DocumentPage.page_number == page_num)
                )).scalar_one_or_none()

                if not page:
                    print(f"  Warning: page {page_num} of document {doc_id} not found, skipping")
                    continue

                page.topics = tags
                page.tagged_at = now
                await session.commit()
                pages_tagged += 1

    # Rollup: document.topics = union of its pages' topics
    docs_rolled = 0
    for doc_id in documents_to_rollup:
        async with db.async_session() as session:
            pages = (await session.execute(
                select(DocumentPage)
                .where(DocumentPage.document_id == doc_id)
                .where(DocumentPage.topics.isnot(None))
            )).scalars().all()

            all_topics: set[str] = set()
            for p in pages:
                tags = p.topics if isinstance(p.topics, list) else json.loads(p.topics or "[]")
                all_topics.update(tags)

            doc = await session.get(MeetingDocument, doc_id)
            if doc:
                doc.topics = sorted(all_topics)
                await session.commit()
                docs_rolled += 1

    # Rollup: meeting.topics = union of its documents' topics
    meetings_rolled = 0
    for meeting_id in meetings_to_rollup:
        async with db.async_session() as session:
            docs = (await session.execute(
                select(MeetingDocument)
                .where(MeetingDocument.meeting_id == meeting_id)
                .where(MeetingDocument.topics.isnot(None))
            )).scalars().all()

            all_topics: set[str] = set()
            for d in docs:
                tags = d.topics if isinstance(d.topics, list) else json.loads(d.topics or "[]")
                all_topics.update(tags)

            meeting = await session.get(Meeting, meeting_id)
            if meeting:
                meeting.topics = sorted(all_topics)
                await session.commit()
                meetings_rolled += 1

    print(f"  Tagged {pages_tagged} pages, rolled up {docs_rolled} docs, {meetings_rolled} meetings")
    return {
        "pages_tagged": pages_tagged,
        "documents_rolled_up": docs_rolled,
        "meetings_rolled_up": meetings_rolled,
    }
