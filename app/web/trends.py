"""All trend SQL for the /trends dashboard and /topic charts.

Every function here is read-only. Two kinds of data source:

  * TOPIC data lives in ``meetings.topics`` (a JSON list). It exists NOW —
    479 of 1,933 meetings are tagged — so the gaining-traction cards and the
    topics-over-time chart work today.

  * FACT data lives in the four typed fact tables (policy_actions,
    legislation_mentions, disciplinary_actions, emerging_topics) surfaced
    through the v_* views. Those tables are EMPTY until the monthly
    extraction pass runs. Each fact function therefore checks whether its
    table has any rows and, if not, returns an empty payload plus
    ``has_data=False`` so the template can render a clean "not yet
    extracted" state instead of an empty chart.

Quarter bucketing matches app/database.py's view definitions exactly:
strftime year + quarter-of-year, e.g. "2026-Q3". We look at the last 8
quarters ending with the current (in-progress) one, and never count meetings
dated in the future (meeting_date <= date('now')).
"""
from __future__ import annotations

from datetime import date

from sqlalchemy import text

import app.database as db


# ---------------------------------------------------------------------------
# Quarter helpers — the 8-quarter window the whole page is framed around.
# ---------------------------------------------------------------------------

def _quarter_of(d: date) -> tuple[int, int]:
    return d.year, (d.month + 2) // 3


def _quarter_label(year: int, q: int) -> str:
    return f"{year}-Q{q}"


def last_n_quarters(n: int = 8, today: date | None = None) -> list[str]:
    """Return the last ``n`` quarter labels, oldest -> newest, ending with the
    quarter that contains ``today`` (the current, in-progress quarter)."""
    today = today or date.today()
    year, q = _quarter_of(today)
    labels: list[str] = []
    for _ in range(n):
        labels.append(_quarter_label(year, q))
        q -= 1
        if q == 0:
            q = 4
            year -= 1
    labels.reverse()
    return labels


def current_quarter_label(today: date | None = None) -> str:
    year, q = _quarter_of(today or date.today())
    return _quarter_label(year, q)


# SQL fragment: bucket an arbitrary date column into a "YYYY-Qn" string.
def _quarter_expr(col: str) -> str:
    return (
        f"strftime('%Y', {col}) || '-Q' || "
        f"((CAST(strftime('%m', {col}) AS INTEGER) + 2) / 3)"
    )


async def _table_has_rows(table: str) -> bool:
    """True if the given fact table has at least one row. Cheap LIMIT 1 probe."""
    async with db.async_session() as session:
        row = (await session.execute(
            text(f"SELECT 1 FROM {table} LIMIT 1")
        )).first()
    return row is not None


# ---------------------------------------------------------------------------
# TOPIC trends — driven by meetings.topics, live NOW.
# ---------------------------------------------------------------------------

async def gaining_traction(limit: int = 6, today: date | None = None) -> list[dict]:
    """Topics picking up steam: discussed by >= 3 distinct boards THIS quarter,
    compared against the prior four quarters.

    Returns cards sorted by current-quarter board reach (then by how new the
    surge is). ``is_new`` flags a topic that no board discussed in the prior
    four quarters — those get the gold "New this quarter" badge.
    """
    today = today or date.today()
    cur_q = current_quarter_label(today)
    prior_qs = last_n_quarters(5, today)[:-1]  # 4 quarters before the current one

    q_expr = _quarter_expr("m.meeting_date")
    async with db.async_session() as session:
        rows = (await session.execute(text(f"""
            SELECT je.value AS topic,
                   {q_expr} AS quarter,
                   COUNT(DISTINCT m.board_id) AS boards,
                   COUNT(*) AS mentions
            FROM meetings m
            JOIN json_each(m.topics) je
            WHERE m.topics IS NOT NULL
              AND m.meeting_date <= date('now')
            GROUP BY topic, quarter
        """))).all()

    # Fold rows into per-topic current vs prior aggregates.
    cur: dict[str, dict] = {}
    prior_boards: dict[str, set] = {}
    prior_set = set(prior_qs)
    for topic, quarter, boards, mentions in rows:
        if quarter == cur_q:
            cur[topic] = {"boards": boards, "mentions": mentions}
        elif quarter in prior_set:
            # track distinct-board presence loosely via count sum; we only
            # need "did any board discuss it before" for is_new.
            prior_boards.setdefault(topic, set()).add(quarter)

    cards: list[dict] = []
    for topic, agg in cur.items():
        if agg["boards"] < 3:
            continue
        is_new = topic not in prior_boards
        cards.append({
            "topic": topic,
            "boards": agg["boards"],
            "mentions": agg["mentions"],
            "is_new": is_new,
        })

    # New surges first, then by board reach, then mentions.
    cards.sort(key=lambda c: (not c["is_new"], -c["boards"], -c["mentions"]))
    return cards[:limit]


