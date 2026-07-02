"""Route smoke tests — temp DB, real app, key markers per page."""
import asyncio
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture(scope="module")
def client_and_ids(tmp_path_factory):
    """One seeded temp DB + one TestClient for the whole module.

    Module-scoped on purpose: server.py holds module-level TTL caches
    (national stats, report HTML) — one DB per module avoids cross-test
    cache bleed.
    """
    import app.database as db

    tmp_path = tmp_path_factory.mktemp("webdb")
    db.DATABASE_URL = f"sqlite+aiosqlite:///{(tmp_path / 't.db').as_posix()}"

    async def seed():
        await db.init_db()
        from app.models import Board, Meeting

        async with db.async_session() as s:
            board = Board(
                state="XX", code="XX_MD", name="Test Medical Board",
                board_type="MD", homepage="https://example.gov",
                discovery_status="manual",
                summary="BOARD ROLLUP: a year of test meetings.",
                summarized_at=datetime.now(timezone.utc),
            )
            s.add(board)
            await s.flush()
            m1 = Meeting(
                board_id=board.id,
                meeting_date=date.today() - timedelta(days=10),
                title="Recent Meeting",
                summary="MEETING SUMMARY: rule 540-X-1 adopted.",
                topics=["licensing"],
                summarized_at=datetime.now(timezone.utc),
            )
            m2 = Meeting(
                board_id=board.id,
                meeting_date=date.today() - timedelta(days=40),
                title="Textless Meeting",
            )
            s.add_all([m1, m2])
            await s.commit()
            return m1.id, m2.id

    m1_id, m2_id = asyncio.run(seed())

    from fastapi.testclient import TestClient
    from app.web import server

    with TestClient(server.app) as client:
        yield client, m1_id, m2_id


def test_home(client_and_ids):
    client, *_ = client_and_ids
    r = client.get("/")
    assert r.status_code == 200
    assert "boardpulse" in r.text


def test_boards_directory(client_and_ids):
    client, *_ = client_and_ids
    r = client.get("/boards")
    assert r.status_code == 200
    assert "XX_MD" in r.text
    assert "Test Medical Board" in r.text


def test_state_page(client_and_ids):
    client, *_ = client_and_ids
    r = client.get("/state/XX")
    assert r.status_code == 200
    assert "Test Medical Board" in r.text


def test_board_page_shows_rollup(client_and_ids):
    client, *_ = client_and_ids
    r = client.get("/board/XX_MD")
    assert r.status_code == 200
    assert "BOARD ROLLUP" in r.text
    assert "12-month rollup" in r.text


def test_meeting_page_shows_own_summary_and_board_context(client_and_ids):
    client, m1_id, _ = client_and_ids
    r = client.get(f"/meeting/{m1_id}")
    assert r.status_code == 200
    assert "Meeting AI Summary" in r.text
    assert "MEETING SUMMARY: rule 540-X-1" in r.text
    assert "Board context" in r.text
    assert "BOARD ROLLUP" in r.text
    # the old misleading framing must be gone
    assert "12-month view" not in r.text


def test_textless_meeting_shows_board_context_only(client_and_ids):
    client, _, m2_id = client_and_ids
    r = client.get(f"/meeting/{m2_id}")
    assert r.status_code == 200
    assert "Meeting AI Summary" not in r.text
    assert "Board context" in r.text
    # accordion initializes OPEN when the meeting has no summary
    assert "boardContextOpen: true" in r.text


def test_topic_page_lists_matching_meeting(client_and_ids):
    client, *_ = client_and_ids
    r = client.get("/topic/licensing")
    assert r.status_code == 200
    assert "Recent Meeting" in r.text


def test_topic_page_excludes_non_matching(client_and_ids):
    client, *_ = client_and_ids
    r = client.get("/topic/telehealth")
    assert r.status_code == 200
    assert "Recent Meeting" not in r.text


def test_404s(client_and_ids):
    client, *_ = client_and_ids
    assert client.get("/board/NOPE_MD").status_code == 404
    assert client.get("/meeting/999999").status_code == 404
