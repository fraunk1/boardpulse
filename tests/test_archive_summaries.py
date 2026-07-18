"""Tests for the 36-month archive backfill: archive prompts/ingest, the
context-not-target rollup rendering, and check_summary(mode='archive')."""
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


# ---------------------------------------------------------------------------
# temp-DB fixture (mirrors test_per_meeting_summaries — dispose the engine on
# this test's loop so leaked aiosqlite connections don't blow up at GC)
# ---------------------------------------------------------------------------

@pytest.fixture
async def temp_db(tmp_path, monkeypatch):
    import app.database as db
    db_file = tmp_path / "test.db"
    monkeypatch.setattr(db, "DATABASE_URL",
                        f"sqlite+aiosqlite:///{db_file.as_posix()}")
    await db.init_db()
    yield db
    await db.engine.dispose()


async def _seed_board_with_docs(db, meeting_specs):
    """Seed one board (XX_MD) with meetings + one text doc each.

    meeting_specs: list of (meeting_date, content_text, summarized) tuples.
    'summarized' True stamps summarized_at + a stored summary (backfilled).
    Returns board.id.
    """
    from app.models import Board, Meeting, MeetingDocument
    async with db.async_session() as session:
        board = Board(state="XX", code="XX_MD", name="Testboard",
                      board_type="MD", homepage="https://x.gov",
                      minutes_url="https://x.gov/minutes",
                      discovery_status="manual")
        session.add(board)
        await session.flush()
        for d, text, summarized in meeting_specs:
            m = Meeting(
                board_id=board.id, meeting_date=d,
                title=f"Testboard — {d.isoformat()}",
            )
            if summarized:
                m.summary = f"STORED SUMMARY for {d.isoformat()}"
                m.topics = ["licensing"]
                m.summarized_at = datetime.now(timezone.utc)
            session.add(m)
            await session.flush()
            if text:
                session.add(MeetingDocument(
                    meeting_id=m.id, doc_type="minutes",
                    filename="m.pdf", file_path="/x/m.pdf",
                    content_text=text))
        await session.commit()
        return board.id


# ---------------------------------------------------------------------------
# check_summary(mode='archive') — a rollup-less file passes
# ---------------------------------------------------------------------------

ARCHIVE_FILE = """=== MEETING: 2024-03-01 ===
topics: [licensing]

The March 2024 meeting reviewed twelve licensing applications and approved a
revised continuing-education attestation form. The board also discussed the
upcoming budget cycle and scheduled the next quarterly session. Staff reported
on pending investigations and routine renewals processed since the prior
meeting. No disciplinary actions were finalized at this session.

=== MEETING: 2024-06-01 ===
topics: []

The June 2024 meeting was procedural: the board confirmed the prior minutes,
heard a staff update on application volumes, and adjourned early for lack of
a quorum on the rulemaking item. The telehealth working group was asked to
return with a revised draft at the next meeting.

=== END ===
"""


def test_check_summary_archive_mode_passes_rollupless_file():
    from app.quality.gates import check_summary, normalize_summary
    covered = {"2024-03-01", "2024-06-01"}
    result = check_summary(
        "XX_MD",
        normalize_summary(ARCHIVE_FILE),
        state="XX",
        db_text_dates=covered,          # sidecar covered dates
        db_all_dates=covered,
        source_texts_by_date={
            "2024-03-01": "twelve licensing applications continuing-education",
            "2024-06-01": "procedural prior minutes telehealth working group",
        },
        minutes_url="https://x.gov/minutes",
        homepage="https://x.gov",
        mode="archive",
    )
    assert result.ok, [f"{e.code}: {e.message}" for e in result.errors]


def test_archive_mode_rejects_ghost_block():
    from app.quality.gates import check_summary, normalize_summary
    # covered only has 2024-03-01; the 2024-06-01 block is a ghost.
    result = check_summary(
        "XX_MD", normalize_summary(ARCHIVE_FILE), state="XX",
        db_text_dates={"2024-03-01"}, db_all_dates={"2024-03-01"},
        source_texts_by_date={"2024-03-01": "twelve licensing applications"},
        minutes_url="https://x.gov/minutes", homepage="https://x.gov",
        mode="archive")
    assert not result.ok
    assert any(e.code == "GHOST_BLOCK" for e in result.errors)


def test_rollup_mode_default_unchanged_by_archive_kwarg():
    """A rollup file that passed before still passes with the default mode
    (the new kwarg defaults to 'rollup')."""
    from app.quality.gates import check_summary, normalize_summary
    from tests.test_per_meeting_summaries import WELL_FORMED
    inputs = dict(
        state="XX",
        db_text_dates={"2026-05-01", "2026-04-01"},
        db_all_dates={"2026-05-01", "2026-04-01"},
        source_texts_by_date={
            "2026-05-01": "adopted rule 540-X-1 licensing rulemaking",
            "2026-04-01": "no quorum",
        },
        minutes_url="https://x.gov", homepage="https://x.gov",
    )
    # WELL_FORMED's rollup is short; both calls should behave identically.
    r_default = check_summary("XX_MD", normalize_summary(WELL_FORMED), **inputs)
    r_rollup = check_summary("XX_MD", normalize_summary(WELL_FORMED),
                             mode="rollup", **inputs)
    assert [e.code for e in r_default.errors] == \
        [e.code for e in r_rollup.errors]


