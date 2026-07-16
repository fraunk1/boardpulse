"""Tests for the structured-facts extraction pipeline (app.extractor.facts).

Two layers, mirroring test_gates.py:
  * Gate unit tests exercise app.quality.gates.check_facts as the pure
    function it is — a synthetic facts-v2 dict + synthetic DB inputs, no
    database — covering one rejection per major code plus the passing case.
  * Ingest wiring tests use a temp sqlite DB. The board + meetings + docs are
    seeded through the async ORM (init_db pattern from test_models.py); the
    facts module's own ingest is SYNC sqlite3, so facts.DB_PATH is pointed at
    the same file and facts.FACTS_DIR at a tmp dir. These cover idempotency,
    disciplinary category replacement, emerging earliest-date-wins, the
    quote-mismatch confidence downgrade + rejection rate, facts_extracted_at
    on all-empty meetings, and in-file dedup.
"""
import json
import sqlite3
import sys
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.quality.gates import check_facts, GateResult  # noqa: E402


# ---------------------------------------------------------------------------
# Synthetic facts-v2 fixture (a dict that passes every gate check)
# ---------------------------------------------------------------------------

D1 = "2026-05-01"
D2 = "2026-04-01"

SRC_D1 = (
    "Minutes of the May meeting. The Board adopted Rule 16-85-1 governing "
    "telehealth standards. The Board discussed House Bill 1234 relating to "
    "physician licensure and voted to monitor it. Disciplinary report: two "
    "licenses were revoked and one physician was placed on probation. The "
    "Board discussed artificial intelligence scribes for the first time."
)
SRC_D2 = (
    "Minutes of the April meeting. No quorum was present and the meeting was "
    "adjourned. Staff noted correspondence would be carried to the next "
    "session."
)


def _good_data() -> dict:
    """Fresh dict each call — the gate mutates confidence in place."""
    return {
        "schema_version": "facts-v2",
        "board_code": "XX_MD",
        "model": "claude-test",
        "meetings": [
            {
                "meeting_date": D1,
                "policy_actions": [{
                    "instrument": "rule", "stage": "adopted",
                    "topic": "telehealth",
                    "title": "Adopt telehealth standards rule",
                    "description": "Board adopted Rule 16-85-1.",
                    "rule_reference": "16-85-1", "action_date": D1,
                    "quote": "The Board adopted Rule 16-85-1 governing "
                             "telehealth standards.",
                    "source_document": "may.pdf", "confidence": "high",
                }],
                "legislation": [{
                    "bill_number": "HB 1234", "bill_state": "XX",
                    "subject": "physician licensure",
                    "topic": "legislation", "involvement": "monitoring",
                    "status_note": None,
                    "quote": "voted to monitor it",
                    "source_document": "may.pdf", "confidence": "medium",
                }],
                "disciplinary": [
                    # bulk entry: the total ("two") is visible in the quote
                    {"category": "revocation", "respondent": None, "count": 2,
                     "quote": "two licenses were revoked",
                     "source_document": "may.pdf", "confidence": "high"},
                    # single unnamed action: count 1, respondent null
                    {"category": "probation", "respondent": None, "count": 1,
                     "quote": "one physician was placed on probation",
                     "source_document": "may.pdf", "confidence": "high"},
                ],
                "emerging_topics": [{
                    "topic_slug": "ai-scribes",
                    "subject": "artificial intelligence scribes",
                    "quote": "The Board discussed artificial intelligence "
                             "scribes for the first time.",
                    "source_document": "may.pdf", "confidence": "medium",
                }],
            },
            {
                "meeting_date": D2,
                "policy_actions": [],
                "legislation": [],
                "disciplinary": [],
                "emerging_topics": [],
            },
        ],
    }


def _gate_kwargs(**over) -> dict:
    kw = dict(
        covered_dates={D1, D2},
        db_text_dates={D1, D2},
        source_texts_by_date={D1: SRC_D1, D2: SRC_D2},
    )
    kw.update(over)
    return kw


def _codes(result: GateResult) -> set[str]:
    return {e.code for e in result.errors}


def _wcodes(result: GateResult) -> set[str]:
    return {w.code for w in result.warnings}


# ===========================================================================
# Gate unit tests — pass + one rejection per major code
# ===========================================================================

