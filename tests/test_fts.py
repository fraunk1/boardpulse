"""Test FTS5 full-text search index."""
import pytest
from datetime import date

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import database as db
from app.models import Board, Meeting
from app.pipeline.fts import rebuild_fts_index, search_summaries


@pytest.fixture(autouse=True)
async def setup_db(tmp_path):
    await db.init_db(url="sqlite+aiosqlite://")
    yield


@pytest.fixture
async def meetings_with_summaries():
    async with db.async_session() as session:
        board = Board(state="TX", code="TX_MD", name="Texas Board",
                      board_type="combined", homepage="https://tmb.state.tx.us",
                      discovery_status="found")
        session.add(board)
        await session.commit()
        await session.refresh(board)

        m1 = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15),
                     title="March Meeting",
                     summary="The board discussed telehealth prescribing authority and interstate compact agreements.")
        m2 = Meeting(board_id=board.id, meeting_date=date(2026, 2, 15),
                     title="February Meeting",
                     summary="Disciplinary actions were taken against three physicians for opioid violations.")
        m3 = Meeting(board_id=board.id, meeting_date=date(2026, 1, 15),
                     title="January Meeting",
                     summary=None)
        session.add_all([m1, m2, m3])
        await session.commit()
        await session.refresh(m1)
        await session.refresh(m2)
    return {"m1": m1, "m2": m2}


@pytest.mark.asyncio
async def test_rebuild_fts_index(meetings_with_summaries):
    result = await rebuild_fts_index()
    assert result["indexed"] == 2


@pytest.mark.asyncio
async def test_search_summaries(meetings_with_summaries):
    await rebuild_fts_index()

    results = await search_summaries("telehealth prescribing")
    assert len(results) == 1
    assert results[0]["meeting_id"] == meetings_with_summaries["m1"].id

    results2 = await search_summaries("opioid")
    assert len(results2) == 1
    assert results2[0]["meeting_id"] == meetings_with_summaries["m2"].id


@pytest.mark.asyncio
async def test_search_no_results(meetings_with_summaries):
    await rebuild_fts_index()
    results = await search_summaries("cryptocurrency blockchain")
    assert len(results) == 0
