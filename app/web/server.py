"""boardpulse web dashboard — Palantir-style intelligence interface."""
import json
import os
import re
import time
from datetime import date, datetime, timezone
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, func, distinct, text
from sqlalchemy.orm import selectinload

from app.models import Board, Meeting, MeetingDocument, WatchlistTerm
from app.config import SCREENSHOTS_DIR, DOCUMENTS_DIR, REPORTS_DIR, EXHIBITS_DIR, DATA_DIR, PROJECT_ROOT, LOGS_DIR
import app.database as db
import app.stats as stats
import app.web.trends as trends

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
    # Seed the four default watch terms on first run (no-op if any exist).
    try:
        await trends.seed_watchlist_if_empty()
    except Exception as exc:  # never block startup on the watchlist
        print(f"Watchlist seed skipped: {exc}")


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


_NATIONAL_STATS_CACHE: dict = {"value": None, "computed_at": 0.0}
_NATIONAL_STATS_TTL_SECONDS = 600


async def _get_national_stats() -> dict:
    """Aggregate stats for the national overview.

    ``meetings_with_files`` stats ~1,400 files on disk, so the result is
    cached in-process for 10 minutes to keep the homepage fast.
    """
    now = time.time()
    if (_NATIONAL_STATS_CACHE["value"] is not None
            and now - _NATIONAL_STATS_CACHE["computed_at"] < _NATIONAL_STATS_TTL_SECONDS):
        return _NATIONAL_STATS_CACHE["value"]

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

    stats = {
        "total_boards": total_boards,
        "total_meetings": total_meetings,
        "total_documents": total_documents,
        "total_summaries": total_summaries,
        "boards_collected": boards_with_meetings,
        "states_covered": states_covered,
        "meetings_with_files": meetings_with_files,
    }
    _NATIONAL_STATS_CACHE["value"] = stats
    _NATIONAL_STATS_CACHE["computed_at"] = now
    return stats


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
        elif (b.discovery_status in ("found", "manual")
              and state_data[b.state]["status"] != "collected"):
            state_data[b.state]["status"] = "discovered"
        elif (b.discovery_status in ("none_published", "blocked")
              and state_data[b.state]["status"] == "pending"):
            # Verified: the board publishes no minutes online (or the site
            # hard-blocks collection) — accounted for, distinct from pending.
            state_data[b.state]["status"] = "no_minutes"

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

    # Recent summaries (latest 8 meetings with summaries, most recently
    # scraped first — excludes future-dated scheduled meetings so they
    # don't crowd out real intelligence at the top of the feed)
    async with db.async_session() as session:
        recent = (await session.execute(
            select(Meeting, Board)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.summary.isnot(None))
            .where(Meeting.meeting_date <= date.today())
            .order_by(Meeting.scraped_at.desc())
            .limit(8)
        )).all()

    recent_summaries = [{
        "meeting": m,
        "board": b,
        "state_name": STATE_NAMES.get(b.state, b.state),
    } for m, b in recent]

    # State colors for map
    state_colors = {s: d["status"] for s, d in state_data.items()}

    # Watchlist (with new-hit counts) + emerging-issues feed. Both are
    # resilient: watchlist counts fall back to 0 on FTS edge cases, the
    # emerging feed is empty-guarded until fact extraction runs.
    watchlist = await trends.watchlist_with_counts(_sanitize_fts_query)
    emerging = await trends.emerging_national(limit=6)

    return templates.TemplateResponse(request, "national.html", context={
        "stats": stats,
        "topics": topics,
        "state_data": state_data,
        "state_colors": state_colors,
        "recent_summaries": recent_summaries,
        "watchlist": watchlist,
        "emerging": emerging,
        "breadcrumbs": [],
    })


# ---------------------------------------------------------------------------
# Pages — Trends Dashboard
# ---------------------------------------------------------------------------

