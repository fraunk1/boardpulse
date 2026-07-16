"""Monthly delta brief — a short, forwardable 'what changed' report.

Design goal: a WEAKER model (Opus 4.8) can produce this reliably because only
TWO small prose slots are model-written. Everything else is pure SQL + string
templating computed here, deterministically, from the live database.

Two-step lifecycle:

  1. build_brief(now_iso)
     Compute every section from SQL. Write three files to
     data/reports/briefs/:
       - YYYY-MM.md          the human brief, with two placeholders
                             (<!-- PROSE:A --> and <!-- PROSE:B -->) where the
                             model prose will be spliced in later
       - YYYY-MM.json        the sidecar: window bounds + every computed number
                             (also the source of the *next* brief's window start)
       - YYYY-MM_prompt.md   a small prompt for the writer model: the computed
                             tables + each new meeting's summary truncated to
                             120 words + instructions to emit exactly
                             '## SLOT A' and '## SLOT B'

  2. ingest_brief_prose(ym)
     Read YYYY-MM_prose.md (the model's answer), splice SLOT A / SLOT B into
     the placeholders in YYYY-MM.md, and regenerate YYYY-MM.html from
     templates/brief_email.html (inline CSS, Outlook-safe, no external JS/CDN).

Everything is read-only against the DB. stdlib sqlite3, opened mode=ro.
"""
from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

# --------------------------------------------------------------------------
# Paths — resolved from this file so the module works regardless of CWD.
# --------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = PROJECT_ROOT / "boardpulse.db"
BRIEFS_DIR = PROJECT_ROOT / "data" / "reports" / "briefs"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

# Fallback window length when there is no prior brief to anchor on.
FALLBACK_DAYS = 35

# The writer prompt must stay small (target < 8k tokens) so a weaker model
# handles it reliably. In a normal month the new-meeting count is small, but a
# first/baseline brief can surface the entire back-catalog — so the prompt caps
# how many meeting summaries it inlines (the full list still lives in the .md
# appendix). Most-recent-first; the prompt notes the total when it truncates.
PROMPT_MAX_SUMMARIES = 24
PROMPT_SUMMARY_WORDS = 120

# bp hex palette (mirrors app/web/templates/base.html tailwind config) — used
# by the inline-CSS email HTML so the brief matches the dashboard brand.
PALETTE = {
    "navy": "#1B2636",
    "slate": "#354358",
    "steel": "#576A83",
    "mist": "#97A8BD",
    "cloud": "#DCE3ED",
    "frost": "#F2F5F9",
    "teal": "#139AD0",
    "teal_d": "#0F7EB0",
    "gold": "#FBAA29",
    "gold_d": "#E8950F",
    "white": "#FFFFFF",
}

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


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def _parse_iso(value: str) -> datetime:
    """Parse an ISO timestamp that may or may not carry a timezone.

    The database mixes naive ('2026-06-17 16:16:49.545104') and tz-aware
    ('2026-07-04 12:09:43+00:00') timestamps in the same column, so every
    comparison is normalized to naive-UTC here to avoid 'can't compare
    offset-naive and offset-aware datetimes' errors.
    """
    if isinstance(value, datetime):
        dt = value
    else:
        s = str(value).strip().replace("T", " ")
        # datetime.fromisoformat handles both forms in 3.11+, but be defensive.
        try:
            dt = datetime.fromisoformat(s)
        except ValueError:
            # Trim fractional seconds / trailing 'Z' if present.
            s2 = s.replace("Z", "+00:00")
            try:
                dt = datetime.fromisoformat(s2)
            except ValueError:
                s3 = re.sub(r"\.\d+", "", s2)
                dt = datetime.fromisoformat(s3)
    if dt.tzinfo is not None:
        dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
    return dt


def _to_naive_utc_iso(value: str | datetime) -> str:
    """Normalize any timestamp to a naive-UTC ISO string for SQL comparison."""
    return _parse_iso(value).isoformat(sep=" ")


def _truncate_words(text: str, limit: int) -> str:
    words = (text or "").split()
    if len(words) <= limit:
        return (text or "").strip()
    return " ".join(words[:limit]).rstrip() + " …"


def _month_name(ym: str) -> str:
    """'2026-07' -> 'July 2026'."""
    try:
        return datetime.strptime(ym + "-01", "%Y-%m-%d").strftime("%B %Y")
    except ValueError:
        return ym


def _state_label(state: str) -> str:
    return STATE_NAMES.get(state, state)


