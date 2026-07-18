"""Shared aggregate queries for refresh reporting and the /ops status page.

Single source of truth for the per-board snapshot SQL — refresh.py used to
own this (as SNAP_SQL); it now imports per_board_counts() from here so
there's exactly one definition of "what counts as coverage" for a board.
"""
from sqlalchemy import text

import app.database as db

# Same aggregate refresh.py has always used for its before/after diff:
# meetings, documents, and documents-with-extracted-text per board.
PER_BOARD_SQL = """
    SELECT b.code,
           COUNT(DISTINCT m.id) AS mtgs,
           COUNT(d.id) AS docs,
           SUM(CASE WHEN d.content_text IS NOT NULL AND d.content_text != ''
                    THEN 1 ELSE 0 END) AS docs_text,
           COUNT(DISTINCT CASE WHEN m.summary IS NOT NULL AND m.summary != ''
                               THEN m.id END) AS mtgs_summarized,
           COUNT(DISTINCT CASE WHEN m.facts_extracted_at IS NOT NULL
                               THEN m.id END) AS mtgs_facts
    FROM boards b
    LEFT JOIN meetings m ON m.board_id = b.id
    LEFT JOIN meeting_documents d ON d.meeting_id = m.id
    GROUP BY b.id
"""


async def per_board_counts() -> dict[str, dict]:
    """Return {board_code: {mtgs, docs, docs_text, mtgs_summarized,
    mtgs_facts}} for every board."""
    async with db.async_session() as session:
        rows = (await session.execute(text(PER_BOARD_SQL))).all()
    return {
        code: {
            "mtgs": mtgs, "docs": docs, "docs_text": docs_text or 0,
            "mtgs_summarized": summarized or 0, "mtgs_facts": facts or 0,
        }
        for code, mtgs, docs, docs_text, summarized, facts in rows
    }


async def extraction_failures() -> list[tuple[str, str]]:
    """Return [(board_code, filename), ...] for documents with no extracted text."""
    async with db.async_session() as session:
        rows = (await session.execute(text(
            "SELECT b.code, d.filename "
            "FROM meeting_documents d "
            "JOIN meetings m ON m.id = d.meeting_id "
            "JOIN boards b ON b.id = m.board_id "
            "WHERE d.content_text IS NULL OR d.content_text = '' "
            "ORDER BY b.code, d.filename"
        ))).all()
    return [(code, filename) for code, filename in rows]


async def status_rollup() -> dict[str, int]:
    """Return {discovery_status: count} across all boards."""
    async with db.async_session() as session:
        rows = (await session.execute(text(
            "SELECT discovery_status, COUNT(*) FROM boards "
            "GROUP BY discovery_status"
        ))).all()
    return {status: count for status, count in rows}


def sanitize_fts_query(q: str) -> str:
    """Turn free-typed user input into a safe FTS5 MATCH expression.

    Splits on whitespace and wraps each token in double quotes, joined by
    spaces. Quoting each token neutralizes FTS5 operators (AND/OR/NOT/NEAR,
    column filters, prefix `*`) and unbalanced quotes — every token becomes
    a literal phrase match, so the query can't raise a syntax error.

    Lives here (not in the web server) so the search page, the monthly brief,
    and the artifact exporter all share one definition.
    """
    tokens = q.split()
    if not tokens:
        return ""
    escaped = [tok.replace('"', '""') for tok in tokens]
    return " ".join(f'"{tok}"' for tok in escaped)


async def coverage_rollup() -> dict:
    """The /ops accounted math — one source of truth for 'board X counts as
    covered': it has extracted document text, or the ledger has verified it
    as none_published/blocked.

    Returns {"rows": [{board, mtgs, docs, docs_text, discovery_status,
    accounted}], "total_boards", "have_docs", "accounted"} with boards ordered
    by state, code.
    """
    from sqlalchemy import select
    from app.models import Board

    async with db.async_session() as session:
        boards = (await session.execute(
            select(Board).order_by(Board.state, Board.code)
        )).scalars().all()

    per_board = await per_board_counts()

    rows = []
    accounted = 0
    have_docs = 0
    for b in boards:
        counts = per_board.get(b.code, {"mtgs": 0, "docs": 0, "docs_text": 0})
        row_has_docs = counts["docs_text"] > 0
        if row_has_docs:
            have_docs += 1
        is_accounted = (b.discovery_status in ("none_published", "blocked")
                        or row_has_docs)
        if is_accounted:
            accounted += 1
        rows.append({
            "board": b,
            "mtgs": counts["mtgs"],
            "docs": counts["docs"],
            "docs_text": counts["docs_text"],
            "discovery_status": b.discovery_status,
            "accounted": is_accounted,
        })
    return {
        "rows": rows,
        "total_boards": len(boards),
        "have_docs": have_docs,
        "accounted": accounted,
    }
