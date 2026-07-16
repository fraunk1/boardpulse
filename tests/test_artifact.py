"""Tests for the dashboard artifact exporter (app/reports/artifact.py).

Strategy mirrors tests/test_brief.py: real schema via the project's async
init_db against a temp file DB, ORM seeding, and every on-disk input
(briefs dir, reports dir, project root for the ledger) monkeypatched to
tmp_path so no test reads or writes live data. The REAL Jinja template is
rendered — these tests are the artifact contract.
"""
import asyncio
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import app.database as db
from app.reports import artifact as artifact_mod
from app.reports import brief as brief_mod


SCRIPT_ROLLUP = ("The board discussed telehealth "
                 "([2026-06-18](/board/XX/XX_MD#2026-06-18)). "
                 "<script>alert(1)</script> End of rollup.")


async def _seed(db_file: Path, now: datetime):
    """Schema + seed rows: 3 boards, in/out-of-window meetings, one document
    with text (FTS), a watchlist term, and a refresh run."""
    db.DATABASE_URL = f"sqlite+aiosqlite:///{db_file.as_posix()}"
    await db.init_db()
    from app.models import (Board, Meeting, MeetingDocument, RefreshRun,
                            WatchlistTerm)

    async with db.async_session() as s:
        b1 = Board(state="XX", code="XX_MD", name="Test Medical Board",
                   board_type="MD", homepage="https://example.gov",
                   minutes_url="https://example.gov/minutes",
                   discovery_status="found", summary=SCRIPT_ROLLUP)
        b2 = Board(state="YY", code="YY_MD", name="Second Medical Board",
                   board_type="DO", homepage="https://example2.gov",
                   discovery_status="found",
                   summary="A quiet year of routine licensing work.")
        b3 = Board(state="ZZ", code="ZZ_DO", name="Third Medical Board",
                   board_type="DO", homepage="https://example3.gov",
                   discovery_status="none_published")
        s.add_all([b1, b2, b3])
        await s.flush()

        # b1: meeting scraped INSIDE the brief window (changed flag on).
        m1 = Meeting(board_id=b1.id, meeting_date=now.date(),
                     title="Recent meeting", topics=["telehealth", "AI"],
                     summary="Discussed AI in licensing.",
                     scraped_at=now - timedelta(days=2))
        # b2: meeting scraped OUTSIDE the window (no changed flag).
        m2 = Meeting(board_id=b2.id,
                     meeting_date=now.date() - timedelta(days=60),
                     title="Old meeting", topics=["licensing"],
                     summary="Routine matters.",
                     scraped_at=now - timedelta(days=45))
        s.add_all([m1, m2])
        await s.flush()

        s.add(MeetingDocument(
            meeting_id=m1.id, doc_type="minutes", filename="min.pdf",
            file_path="XX_MD/min.pdf",
            content_text="The board discussed AI and telehealth policy. "
                         "Dr. Case was fined for late renewal.",
            scraped_at=now - timedelta(days=2)))
        s.add(WatchlistTerm(term="AI", label="AI",
                            created_at=now - timedelta(days=90)))
        s.add(RefreshRun(started_at=now - timedelta(hours=2),
                         finished_at=now - timedelta(hours=1),
                         boards_changed=1, boards_regressed=None,
                         docs_before=1, docs_after=2, exit_code=0))
        await s.commit()

    async with db.engine.begin() as conn:
        await conn.exec_driver_sql("INSERT INTO doc_fts(doc_fts) VALUES('rebuild')")
        # One in-window disciplinary fact so the Sources card has a quote.
        await conn.exec_driver_sql(
            "INSERT INTO extraction_runs (id, board_id, prompt_version, "
            "source_file, meetings_covered, facts_inserted, status, "
            "created_at) VALUES (1,1,'facts-v1','x.json',1,1,'ingested',"
            "'2026-07-01 10:00:00')")
        await conn.exec_driver_sql(
            "INSERT INTO disciplinary_actions (run_id, meeting_id, "
            "document_id, category, action_count, quote, confidence) "
            "VALUES (1,1,1,'fine',1,"
            "'Dr. Case was fined for late renewal','high')")
    await db.engine.dispose()


