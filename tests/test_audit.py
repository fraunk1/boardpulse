"""Tests for the standing provenance audit (app/quality/audit.py)."""
import asyncio
import json
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import app.database as db
from app.quality import audit as audit_mod


async def _make_schema(db_file: Path):
    url = f"sqlite+aiosqlite:///{db_file.as_posix()}"
    await db.init_db(url=url)
    await db.engine.dispose()


@pytest.fixture
def seeded(tmp_path, monkeypatch):
    """Temp DB with one verifiable fact, one fabricated-quote fact, and one
    multi-count fact whose count is not visible in its quote."""
    db_file = tmp_path / "audit.db"
    asyncio.run(_make_schema(db_file))
    monkeypatch.setattr(audit_mod, "AUDIT_PATH", tmp_path / "facts_audit.json")

    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO boards (id, state, code, name, board_type, homepage, "
        "discovery_status) VALUES (1,'XX','XX_MD','Test Board','MD',"
        "'https://example.gov','found')")
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    cur.execute(
        "INSERT INTO meetings (id, board_id, meeting_date, title, scraped_at) "
        "VALUES (1,1,?,?,?)",
        ((now - timedelta(days=3)).date().isoformat(), "Mtg", now))
    cur.execute(
        "INSERT INTO meeting_documents (id, meeting_id, doc_type, filename, "
        "file_path, content_text, scraped_at) VALUES (1,1,'minutes','m.pdf',"
        "'x/m.pdf','The Board issued a reprimand to Dr. Example and fined "
        "two physicians for late renewal.',?)", (now,))
    cur.execute(
        "INSERT INTO extraction_runs (id, board_id, prompt_version, "
        "source_file, meetings_covered, facts_inserted, status, created_at) "
        "VALUES (1,1,'facts-v1','x.json',1,3,'ingested',"
        "'2026-07-01 10:00:00')")
    # Verifiable quote, count visible ('two').
    cur.execute(
        "INSERT INTO disciplinary_actions (run_id, meeting_id, document_id, "
        "category, action_count, quote, confidence) VALUES "
        "(1,1,1,'fine',2,'fined two physicians for late renewal','high')")
    # Fabricated quote (not in the document text).
    cur.execute(
        "INSERT INTO disciplinary_actions (run_id, meeting_id, document_id, "
        "category, action_count, quote, confidence) VALUES "
        "(1,1,1,'revocation',1,'the Board revoked nine licenses summarily',"
        "'high')")
    # Multi-count whose number is NOT visible in its quote.
    cur.execute(
        "INSERT INTO disciplinary_actions (run_id, meeting_id, document_id, "
        "category, action_count, quote, confidence) VALUES "
        "(1,1,1,'reprimand',3,'The Board issued a reprimand to Dr. Example',"
        "'high')")
    con.commit()
    con.close()
    return db_file


def test_audit_scorecard(seeded, tmp_path):
    sc = audit_mod.audit_facts(db_path=seeded, write=True)

    disc = sc["tables"]["disciplinary_actions"]
    assert disc["rows"] == 3
    assert disc["quoted"] == 3
    assert disc["quote_verified"] == 2          # the fabricated one fails
    assert len(disc["quote_mismatch_ids"]) == 1
    assert disc["doc_linked"] == 3
    assert disc["boards_contributing"] == 1
    # 'fine x 2' has 'two' in its quote; 'reprimand x 3' does not.
    assert disc["multi_count_rows"] == 2
    assert disc["count_not_in_quote"] == 1

    for empty_table in ("policy_actions", "legislation_mentions",
                        "emerging_topics"):
        assert sc["tables"][empty_table]["rows"] == 0

    assert sc["overall"]["quote_verified"] == 2
    assert sc["overall"]["quoted"] == 3

    # Persisted for /ops and the artifact.
    on_disk = json.loads(
        (tmp_path / "facts_audit.json").read_text(encoding="utf-8"))
    assert on_disk["overall"]["quote_verified"] == 2
    assert audit_mod.latest_audit()["overall"]["quoted"] == 3


def test_count_visible_heuristic():
    assert audit_mod._count_visible(2, "fined two physicians")
    assert audit_mod._count_visible(15, "closed the following fifteen complaints")
    assert audit_mod._count_visible(4, "issued 4 citations")
    assert not audit_mod._count_visible(3, "accepted the consent agreement")


def test_no_audit_file(tmp_path, monkeypatch):
    monkeypatch.setattr(audit_mod, "AUDIT_PATH", tmp_path / "missing.json")
    assert audit_mod.latest_audit() is None