async def topics_over_time(top_n: int = 6, today: date | None = None) -> dict:
    """Quarterly meeting-mention counts for the top ``top_n`` topics over the
    last 8 quarters.

    Returns {"quarters": [...labels...], "series": [{"name": topic,
    "data": [...]}]} ready to hand to ApexCharts. "Top" = most total mentions
    across the window.
    """
    quarters = last_n_quarters(12, today)
    q_set = set(quarters)
    q_expr = _quarter_expr("m.meeting_date")

    async with db.async_session() as session:
        rows = (await session.execute(text(f"""
            SELECT je.value AS topic,
                   {q_expr} AS quarter,
                   COUNT(*) AS mentions
            FROM meetings m
            JOIN json_each(m.topics) je
            WHERE m.topics IS NOT NULL
              AND m.meeting_date <= date('now')
            GROUP BY topic, quarter
        """))).all()

    totals: dict[str, int] = {}
    by_topic_q: dict[str, dict[str, int]] = {}
    for topic, quarter, mentions in rows:
        if quarter not in q_set:
            continue
        totals[topic] = totals.get(topic, 0) + mentions
        by_topic_q.setdefault(topic, {})[quarter] = mentions

    top_topics = sorted(totals, key=lambda t: -totals[t])[:top_n]

    series = []
    for topic in top_topics:
        data = [by_topic_q.get(topic, {}).get(q, 0) for q in quarters]
        series.append({"name": topic.replace("-", " "), "data": data})

    return {"quarters": quarters, "series": series}


async def topic_quarterly(slug: str, today: date | None = None) -> dict:
    """For a single topic page: meetings-mentioning and boards-discussing by
    quarter over the last 8 quarters.

    Returns {"quarters": [...], "meetings": [...], "boards": [...]}.
    """
    quarters = last_n_quarters(12, today)
    q_set = set(quarters)
    q_expr = _quarter_expr("m.meeting_date")

    async with db.async_session() as session:
        rows = (await session.execute(text(f"""
            SELECT {q_expr} AS quarter,
                   COUNT(*) AS mentions,
                   COUNT(DISTINCT m.board_id) AS boards
            FROM meetings m
            JOIN json_each(m.topics) je
            WHERE m.topics IS NOT NULL
              AND je.value = :slug
              AND m.meeting_date <= date('now')
            GROUP BY quarter
        """), {"slug": slug})).all()

    by_q = {quarter: (mentions, boards) for quarter, mentions, boards in rows}
    meetings = [by_q.get(q, (0, 0))[0] for q in quarters]
    boards = [by_q.get(q, (0, 0))[1] for q in quarters]
    return {"quarters": quarters, "meetings": meetings, "boards": boards}


# ---------------------------------------------------------------------------
# FACT trends — driven by the fact tables. EMPTY until extraction runs.
# Each returns has_data=False + empty payload when its table has no rows.
# ---------------------------------------------------------------------------

async def rulemaking_pipeline(today: date | None = None) -> dict:
    """Rulemaking activity from v_policy_actions.

    Two views:
      * pipeline: count of policy actions by lifecycle stage (a funnel-style
        snapshot of where rulemaking sits).
      * adopted_over_time: quarterly count of rule ADOPTIONS
        (instrument='rule', stage='adopted') across the last 8 quarters.

    Returns has_data=False with empty payload when policy_actions is empty.
    """
    empty = {
        "has_data": False,
        "pipeline": [],
        "quarters": last_n_quarters(12, today),
        "adopted_series": [{"name": "Rules adopted", "data": []}],
        "boards_contributing": 0,
    }
    if not await _table_has_rows("policy_actions"):
        return empty

    quarters = last_n_quarters(12, today)
    q_set = set(quarters)

    async with db.async_session() as session:
        boards_contributing = (await session.execute(text(
            "SELECT COUNT(DISTINCT board_code) FROM v_policy_actions"
        ))).scalar() or 0
        stage_rows = (await session.execute(text("""
            SELECT stage, COUNT(*) AS n
            FROM v_policy_actions
            WHERE action_date <= date('now')
            GROUP BY stage
            ORDER BY n DESC
        """))).all()

        adopted_rows = (await session.execute(text("""
            SELECT quarter, COUNT(*) AS n
            FROM v_policy_actions
            WHERE instrument = 'rule' AND stage = 'adopted'
              AND action_date <= date('now')
            GROUP BY quarter
        """))).all()

    pipeline = [
        {"stage": stage.replace("_", " "), "count": n}
        for stage, n in stage_rows
    ]
    adopted_by_q = {q: n for q, n in adopted_rows if q in q_set}
    adopted_data = [adopted_by_q.get(q, 0) for q in quarters]

    return {
        "has_data": True,
        "pipeline": pipeline,
        "quarters": quarters,
        "adopted_series": [{"name": "Rules adopted", "data": adopted_data}],
        "boards_contributing": boards_contributing,
    }


