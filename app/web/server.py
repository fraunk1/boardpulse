"""boardpulse web dashboard — FastAPI application."""
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, func

from app.models import Board, Meeting, MeetingDocument
from app.config import SCREENSHOTS_DIR, DOCUMENTS_DIR, REPORTS_DIR
import app.database as db

# Paths
WEB_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = WEB_DIR / "templates"
STATIC_DIR = WEB_DIR / "static"

# App
app = FastAPI(title="boardpulse", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.on_event("startup")
async def startup():
    """Initialize database on startup."""
    from app.database import init_db
    await init_db()


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the main dashboard page with the US map."""
    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).order_by(Board.state, Board.code)
        )).scalars().all()

    # Build a lookup: state_abbr -> list of board dicts (for multi-board states)
    state_boards: dict[str, list[dict]] = {}
    for b in boards:
        info = {
            "code": b.code,
            "name": b.name,
            "board_type": b.board_type,
            "discovery_status": b.discovery_status,
            "has_meetings": False,
        }
        state_boards.setdefault(b.state, []).append(info)

    # Check which boards have meetings
    async with db.async_session() as session:
        counts = (await session.execute(
            select(Meeting.board_id, func.count(Meeting.id))
            .group_by(Meeting.board_id)
        )).all()
    meeting_counts = {board_id: count for board_id, count in counts}

    for b in boards:
        for sb in state_boards.get(b.state, []):
            if sb["code"] == b.code and meeting_counts.get(b.id, 0) > 0:
                sb["has_meetings"] = True

    # Determine color for each state
    state_colors: dict[str, str] = {}
    for state_abbr, board_list in state_boards.items():
        if any(sb["has_meetings"] for sb in board_list):
            state_colors[state_abbr] = "collected"
        elif any(sb["discovery_status"] == "found" for sb in board_list):
            state_colors[state_abbr] = "discovered"
        else:
            state_colors[state_abbr] = "not_scraped"

    # Stats for the header
    total_boards = len(boards)
    collected_count = sum(1 for b in boards if meeting_counts.get(b.id, 0) > 0)
    discovered_count = sum(1 for b in boards if b.discovery_status == "found" and meeting_counts.get(b.id, 0) == 0)
    pending_count = total_boards - collected_count - discovered_count
    total_meetings = sum(meeting_counts.values()) if meeting_counts else 0

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "state_boards": state_boards,
        "state_colors": state_colors,
        "total_boards": total_boards,
        "collected_count": collected_count,
        "discovered_count": discovered_count,
        "pending_count": pending_count,
        "total_meetings": total_meetings,
    })


# ---------------------------------------------------------------------------
# HTMX Partials
# ---------------------------------------------------------------------------

@app.get("/board/{state}", response_class=HTMLResponse)
async def board_by_state(request: Request, state: str):
    """HTMX partial: board detail for a state (shows first board, or multi-board selector)."""
    state = state.upper()
    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).where(Board.state == state).order_by(Board.code)
        )).scalars().all()

    if not boards:
        raise HTTPException(status_code=404, detail=f"No boards found for state {state}")

    board = boards[0]
    return await _render_board_detail(request, board, boards)


@app.get("/board/{state}/{code}", response_class=HTMLResponse)
async def board_by_code(request: Request, state: str, code: str):
    """HTMX partial: specific board detail (for multi-board states)."""
    state = state.upper()
    code = code.upper()
    async with db.async_session() as session:
        board = (await session.execute(
            select(Board).where(Board.code == code)
        )).scalar_one_or_none()

        all_boards = (await session.execute(
            select(Board).where(Board.state == state).order_by(Board.code)
        )).scalars().all()

    if not board:
        raise HTTPException(status_code=404, detail=f"Board {code} not found")

    return await _render_board_detail(request, board, all_boards)


async def _render_board_detail(request: Request, board: Board, all_boards: list[Board]):
    """Render the board detail partial with meetings and documents."""
    async with db.async_session() as session:
        meetings = (await session.execute(
            select(Meeting)
            .where(Meeting.board_id == board.id)
            .order_by(Meeting.meeting_date.desc())
        )).scalars().all()

        meeting_data = []
        for m in meetings:
            docs = (await session.execute(
                select(MeetingDocument)
                .where(MeetingDocument.meeting_id == m.id)
                .order_by(MeetingDocument.doc_type)
            )).scalars().all()
            meeting_data.append({"meeting": m, "documents": docs})

    return templates.TemplateResponse("partials/board_detail.html", {
        "request": request,
        "board": board,
        "all_boards": all_boards,
        "meeting_data": meeting_data,
        "has_multiple_boards": len(all_boards) > 1,
    })


# ---------------------------------------------------------------------------
# File Serving
# ---------------------------------------------------------------------------

@app.get("/screenshot/{path:path}")
async def serve_screenshot(path: str):
    """Serve a screenshot image from the data/screenshots directory."""
    file_path = SCREENSHOTS_DIR / path
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="Screenshot not found")
    if not str(file_path.resolve()).startswith(str(SCREENSHOTS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")
    return FileResponse(str(file_path), media_type="image/png")


@app.get("/document/{path:path}")
async def serve_document(path: str):
    """Serve or download a document from the data/documents directory."""
    file_path = DOCUMENTS_DIR / path
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="Document not found")
    if not str(file_path.resolve()).startswith(str(DOCUMENTS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")
    suffix = file_path.suffix.lower()
    media_types = {".pdf": "application/pdf", ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", ".html": "text/html", ".txt": "text/plain"}
    media_type = media_types.get(suffix, "application/octet-stream")
    return FileResponse(str(file_path), media_type=media_type, filename=file_path.name)


# ---------------------------------------------------------------------------
# API — Trigger Collection
# ---------------------------------------------------------------------------

@app.post("/collect/{code}", response_class=HTMLResponse)
async def trigger_collect(request: Request, code: str):
    """Trigger async collection for a board. Returns an HTMX partial with status."""
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
    """Start the uvicorn server."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)
