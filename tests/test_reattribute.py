"""Month-placeholder re-dating (app.scraper.reattribute).

Two layers, mirroring test_facts.py:
  * Pure-function tests for is_month_placeholder / extract_meeting_date — no
    database. These cover the guards that keep the repair from inventing new
    errors: the source-typo year, the agenda-cites-prior-meeting trap, and
    boards that genuinely meet on the 1st.
  * Wiring tests on a temp sqlite DB seeded through the async ORM (init_db
    pattern from test_models.py), covering the real Maryland shape: one
    placeholder holding both Panel A and Panel B, which must split into two
    correctly-dated meetings with agendas left behind.
"""
import asyncio
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.scraper.reattribute import (  # noqa: E402
    extract_meeting_date,
    is_redate_candidate,
    reattribute_placeholder_meetings,
)

# Real Maryland text: the Panel A minutes for June 2026.
JUN_A = (
    "MARYLAND BOARD OF PHYSICIANS\n\nBOARD\nOPEN MEETING MINUTES\n"
    "4201 Patterson Avenue, Baltimore, MD\nRoom 100\nJune 10, 2026\n\n"
    "The Maryland Board of Physicians (the Board) met Wednesday, June 10, 2026 "
    "with the following members present:\n")
# Panel B, same month, two weeks later.
JUN_B = (
    "MARYLAND BOARD OF PHYSICIANS\n\nOPEN MEETING MINUTES\nRoom 100\n"
    "June 24, 2026\n\nThe Maryland Board of Physicians (the Board) met "
    "Wednesday, June 24, 2026 with the following members present:\n")
# The real Feb 2026 Panel B minutes: header says 2026, the "met" sentence
# carries a source typo reading 2025.
FEB_B_TYPO = (
    "MARYLAND BOARD OF PHYSICIANS\n\nOPEN MEETING MINUTES\nRoom 100\n"
    "February 25, 2026\n\nThe Maryland Board of Physicians (the Board) met "
    "Wednesday,  February  25,  2025  with the following members present:\n")


# ---------------------------------------------------------------------------
# Pure functions
# ---------------------------------------------------------------------------

def test_day_one_is_a_candidate():
    assert is_redate_candidate(date(2026, 6, 1))


def test_non_first_day_is_never_a_candidate():
    assert not is_redate_candidate(date(2026, 6, 10))


def test_extracts_date_from_met_sentence():
    assert extract_meeting_date(JUN_A, date(2026, 6, 1)) == date(2026, 6, 10)
    assert extract_meeting_date(JUN_B, date(2026, 6, 1)) == date(2026, 6, 24)


def test_genuine_first_of_month_resolves_to_itself():
    """A board that really met on the 1st must survive untouched: its minutes
    confirm the 1st, the extracted date equals the stored date, and the caller
    skips it. This is what makes the day-1 candidate rule safe."""
    text = ("OPEN MEETING MINUTES\nApril 1, 2026\n\nThe Board met Wednesday, "
            "April 1, 2026 with the following members present:\n")
    assert extract_meeting_date(text, date(2026, 4, 1)) == date(2026, 4, 1)


def test_source_typo_in_year_is_rejected_and_header_wins():
    """Feb26B says "met ... February 25, 2025". The month/year guard rejects
    that candidate and falls through to the 2026 header date."""
    assert extract_meeting_date(FEB_B_TYPO, date(2026, 2, 1)) == date(2026, 2, 25)


def test_date_from_a_different_month_is_rejected():
    """An agenda reciting the PRIOR meeting must not move the document."""
    agenda = ("AGENDA\nApproval of the minutes of the meeting held "
              "May 13, 2026.\n")
    assert extract_meeting_date(agenda, date(2026, 6, 1)) is None


def test_no_date_returns_none():
    assert extract_meeting_date("No dates here at all.", date(2026, 6, 1)) is None
    assert extract_meeting_date("", date(2026, 6, 1)) is None


# ---------------------------------------------------------------------------
# Wiring — temp DB
# ---------------------------------------------------------------------------

@pytest.fixture
def seeded(tmp_path):
    """One placeholder meeting holding Panel A + Panel B minutes and an agenda."""
    import app.database as db

    db.DATABASE_URL = f"sqlite+aiosqlite:///{(tmp_path / 'r.db').as_posix()}"

    async def _seed():
        await db.init_db()
        from app.models import Board, Meeting, MeetingDocument
        async with db.async_session() as s:
            board = Board(state="MD", code="MD_MD",
                          name="Maryland Board of Physicians", board_type="MD",
                          homepage="https://example.gov",
                          discovery_status="manual")
            s.add(board)
            await s.flush()
            m = Meeting(board_id=board.id, meeting_date=date(2026, 6, 1),
                        title="Maryland Board of Physicians — June 01, 2026",
                        summary="Merged summary of both panels.",
                        scraped_at=datetime.now(timezone.utc))
            s.add(m)
            await s.flush()
            s.add_all([
                MeetingDocument(meeting_id=m.id, doc_type="minutes",
                                filename="Jun26Aminutes.pdf",
                                file_path="MD_MD/Jun26Aminutes.pdf",
                                content_text=JUN_A,
                                scraped_at=datetime.now(timezone.utc)),
                MeetingDocument(meeting_id=m.id, doc_type="minutes",
                                filename="Jun26Bminutes.pdf",
                                file_path="MD_MD/Jun26Bminutes.pdf",
                                content_text=JUN_B,
                                scraped_at=datetime.now(timezone.utc)),
                MeetingDocument(meeting_id=m.id, doc_type="agenda",
                                filename="Jun26Aagenda.pdf",
                                file_path="MD_MD/Jun26Aagenda.pdf",
                                content_text="AGENDA\nApproval of minutes of "
                                             "May 13, 2026.\n",
                                scraped_at=datetime.now(timezone.utc)),
            ])
            await s.commit()

    asyncio.run(_seed())
    asyncio.run(db.engine.dispose())
    yield
    asyncio.run(db.engine.dispose())


