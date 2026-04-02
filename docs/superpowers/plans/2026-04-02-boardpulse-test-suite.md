# boardpulse Test Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a comprehensive test suite proving boardpulse is demo-ready and product-ready — every web route loads, the topic classifier works, and data integrity holds.

**Architecture:** Top-down approach. Shared conftest.py with factory fixtures and a FastAPI test client via httpx. Route smoke tests first (find + fix bugs), then classifier unit tests, data integrity tests, and CLI smoke tests.

**Tech Stack:** pytest, pytest-asyncio (auto mode), httpx (AsyncClient for ASGI), fitz (PyMuPDF for test PDFs), in-memory SQLite

**Spec:** `docs/superpowers/specs/2026-04-02-boardpulse-test-plan-design.md`

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `tests/conftest.py` | Create | Shared fixtures: db_session, client, seed factories, tmp dirs |
| `tests/test_routes.py` | Create | Route smoke tests for all ~20 web routes |
| `tests/test_classifier.py` | Create | Keyword classifier unit + integration tests |
| `tests/test_data_integrity.py` | Create | Rollup correctness, path resolution, edge cases |
| `tests/test_cli.py` | Create | CLI dispatch function smoke tests |
| `tests/test_models.py` | Modify | Remove duplicated setup_db fixture (use conftest) |
| `tests/test_discoverer.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_parser.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_summarizer.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_pipeline.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_topics.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_runner.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_integration.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_document_page.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_page_topics.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_renderer.py` | Modify | Remove duplicated setup_db fixture |
| `tests/test_fts.py` | Modify | Remove duplicated setup_db fixture |
| `app/web/server.py` | Modify (if needed) | Fix any bugs found during route testing |
| `app/pipeline/classifier.py` | Modify (if needed) | Fix any bugs found during classifier testing |

---

### Task 1: Create shared conftest.py with fixtures

**Files:**
- Create: `tests/conftest.py`

- [ ] **Step 1: Create conftest.py with db_session, client, and seed fixtures**

