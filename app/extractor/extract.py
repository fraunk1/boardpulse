"""Extract text from all collected documents that don't have content_text yet."""
from pathlib import Path

from sqlalchemy import select

import app.database as db
from app.models import MeetingDocument
from app.extractor.parser import extract_text_from_file


async def extract_all():
    """Run text extraction on all documents missing content_text."""
    await db.init_db()

    async with db.async_session() as session:
        result = await session.execute(
            select(MeetingDocument).where(MeetingDocument.content_text.is_(None))
        )
        docs = list(result.scalars().all())

    if not docs:
        print("No documents need text extraction.")
        return

    print(f"Extracting text from {len(docs)} documents...")
    success = 0
    failed = 0

    for doc in docs:
        file_path = Path(doc.file_path)
        text = extract_text_from_file(file_path)
        if text:
            async with db.async_session() as session:
                db_doc = await session.get(MeetingDocument, doc.id)
                db_doc.content_text = text
                await session.commit()
            success += 1
        else:
            failed += 1
            print(f"  Failed: {doc.filename}")

    print(f"Extraction complete: {success} succeeded, {failed} failed")