def _write_inputs(tmp: Path, now: datetime):
    """Brief (md + sidecar) and landscape report files."""
    briefs = tmp / "briefs"
    reports = tmp / "reports"
    briefs.mkdir(exist_ok=True)
    reports.mkdir(exist_ok=True)

    ym = now.strftime("%Y-%m")
    since = (now - timedelta(days=10)).isoformat(sep=" ", timespec="seconds")
    until = now.isoformat(sep=" ", timespec="seconds")
    (briefs / f"{ym}.md").write_text(
        "# Board Pulse — Monthly Delta Brief\n\n"
        "## The month in brief\n\nA quiet period overall.\n\n"
        "<script>alert(2)</script>\n\n"
        "| Measure | This brief |\n| --- | ---: |\n| Meetings tracked | 2 |\n",
        encoding="utf-8")
    (briefs / f"{ym}.json").write_text(
        '{"window": {"ym": "%s", "since": "%s", "until": "%s"},'
        ' "sections": {"coverage": {"total_boards": 3, "new_meetings": 1,'
        ' "boards_touched": 1}, "counts": {"rule_changes": 0}}}'
        % (ym, since, until), encoding="utf-8")

    (reports / f"{now.date().isoformat()}-board-landscape.md").write_text(
        "# National Landscape\n\nIntro paragraph.\n\n"
        "## Section One\n\nA claim about telehealth "
        "([Test Medical Board, meeting](/board/XX/XX_MD#2026-06-18)) "
        "and an internal [meeting link](/meeting/5) too.\n\n"
        "## Section Two\n\nSecond section body.\n",
        encoding="utf-8")
    return briefs, reports


@pytest.fixture
def built(tmp_path, monkeypatch):
    """Build the artifact against a fully seeded temp environment.

    Returns (html, out_path).
    """
    from app.quality import audit as audit_mod

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    briefs, reports = _write_inputs(tmp_path, now)
    monkeypatch.setattr(brief_mod, "BRIEFS_DIR", briefs)
    monkeypatch.setattr(artifact_mod, "REPORTS_DIR", reports)
    monkeypatch.setattr(audit_mod, "AUDIT_PATH", tmp_path / "facts_audit.json")
    # Point the ledger lookup at tmp (no coverage_ledger.json -> []).
    monkeypatch.setattr(artifact_mod, "PROJECT_ROOT", tmp_path)

    out = tmp_path / "out" / "dashboard.html"

    async def run():
        await _seed(tmp_path / "a.db", now)
        audit_mod.audit_facts(db_path=tmp_path / "a.db", write=True)
        path = await artifact_mod.build_artifact(out_path=out)
        await db.engine.dispose()
        return path

    path = asyncio.run(run())
    return path.read_text(encoding="utf-8"), path


def test_builds_utf8_file(built):
    html, path = built
    assert path.exists()
    assert len(html) > 10_000


def test_fragment_contract(built):
    html, _ = built
    assert html.lstrip().lower().startswith("<title>")
    assert "<!DOCTYPE" not in html
    assert not re.search(r"<html\b", html, re.I)
    assert not re.search(r"<head\b", html, re.I)   # <header> stays legal
    assert not re.search(r"<body\b", html, re.I)
    # ...and the fragment DOES use <header>, proving the \b matters.
    assert "<header" in html


def test_csp_contract_no_external_resources(built):
    html, _ = built
    assert not re.search(
        r"""(?:src|srcset)\s*=\s*["'](?:https?:)?//""", html, re.I)
    assert not re.search(r"<link\b|<iframe\b", html, re.I)
    assert "@import" not in html
    assert not re.search(r"""url\(\s*["']?(?:https?:)?//""", html, re.I)
    assert "fetch(" not in html
    # Navigation links ARE allowed — the rewritten citation must be present.
    assert 'href="https://example.gov/minutes"' in html


def test_landscape_citation_rewritten(built):
    html, _ = built
    # Citation text kept, dashboard-internal URL gone.
    assert "/board/XX/XX_MD" not in html
    assert "/meeting/5" not in html
    assert "meeting link" in html          # internal link demoted to text
    assert "Section One" in html and "Section Two" in html


