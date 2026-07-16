"""Self-contained dashboard artifact — the executive "check it monthly" page.

Exports ONE self-contained HTML fragment (no external resources, no
<!DOCTYPE>/<html>/<head>/<body> wrapper) that a Claude session publishes as a
private claude.ai Artifact at a stable URL after each refresh. The artifact
runtime wraps the fragment in a full document and enforces a strict CSP, so
everything — styles, scripts, charts, the US map — must be inline.

Data comes from the same query layer the live dashboard uses (app.stats,
app.web.trends) plus the on-disk report files (monthly brief, national
landscape). The template is templates/artifact_dashboard.html, rendered with
its own Jinja2 environment — no FastAPI import.

The publish half lives outside this module: the refresh skill reads
data/reports/artifact/ARTIFACT.json (written by the publishing Claude session,
never by this exporter) to republish to the same URL instead of minting a new
artifact.
"""
from __future__ import annotations

import html as html_mod
import json
import math
import re
from datetime import date, datetime, timedelta
from pathlib import Path

from sqlalchemy import select, text

import app.database as db
import app.stats as stats
from app.config import PROJECT_ROOT, REPORTS_DIR
from app.models import RefreshRun
from app.reports import brief as brief_mod
from app.reports.brief import STATE_NAMES, _truncate_words
import app.web.trends as trends

ARTIFACT_DIR = REPORTS_DIR / "artifact"
TEMPLATES_DIR = PROJECT_ROOT / "templates"
US_MAP_PARTIAL = (PROJECT_ROOT / "app" / "web" / "templates"
                  / "partials" / "us_map_paths.html")

MAX_BYTES = 4_500_000
ROLLUP_WORDS = 120

# Categorical chart palette, validated (dataviz six-checks) against white and
# the dark card surface #1B2636. Series always take colors in this fixed
# order; the template exposes them as --chart-1..6 per theme.
CHART_COLORS_LIGHT = ["#0F7EB0", "#B45309", "#2E7D4F",
                      "#A23B72", "#5B5BD6", "#9A6E00"]
CHART_COLORS_DARK = ["#2E8FC4", "#C67C0E", "#3F9A63",
                     "#C05590", "#7D7DE8", "#A98A2A"]
MAX_SERIES = len(CHART_COLORS_LIGHT)


class ArtifactValidationError(ValueError):
    """The rendered HTML violates the artifact contract."""

    def __init__(self, violations: list[str]):
        self.violations = violations
        super().__init__("; ".join(violations))


# ---------------------------------------------------------------------------
# Validation — the artifact contract, enforced at build time and in tests.
# ---------------------------------------------------------------------------

# \b after head/body/html keeps <header>/<h1> etc. legal.
_WRAPPER_RE = re.compile(r"<!DOCTYPE|<html\b|<head\b|<body\b", re.I)
# Any src/srcset that leaves the document (a href stays legal — links only
# navigate, they never load a resource under the artifact CSP).
_EXT_SRC_RE = re.compile(r"""(?:src|srcset)\s*=\s*["'](?:https?:)?//""", re.I)
_LINK_TAG_RE = re.compile(r"<link\b|<iframe\b|<object\b|<embed\b", re.I)
_CSS_EXT_RE = re.compile(r"""@import|url\(\s*["']?(?:https?:)?//""", re.I)
_JS_NET_RE = re.compile(
    r"fetch\s*\(|XMLHttpRequest|WebSocket\s*\(|EventSource\s*\(|sendBeacon",
    re.I)


def validate_artifact_html(html: str, max_bytes: int = MAX_BYTES) -> list[str]:
    """Return contract violations for the rendered fragment (empty = valid)."""
    violations: list[str] = []
    if not html.lstrip().lower().startswith("<title>"):
        violations.append("fragment must start with a <title> element")
    m = _WRAPPER_RE.search(html)
    if m:
        violations.append(f"forbidden document wrapper tag: {m.group(0)!r}")
    if _EXT_SRC_RE.search(html):
        violations.append("external src/srcset resource load found")
    m = _LINK_TAG_RE.search(html)
    if m:
        violations.append(f"forbidden resource-loading tag: {m.group(0)!r}")
    if _CSS_EXT_RE.search(html):
        violations.append("external CSS load (@import / url(http...)) found")
    if _JS_NET_RE.search(html):
        violations.append("network API call in script (fetch/XHR/...) found")
    size = len(html.encode("utf-8"))
    if size > max_bytes:
        violations.append(f"output is {size:,} bytes (cap {max_bytes:,})")
    return violations


