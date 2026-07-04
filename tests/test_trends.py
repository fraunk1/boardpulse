"""Trends dashboard + watchlist tests.

Follows tests/test_web.py exactly: one module-scoped seeded temp DB + one
TestClient, with asyncio.run(db.engine.dispose()) after seeding and after the
yield so no pooled aiosqlite connection is bound to a dead event loop.

The seed deliberately leaves the four FACT tables (policy_actions,
legislation_mentions, disciplinary_actions, emerging_topics) empty — that is
the real-world state until extraction runs — so the fact-section empty-guard
tests exercise the shipped code path, not a special case.
"""
import asyncio
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    """One seeded temp DB + one TestClient for the whole module."""
    import app.database as db

    tmp_path = tmp_path_factory.mktemp("trendsdb")
    db.DATABASE_URL = f"sqlite+aiosqlite:///{(tmp_path / 't.db').as_posix()}"

    async def seed():
        await db.init_db()
        from app.models import Board, Meeting, MeetingDocument

        async with db.async_session() as s:
            board = Board(
                state="XX", code="XX_MD", name="Test Medical Board",
                board_type="MD", homepage="https://example.gov",
                discovery_status="manual",
            )
            board2 = Board(
                state="YY", code="YY_MD", name="Second Medical Board",
                board_type="DO", homepage="https://example2.gov",
                discovery_status="manual",
            )
            board3 = Board(
                state="ZZ", code="ZZ_MD", name="Third Medical Board",
                board_type="MD", homepage="https://example3.gov",
                discovery_status="manual",
            )
            s.add_all([board, board2, board3])
            await s.flush()

            # Three boards all discuss "telehealth" THIS quarter -> should
            # qualify for gaining-traction (>=3 boards). "AI" only on one.
            # Use today itself so the meetings are guaranteed to fall in the
            # CURRENT quarter regardless of how far into the quarter we are
            # (a fixed days-ago offset can cross the quarter boundary early
            # in a quarter and silently drop these out of "this quarter").
            today = date.today()
            recent = today
            m1 = Meeting(board_id=board.id, meeting_date=recent,
                         title="Board A recent", topics=["telehealth", "AI"])
            m2 = Meeting(board_id=board2.id, meeting_date=recent,
                         title="Board B recent", topics=["telehealth"])
            m3 = Meeting(board_id=board3.id, meeting_date=recent,
                         title="Board C recent", topics=["telehealth"])
            # An older meeting (prior year) so topics-over-time has >1 quarter
            # of data and licensing is clearly not a "new this quarter" topic.
            m_old = Meeting(board_id=board.id,
                            meeting_date=today - timedelta(days=200),
                            title="Board A old", topics=["licensing"])
            s.add_all([m1, m2, m3, m_old])
            await s.flush()

            # A document with searchable text so watchlist FTS counts work.
            doc = MeetingDocument(
                meeting_id=m1.id, doc_type="minutes",
                filename="min.pdf", file_path="XX_MD/min.pdf",
                content_text="The board discussed telehealth licensure at length.",
                scraped_at=datetime.now(timezone.utc),
            )
            s.add(doc)
            await s.commit()
            # rebuild FTS so the watchlist query sees the doc
            await s.execute(
                __import__("sqlalchemy").text(
                    "INSERT INTO doc_fts(doc_fts) VALUES('rebuild')"))
            await s.commit()
            return board.code

    board_code = asyncio.run(seed())
    asyncio.run(db.engine.dispose())

    from fastapi.testclient import TestClient
    from app.web import server

    with TestClient(server.app) as c:
        # expose the seeded board code for board-page tests
        c.seeded_board_code = board_code
        yield c

    asyncio.run(db.engine.dispose())


# ---------------------------------------------------------------------------
# /trends smoke — 200 + the five anchored section markers render
# ---------------------------------------------------------------------------

def test_trends_smoke(client):
    r = client.get("/trends")
    assert r.status_code == 200
    body = r.text
    # all five anchored sections present
    for anchor in ("emerging", "topics", "rulemaking", "legislation", "discipline"):
        assert f'id="{anchor}"' in body
    # discipline caveat line is present verbatim
    assert "reporting practices differ by state" in body
    # ApexCharts is loaded on this page (vendored, offline)
    assert "/static/vendor/apexcharts.min.js" in body


# ---------------------------------------------------------------------------
# Gaining-traction shape on the seeded DB
# ---------------------------------------------------------------------------

def test_gaining_traction_shape(client):
    """telehealth is discussed by 3 boards this quarter -> a card; the page
    shows the topic and its 'New this quarter' gold badge (no prior-year data
    for it in the seed)."""
    r = client.get("/trends")
    assert r.status_code == 200
    body = r.text
    # telehealth reached 3 boards this quarter -> present as a gaining card
    assert "Telehealth" in body
    # it's new (no prior quarters in seed) -> gold badge text present
    assert "New this quarter" in body


