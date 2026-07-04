"""Tests for the per-meeting summary contract: parser, ingest, schema."""
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.extractor.summarizer import parse_board_summary_file  # noqa: E402


# ---------------------------------------------------------------------------
# parse_board_summary_file
# ---------------------------------------------------------------------------

WELL_FORMED = """---
topics: ["licensing", "rulemaking"]
board: XX_MD
state: XX
---

# Testboard — 12-Month Board Summary

**Period:** 2025-07-01 to 2026-06-01
**Meetings analyzed:** 2

The board did rollup things ([2026-05-01](/board/XX/XX_MD#2026-05-01)).

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | 2026-05-01 | Testboard | [Minutes page](https://x.gov) |

=== MEETING: 2026-05-01 ===
topics: [rulemaking, licensing]

The May meeting adopted rule 540-X-1.

=== MEETING: 2026-04-01 ===
topics: []

The April meeting had no quorum.

=== END ===
"""


def test_parse_well_formed():
    board_topics, rollup, meetings = parse_board_summary_file(WELL_FORMED)
    assert board_topics == ["licensing", "rulemaking"]
    assert "rollup things" in rollup
    assert "Sources" in rollup            # sources table stays in the rollup
    assert set(meetings) == {"2026-05-01", "2026-04-01"}
    may_summary, may_topics = meetings["2026-05-01"]
    assert "adopted rule 540-X-1" in may_summary
    assert may_topics == ["rulemaking", "licensing"]
    assert "topics:" not in may_summary   # topics line stripped from body
    apr_summary, apr_topics = meetings["2026-04-01"]
    assert apr_topics == []
    assert "END" not in apr_summary       # end delimiter stripped


def test_parse_tolerates_delimiter_drift():
    drift = WELL_FORMED.replace(
        "=== MEETING: 2026-05-01 ===",
        "==  MEETING: 2026-05-01 — Board Meeting ====")
    _t, _r, meetings = parse_board_summary_file(drift)
    assert "2026-05-01" in meetings


def test_parse_tolerates_missing_end_and_bare_topics():
    text = WELL_FORMED.replace("=== END ===", "").replace(
        "topics: [rulemaking, licensing]", "topics: rulemaking, licensing")
    _t, _r, meetings = parse_board_summary_file(text)
    assert meetings["2026-05-01"][1] == ["rulemaking", "licensing"]


def test_parse_missing_topics_line():
    text = WELL_FORMED.replace("topics: [rulemaking, licensing]\n", "")
    _t, _r, meetings = parse_board_summary_file(text)
    summary, topics = meetings["2026-05-01"]
    assert topics == []
    assert "adopted rule" in summary


def test_parse_legacy_file_falls_back_to_rollup_only():
    legacy = """---
topics: ["licensing"]
board: XX_MD
state: XX
---

# Testboard — Meeting Summary

Old single-blob summary with no meeting sections.
"""
    board_topics, rollup, meetings = parse_board_summary_file(legacy)
    assert board_topics == ["licensing"]
    assert "single-blob" in rollup
    assert meetings == {}


def test_parse_duplicate_date_first_wins():
    dup = WELL_FORMED.replace(
        "=== MEETING: 2026-04-01 ===",
        "=== MEETING: 2026-05-01 ===")
    _t, _r, meetings = parse_board_summary_file(dup)
    assert len(meetings) == 1
    assert "adopted rule" in meetings["2026-05-01"][0]


def test_parse_empty_file():
    _t, rollup, meetings = parse_board_summary_file("")
    assert rollup == ""
    assert meetings == {}


# ---------------------------------------------------------------------------
# prompt contract present
# ---------------------------------------------------------------------------

def test_per_board_prompt_carries_new_contract():
    from app.extractor.prompts import per_board_prompt
    prompt = per_board_prompt(
        board_name="Testboard", state="XX", board_code="XX_MD",
        meetings=[{
            "meeting_date": "2026-05-01", "title": "Board Meeting",
            "documents": [{"doc_type": "minutes", "filename": "m.pdf",
                           "content_text": "hello"}],
        }],
        minutes_url="https://x.gov",
    )
    assert "=== MEETING: YYYY-MM-DD ===" in prompt
    assert "=== END ===" in prompt
    assert "OMIT blocks" in prompt
    assert "12-Month Board Summary" in prompt


# ---------------------------------------------------------------------------
# ingest against a temp DB
# ---------------------------------------------------------------------------

@pytest.fixture
async def temp_db(tmp_path, monkeypatch):
    import app.database as db
    db_file = tmp_path / "test.db"
    monkeypatch.setattr(db, "DATABASE_URL",
                        f"sqlite+aiosqlite:///{db_file.as_posix()}")
    await db.init_db()
    yield db
    # Close pooled connections while this test's loop is still alive —
    # leaked aiosqlite connections raise "Event loop is closed" at GC.
    await db.engine.dispose()


async def _seed_board(db, tmp_path, monkeypatch, meeting_dates):
    from app.models import Board, Meeting
    import app.extractor.summarizer as summarizer
    monkeypatch.setattr(summarizer, "REPORTS_DIR", tmp_path)

    async with db.async_session() as session:
        board = Board(state="XX", code="XX_MD", name="Testboard",
                      board_type="MD", homepage="https://x.gov",
                      discovery_status="manual")
        session.add(board)
        await session.flush()
        for d in meeting_dates:
            session.add(Meeting(
                board_id=board.id, meeting_date=d,
                title=f"Testboard — {d.isoformat()}",
                # simulate the OLD copied board blob
                summary="OLD BOARD BLOB", topics=["licensing"],
            ))
        await session.commit()
        return board.id