def _sanitize_rendered_html(html: str) -> str:
    """Defense-in-depth for markdown-rendered blocks (brief, landscape).

    The markdown package passes raw HTML through, and those files carry
    model-written prose — strip script tags, inline event handlers, and
    javascript: URLs before the block is marked safe for the template.
    """
    html = re.sub(r"(?is)<script\b.*?</script>", "", html)
    html = re.sub(r"(?is)<script\b[^>]*>", "", html)
    html = re.sub(r"""(?i)\s+on\w+\s*=\s*("[^"]*"|'[^']*'|\S+)""", "", html)
    html = re.sub(r"""(?i)(href|src)\s*=\s*(["']?)\s*javascript:[^"'\s>]*""",
                  r'\1=\2#', html)
    return html


# ---------------------------------------------------------------------------
# SVG charts — server-rendered, no library. Colors ride CSS custom properties
# (inline style="" attributes, since SVG presentation attributes can't take
# var()), so the same markup follows the light/dark theme.
# ---------------------------------------------------------------------------

def _nice_step(max_val: float, ticks: int = 4) -> float:
    raw = max(max_val, 1) / ticks
    mag = 10 ** math.floor(math.log10(raw))
    for f in (1, 2, 5, 10):
        if f * mag >= raw:
            return f * mag
    return 10 * mag


def _svg_line_chart(quarters: list[str], series: list[dict], *,
                    width: int = 760, height: int = 300,
                    end_labels: bool = False, title: str = "") -> str:
    """Multi-series quarterly line chart as an inline SVG string.

    series = [{"name": str, "data": [int, ...]}] — max MAX_SERIES series,
    each series i stroked with var(--chart-{i+1}). Every point carries a
    <title> for native hover; end_labels adds a name+value label at the last
    point (use only when series count is small enough not to collide).
    """
    series = series[:MAX_SERIES]
    n = max(len(quarters), 2)
    pad_l, pad_t, pad_b = 42, 14, 30
    pad_r = 118 if end_labels else 36
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_t - pad_b

    max_val = max((max(s["data"]) for s in series if s["data"]), default=0)
    step = _nice_step(max_val)
    y_top = step * 4 if max_val else 4

    def x(i: int) -> float:
        return round(pad_l + i / (n - 1) * plot_w, 1)

    def y(v: float) -> float:
        return round(pad_t + plot_h - (v / y_top) * plot_h, 1)

    esc = html_mod.escape
    parts: list[str] = []
    parts.append(
        f'<svg viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{esc(title)}" xmlns="http://www.w3.org/2000/svg" '
        f'class="bp-chart">')

    # gridlines + y tick labels
    for t in range(5):
        v = step * t
        yy = y(v)
        parts.append(
            f'<line x1="{pad_l}" y1="{yy}" x2="{width - pad_r}" y2="{yy}" '
            f'style="stroke:var(--line);stroke-width:1"/>')
        parts.append(
            f'<text x="{pad_l - 8}" y="{yy + 3.5}" text-anchor="end" '
            f'style="fill:var(--muted);font-size:10px;'
            f'font-family:var(--font-mono)">{v:g}</text>')

    # x labels — every other quarter to stay readable at phone widths
    for i, q in enumerate(quarters):
        if i % 2 != (len(quarters) - 1) % 2:
            continue
        parts.append(
            f'<text x="{x(i)}" y="{height - 8}" text-anchor="middle" '
            f'style="fill:var(--muted);font-size:10px;'
            f'font-family:var(--font-mono)">{esc(q)}</text>')

    for si, s in enumerate(series):
        color = f"var(--chart-{si + 1})"
        data = list(s["data"])[:n]
        pts = " ".join(f"{x(i)},{y(v)}" for i, v in enumerate(data))
        parts.append(
            f'<polyline points="{pts}" style="fill:none;stroke:{color};'
            f'stroke-width:2;stroke-linejoin:round;stroke-linecap:round"/>')
        for i, v in enumerate(data):
            label = f"{esc(quarters[i])} - {esc(s['name'])}: {v}"
            parts.append(
                f'<circle cx="{x(i)}" cy="{y(v)}" r="2.5" '
                f'style="fill:{color}"/>')
            parts.append(
                f'<circle cx="{x(i)}" cy="{y(v)}" r="8" style="fill:#000;'
                f'fill-opacity:0"><title>{label}</title></circle>')
        if end_labels and data:
            lx, ly = x(len(data) - 1) + 8, y(data[-1]) + 4
            parts.append(
                f'<text x="{lx}" y="{ly}" style="fill:{color};'
                f'font-size:11px;font-weight:600;'
                f'font-family:var(--font-body)">{esc(s["name"])} '
                f'<tspan style="font-family:var(--font-mono)">'
                f'{data[-1]}</tspan></text>')

    parts.append("</svg>")
    return "".join(parts)