def test_gaining_traction_function_direct(client):
    """Call the trend function directly to assert the returned card shape."""
    import app.web.trends as trends
    cards = asyncio.run(trends.gaining_traction(limit=6))
    telehealth = [c for c in cards if c["topic"] == "telehealth"]
    assert telehealth, "telehealth should qualify (3 boards this quarter)"
    card = telehealth[0]
    assert card["boards"] >= 3
    assert set(card.keys()) == {"topic", "boards", "mentions", "is_new"}
    assert card["is_new"] is True
    # AI is only on one board -> must NOT appear
    assert not any(c["topic"] == "AI" for c in cards)


# ---------------------------------------------------------------------------
# Fact-section empty guards — tables are empty, sections still render
# ---------------------------------------------------------------------------

def test_fact_sections_empty_guard(client):
    """With the fact tables empty, /trends must render the 'Not yet extracted'
    state for rulemaking / legislation / discipline without error."""
    r = client.get("/trends")
    assert r.status_code == 200
    assert "Not yet extracted" in r.text


def test_fact_functions_return_empty_flags(client):
    import app.web.trends as trends
    rulemaking = asyncio.run(trends.rulemaking_pipeline())
    legislation = asyncio.run(trends.legislation_table())
    discipline = asyncio.run(trends.discipline_trends())
    emerging = asyncio.run(trends.emerging_national())
    assert rulemaking["has_data"] is False
    assert legislation["has_data"] is False
    assert discipline["has_data"] is False
    assert emerging["has_data"] is False
    # empty payloads are still well-formed for the template
    assert rulemaking["pipeline"] == []
    assert legislation["rows"] == []
    assert discipline["category_series"] == []
    assert emerging["items"] == []


def test_national_page_renders_watchlist_and_emerging(client):
    """National page must render the watchlist card and the empty-guarded
    emerging feed without error."""
    r = client.get("/")
    assert r.status_code == 200
    body = r.text
    assert 'id="watchlist-card"' in body
    assert "Emerging Issues" in body
    # emerging feed empty-guard copy (fact table is empty)
    assert "No emerging issues extracted yet" in body


# ---------------------------------------------------------------------------
# Watchlist add / seen / delete round-trip
# ---------------------------------------------------------------------------

def test_watchlist_seeded(client):
    """Startup seeds the four default terms when the table is empty."""
    r = client.get("/")
    assert r.status_code == 200
    body = r.text
    for label in ("Telehealth", "Licensure Compact", "Scope of Practice"):
        assert label in body


def test_watchlist_add_seen_delete_roundtrip(client):
    # ADD a new term
    r = client.post("/watchlist", data={"term": "opioids"})
    assert r.status_code == 200
    assert "Opioids" in r.text  # label title-cased
    assert 'id="watchlist-card"' in r.text  # returns the card partial

    # find its id from the DB
    import app.database as db
    from app.models import WatchlistTerm
    from sqlalchemy import select

    async def _find(term):
        async with db.async_session() as s:
            row = (await s.execute(
                select(WatchlistTerm).where(WatchlistTerm.term == term)
            )).scalar_one_or_none()
            return (row.id, row.acknowledged_at) if row else (None, None)

    term_id, ack_before = asyncio.run(_find("opioids"))
    assert term_id is not None
    assert ack_before is None

    # SEEN -> sets acknowledged_at
    r = client.post(f"/watchlist/{term_id}/seen")
    assert r.status_code == 200
    _, ack_after = asyncio.run(_find("opioids"))
    assert ack_after is not None

    # DELETE -> term gone
    r = client.post(f"/watchlist/{term_id}/delete")
    assert r.status_code == 200
    gone_id, _ = asyncio.run(_find("opioids"))
    assert gone_id is None


def test_watchlist_add_blank_is_noop(client):
    """Posting a blank term doesn't create a row, still returns the card."""
    r = client.post("/watchlist", data={"term": "   "})
    assert r.status_code == 200
    assert 'id="watchlist-card"' in r.text


def test_watchlist_new_hit_count(client):
    """A never-acknowledged term matching a scraped doc reports new_count > 0."""
    import app.web.trends as trends
    from app.web.server import _sanitize_fts_query

    rows = asyncio.run(trends.watchlist_with_counts(_sanitize_fts_query))
    telehealth = [w for w in rows if w["term"] == "telehealth"]
    assert telehealth, "telehealth is a seeded term"
    # seeded doc contains 'telehealth', never acknowledged -> counts as new
    assert telehealth[0]["new_count"] >= 1


# ---------------------------------------------------------------------------
# Topic + board pages render their new charts without error
# ---------------------------------------------------------------------------

def test_topic_page_has_quarterly_chart(client):
    r = client.get("/topic/telehealth")
    assert r.status_code == 200
    body = r.text
    assert "chart-topic-quarterly" in body
    assert "/static/vendor/apexcharts.min.js" in body


def test_board_page_has_topic_breakdown(client):
    r = client.get(f"/board/{client.seeded_board_code}")
    assert r.status_code == 200
    # the seeded board has topic'd meetings, so the ranked bar chart renders
    assert "What this board is working on" in r.text
    assert "width:" in r.text  # a proportional bar
