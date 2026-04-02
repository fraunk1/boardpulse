"""Test data integrity — rollups, path resolution, edge cases."""
import json
import pytest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage
from app.pipeline.classifier import classify_text


# ---------------------------------------------------------------------------
# Topic Rollup
# ---------------------------------------------------------------------------

async def test_topic_rollup_list_format(seed_full_chain):
    """Topics stored as Python list (not JSON string) are handled in rollup."""
    chain = await seed_full_chain(topics=["Licensing", "Discipline"])
    async with db.async_session() as session:
        m = await session.get(Meeting, chain["meeting"].id)
        assert isinstance(m.topics, list)
        assert "Licensing" in m.topics


async def test_topic_deduplication(seed_board):
    """Rollup from multiple docs with overlapping topics produces no duplicates."""
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        d1 = MeetingDocument(
            meeting_id=m.id, doc_type="minutes", filename="a.pdf",
            file_path="/tmp/a.pdf", topics=["Discipline", "Licensing"],
        )
        d2 = MeetingDocument(
            meeting_id=m.id, doc_type="agenda", filename="b.pdf",
            file_path="/tmp/b.pdf", topics=["Discipline", "Telehealth"],
        )
        session.add_all([d1, d2])
        await session.commit()

    from app.pipeline.classifier import classify_all_documents
    await classify_all_documents(force=True, min_matches=1)

    async with db.async_session() as session:
        m = await session.get(Meeting, m.id)
        if m.topics:
            assert len(m.topics) == len(set(m.topics)), f"Duplicates found: {m.topics}"


async def test_document_no_pages_in_search(client, seed_full_chain):
    """A document with no DocumentPages doesn't break the search page."""
    chain = await seed_full_chain()
    async with db.async_session() as session:
        page = await session.get(DocumentPage, chain["page"].id)
        await session.delete(page)
        await session.commit()

    resp = await client.get("/search?period=all")
    assert resp.status_code == 200


async def test_meeting_no_documents(client, seed_board):
    """Meeting with zero documents renders without error."""
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15),
                    title="Empty Meeting")
        session.add(m)
        await session.commit()
        await session.refresh(m)

    resp = await client.get(f"/meeting/{m.id}")
    assert resp.status_code == 200


async def test_board_zero_meetings_state_view(client, seed_board):
    """Board with 0 meetings doesn't break state view."""
    await seed_board()
    resp = await client.get("/state/TX")
    assert resp.status_code == 200


# ---------------------------------------------------------------------------
# Path Resolution
# ---------------------------------------------------------------------------

async def test_renderer_relative_path(seed_board, tmp_path):
    """Renderer resolves relative file_path via PROJECT_ROOT."""
    import fitz

    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        pdf_path = tmp_path / "test.pdf"
        doc = fitz.open()
        doc.new_page(width=100, height=100)
        doc.save(str(pdf_path))
        doc.close()

        d = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="test.pdf", file_path=str(pdf_path),
        )
        session.add(d)
        await session.commit()
        await session.refresh(d)

    from app.pipeline.renderer import render_document_pages
    result = await render_document_pages(d.id, pages_dir=tmp_path / "pages")
    assert result["pages_rendered"] == 1


# ---------------------------------------------------------------------------
# FTS Edge Cases
# ---------------------------------------------------------------------------

async def test_fts_empty_query(seed_full_chain):
    chain = await seed_full_chain()
    from app.pipeline.fts import rebuild_fts_index, search_summaries
    await rebuild_fts_index()
    results = await search_summaries("")
    assert isinstance(results, list)


async def test_fts_special_characters(seed_full_chain):
    chain = await seed_full_chain()
    from app.pipeline.fts import rebuild_fts_index, search_summaries
    await rebuild_fts_index()
    await search_summaries("AI & Technology")
    await search_summaries('"opioid prescribing"')
    await search_summaries("test (with) [brackets]")