def _connect_ro(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Open the DB strictly read-only (URI mode=ro)."""
    path = Path(db_path) if db_path else DB_PATH
    uri = f"file:{path.as_posix()}?mode=ro"
    con = sqlite3.connect(uri, uri=True)
    con.row_factory = sqlite3.Row
    return con


def _prior_brief_sidecar() -> Optional[dict]:
    """Return the most recent prior brief's sidecar JSON, or None.

    The next brief's window starts at the prior brief's 'until' bound.
    """
    if not BRIEFS_DIR.exists():
        return None
    sidecars = sorted(BRIEFS_DIR.glob("*.json"))
    if not sidecars:
        return None
    latest = sidecars[-1]
    try:
        return json.loads(latest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


# --------------------------------------------------------------------------
# Section computation — every number the brief reports comes from here.
# Each function is defensive: empty tables yield empty results, never errors.
# --------------------------------------------------------------------------

def _sec_coverage(con: sqlite3.Connection, since: str, until: str) -> dict:
    """Section 1 — headline coverage counts for the window."""
    cur = con.cursor()
    total_boards = cur.execute("SELECT count(*) FROM boards").fetchone()[0]
    total_meetings = cur.execute("SELECT count(*) FROM meetings").fetchone()[0]
    total_docs = cur.execute("SELECT count(*) FROM meeting_documents").fetchone()[0]

    # New meetings = learned about (scraped_at) within the window. scraped_at
    # carries mixed tz formats; the window bounds are naive-UTC ISO, and SQLite
    # string comparison of ISO timestamps is chronological for same-shaped
    # strings. To be robust to the '+00:00' suffix we compare on the leading
    # 19 chars (YYYY-MM-DD HH:MM:SS), which sorts correctly in either form.
    new_meetings = cur.execute(
        "SELECT count(*) FROM meetings "
        "WHERE substr(replace(scraped_at,'T',' '),1,19) > ? "
        "AND substr(replace(scraped_at,'T',' '),1,19) <= ?",
        (since[:19], until[:19]),
    ).fetchone()[0]

    boards_touched = cur.execute(
        "SELECT count(DISTINCT board_id) FROM meetings "
        "WHERE substr(replace(scraped_at,'T',' '),1,19) > ? "
        "AND substr(replace(scraped_at,'T',' '),1,19) <= ?",
        (since[:19], until[:19]),
    ).fetchone()[0]

    return {
        "total_boards": total_boards,
        "total_meetings": total_meetings,
        "total_documents": total_docs,
        "new_meetings": new_meetings,
        "boards_touched": boards_touched,
    }


def _sec_by_the_numbers(con: sqlite3.Connection, prior: Optional[dict]) -> dict:
    """Section 3 — current fact-table totals vs. the prior brief.

    Compares the four fact classes plus meetings/documents against the numbers
    the prior brief recorded in its sidecar. With no prior brief every 'prior'
    is None and the template shows a dash.
    """
    cur = con.cursor()

    def one(sql: str) -> int:
        return cur.execute(sql).fetchone()[0]

    current = {
        "meetings": one("SELECT count(*) FROM meetings"),
        "documents": one("SELECT count(*) FROM meeting_documents"),
        "policy_actions": one("SELECT count(*) FROM policy_actions"),
        "legislation": one("SELECT count(*) FROM legislation_mentions"),
        "disciplinary": one("SELECT count(*) FROM disciplinary_actions"),
        "emerging_topics": one("SELECT count(*) FROM emerging_topics"),
    }

    prior_totals = (prior or {}).get("sections", {}).get("by_the_numbers", {})
    rows = []
    labels = {
        "meetings": "Meetings tracked",
        "documents": "Documents held",
        "policy_actions": "Rule / policy actions",
        "legislation": "Bills mentioned",
        "disciplinary": "Discipline records",
        "emerging_topics": "First-mention topics",
    }
    for key, label in labels.items():
        now_val = current[key]
        prev = prior_totals.get(key, {}).get("current") if prior_totals else None
        # prior_totals stores each row as {"current": N}; fall back to None.
        if isinstance(prev, dict):
            prev = prev.get("current")
        delta = (now_val - prev) if isinstance(prev, int) else None
        rows.append({
            "key": key,
            "label": label,
            "current": now_val,
            "prior": prev if isinstance(prev, int) else None,
            "delta": delta,
        })
    return {"rows": rows, "has_prior": prior is not None}


def _sec_first_mentions(con: sqlite3.Connection, since: str, until: str) -> list[dict]:
    """Section 4 — new emerging_topics first mentioned in the window."""
    cur = con.cursor()
    try:
        rows = cur.execute(
            """
            SELECT et.topic_slug, et.subject, et.first_mentioned_on,
                   et.quote, b.code AS board_code, b.state
            FROM emerging_topics et
            JOIN boards b ON b.id = et.board_id
            WHERE et.first_mentioned_on > ? AND et.first_mentioned_on <= ?
            ORDER BY et.first_mentioned_on DESC, b.code
            """,
            (since[:10], until[:10]),
        ).fetchall()
    except sqlite3.OperationalError:
        return []
    return [{
        "topic_slug": r["topic_slug"],
        "subject": r["subject"],
        "date": r["first_mentioned_on"],
        "quote": r["quote"],
        "board_code": r["board_code"],
        "state": r["state"],
        "state_label": _state_label(r["state"]),
    } for r in rows]


def _sec_rule_changes(con: sqlite3.Connection, since: str, until: str) -> list[dict]:
    """Section 5 — new policy_actions in the window.

    Each rendered as '{Board}: {topic} moved to {stage}'.
    """
    cur = con.cursor()
    try:
        rows = cur.execute(
            """
            SELECT pa.topic, pa.stage, pa.instrument, pa.title,
                   pa.rule_reference, pa.action_date, pa.quote,
                   pa.board_code, pa.state
            FROM v_policy_actions pa
            WHERE pa.action_date > ? AND pa.action_date <= ?
            ORDER BY pa.action_date DESC, pa.board_code
            """,
            (since[:10], until[:10]),
        ).fetchall()
    except sqlite3.OperationalError:
        return []
    out = []
    for r in rows:
        topic = (r["topic"] or "").replace("-", " ")
        stage = (r["stage"] or "").replace("_", " ")
        out.append({
            "board_code": r["board_code"],
            "state": r["state"],
            "state_label": _state_label(r["state"]),
            "topic": topic,
            "stage": stage,
            "instrument": r["instrument"],
            "title": r["title"],
            "rule_reference": r["rule_reference"],
            "date": r["action_date"],
            "quote": r["quote"],
            "headline": f"{_state_label(r['state'])}: {topic} moved to {stage}",
        })
    return out


def _sec_bills(con: sqlite3.Connection, since: str, until: str) -> list[dict]:
    """Section 6 — new legislation_mentions in the window."""
    cur = con.cursor()
    try:
        rows = cur.execute(
            """
            SELECT l.bill_number, l.bill_state, l.subject, l.topic,
                   l.involvement, l.status_note, l.quote,
                   l.board_code, l.state, l.meeting_date
            FROM v_legislation l
            WHERE l.meeting_date > ? AND l.meeting_date <= ?
            ORDER BY l.meeting_date DESC, l.bill_state, l.bill_number
            """,
            (since[:10], until[:10]),
        ).fetchall()
    except sqlite3.OperationalError:
        return []
    return [{
        "bill_number": r["bill_number"],
        "bill_state": r["bill_state"],
        "subject": r["subject"],
        "topic": (r["topic"] or "").replace("-", " ") if r["topic"] else None,
        "involvement": r["involvement"],
        "status_note": r["status_note"],
        "quote": r["quote"],
        "board_code": r["board_code"],
        "state": r["state"],
        "state_label": _state_label(r["state"]),
        "date": r["meeting_date"],
    } for r in rows]


def _sec_watchlist(con: sqlite3.Connection, since: str, until: str) -> list[dict]:
    """Section 7 — per watchlist term, new full-text hits in the window.

    A 'new hit' = a meeting_document whose text matches the term AND whose
    meeting was scraped inside the window. Up to 3 example citations per term.
    """
    # Shared FTS5 sanitizer (same definition the search page uses). Imported
    # here, not at module top, so importing brief stays dependency-light.
    from app.stats import sanitize_fts_query

    cur = con.cursor()
    try:
        terms = cur.execute(
            "SELECT id, term, label FROM watchlist_terms ORDER BY label"
        ).fetchall()
    except sqlite3.OperationalError:
        return []

    results = []
    for t in terms:
        term = t["term"]
        fts_query = sanitize_fts_query(term) or f'"{term}"'
        try:
            hits = cur.execute(
                """
                SELECT m.id AS meeting_id, m.meeting_date, m.title,
                       b.code AS board_code, b.state
                FROM doc_fts
                JOIN meeting_documents d ON d.id = doc_fts.rowid
                JOIN meetings m ON m.id = d.meeting_id
                JOIN boards b ON b.id = m.board_id
                WHERE doc_fts MATCH ?
                  AND substr(replace(m.scraped_at,'T',' '),1,19) > ?
                  AND substr(replace(m.scraped_at,'T',' '),1,19) <= ?
                GROUP BY m.id
                ORDER BY m.meeting_date DESC
                """,
                (fts_query, since[:19], until[:19]),
            ).fetchall()
        except sqlite3.OperationalError:
            hits = []
        cites = [{
            "meeting_id": h["meeting_id"],
            "date": h["meeting_date"],
            "title": h["title"],
            "board_code": h["board_code"],
            "state": h["state"],
            "state_label": _state_label(h["state"]),
        } for h in hits[:3]]
        results.append({
            "term": term,
            "label": t["label"],
            "count": len(hits),
            "citations": cites,
        })
    return results


def _sec_discipline(con: sqlite3.Connection, since: str, until: str) -> dict:
    """Section 8 — discipline category counts this window vs. trailing-3-month avg.

    'This window' = disciplinary_actions whose meeting_date is in the window.
    'Trailing avg' = the monthly average over the 3 full months preceding the
    window start (a stable baseline to say 'more than usual / less than usual').
    """
    cur = con.cursor()
    try:
        this_rows = cur.execute(
            """
            SELECT da.category, COALESCE(SUM(da.action_count), 0) AS n
            FROM v_disciplinary da
            WHERE da.meeting_date > ? AND da.meeting_date <= ?
            GROUP BY da.category
            """,
            (since[:10], until[:10]),
        ).fetchall()
        boards_contributing = cur.execute(
            "SELECT COUNT(DISTINCT board_code) FROM v_disciplinary "
            "WHERE meeting_date > ? AND meeting_date <= ?",
            (since[:10], until[:10]),
        ).fetchone()[0]
        total_boards = cur.execute("SELECT count(*) FROM boards").fetchone()[0]
    except sqlite3.OperationalError:
        return {"rows": [], "trailing_start": None, "trailing_end": None,
                "boards_contributing": 0, "total_boards": 0}

    since_date = _parse_iso(since).date()
    trailing_start = (since_date - timedelta(days=90)).isoformat()
    trailing_end = since_date.isoformat()
    try:
        trail_rows = cur.execute(
            """
            SELECT da.category, COALESCE(SUM(da.action_count), 0) AS n
            FROM v_disciplinary da
            WHERE da.meeting_date > ? AND da.meeting_date <= ?
            GROUP BY da.category
            """,
            (trailing_start, trailing_end),
        ).fetchall()
    except sqlite3.OperationalError:
        trail_rows = []

    this_map = {r["category"]: r["n"] for r in this_rows}
    trail_map = {r["category"]: r["n"] for r in trail_rows}
    categories = sorted(set(this_map) | set(trail_map))
    rows = []
    for cat in categories:
        this_n = this_map.get(cat, 0)
        trail_avg = round(trail_map.get(cat, 0) / 3.0, 1)
        rows.append({
            "category": cat.replace("_", " "),
            "this_window": this_n,
            "trailing_avg": trail_avg,
        })
    return {
        "rows": rows,
        "trailing_start": trailing_start,
        "trailing_end": trailing_end,
        "boards_contributing": boards_contributing,
        "total_boards": total_boards,
    }


def _sec_new_meetings(con: sqlite3.Connection, since: str, until: str) -> list[dict]:
    """Section 9 (appendix) — new meetings grouped by state.

    Also carries each meeting's own summary (untruncated here; the prompt
    builder truncates to 120 words) so the writer model has real substance.
    """
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT m.id AS meeting_id, m.meeting_date, m.title, m.summary,
               m.scraped_at, b.code AS board_code, b.state, b.name AS board_name
        FROM meetings m
        JOIN boards b ON b.id = m.board_id
        WHERE substr(replace(m.scraped_at,'T',' '),1,19) > ?
          AND substr(replace(m.scraped_at,'T',' '),1,19) <= ?
        ORDER BY b.state, b.code, m.meeting_date DESC
        """,
        (since[:19], until[:19]),
    ).fetchall()
    return [{
        "meeting_id": r["meeting_id"],
        "date": r["meeting_date"],
        "title": r["title"],
        "summary": r["summary"],
        "board_code": r["board_code"],
        "board_name": r["board_name"],
        "state": r["state"],
        "state_label": _state_label(r["state"]),
    } for r in rows]


