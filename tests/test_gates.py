"""Tests for the summary ingest gate (app.quality.gates).

Unit tests exercise check_summary() as the pure function it is — synthetic
file text + synthetic DB inputs, no database. Ingest wiring tests use a
temp sqlite DB (pattern from test_per_meeting_summaries.py). The final
integration test runs the gate over every REAL summary file in
data/reports/ against the live boardpulse.db (skipped cleanly when the DB
isn't present, e.g. in CI).
"""
import sqlite3
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.quality.gates import (  # noqa: E402
    GateError, GateResult, check_summary, normalize_summary,
)


# ---------------------------------------------------------------------------
# Synthetic fixture: a file that passes every check
# ---------------------------------------------------------------------------

D1 = "2026-05-01"
D2 = "2026-04-01"
OLD = "2025-06-15"  # real meeting that has slid out of the 12-month window

# 29 words x 7 = ~203 words of neutral prose (no names, no big numbers).
_FILLER = (
    "The board continued its routine review of licensing and rulemaking "
    "matters, heard staff updates on operations, and considered routine "
    "correspondence from members of the public during the reporting "
    "period. "
) * 7
_BLOCK_FILLER = (
    "The board continued its routine review of licensing and rulemaking "
    "matters, heard staff updates on operations, and considered routine "
    "correspondence from members of the public during the reporting "
    "period. "
) * 2

GOOD = f"""---
topics: ["licensing", "rulemaking"]
board: XX_MD
state: XX
---

# Testboard — 12-Month Board Summary

**Period:** {D2} to {D1}
**Meetings analyzed:** 2

{_FILLER}The board adopted rule 540-X-1 ([{D1}](/board/XX/XX_MD#{D1})), \
heard a licensure report ([{D1}](/board/XX/XX_MD#{D1})), and lost quorum \
in April ([{D2}](/board/XX/XX_MD#{D2})).

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | {D1} | Testboard | [Minutes page](https://x.gov/minutes) |
| 2 | {D2} | Testboard | [Minutes page](https://x.gov/minutes) |

=== MEETING: {D1} ===
topics: [rulemaking, licensing]

{_BLOCK_FILLER}The May meeting adopted rule 540-X-1.

=== MEETING: {D2} ===
topics: []

{_BLOCK_FILLER}The April meeting had no quorum.

=== END ===
"""


def _kwargs(**over):
    kw = dict(
        state="XX",
        db_text_dates={D1, D2},
        db_all_dates={D1, D2, OLD},
        source_texts_by_date={
            D1: "Minutes of the May meeting. The board adopted rule 540-X-1.",
            D2: "Minutes of the April meeting. No quorum was present.",
        },
        minutes_url="https://x.gov/minutes",
        homepage="https://www.x.gov",
    )
    kw.update(over)
    return kw


def _codes(result: GateResult) -> set[str]:
    return {e.code for e in result.errors}


def _warning_codes(result: GateResult) -> set[str]:
    return {w.code for w in result.warnings}


# ---------------------------------------------------------------------------
# passing + normalization
# ---------------------------------------------------------------------------

def test_good_file_passes():
    result = check_summary("XX_MD", GOOD, **_kwargs())
    assert result.ok, [f"{e.code}: {e.message}" for e in result.errors]
    assert result.errors == []
    assert result.warnings == []


def test_fence_wrapped_input_normalizes_then_passes():
    raw = "﻿```markdown\n" + GOOD + "\n```\n"
    norm = normalize_summary(raw)
    assert not norm.startswith("```")
    assert not norm.startswith("﻿")
    assert norm.rstrip().endswith("=== END ===")
    result = check_summary("XX_MD", norm, **_kwargs())
    assert result.ok


def test_normalize_leaves_clean_text_alone():
    assert normalize_summary(GOOD) == GOOD.strip()


# ---------------------------------------------------------------------------
# S1 STRUCTURE / LEGACY_FORMAT
# ---------------------------------------------------------------------------