def _dates():
    import app.database as db
    from app.models import Meeting
    from sqlalchemy import select

    async def _q():
        async with db.async_session() as s:
            rows = (await s.execute(
                select(Meeting).order_by(Meeting.meeting_date))).scalars().all()
            return [(m.meeting_date, m.title) for m in rows]

    out = asyncio.run(_q())
    asyncio.run(asyncio.sleep(0))
    return out


def test_split_creates_two_real_meetings(seeded):
    res = asyncio.run(reattribute_placeholder_meetings("MD_MD"))
    assert res.moved == 2
    assert res.meetings_created == 2
    dates = [d for d, _ in _dates()]
    assert date(2026, 6, 10) in dates
    assert date(2026, 6, 24) in dates


def test_agenda_stays_behind_so_placeholder_survives(seeded):
    """The agenda has no trustworthy date, so its placeholder must remain
    rather than be deleted out from under it."""
    import app.database as db
    from app.models import Meeting, MeetingDocument
    from sqlalchemy import select

    asyncio.run(reattribute_placeholder_meetings("MD_MD"))

    async def _q():
        async with db.async_session() as s:
            ph = (await s.execute(select(Meeting).where(
                Meeting.meeting_date == date(2026, 6, 1)))).scalar_one_or_none()
            if ph is None:
                return None
            docs = (await s.execute(select(MeetingDocument).where(
                MeetingDocument.meeting_id == ph.id))).scalars().all()
            return [d.filename for d in docs]

    left = asyncio.run(_q())
    assert left == ["Jun26Aagenda.pdf"]


def test_dissolved_placeholder_leaves_no_orphan_facts(seeded):
    """Facts hang off meeting_id with no ORM cascade, and SQLite does not
    enforce foreign keys by default -- so a dissolved placeholder must clear
    them explicitly or they survive pointing at a deleted meeting."""
    import app.database as db
    from app.models import Meeting, MeetingDocument
    from sqlalchemy import select, text

    async def _setup_and_run():
        async with db.async_session() as s:
            ph = (await s.execute(select(Meeting).where(
                Meeting.meeting_date == date(2026, 6, 1)))).scalar_one()
            # Drop the agenda so the placeholder empties out entirely, and
            # attach a fact to it the way extraction would have.
            ag = (await s.execute(select(MeetingDocument).where(
                MeetingDocument.meeting_id == ph.id,
                MeetingDocument.doc_type == "agenda"))).scalar_one()
            await s.delete(ag)
            await s.execute(
                text("INSERT INTO emerging_topics "
                     "(run_id, board_id, meeting_id, topic_slug, subject, "
                     " first_mentioned_on, quote, confidence) "
                     "VALUES (1, :b, :m, 'ai-scribes', 'AI scribes', "
                     "        '2026-06-01', 'the Board discussed AI scribes', "
                     "        'high')"),
                {"b": ph.board_id, "m": ph.id})
            await s.commit()
            return ph.id

    ph_id = asyncio.run(_setup_and_run())
    res = asyncio.run(reattribute_placeholder_meetings("MD_MD"))
    assert res.placeholders_removed == 1

    async def _count():
        async with db.async_session() as s:
            n = (await s.execute(
                text("SELECT COUNT(*) FROM emerging_topics "
                     "WHERE meeting_id = :m"), {"m": ph_id})).scalar()
            gone = (await s.execute(select(Meeting).where(
                Meeting.id == ph_id))).scalar_one_or_none()
            return n, gone

    orphans, gone = asyncio.run(_count())
    assert gone is None, "placeholder should be deleted"
    assert orphans == 0, "facts must not survive their deleted meeting"


def test_pre_existing_empty_meeting_is_left_alone(seeded):
    """A day-1 meeting that already had no documents is not this operation's
    business. Boards publish scheduled meetings whose minutes have not appeared
    yet; deleting those would silently drop known upcoming meetings."""
    import app.database as db
    from app.models import Board, Meeting
    from sqlalchemy import select

    async def _add_empty():
        async with db.async_session() as s:
            board = (await s.execute(select(Board))).scalars().first()
            s.add(Meeting(board_id=board.id, meeting_date=date(2026, 12, 1),
                          title="Scheduled — December 01, 2026",
                          scraped_at=datetime.now(timezone.utc)))
            await s.commit()

    asyncio.run(_add_empty())
    asyncio.run(reattribute_placeholder_meetings("MD_MD"))

    async def _still_there():
        async with db.async_session() as s:
            return (await s.execute(select(Meeting).where(
                Meeting.meeting_date == date(2026, 12, 1)
            ))).scalar_one_or_none()

    assert asyncio.run(_still_there()) is not None


def test_dry_run_changes_nothing(seeded):
    before = _dates()
    res = asyncio.run(reattribute_placeholder_meetings("MD_MD", dry_run=True))
    assert res.moved == 2
    assert _dates() == before


def test_idempotent(seeded):
    first = asyncio.run(reattribute_placeholder_meetings("MD_MD"))
    second = asyncio.run(reattribute_placeholder_meetings("MD_MD"))
    assert first.moved == 2
    assert second.moved == 0