# --------------------------------------------------------------------------
# Markdown rendering — the .md the server template renders, with placeholders.
# --------------------------------------------------------------------------

def _render_markdown(data: dict) -> str:
    """Assemble the brief .md with <!-- PROSE:A --> / <!-- PROSE:B --> markers."""
    ym = data["window"]["ym"]
    month = _month_name(ym)
    since = data["window"]["since"]
    until = data["window"]["until"]
    cov = data["sections"]["coverage"]
    is_first = data["window"]["is_first_brief"]

    L: list[str] = []
    L.append(f"# Board Pulse — Monthly Delta Brief")
    L.append("")
    L.append(f"**Period:** {month}  ")
    L.append(f"**Window:** {since[:10]} → {until[:10]}  ")
    if is_first:
        L.append(f"**Note:** This is the first brief. It establishes the "
                 f"baseline; the window uses a {FALLBACK_DAYS}-day look-back.  ")
    L.append(f"**Coverage:** {cov['total_boards']} boards tracked · "
             f"{cov['new_meetings']} new meeting record(s) this period across "
             f"{cov['boards_touched']} board(s) · "
             f"{cov['total_meetings']} meetings and {cov['total_documents']} "
             f"documents held in total.")
    L.append("")

    # Section 2 — SLOT A prose placeholder
    L.append("## The month in brief")
    L.append("")
    L.append("<!-- PROSE:A -->")
    L.append("")

    # Section 3 — by the numbers vs prior brief
    L.append("## By the numbers")
    L.append("")
    btn = data["sections"]["by_the_numbers"]
    if btn["has_prior"]:
        L.append("| Measure | This brief | Prior brief | Change |")
        L.append("| --- | ---: | ---: | ---: |")
        for r in btn["rows"]:
            prior = r["prior"] if r["prior"] is not None else "—"
            if r["delta"] is None:
                delta = "—"
            elif r["delta"] > 0:
                delta = f"+{r['delta']}"
            else:
                delta = str(r["delta"])
            L.append(f"| {r['label']} | {r['current']} | {prior} | {delta} |")
    else:
        L.append("| Measure | This brief |")
        L.append("| --- | ---: |")
        for r in btn["rows"]:
            L.append(f"| {r['label']} | {r['current']} |")
        L.append("")
        L.append("_No prior brief to compare against — this establishes the baseline._")
    L.append("")

    # Section 4 — first mentions
    L.append("## First mentions")
    L.append("")
    fm = data["sections"]["first_mentions"]
    if fm:
        for r in fm:
            L.append(f"- **{r['state_label']}** — {r['subject']} "
                     f"({r['date']}). “{_truncate_words(r['quote'], 40)}”")
    else:
        L.append("_Nothing this period._")
    L.append("")

    # Section 5 — rule changes + SLOT B gloss
    L.append("## Rule changes")
    L.append("")
    rc = data["sections"]["rule_changes"]
    if rc:
        for r in rc:
            ref = f" ({r['rule_reference']})" if r["rule_reference"] else ""
            L.append(f"- {r['headline']}{ref} — {r['date']}.")
        L.append("")
        L.append("<!-- PROSE:B -->")
    else:
        L.append("_Nothing this period._")
    L.append("")

    # Section 6 — bills
    L.append("## Bills mentioned")
    L.append("")
    bills = data["sections"]["bills"]
    if bills:
        for r in bills:
            inv = f" — {r['involvement']}" if r["involvement"] else ""
            L.append(f"- **{r['bill_state']} {r['bill_number']}**{inv}: "
                     f"{r['subject']} ({r['state_label']} board, {r['date']}).")
    else:
        L.append("_Nothing this period._")
    L.append("")

    # Section 7 — watchlist
    L.append("## Watchlist")
    L.append("")
    wl = data["sections"]["watchlist"]
    if wl:
        for r in wl:
            if r["count"]:
                cites = "; ".join(
                    f"{c['board_code']} {c['date']}" for c in r["citations"]
                )
                more = "" if r["count"] <= 3 else f" (+{r['count'] - 3} more)"
                L.append(f"- **{r['label']}** — {r['count']} new hit(s): "
                         f"{cites}{more}.")
            else:
                L.append(f"- **{r['label']}** — no new hits.")
    else:
        L.append("_No watchlist terms configured._")
    L.append("")

    # Section 8 — discipline
    L.append("## Discipline")
    L.append("")
    disc = data["sections"]["discipline"]
    if disc["rows"]:
        L.append("| Category | This window | Trailing 3-mo avg |")
        L.append("| --- | ---: | ---: |")
        for r in disc["rows"]:
            L.append(f"| {r['category']} | {r['this_window']} | "
                     f"{r['trailing_avg']} |")
        if disc.get("total_boards"):
            L.append("")
            L.append(f"_Basis: {disc.get('boards_contributing', 0)} of "
                     f"{disc['total_boards']} boards reported discipline in "
                     f"this window; meetings with readable documents only._")
    else:
        L.append("_Nothing this period._")
    L.append("")

    # Section 9 — appendix: new meetings by state
    L.append("## Appendix — new meetings by state")
    L.append("")
    nm = data["sections"]["new_meetings"]
    if nm:
        by_state: dict[str, list] = {}
        for m in nm:
            by_state.setdefault(m["state_label"], []).append(m)
        for state_label in sorted(by_state):
            L.append(f"**{state_label}**")
            L.append("")
            for m in by_state[state_label]:
                title = m["title"] or "(untitled meeting)"
                L.append(f"- {m['board_code']} — {m['date']} — {title}")
            L.append("")
    else:
        L.append("_No new meetings this period._")
    L.append("")

    L.append("---")
    L.append("")
    L.append("_Board Pulse · Federation of State Medical Boards. "
             "This brief is descriptive; it records what boards did and "
             "discussed, not what they should do._")
    L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------
