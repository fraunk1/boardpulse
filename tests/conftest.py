"""Shared test fixtures for boardpulse."""
import json
import pytest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch

import httpx

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage, PipelineRun, PipelineEvent


@pytest.fixture(autouse=True)
async def db_session():
    """Initialize a fresh in-memory DB for each test."""
    await db.init_db(url="sqlite+aiosqlite://")
    yield


@pytest.fixture
async def client():
    """Async HTTP client for testing FastAPI routes.

    Patches the startup event so it doesn't re-init the DB
    (db_session already set up the in-memory DB).
    """
    from app.web.server import app

    # Remove the startup handler that would re-init to file DB
    app.router.on_startup.clear()

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        yield c

    # Restore startup handler for next test
    from app.web.server import startup
    app.router.on_startup.append(startup)


@pytest.fixture
async def seed_board():
    """Factory: create a Board record."""
    async def _create(code="TX_MD", state="TX", name="Texas Medical Board",
                      board_type="combined", homepage="https://tmb.state.tx.us"):
        async with db.async_session() as session:
            board = Board(
                state=state, code=code, name=name,
                board_type=board_type, homepage=homepage,
                discovery_status="found",
            )
            session.add(board)
            await session.commit()
            await session.refresh(board)
            return board
    return _create


@pytest.fixture
async def seed_full_chain(tmp_path, seed_board):
    """Factory: create Board -> Meeting -> Document -> Page with topics and images.

    Returns dict with all created objects and the tmp pages dir.
    """
    async def _create(
        code="TX_MD", state="TX", board_name="Texas Medical Board",
        meeting_date=None, summary="The board discussed telehealth and discipline.",
        topics=None, doc_type="minutes",
    ):
        if meeting_date is None:
            meeting_date = date(2026, 3, 15)
        if topics is None:
            topics = ["Discipline", "Telehealth"]

        board = await seed_board(code=code, state=state, name=board_name)

        async with db.async_session() as session:
            meeting = Meeting(
                board_id=board.id, meeting_date=meeting_date,
                title=f"{board_name} — {meeting_date.strftime('%B %Y')}",
                summary=summary, topics=topics,
            )
            session.add(meeting)
            await session.commit()
            await session.refresh(meeting)

            # Create a document with extracted text
            doc = MeetingDocument(
                meeting_id=meeting.id, doc_type=doc_type,
                filename=f"{meeting_date.isoformat()}_minutes.pdf",
                file_path=str(tmp_path / "documents" / code / f"{meeting_date.isoformat()}_minutes.pdf"),
                content_text=(
                    "The board convened to discuss disciplinary actions. "
                    "Three physicians were placed on probation for telehealth violations. "
                    "The committee reviewed licensing applications and rulemaking proposals."
                ),
                topics=topics,
            )
            session.add(doc)
            await session.commit()
            await session.refresh(doc)

            # Create page images (1x1 white PNG)
            pages_dir = tmp_path / "pages" / code / str(doc.id)
            pages_dir.mkdir(parents=True, exist_ok=True)

            _write_tiny_png(pages_dir / "page_001.png")
            _write_tiny_png(pages_dir / "page_001_thumb.png")

            page = DocumentPage(
                document_id=doc.id, page_number=1,
                image_path=str(pages_dir / "page_001.png"),
                thumb_path=str(pages_dir / "page_001_thumb.png"),
                topics=topics,
                tagged_at=datetime.now(timezone.utc),
                rendered_at=datetime.now(timezone.utc),
            )
            session.add(page)
            await session.commit()
            await session.refresh(page)

        return {
            "board": board, "meeting": meeting,
            "doc": doc, "page": page,
            "pages_dir": tmp_path / "pages",
        }
    return _create


@pytest.fixture
async def seed_pipeline_run():
    """Factory: create a PipelineRun with events."""
    async def _create(status="completed", trigger="manual"):
        async with db.async_session() as session:
            run = PipelineRun(
                started_at=datetime.now(timezone.utc),
                completed_at=datetime.now(timezone.utc) if status == "completed" else None,
                status=status, trigger=trigger,
                boards_collected=5, new_meetings_found=10,
                new_documents_found=15, boards_summarized=3,
            )
            session.add(run)
            await session.commit()
            await session.refresh(run)

            event = PipelineEvent(
                run_id=run.id, timestamp=datetime.now(timezone.utc),
                stage="collect", event_type="completed",
                board_code="TX_MD", detail="10 new meetings",
            )
            session.add(event)
            await session.commit()
            return run
    return _create


def _write_tiny_png(path: Path):
    """Write a minimal valid 1x1 white PNG file."""
    import struct, zlib
    path.parent.mkdir(parents=True, exist_ok=True)
    # Minimal PNG: 8-byte sig + IHDR + IDAT + IEND
    sig = b'\x89PNG\r\n\x1a\n'
    def chunk(ctype, data):
        c = ctype + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    ihdr = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
    raw = zlib.compress(b'\x00\xff\xff\xff')
    png = sig + chunk(b'IHDR', ihdr) + chunk(b'IDAT', raw) + chunk(b'IEND', b'')
    path.write_bytes(png)