@app.get("/trends", response_class=HTMLResponse)
async def trends_view(request: Request):
    """Trends dashboard — topics over time (live), plus rulemaking,
    legislation, and discipline (fact-backed, empty-guarded until extraction
    runs)."""
    gaining = await trends.gaining_traction(limit=6)
    tot = await trends.topics_over_time(top_n=6)
    rulemaking = await trends.rulemaking_pipeline()
    legislation = await trends.legislation_table()
    discipline = await trends.discipline_trends()

    return templates.TemplateResponse(request, "trends.html", context={
        "gaining": gaining,
        "topics_over_time": tot,
        "rulemaking": rulemaking,
        "legislation": legislation,
        "discipline": discipline,
        "current_quarter": trends.current_quarter_label(),
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
        "page_title": "Trends",
    })


# ---------------------------------------------------------------------------
# Watchlist — HTMX add / mark-seen / delete, all re-render the card partial
# ---------------------------------------------------------------------------

async def _render_watchlist_card(request: Request) -> HTMLResponse:
    """Render just the watchlist card partial (for HTMX swaps)."""
    watchlist = await trends.watchlist_with_counts(_sanitize_fts_query)
    return templates.TemplateResponse(
        request, "partials/watchlist_card.html", context={"watchlist": watchlist})


def _parse_urlencoded_form(body: bytes) -> dict[str, str]:
    """Parse an application/x-www-form-urlencoded body without needing
    python-multipart (which isn't installed). HTMX posts this content type by
    default, so this covers the watchlist add form. Last value wins per key.
    """
    from urllib.parse import parse_qsl
    return dict(parse_qsl(body.decode("utf-8", errors="replace"),
                          keep_blank_values=True))


@app.post("/watchlist", response_class=HTMLResponse)
async def watchlist_add(request: Request):
    """Add a watch term. Label = the term, title-cased. Idempotent on term.

    Reads the term from the urlencoded HTMX form body directly (Starlette's
    request.form() would require python-multipart, which isn't a dependency
    here).
    """
    form = _parse_urlencoded_form(await request.body())
    term = (form.get("term") or "").strip()
    if term:
        label = term if term.isupper() else term.title()
        async with db.async_session() as session:
            existing = (await session.execute(
                select(WatchlistTerm).where(WatchlistTerm.term == term)
            )).scalar_one_or_none()
            if existing is None:
                session.add(WatchlistTerm(term=term, label=label))
                await session.commit()
    return await _render_watchlist_card(request)


@app.post("/watchlist/{term_id}/delete", response_class=HTMLResponse)
async def watchlist_delete(request: Request, term_id: int):
    """Remove a watch term."""
    async with db.async_session() as session:
        term = (await session.execute(
            select(WatchlistTerm).where(WatchlistTerm.id == term_id)
        )).scalar_one_or_none()
        if term is not None:
            await session.delete(term)
            await session.commit()
    return await _render_watchlist_card(request)


@app.post("/watchlist/{term_id}/seen", response_class=HTMLResponse)
async def watchlist_seen(request: Request, term_id: int):
    """Mark a watch term seen — sets acknowledged_at=now so its new-hit count
    resets to zero until fresh documents arrive."""
    async with db.async_session() as session:
        term = (await session.execute(
            select(WatchlistTerm).where(WatchlistTerm.id == term_id)
        )).scalar_one_or_none()
        if term is not None:
            term.acknowledged_at = datetime.now(timezone.utc)
            await session.commit()
    return await _render_watchlist_card(request)


# ---------------------------------------------------------------------------
# Pages — Topic Drill-Down
# ---------------------------------------------------------------------------

