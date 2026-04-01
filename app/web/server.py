"""boardpulse web dashboard — Palantir-style intelligence interface."""
import json
import os
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, func, distinct

from app.models import Board, Meeting, MeetingDocument
from app.config import SCREENSHOTS_DIR, DOCUMENTS_DIR, REPORTS_DIR, EXHIBITS_DIR
import app.database as db

# Paths
WEB_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = WEB_DIR / "templates"
STATIC_DIR = WEB_DIR / "static"

# App
app = FastAPI(title="boardpulse", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

templates.env.filters["basename"] = os.path.basename


# State name lookup
STATE_NAMES = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'DC': 'District of Columbia', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii',
    'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine',
    'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
    'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska',
    'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
    'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island',
    'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas',
    'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
}

templates.env.globals["STATE_NAMES"] = STATE_NAMES


def _relative_screenshot_path(absolute_path: str) -> str:
    try:
        return str(Path(absolute_path).relative_to(SCREENSHOTS_DIR))
    except ValueError:
        return absolute_path


templates.env.globals["relative_screenshot"] = _relative_screenshot_path


@app.on_event("startup")
async def startup():
    from app.database import init_db
    await init_db()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

async def _get_all_topics_with_counts() -> list[dict]:
    """Get all unique topics across meetings with their counts."""
    async with db.async_session() as session:
        meetings = (await session.execute(
            select(Meeting.topics, Meeting.board_id)
            .where(Meeting.topics.isnot(None))
        )).all()

    topic_counts: dict[str, int] = {}
    topic_boards: dict[str, set] = {}
    for topics_json, board_id in meetings:
        if not topics_json:
            continue
        tags = topics_json if isinstance(topics_json, list) else json.loads(topics_json)
        for tag in tags:
            topic_counts[tag] = topic_counts.get(tag, 0) + 1
            topic_boards.setdefault(tag, set()).add(board_id)

    return sorted([
        {"name": t, "count": c, "board_count": len(topic_boards.get(t, set()))}
        for t, c in topic_counts.items()
    ], key=lambda x: -x["count"])


async def _get_national_stats() -> dict:
    """Aggregate stats for the national overview."""
    async with db.async_session() as session:
        total_boards = (await session.execute(
            select(func.count(Board.id))
        )).scalar()

        total_meetings = (await session.execute(
            select(func.count(Meeting.id))
        )).scalar()

        total_documents = (await session.execute(
            select(func.count(MeetingDocument.id))
        )).scalar()

        total_summaries = (await session.execute(
            select(func.count(Meeting.id)).where(Meeting.summary.isnot(None))
        )).scalar()

        boards_with_meetings = (await session.execute(
            select(func.count(distinct(Meeting.board_id)))
        )).scalar()

        states_covered = (await session.execute(
            select(func.count(distinct(Board.state)))
            .where(Board.id.in_(
                select(distinct(Meeting.board_id))
            ))
        )).scalar()

    # Count meetings that have at least one document file on disk
    async with db.async_session() as session:
        doc_rows = (await session.execute(
            select(MeetingDocument.meeting_id, Board.code, MeetingDocument.filename)
            .join(Meeting, MeetingDocument.meeting_id == Meeting.id)
            .join(Board, Meeting.board_id == Board.id)
        )).all()
    meetings_with_files = len({
        mid for mid, code, fn in doc_rows
        if (DOCUMENTS_DIR / code / fn).exists()
    })

    return {
        "total_boards": total_boards,
        "total_meetings": total_meetings,
        "total_documents": total_documents,
        "total_summaries": total_summaries,
        "boards_collected": boards_with_meetings,
        "states_covered": states_covered,
        "meetings_with_files": meetings_with_files,
    }


async def _get_state_coverage() -> dict[str, dict]:
    """Get meeting counts per state for the map."""
    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).order_by(Board.state, Board.code)
        )).scalars().all()

        counts = (await session.execute(
            select(Meeting.board_id, func.count(Meeting.id))
            .group_by(Meeting.board_id)
        )).all()

    meeting_counts = {board_id: count for board_id, count in counts}

    state_data: dict[str, dict] = {}
    for b in boards:
        if b.state not in state_data:
            state_data[b.state] = {
                "name": STATE_NAMES.get(b.state, b.state),
                "boards": [],
                "total_meetings": 0,
                "status": "pending",
            }
        mc = meeting_counts.get(b.id, 0)
        state_data[b.state]["boards"].append({
            "code": b.code,
            "name": b.name,
            "board_type": b.board_type,
            "meetings": mc,
        })
        state_data[b.state]["total_meetings"] += mc
        if mc > 0:
            state_data[b.state]["status"] = "collected"
        elif b.discovery_status == "found" and state_data[b.state]["status"] != "collected":
            state_data[b.state]["status"] = "discovered"

    return state_data