# ---------------------------------------------------------------------------
# Landscape report — latest *-board-landscape.md, citations rewritten to each
# board's PUBLIC site (dashboard-internal /meeting/... links are dead inside
# an artifact), split into per-heading <details> sections.
# ---------------------------------------------------------------------------

_CITATION_RE = re.compile(
    r"\[([^\]]+)\]\(/board/(\w{2})/(\w+_\w+)#(\d{4}-\d{2}-\d{2})\)")
_INTERNAL_LINK_RE = re.compile(r"\[([^\]]+)\]\(/[^)]*\)")
_ANY_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")


def _strip_md_links(text_val: str) -> str:
    """Markdown links -> their text (for blocks rendered as plain text,
    like the board-grid rollup snippets, where a raw [date](/board/...)
    would show up literally)."""
    return _ANY_MD_LINK_RE.sub(r"\1", text_val or "")


def _rewrite_landscape_links(md_text: str, board_links: dict[str, str]) -> str:
    def _cite(m: re.Match) -> str:
        url = board_links.get(m.group(3), "")
        return f"[{m.group(1)}]({url})" if url else m.group(1)

    md_text = _CITATION_RE.sub(_cite, md_text)
    # Any remaining dashboard-internal link would 404 inside the artifact —
    # drop to plain text.
    return _INTERNAL_LINK_RE.sub(r"\1", md_text)


def _render_landscape(md_text: str, board_links: dict[str, str]) -> dict:
    import markdown as _markdown

    md_text = _rewrite_landscape_links(md_text, board_links)

    def _to_html(chunk: str) -> str:
        return _sanitize_rendered_html(
            _markdown.markdown(chunk, extensions=["tables"]))

    sections: list[dict] = []
    intro_lines: list[str] = []
    current_title: str | None = None
    current_lines: list[str] = []
    for line in md_text.splitlines():
        if line.startswith("## "):
            if current_title is not None:
                sections.append({"title": current_title,
                                 "html": _to_html("\n".join(current_lines))})
            current_title = line[3:].strip()
            current_lines = []
        elif current_title is None:
            intro_lines.append(line)
        else:
            current_lines.append(line)
    if current_title is not None:
        sections.append({"title": current_title,
                         "html": _to_html("\n".join(current_lines))})

    # Drop the top-level "# ..." heading from the intro — the tab supplies it.
    intro_md = re.sub(r"^#\s+.*$", "", "\n".join(intro_lines),
                      count=1, flags=re.M)
    return {"intro_html": _to_html(intro_md), "sections": sections}


# ---------------------------------------------------------------------------
# Data assembly
# ---------------------------------------------------------------------------

async def _latest_refresh_run() -> RefreshRun | None:
    async with db.async_session() as session:
        return (await session.execute(
            select(RefreshRun).order_by(RefreshRun.id.desc()).limit(1)
        )).scalars().first()