def test_board_grid_and_changed_flag(built):
    html, _ = built
    for code in ("XX_MD", "YY_MD", "ZZ_DO"):
        assert code in html
    # Exactly one board (XX_MD) was scraped inside the brief window.
    assert html.count('class="upd"') == 1
    # none_published board renders its status dot class.
    assert "st-none_published" in html
    # Rollup markdown citation links are stripped to their text.
    assert "[2026-06-18]" not in html
    assert "(/board/" not in html


def test_rollup_script_escaped(built):
    html, _ = built
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    # Script inside the brief markdown is stripped by the sanitizer.
    assert "alert(2)" not in html


def test_sources_and_verification_card(built):
    html, _ = built
    assert "Sources &amp; verification" in html
    # Audit scorecard rendered (1 quoted fact, verified).
    assert "stored quotes verify word-for-word" in html
    # The in-window disciplinary fact's quote appears in the expander.
    assert "Dr. Case was fined for late renewal" in html
    # All four fact-type expanders present.
    for label in ("Discipline", "Rules &amp; policy", "Bills", "Emerging topics"):
        assert label in html
    # Footer carries the audit line.
    assert "Provenance audit" in html


def test_theme_and_charts_present(built):
    html, _ = built
    assert "prefers-color-scheme: dark" in html
    assert '[data-theme="dark"]' in html
    assert '[data-theme="light"]' in html
    # Charts rendered as inline SVG riding CSS variables.
    assert "var(--chart-1)" in html
    assert "<svg" in html


def test_size_cap_enforced(tmp_path, monkeypatch):
    from app.quality import audit as audit_mod

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    briefs, reports = _write_inputs(tmp_path, now)
    monkeypatch.setattr(brief_mod, "BRIEFS_DIR", briefs)
    monkeypatch.setattr(artifact_mod, "REPORTS_DIR", reports)
    monkeypatch.setattr(audit_mod, "AUDIT_PATH", tmp_path / "facts_audit.json")
    monkeypatch.setattr(artifact_mod, "PROJECT_ROOT", tmp_path)

    async def run():
        await _seed(tmp_path / "a.db", now)
        try:
            with pytest.raises(artifact_mod.ArtifactValidationError):
                await artifact_mod.build_artifact(
                    out_path=tmp_path / "small.html", max_bytes=1000)
        finally:
            await db.engine.dispose()

    asyncio.run(run())
    assert not (tmp_path / "small.html").exists()


def test_empty_db_degrades_gracefully(tmp_path, monkeypatch):
    """No boards, no brief, no landscape — build still succeeds with
    placeholder states (mirrors trends.py's has_data philosophy)."""
    from app.quality import audit as audit_mod

    empty_briefs = tmp_path / "briefs"
    empty_reports = tmp_path / "reports"
    empty_briefs.mkdir()
    empty_reports.mkdir()
    monkeypatch.setattr(brief_mod, "BRIEFS_DIR", empty_briefs)
    monkeypatch.setattr(artifact_mod, "REPORTS_DIR", empty_reports)
    monkeypatch.setattr(audit_mod, "AUDIT_PATH", tmp_path / "facts_audit.json")
    monkeypatch.setattr(artifact_mod, "PROJECT_ROOT", tmp_path)

    db.DATABASE_URL = f"sqlite+aiosqlite:///{(tmp_path / 'e.db').as_posix()}"

    async def run():
        path = await artifact_mod.build_artifact(out_path=tmp_path / "e.html")
        await db.engine.dispose()
        return path

    html = asyncio.run(run()).read_text(encoding="utf-8")
    assert "No monthly brief generated yet" in html
    assert "No national landscape report generated yet" in html
    assert not artifact_mod.validate_artifact_html(html)


def test_validate_artifact_html_unit():
    v = artifact_mod.validate_artifact_html
    ok = "<title>x</title><style></style><div><header>h</header></div>"
    assert v(ok) == []
    assert any("wrapper" in s for s in v("<title>x</title><body>"))
    assert any("src" in s for s in
               v('<title>x</title><img src="https://evil.example/x.png">'))
    assert any("resource-loading" in s for s in
               v('<title>x</title><link rel="stylesheet">'))
    assert any("<title>" in s for s in v("<div>no title</div>"))
    assert any("bytes" in s for s in v("<title>x</title>" + "a" * 100,
                                       max_bytes=50))