async def legislation_table(limit: int = 40, today: date | None = None) -> dict:
    """Bills boards discussed, from v_legislation.

    Returns has_data=False + empty rows when legislation_mentions is empty.
    Otherwise: one row per (bill, state) with how the board engaged and how
    many boards touched it, most-recently-seen first.
    """
    empty = {"has_data": False, "rows": [], "boards_contributing": 0}
    if not await _table_has_rows("legislation_mentions"):
        return empty

    async with db.async_session() as session:
        boards_contributing = (await session.execute(text(
            "SELECT COUNT(DISTINCT board_code) FROM v_legislation"
        ))).scalar() or 0
        rows = (await session.execute(text("""
            SELECT vl.bill_number,
                   vl.bill_state,
                   MAX(vl.subject) AS subject,
                   GROUP_CONCAT(DISTINCT vl.involvement) AS involvements,
                   COUNT(DISTINCT vl.board_code) AS boards,
                   MAX(vl.meeting_date) AS last_seen,
                   MAX(vl.topic) AS topic,
                   -- meeting_id of this bill's most-recent mention, so the row
                   -- links straight to a source meeting (drill-through).
                   (SELECT vl2.meeting_id FROM v_legislation vl2
                    WHERE vl2.bill_number = vl.bill_number
                      AND vl2.bill_state = vl.bill_state
                    ORDER BY vl2.meeting_date DESC LIMIT 1) AS meeting_id
            FROM v_legislation vl
            WHERE vl.meeting_date <= date('now')
            GROUP BY vl.bill_number, vl.bill_state
            ORDER BY last_seen DESC
            LIMIT :limit
        """), {"limit": limit})).all()

    table_rows = []
    for r in rows:
        last_seen = r.last_seen
        if isinstance(last_seen, str):
            try:
                last_seen = date.fromisoformat(last_seen)
            except ValueError:
                last_seen = None
        table_rows.append({
            "bill_number": r.bill_number,
            "bill_state": r.bill_state,
            "subject": r.subject,
            "involvements": (r.involvements or "").replace(",", ", "),
            "boards": r.boards,
            "last_seen": last_seen,
            "topic": (r.topic or "").replace("-", " "),
            "meeting_id": r.meeting_id,
        })
    return {"has_data": True, "rows": table_rows,
            "boards_contributing": boards_contributing}


async def emerging_national(limit: int = 6) -> dict:
    """Latest emerging topics nationally, from EmergingTopic (via a direct
    query so we get the board + quote for the feed).

    Returns has_data=False + empty items when emerging_topics is empty.
    """
    empty = {"has_data": False, "items": []}
    if not await _table_has_rows("emerging_topics"):
        return empty

    async with db.async_session() as session:
        rows = (await session.execute(text("""
            SELECT et.topic_slug,
                   et.subject,
                   et.first_mentioned_on,
                   et.quote,
                   b.code AS board_code,
                   b.state AS board_state
            FROM emerging_topics et
            JOIN boards b ON b.id = et.board_id
            ORDER BY et.first_mentioned_on DESC
            LIMIT :limit
        """), {"limit": limit})).all()

    items = []
    for r in rows:
        first = r.first_mentioned_on
        if isinstance(first, str):
            try:
                first = date.fromisoformat(first)
            except ValueError:
                first = None
        items.append({
            "topic": (r.topic_slug or "").replace("-", " "),
            "subject": r.subject,
            "first_mentioned_on": first,
            "quote": r.quote,
            "board_code": r.board_code,
            "board_state": r.board_state,
        })
    return {"has_data": True, "items": items}


# ---------------------------------------------------------------------------
# Board activity — quarterly meeting counts for the board-page sparkline.
# Driven by meetings, live NOW.
# ---------------------------------------------------------------------------