def _latest_brief() -> dict | None:
    """Latest monthly brief (rendered HTML + sidecar numbers), or None."""
    import markdown as _markdown

    ym = brief_mod.latest_brief_ym()
    if not ym:
        return None
    md_path = brief_mod.BRIEFS_DIR / f"{ym}.md"
    sidecar_path = brief_mod.BRIEFS_DIR / f"{ym}.json"
    sidecar: dict = {}
    if sidecar_path.exists():
        try:
            sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            sidecar = {}
    body = md_path.read_text(encoding="utf-8")
    # Drop the file's own H1 — the panel supplies the heading.
    body = re.sub(r"^#\s+.*$", "", body, count=1, flags=re.M)
    return {
        "ym": ym,
        "month_name": brief_mod._month_name(ym),
        "html": _sanitize_rendered_html(
            _markdown.markdown(body, extensions=["tables"])),
        "coverage": sidecar.get("sections", {}).get("coverage", {}),
        "counts": sidecar.get("sections", {}).get("counts", {}),
        "window": sidecar.get("window", {}),
    }


_BOARD_GRID_SQL = """
    SELECT b.code, b.state, b.name, b.board_type, b.discovery_status,
           b.minutes_url, b.homepage, b.summary,
           COUNT(m.id) AS mtgs,
           MAX(CASE WHEN m.meeting_date <= date('now')
                    THEN m.meeting_date END) AS last_meeting,
           MAX(CASE WHEN substr(replace(m.scraped_at,'T',' '),1,19) > :since
                    THEN 1 ELSE 0 END) AS changed
    FROM boards b
    LEFT JOIN meetings m ON m.board_id = b.id
    GROUP BY b.id
    ORDER BY b.state, b.code
"""


async def _board_grid(changed_since: str) -> list[dict]:
    """One row per board: status, last meeting, changed-this-period flag,
    docs+text counts, truncated rollup snippet, public link."""
    per_board = await stats.per_board_counts()
    async with db.async_session() as session:
        rows = (await session.execute(
            text(_BOARD_GRID_SQL), {"since": changed_since[:19]})).all()

    grid: list[dict] = []
    for r in rows:
        counts = per_board.get(r.code, {})
        # Same status bucketing as the dashboard's /boards directory.
        if r.mtgs > 0:
            status = "collected"
        elif r.discovery_status in ("found", "manual"):
            status = "discovered"
        elif r.discovery_status in ("none_published", "blocked"):
            status = r.discovery_status
        else:
            status = "pending"
        grid.append({
            "code": r.code,
            "state": r.state,
            "state_name": STATE_NAMES.get(r.state, r.state),
            "name": r.name,
            "board_type": r.board_type,
            "status": status,
            "mtgs": r.mtgs,
            "docs_text": counts.get("docs_text", 0),
            "mtgs_summarized": counts.get("mtgs_summarized", 0),
            "last_meeting": r.last_meeting,
            "changed": bool(r.changed),
            "rollup": _truncate_words(_strip_md_links(r.summary), ROLLUP_WORDS),
            "url": r.minutes_url or r.homepage or "",
        })
    return grid


def _state_statuses(grid: list[dict]) -> dict[str, str]:
    """Per-state map status with the dashboard's precedence: collected >
    discovered > no_minutes > pending."""
    rank = {"pending": 0, "no_minutes": 1, "discovered": 2, "collected": 3}
    to_state = {"collected": "collected", "discovered": "discovered",
                "none_published": "no_minutes", "blocked": "no_minutes",
                "pending": "pending"}
    out: dict[str, str] = {}
    for row in grid:
        cand = to_state[row["status"]]
        best = out.get(row["state"])
        if best is None or rank[cand] > rank[best]:
            out[row["state"]] = cand
    return out


def _build_map_svg(state_statuses: dict[str, str]) -> str:
    """Wrap the shared US map path set in an inline SVG with per-state fills."""
    try:
        paths = US_MAP_PARTIAL.read_text(encoding="utf-8")
    except OSError:
        return ""
    css = ["<style>"]
    for state, status in sorted(state_statuses.items()):
        css.append(
            f'.bp-map [data-state="{state}"]{{fill:var(--map-{status})}}')
    css.append("</style>")
    return (
        '<svg viewBox="0 0 960 600" role="img" '
        'aria-label="Coverage by state" class="bp-map" '
        'xmlns="http://www.w3.org/2000/svg">'
        + "".join(css) + paths + "</svg>")


_SOURCE_ROW_CAP = 30
_SOURCE_QUOTE_WORDS = 40


