"""Tests for the monthly delta brief (app/reports/brief.py).

Strategy: build the real schema (tables + views + FTS) with the project's own
async init_db against a temp file DB, dispose the engine (mirroring
tests/test_models.py's disposal), then seed rows with stdlib sqlite3 and run
the synchronous brief builder against that file. BRIEFS_DIR is monkeypatched to
tmp_path so no test ever writes the live data/reports/briefs.
"""
import json
import sqlite3
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import database as db
from app.reports import brief as brief_mod


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

async def _make_schema(db_file: Path):
    """Create the full boardpulse schema (tables + views + FTS) in db_file."""
    url = f"sqlite+aiosqlite:///{db_file.as_posix()}"
    await db.init_db(url=url)
    # Dispose so aiosqlite's connection (bound to this loop) is closed before
    # we reopen the file with stdlib sqlite3 — avoids "Event loop is closed".
    await db.engine.dispose()


@pytest.fixture
async def seeded_db(tmp_path, monkeypatch):
    """A temp DB with schema + seed rows; BRIEFS_DIR pointed at tmp_path.

    Returns the db file Path. Seeds:
      - 2 boards (CA_MD, TX_MD)
      - meetings scraped inside and outside a 35-day window
      - one document with text (for watchlist FTS)
    Fact tables are intentionally left EMPTY (the real-world state today) so
    the graceful-degradation path is the default under test; individual tests
    add fact rows where they need them.
    """
    db_file = tmp_path / "test_boardpulse.db"
    await _make_schema(db_file)

    briefs_dir = tmp_path / "briefs"
    briefs_dir.mkdir()
    monkeypatch.setattr(brief_mod, "BRIEFS_DIR", briefs_dir)
    monkeypatch.setattr(brief_mod, "DB_PATH", db_file)

    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Boards
    cur.execute(
        "INSERT INTO boards (id, state, code, name, board_type, homepage, "
        "discovery_status) VALUES (1,'CA','CA_MD','Medical Board of California',"
        "'combined','https://mbc.ca.gov','found')")
    cur.execute(
        "INSERT INTO boards (id, state, code, name, board_type, homepage, "
        "discovery_status) VALUES (2,'TX','TX_MD','Texas Medical Board',"
        "'combined','https://tmb.state.tx.us','found')")

    # Window = (until - 35d, until]. until = 2026-07-01 12:00:00.
    # In-window scraped_at: 2026-06-20 ; out-of-window: 2026-05-01.
    # in-window uses tz-aware form, out uses naive form, to exercise _parse_iso.
    cur.execute(
        "INSERT INTO meetings (id, board_id, meeting_date, title, summary, "
        "scraped_at) VALUES (1,1,'2026-06-18','June CA Meeting',"
        "'The board discussed telehealth rulemaking and reviewed licensing "
        "backlogs. Several disciplinary matters were heard.',"
        "'2026-06-20 09:00:00+00:00')")
    cur.execute(
        "INSERT INTO meetings (id, board_id, meeting_date, title, summary, "
        "scraped_at) VALUES (2,2,'2026-06-15','June TX Meeting',"
        "'Texas board reviewed scope-of-practice petitions and AI in clinical "
        "documentation was raised for the first time.',"
        "'2026-06-21 14:30:00')")
    # Out-of-window (older) meeting — must NOT count as new.
    cur.execute(
        "INSERT INTO meetings (id, board_id, meeting_date, title, summary, "
        "scraped_at) VALUES (3,1,'2026-04-10','April CA Meeting','Old meeting.',"
        "'2026-05-01 09:00:00')")

    # A document with text (for watchlist FTS)
    cur.execute(
        "INSERT INTO meeting_documents (id, meeting_id, doc_type, filename, "
        "file_path, content_text, scraped_at) VALUES (1,2,'minutes','tx.pdf',"
        "'x/tx.pdf','The board discussed artificial intelligence and telehealth "
        "policy.','2026-06-21 14:30:00')")
    cur.execute("INSERT INTO doc_fts(doc_fts) VALUES('rebuild')")

    # (refresh_runs / board_snapshots are not needed by any brief section —
    # by-the-numbers deltas come from the prior brief's sidecar, not the
    # snapshot table — so the fixture omits them.)

    con.commit()
    con.close()
    return db_file


def _add_extraction_run(db_file: Path, board_id: int = 1) -> int:
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO extraction_runs (board_id, prompt_version, source_file, "
        "meetings_covered, facts_inserted, status, created_at) "
        "VALUES (?, 'facts-v1', 'x.json', 1, 1, 'ingested', "
        "'2026-06-25 10:00:00')", (board_id,))
    run_id = cur.lastrowid
    con.commit()
    con.close()
    return run_id


# ---------------------------------------------------------------------------
# Core: build writes .md with both placeholders + sidecar with window bounds
# ---------------------------------------------------------------------------