# ---------------------------------------------------------------------------
# Pages — National Overview
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def national_overview(request: Request):
    """Landing page — national intelligence overview."""
    stats = await _get_national_stats()
    topics = await _get_all_topics_with_counts()
    state_data = await _get_state_coverage()

    # Recent summaries (latest 8 meetings with summaries)
    async with db.async_session() as session:
        recent = (await session.execute(
            select(Meeting, Board)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.summary.isnot(None))
            .order_by(Meeting.meeting_date.desc())
            .limit(8)
        )).all()

    recent_summaries = [{
        "meeting": m,
        "board": b,
        "state_name": STATE_NAMES.get(b.state, b.state),
    } for m, b in recent]

    # State colors for map
    state_colors = {s: d["status"] for s, d in state_data.items()}

    return templates.TemplateResponse(request, "national.html", context={
        "stats": stats,
        "topics": topics,
        "state_data": state_data,
        "state_colors": state_colors,
        "recent_summaries": recent_summaries,
        "breadcrumbs": [],
    })


# ---------------------------------------------------------------------------
# Pages — Topic Drill-Down
# ---------------------------------------------------------------------------

@app.get("/topic/{slug}", response_class=HTMLResponse)
async def topic_view(request: Request, slug: str):
    """Topic drill-down — all boards/meetings with this topic."""
    display_name = slug.replace("-", " ").title()

    async with db.async_session() as session:
        meetings = (await session.execute(
            select(Meeting, Board)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.topics.isnot(None))
            .order_by(Meeting.meeting_date.desc())
        )).all()

    # Filter to meetings that have this topic
    filtered = []
    board_ids = set()
    state_set = set()
    for m, b in meetings:
        tags = m.topics if isinstance(m.topics, list) else json.loads(m.topics or "[]")
        if slug in tags:
            filtered.append({"meeting": m, "board": b, "state_name": STATE_NAMES.get(b.state, b.state)})
            board_ids.add(b.id)
            state_set.add(b.state)

    return templates.TemplateResponse(request, "topic.html", context={
        "topic_slug": slug,
        "topic_name": display_name,
        "meetings": filtered,
        "board_count": len(board_ids),
        "state_count": len(state_set),
        "meeting_count": len(filtered),
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
    })


# ---------------------------------------------------------------------------
# Pages — State Drill-Down
# ---------------------------------------------------------------------------

@app.get("/state/{abbr}", response_class=HTMLResponse)
async def state_view(request: Request, abbr: str):
    """State drill-down — all boards and meetings for a state."""
    abbr = abbr.upper()
    state_name = STATE_NAMES.get(abbr, abbr)

    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).where(Board.state == abbr).order_by(Board.code)
        )).scalars().all()

    if not boards:
        raise HTTPException(status_code=404, detail=f"No boards found for {abbr}")

    board_data = []
    for b in boards:
        async with db.async_session() as session:
            meeting_count = (await session.execute(
                select(func.count(Meeting.id)).where(Meeting.board_id == b.id)
            )).scalar()
            summary_count = (await session.execute(
                select(func.count(Meeting.id))
                .where(Meeting.board_id == b.id, Meeting.summary.isnot(None))
            )).scalar()
            doc_count = (await session.execute(
                select(func.count(MeetingDocument.id))
                .where(MeetingDocument.meeting_id.in_(
                    select(Meeting.id).where(Meeting.board_id == b.id)
                ))
            )).scalar()

            # Get topics for this board
            topic_meetings = (await session.execute(
                select(Meeting.topics)
                .where(Meeting.board_id == b.id, Meeting.topics.isnot(None))
            )).scalars().all()

            # Count meetings with actual files on disk
            doc_rows = (await session.execute(
                select(MeetingDocument.meeting_id, MeetingDocument.filename)
                .where(MeetingDocument.meeting_id.in_(
                    select(Meeting.id).where(Meeting.board_id == b.id)
                ))
            )).all()
        meetings_with_files = len({
            mid for mid, fn in doc_rows
            if (DOCUMENTS_DIR / b.code / fn).exists()
        })

        topics = set()
        for t in topic_meetings:
            tags = t if isinstance(t, list) else json.loads(t or "[]")
            topics.update(tags)

        board_data.append({
            "board": b,
            "meetings": meeting_count,
            "summaries": summary_count,
            "documents": doc_count,
            "meetings_with_files": meetings_with_files,
            "topics": sorted(topics),
        })

    return templates.TemplateResponse(request, "state.html", context={
        "state_abbr": abbr,
        "state_name": state_name,
        "board_data": board_data,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
    })