def test_good_facts_pass():
    result = check_facts("XX_MD", _good_data(), **_gate_kwargs())
    assert result.ok, [f"{e.code}: {e.message}" for e in result.errors]
    assert result.errors == []


def test_bad_json_rejected():
    result = check_facts("XX_MD", "{not valid json", **_gate_kwargs())
    assert not result.ok
    assert "BAD_JSON" in _codes(result)


def test_wrong_schema_version_rejected():
    data = _good_data()
    data["schema_version"] = "facts-v1"  # superseded by facts-v2
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "STRUCTURE" in _codes(result)


def test_board_code_mismatch_rejected():
    data = _good_data()
    data["board_code"] = "YY_MD"
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert any(e.code == "STRUCTURE" and "XX_MD" in e.message
               for e in result.errors)


def test_ghost_meeting_rejected():
    data = _good_data()
    data["meetings"][0]["meeting_date"] = "2026-05-15"  # not covered / no text
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "GHOST_MEETING" in _codes(result)


def test_missing_covered_meeting_rejected():
    data = _good_data()
    data["meetings"] = data["meetings"][:1]  # drop D2
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert any(e.code == "MISSING_MEETING" and D2 in e.message
               for e in result.errors)


def test_bad_enum_rejected():
    data = _good_data()
    data["meetings"][0]["policy_actions"][0]["instrument"] = "decree"
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "BAD_ENUM" in _codes(result)


def test_missing_field_rejected():
    data = _good_data()
    del data["meetings"][0]["policy_actions"][0]["stage"]
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "FIELD" in _codes(result)


def test_disciplinary_count_must_be_int():
    data = _good_data()
    data["meetings"][0]["disciplinary"][0]["count"] = "2"  # string, not int
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "FIELD" in _codes(result)


def test_disciplinary_fabricated_quote_rejected():
    """facts-v2: disciplinary quotes are hard-checked, like emerging topics."""
    data = _good_data()
    data["meetings"][0]["disciplinary"][0]["quote"] = \
        "This sentence never appears in the minutes at all."
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "FABRICATED_QUOTE" in _codes(result)


def test_bulk_count_not_in_quote_rejected():
    """A bulk entry (count >= 2) must carry its number inside the quote."""
    data = _good_data()
    data["meetings"][0]["disciplinary"][0]["count"] = 3  # quote says "two"
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "COUNT_NOT_IN_QUOTE" in _codes(result)


def test_respondent_with_count_over_one_rejected():
    data = _good_data()
    data["meetings"][0]["disciplinary"][0]["respondent"] = "Dr. Example"
    # count stays 2 -> itemized entries must be count 1
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "COUNT_RULE" in _codes(result)


def test_two_itemized_same_category_pass():
    """Two actions in the same category are two entries now — not a dup."""
    data = _good_data()
    data["meetings"][0]["disciplinary"] = [
        {"category": "revocation", "respondent": "Dr. A", "count": 1,
         "quote": "two licenses were revoked",
         "source_document": "may.pdf", "confidence": "high"},
        {"category": "revocation", "respondent": "Dr. B", "count": 1,
         "quote": "two licenses were revoked",
         "source_document": "may.pdf", "confidence": "high"},
    ]
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert result.ok, [f"{e.code}: {e.message}" for e in result.errors]


def test_duplicate_respondent_rejected():
    data = _good_data()
    entry = {"category": "revocation", "respondent": "Dr. A", "count": 1,
             "quote": "two licenses were revoked",
             "source_document": "may.pdf", "confidence": "high"}
    data["meetings"][0]["disciplinary"] = [entry, dict(entry)]
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "DUPLICATE_FACT" in _codes(result)


def test_zero_count_rejected():
    data = _good_data()
    data["meetings"][0]["disciplinary"][1]["count"] = 0
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "FIELD" in _codes(result)


def test_emerging_fabricated_quote_rejected():
    data = _good_data()
    data["meetings"][0]["emerging_topics"][0]["quote"] = \
        "This exact sentence never appears in the minutes."
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "FABRICATED_QUOTE" in _codes(result)