async def test_build_writes_md_with_placeholders(seeded_db):
    # Need a rule change for the PROSE:B placeholder to appear.
    run_id = _add_extraction_run(seeded_db)
    con = sqlite3.connect(seeded_db)
    con.execute(
        "INSERT INTO policy_actions (run_id, meeting_id, instrument, stage, "
        "topic, title, action_date, confidence, fact_hash) VALUES "
        "(?,1,'rule','adopted','telehealth','Telehealth rule','2026-06-19',"
        "'high','h1')", (run_id,))
    con.commit()
    con.close()

    sidecar = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)

    md_path = brief_mod.BRIEFS_DIR / "2026-07.md"
    assert md_path.exists()
    md = md_path.read_text(encoding="utf-8")
    assert "<!-- PROSE:A -->" in md
    assert "<!-- PROSE:B -->" in md

    # Sidecar carries window bounds + numbers
    json_path = brief_mod.BRIEFS_DIR / "2026-07.json"
    assert json_path.exists()
    assert sidecar["window"]["since"][:10] == "2026-05-27"  # 35 days before
    assert sidecar["window"]["until"][:10] == "2026-07-01"
    assert sidecar["window"]["is_first_brief"] is True
    assert "coverage" in sidecar["sections"]


async def test_prompt_file_is_written_and_small(seeded_db):
    brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    prompt_path = brief_mod.BRIEFS_DIR / "2026-07_prompt.md"
    assert prompt_path.exists()
    text = prompt_path.read_text(encoding="utf-8")
    assert "## SLOT A" in text
    assert "## SLOT B" in text
    # Rough token bound: << 8k tokens. ~4 chars/token heuristic.
    assert len(text) < 32000, f"prompt too big: {len(text)} chars"


# ---------------------------------------------------------------------------
# Sections compute correct counts on seeded data
# ---------------------------------------------------------------------------

async def test_coverage_counts_new_meetings_in_window(seeded_db):
    sidecar = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    cov = sidecar["sections"]["coverage"]
    assert cov["total_boards"] == 2
    assert cov["total_meetings"] == 3
    # Two meetings scraped in-window (2026-06-20, 2026-06-21); one out.
    assert cov["new_meetings"] == 2
    assert cov["boards_touched"] == 2


async def test_appendix_new_meetings_by_state(seeded_db):
    brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    assert "Appendix — new meetings by state" in md
    assert "California" in md
    assert "Texas" in md
    # Out-of-window meeting title must not appear in the appendix.
    assert "April CA Meeting" not in md


async def test_first_mentions_section(seeded_db):
    run_id = _add_extraction_run(seeded_db, board_id=2)
    con = sqlite3.connect(seeded_db)
    con.execute(
        "INSERT INTO emerging_topics (run_id, board_id, meeting_id, topic_slug, "
        "subject, first_mentioned_on, quote, confidence) VALUES "
        "(?,2,2,'ai-documentation','AI in clinical documentation',"
        "'2026-06-15','AI was raised for the first time.','high')", (run_id,))
    con.commit()
    con.close()

    sidecar = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    fm = sidecar["sections"]["counts"]["first_mentions"]
    assert fm == 1
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    assert "AI in clinical documentation" in md


async def test_rule_changes_headline_format(seeded_db):
    run_id = _add_extraction_run(seeded_db)
    con = sqlite3.connect(seeded_db)
    con.execute(
        "INSERT INTO policy_actions (run_id, meeting_id, instrument, stage, "
        "topic, title, action_date, confidence, fact_hash) VALUES "
        "(?,1,'rule','adopted','telehealth','Telehealth rule','2026-06-19',"
        "'high','h1')", (run_id,))
    con.commit()
    con.close()

    brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    # '{Board}: {topic} moved to {stage}'
    assert "California: telehealth moved to adopted" in md


async def test_bills_section(seeded_db):
    run_id = _add_extraction_run(seeded_db, board_id=2)
    con = sqlite3.connect(seeded_db)
    con.execute(
        "INSERT INTO legislation_mentions (run_id, meeting_id, bill_number, "
        "bill_state, subject, involvement, confidence, fact_hash) VALUES "
        "(?,2,'HB 945','TX','AI Medical Services Act','opposing','high','b1')",
        (run_id,))
    con.commit()
    con.close()

    sidecar = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    assert sidecar["sections"]["counts"]["bills"] == 1
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    assert "TX HB 945" in md
    assert "AI Medical Services Act" in md


async def test_watchlist_counts_new_hits(seeded_db):
    con = sqlite3.connect(seeded_db)
    con.execute("INSERT INTO watchlist_terms (term, label, created_at) VALUES "
                "('artificial intelligence','AI','2026-06-01 00:00:00')")
    con.commit()
    con.close()

    sidecar = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    # Doc text mentions 'artificial intelligence' and its meeting is in-window.
    assert sidecar["sections"]["counts"]["watchlist_hits"] >= 1
    assert "**AI**" in md