@app.get("/topic/{slug}", response_class=HTMLResponse)
async def topic_view(request: Request, slug: str):
    """Topic drill-down — all boards/meetings with this topic."""
    display_name = slug.replace("-", " ").title()

    # SQL-side topic filter via SQLite's json_each table-valued function,
    # instead of loading every meeting and filtering in Python.
    async with db.async_session() as session:
        meetings = (await session.execute(
            select(Meeting, Board)
            .join(Board, Meeting.board_id == Board.id)
            .options(selectinload(Meeting.board))
            .where(Meeting.topics.isnot(None))
            .where(text(
                "EXISTS (SELECT 1 FROM json_each(meetings.topics) "
                "WHERE json_each.value = :slug)"
            )).params(slug=slug)
            .order_by(Meeting.meeting_date.desc())
        )).all()

    filtered = []
    board_ids = set()
    state_set = set()
    for m, b in meetings:
        filtered.append({"meeting": m, "board": b, "state_name": STATE_NAMES.get(b.state, b.state)})
        board_ids.add(b.id)
        state_set.add(b.state)

    # Quarterly chart data: meetings mentioning + boards discussing this topic.
    topic_quarterly = await trends.topic_quarterly(slug)

    return templates.TemplateResponse(request, "topic.html", context={
        "topic_slug": slug,
        "topic_name": display_name,
        "meetings": filtered,
        "board_count": len(board_ids),
        "state_count": len(state_set),
        "meeting_count": len(filtered),
        "topic_quarterly": topic_quarterly,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
    })


# ---------------------------------------------------------------------------
# Pages — State Drill-Down
# ---------------------------------------------------------------------------