def test_too_many_facts_rejected():
    from app.quality.gates import FACTS_MAX_PER_FILE
    data = _good_data()
    data["meetings"][0]["policy_actions"] = [
        {"instrument": "rule", "stage": "discussed", "topic": "other",
         "title": f"Item {i}", "description": None, "rule_reference": None,
         "action_date": D1, "quote": None, "source_document": "may.pdf",
         "confidence": "low"}
        for i in range(FACTS_MAX_PER_FILE + 1)
    ]
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "TOO_MANY_FACTS" in _codes(result)


# ---------------------------------------------------------------------------
# F5 quote mismatch — single downgrade (warning) vs file-level rejection
# ---------------------------------------------------------------------------

def test_single_quote_mismatch_downgrades_confidence():
    data = _good_data()
    # facts-v2: only policy + legislation quotes are soft-rate-pooled
    # (disciplinary + emerging are hard-checked). Pad the pool with three
    # more good-quoted policy facts so ONE mismatch stays under 30%.
    for i, q in enumerate((
            "Minutes of the May meeting.",
            "The Board discussed House Bill 1234",
            "voted to monitor it")):
        data["meetings"][0]["policy_actions"].append({
            "instrument": "position", "stage": "discussed", "topic": "other",
            "title": f"Padding item {i}", "description": "Padding fact.",
            "rule_reference": None, "action_date": D1, "quote": q,
            "source_document": "may.pdf", "confidence": "low"})
    data["meetings"][0]["legislation"][0]["quote"] = "not a real substring"
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert result.ok  # 1/5 mismatched — under the 30% file-level threshold
    assert "QUOTE_MISMATCH" in _wcodes(result)
    # confidence forced to low IN PLACE on the passed dict
    assert data["meetings"][0]["legislation"][0]["confidence"] == "low"


def test_quote_mismatch_rate_over_30pct_rejects():
    data = _good_data()
    # break the policy + legislation quotes = 2/2 soft-checked = 100%.
    # (disciplinary + emerging quotes are hard-checked, not rate-pooled.)
    data["meetings"][0]["policy_actions"][0]["quote"] = "fake one"
    data["meetings"][0]["legislation"][0]["quote"] = "fake two"
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "QUOTE_MISMATCH_RATE" in _codes(result)


def test_in_file_duplicate_policy_rejected():
    data = _good_data()
    dup = json.loads(json.dumps(data["meetings"][0]["policy_actions"][0]))
    data["meetings"][0]["policy_actions"].append(dup)
    result = check_facts("XX_MD", data, **_gate_kwargs())
    assert not result.ok
    assert "DUPLICATE_FACT" in _codes(result)


# ===========================================================================
# Ingest wiring — temp sqlite DB (async seed, sync ingest)
# ===========================================================================

@pytest.fixture
async def facts_db(tmp_path, monkeypatch):
    """Seed a board + meetings + docs, then hand back a sync-ingest harness.

    Returns (db_file, out_dir, board_id). facts.DB_PATH and facts.FACTS_DIR
    are monkeypatched so ingest_facts_file() writes to this temp DB and dir.
    """
    import app.database as db
    import app.extractor.facts as facts_mod
    from app.models import Board, Meeting, MeetingDocument

    db_file = tmp_path / "facts_test.db"
    out_dir = tmp_path / "facts"
    out_dir.mkdir()

    monkeypatch.setattr(db, "DATABASE_URL",
                        f"sqlite+aiosqlite:///{db_file.as_posix()}")
    await db.init_db()

    async with db.async_session() as session:
        board = Board(state="XX", code="XX_MD", name="Testboard",
                      board_type="MD", homepage="https://x.gov",
                      minutes_url="https://x.gov/minutes",
                      discovery_status="manual")
        session.add(board)
        await session.flush()
        board_id = board.id
        for d, src in ((date(2026, 5, 1), SRC_D1), (date(2026, 4, 1), SRC_D2)):
            meeting = Meeting(board_id=board.id, meeting_date=d,
                              title=f"Meeting {d.isoformat()}")
            session.add(meeting)
            await session.flush()
            session.add(MeetingDocument(
                meeting_id=meeting.id, doc_type="minutes",
                filename="may.pdf" if d.month == 5 else "apr.pdf",
                file_path=f"docs/{d.isoformat()}.pdf", content_text=src))
        await session.commit()
    await db.engine.dispose()  # release the async pool; ingest is sync

    monkeypatch.setattr(facts_mod, "DB_PATH", db_file)
    monkeypatch.setattr(facts_mod, "FACTS_DIR", out_dir)

    return db_file, out_dir, board_id