# ---------------------------------------------------------------------------
# Empty fact tables -> 'nothing this period', no crash
# ---------------------------------------------------------------------------

async def test_empty_fact_tables_degrade_gracefully(seeded_db):
    # seeded_db leaves all four fact tables empty.
    sidecar = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    # Each fact-driven section says 'Nothing this period.'
    assert md.count("_Nothing this period._") >= 3
    # Counts are all zero
    counts = sidecar["sections"]["counts"]
    assert counts["rule_changes"] == 0
    assert counts["bills"] == 0
    assert counts["first_mentions"] == 0


async def test_no_watchlist_terms_message(seeded_db):
    brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    assert "_No watchlist terms configured._" in md


# ---------------------------------------------------------------------------
# ingest_brief_prose splices correctly
# ---------------------------------------------------------------------------

async def test_ingest_prose_splices_slots(seeded_db):
    # Need a rule change so PROSE:B placeholder exists.
    run_id = _add_extraction_run(seeded_db)
    con = sqlite3.connect(seeded_db)
    con.execute(
        "INSERT INTO policy_actions (run_id, meeting_id, instrument, stage, "
        "topic, title, action_date, confidence, fact_hash) VALUES "
        "(?,1,'rule','adopted','telehealth','Telehealth rule','2026-06-19',"
        "'high','h1')", (run_id,))
    con.commit()
    con.close()

    brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)

    prose = (
        "## SLOT A\n"
        "This month the boards were quiet but steady, with telehealth work "
        "continuing in California.\n\n"
        "## SLOT B\n"
        "California adopted a telehealth rule. It was the main change. "
        "No other rules moved.\n"
    )
    (brief_mod.BRIEFS_DIR / "2026-07_prose.md").write_text(prose, encoding="utf-8")

    html_path = brief_mod.ingest_brief_prose("2026-07")
    assert html_path.exists()

    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    # Placeholders gone, prose in.
    assert "<!-- PROSE:A -->" not in md
    assert "<!-- PROSE:B -->" not in md
    assert "quiet but steady" in md
    assert "California adopted a telehealth rule" in md

    html = html_path.read_text(encoding="utf-8")
    assert "quiet but steady" in html
    # Email HTML is self-contained: no external scripts/CDN/remote fetches.
    assert "<script" not in html.lower()
    # No external resource URLs (the only 'http' allowed is the SVG xmlns).
    assert "src=\"http" not in html.lower()
    assert "href=\"http" not in html.lower()
    assert "cdn.jsdelivr" not in html.lower()
    assert "unpkg.com" not in html.lower()
    assert "googleapis" not in html.lower()


async def test_ingest_prose_missing_file_omits_placeholders(seeded_db):
    # Build, then ingest with NO prose file present — brief still renders.
    brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    html_path = brief_mod.ingest_brief_prose("2026-07")
    assert html_path.exists()
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    assert "<!-- PROSE:A -->" not in md
    assert "<!-- PROSE:B -->" not in md


# ---------------------------------------------------------------------------
# Second brief window starts at first brief 'until'
# ---------------------------------------------------------------------------

async def test_second_brief_window_chains_from_first(seeded_db):
    first = brief_mod.build_brief("2026-06-01T12:00:00+00:00", db_path=seeded_db)
    assert first["window"]["is_first_brief"] is True

    second = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    assert second["window"]["is_first_brief"] is False
    # Second window's 'since' == first window's 'until'.
    assert second["window"]["since"][:19] == first["window"]["until"][:19]


async def test_second_brief_by_the_numbers_shows_delta(seeded_db):
    # First brief: no facts. Then add a policy action. Second brief should
    # report a +1 delta on rule/policy actions vs. the first brief.
    brief_mod.build_brief("2026-06-01T12:00:00+00:00", db_path=seeded_db)

    run_id = _add_extraction_run(seeded_db)
    con = sqlite3.connect(seeded_db)
    con.execute(
        "INSERT INTO policy_actions (run_id, meeting_id, instrument, stage, "
        "topic, title, action_date, confidence, fact_hash) VALUES "
        "(?,1,'rule','adopted','telehealth','Telehealth rule','2026-06-19',"
        "'high','h1')", (run_id,))
    con.commit()
    con.close()

    second = brief_mod.build_brief("2026-07-01T12:00:00+00:00", db_path=seeded_db)
    btn = second["sections"]["by_the_numbers"]
    pa = btn["policy_actions"]
    assert pa["current"] == 1
    # The rendered md should show a '+1' change for the rule/policy row.
    md = (brief_mod.BRIEFS_DIR / "2026-07.md").read_text(encoding="utf-8")
    assert "+1" in md
