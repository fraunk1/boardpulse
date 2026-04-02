"""FTS5 full-text search index for meeting summaries."""
from sqlalchemy import select, text

import app.database as db
from app.models import Meeting


async def rebuild_fts_index() -> dict:
    """Create/rebuild the FTS5 virtual table from Meeting.summary data."""
    async with db.async_session() as session:
        conn = await session.connection()

        await conn.execute(text("DROP TABLE IF EXISTS meeting_summaries_fts"))

        await conn.execute(text(
            "CREATE VIRTUAL TABLE meeting_summaries_fts USING fts5("
            "  meeting_id UNINDEXED, summary"
            ")"
        ))

        meetings = (await session.execute(
            select(Meeting.id, Meeting.summary)
            .where(Meeting.summary.isnot(None))
        )).all()

        indexed = 0
        for meeting_id, summary in meetings:
            await conn.execute(
                text("INSERT INTO meeting_summaries_fts(meeting_id, summary) VALUES (:mid, :summary)"),
                {"mid": meeting_id, "summary": summary},
            )
            indexed += 1

        await conn.commit()

    print(f"  FTS index rebuilt: {indexed} meetings indexed")
    return {"indexed": indexed}


async def search_summaries(query: str, limit: int = 50) -> list[dict]:
    """Search meeting summaries using FTS5. Returns list of dicts with meeting_id and snippet."""
    async with db.async_session() as session:
        conn = await session.connection()

        try:
            rows = (await conn.execute(
                text(
                    "SELECT meeting_id, snippet(meeting_summaries_fts, 1, '<mark>', '</mark>', '...', 40) as snippet "
                    "FROM meeting_summaries_fts "
                    "WHERE summary MATCH :query "
                    "ORDER BY rank "
                    "LIMIT :limit"
                ),
                {"query": query, "limit": limit},
            )).all()
        except Exception:
            return []

    return [{"meeting_id": row[0], "snippet": row[1]} for row in rows]
