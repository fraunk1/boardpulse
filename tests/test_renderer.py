"""Test PDF page renderer."""
import pytest
from datetime import date, datetime, timezone
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage
from app.pipeline.renderer import render_document_pages


@pytest.fixture(autouse=True)
async def setup_db(tmp_path):
    await db.init_db(url="sqlite+aiosqlite://")
    yield


def _create_test_pdf(path: Path, num_pages: int = 3):
    import fitz
    doc = fitz.open()
    for _ in range(num_pages):
        doc.new_page(width=612, height=792)
    doc.save(str(path))
    doc.close()


@pytest.mark.asyncio
async def test_render_document_pages(tmp_path):
    pdf_path = tmp_path / "documents" / "TX_MD" / "march.pdf"
    pdf_path.parent.mkdir(parents=True)
    _create_test_pdf(pdf_path, num_pages=3)

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
                              filename="march.pdf", file_path=str(pdf_path))
        session.add(doc)
        await session.commit()
        await session.refresh(doc)

    pages_dir = tmp_path / "pages"
    result = await render_document_pages(doc.id, pages_dir=pages_dir)

    assert result["pages_rendered"] == 3
    assert result["document_id"] == doc.id

    doc_pages_dir = pages_dir / "TX_MD" / str(doc.id)
    assert (doc_pages_dir / "page_001.png").exists()
    assert (doc_pages_dir / "page_001_thumb.png").exists()
    assert (doc_pages_dir / "page_003.png").exists()
    assert (doc_pages_dir / "page_003_thumb.png").exists()

    full_size = (doc_pages_dir / "page_001.png").stat().st_size
    thumb_size = (doc_pages_dir / "page_001_thumb.png").stat().st_size
    assert thumb_size < full_size

    from sqlalchemy import select, func
    async with db.async_session() as session:
        count = (await session.execute(
            select(func.count(DocumentPage.id))
            .where(DocumentPage.document_id == doc.id)
        )).scalar()
        assert count == 3


@pytest.mark.asyncio
async def test_render_skips_already_rendered(tmp_path):
    pdf_path = tmp_path / "documents" / "TX_MD" / "march.pdf"
    pdf_path.parent.mkdir(parents=True)
    _create_test_pdf(pdf_path, num_pages=2)

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
                              filename="march.pdf", file_path=str(pdf_path))
        session.add(doc)
        await session.commit()
        await session.refresh(doc)

    pages_dir = tmp_path / "pages"

    r1 = await render_document_pages(doc.id, pages_dir=pages_dir)
    assert r1["pages_rendered"] == 2

    r2 = await render_document_pages(doc.id, pages_dir=pages_dir)
    assert r2["pages_rendered"] == 0
    assert r2["skipped"] is True