# Prompt rendering — the small writer-model prompt (target < 8k tokens).
# --------------------------------------------------------------------------

def _render_prompt(data: dict) -> str:
    ym = data["window"]["ym"]
    month = _month_name(ym)
    cov = data["sections"]["coverage"]
    rc = data["sections"]["rule_changes"]
    fm = data["sections"]["first_mentions"]
    nm = data["sections"]["new_meetings"]

    P: list[str] = []
    P.append(f"# Writer prompt — Board Pulse delta brief, {month}")
    P.append("")
    P.append("You are writing two short prose slots for a monthly 'what changed' "
             "brief that a state-medical-board regulator forwards to colleagues. "
             "Audience: non-technical regulators. Voice: plain English, calm, "
             "descriptive. Describe what boards did and discussed; never say what "
             "boards should do, and never add statistics or claims not present in "
             "the data below.")
    P.append("")
    P.append("## Computed facts (already true — do not restate as a list)")
    P.append("")
    P.append(f"- Window: {data['window']['since'][:10]} to "
             f"{data['window']['until'][:10]}.")
    P.append(f"- Boards tracked: {cov['total_boards']}. New meeting records this "
             f"period: {cov['new_meetings']} across {cov['boards_touched']} board(s).")
    P.append(f"- Rule/policy actions this period: {len(rc)}. "
             f"First-mention topics: {len(fm)}. New meetings: {len(nm)}.")
    P.append("")

    if rc:
        P.append("### Rule changes this period")
        for r in rc:
            ref = f" [{r['rule_reference']}]" if r["rule_reference"] else ""
            P.append(f"- {r['headline']}{ref} ({r['date']}).")
            if r["quote"]:
                P.append(f"    quote: \"{_truncate_words(r['quote'], 30)}\"")
        P.append("")
    else:
        P.append("### Rule changes this period\n- None.\n")

    if fm:
        P.append("### First mentions this period")
        for r in fm:
            P.append(f"- {r['state_label']}: {r['subject']} ({r['date']}).")
        P.append("")

    # New-meeting summaries, each truncated to bound prompt size. Only meetings
    # that actually carry a summary are useful to the writer; take the most
    # recent PROMPT_MAX_SUMMARIES so the prompt stays well under the token cap
    # even on a first/baseline brief that surfaces the whole back-catalog.
    summarized = [m for m in nm if m["summary"]]
    summarized.sort(key=lambda m: (m["date"] or ""), reverse=True)
    shown = summarized[:PROMPT_MAX_SUMMARIES]
    if shown:
        P.append(f"### Recent new-meeting summaries "
                 f"(truncated to {PROMPT_SUMMARY_WORDS} words each)")
        if len(summarized) > len(shown):
            P.append(f"_Showing the {len(shown)} most recent of "
                     f"{len(summarized)} summarized new meetings; the full list "
                     f"is in the brief appendix._")
        P.append("")
        for m in shown:
            P.append(f"**{m['state_label']} · {m['board_code']} · {m['date']}**")
            P.append(_truncate_words(m["summary"], PROMPT_SUMMARY_WORDS))
            P.append("")

    P.append("---")
    P.append("")
    P.append("## Your output — emit EXACTLY these two headed sections, nothing else")
    P.append("")
    P.append("## SLOT A")
    P.append("Write the 'month in brief' overview. At most 150 words, one to two "
             "short paragraphs. Summarize the shape of the period from the facts "
             "and summaries above. Descriptive, plain English. No recommendations, "
             "no invented numbers.")
    P.append("")
    P.append("## SLOT B")
    P.append("Write exactly three sentences glossing the top rule changes this "
             "period (from the 'Rule changes' list above). If there were no rule "
             "changes, write exactly: 'No rule or policy changes were recorded "
             "this period.' Descriptive only.")
    P.append("")
    return "\n".join(P)


