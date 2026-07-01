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
        async with db.async_session() as session:
            db_doc = await session.get(MeetingDocument, doc.id)
            if text:
                db_doc.content_text = text
                success += 1
            else:
                # Mark permanently-failed extractions (scanned/image PDFs)
                # with an empty string so they are not retried on every
                # refresh run. NULL = "not yet attempted"; "" = "no text".
                # To force a retry: UPDATE meeting_documents
                #   SET content_text = NULL WHERE content_text = ''
                db_doc.content_text = ""
                failed += 1
                print(f"  Failed: {doc.filename}")
            await session.commit()

    print(f"Extraction complete: {success} succeeded, {failed} failed")