async def board_activity_sparkline(board_id: int, quarters: int = 8,
                                   today: date | None = None) -> list[int]:
    """Meeting counts per quarter for one board over the last ``quarters``
    quarters (oldest -> newest). ~24 months at the default of 8."""
    qs = last_n_quarters(quarters, today)
    q_set = set(qs)
    q_expr = _quarter_expr("meeting_date")

    async with db.async_session() as session:
        rows = (await session.execute(text(f"""
            SELECT {q_expr} AS quarter, COUNT(*) AS n
            FROM meetings
            WHERE board_id = :bid
              AND meeting_date <= date('now')
            GROUP BY quarter
        """), {"bid": board_id})).all()

    by_q = {quarter: n for quarter, n in rows if quarter in q_set}
    return [by_q.get(q, 0) for q in qs]


async def board_topic_breakdown(board_id: int, months: int = 24,
                                today: date | None = None) -> list[dict]:
    """What this board discussed — meeting counts per topic over the trailing
    ``months`` months, ranked most-discussed first. Returns
    [{topic, count, pct}] where pct is relative to the top topic (for bar
    widths). Reads meetings.topics via json_each, so it reflects summarized
    meetings only (fills in as summaries land)."""
    today = today or date.today()
    # trailing window start, month arithmetic without dateutil
    y, m = today.year, today.month - months
    while m <= 0:
        m += 12
        y -= 1
    start = f"{y:04d}-{m:02d}-01"

    async with db.async_session() as session:
        rows = (await session.execute(text("""
            SELECT je.value AS topic, COUNT(DISTINCT m.id) AS n
            FROM meetings m, json_each(m.topics) je
            WHERE m.board_id = :bid
              AND m.topics IS NOT NULL
              AND m.meeting_date >= :start
              AND m.meeting_date <= date('now')
            GROUP BY je.value
            ORDER BY n DESC
        """), {"bid": board_id, "start": start})).all()

    if not rows:
        return []
    top = rows[0][1]
    return [{"topic": t, "count": n, "pct": round(100 * n / top)}
            for t, n in rows]


# ---------------------------------------------------------------------------
# Watchlist — standing full-text queries with new-hit counts.
# ---------------------------------------------------------------------------

# Seeds inserted the first time the watchlist is empty.
WATCHLIST_SEEDS = [
    ("AI", "AI"),
    ("telehealth", "Telehealth"),
    ("licensure compact", "Licensure Compact"),
    ("scope of practice", "Scope of Practice"),
]


async def seed_watchlist_if_empty() -> None:
    """Insert the four default watch terms if the table has no rows."""
    from datetime import datetime, timezone
    from app.models import WatchlistTerm
    from sqlalchemy import select, func

    async with db.async_session() as session:
        count = (await session.execute(
            select(func.count(WatchlistTerm.id))
        )).scalar()
        if count:
            return
        now = datetime.now(timezone.utc)
        for term, label in WATCHLIST_SEEDS:
            session.add(WatchlistTerm(term=term, label=label, created_at=now))
        await session.commit()


async def watchlist_with_counts(fts_sanitizer) -> list[dict]:
    """Return every watch term with its NEW-hit count.

    A "new hit" is a document that (a) matches the term in the FTS index and
    (b) was scraped after the term was last acknowledged. If the term has
    never been acknowledged, every current match counts as new.

    ``fts_sanitizer`` is server.py's ``_sanitize_fts_query`` — passed in so
    trends.py doesn't import from the web server (avoids a cycle).
    """
    from app.models import WatchlistTerm
    from sqlalchemy import select

    async with db.async_session() as session:
        terms = (await session.execute(
            select(WatchlistTerm).order_by(WatchlistTerm.created_at.asc())
        )).scalars().all()

    results: list[dict] = []
    for t in terms:
        fts_query = fts_sanitizer(t.term)
        new_count = 0
        if fts_query:
            async with db.async_session() as session:
                try:
                    if t.acknowledged_at is not None:
                        row = (await session.execute(text("""
                            SELECT COUNT(*)
                            FROM doc_fts
                            JOIN meeting_documents d ON d.id = doc_fts.rowid
                            WHERE doc_fts MATCH :q
                              AND d.scraped_at > :ack
                        """), {"q": fts_query, "ack": t.acknowledged_at})).scalar()
                    else:
                        row = (await session.execute(text("""
                            SELECT COUNT(*)
                            FROM doc_fts
                            JOIN meeting_documents d ON d.id = doc_fts.rowid
                            WHERE doc_fts MATCH :q
                        """), {"q": fts_query})).scalar()
                    new_count = row or 0
                except Exception:
                    # Malformed FTS edge case — never break the homepage.
                    new_count = 0
        results.append({
            "id": t.id,
            "term": t.term,
            "label": t.label,
            "new_count": new_count,
            "acknowledged_at": t.acknowledged_at,
        })
    return results