def test_legacy_format_rejected():
    legacy = GOOD.split("=== MEETING:")[0]  # rollup only, no blocks
    result = check_summary("XX_MD", legacy, **_kwargs())
    assert not result.ok
    assert "LEGACY_FORMAT" in _codes(result)


def test_structure_missing_frontmatter():
    body = GOOD.split("---\n", 2)[2]
    result = check_summary("XX_MD", body, **_kwargs())
    assert not result.ok
    assert "STRUCTURE" in _codes(result)


def test_structure_board_mismatch():
    text = GOOD.replace("board: XX_MD", "board: YY_MD")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "STRUCTURE" and "XX_MD" in e.message
               for e in result.errors)


def test_structure_missing_end():
    text = GOOD.replace("=== END ===", "")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "STRUCTURE" and "END" in e.message
               for e in result.errors)


# ---------------------------------------------------------------------------
# S2 GHOST_BLOCK / MISSING_BLOCK
# ---------------------------------------------------------------------------

def test_ghost_block_is_hard_error():
    # 2026-04-15 is mid-window and matches no meeting at all: fabricated.
    text = GOOD.replace(f"=== MEETING: {D2} ===", "=== MEETING: 2026-04-15 ===")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "GHOST_BLOCK" and D1 in e.message
               for e in result.errors)  # message lists the valid dates


def test_ghost_block_window_drift_is_warning():
    # OLD is a real meeting date older than every current text date — the
    # window slid past it after the summary was written. Not a rejection.
    text = GOOD.replace(f"=== MEETING: {D2} ===", f"=== MEETING: {OLD} ===")
    result = check_summary("XX_MD", text, **_kwargs())
    assert result.ok
    assert "GHOST_BLOCK" in _warning_codes(result)


def test_missing_block_is_warning_not_rejection():
    # A text-bearing date with no block = stale summary (new text landed
    # after it was written). Flagged, but never a rejection.
    result = check_summary(
        "XX_MD", GOOD,
        **_kwargs(db_text_dates={D1, D2, "2026-03-01"},
                  db_all_dates={D1, D2, OLD, "2026-03-01"}))
    assert result.ok
    assert any(w.code == "MISSING_BLOCK" and "2026-03-01" in w.message
               for w in result.warnings)


# ---------------------------------------------------------------------------
# S3 GHOST_CITATION / S5 CITATION_FORMAT
# ---------------------------------------------------------------------------

def test_ghost_citation():
    text = GOOD.replace(f"[{D2}](/board/XX/XX_MD#{D2})",
                        "[2024-01-01](/board/XX/XX_MD#2024-01-01)")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "GHOST_CITATION" in _codes(result)


def test_citation_format_wrong_path():
    text = GOOD.replace(f"[{D2}](/board/XX/XX_MD#{D2})",
                        f"[{D2}](/board/XX/YY_MD#{D2})")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "CITATION_FORMAT" in _codes(result)


def test_citation_format_bracket_anchor_mismatch():
    text = GOOD.replace(f"[{D2}](/board/XX/XX_MD#{D2})",
                        f"[{D2}](/board/XX/XX_MD#{D1})")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "CITATION_FORMAT" in _codes(result)


def test_citation_format_too_few_citations():
    import re
    text = re.sub(r"\(\[\d{4}-\d{2}-\d{2}\]\(/board/[^)]*\)\)", "", GOOD)
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "CITATION_FORMAT" and "at least 2" in e.message
               for e in result.errors)


# ---------------------------------------------------------------------------
# S4 LENGTH
# ---------------------------------------------------------------------------

def test_rollup_too_short():
    text = GOOD.replace(_FILLER, "")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "LENGTH" and "Rollup" in e.message
               for e in result.errors)


def test_block_too_long():
    text = GOOD.replace("The May meeting adopted rule 540-X-1.",
                        "The May meeting adopted rule 540-X-1. " + _FILLER * 2)
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "LENGTH" and D1 in e.message
               for e in result.errors)