def _write_facts_file(out_dir: Path, data: dict, covered=(D1, D2)) -> Path:
    """Write a {code}_01_facts.json + its sidecar meta, return the json path."""
    path = out_dir / "XX_MD_01_facts.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    (out_dir / "XX_MD_01_facts_prompt.meta.json").write_text(
        json.dumps({"board_code": "XX_MD", "covered_dates": list(covered),
                    "budget_chars": 360000}), encoding="utf-8")
    return path


def _counts(db_file: Path) -> dict:
    con = sqlite3.connect(db_file)
    try:
        return {
            "policy": con.execute(
                "SELECT COUNT(*) FROM policy_actions").fetchone()[0],
            "legislation": con.execute(
                "SELECT COUNT(*) FROM legislation_mentions").fetchone()[0],
            "disciplinary": con.execute(
                "SELECT COUNT(*) FROM disciplinary_actions").fetchone()[0],
            "emerging": con.execute(
                "SELECT COUNT(*) FROM emerging_topics").fetchone()[0],
            "runs_ingested": con.execute(
                "SELECT COUNT(*) FROM extraction_runs "
                "WHERE status='ingested'").fetchone()[0],
            "runs_failed": con.execute(
                "SELECT COUNT(*) FROM extraction_runs "
                "WHERE status='failed'").fetchone()[0],
            "facts_extracted": con.execute(
                "SELECT COUNT(*) FROM meetings "
                "WHERE facts_extracted_at IS NOT NULL").fetchone()[0],
        }
    finally:
        con.close()


async def test_ingest_success_writes_all_tables(facts_db):
    from app.extractor.facts import ingest_facts_file
    db_file, out_dir, _ = facts_db
    path = _write_facts_file(out_dir, _good_data())

    assert ingest_facts_file(path) is True
    c = _counts(db_file)
    assert c["policy"] == 1
    assert c["legislation"] == 1
    assert c["disciplinary"] == 2
    assert c["emerging"] == 1
    assert c["runs_ingested"] == 1
    # BOTH covered meetings marked, including the all-empty D2.
    assert c["facts_extracted"] == 2
    assert not Path(str(path) + ".errors.txt").exists()


async def test_ingest_reject_writes_errors_and_no_facts(facts_db):
    from app.extractor.facts import ingest_facts_file
    db_file, out_dir, _ = facts_db
    data = _good_data()
    data["meetings"][0]["policy_actions"][0]["instrument"] = "decree"  # bad
    path = _write_facts_file(out_dir, data)

    assert ingest_facts_file(path) is False
    assert Path(str(path) + ".errors.txt").exists()
    assert "BAD_ENUM" in Path(str(path) + ".errors.txt").read_text(
        encoding="utf-8")
    c = _counts(db_file)
    assert c["policy"] == 0 and c["legislation"] == 0
    assert c["disciplinary"] == 0 and c["emerging"] == 0
    assert c["runs_failed"] == 1 and c["runs_ingested"] == 0
    assert c["facts_extracted"] == 0  # nothing marked on rejection


async def test_double_ingest_is_idempotent(facts_db):
    from app.extractor.facts import ingest_facts_file
    db_file, out_dir, _ = facts_db
    path = _write_facts_file(out_dir, _good_data())

    assert ingest_facts_file(path) is True
    first = _counts(db_file)
    assert ingest_facts_file(path) is True  # again, identical file
    second = _counts(db_file)

    for k in ("policy", "legislation", "disciplinary", "emerging"):
        assert first[k] == second[k], f"{k} count changed on re-ingest"
    assert second["runs_ingested"] == 2  # provenance rows accumulate...
    assert second["facts_extracted"] == 2  # ...but facts do not duplicate