# --------------------------------------------------------------------------
# Public API
# --------------------------------------------------------------------------

def build_brief(now_iso: str, db_path: Optional[Path] = None) -> dict:
    """Compute all sections from SQL and write .md + sidecar .json + _prompt.md.

    Args:
        now_iso: the 'until' bound of the window (ISO timestamp, any tz).
        db_path: override DB path (tests point this at a temp DB).

    Returns:
        The sidecar dict (window bounds + every computed number).
    """
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)

    until = _to_naive_utc_iso(now_iso)
    prior = _prior_brief_sidecar()
    if prior and prior.get("window", {}).get("until"):
        since = _to_naive_utc_iso(prior["window"]["until"])
        is_first = False
    else:
        since = (_parse_iso(until) - timedelta(days=FALLBACK_DAYS)).isoformat(sep=" ")
        is_first = True

    ym = _parse_iso(until).strftime("%Y-%m")

    con = _connect_ro(db_path)
    try:
        sections = {
            "coverage": _sec_coverage(con, since, until),
            "by_the_numbers": _sec_by_the_numbers(con, prior),
            "first_mentions": _sec_first_mentions(con, since, until),
            "rule_changes": _sec_rule_changes(con, since, until),
            "bills": _sec_bills(con, since, until),
            "watchlist": _sec_watchlist(con, since, until),
            "discipline": _sec_discipline(con, since, until),
            "new_meetings": _sec_new_meetings(con, since, until),
        }
    finally:
        con.close()

    data = {
        "window": {
            "ym": ym,
            "since": since,
            "until": until,
            "is_first_brief": is_first,
            "fallback_days": FALLBACK_DAYS,
        },
        "sections": sections,
    }

    # Sidecar: store window bounds + every computed number. by_the_numbers is
    # reshaped so the *next* brief can read prior totals as {"current": N}.
    btn_current = {
        r["key"]: {"current": r["current"]}
        for r in sections["by_the_numbers"]["rows"]
    }
    sidecar = {
        "window": data["window"],
        "sections": {
            "coverage": sections["coverage"],
            "by_the_numbers": btn_current,
            "counts": {
                "first_mentions": len(sections["first_mentions"]),
                "rule_changes": len(sections["rule_changes"]),
                "bills": len(sections["bills"]),
                "watchlist_terms": len(sections["watchlist"]),
                "watchlist_hits": sum(w["count"] for w in sections["watchlist"]),
                "discipline_categories": len(sections["discipline"]["rows"]),
                "new_meetings": len(sections["new_meetings"]),
            },
            "discipline": sections["discipline"],
        },
        "generated_at": _to_naive_utc_iso(datetime.now(timezone.utc)),
    }

    md = _render_markdown(data)
    prompt = _render_prompt(data)

    (BRIEFS_DIR / f"{ym}.md").write_text(md, encoding="utf-8")
    (BRIEFS_DIR / f"{ym}.json").write_text(
        json.dumps(sidecar, indent=2, default=str), encoding="utf-8")
    (BRIEFS_DIR / f"{ym}_prompt.md").write_text(prompt, encoding="utf-8")

    return sidecar


