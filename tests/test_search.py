"""Full-text search + ops status page tests — temp DB, real app."""
import asyncio
import sqlite3
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture(scope="module")
def client_and_ids(tmp_path_factory):
    """One seeded temp DB + one TestClient for the whole module.

    Module-scoped on purpose, matching tests/test_web.py: server.py holds
    module-level TTL caches — one DB per module avoids cross-test cache bleed.
    """
    import app.database as db

    tmp_path = tmp_path_factory.mktemp("searchdb")
    db_path = tmp_path / "t.db"
    db.DATABASE_URL = f"sqlite+aiosqlite:///{db_path.as_posix()}"

    async def seed():
        await db.init_db()
        from app.models import Board, Meeting, MeetingDocument

        async with db.async_session() as s:
            board = Board(
                state="XX", code="XX_MD", name="Test Medical Board",
                board_type="MD", homepage="https://example.gov",
                discovery_status="manual",
            )
            s.add(board)
            await s.flush()
            m1 = Meeting(
                board_id=board.id,
                meeting_date=date.today(),
                title="Regular Session",
                scraped_at=datetime.now(timezone.utc),
            )
            s.add(m1)
            await s.flush()
            doc = MeetingDocument(
                meeting_id=m1.id,
                doc_type="minutes",
                filename="minutes.pdf",
                file_path="minutes.pdf",
                content_text=(
                    "The board discussed the telehealth pilot program and "
                    "voted to extend it through the next fiscal year."
                ),
            )
            s.add(doc)
            await s.commit()
            return m1.id

    m1_id = asyncio.run(seed())
    # seed() ran in its own (now-closed) loop; drop that loop's pooled
    # connections before the TestClient loop takes over the engine.
    asyncio.run(db.engine.dispose())

    # init_db()'s first-startup FTS population runs inside the SAME engine.begin()
    # transaction that creates the schema — before the seed data above exists.
    # So explicitly rebuild the FTS index here after seeding, via a plain
    # sync sqlite3 connection (mirrors refresh.py's rebuild_fts_index()).
    con = sqlite3.connect(db_path)
    con.execute(
        "CREATE VIRTUAL TABLE IF NOT EXISTS doc_fts USING fts5("
        "content_text, content='meeting_documents', content_rowid='id')")
    con.execute("INSERT INTO doc_fts(doc_fts) VALUES('rebuild')")
    con.commit()
    con.close()

    from fastapi.testclient import TestClient
    from app.web import server

    with TestClient(server.app) as client:
        yield client, m1_id

    # ...and drop the connections the app created on the TestClient's loop.
    asyncio.run(db.engine.dispose())


def test_search_finds_highlighted_result(client_and_ids):
    client, m1_id = client_and_ids
    r = client.get("/search", params={"q": "telehealth"})
    assert r.status_code == 200
    assert "<mark>" in r.text
    assert f"/meeting/{m1_id}" in r.text


def test_search_unbalanced_quote_no_500(client_and_ids):
    client, _ = client_and_ids
    r = client.get("/search", params={"q": '"unbalanced'})
    assert r.status_code == 200


def test_search_empty_query(client_and_ids):
    client, _ = client_and_ids
    r = client.get("/search")
    assert r.status_code == 200


def test_ops_page_shows_seeded_board(client_and_ids):
    client, _ = client_and_ids
    r = client.get("/ops")
    assert r.status_code == 200
    assert "XX_MD" in r.text
