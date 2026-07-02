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
    "meetings": {"summarized_at": "DATETIME"},
}

# Indexes for the hot query paths (models declare index=True for fresh DBs;
# these bring existing DBs up to parity).
_SCHEMA_INDEXES = [
    ("ix_meetings_board_id", "meetings", "board_id"),
    ("ix_meetings_meeting_date", "meetings", "meeting_date"),
    ("ix_meeting_documents_meeting_id", "meeting_documents", "meeting_id"),
]


async def init_db(url: str | None = None):
    """Create engine, session factory, and all tables.

    Args:
        url: Override database URL. If None, uses module-level DATABASE_URL.
    """
    global engine, async_session
    db_url = url or DATABASE_URL
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