# --------------------------------------------------------------------------
# Prose ingest + email-HTML rendering
# --------------------------------------------------------------------------

_SLOT_RE = re.compile(
    r"^##\s*SLOT\s+([AB])\s*$(.*?)(?=^##\s*SLOT\s+[AB]\s*$|\Z)",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)


def _parse_prose(text: str) -> dict[str, str]:
    """Split a '## SLOT A ... ## SLOT B ...' file into {'A': ..., 'B': ...}."""
    out: dict[str, str] = {}
    for m in _SLOT_RE.finditer(text or ""):
        out[m.group(1).upper()] = m.group(2).strip()
    return out


def _splice_prose(md: str, prose: dict[str, str]) -> str:
    """Replace the placeholder markers with prose (or drop them if absent)."""
    a = prose.get("A", "").strip()
    b = prose.get("B", "").strip()
    # If a slot has no prose, remove the marker line entirely so the brief
    # still renders cleanly (placeholders omitted).
    md = md.replace("<!-- PROSE:A -->", a if a else "")
    md = md.replace("<!-- PROSE:B -->", b if b else "")
    # Collapse any blank runs the removal may have produced.
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md


def _sparkline_svg(values: list[float], color: str, width: int = 120,
                   height: int = 28) -> str:
    """A tiny inline SVG polyline sparkline (no JS, Outlook-tolerant)."""
    if not values:
        return ""
    if len(values) == 1:
        values = [values[0], values[0]]
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1.0
    n = len(values)
    pts = []
    for i, v in enumerate(values):
        x = round(i / (n - 1) * (width - 4) + 2, 1)
        y = round(height - 2 - ((v - lo) / span) * (height - 4), 1)
        pts.append(f"{x},{y}")
    poly = " ".join(pts)
    return (
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'xmlns="http://www.w3.org/2000/svg" style="display:block">'
        f'<polyline points="{poly}" fill="none" stroke="{color}" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        f'</svg>'
    )