# ---------------------------------------------------------------------------
# S6 SOURCES
# ---------------------------------------------------------------------------

def test_source_host_mismatch():
    text = GOOD.replace("[Minutes page](https://x.gov/minutes)",
                        "[Minutes page](https://evil.example.com/minutes)")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "SOURCE_HOST" in _codes(result)


def test_source_host_subdomain_accepted():
    text = GOOD.replace("[Minutes page](https://x.gov/minutes)",
                        "[Minutes page](https://docs.x.gov/minutes)")
    result = check_summary("XX_MD", text, **_kwargs())
    assert result.ok


def test_sources_section_required():
    text = GOOD.replace("## Sources", "## Bibliography")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "SOURCES" in _codes(result)


# ---------------------------------------------------------------------------
# S7 TOPICS
# ---------------------------------------------------------------------------

def test_bad_topic_lists_valid_values():
    text = GOOD.replace("topics: [rulemaking, licensing]",
                        "topics: [rulemaking, quantum]")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "BAD_TOPIC" and "quantum" in e.message
               and "licensing" in e.message for e in result.errors)


def test_topic_union_mismatch_is_warning():
    text = GOOD.replace('topics: ["licensing", "rulemaking"]',
                        'topics: ["licensing", "rulemaking", "telehealth"]')
    result = check_summary("XX_MD", text, **_kwargs())
    assert result.ok
    assert any(w.code == "TOPIC_UNION" and "telehealth" in w.message
               for w in result.warnings)


# ---------------------------------------------------------------------------
# S8 NAME_CHECK
# ---------------------------------------------------------------------------

def test_name_check_fabricated_name():
    text = GOOD.replace(
        "The May meeting adopted rule 540-X-1.",
        "The May meeting adopted rule 540-X-1 after testimony from "
        "Jane Qzxjkl, M.D. regarding the matter.")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert any(e.code == "NAME_CHECK" and "Qzxjkl" in e.message
               for e in result.errors)


def test_name_check_verifies_against_block_date_source():
    text = GOOD.replace(
        "The May meeting adopted rule 540-X-1.",
        "The May meeting adopted rule 540-X-1 on a motion by Dr. Quorumson.")
    kw = _kwargs()
    kw["source_texts_by_date"][D1] += " Motion by Dr. Quorumson carried."
    result = check_summary("XX_MD", text, **kw)
    assert result.ok


def test_name_check_falls_back_to_board_corpus():
    # Name appears only in ANOTHER date's source text (combined-PDF slop).
    text = GOOD.replace(
        "The April meeting had no quorum.",
        "The April meeting had no quorum, as noted by Dr. Quorumson.")
    kw = _kwargs()
    kw["source_texts_by_date"][D1] += " Dr. Quorumson attended in May."
    result = check_summary("XX_MD", text, **kw)
    assert result.ok


def test_name_check_skipped_when_source_text_missing():
    text = GOOD.replace(
        "The April meeting had no quorum.",
        "The April meeting had no quorum, as noted by Dr. Nowheremann.")
    kw = _kwargs()
    del kw["source_texts_by_date"][D2]  # no source text for that date
    result = check_summary("XX_MD", text, **kw)
    assert "NAME_CHECK" not in _codes(result)


# ---------------------------------------------------------------------------
# S9 NUMERIC (warnings only)
# ---------------------------------------------------------------------------

def test_unverifiable_numbers_warn_but_pass():
    text = GOOD.replace(
        "The May meeting adopted rule 540-X-1.",
        "The May meeting adopted rule 540-X-1 with a budget of 123456 "
        "dollars, a 47% increase.")
    result = check_summary("XX_MD", text, **_kwargs())
    assert result.ok
    assert any(w.code == "NUMERIC" and "123456" in w.message
               for w in result.warnings)
    assert any(w.code == "NUMERIC" and "47" in w.message
               for w in result.warnings)


