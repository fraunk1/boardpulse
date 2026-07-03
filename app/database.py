"""Async database session factory."""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.models import Base

# Default from config; can be overridden before calling init_db() (e.g., in tests)
from app.config import DATABASE_URL as _DEFAULT_URL
DATABASE_URL = _DEFAULT_URL

engine = None
async_session = None


# Columns added after the original schema shipped. create_all() only creates
# missing TABLES — it never alters existing ones — so pre-existing databases
# are upgraded here with idempotent, metadata-only ALTERs (instant on SQLite).
_SCHEMA_ADDITIONS: dict[str, dict[str, str]] = {
    "boards": {"summary": "TEXT", "summarized_at": "DATETIME"},
    "meetings": {"summarized_at": "DATETIME", "facts_extracted_at": "DATETIME"},
}

# Indexes for the hot query paths (models declare index=True for fresh DBs;
# these bring existing DBs up to parity).
_SCHEMA_INDEXES = [
    ("ix_meetings_board_id", "meetings", "board_id"),
    ("ix_meetings_meeting_date", "meetings", "meeting_date"),
    ("ix_meeting_documents_meeting_id", "meeting_documents", "meeting_id"),
    ("ix_policy_actions_topic_date", "policy_actions", "topic, action_date"),
    ("ix_policy_actions_stage", "policy_actions", "stage"),
    ("ix_legislation_bill", "legislation_mentions", "bill_state, bill_number"),
    ("ix_disciplinary_category", "disciplinary_actions", "category"),
]

# Reporting views, recreated on every startup so their definitions are always
# current (DROP + CREATE is idempotent; SQLite views are just stored SQL).
_QUARTER_EXPR = (
    "strftime('%Y', {col}) || '-Q' || "
    "((CAST(strftime('%m', {col}) AS INTEGER) + 2) / 3)"
)

_SCHEMA_VIEWS: dict[str, str] = {
    "v_policy_actions": f"""
        SELECT pa.*, b.code AS board_code, b.state, m.meeting_date,
               strftime('%Y', pa.action_date) AS yr,
               {_QUARTER_EXPR.format(col='pa.action_date')} AS quarter
        FROM policy_actions pa
        JOIN meetings m ON m.id = pa.meeting_id
        JOIN boards b ON b.id = m.board_id
    """,
    "v_legislation": f"""
        SELECT l.*, b.code AS board_code, b.state, m.meeting_date,
               {_QUARTER_EXPR.format(col='m.meeting_date')} AS quarter
        FROM legislation_mentions l
        JOIN meetings m ON m.id = l.meeting_id
        JOIN boards b ON b.id = m.board_id
    """,
    "v_disciplinary": f"""
        SELECT da.*, b.code AS board_code, b.state, m.meeting_date,
               {_QUARTER_EXPR.format(col='m.meeting_date')} AS quarter
        FROM disciplinary_actions da
        JOIN meetings m ON m.id = da.meeting_id
        JOIN boards b ON b.id = m.board_id
    """,
    "v_emerging_national": """
        SELECT et.topic_slug,
               MIN(et.first_mentioned_on) AS first_seen_nationally,
               COUNT(*) AS boards_mentioning
        FROM emerging_topics et
        GROUP BY et.topic_slug
    """,
    "v_board_deltas": """
        SELECT bs.run_id, rr.started_at, b.code AS board_code,
               bs.mtgs, bs.docs, bs.docs_text,
               bs.mtgs_summarized, bs.mtgs_facts,
               bs.docs - LAG(bs.docs) OVER w AS docs_added,
               bs.mtgs - LAG(bs.mtgs) OVER w AS mtgs_added,
               bs.mtgs_facts - LAG(bs.mtgs_facts) OVER w AS facts_added
        FROM board_snapshots bs
        JOIN refresh_runs rr ON rr.id = bs.run_id
        JOIN boards b ON b.id = bs.board_id
        WINDOW w AS (PARTITION BY bs.board_id ORDER BY bs.run_id)
    """,
}


async def init_db(url: str | None = None):
    """Create engine, session factory, and all tables.

    Args:
        url: Override database URL. If None, uses module-level DATABASE_URL.
    """
    global engine, async_session
    db_url = url or DATABASE_URL
    if engine is not None:
        # Dispose the previous engine's pooled connections before replacing
        # it — otherwise re-init (tests, refresh snapshots) leaks aiosqlite
        # connections bound to a dead event loop ("Event loop is closed"
        # errors at interpreter shutdown; fails CI on Linux).
        await engine.dispose()
    engine = create_async_engine(db_url, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        # ensure_schema: upgrade pre-existing tables in place
        for table, cols in _SCHEMA_ADDITIONS.items():
            rows = await conn.exec_driver_sql(f"PRAGMA table_info({table})")
            existing = {r[1] for r in rows.fetchall()}
            for col, ddl in cols.items():
                if col not in existing:
                    await conn.exec_driver_sql(
                        f"ALTER TABLE {table} ADD COLUMN {col} {ddl}")

        for name, table, column in _SCHEMA_INDEXES:
            await conn.exec_driver_sql(
                f"CREATE INDEX IF NOT EXISTS {name} ON {table} ({column})")

        for view_name, view_sql in _SCHEMA_VIEWS.items():
            await conn.exec_driver_sql(f"DROP VIEW IF EXISTS {view_name}")
            await conn.exec_driver_sql(
                f"CREATE VIEW {view_name} AS {view_sql}")

        # Full-text search over meeting document text (FTS5, external-content
        # table so the indexed text isn't duplicated on disk). First startup
        # against a pre-existing DB backfills the index once; after that,
        # refresh.py keeps it current with a 'rebuild' after each extract pass.
        await conn.exec_driver_sql(
            "CREATE VIRTUAL TABLE IF NOT EXISTS doc_fts USING fts5("
            "content_text, content='meeting_documents', content_rowid='id')")

        fts_count = (await conn.exec_driver_sql(
            "SELECT count(*) FROM doc_fts")).scalar()
        if not fts_count:
            has_text = (await conn.exec_driver_sql(
                "SELECT 1 FROM meeting_documents "
                "WHERE content_text IS NOT NULL AND content_text != '' LIMIT 1"
            )).first()
            if has_text:
                await conn.exec_driver_sql(
                    "INSERT INTO doc_fts(doc_fts) VALUES('rebuild')")