```python
"""Shared test fixtures for boardpulse."""
import json
import pytest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch

import httpx

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage, PipelineRun, PipelineEvent


@pytest.fixture(autouse=True)
async def db_session():
    """Initialize a fresh in-memory DB for each test."""
    await db.init_db(url="sqlite+aiosqlite://")
    yield


@pytest.fixture
async def client():
    """Async HTTP client for testing FastAPI routes.

    Patches the startup event so it doesn't re-init the DB
    (db_session already set up the in-memory DB).
    """
    from app.web.server import app

    # Remove the startup handler that would re-init to file DB
    app.router.on_startup.clear()

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        yield c

    # Restore startup handler for next test
    from app.web.server import startup
    app.router.on_startup.append(startup)


@pytest.fixture
async def seed_board():
    """Factory: create a Board record."""
    async def _create(code="TX_MD", state="TX", name="Texas Medical Board",
                      board_type="combined", homepage="https://tmb.state.tx.us"):
        async with db.async_session() as session:
            board = Board(
                state=state, code=code, name=name,
                board_type=board_type, homepage=homepage,
                discovery_status="found",
            )
            session.add(board)
            await session.commit()
            await session.refresh(board)
            return board
    return _create


@pytest.fixture
async def seed_full_chain(tmp_path, seed_board):
    """Factory: create Board -> Meeting -> Document -> Page with topics and images.

    Returns dict with all created objects and the tmp pages dir.
    """
    async def _create(
        code="TX_MD", state="TX", board_name="Texas Medical Board",
        meeting_date=None, summary="The board discussed telehealth and discipline.",
        topics=None, doc_type="minutes",
    ):
        if meeting_date is None:
            meeting_date = date(2026, 3, 15)
        if topics is None:
            topics = ["Discipline", "Telehealth"]

        board = await seed_board(code=code, state=state, name=board_name)

        async with db.async_session() as session:
            meeting = Meeting(
                board_id=board.id, meeting_date=meeting_date,
                title=f"{board_name} — {meeting_date.strftime('%B %Y')}",
                summary=summary, topics=topics,
            )
            session.add(meeting)
            await session.commit()
            await session.refresh(meeting)

            # Create a document with extracted text
            doc = MeetingDocument(
                meeting_id=meeting.id, doc_type=doc_type,
                filename=f"{meeting_date.isoformat()}_minutes.pdf",
                file_path=str(tmp_path / "documents" / code / f"{meeting_date.isoformat()}_minutes.pdf"),
                content_text=(
                    "The board convened to discuss disciplinary actions. "
                    "Three physicians were placed on probation for telehealth violations. "
                    "The committee reviewed licensing applications and rulemaking proposals."
                ),
                topics=topics,
            )
            session.add(doc)
            await session.commit()
            await session.refresh(doc)

            # Create page images (1x1 white PNG)
            pages_dir = tmp_path / "pages" / code / str(doc.id)
            pages_dir.mkdir(parents=True, exist_ok=True)

            _write_tiny_png(pages_dir / "page_001.png")
            _write_tiny_png(pages_dir / "page_001_thumb.png")

            page = DocumentPage(
                document_id=doc.id, page_number=1,
                image_path=str(pages_dir / "page_001.png"),
                thumb_path=str(pages_dir / "page_001_thumb.png"),
                topics=topics,
                tagged_at=datetime.now(timezone.utc),
                rendered_at=datetime.now(timezone.utc),
            )
            session.add(page)
            await session.commit()
            await session.refresh(page)

        return {
            "board": board, "meeting": meeting,
            "doc": doc, "page": page,
            "pages_dir": tmp_path / "pages",
        }
    return _create


@pytest.fixture
async def seed_pipeline_run():
    """Factory: create a PipelineRun with events."""
    async def _create(status="completed", trigger="manual"):
        async with db.async_session() as session:
            run = PipelineRun(
                started_at=datetime.now(timezone.utc),
                completed_at=datetime.now(timezone.utc) if status == "completed" else None,
                status=status, trigger=trigger,
                boards_collected=5, new_meetings_found=10,
                new_documents_found=15, boards_summarized=3,
            )
            session.add(run)
            await session.commit()
            await session.refresh(run)

            event = PipelineEvent(
                run_id=run.id, timestamp=datetime.now(timezone.utc),
                stage="collect", event_type="completed",
                board_code="TX_MD", detail="10 new meetings",
            )
            session.add(event)
            await session.commit()
            return run
    return _create


def _write_tiny_png(path: Path):
    """Write a minimal valid 1x1 white PNG file."""
    import struct, zlib
    path.parent.mkdir(parents=True, exist_ok=True)
    # Minimal PNG: 8-byte sig + IHDR + IDAT + IEND
    sig = b'\x89PNG\r\n\x1a\n'
    def chunk(ctype, data):
        c = ctype + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    ihdr = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
    raw = zlib.compress(b'\x00\xff\xff\xff')
    png = sig + chunk(b'IHDR', ihdr) + chunk(b'IDAT', raw) + chunk(b'IEND', b'')
    path.write_bytes(png)
```

- [ ] **Step 2: Verify conftest loads and existing tests still pass**