# ---------------------------------------------------------------------------
# archive prompt builder + year chunking
# ---------------------------------------------------------------------------

def test_archive_prompt_has_no_rollup_layer():
    from app.extractor.prompts import archive_bundle_prompt
    prompt = archive_bundle_prompt(
        board_name="Testboard", state="XX", board_code="XX_MD", year="2024",
        meetings=[{
            "meeting_date": "2024-03-01", "title": "Board Meeting",
            "documents": [{"doc_type": "minutes", "filename": "m.pdf",
                           "content_text": "hello"}],
        }],
        minutes_url="https://x.gov")
    assert "=== MEETING: YYYY-MM-DD ===" in prompt
    assert "=== END ===" in prompt
    # NO rollup / sources / frontmatter contract in an archive prompt. (The
    # prompt DOES tell the model NOT to write a rollup or Sources table, so
    # we check the CONTRACT skeleton is absent, not the negative instruction.)
    assert "12-Month Board Summary" not in prompt
    assert "| # | Date | Board | Source |" not in prompt
    assert "BOARD ROLLUP" not in prompt


async def test_prepare_archive_bundles_chunks_by_year(
        temp_db, tmp_path, monkeypatch):
    import app.extractor.summarizer as summarizer
    from app.extractor.summarizer import prepare_archive_bundles

    monkeypatch.setattr(summarizer, "REPORTS_DIR", tmp_path)
    monkeypatch.setattr(summarizer, "ARCHIVE_DIR", tmp_path / "archive")

    today = date.today()
    old_2023 = date(2023, 5, 1)
    old_2024a = date(2024, 3, 1)
    old_2024b = date(2024, 9, 1)
    in_window = today - timedelta(days=30)
    await _seed_board_with_docs(temp_db, [
        (old_2023, "2023 minutes text", False),
        (old_2024a, "2024 spring minutes text", False),
        (old_2024b, "2024 fall minutes text", False),
        (in_window, "recent minutes text", False),  # inside window -> excluded
    ])

    paths = await prepare_archive_bundles(board_code="XX_MD")
    names = sorted(p.name for p in paths)
    # One prompt per calendar year (single 'a' chunk each here).
    assert "XX_MD_2023a_prompt.md" in names
    assert "XX_MD_2024a_prompt.md" in names
    # In-window meeting must NOT appear in any archive prompt.
    for p in paths:
        assert in_window.isoformat() not in p.read_text(encoding="utf-8")

    # Sidecars are mode='archive' with the year's dates as covered.
    meta_2024 = json.loads(
        (tmp_path / "archive" / "XX_MD_2024a_prompt.meta.json")
        .read_text(encoding="utf-8"))
    assert meta_2024["mode"] == "archive"
    assert set(meta_2024["covered_dates"]) == {
        old_2024a.isoformat(), old_2024b.isoformat()}


async def test_prepare_archive_excludes_already_summarized(
        temp_db, tmp_path, monkeypatch):
    import app.extractor.summarizer as summarizer
    from app.extractor.summarizer import prepare_archive_bundles

    monkeypatch.setattr(summarizer, "REPORTS_DIR", tmp_path)
    monkeypatch.setattr(summarizer, "ARCHIVE_DIR", tmp_path / "archive")

    old_done = date(2023, 4, 1)     # old but ALREADY summarized -> excluded
    old_todo = date(2023, 8, 1)     # old + unsummarized + text -> included
    await _seed_board_with_docs(temp_db, [
        (old_done, "already done text", True),
        (old_todo, "needs summary text", False),
    ])

    paths = await prepare_archive_bundles(board_code="XX_MD")
    assert len(paths) == 1
    text = paths[0].read_text(encoding="utf-8")
    assert old_todo.isoformat() in text
    assert old_done.isoformat() not in text


# ---------------------------------------------------------------------------
# archive ingest: never touches Board.summary, write-once per meeting
# ---------------------------------------------------------------------------