async def test_ingest_per_meeting(temp_db, tmp_path, monkeypatch):
    from sqlalchemy import select
    from app.models import Board, Meeting
    from app.extractor.summarizer import ingest_board_summary

    today = date.today()
    d_in_file = today - timedelta(days=30)
    d_not_in_file = today - timedelta(days=60)
    await _seed_board(temp_db, tmp_path, monkeypatch,
                      [d_in_file, d_not_in_file])

    content = WELL_FORMED.replace("2026-05-01", d_in_file.isoformat())
    (tmp_path / "XX_MD_summary.md").write_text(content, encoding="utf-8")

    # force=True: this test exercises the DB-write semantics (match/clear),
    # not the ingest gate — the minimal fixture is far below the gate's
    # content bands. Gate behavior has its own tests in test_gates.py.
    ok = await ingest_board_summary("XX_MD", force=True)
    assert ok

    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        assert "rollup things" in board.summary
        assert board.summarized_at is not None

        meetings = (await session.execute(
            select(Meeting).order_by(Meeting.meeting_date.desc())
        )).scalars().all()
        matched = next(m for m in meetings
                       if m.meeting_date == d_in_file)
        cleared = next(m for m in meetings
                       if m.meeting_date == d_not_in_file)
        assert "adopted rule 540-X-1" in matched.summary
        assert matched.topics == ["rulemaking", "licensing"]
        assert matched.summarized_at is not None
        # not in the file -> stale blob cleared
        assert cleared.summary is None
        assert cleared.topics is None


async def test_ingest_legacy_sets_rollup_and_clears_meetings(
        temp_db, tmp_path, monkeypatch):
    from sqlalchemy import select
    from app.models import Board, Meeting
    from app.extractor.summarizer import ingest_board_summary

    d = date.today() - timedelta(days=10)
    await _seed_board(temp_db, tmp_path, monkeypatch, [d])
    (tmp_path / "XX_MD_summary.md").write_text(
        "---\ntopics: [\"licensing\"]\n---\n\nLegacy blob only.",
        encoding="utf-8")

    # Legacy files are rejected by the ingest gate; force=True is now the
    # only path that lets one through (gate rejection covered in test_gates).
    assert not await ingest_board_summary("XX_MD")
    assert await ingest_board_summary("XX_MD", force=True)
    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        assert "Legacy blob" in board.summary
        meeting = (await session.execute(select(Meeting))).scalars().first()
        # legacy format: meetings untouched (still carry whatever they had)
        assert meeting.summary == "OLD BOARD BLOB"


async def test_national_bundle_uses_rollup_only(temp_db, tmp_path, monkeypatch):
    from app.extractor.summarizer import prepare_national_bundle
    import app.extractor.summarizer as summarizer

    d = date.today() - timedelta(days=30)
    await _seed_board(temp_db, tmp_path, monkeypatch, [d])

    content = WELL_FORMED.replace("2026-05-01", d.isoformat())
    (tmp_path / "XX_MD_summary.md").write_text(content, encoding="utf-8")
    # need >= 2 boards for a bundle; write a second legacy file + board
    from app.models import Board
    async with temp_db.async_session() as session:
        session.add(Board(state="YY", code="YY_MD", name="Other",
                          board_type="MD", homepage="https://y.gov",
                          discovery_status="manual"))
        await session.commit()
    (tmp_path / "YY_MD_summary.md").write_text(
        "---\ntopics: []\n---\n\nOther rollup.", encoding="utf-8")

    path = await prepare_national_bundle()
    assert path is not None
    text = path.read_text(encoding="utf-8")
    assert "rollup things" in text
    # per-meeting block content must NOT leak into the national prompt
    assert "adopted rule 540-X-1" not in text
    assert "=== MEETING:" not in text


# ---------------------------------------------------------------------------
# ensure_schema idempotence
# ---------------------------------------------------------------------------

async def test_ensure_schema_upgrades_old_db(tmp_path, monkeypatch):
    import sqlite3
    import app.database as db

    db_file = tmp_path / "old.db"
    con = sqlite3.connect(db_file)
    # old-era schema: boards without summary columns
    con.execute("""CREATE TABLE boards (
        id INTEGER PRIMARY KEY, state VARCHAR(2), code VARCHAR(10) UNIQUE,
        name VARCHAR(200), board_type VARCHAR(10), homepage TEXT,
        minutes_url TEXT, phone VARCHAR(30), email VARCHAR(100),
        address TEXT, discovery_status VARCHAR(20),
        last_scraped_at DATETIME)""")
    con.execute("""CREATE TABLE meetings (
        id INTEGER PRIMARY KEY, board_id INTEGER, meeting_date DATE,
        title TEXT, meeting_type VARCHAR(20), source_url TEXT,
        screenshot_path TEXT, summary TEXT, topics JSON,
        scraped_at DATETIME)""")
    con.commit()
    con.close()

    monkeypatch.setattr(db, "DATABASE_URL",
                        f"sqlite+aiosqlite:///{db_file.as_posix()}")
    await db.init_db()
    await db.init_db()  # second run must be a no-op

    con = sqlite3.connect(db_file)
    board_cols = {r[1] for r in con.execute("PRAGMA table_info(boards)")}
    meeting_cols = {r[1] for r in con.execute("PRAGMA table_info(meetings)")}
    indexes = {r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type='index'")}
    con.close()

    assert {"summary", "summarized_at"} <= board_cols
    assert "summarized_at" in meeting_cols
    assert {"ix_meetings_board_id", "ix_meetings_meeting_date"} <= indexes
