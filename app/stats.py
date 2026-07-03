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
