"""Route smoke tests — verify every page loads with seeded data."""
import pytest

from app import database as db
from app.models import Board


# ---------------------------------------------------------------------------
# National Overview
# ---------------------------------------------------------------------------

async def test_national_overview(client, seed_full_chain):
    chain = await seed_full_chain()
    resp = await client.get("/")
    assert resp.status_code == 200
    html = resp.text
    assert "Texas Medical Board" in html or "TX_MD" in html
    assert "1" in html  # at least 1 meeting


async def test_national_overview_empty_db(client, seed_board):
    await seed_board()
    resp = await client.get("/")
    assert resp.status_code == 200


# ---------------------------------------------------------------------------
# State View
# ---------------------------------------------------------------------------

async def test_state_view(client, seed_full_chain):
    await seed_full_chain()
    resp = await client.get("/state/TX")
    assert resp.status_code == 200
    assert "Texas Medical Board" in resp.text


async def test_state_view_lowercase(client, seed_full_chain):
    await seed_full_chain()
    resp = await client.get("/state/tx")
    assert resp.status_code == 200


async def test_state_view_404(client):
    resp = await client.get("/state/ZZ")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Board View
# ---------------------------------------------------------------------------

async def test_board_view(client, seed_full_chain):
    chain = await seed_full_chain()
    resp = await client.get("/board/TX_MD")
    assert resp.status_code == 200
    assert "Texas Medical Board" in resp.text


async def test_board_view_404(client):
    resp = await client.get("/board/NOPE_MD")
    assert resp.status_code == 404


async def test_board_redirect(client, seed_full_chain):
    await seed_full_chain()
    resp = await client.get("/board/TX/TX_MD", follow_redirects=False)
    assert resp.status_code == 301
    assert "/board/TX_MD" in resp.headers["location"]


async def test_board_view_no_meetings(client, seed_board):
    await seed_board()
    resp = await client.get("/board/TX_MD")
    assert resp.status_code == 200


# ---------------------------------------------------------------------------
# Meeting View
# ---------------------------------------------------------------------------

async def test_meeting_view(client, seed_full_chain):
    chain = await seed_full_chain()
    mid = chain["meeting"].id
    resp = await client.get(f"/meeting/{mid}")
    assert resp.status_code == 200
    assert "Texas Medical Board" in resp.text


async def test_meeting_view_404(client):
    resp = await client.get("/meeting/99999")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Page Viewer
# ---------------------------------------------------------------------------

async def test_page_viewer(client, seed_full_chain):
    chain = await seed_full_chain()
    pid = chain["page"].id
    resp = await client.get(f"/page/{pid}")
    assert resp.status_code == 200
    assert "page" in resp.text.lower()


async def test_page_viewer_404(client):
    resp = await client.get("/page/99999")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

async def test_search_all(client, seed_full_chain):
    chain = await seed_full_chain()
    resp = await client.get("/search?period=all")
    assert resp.status_code == 200
    html = resp.text
    assert "Discipline" in html or "Telehealth" in html
    assert "page" in html.lower()


async def test_search_by_topic(client, seed_full_chain):
    chain = await seed_full_chain()
    resp = await client.get("/search?topic=Discipline&period=all")
    assert resp.status_code == 200
    assert "Discipline" in resp.text


async def test_search_by_state(client, seed_full_chain):
    chain = await seed_full_chain()
    resp = await client.get("/search?state=TX&period=all")
    assert resp.status_code == 200


async def test_search_fts(client, seed_full_chain):
    chain = await seed_full_chain()
    from app.pipeline.fts import rebuild_fts_index
    await rebuild_fts_index()
    resp = await client.get("/search?q=telehealth&period=all")
    assert resp.status_code == 200


async def test_search_no_results(client, seed_full_chain):
    chain = await seed_full_chain()
    from app.pipeline.fts import rebuild_fts_index
    await rebuild_fts_index()
    resp = await client.get("/search?q=xyznonexistent&period=all")
    assert resp.status_code == 200
    assert "No results" in resp.text


async def test_search_htmx(client, seed_full_chain):
    chain = await seed_full_chain()
    resp = await client.get("/search?period=all", headers={"HX-Request": "true"})
    assert resp.status_code == 200
    assert "<!DOCTYPE" not in resp.text


async def test_search_empty_db(client, seed_board):
    await seed_board()
    resp = await client.get("/search?period=all")
    assert resp.status_code == 200


# ---------------------------------------------------------------------------
# Pipeline UI
# ---------------------------------------------------------------------------

async def test_pipeline_list(client, seed_pipeline_run):
    run = await seed_pipeline_run()
    resp = await client.get("/pipeline/")
    assert resp.status_code == 200


async def test_pipeline_list_empty(client):
    resp = await client.get("/pipeline/")
    assert resp.status_code == 200


async def test_pipeline_detail(client, seed_pipeline_run):
    run = await seed_pipeline_run()
    resp = await client.get(f"/pipeline/{run.id}")
    assert resp.status_code == 200
    assert "collect" in resp.text.lower()


async def test_pipeline_detail_404(client):
    resp = await client.get("/pipeline/99999")
    assert resp.status_code == 404


async def test_pipeline_start(client):
    resp = await client.post("/pipeline/start")
    assert resp.status_code == 202


# ---------------------------------------------------------------------------
# File Serving
# ---------------------------------------------------------------------------

async def test_page_image(client, seed_full_chain):
    chain = await seed_full_chain()
    pid = chain["page"].id
    resp = await client.get(f"/page-image/{pid}")
    assert resp.status_code == 200
    assert resp.headers["content-type"] == "image/png"


async def test_page_image_404(client):
    resp = await client.get("/page-image/99999")
    assert resp.status_code == 404


async def test_page_thumb(client, seed_full_chain):
    chain = await seed_full_chain()
    pid = chain["page"].id
    resp = await client.get(f"/page-thumb/{pid}")
    assert resp.status_code == 200
    assert resp.headers["content-type"] == "image/png"


async def test_page_thumb_404(client):
    resp = await client.get("/page-thumb/99999")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Redirects & Triggers
# ---------------------------------------------------------------------------

async def test_topic_redirect(client):
    resp = await client.get("/topic/telehealth", follow_redirects=False)
    assert resp.status_code == 301
    assert "/search?topic=telehealth" in resp.headers["location"]


async def test_collect_trigger(client, seed_board):
    await seed_board()
    resp = await client.post("/collect/TX_MD")
    assert resp.status_code == 202


async def test_collect_trigger_404(client):
    resp = await client.post("/collect/NOPE_MD")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

async def test_report_missing(client, tmp_path):
    from unittest.mock import patch
    empty_dir = tmp_path / "empty_reports"
    empty_dir.mkdir()
    with patch("app.web.server.REPORTS_DIR", empty_dir):
        resp = await client.get("/report")
        assert resp.status_code == 200
        assert "No report" in resp.text


async def test_report_exists(client, tmp_path):
    from unittest.mock import patch
    from app.config import REPORTS_DIR
    report_dir = tmp_path / "reports"
    report_dir.mkdir()
    report_file = report_dir / "2026-04-01-board-landscape.md"
    report_file.write_text("# National Landscape\n\nTest report content.", encoding="utf-8")
    with patch("app.web.server.REPORTS_DIR", report_dir):
        resp = await client.get("/report")
        assert resp.status_code == 200
        assert "Test report content" in resp.text