@app.get("/state/{abbr}", response_class=HTMLResponse)
async def state_view(request: Request, abbr: str):
    """State drill-down — all boards and meetings for a state.

    Runs a constant number of queries regardless of how many boards the
    state has (previously ran 5+ queries per board in a Python loop).
    """
    abbr = abbr.upper()
    state_name = STATE_NAMES.get(abbr, abbr)

    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).where(Board.state == abbr).order_by(Board.code)
        )).scalars().all()

        if not boards:
            raise HTTPException(status_code=404, detail=f"No boards found for {abbr}")

        board_ids = [b.id for b in boards]

        # One GROUP BY query: meeting count + summary count per board.
        meeting_stats = (await session.execute(
            select(
                Meeting.board_id,
                func.count(Meeting.id),
                func.sum(func.iif(Meeting.summary.isnot(None), 1, 0)),
            )
            .where(Meeting.board_id.in_(board_ids))
            .group_by(Meeting.board_id)
        )).all()
        meeting_stats_by_board = {
            board_id: (count, summary_count or 0)
            for board_id, count, summary_count in meeting_stats
        }

        # One GROUP BY query: document count per board (joined through meetings).
        doc_counts = (await session.execute(
            select(Meeting.board_id, func.count(MeetingDocument.id))
            .join(MeetingDocument, MeetingDocument.meeting_id == Meeting.id)
            .where(Meeting.board_id.in_(board_ids))
            .group_by(Meeting.board_id)
        )).all()
        doc_count_by_board = {board_id: count for board_id, count in doc_counts}

        # One query: (board_id, topics) rows for topic aggregation in Python.
        topic_rows = (await session.execute(
            select(Meeting.board_id, Meeting.topics)
            .where(Meeting.board_id.in_(board_ids), Meeting.topics.isnot(None))
        )).all()

        # One query: (board_id, code, filename) doc rows for the on-disk
        # existence check, so that loop doesn't hit the DB per row.
        doc_rows = (await session.execute(
            select(Meeting.board_id, Board.code, MeetingDocument.filename, MeetingDocument.meeting_id)
            .join(MeetingDocument, MeetingDocument.meeting_id == Meeting.id)
            .join(Board, Meeting.board_id == Board.id)
            .where(Meeting.board_id.in_(board_ids))
        )).all()

    topics_by_board: dict[int, set] = {}
    for board_id, topics_json in topic_rows:
        tags = topics_json if isinstance(topics_json, list) else json.loads(topics_json or "[]")
        topics_by_board.setdefault(board_id, set()).update(tags)

    meetings_with_files_by_board: dict[int, set] = {}
    for board_id, code, filename, meeting_id in doc_rows:
        if (DOCUMENTS_DIR / code / filename).exists():
            meetings_with_files_by_board.setdefault(board_id, set()).add(meeting_id)

    board_data = []
    for b in boards:
        meeting_count, summary_count = meeting_stats_by_board.get(b.id, (0, 0))
        board_data.append({
            "board": b,
            "meetings": meeting_count,
            "summaries": summary_count,
            "documents": doc_count_by_board.get(b.id, 0),
            "meetings_with_files": len(meetings_with_files_by_board.get(b.id, set())),
            "topics": sorted(topics_by_board.get(b.id, set())),
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
# Pages — Full-Text Search
# ---------------------------------------------------------------------------

_SEARCH_PAGE_SIZE = 25


def _sanitize_fts_query(q: str) -> str:
    """Turn free-typed user input into a safe FTS5 MATCH expression.

    Splits on whitespace and wraps each token in double quotes, joined by
    spaces. Quoting each token neutralizes FTS5 operators (AND/OR/NOT/NEAR,
    column filters, prefix `*`) and unbalanced quotes — every token becomes
    a literal phrase match, so the query can't raise a syntax error.
    """
    tokens = q.split()
    if not tokens:
        return ""
    escaped = [tok.replace('"', '""') for tok in tokens]
    return " ".join(f'"{tok}"' for tok in escaped)


@app.get("/search", response_class=HTMLResponse)
async def search_view(request: Request, q: str = "", page: int = 1):
    """Full-text search across meeting document text (SQLite FTS5)."""
    q = (q or "").strip()
    page = max(1, page)
    results: list[dict] = []
    has_next = False
    error = False

    if q:
        fts_query = _sanitize_fts_query(q)
        offset = (page - 1) * _SEARCH_PAGE_SIZE
        try:
            async with db.async_session() as session:
                rows = (await session.execute(text(
                    """
                    SELECT
                        d.id AS doc_id,
                        d.doc_type,
                        m.id AS meeting_id,
                        m.meeting_date,
                        m.title,
                        b.code AS board_code,
                        b.state AS board_state,
                        snippet(doc_fts, 0, '<mark>', '</mark>', ' … ', 14) AS snippet
                    FROM doc_fts
                    JOIN meeting_documents d ON d.id = doc_fts.rowid
                    JOIN meetings m ON m.id = d.meeting_id
                    JOIN boards b ON b.id = m.board_id
                    WHERE doc_fts MATCH :query
                    ORDER BY bm25(doc_fts)
                    LIMIT :limit OFFSET :offset
                    """
                ), {"query": fts_query, "limit": _SEARCH_PAGE_SIZE + 1, "offset": offset})).all()
        except Exception:
            # Malformed/edge-case FTS5 query — never surface a 500, just show
            # a friendly empty state.
            rows = []
            error = True

        has_next = len(rows) > _SEARCH_PAGE_SIZE
        rows = rows[:_SEARCH_PAGE_SIZE]

        for r in rows:
            # Raw SQL via text() returns SQLite's stored TEXT for a Date
            # column, not a parsed date.fromisoformat() object — parse it
            # here so the template can call .strftime() like it does
            # everywhere else (ORM queries auto-convert; this one doesn't).
            meeting_date = r.meeting_date
            if isinstance(meeting_date, str):
                meeting_date = date.fromisoformat(meeting_date)
            results.append({
                "doc_id": r.doc_id,
                "doc_type": r.doc_type,
                "meeting_id": r.meeting_id,
                "meeting_date": meeting_date,
                "title": r.title,
                "board_code": r.board_code,
                "board_state": r.board_state,
                "state_name": STATE_NAMES.get(r.board_state, r.board_state),
                "snippet": r.snippet,
            })

    return templates.TemplateResponse(request, "search.html", context={
        "q": q,
        "page": page,
        "results": results,
        "result_count": len(results),
        "has_next": has_next,
        "has_prev": page > 1,
        "error": error,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
        "page_title": "Search",
    })


# ---------------------------------------------------------------------------
# Pages — Ops Status
# ---------------------------------------------------------------------------

def _latest_refresh_log() -> dict | None:
    """Return {path, mtime, diff_text} for the newest refresh-*.log, or None."""
    if not LOGS_DIR.exists():
        return None
    log_files = sorted(LOGS_DIR.glob("refresh-*.log"), reverse=True)
    if not log_files:
        return None
    log_path = log_files[0]
    try:
        text_content = log_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    marker = "REFRESH DIFF"
    idx = text_content.find(marker)
    diff_text = text_content[idx:] if idx != -1 else text_content

    return {
        "name": log_path.name,
        "mtime": datetime.fromtimestamp(log_path.stat().st_mtime),
        "diff_text": diff_text.strip(),
    }


def _load_coverage_ledger() -> dict:
    ledger_path = PROJECT_ROOT / "coverage_ledger.json"
    if not ledger_path.exists():
        return {}
    try:
        return json.loads(ledger_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


@app.get("/ops", response_class=HTMLResponse)
async def ops_view(request: Request):
    """Operational status page — refresh health, per-board coverage, failures."""
    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).order_by(Board.state, Board.code)
        )).scalars().all()

    per_board = await stats.per_board_counts()
    failures = await stats.extraction_failures()
    rollup = await stats.status_rollup()

    coverage_rows = []
    accounted = 0
    have_docs = 0
    for b in boards:
        counts = per_board.get(b.code, {"mtgs": 0, "docs": 0, "docs_text": 0})
        row_has_docs = counts["docs_text"] > 0
        if row_has_docs:
            have_docs += 1
        is_accounted = b.discovery_status in ("none_published", "blocked") or row_has_docs
        if is_accounted:
            accounted += 1
        coverage_rows.append({
            "board": b,
            "mtgs": counts["mtgs"],
            "docs": counts["docs"],
            "docs_text": counts["docs_text"],
            "discovery_status": b.discovery_status,
            "accounted": is_accounted,
        })

    total_boards = len(boards)

    return templates.TemplateResponse(request, "ops.html", context={
        "last_refresh": _latest_refresh_log(),
        "coverage_rows": coverage_rows,
        "total_boards": total_boards,
        "have_docs": have_docs,
        "accounted": accounted,
        "unaccounted": total_boards - accounted,
        "status_rollup": sorted(rollup.items()),
        "failures": failures,
        "failure_count": len(failures),
        "ledger": _load_coverage_ledger(),
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
        "page_title": "Ops",
    })