def _render_email_html(md_body: str, sidecar: dict) -> str:
    """Render the inline-CSS, Outlook-safe HTML from templates/brief_email.html.

    The template is a light-weight {{ }} string template (NOT Jinja) so this
    module has no runtime dependency on the web layer. Body markdown is
    converted with the stdlib-friendly `markdown` package already in
    requirements; a tiny fallback keeps it working if that import fails.
    """
    try:
        import markdown as _md
        body_html = _md.markdown(md_body, extensions=["tables"])
    except Exception:
        # Minimal fallback: escape + paragraph-split so we never crash.
        import html as _html
        paras = [p.strip() for p in md_body.split("\n\n") if p.strip()]
        body_html = "\n".join(f"<p>{_html.escape(p)}</p>" for p in paras)

    window = sidecar.get("window", {})
    counts = sidecar.get("sections", {}).get("counts", {})
    cov = sidecar.get("sections", {}).get("coverage", {})
    ym = window.get("ym", "")
    month = _month_name(ym)

    # A sparkline of the by-the-numbers current values (visual texture only).
    btn = sidecar.get("sections", {}).get("by_the_numbers", {})
    spark_vals = [v.get("current", 0) for v in btn.values()] if btn else []
    spark = _sparkline_svg(spark_vals, PALETTE["teal"])

    template_path = TEMPLATES_DIR / "brief_email.html"
    template = template_path.read_text(encoding="utf-8")

    replacements = {
        "{{MONTH}}": month,
        "{{SINCE}}": str(window.get("since", ""))[:10],
        "{{UNTIL}}": str(window.get("until", ""))[:10],
        "{{TOTAL_BOARDS}}": str(cov.get("total_boards", "—")),
        "{{NEW_MEETINGS}}": str(cov.get("new_meetings", "—")),
        "{{BOARDS_TOUCHED}}": str(cov.get("boards_touched", "—")),
        "{{RULE_CHANGES}}": str(counts.get("rule_changes", 0)),
        "{{FIRST_MENTIONS}}": str(counts.get("first_mentions", 0)),
        "{{BILLS}}": str(counts.get("bills", 0)),
        "{{SPARKLINE}}": spark,
        "{{BODY}}": body_html,
        # Palette hooks so the template can reference brand colors by name.
        "{{C_NAVY}}": PALETTE["navy"],
        "{{C_TEAL}}": PALETTE["teal"],
        "{{C_TEAL_D}}": PALETTE["teal_d"],
        "{{C_GOLD}}": PALETTE["gold"],
        "{{C_STEEL}}": PALETTE["steel"],
        "{{C_MIST}}": PALETTE["mist"],
        "{{C_CLOUD}}": PALETTE["cloud"],
        "{{C_FROST}}": PALETTE["frost"],
    }
    for k, v in replacements.items():
        template = template.replace(k, v)
    return template