# ---------------------------------------------------------------------------
# Pages — Board Detail
# ---------------------------------------------------------------------------

@app.get("/board/{state}/{code}")
async def board_redirect(state: str, code: str):
    """Redirect old /board/{state}/{code} URLs to /board/{code}.

    Preserves fragment anchors (e.g. #2025-08-01) via client-side redirect.
    """
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url=f"/board/{code.upper()}", status_code=301)


@app.get("/board/{code}", response_class=HTMLResponse)
async def board_view(request: Request, code: str):
    """Board detail — full meeting timeline with summaries."""
    code = code.upper()

    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == code)
        )).scalar_one_or_none()

    if not board:
        raise HTTPException(status_code=404, detail=f"Board {code} not found")

    async with db.async_session() as session:
        meetings = (await session.execute(
            select(Meeting)
            .where(Meeting.board_id == board.id)
            .order_by(Meeting.meeting_date.desc())
        )).scalars().all()

        meeting_data = []
        for m in meetings:
            docs_all = (await session.execute(
                select(MeetingDocument)
                .where(MeetingDocument.meeting_id == m.id)
                .order_by(MeetingDocument.doc_type)
            )).scalars().all()
            # Only include documents whose files exist on disk
            docs = [d for d in docs_all if (DOCUMENTS_DIR / board.code / d.filename).exists()]
            meeting_data.append({"meeting": m, "documents": docs})

    # Topic breakdown
    topic_counts: dict[str, int] = {}
    for item in meeting_data:
        for tag in (item["meeting"].topics or []):
            topic_counts[tag] = topic_counts.get(tag, 0) + 1
    topics_sorted = sorted(topic_counts.items(), key=lambda x: -x[1])

    state_name = STATE_NAMES.get(board.state, board.state)

    return templates.TemplateResponse(request, "board.html", context={
        "board": board,
        "meeting_data": meeting_data,
        "topic_counts": topics_sorted,
        "state_name": state_name,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
            {"label": state_name, "url": f"/state/{board.state}"},
        ],
    })


# ---------------------------------------------------------------------------
# Pages — Meeting Detail
# ---------------------------------------------------------------------------

@app.get("/meeting/{meeting_id}", response_class=HTMLResponse)
async def meeting_view(request: Request, meeting_id: int):
    """Meeting detail — full summary, documents, exhibits."""
    async with db.async_session() as session:
        meeting = (await session.execute(
            select(Meeting).where(Meeting.id == meeting_id)
        )).scalar_one_or_none()

        if not meeting:
            raise HTTPException(status_code=404, detail="Meeting not found")

        board = (await session.execute(
            select(Board).where(Board.id == meeting.board_id)
        )).scalar_one_or_none()

        docs_all = (await session.execute(
            select(MeetingDocument)
            .where(MeetingDocument.meeting_id == meeting.id)
            .order_by(MeetingDocument.doc_type)
        )).scalars().all()

    # Only include documents whose files actually exist on disk
    docs = [d for d in docs_all if (DOCUMENTS_DIR / board.code / d.filename).exists()]

    # Check for exhibits
    exhibits = []
    exhibit_base = EXHIBITS_DIR / board.code
    if exhibit_base.exists():
        for exhibit_dir in sorted(exhibit_base.iterdir()):
            if not exhibit_dir.is_dir():
                continue
            pages = sorted(exhibit_dir.glob("page_*.png"))
            if pages:
                exhibits.append({
                    "name": exhibit_dir.name,
                    "page_count": len(pages),
                    "thumbnail": f"/exhibit/{board.code}/{exhibit_dir.name}/1",
                })

    state_name = STATE_NAMES.get(board.state, board.state)

    return templates.TemplateResponse(request, "meeting.html", context={
        "meeting": meeting,
        "board": board,
        "documents": docs,
        "exhibits": exhibits,
        "state_name": state_name,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
            {"label": state_name, "url": f"/state/{board.state}"},
            {"label": board.name, "url": f"/board/{board.code}"},
        ],
    })


# ---------------------------------------------------------------------------
# Pages — Exhibit Viewer
# ---------------------------------------------------------------------------