# ---------------------------------------------------------------------------
# S10 REFUSAL
# ---------------------------------------------------------------------------

def test_refusal_text_in_block():
    text = GOOD.replace("The April meeting had no quorum.",
                        "I cannot summarize this meeting.")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "REFUSAL" in _codes(result)


def test_placeholder_text_in_block():
    text = GOOD.replace("The April meeting had no quorum.",
                        "(No extracted text available)")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "REFUSAL" in _codes(result)


def test_instruction_echo_in_rollup():
    text = GOOD.replace("**Meetings analyzed:** 2",
                        "**Meetings analyzed:** 2\n\nOutput Format")
    result = check_summary("XX_MD", text, **_kwargs())
    assert not result.ok
    assert "REFUSAL" in _codes(result)


# ---------------------------------------------------------------------------
# ingest wiring (temp sqlite DB, pattern from test_per_meeting_summaries)
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


async def _seed_board(db, tmp_path, monkeypatch, code="XX_MD", state="XX",
                      homepage="https://x.gov", dates_with_text=()):
    from app.models import Board, Meeting, MeetingDocument
    import app.extractor.summarizer as summarizer
    monkeypatch.setattr(summarizer, "REPORTS_DIR", tmp_path)

    async with db.async_session() as session:
        board = Board(state=state, code=code, name="Testboard",
                      board_type="MD", homepage=homepage,
                      minutes_url=f"{homepage}/minutes",
                      discovery_status="manual")
        session.add(board)
        await session.flush()
        for d, text in dates_with_text:
            meeting = Meeting(board_id=board.id, meeting_date=d,
                              title=f"Meeting {d.isoformat()}")
            session.add(meeting)
            await session.flush()
            if text:
                session.add(MeetingDocument(
                    meeting_id=meeting.id, doc_type="minutes",
                    filename="m.pdf", file_path="docs/m.pdf",
                    content_text=text))
        await session.commit()
        return board.id


LEGACY_FILE = """---
topics: ["licensing"]
board: XX_MD
state: XX
---

Old single-blob summary with no meeting sections.
"""


async def test_ingest_rejects_writes_errors_file(temp_db, tmp_path, monkeypatch):
    from sqlalchemy import select
    from app.models import Board
    from app.extractor.summarizer import ingest_board_summary

    d = date.today() - timedelta(days=30)
    await _seed_board(temp_db, tmp_path, monkeypatch,
                      dates_with_text=[(d, "Minutes text.")])
    (tmp_path / "XX_MD_summary.md").write_text(LEGACY_FILE, encoding="utf-8")

    ok = await ingest_board_summary("XX_MD")
    assert not ok

    errors_path = tmp_path / "XX_MD_summary.errors.txt"
    assert errors_path.exists()
    assert "LEGACY_FORMAT:" in errors_path.read_text(encoding="utf-8")

    # Nothing was written to the database.
    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        assert board.summary is None
        assert board.summarized_at is None


async def test_ingest_force_bypasses_gate(temp_db, tmp_path, monkeypatch, capsys):
    from sqlalchemy import select
    from app.models import Board
    from app.extractor.summarizer import ingest_board_summary

    d = date.today() - timedelta(days=30)
    await _seed_board(temp_db, tmp_path, monkeypatch,
                      dates_with_text=[(d, "Minutes text.")])
    (tmp_path / "XX_MD_summary.md").write_text(LEGACY_FILE, encoding="utf-8")

    ok = await ingest_board_summary("XX_MD", force=True)
    assert ok
    assert "WARNING" in capsys.readouterr().out

    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        assert "single-blob" in board.summary