def ingest_brief_prose(ym: str) -> Path:
    """Splice model prose into the brief and (re)generate the email HTML.

    Reads YYYY-MM_prose.md, splices SLOT A / SLOT B into the placeholders in
    YYYY-MM.md, then writes YYYY-MM.html.

    Returns the path to the generated HTML.
    """
    md_path = BRIEFS_DIR / f"{ym}.md"
    prose_path = BRIEFS_DIR / f"{ym}_prose.md"
    sidecar_path = BRIEFS_DIR / f"{ym}.json"
    html_path = BRIEFS_DIR / f"{ym}.html"

    if not md_path.exists():
        raise FileNotFoundError(f"Brief markdown not found: {md_path}")

    md = md_path.read_text(encoding="utf-8")
    prose = _parse_prose(prose_path.read_text(encoding="utf-8")) \
        if prose_path.exists() else {}
    md_spliced = _splice_prose(md, prose)
    # Persist the spliced markdown back so the server template renders prose.
    md_path.write_text(md_spliced, encoding="utf-8")

    sidecar = {}
    if sidecar_path.exists():
        try:
            sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            sidecar = {}

    html = _render_email_html(md_spliced, sidecar)
    html_path.write_text(html, encoding="utf-8")
    return html_path


def latest_brief_ym() -> Optional[str]:
    """The YYYY-MM of the most recent brief on disk, or None."""
    if not BRIEFS_DIR.exists():
        return None
    mds = sorted(BRIEFS_DIR.glob("*.md"))
    mds = [p for p in mds if re.fullmatch(r"\d{4}-\d{2}", p.stem)]
    return mds[-1].stem if mds else None