async def test_archive_ingest_never_touches_board_summary(
        temp_db, tmp_path, monkeypatch):
    import app.extractor.summarizer as summarizer
    from sqlalchemy import select
    from app.models import Board, Meeting
    from app.extractor.summarizer import ingest_archive_summary

    monkeypatch.setattr(summarizer, "REPORTS_DIR", tmp_path)
    archive_dir = tmp_path / "archive"
    archive_dir.mkdir()
    monkeypatch.setattr(summarizer, "ARCHIVE_DIR", archive_dir)

    d1 = date(2024, 3, 1)
    d2 = date(2024, 6, 1)
    await _seed_board_with_docs(temp_db, [
        (d1, "twelve licensing applications continuing-education", False),
        (d2, "procedural prior minutes telehealth working group", False),
    ])
    # Give the board a pre-existing rollup we can prove stays intact.
    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        board.summary = "PRE-EXISTING 12-MONTH ROLLUP"
        board.summarized_at = datetime.now(timezone.utc)
        await session.commit()
        # Re-read the persisted value (SQLite drops tzinfo on roundtrip), so
        # the later equality check compares like against like.
    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        board_summarized_at = board.summarized_at

    stem = "XX_MD_2024a"
    (archive_dir / f"{stem}_summary.md").write_text(
        ARCHIVE_FILE, encoding="utf-8")
    (archive_dir / f"{stem}_prompt.meta.json").write_text(json.dumps({
        "mode": "archive",
        "covered_dates": [d1.isoformat(), d2.isoformat()],
        "target_dates": [d1.isoformat(), d2.isoformat()],
    }), encoding="utf-8")

    assert await ingest_archive_summary(stem)

    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        # Board rollup deliberately untouched by archive ingest.
        assert board.summary == "PRE-EXISTING 12-MONTH ROLLUP"
        assert board.summarized_at == board_summarized_at

        meetings = {m.meeting_date: m for m in (await session.execute(
            select(Meeting))).scalars().all()}
        # The archive blocks landed on their own meetings.
        assert "March 2024" in meetings[d1].summary
        assert meetings[d1].topics == ["licensing"]
        assert meetings[d1].summarized_at is not None
        assert "June 2024" in meetings[d2].summary


async def test_archive_ingest_write_once(temp_db, tmp_path, monkeypatch):
    import app.extractor.summarizer as summarizer
    from sqlalchemy import select
    from app.models import Meeting
    from app.extractor.summarizer import ingest_archive_summary

    monkeypatch.setattr(summarizer, "REPORTS_DIR", tmp_path)
    archive_dir = tmp_path / "archive"
    archive_dir.mkdir()
    monkeypatch.setattr(summarizer, "ARCHIVE_DIR", archive_dir)

    d1 = date(2024, 3, 1)
    d2 = date(2024, 6, 1)
    # d1 is ALREADY summarized -> archive block must not overwrite it.
    await _seed_board_with_docs(temp_db, [
        (d1, "twelve licensing applications", True),
        (d2, "procedural prior minutes telehealth working group", False),
    ])

    stem = "XX_MD_2024a"
    (archive_dir / f"{stem}_summary.md").write_text(
        ARCHIVE_FILE, encoding="utf-8")
    (archive_dir / f"{stem}_prompt.meta.json").write_text(json.dumps({
        "mode": "archive",
        "covered_dates": [d1.isoformat(), d2.isoformat()],
        "target_dates": [d1.isoformat(), d2.isoformat()],
    }), encoding="utf-8")

    assert await ingest_archive_summary(stem, force=True)

    async with temp_db.async_session() as session:
        meetings = {m.meeting_date: m for m in (await session.execute(
            select(Meeting))).scalars().all()}
        # d1 kept its stored summary; d2 (fresh) got the archive block.
        assert meetings[d1].summary == f"STORED SUMMARY for {d1.isoformat()}"
        assert "June 2024" in meetings[d2].summary


# ---------------------------------------------------------------------------
# context-not-target: prepare_board_bundle skips already-summarized meetings
# as TARGETS but still renders their stored summary as CONTEXT
# ---------------------------------------------------------------------------

async def test_rollup_context_not_target(temp_db, tmp_path, monkeypatch):
    import app.extractor.summarizer as summarizer
    from app.extractor.summarizer import (
        prepare_board_bundle, _read_prompt_sidecar,
    )

    monkeypatch.setattr(summarizer, "REPORTS_DIR", tmp_path)

    today = date.today()
    d_done = today - timedelta(days=40)   # summarized already -> context only
    d_todo = today - timedelta(days=20)   # unsummarized + text -> target
    await _seed_board_with_docs(temp_db, [
        (d_done, "the already-summarized meeting raw text", True),
        (d_todo, "the fresh meeting raw text to summarize", False),
    ])

    path = await prepare_board_bundle("XX_MD")
    assert path is not None
    prompt = path.read_text(encoding="utf-8")

    # The done meeting's STORED summary appears as context, under the
    # do-not-emit header; its RAW doc text does NOT.
    assert f"STORED SUMMARY for {d_done.isoformat()}" in prompt
    assert "ALREADY SUMMARIZED — context only" in prompt
    assert "the already-summarized meeting raw text" not in prompt
    # The todo meeting carries full raw text (it's a target).
    assert "the fresh meeting raw text to summarize" in prompt

    # Sidecar: covered includes both; target only the unsummarized one.
    meta = _read_prompt_sidecar(tmp_path / "XX_MD_prompt.meta.json")
    assert meta["mode"] == "rollup"
    assert set(meta["covered_dates"]) == {
        d_done.isoformat(), d_todo.isoformat()}
    assert meta["target_dates"] == [d_todo.isoformat()]