async def test_ingest_success_preserved_and_clears_stale_errors(
        temp_db, tmp_path, monkeypatch):
    from sqlalchemy import select
    from app.models import Board, Meeting
    from app.extractor.summarizer import ingest_board_summary

    da = date.today() - timedelta(days=30)
    db_date = date.today() - timedelta(days=60)
    await _seed_board(temp_db, tmp_path, monkeypatch, dates_with_text=[
        (da, "Minutes of the May meeting. The board adopted rule 540-X-1."),
        (db_date, "Minutes of the April meeting. No quorum was present."),
    ])

    content = GOOD.replace(D1, da.isoformat()).replace(D2, db_date.isoformat())
    (tmp_path / "XX_MD_summary.md").write_text(content, encoding="utf-8")
    errors_path = tmp_path / "XX_MD_summary.errors.txt"
    errors_path.write_text("STALE: old rejection\n", encoding="utf-8")

    ok = await ingest_board_summary("XX_MD")
    assert ok
    assert not errors_path.exists()  # stale rejection record removed

    # Existing success behavior preserved: rollup on board, blocks on
    # their own meetings.
    async with temp_db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == "XX_MD"))).scalar_one()
        assert "routine review of licensing" in board.summary
        meetings = (await session.execute(select(Meeting))).scalars().all()
        by_date = {m.meeting_date: m for m in meetings}
        assert "adopted rule 540-X-1" in by_date[da].summary
        assert by_date[da].topics == ["rulemaking", "licensing"]
        assert "no quorum" in by_date[db_date].summary


async def test_ingest_all_returns_counts_and_prints_summary(
        temp_db, tmp_path, monkeypatch, capsys):
    from app.extractor.summarizer import ingest_all_summaries

    da = date.today() - timedelta(days=30)
    db_date = date.today() - timedelta(days=60)
    await _seed_board(temp_db, tmp_path, monkeypatch, dates_with_text=[
        (da, "Minutes of the May meeting. The board adopted rule 540-X-1."),
        (db_date, "Minutes of the April meeting. No quorum was present."),
    ])
    await _seed_board(temp_db, tmp_path, monkeypatch, code="YY_MD",
                      state="YY", homepage="https://y.gov",
                      dates_with_text=[(da, "Some minutes text.")])

    good = GOOD.replace(D1, da.isoformat()).replace(D2, db_date.isoformat())
    (tmp_path / "XX_MD_summary.md").write_text(good, encoding="utf-8")
    (tmp_path / "YY_MD_summary.md").write_text(
        LEGACY_FILE.replace("XX_MD", "YY_MD").replace("state: XX", "state: YY"),
        encoding="utf-8")

    ingested, rejected = await ingest_all_summaries()
    assert ingested == 1
    assert rejected == ["YY_MD"]
    out = capsys.readouterr().out
    assert "INGEST: 1 ok, 1 rejected (YY_MD)" in out


# ---------------------------------------------------------------------------
# integration: every real summary file must pass against the live DB
# ---------------------------------------------------------------------------

def test_all_real_summary_files_pass_gate():
    db_path = ROOT / "boardpulse.db"
    if not db_path.exists():
        pytest.skip("boardpulse.db not present — live-DB gate check "
                    "runs only on a machine with the real database")
    files = sorted((ROOT / "data" / "reports").glob("*_summary.md"))
    if not files:
        pytest.skip("no real summary files in data/reports/")

    from _validate_summaries import gate_inputs

    con = sqlite3.connect(db_path)
    failures = []
    try:
        for f in files:
            code = f.stem.replace("_summary", "")
            inputs = gate_inputs(con, code)
            if inputs is None:
                failures.append((code, [GateError("NO_BOARD",
                                                  "board missing from DB")]))
                continue
            result = check_summary(
                code, normalize_summary(f.read_text(encoding="utf-8")),
                **inputs)
            if not result.ok:
                failures.append((code, result.errors))
    finally:
        con.close()

    for code, errs in failures:  # make regressions debuggable
        print(f"\nFAIL {code}:")
        for e in errs:
            print(f"  {e.code}: {e.message}")
    assert not failures, (
        f"{len(failures)}/{len(files)} real summary files failed the gate: "
        f"{[c for c, _ in failures]}")