@app.get("/exhibit/{board_code}/{exhibit_name}", response_class=HTMLResponse)
async def exhibit_viewer(request: Request, board_code: str, exhibit_name: str):
    """Full exhibit page viewer with navigation."""
    board_code = board_code.upper()
    exhibit_dir = EXHIBITS_DIR / board_code / exhibit_name

    if not exhibit_dir.exists() or not exhibit_dir.is_dir():
        raise HTTPException(status_code=404, detail="Exhibit not found")

    pages = sorted(exhibit_dir.glob("page_*.png"))
    if not pages:
        raise HTTPException(status_code=404, detail="No pages in exhibit")

    # Get board info for breadcrumbs
    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == board_code)
        )).scalar_one_or_none()

    state_name = STATE_NAMES.get(board.state, board.state) if board else ""

    page_data = [{"num": i + 1, "url": f"/exhibit/{board_code}/{exhibit_name}/{i + 1}"} for i in range(len(pages))]

    breadcrumbs = [{"label": "National", "url": "/"}]
    if board:
        breadcrumbs.append({"label": state_name, "url": f"/state/{board.state}"})
        breadcrumbs.append({"label": board.name, "url": f"/board/{board_code}"})

    return templates.TemplateResponse(request, "exhibit.html", context={
        "board_code": board_code,
        "exhibit_name": exhibit_name,
        "pages": page_data,
        "total_pages": len(pages),
        "board": board,
        "state_name": state_name,
        "breadcrumbs": breadcrumbs,
    })


@app.get("/exhibit/{board_code}/{exhibit_name}/{page_num}")
async def serve_exhibit_page(board_code: str, exhibit_name: str, page_num: int):
    """Serve a single exhibit page image."""
    board_code = board_code.upper()
    img_path = EXHIBITS_DIR / board_code / exhibit_name / f"page_{page_num:03d}.png"

    if not img_path.exists():
        raise HTTPException(status_code=404, detail="Page not found")
    if not str(img_path.resolve()).startswith(str(EXHIBITS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")

    return FileResponse(str(img_path), media_type="image/png")


# ---------------------------------------------------------------------------
# Pages — National Landscape Report
# ---------------------------------------------------------------------------

@app.get("/report", response_class=HTMLResponse)
async def national_report(request: Request):
    """Serve the latest national landscape report as rendered HTML."""
    import markdown

    report_files = sorted(REPORTS_DIR.glob("*-board-landscape.md"), reverse=True)
    if not report_files:
        return HTMLResponse("<h1>No report available</h1><p>Run <code>python cli.py summarize --national</code> first.</p>")

    report_path = report_files[0]
    md_text = report_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    return templates.TemplateResponse(request, "report.html", context={
        "report_html": html_body,
        "report_date": report_path.stem[:10],
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
    })


# ---------------------------------------------------------------------------
# File Serving
# ---------------------------------------------------------------------------

@app.get("/screenshot/{path:path}")
async def serve_screenshot(path: str):
    file_path = SCREENSHOTS_DIR / path
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="Screenshot not found")
    if not str(file_path.resolve()).startswith(str(SCREENSHOTS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")
    return FileResponse(str(file_path), media_type="image/png")


@app.get("/document/{path:path}")
async def serve_document(path: str):
    file_path = DOCUMENTS_DIR / path
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="Document not found")
    if not str(file_path.resolve()).startswith(str(DOCUMENTS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")
    suffix = file_path.suffix.lower()
    media_types = {".pdf": "application/pdf", ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", ".html": "text/html", ".txt": "text/plain"}
    return FileResponse(str(file_path), media_type=media_types.get(suffix, "application/octet-stream"), filename=file_path.name)


# ---------------------------------------------------------------------------
# API — Trigger Collection
# ---------------------------------------------------------------------------

@app.post("/collect/{code}", response_class=HTMLResponse)
async def trigger_collect(request: Request, code: str):
    code = code.upper()
    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == code)
        )).scalar_one_or_none()

    if not board:
        raise HTTPException(status_code=404, detail=f"Board {code} not found")

    import asyncio
    from app.scraper.collector import collect_all

    async def _run():
        try:
            await collect_all(board_code=code)
        except Exception as e:
            print(f"Collection error for {code}: {e}")

    asyncio.create_task(_run())

    return HTMLResponse(
        content=f'''
        <div class="flex items-center gap-2 text-sm text-amber-600 bg-amber-50 border border-amber-200 rounded-lg px-3 py-2">
            <svg class="animate-spin h-4 w-4" viewBox="0 0 24 24" fill="none">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"/>
            </svg>
            Collection started for {code}. Refresh the page to see results.
        </div>
        ''',
        status_code=202,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def run_server(host: str = "0.0.0.0", port: int = 8099):
    import uvicorn
    uvicorn.run(app, host=host, port=port)