async def test_disciplinary_replaced_not_duplicated(facts_db):
    """Re-ingesting a meeting REPLACES its disciplinary rows (facts-v2:
    a bulk tally corrected into two itemized rows)."""
    from app.extractor.facts import ingest_facts_file
    db_file, out_dir, _ = facts_db

    # First ingest: one bulk revocation row (count=2).
    ingest_facts_file(_write_facts_file(out_dir, _good_data()))

    # Second ingest: the same meeting, now itemized into two entries.
    data = _good_data()
    data["meetings"][0]["disciplinary"] = [
        {"category": "revocation", "respondent": "Dr. A", "count": 1,
         "quote": "two licenses were revoked",
         "source_document": "may.pdf", "confidence": "high"},
        {"category": "revocation", "respondent": "Dr. B", "count": 1,
         "quote": "two licenses were revoked",
         "source_document": "may.pdf", "confidence": "high"},
    ]
    assert ingest_facts_file(_write_facts_file(out_dir, data)) is True

    con = sqlite3.connect(db_file)
    try:
        rows = con.execute(
            "SELECT respondent, action_count FROM disciplinary_actions "
            "WHERE category='revocation' ORDER BY respondent").fetchall()
    finally:
        con.close()
    # Delete-and-replace per meeting: the bulk row is gone, two itemized
    # rows remain, and the total is arithmetic (1+1 = the old tally).
    assert rows == [("Dr. A", 1), ("Dr. B", 1)]


async def test_emerging_earliest_date_wins(facts_db):
    """A later file that mentions the same slug at an EARLIER date wins."""
    from app.extractor.facts import ingest_facts_file
    import app.database as db
    from app.models import Board, Meeting, MeetingDocument
    db_file, out_dir, board_id = facts_db

    # Ingest the good file first: ai-scribes first_mentioned_on = D1 (May).
    ingest_facts_file(_write_facts_file(out_dir, _good_data()))

    # Add an EARLIER text-bearing meeting (March) that also mentions AI.
    D0 = "2026-03-01"
    src0 = ("Minutes of the March meeting. The Board discussed artificial "
            "intelligence scribes as an emerging concern.")
    monkey_url = f"sqlite+aiosqlite:///{db_file.as_posix()}"
    db.DATABASE_URL = monkey_url
    await db.init_db()
    async with db.async_session() as session:
        m = Meeting(board_id=board_id, meeting_date=date(2026, 3, 1),
                    title="March")
        session.add(m)
        await session.flush()
        session.add(MeetingDocument(
            meeting_id=m.id, doc_type="minutes", filename="mar.pdf",
            file_path="docs/mar.pdf", content_text=src0))
        await session.commit()
    await db.engine.dispose()

    earlier = {
        "schema_version": "facts-v2", "board_code": "XX_MD",
        "model": "claude-test",
        "meetings": [{
            "meeting_date": D0,
            "policy_actions": [], "legislation": [], "disciplinary": [],
            "emerging_topics": [{
                "topic_slug": "ai-scribes",
                "subject": "artificial intelligence scribes",
                "quote": "The Board discussed artificial intelligence "
                         "scribes as an emerging concern.",
                "source_document": "mar.pdf", "confidence": "medium"}],
        }],
    }
    path = out_dir / "XX_MD_02_facts.json"
    path.write_text(json.dumps(earlier), encoding="utf-8")
    (out_dir / "XX_MD_02_facts_prompt.meta.json").write_text(
        json.dumps({"board_code": "XX_MD", "covered_dates": [D0]}),
        encoding="utf-8")

    assert ingest_facts_file(path) is True

    con = sqlite3.connect(db_file)
    try:
        rows = con.execute(
            "SELECT topic_slug, first_mentioned_on FROM emerging_topics"
        ).fetchall()
    finally:
        con.close()
    # Still ONE row (upsert), now dated to the earlier March meeting.
    assert len(rows) == 1
    assert rows[0][0] == "ai-scribes"
    assert rows[0][1][:10] == D0


async def test_facts_extracted_set_on_all_empty_meeting(facts_db):
    """A meeting with zero facts still gets facts_extracted_at set."""
    from app.extractor.facts import ingest_facts_file
    db_file, out_dir, _ = facts_db

    empty = {
        "schema_version": "facts-v2", "board_code": "XX_MD",
        "model": "claude-test",
        "meetings": [
            {"meeting_date": D1, "policy_actions": [], "legislation": [],
             "disciplinary": [], "emerging_topics": []},
            {"meeting_date": D2, "policy_actions": [], "legislation": [],
             "disciplinary": [], "emerging_topics": []},
        ],
    }
    path = _write_facts_file(out_dir, empty)
    assert ingest_facts_file(path) is True

    con = sqlite3.connect(db_file)
    try:
        n = con.execute("SELECT COUNT(*) FROM meetings "
                        "WHERE facts_extracted_at IS NOT NULL").fetchone()[0]
        facts = con.execute(
            "SELECT COUNT(*) FROM policy_actions").fetchone()[0]
    finally:
        con.close()
    assert n == 2  # both covered meetings marked
    assert facts == 0  # but no facts written