async def _window_fact_sources(since: str, until: str) -> list[dict]:
    """The verbatim quotes behind this window's fact-backed numbers, per
    fact type — the artifact's expandable 'show your work' payload
    (Frank's V4-C ruling). Rows capped; quotes truncated."""
    s, u = since[:10], until[:10]
    sections: list[dict] = []
    async with db.async_session() as session:
        async def grab(label, count_sql, rows_sql):
            total = (await session.execute(
                text(count_sql), {"s": s, "u": u})).scalar() or 0
            rows = (await session.execute(
                text(rows_sql), {"s": s, "u": u,
                                 "l": _SOURCE_ROW_CAP})).all()
            sections.append({"label": label, "total": total, "rows": [
                {"who": r.who, "when": str(r.when_)[:10], "what": r.what,
                 "quote": _truncate_words(r.quote or "",
                                          _SOURCE_QUOTE_WORDS)}
                for r in rows]})

        await grab(
            "Discipline",
            "SELECT COUNT(*) FROM v_disciplinary "
            "WHERE meeting_date > :s AND meeting_date <= :u",
            "SELECT board_code AS who, meeting_date AS when_, "
            "       category || ' x ' || action_count AS what, quote "
            "FROM v_disciplinary "
            "WHERE meeting_date > :s AND meeting_date <= :u "
            "ORDER BY meeting_date DESC LIMIT :l")
        await grab(
            "Rules & policy",
            "SELECT COUNT(*) FROM v_policy_actions "
            "WHERE action_date > :s AND action_date <= :u",
            "SELECT board_code AS who, action_date AS when_, "
            "       title AS what, quote "
            "FROM v_policy_actions "
            "WHERE action_date > :s AND action_date <= :u "
            "ORDER BY action_date DESC LIMIT :l")
        await grab(
            "Bills",
            "SELECT COUNT(*) FROM v_legislation "
            "WHERE meeting_date > :s AND meeting_date <= :u",
            "SELECT board_code AS who, meeting_date AS when_, "
            "       bill_state || ' ' || bill_number AS what, quote "
            "FROM v_legislation "
            "WHERE meeting_date > :s AND meeting_date <= :u "
            "ORDER BY meeting_date DESC LIMIT :l")
        await grab(
            "Emerging topics",
            "SELECT COUNT(*) FROM emerging_topics "
            "WHERE first_mentioned_on > :s AND first_mentioned_on <= :u",
            "SELECT b.code AS who, et.first_mentioned_on AS when_, "
            "       et.subject AS what, et.quote "
            "FROM emerging_topics et JOIN boards b ON b.id = et.board_id "
            "WHERE et.first_mentioned_on > :s AND et.first_mentioned_on <= :u "
            "ORDER BY et.first_mentioned_on DESC LIMIT :l")
    return sections