# ---------------------------------------------------------------------------
# Pages — Boards Directory
# ---------------------------------------------------------------------------

@app.get("/boards", response_class=HTMLResponse)
async def boards_directory(request: Request):
    """Flat directory of every board — one row per board, one aggregate query."""
    async with db.async_session() as session:
        rows = (await session.execute(
            select(
                Board,
                func.count(Meeting.id),
                func.max(Meeting.scraped_at),
            )
            .outerjoin(Meeting, Meeting.board_id == Board.id)
            .group_by(Board.id)
            .order_by(Board.state, Board.code)
        )).all()

    board_rows = []
    for board, meeting_count, last_meeting_scraped_at in rows:
        if meeting_count > 0:
            status = "collected"
        elif board.discovery_status in ("found", "manual"):
            status = "discovered"
        elif board.discovery_status == "none_published":
            status = "none_published"
        elif board.discovery_status == "blocked":
            status = "blocked"
        else:
            status = "pending"

        board_rows.append({
            "board": board,
            "meeting_count": meeting_count,
            "last_scraped_at": board.last_scraped_at or last_meeting_scraped_at,
            "status": status,
        })

    return templates.TemplateResponse(request, "boards.html", context={
        "board_rows": board_rows,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
        ],
        "page_title": "Boards",
    })


# ---------------------------------------------------------------------------
# Pages — Board Detail
# ---------------------------------------------------------------------------