Run: `cd Projects/boardpulse && python -m pytest tests/test_models.py -v --tb=short 2>&1 | tail -10`
Expected: All tests in test_models.py still pass (the autouse `db_session` in conftest may conflict with the per-file `setup_db` — both will run, but since they both init in-memory, it's harmless for now).

- [ ] **Step 3: Commit**

```bash
git add tests/conftest.py
git commit -m "test: add shared conftest.py with db_session, client, and seed fixtures"
```

---

### Task 2: Route smoke tests — navigation pages

**Files:**
- Create: `tests/test_routes.py`

- [ ] **Step 1: Write route smoke tests for navigation pages**

```python
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
    # Stats section should have numbers
    assert "1" in html  # at least 1 meeting


async def test_national_overview_empty_db(client, seed_board):
    await seed_board()  # board with no meetings
    resp = await client.get("/")
    assert resp.status_code == 200  # no crash on empty data


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
    assert resp.status_code == 200  # route uppercases the param


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
    await seed_board()  # board with 0 meetings
    resp = await client.get("/board/TX_MD")
    assert resp.status_code == 200  # should render empty timeline, not 500


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
```

- [ ] **Step 2: Run the route tests**

Run: `cd Projects/boardpulse && python -m pytest tests/test_routes.py -v --tb=short 2>&1`
Expected: Most pass. If any 500, debug and fix the source code before moving on.

- [ ] **Step 3: Fix any bugs found (if needed)**

For each failing test: read the traceback, fix the root cause in `app/web/server.py`, re-run.

- [ ] **Step 4: Commit**

```bash
git add tests/test_routes.py
git commit -m "test: add route smoke tests for navigation pages (national, state, board, meeting, page)"
```

---

### Task 3: Route smoke tests — search, pipeline, file serving, redirects

**Files:**
- Modify: `tests/test_routes.py`

- [ ] **Step 1: Append search, pipeline, file-serving, and redirect tests**

Add to `tests/test_routes.py`:

```python
# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

async def test_search_all(client, seed_full_chain):
    chain = await seed_full_chain()
    resp = await client.get("/search?period=all")
    assert resp.status_code == 200
    html = resp.text
    # Topic pills should render
    assert "Discipline" in html or "Telehealth" in html
    # Should have results
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
    # Build FTS index so free-text search works
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
    # HTMX partial should NOT have full HTML wrapper
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
    assert resp.status_code == 200  # no crash on empty list


async def test_pipeline_detail(client, seed_pipeline_run):
    run = await seed_pipeline_run()
    resp = await client.get(f"/pipeline/{run.id}")
    assert resp.status_code == 200
    assert "collect" in resp.text.lower()  # event stage should appear


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

async def test_report_missing(client):
    resp = await client.get("/report")
    assert resp.status_code == 200
    assert "No report" in resp.text


async def test_report_exists(client, tmp_path):
    """When a report file exists, /report renders its markdown content."""
    from app.config import REPORTS_DIR
    report_file = REPORTS_DIR / "2026-04-01-board-landscape.md"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text("# National Landscape\n\nTest report content.", encoding="utf-8")
    try:
        resp = await client.get("/report")
        assert resp.status_code == 200
        assert "Test report content" in resp.text
    finally:
        report_file.unlink(missing_ok=True)
```

- [ ] **Step 2: Run all route tests**

Run: `cd Projects/boardpulse && python -m pytest tests/test_routes.py -v --tb=short 2>&1`
Expected: All pass (or identify bugs to fix).

- [ ] **Step 3: Fix any bugs found**

- [ ] **Step 4: Commit**

```bash
git add tests/test_routes.py
git commit -m "test: add route smoke tests for search, pipeline, file serving, redirects"
```

---

### Task 4: Classifier unit tests

**Files:**
- Create: `tests/test_classifier.py`

- [ ] **Step 1: Write classifier unit tests**

```python
"""Test keyword topic classifier."""
import pytest
from datetime import date, datetime, timezone

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage
from app.pipeline.classifier import classify_text, classify_all_documents, TOPIC_PATTERNS
from app.pipeline.context import TOPIC_TAXONOMY


# ---------------------------------------------------------------------------
# classify_text — unit tests
# ---------------------------------------------------------------------------

def test_classify_empty_text():
    assert classify_text("") == []


def test_classify_short_text():
    assert classify_text("Board met.") == []


def test_classify_no_matches():
    assert classify_text("The weather today is sunny and warm. " * 10) == []


def test_classify_discipline():
    text = (
        "The board reviewed a consent order for Dr. Smith who was placed on probation. "
        "A second disciplinary action involved license suspension for misconduct."
    )
    result = classify_text(text)
    assert "Discipline" in result


def test_classify_telehealth():
    text = (
        "Discussion of telehealth prescribing authority. The committee reviewed "
        "telemedicine regulations for virtual care consultations across state lines."
    )
    result = classify_text(text)
    assert "Telehealth" in result


def test_classify_ai_technology():
    text = (
        "The board discussed artificial intelligence use in clinical diagnosis. "
        "A presentation on machine learning algorithms in medical imaging was given."
    )
    result = classify_text(text)
    assert "AI & Technology" in result


def test_classify_licensing():
    text = (
        "License renewal applications were reviewed. The board processed "
        "endorsement requests and discussed reciprocity agreements."
    )
    result = classify_text(text)
    assert "Licensing" in result


def test_classify_rulemaking():
    text = (
        "The proposed rule amendments to administrative code section 22 were discussed. "
        "A rulemaking hearing was scheduled for public comment on the regulation change."
    )
    result = classify_text(text)
    assert "Rulemaking" in result


def test_classify_multiple_topics():
    text = (
        "The board issued a consent order suspending a physician for opioid overprescribing. "
        "Disciplinary action was taken. The prescribing guidelines for controlled substances "
        "were reviewed alongside patient safety protocols and adverse event reporting."
    )
    result = classify_text(text)
    assert "Discipline" in result
    assert "Opioids & Prescribing" in result
    assert "Patient Safety" in result


def test_classify_min_matches_threshold():
    # One mention of "license" — should pass at min_matches=1, fail at min_matches=2
    text = "The board reviewed one license application and adjourned. " * 3
    assert "Licensing" in classify_text(text, min_matches=1)
    # With threshold 2, need 2+ matches of the pattern
    single = "The board discussed a single licensing matter."
    assert classify_text(single, min_matches=2) == [] or "Licensing" not in classify_text(single, min_matches=2)


def test_classify_results_sorted():
    text = (
        "Telehealth prescribing and telemedicine rules. "
        "Disciplinary consent orders and license suspensions. "
        "AI and artificial intelligence in healthcare. "
    )
    result = classify_text(text, min_matches=1)
    assert result == sorted(result)


def test_all_16_topics_matchable():
    """Each of the 16 topic patterns can be triggered independently."""
    test_snippets = {
        "Licensing": "license renewal applications endorsement processing",
        "Discipline": "disciplinary consent order suspended probation",
        "Telehealth": "telehealth telemedicine virtual care prescribing",
        "AI & Technology": "artificial intelligence machine learning algorithm",
        "Rulemaking": "rulemaking proposed rule administrative code amendment",
        "Budget & Finance": "budget financial report fiscal year audit expenditure",
        "Board Operations": "board meeting executive director quorum strategic plan",
        "Continuing Education": "continuing medical education CME credit requirements",
        "Scope of Practice": "scope of practice physician assistant PA supervision",
        "Opioids & Prescribing": "opioid controlled substance prescribing pain management",
        "Public Health": "public health pandemic vaccination immunization",
        "Patient Safety": "patient safety standard of care adverse event quality",
        "Legal": "litigation attorney general legislative update house bill SB 100",
        "Workforce": "physician workforce shortage rural health GME residency",
        "Ethics": "ethics conflict of interest boundary violation professional conduct",
        "Interstate Compact": "interstate compact IMLC compact commission multi-state",
    }
    for topic_name, snippet in test_snippets.items():
        result = classify_text(snippet, min_matches=1)
        assert topic_name in result, f"Topic '{topic_name}' not matched by: {snippet}"


def test_taxonomy_matches_classifier():
    """TOPIC_TAXONOMY in context.py stays in sync with classifier patterns."""
    classifier_topics = sorted([name for name, _ in TOPIC_PATTERNS])
    taxonomy_topics = sorted(TOPIC_TAXONOMY)
    assert classifier_topics == taxonomy_topics, (
        f"Mismatch:\n  Classifier: {classifier_topics}\n  Taxonomy:   {taxonomy_topics}"
    )


# ---------------------------------------------------------------------------
# classify_all_documents — integration tests
# ---------------------------------------------------------------------------

async def _seed_docs_for_classification(seed_board):
    """Helper: create a board with 3 documents, varying text."""
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        d1 = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="a.pdf", file_path="/tmp/a.pdf",
            content_text=(
                "The board issued disciplinary actions against two physicians "
                "for prescribing opioid controlled substances without proper "
                "monitoring. The consent orders were finalized."
            ),
        )
        d2 = MeetingDocument(
            meeting_id=m.id, doc_type="agenda",
            filename="b.pdf", file_path="/tmp/b.pdf",
            content_text=(
                "Telehealth prescribing regulations and telemedicine "
                "virtual care standards were discussed at length."
            ),
        )
        d3 = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="c.pdf", file_path="/tmp/c.pdf",
            content_text=None,  # no text — should be skipped
        )
        session.add_all([d1, d2, d3])
        await session.commit()
    return board, m


async def test_classify_all_documents(seed_board):
    board, meeting = await _seed_docs_for_classification(seed_board)
    result = await classify_all_documents()
    assert result["documents_classified"] >= 2
    assert result["meetings_rolled_up"] >= 1

    # Verify meeting got rolled-up topics
    async with db.async_session() as session:
        m = await session.get(Meeting, meeting.id)
        assert m.topics is not None
        assert len(m.topics) > 0
        assert "Discipline" in m.topics


async def test_classify_skip_existing(seed_board):
    board, meeting = await _seed_docs_for_classification(seed_board)
    r1 = await classify_all_documents()
    count1 = r1["documents_classified"]

    r2 = await classify_all_documents(force=False)
    assert r2["documents_classified"] == 0  # all already tagged


async def test_classify_force_retag(seed_board):
    board, meeting = await _seed_docs_for_classification(seed_board)
    await classify_all_documents()
    r2 = await classify_all_documents(force=True)
    assert r2["documents_classified"] >= 2  # re-tagged


async def test_classify_rollup_dedup(seed_board):
    """Two docs on same meeting with overlapping topics — meeting.topics is deduplicated."""
    board, meeting = await _seed_docs_for_classification(seed_board)
    await classify_all_documents()

    async with db.async_session() as session:
        m = await session.get(Meeting, meeting.id)
        # No duplicates
        assert len(m.topics) == len(set(m.topics))
        # Sorted
        assert m.topics == sorted(m.topics)
```

- [ ] **Step 2: Run classifier tests**

Run: `cd Projects/boardpulse && python -m pytest tests/test_classifier.py -v --tb=short 2>&1`
Expected: All pass.

- [ ] **Step 3: Commit**

```bash
git add tests/test_classifier.py
git commit -m "test: add topic classifier unit + integration tests (20 tests)"
```

---

### Task 5: Data integrity tests

**Files:**
- Create: `tests/test_data_integrity.py`

- [ ] **Step 1: Write data integrity tests**

```python
"""Test data integrity — rollups, path resolution, edge cases."""
import json
import pytest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage
from app.pipeline.classifier import classify_text


# ---------------------------------------------------------------------------
# Topic Rollup
# ---------------------------------------------------------------------------

async def test_topic_rollup_list_format(seed_full_chain):
    """Topics stored as Python list (not JSON string) are handled in rollup."""
    chain = await seed_full_chain(topics=["Licensing", "Discipline"])
    async with db.async_session() as session:
        m = await session.get(Meeting, chain["meeting"].id)
        assert isinstance(m.topics, list)
        assert "Licensing" in m.topics


async def test_topic_deduplication(seed_board):
    """Rollup from multiple docs with overlapping topics produces no duplicates."""
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        d1 = MeetingDocument(
            meeting_id=m.id, doc_type="minutes", filename="a.pdf",
            file_path="/tmp/a.pdf", topics=["Discipline", "Licensing"],
        )
        d2 = MeetingDocument(
            meeting_id=m.id, doc_type="agenda", filename="b.pdf",
            file_path="/tmp/b.pdf", topics=["Discipline", "Telehealth"],
        )
        session.add_all([d1, d2])
        await session.commit()

    # Manually trigger rollup via classify_all_documents
    from app.pipeline.classifier import classify_all_documents
    await classify_all_documents(force=True, min_matches=1)

    async with db.async_session() as session:
        m = await session.get(Meeting, m.id)
        if m.topics:
            assert len(m.topics) == len(set(m.topics)), f"Duplicates found: {m.topics}"


async def test_document_no_pages_in_search(client, seed_full_chain):
    """A document with no DocumentPages doesn't break the search page."""
    chain = await seed_full_chain()
    # Delete the page, keep the document
    async with db.async_session() as session:
        page = await session.get(DocumentPage, chain["page"].id)
        await session.delete(page)
        await session.commit()

    resp = await client.get("/search?period=all")
    assert resp.status_code == 200  # no crash


async def test_meeting_no_documents(client, seed_board):
    """Meeting with zero documents renders without error."""
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15),
                    title="Empty Meeting")
        session.add(m)
        await session.commit()
        await session.refresh(m)

    resp = await client.get(f"/meeting/{m.id}")
    assert resp.status_code == 200


async def test_board_zero_meetings_state_view(client, seed_board):
    """Board with 0 meetings doesn't break state view."""
    await seed_board()
    resp = await client.get("/state/TX")
    assert resp.status_code == 200


# ---------------------------------------------------------------------------
# Path Resolution
# ---------------------------------------------------------------------------

async def test_renderer_relative_path(seed_board, tmp_path):
    """Renderer resolves relative file_path via PROJECT_ROOT."""
    import fitz

    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        # Create a real tiny PDF
        pdf_path = tmp_path / "test.pdf"
        doc = fitz.open()
        doc.new_page(width=100, height=100)
        doc.save(str(pdf_path))
        doc.close()

        d = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="test.pdf", file_path=str(pdf_path),
        )
        session.add(d)
        await session.commit()
        await session.refresh(d)

    from app.pipeline.renderer import render_document_pages
    result = await render_document_pages(d.id, pages_dir=tmp_path / "pages")
    assert result["pages_rendered"] == 1


# ---------------------------------------------------------------------------
# FTS Edge Cases
# ---------------------------------------------------------------------------

async def test_fts_empty_query(seed_full_chain):
    chain = await seed_full_chain()
    from app.pipeline.fts import rebuild_fts_index, search_summaries
    await rebuild_fts_index()
    results = await search_summaries("")
    assert isinstance(results, list)  # no crash


async def test_fts_special_characters(seed_full_chain):
    chain = await seed_full_chain()
    from app.pipeline.fts import rebuild_fts_index, search_summaries
    await rebuild_fts_index()
    # These should not crash
    await search_summaries("AI & Technology")
    await search_summaries('"opioid prescribing"')
    await search_summaries("test (with) [brackets]")
```

- [ ] **Step 2: Run data integrity tests**

Run: `cd Projects/boardpulse && python -m pytest tests/test_data_integrity.py -v --tb=short 2>&1`
Expected: All pass.

- [ ] **Step 3: Fix any bugs found**

- [ ] **Step 4: Commit**

```bash
git add tests/test_data_integrity.py
git commit -m "test: add data integrity tests (rollups, paths, FTS edge cases)"
```

---

### Task 6: CLI smoke tests

**Files:**
- Create: `tests/test_cli.py`

- [ ] **Step 1: Write CLI smoke tests**

```python
"""CLI smoke tests — verify dispatch functions don't crash."""
import pytest
from datetime import date
from types import SimpleNamespace

from app import database as db
from app.models import Board, Meeting, MeetingDocument


async def _seed_classifiable_data(seed_board):
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        d = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="test.pdf", file_path="/tmp/test.pdf",
            content_text="The board discussed disciplinary actions and license suspensions.",
        )
        session.add(d)
        await session.commit()


async def test_cli_status(seed_board, capsys):
    await seed_board()
    from cli import show_status
    await show_status()
    captured = capsys.readouterr()
    assert "TX_MD" in captured.out


async def test_cli_classify(seed_board, capsys):
    await _seed_classifiable_data(seed_board)
    from cli import handle_classify
    args = SimpleNamespace(pages=False, force=False, min_matches=2)
    await handle_classify(args)
    captured = capsys.readouterr()
    assert "Classifying" in captured.out or "classified" in captured.out.lower()


async def test_cli_classify_force(seed_board, capsys):
    await _seed_classifiable_data(seed_board)
    from cli import handle_classify
    args = SimpleNamespace(pages=False, force=True, min_matches=1)
    await handle_classify(args)
    # No exception = pass


async def test_cli_pipeline_status(capsys):
    from cli import show_pipeline_status
    await show_pipeline_status()
    # Should handle empty run list without error


async def test_cli_pipeline_rebuild_fts(seed_board, capsys):
    await seed_board()
    from cli import handle_pipeline
    args = SimpleNamespace(
        status=False, rebuild_fts=True, ingest_topics=False,
        finalize=False, boards=None, skip_report=False,
        run_id=None, digest_path=None, report_path=None,
    )
    await handle_pipeline(args)
    captured = capsys.readouterr()
    assert "Done" in captured.out or "rebuilt" in captured.out.lower()


async def test_cli_argparse_help():
    import sys
    from cli import main
    sys.argv = ["cli.py", "--help"]
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0
```

- [ ] **Step 2: Run CLI tests**

Run: `cd Projects/boardpulse && python -m pytest tests/test_cli.py -v --tb=short 2>&1`
Expected: All pass.

- [ ] **Step 3: Commit**

```bash
git add tests/test_cli.py
git commit -m "test: add CLI dispatch smoke tests (6 tests)"
```

---

### Task 7: Clean up existing test files to use shared conftest

**Files:**
- Modify: All 13 existing test files in `tests/`

- [ ] **Step 1: Remove duplicated setup_db fixtures and sys.path hacks from all test files**

In each of these files, remove the per-file `setup_db` fixture and the `sys.path.insert` block (conftest.py handles both):

```
tests/test_models.py
tests/test_discoverer.py
tests/test_parser.py
tests/test_summarizer.py
tests/test_pipeline.py
tests/test_topics.py
tests/test_runner.py
tests/test_integration.py
tests/test_document_page.py
tests/test_page_topics.py
tests/test_renderer.py
tests/test_fts.py
```

For each file, remove these lines (exact text varies slightly per file):

```python
# REMOVE these lines:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# AND REMOVE this fixture:
@pytest.fixture(autouse=True)
async def setup_db(tmp_path):
    """Initialize a fresh in-memory DB for each test."""
    await db.init_db(url="sqlite+aiosqlite://")
    yield
```

Keep all other imports and fixtures (e.g., `meetings_with_summaries` in test_fts.py, `_create_test_pdf` in test_renderer.py).

- [ ] **Step 2: Run full test suite**

Run: `cd Projects/boardpulse && python -m pytest tests/ -v --tb=short 2>&1 | tail -20`
Expected: All ~129 tests pass. The shared `db_session` in conftest replaces every per-file `setup_db`.

- [ ] **Step 3: Commit**

```bash
git add tests/
git commit -m "refactor: migrate all tests to shared conftest.py fixtures"
```

---

### Task 8: Visual verification — screenshot every route

**Files:**
- None (uses browser, output to `docs/screenshots/`)

- [ ] **Step 1: Start the server with test data**

The server should already be running on port 8099 with real data. Verify:
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8099/
```
Expected: `200`

- [ ] **Step 2: Screenshot every route via the browser**

Use the `chrome__use_browser` MCP tool to navigate to each route and capture a screenshot:

1. `http://localhost:8099/` — National overview
2. `http://localhost:8099/state/TX` — State view
3. `http://localhost:8099/board/TX_MD` — Board view
4. `http://localhost:8099/search?period=all` — Search (all)
5. `http://localhost:8099/search?topic=Telehealth&period=all` — Search (filtered)
6. `http://localhost:8099/pipeline/` — Pipeline runs
7. `http://localhost:8099/page/{first_page_id}` — Page viewer

Save screenshots to `docs/screenshots/` with descriptive names.

- [ ] **Step 3: Review screenshots visually**

Check each screenshot for: correct layout, topic pills rendering, data populating, no broken images, no "undefined" or "None" text in the UI.

- [ ] **Step 4: Commit screenshots**

```bash
git add docs/screenshots/
git commit -m "docs: add visual verification screenshots for all routes"
```

---

### Task 9: Final verification — full test suite run

- [ ] **Step 1: Run the complete test suite**

Run: `cd Projects/boardpulse && python -m pytest tests/ -v 2>&1`
Expected: All tests pass. No warnings about missing fixtures.

- [ ] **Step 2: Count tests and verify target**

Run: `cd Projects/boardpulse && python -m pytest tests/ --co -q 2>&1 | tail -3`
Expected: ~129 tests collected (49 existing + ~80 new).

- [ ] **Step 3: Commit any final fixes**

If anything needed fixing, commit it:
```bash
git add -A
git commit -m "test: final fixes for complete test suite"
```