def _load_coverage_ledger() -> list[dict]:
    """coverage_ledger.json as [{code, status, date, note}], or []."""
    ledger_path = PROJECT_ROOT / "coverage_ledger.json"
    if not ledger_path.exists():
        return []
    try:
        raw = json.loads(ledger_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    out = []
    for code, entry in sorted(raw.items()):
        if isinstance(entry, dict):
            out.append({"code": code,
                        "status": entry.get("status", ""),
                        "date": entry.get("date", ""),
                        "note": entry.get("note", "")})
    return out


def _fmt_dt(value) -> str:
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")
    return str(value)[:10]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def build_artifact(out_path: Path | None = None,
                         max_bytes: int = MAX_BYTES,
                         today: date | None = None) -> Path:
    """Assemble, render, validate, and write the dashboard artifact HTML.

    Raises ArtifactValidationError if the output violates the artifact
    contract (wrapper tags, external resources, size cap).
    """
    from jinja2 import Environment, FileSystemLoader

    from app.database import init_db
    await init_db()

    today = today or date.today()
    out = Path(out_path) if out_path else ARTIFACT_DIR / "boardpulse-dashboard.html"
    out.parent.mkdir(parents=True, exist_ok=True)

    run = await _latest_refresh_run()
    coverage = await stats.coverage_rollup()
    per_board = await stats.per_board_counts()
    totals = {
        "mtgs": sum(c["mtgs"] for c in per_board.values()),
        "docs": sum(c["docs"] for c in per_board.values()),
        "docs_text": sum(c["docs_text"] for c in per_board.values()),
        "mtgs_summarized": sum(c["mtgs_summarized"] for c in per_board.values()),
    }

    brief = _latest_brief()
    window_since = (brief or {}).get("window", {}).get("since") \
        or (datetime.now() - timedelta(days=35)).isoformat(sep=" ")
    window_until = (brief or {}).get("window", {}).get("until") \
        or datetime.now().isoformat(sep=" ")

    grid = await _board_grid(window_since)
    changed_count = sum(1 for r in grid if r["changed"])
    map_svg = _build_map_svg(_state_statuses(grid))

    tot = await trends.topics_over_time(top_n=MAX_SERIES)
    ai = await trends.topic_quarterly("AI")
    gaining = await trends.gaining_traction(limit=6)
    emerging = await trends.emerging_national(limit=8)
    watchlist = await trends.watchlist_with_counts(stats.sanitize_fts_query)
    for item in emerging.get("items", []):
        item["quote"] = _truncate_words(item.get("quote") or "", 40)

    topics_chart = _svg_line_chart(
        tot["quarters"], tot["series"],
        title="Topic mentions by quarter") if tot["series"] else ""
    ai_chart = _svg_line_chart(
        ai["quarters"],
        [{"name": "Meetings", "data": ai["meetings"]},
         {"name": "Boards", "data": ai["boards"]}],
        end_labels=True, title="AI focus by quarter") \
        if any(ai["meetings"]) else ""

    landscape = None
    landscape_files = sorted(REPORTS_DIR.glob("*-board-landscape.md"),
                             reverse=True)
    if landscape_files:
        board_links = {r["code"]: r["url"] for r in grid if r["url"]}
        landscape = _render_landscape(
            landscape_files[0].read_text(encoding="utf-8"), board_links)
        landscape["date"] = landscape_files[0].stem[:10]

    regressed = []
    if run and run.boards_regressed:
        regressed = [c.strip() for c in run.boards_regressed.split(",")
                     if c.strip()]

    from app.quality.audit import latest_audit
    audit = latest_audit()
    fact_sources = await _window_fact_sources(window_since, window_until)

    ctx = {
        "generated_on": today.isoformat(),
        "header": {
            "refresh_date": _fmt_dt(run.finished_at or run.started_at) if run else "",
            "refresh_ok": bool(run and run.exit_code == 0),
            "boards_changed": run.boards_changed if run else 0,
            "regressed": regressed,
            "accounted": coverage["accounted"],
            "total_boards": coverage["total_boards"],
            "have_docs": coverage["have_docs"],
            **totals,
        },
        "brief": brief,
        "map_svg": map_svg,
        "watchlist": watchlist,
        "emerging": emerging,
        "gaining": gaining,
        "topics_chart": topics_chart,
        "topics_legend": [s["name"] for s in tot["series"]],
        "ai_chart": ai_chart,
        "landscape": landscape,
        "boards": grid,
        "changed_count": changed_count,
        "ledger": _load_coverage_ledger(),
        "audit": audit,
        "fact_sources": fact_sources,
        "chart_colors_light": CHART_COLORS_LIGHT,
        "chart_colors_dark": CHART_COLORS_DARK,
    }

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)),
                      autoescape=True)
    rendered = env.get_template("artifact_dashboard.html").render(**ctx)

    violations = validate_artifact_html(rendered, max_bytes=max_bytes)
    if violations:
        raise ArtifactValidationError(violations)

    out.write_text(rendered, encoding="utf-8")

    # Per-section byte report so size regressions surface in the transcript.
    report = {
        "total": len(rendered.encode("utf-8")),
        "map": len(map_svg.encode("utf-8")),
        "charts": len((topics_chart + ai_chart).encode("utf-8")),
        "brief": len((brief or {}).get("html", "").encode("utf-8")),
        "landscape": sum(len(s["html"].encode("utf-8"))
                         for s in (landscape or {}).get("sections", [])),
        "boards": sum(len(r["rollup"].encode("utf-8")) for r in grid),
    }
    print("artifact bytes: " + "  ".join(
        f"{k}={v:,}" for k, v in report.items()))
    return out
