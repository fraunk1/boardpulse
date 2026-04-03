"""boardpulse web dashboard — Palantir-style intelligence interface."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, func, distinct

from app.models import Board, Meeting, MeetingDocument, PipelineRun, PipelineEvent, DocumentPage, IntelligenceBrief, MeetingIntelligence
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

def _clean_summary_preview(summary: str | None, max_len: int = 180) -> str:
    """Strip YAML frontmatter, markdown headers, and metadata from summary preview."""
    if not summary:
        return ""
    import re
    text = summary
    # Strip YAML frontmatter
    text = re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, flags=re.DOTALL)
    # Strip markdown headers
    text = re.sub(r'^#+\s+.*$', '', text, flags=re.MULTILINE)
    # Strip bold field labels like **Period:** ...
    text = re.sub(r'\*\*[A-Za-z ]+:\*\*\s*[^\n]*', '', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Trim to length
    if len(text) > max_len:
        text = text[:max_len].rsplit(' ', 1)[0] + "..."
    return text


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


async def _get_trending_topics() -> list[dict]:
    """Compare topic frequency in last 3 months vs prior 3 months to find trends."""
    from datetime import date, timedelta

    now = date.today()
    recent_start = now - timedelta(days=90)
    prior_start = now - timedelta(days=180)

    async with db.async_session() as session:
        # Recent period meetings with topics
        recent_meetings = (await session.execute(
            select(Meeting.topics)
            .where(Meeting.topics.isnot(None))
            .where(Meeting.meeting_date >= recent_start)
        )).scalars().all()

        # Prior period meetings with topics
        prior_meetings = (await session.execute(
            select(Meeting.topics)
            .where(Meeting.topics.isnot(None))
            .where(Meeting.meeting_date >= prior_start)
            .where(Meeting.meeting_date < recent_start)
        )).scalars().all()

    def count_topics(meetings):
        counts = {}
        for topics_raw in meetings:
            tags = topics_raw if isinstance(topics_raw, list) else json.loads(topics_raw or "[]")
            for t in tags:
                counts[t] = counts.get(t, 0) + 1
        return counts

    recent_counts = count_topics(recent_meetings)
    prior_counts = count_topics(prior_meetings)

    trends = []
    all_topics = set(list(recent_counts.keys()) + list(prior_counts.keys()))
    for topic in all_topics:
        recent = recent_counts.get(topic, 0)
        prior = prior_counts.get(topic, 0)
        if prior > 0:
            change_pct = round(((recent - prior) / prior) * 100)
        elif recent > 0:
            change_pct = 100  # new topic
        else:
            change_pct = 0
        trends.append({
            "name": topic,
            "recent": recent,
            "prior": prior,
            "change_pct": change_pct,
            "direction": "up" if change_pct > 5 else ("down" if change_pct < -5 else "flat"),
        })

    # Sort by absolute change, biggest movers first
    trends.sort(key=lambda x: abs(x["change_pct"]), reverse=True)
    return trends[:8]


async def _get_topic_by_state_matrix() -> dict:
    """Build a topic × state matrix for cross-state comparison."""
    async with db.async_session() as session:
        rows = (await session.execute(
            select(Board.state, Meeting.topics)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.topics.isnot(None))
        )).all()

    # Count topic occurrences per state
    matrix: dict[str, dict[str, int]] = {}
    for state, topics_raw in rows:
        tags = topics_raw if isinstance(topics_raw, list) else json.loads(topics_raw or "[]")
        for t in tags:
            if t not in matrix:
                matrix[t] = {}
            matrix[t][state] = matrix[t].get(state, 0) + 1

    # Pick top 8 topics by total mentions
    topic_totals = {t: sum(states.values()) for t, states in matrix.items()}
    top_topics = sorted(topic_totals, key=topic_totals.get, reverse=True)[:8]

    # Get all states that have data
    all_states = sorted({s for states in matrix.values() for s in states})

    return {
        "topics": top_topics,
        "states": all_states,
        "matrix": {t: matrix[t] for t in top_topics},
        "totals": {t: topic_totals[t] for t in top_topics},
    }


async def _get_activity_by_month(months: int = 12) -> dict:
    """Get meeting counts grouped by month — total + per-topic breakdown.

    Returns {"months": ["2025-05", ...], "total": [n, ...],
             "series": [{"topic": "Discipline", "data": [n, ...]}, ...]}
    """
    from datetime import timedelta, date as _date
    import json as _json
    cutoff = _date.today().replace(day=1) - timedelta(days=months * 31)

    async with db.async_session() as session:
        # 1) Total meetings per month
        total_rows = (await session.execute(
            select(
                func.strftime('%Y-%m', Meeting.meeting_date).label('month'),
                func.count(Meeting.id).label('count')
            )
            .where(Meeting.meeting_date >= cutoff)
            .group_by(func.strftime('%Y-%m', Meeting.meeting_date))
            .order_by(func.strftime('%Y-%m', Meeting.meeting_date))
        )).all()

        month_labels = [r.month for r in total_rows]
        total_counts = [r.count for r in total_rows]

        # 2) Per-topic counts via json_each (SQLite)
        from sqlalchemy import text
        topic_rows = (await session.execute(text("""
            SELECT strftime('%Y-%m', m.meeting_date) AS month,
                   j.value AS topic,
                   COUNT(DISTINCT m.id) AS cnt
            FROM meetings m, json_each(m.topics) j
            WHERE m.topics IS NOT NULL
              AND m.meeting_date >= :cutoff
            GROUP BY month, topic
            ORDER BY month, topic
        """), {"cutoff": str(cutoff)})).all()

    # Pivot: pick top 6 topics by overall volume in the window
    from collections import defaultdict
    topic_totals = defaultdict(int)
    topic_month = defaultdict(lambda: defaultdict(int))
    for r in topic_rows:
        topic_totals[r.topic] += r.cnt
        topic_month[r.topic][r.month] = r.cnt

    top_topics = sorted(topic_totals, key=topic_totals.get, reverse=True)[:6]

    series = []
    for t in top_topics:
        series.append({
            "topic": t,
            "data": [topic_month[t].get(m, 0) for m in month_labels]
        })

    return {"months": month_labels, "total": total_counts, "series": series}


async def _get_recent_activity(limit: int = 12) -> list[dict]:
    """Get the most recent meetings with summaries — the activity feed."""
    async with db.async_session() as session:
        rows = (await session.execute(
            select(Meeting, Board)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.summary.isnot(None))
            .order_by(Meeting.meeting_date.desc())
            .limit(limit)
        )).all()

    return [{
        "meeting": m,
        "board": b,
        "state_name": STATE_NAMES.get(b.state, b.state),
        "summary_preview": _clean_summary_preview(m.summary),
    } for m, b in rows]


# ---------------------------------------------------------------------------
# API — AI Intelligence Brief
# ---------------------------------------------------------------------------

@app.post("/api/generate-brief")
async def generate_brief():
    """Return the latest stored intelligence brief, or a data-driven fallback."""
    from datetime import date, timedelta

    # First: check for a stored brief
    try:
        async with db.async_session() as session:
            latest = (await session.execute(
                select(IntelligenceBrief)
                .order_by(IntelligenceBrief.generated_at.desc())
                .limit(1)
            )).scalar_one_or_none()

        if latest:
            age_days = (datetime.now(timezone.utc) - latest.generated_at).days
            meta = f'<p class="mt-3 text-[10px] text-bp-mist italic">Generated {latest.generated_at.strftime("%b %d, %Y at %I:%M %p")} by {latest.generated_by} · {latest.meetings_analyzed} meetings across {latest.boards_covered} boards</p>'
            if age_days > 7:
                meta += '<p class="text-[10px] text-amber-500 mt-1">This brief is over a week old. Run the pipeline to generate a fresh one.</p>'
            return JSONResponse({"brief": latest.brief_html + meta})
    except Exception:
        pass  # Table may not exist yet

    # Fallback: data-driven summary from raw meeting data
    cutoff = date.today() - timedelta(days=90)
    async with db.async_session() as session:
        rows = (await session.execute(
            select(Meeting.topics, Board.code)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.summary.isnot(None), Meeting.meeting_date >= cutoff)
        )).all()

    if not rows:
        return JSONResponse({"brief": "<p>No meeting data available for the last 90 days. Run the pipeline to collect data.</p>"})

    from collections import Counter
    boards_seen = set(r[1] for r in rows)
    topics_all = []
    for topics, _ in rows:
        tags = topics if isinstance(topics, list) else json.loads(topics or "[]")
        topics_all.extend(tags)
    top_topics = Counter(topics_all).most_common(5)
    top_str = ", ".join(f"{t} ({c})" for t, c in top_topics)

    brief_html = f"""
    <p><strong>Last 90 days:</strong> {len(rows)} meetings with summaries across {len(boards_seen)} boards.
    Top topics: {top_str}.</p>
    <p class="mt-2">No AI-generated brief has been stored yet. When the pipeline runs,
    Claude will analyze meeting content and write a full intelligence brief that appears here.</p>
    <p class="mt-2 text-[10px] text-bp-mist italic">Briefs are generated during scheduled pipeline runs — not on-demand.</p>
    """
    return JSONResponse({"brief": brief_html})


# ---------------------------------------------------------------------------
# Pages — National Overview
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def national_overview(request: Request):
    """Landing page — national intelligence overview."""
    stats = await _get_national_stats()
    topics = await _get_all_topics_with_counts()
    state_data = await _get_state_coverage()
    trending = await _get_trending_topics()
    activity = await _get_recent_activity(limit=12)
    topic_matrix = await _get_topic_by_state_matrix()
    activity_by_month = await _get_activity_by_month(months=12)

    # State colors for map
    state_colors = {s: d["status"] for s, d in state_data.items()}

    return templates.TemplateResponse(request, "national.html", context={
        "stats": stats,
        "topics": topics,
        "state_data": state_data,
        "state_colors": state_colors,
        "recent_summaries": activity[:8],
        "trending": trending,
        "activity": activity,
        "topic_matrix": topic_matrix,
        "activity_by_month": activity_by_month,
        "breadcrumbs": [],
    })


# ---------------------------------------------------------------------------
# Pages — Topic Drill-Down
# ---------------------------------------------------------------------------

@app.get("/topic/{slug}", response_class=HTMLResponse)
async def topic_redirect(slug: str):
    """Redirect old /topic/{slug} URLs to unified search."""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url=f"/search?topic={slug}", status_code=301)


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

    # Get page counts for PDF documents (for page-image rendering)
    doc_pages = []
    for d in docs:
        file_path = DOCUMENTS_DIR / board.code / d.filename
        page_count = 0
        if file_path.suffix.lower() == ".pdf":
            try:
                import fitz
                pdf = fitz.open(str(file_path))
                page_count = len(pdf)
                pdf.close()
            except Exception:
                pass
        doc_pages.append({
            "doc": d,
            "page_count": page_count,
            "is_pdf": file_path.suffix.lower() == ".pdf",
        })

    state_name = STATE_NAMES.get(board.state, board.state)

    return templates.TemplateResponse(request, "meeting.html", context={
        "meeting": meeting,
        "board": board,
        "doc_pages": doc_pages,
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
    """Serve the latest national landscape report with deep-linked citations.

    Citation links are rewritten from /board/{state}/{code}#{date}
    to /meeting/{id}#page-{best_page} so clicking a citation jumps
    directly to the evidence page in the document viewer.
    """
    import markdown
    import re as _re
    import fitz

    report_files = sorted(REPORTS_DIR.glob("*-board-landscape.md"), reverse=True)
    if not report_files:
        return HTMLResponse("<h1>No report available</h1><p>Run <code>python cli.py summarize --national</code> first.</p>")

    report_path = report_files[0]
    md_text = report_path.read_text(encoding="utf-8")

    # Build citation index: map (board_code, date) → (meeting_id, best_page)
    citation_index = {}
    async with db.async_session() as session:
        all_meetings = (await session.execute(
            select(Meeting, Board)
            .join(Board, Meeting.board_id == Board.id)
        )).all()
        for m, b in all_meetings:
            citation_index[(b.code, m.meeting_date.isoformat())] = m.id

    # Rewrite citation links in markdown before rendering
    # Pattern: [text](/board/{state}/{code}#{date})
    def _rewrite_citation(match):
        link_text = match.group(1)
        state = match.group(2)
        code = match.group(3)
        date_str = match.group(4)

        meeting_id = citation_index.get((code, date_str))
        if meeting_id:
            # Find best page for the claim text (context before the link)
            best_page = 1
            doc_path = DOCUMENTS_DIR / code
            if doc_path.exists():
                # Get the claim text from preceding context
                start = max(0, match.start() - 300)
                claim_text = md_text[start:match.start()].strip()
                # Find the PDF for this date
                for pdf_file in doc_path.glob(f"{date_str}*.pdf"):
                    try:
                        doc = fitz.open(str(pdf_file))
                        # Simple best-page: find page with most matching words
                        words = [w for w in _re.sub(r'[^\w\s]', '', claim_text).split() if len(w) >= 5][:8]
                        skip = {'board', 'meeting', 'state', 'medical', 'discussed', 'which', 'their', 'about', 'would'}
                        words = [w for w in words if w.lower() not in skip]
                        best_score = 0
                        for idx in range(len(doc)):
                            page_text = doc[idx].get_text("text").lower()
                            score = sum(1 for w in words if w.lower() in page_text)
                            if score > best_score:
                                best_score = score
                                best_page = idx + 1
                        doc.close()
                        break  # use first matching PDF
                    except Exception:
                        pass

            return f"[{link_text}](/meeting/{meeting_id}#page-{best_page})"
        return match.group(0)  # leave unchanged if no match

    md_text = _re.sub(
        r'\[([^\]]+)\]\(/board/(\w{2})/(\w+_\w+)#(\d{4}-\d{2}-\d{2})\)',
        _rewrite_citation,
        md_text,
    )

    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    return templates.TemplateResponse(request, "report.html", context={
        "report_html": html_body,
        "report_date": report_path.stem[:10],
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
    })


# ---------------------------------------------------------------------------
# Pages — Pipeline Runs
# ---------------------------------------------------------------------------

@app.get("/pipeline/", response_class=HTMLResponse)
async def pipeline_list(request: Request):
    """Pipeline runs list — history of all pipeline executions."""
    async with db.async_session() as session:
        runs = (await session.execute(
            select(PipelineRun).order_by(PipelineRun.started_at.desc()).limit(50)
        )).scalars().all()

    for run in runs:
        if run.started_at and run.completed_at:
            delta = run.completed_at - run.started_at
            minutes = int(delta.total_seconds() // 60)
            seconds = int(delta.total_seconds() % 60)
            run.duration = f"{minutes}m {seconds}s" if minutes else f"{seconds}s"
        else:
            run.duration = None

    return templates.TemplateResponse(request, "pipeline_list.html", context={
        "runs": runs,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
        "page_title": "Pipeline",
    })


@app.get("/pipeline/{run_id}", response_class=HTMLResponse)
async def pipeline_detail(request: Request, run_id: int):
    """Pipeline run detail — stats, digest, event timeline."""
    import markdown as md_lib

    async with db.async_session() as session:
        run = await session.get(PipelineRun, run_id)
        if not run:
            raise HTTPException(status_code=404, detail="Pipeline run not found")

        events = (await session.execute(
            select(PipelineEvent)
            .where(PipelineEvent.run_id == run_id)
            .order_by(PipelineEvent.timestamp)
        )).scalars().all()

    duration = None
    if run.started_at and run.completed_at:
        delta = run.completed_at - run.started_at
        minutes = int(delta.total_seconds() // 60)
        seconds = int(delta.total_seconds() % 60)
        duration = f"{minutes}m {seconds}s" if minutes else f"{seconds}s"

    digest_html = None
    if run.digest_path:
        digest_file = Path(run.digest_path)
        if not digest_file.is_absolute():
            from app.config import PROJECT_ROOT
            digest_file = PROJECT_ROOT / digest_file
        if digest_file.exists():
            digest_md = digest_file.read_text(encoding="utf-8")
            digest_html = md_lib.markdown(digest_md, extensions=["tables", "fenced_code"])

    stages = {}
    for e in events:
        stages.setdefault(e.stage, []).append(e)

    return templates.TemplateResponse(request, "pipeline_detail.html", context={
        "run": run,
        "events": events,
        "stages": stages,
        "duration": duration,
        "digest_html": digest_html,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
            {"label": "Pipeline", "url": "/pipeline/"},
        ],
        "page_title": f"Run #{run_id}",
    })


# ---------------------------------------------------------------------------
# API — Trigger Pipeline Run
# ---------------------------------------------------------------------------

@app.post("/pipeline/start", response_class=HTMLResponse)
async def trigger_pipeline(request: Request):
    """Start a pipeline run in the background (Stages 1-3: collect, extract, delta)."""
    import asyncio
    from app.pipeline.runner import PipelineRunner

    async def _run_pipeline():
        runner = PipelineRunner(trigger="dashboard")
        try:
            run_id = await runner.start()
            await runner.run_collection()
            await runner.run_extraction()
            delta = await runner.compute_and_write_context()

            total_new = sum(d["new_meetings"] for d in delta.values())
            total_docs = sum(d["new_documents"] for d in delta.values())

            async with db.async_session() as session:
                run = await session.get(PipelineRun, run_id)
                run.boards_collected = len(delta)
                run.new_meetings_found = total_new
                run.new_documents_found = total_docs
                await session.commit()

            if not delta:
                await runner.finalize()

        except Exception as e:
            await runner.mark_failed(str(e))

    asyncio.create_task(_run_pipeline())

    return HTMLResponse(
        content='''
        <div class="flex items-center gap-2 text-sm text-bp-teal bg-blue-50 border border-blue-200 rounded-lg px-3 py-2">
            <svg class="animate-spin h-4 w-4" viewBox="0 0 24 24" fill="none">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"/>
            </svg>
            Pipeline run started. Refresh the page to track progress.
        </div>
        ''',
        status_code=202,
    )


# ---------------------------------------------------------------------------
# Pages — Page Viewer
# ---------------------------------------------------------------------------

@app.get("/page/{page_id}", response_class=HTMLResponse)
async def page_viewer(request: Request, page_id: int):
    """Dedicated page viewer with context bar and filmstrip navigation."""
    async with db.async_session() as session:
        page = await session.get(DocumentPage, page_id)
        if not page:
            raise HTTPException(status_code=404, detail="Page not found")

        doc = await session.get(MeetingDocument, page.document_id)
        meeting = await session.get(Meeting, doc.meeting_id)
        board = await session.get(Board, meeting.board_id)

        all_pages = (await session.execute(
            select(DocumentPage)
            .where(DocumentPage.document_id == doc.id)
            .order_by(DocumentPage.page_number)
        )).scalars().all()

    total_pages = len(all_pages)
    state_name = STATE_NAMES.get(board.state, board.state)

    current_idx = next(i for i, p in enumerate(all_pages) if p.id == page_id)
    prev_page = all_pages[current_idx - 1] if current_idx > 0 else None
    next_page = all_pages[current_idx + 1] if current_idx < total_pages - 1 else None

    return templates.TemplateResponse(request, "page_viewer.html", context={
        "page": page,
        "doc": doc,
        "meeting": meeting,
        "board": board,
        "all_pages": all_pages,
        "total_pages": total_pages,
        "prev_page": prev_page,
        "next_page": next_page,
        "state_name": state_name,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
            {"label": state_name, "url": f"/state/{board.state}"},
            {"label": board.name, "url": f"/board/{board.code}"},
            {"label": meeting.title or meeting.meeting_date.isoformat(), "url": f"/meeting/{meeting.id}"},
        ],
        "page_title": f"Page {page.page_number}",
    })


@app.get("/page-image/{page_id}")
async def serve_page_image(page_id: int):
    """Serve a pre-rendered full-res page image."""
    async with db.async_session() as session:
        page = await session.get(DocumentPage, page_id)
        if not page:
            raise HTTPException(status_code=404, detail="Page not found")

    img_path = Path(page.image_path)
    if not img_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(str(img_path), media_type="image/png",
                        headers={"Cache-Control": "public, max-age=86400"})


@app.get("/page-thumb/{page_id}")
async def serve_page_thumb(page_id: int):
    """Serve a pre-rendered page thumbnail."""
    async with db.async_session() as session:
        page = await session.get(DocumentPage, page_id)
        if not page:
            raise HTTPException(status_code=404, detail="Page not found")

    thumb_path = Path(page.thumb_path)
    if not thumb_path.exists():
        raise HTTPException(status_code=404, detail="Thumbnail not found")

    return FileResponse(str(thumb_path), media_type="image/png",
                        headers={"Cache-Control": "public, max-age=86400"})


# ---------------------------------------------------------------------------
# Pages — Unified Search
# ---------------------------------------------------------------------------

@app.get("/search", response_class=HTMLResponse)
async def search_page(
    request: Request,
    q: str = "",
    state: str = "",
    period: str = "12m",
    doc_type: str = "",
):
    """Unified search — topics, free text, filters."""
    from datetime import timedelta, date as date_type
    from app.pipeline.fts import search_summaries
    from app.pipeline.context import TOPIC_TAXONOMY

    # Parse topic params (can appear multiple times in URL)
    topic = request.query_params.getlist("topic") if hasattr(request.query_params, 'getlist') else []
    if not topic:
        # Try single value
        single = request.query_params.get("topic", "")
        if single:
            topic = [single]

    # Period filter
    period_days = {"3m": 90, "6m": 180, "12m": 365, "all": 99999}
    cutoff_days = period_days.get(period, 365)
    cutoff_date = date_type.today() - timedelta(days=cutoff_days) if cutoff_days < 99999 else date_type(2000, 1, 1)

    async with db.async_session() as session:
        # Base query: pages joined through to boards
        query = (
            select(DocumentPage, MeetingDocument, Meeting, Board)
            .join(MeetingDocument, DocumentPage.document_id == MeetingDocument.id)
            .join(Meeting, MeetingDocument.meeting_id == Meeting.id)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.meeting_date >= cutoff_date)
        )

        # Topic filter
        if topic:
            from sqlalchemy import or_
            conditions = [DocumentPage.topics.like(f'%"{t}"%') for t in topic]
            query = query.where(or_(*conditions))
        else:
            query = query.where(DocumentPage.topics.isnot(None))

        # State filter
        if state:
            query = query.where(Board.state == state.upper())

        # Doc type filter
        if doc_type:
            query = query.where(MeetingDocument.doc_type == doc_type)

        query = query.order_by(Meeting.meeting_date.desc(), DocumentPage.page_number)
        rows = (await session.execute(query)).all()

    # FTS search (if free text query)
    fts_meeting_ids = None
    fts_snippets = {}
    if q:
        fts_results = await search_summaries(q)
        fts_meeting_ids = {r["meeting_id"] for r in fts_results}
        fts_snippets = {r["meeting_id"]: r["snippet"] for r in fts_results}
        if fts_meeting_ids:
            rows = [r for r in rows if r[2].id in fts_meeting_ids]
        else:
            rows = []

    # Group by meeting for hybrid view
    meetings_grouped: dict[int, dict] = {}
    for page, doc, meeting, board in rows:
        mid = meeting.id
        if mid not in meetings_grouped:
            meetings_grouped[mid] = {
                "meeting": meeting,
                "board": board,
                "doc": doc,
                "state_name": STATE_NAMES.get(board.state, board.state),
                "pages": [],
                "snippet": fts_snippets.get(mid, ""),
            }
        meetings_grouped[mid]["pages"].append(page)

    results = list(meetings_grouped.values())
    total_pages = sum(len(r["pages"]) for r in results)

    # Get all states for filter dropdown
    async with db.async_session() as session:
        states = (await session.execute(
            select(distinct(Board.state)).order_by(Board.state)
        )).scalars().all()

    is_htmx = request.headers.get("HX-Request") == "true"
    template = "partials/search_results.html" if is_htmx else "search.html"

    return templates.TemplateResponse(request, template, context={
        "q": q,
        "active_topics": topic,
        "all_topics": TOPIC_TAXONOMY,
        "state_filter": state,
        "period": period,
        "doc_type": doc_type,
        "results": results,
        "total_pages": total_pages,
        "total_meetings": len(results),
        "states": states,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
        "page_title": "Search",
    })


# ---------------------------------------------------------------------------
# File Serving
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# On-Demand PDF Page Renderer
# ---------------------------------------------------------------------------

@app.get("/document-page/{board_code}/{filename}/{page_num}")
async def render_document_page(board_code: str, filename: str, page_num: int):
    """Render a single PDF page as a PNG image on demand."""
    import fitz
    from fastapi.responses import Response

    file_path = DOCUMENTS_DIR / board_code / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Document not found")
    if not str(file_path.resolve()).startswith(str(DOCUMENTS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")
    if file_path.suffix.lower() != ".pdf":
        raise HTTPException(status_code=400, detail="Not a PDF")

    try:
        doc = fitz.open(str(file_path))
        if page_num < 1 or page_num > len(doc):
            doc.close()
            raise HTTPException(status_code=404, detail="Page not found")
        page = doc[page_num - 1]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")
        doc.close()
        return Response(content=img_bytes, media_type="image/png",
                        headers={"Cache-Control": "public, max-age=86400"})
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


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
    """Serve a document file. PDFs render inline (no download prompt)."""
    file_path = DOCUMENTS_DIR / path
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="Document not found")
    if not str(file_path.resolve()).startswith(str(DOCUMENTS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")
    suffix = file_path.suffix.lower()
    media_types = {".pdf": "application/pdf", ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", ".html": "text/html", ".txt": "text/plain"}
    media_type = media_types.get(suffix, "application/octet-stream")
    # PDFs and HTML serve inline (viewable in browser). Others prompt download.
    if suffix in (".pdf", ".html", ".htm", ".txt"):
        return FileResponse(str(file_path), media_type=media_type)
    else:
        return FileResponse(str(file_path), media_type=media_type, filename=file_path.name)


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