# KEEP: live fallback for citation links in /report that the citation-rewriter couldn't resolve to a specific page.
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

    # What this board discussed — topic breakdown over the trailing 24 months
    # (replaces the meeting-count sparkline as the quick "focus" metric).
    topic_breakdown = await trends.board_topic_breakdown(board.id, months=24)

    return templates.TemplateResponse(request, "board.html", context={
        "board": board,
        "meeting_data": meeting_data,
        "topic_counts": topics_sorted,
        "state_name": state_name,
        "topic_breakdown": topic_breakdown,
        "breadcrumbs": [
            {"label": "National", "url": "/"},
            {"label": state_name, "url": f"/state/{board.state}"},
        ],
    })


# ---------------------------------------------------------------------------
# Pages — Meeting Detail
# ---------------------------------------------------------------------------

# Unbounded-but-safe cache of PDF page counts, keyed by (file_path, mtime).
# No TTL/eviction: the mtime in the key means a changed file just gets a
# new entry; stale entries for ~1,400 files cost negligible memory.
_PAGE_COUNT_CACHE: dict = {}


def _document_display_name(filename: str) -> str:
    """Turn a stored filename into a readable document title.

    Strips the `YYYY-MM-DD_` date prefix and extension, URL-decodes the
    escaped spaces/punctuation, and tidies whitespace — so a reader sees
    "Utilization of Medical Assistants" instead of
    "2025-03-07_Utilization%20of%20Medical%20Assistants.pdf".
    """
    from urllib.parse import unquote
    name = unquote(filename)
    name = re.sub(r"^\d{4}-\d{2}-\d{2}[_-]+", "", name)   # drop date prefix
    name = re.sub(r"\.(pdf|docx?|xlsx?|html?)$", "", name, flags=re.I)
    name = re.sub(r"[_]+", " ", name).strip()
    return name or filename


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

    # Get page counts for PDF documents (for page-image rendering). Cached
    # by (file_path, mtime) so ~1,400 files aren't re-opened with fitz on
    # every hit — a changed file gets a fresh cache entry since mtime is
    # part of the key, so no eviction/TTL is needed.
    doc_pages = []
    for d in docs:
        file_path = DOCUMENTS_DIR / board.code / d.filename
        page_count = 0
        if file_path.suffix.lower() == ".pdf":
            cache_key = (str(file_path), file_path.stat().st_mtime)
            if cache_key in _PAGE_COUNT_CACHE:
                page_count = _PAGE_COUNT_CACHE[cache_key]
            else:
                try:
                    import fitz
                    pdf = fitz.open(str(file_path))
                    page_count = pdf.page_count
                    pdf.close()
                except Exception:
                    pass
                _PAGE_COUNT_CACHE[cache_key] = page_count
        doc_pages.append({
            "doc": d,
            "page_count": page_count,
            "is_pdf": file_path.suffix.lower() == ".pdf",
            "display_name": _document_display_name(d.filename),
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

# Single-slot in-process cache for the rendered report: keyed on
# (report_path, report_mtime) so a re-run of `summarize --national` (which
# writes a new/changed file) invalidates it automatically. Intentionally
# NOT an LRU — only the latest report is ever kept.
_REPORT_CACHE: dict = {}


@app.get("/briefs", response_class=HTMLResponse)
async def briefs_latest(request: Request):
    from app.reports import brief as brief_mod
    return await _render_brief(request, brief_mod.latest_brief_ym())


@app.get("/briefs/{ym}", response_class=HTMLResponse)
async def briefs_month(request: Request, ym: str):
    return await _render_brief(request, ym)


@app.get("/briefs/{ym}/email", response_class=HTMLResponse)
async def briefs_email(ym: str):
    from app.reports import brief as brief_mod
    html_path = brief_mod.BRIEFS_DIR / f"{ym}.html"
    if not html_path.exists():
        raise HTTPException(status_code=404,
                            detail="Email version not generated for this brief")
    return HTMLResponse(html_path.read_text(encoding="utf-8"))


async def _render_brief(request: Request, ym):
    import re
    import markdown as _markdown
    from app.reports import brief as brief_mod
    all_briefs = sorted(
        (p.stem for p in brief_mod.BRIEFS_DIR.glob("*.md")
         if re.fullmatch(r"\d{4}-\d{2}", p.stem)), reverse=True)
    brief_html, has_html = None, False
    if ym:
        md_path = brief_mod.BRIEFS_DIR / f"{ym}.md"
        if md_path.exists():
            brief_html = _markdown.markdown(
                md_path.read_text(encoding="utf-8"), extensions=["tables"])
        has_html = (brief_mod.BRIEFS_DIR / f"{ym}.html").exists()
    return templates.TemplateResponse(request, "brief.html", {
        "brief_ym": ym, "brief_html": brief_html,
        "all_briefs": all_briefs, "has_html": has_html,
        "page_title": "Monthly Delta Brief",
    })


@app.get("/report", response_class=HTMLResponse)
async def national_report(request: Request):
    """Serve the latest national landscape report with deep-linked citations.

    Citation links are rewritten from /board/{state}/{code}#{date}
    to /meeting/{id}#page-{best_page} so clicking a citation jumps
    directly to the evidence page in the document viewer.

    The fitz-based "best page" citation scan is expensive, so the rendered
    HTML body is cached in-process keyed on (report_path, report_mtime).
    """
    report_files = sorted(REPORTS_DIR.glob("*-board-landscape.md"), reverse=True)
    if not report_files:
        return HTMLResponse("<h1>No report available</h1><p>Run <code>python cli.py summarize --national</code> first.</p>")

    report_path = report_files[0]
    report_mtime = report_path.stat().st_mtime
    cache_key = (str(report_path), report_mtime)

    cached = _REPORT_CACHE.get(cache_key)
    if cached is not None:
        html_body = cached["html_body"]
    else:
        import markdown
        import re as _re
        import fitz

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

        # Single-slot cache: clear before inserting the new (and only) entry.
        _REPORT_CACHE.clear()
        _REPORT_CACHE[cache_key] = {"html_body": html_body}

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

# ---------------------------------------------------------------------------
# On-Demand PDF Page Renderer
# ---------------------------------------------------------------------------

_PAGE_RENDER_DPI = 150
_PAGE_CACHE_DIR = DATA_DIR / "cache" / "pages"


@app.get("/document-page/{board_code}/{filename}/{page_num}")
async def render_document_page(board_code: str, filename: str, page_num: int):
    """Render a single PDF page as a PNG image on demand, with a disk cache.

    Cached PNGs live under DATA_DIR/cache/pages/{board_code}/{filename}/{page}-{dpi}.png.
    A cache hit is served directly when it's at least as new as the source
    PDF; otherwise the page is re-rendered with fitz and the cache is refreshed.
    """
    import fitz
    from fastapi.responses import Response

    file_path = DOCUMENTS_DIR / board_code / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Document not found")
    if not str(file_path.resolve()).startswith(str(DOCUMENTS_DIR.resolve())):
        raise HTTPException(status_code=403, detail="Access denied")
    if file_path.suffix.lower() != ".pdf":
        raise HTTPException(status_code=400, detail="Not a PDF")

    cache_path = _PAGE_CACHE_DIR / board_code / filename / f"{page_num}-{_PAGE_RENDER_DPI}.png"

    if cache_path.exists() and cache_path.stat().st_mtime >= file_path.stat().st_mtime:
        return FileResponse(str(cache_path), media_type="image/png",
                             headers={"Cache-Control": "public, max-age=86400"})

    try:
        doc = fitz.open(str(file_path))
        if page_num < 1 or page_num > len(doc):
            doc.close()
            raise HTTPException(status_code=404, detail="Page not found")
        page = doc[page_num - 1]
        pix = page.get_pixmap(dpi=_PAGE_RENDER_DPI)
        img_bytes = pix.tobytes("png")
        doc.close()

        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_bytes(img_bytes)

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