async def test_ingest_all_facts_scans_dir(facts_db):
    from app.extractor.facts import ingest_all_facts
    db_file, out_dir, _ = facts_db
    _write_facts_file(out_dir, _good_data())
    # a second, rejectable file
    bad = _good_data()
    bad["meetings"][0]["policy_actions"][0]["topic"] = "quantum"
    p2 = out_dir / "XX_MD_02_facts.json"
    p2.write_text(json.dumps(bad), encoding="utf-8")
    (out_dir / "XX_MD_02_facts_prompt.meta.json").write_text(
        json.dumps({"board_code": "XX_MD", "covered_dates": [D1, D2]}),
        encoding="utf-8")

    ingested, rejected = ingest_all_facts()
    assert ingested == 1
    assert rejected == ["XX_MD_02_facts.json"]


async def test_facts_status_reports_coverage(facts_db):
    from app.extractor.facts import ingest_facts_file, facts_status
    db_file, out_dir, _ = facts_db

    # Before ingest: 0% coverage.
    before = facts_status()
    xx = next(r for r in before if r["board_code"] == "XX_MD")
    assert xx["text_meetings"] == 2
    assert xx["facts_extracted"] == 0
    assert xx["coverage_pct"] == 0.0

    ingest_facts_file(_write_facts_file(out_dir, _good_data()))

    after = facts_status()
    xx = next(r for r in after if r["board_code"] == "XX_MD")
    assert xx["facts_extracted"] == 2
    assert xx["coverage_pct"] == 100.0


# ===========================================================================
# prepare_facts_bundles — chunking + sidecar
# ===========================================================================

async def test_prepare_writes_prompt_and_sidecar(facts_db, monkeypatch):
    import app.database as db
    import app.extractor.facts as facts_mod
    db_file, out_dir, _ = facts_db

    # prepare uses the async engine — repoint it at the temp DB.
    monkeypatch.setattr(db, "DATABASE_URL",
                        f"sqlite+aiosqlite:///{db_file.as_posix()}")
    monkeypatch.setattr(facts_mod, "FACTS_DIR", out_dir)

    written = await facts_mod.prepare_facts_bundles(board_code="XX_MD")
    await db.engine.dispose()

    assert len(written) == 1
    prompt = written[0]
    assert prompt.name == "XX_MD_01_facts_prompt.md"
    body = prompt.read_text(encoding="utf-8")
    assert "facts-v2" in body
    assert D1 in body and D2 in body

    meta = json.loads(
        (out_dir / "XX_MD_01_facts_prompt.meta.json").read_text(
            encoding="utf-8"))
    assert set(meta["covered_dates"]) == {D1, D2}
    assert meta["budget_chars"] == facts_mod.FACTS_MAX_PROMPT_CHARS


async def test_prepare_skips_already_extracted(facts_db, monkeypatch):
    import app.database as db
    import app.extractor.facts as facts_mod
    from app.extractor.facts import ingest_facts_file
    db_file, out_dir, _ = facts_db

    # Ingest everything first, so both meetings have facts_extracted_at set.
    ingest_facts_file(_write_facts_file(out_dir, _good_data()))

    monkeypatch.setattr(db, "DATABASE_URL",
                        f"sqlite+aiosqlite:///{db_file.as_posix()}")
    monkeypatch.setattr(facts_mod, "FACTS_DIR", out_dir)

    written = await facts_mod.prepare_facts_bundles(board_code="XX_MD")
    await db.engine.dispose()
    assert written == []  # nothing left to extract

    # force=True re-selects them.
    monkeypatch.setattr(db, "DATABASE_URL",
                        f"sqlite+aiosqlite:///{db_file.as_posix()}")
    written = await facts_mod.prepare_facts_bundles(
        board_code="XX_MD", force=True)
    await db.engine.dispose()
    assert len(written) == 1
