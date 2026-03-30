"""Async database session factory."""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.models import Base

# Default from config; can be overridden before calling init_db() (e.g., in tests)
from app.config import DATABASE_URL as _DEFAULT_URL
DATABASE_URL = _DEFAULT_URL

engine = None
async_session = None


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
