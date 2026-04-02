"""Render PDF document pages as full-res + thumbnail PNG images."""
from datetime import datetime, timezone
from pathlib import Path

import fitz
from sqlalchemy import select, func

import app.database as db
from app.models import MeetingDocument, DocumentPage, Meeting, Board
from app.config import PAGES_DIR

THUMB_WIDTH = 200


async def render_document_pages(
    document_id: int,
    pages_dir: Path | None = None,
) -> dict:
    """Render all pages of a PDF as full-res (150 DPI) + thumbnail (~200px) PNGs."""
    if db.engine is None:
        await db.init_db()
    output_dir = pages_dir or PAGES_DIR

    async with db.async_session() as session:
        existing = (await session.execute(
            select(func.count(DocumentPage.id))
            .where(DocumentPage.document_id == document_id)
        )).scalar() or 0

        if existing > 0:
            return {"document_id": document_id, "pages_rendered": 0, "skipped": True}

        doc = await session.get(MeetingDocument, document_id)
        if not doc:
            return {"document_id": document_id, "pages_rendered": 0, "error": "not found"}

        meeting = await session.get(Meeting, doc.meeting_id)
        board = await session.get(Board, meeting.board_id)
        board_code = board.code

    file_path = Path(doc.file_path)
    if not file_path.exists():
        return {"document_id": document_id, "pages_rendered": 0, "error": "file not found"}

    if file_path.suffix.lower() != ".pdf":
        return {"document_id": document_id, "pages_rendered": 0, "error": "not a PDF"}

    doc_dir = output_dir / board_code / str(document_id)
    doc_dir.mkdir(parents=True, exist_ok=True)

    try:
        pdf = fitz.open(str(file_path))
    except Exception as e:
        return {"document_id": document_id, "pages_rendered": 0, "error": str(e)}

    now = datetime.now(timezone.utc)
    pages_rendered = 0

    for page_idx in range(len(pdf)):
        page_num = page_idx + 1
        page = pdf[page_idx]

        full_path = doc_dir / f"page_{page_num:03d}.png"
        pix = page.get_pixmap(dpi=150)
        pix.save(str(full_path))

        scale = THUMB_WIDTH / page.rect.width
        thumb_matrix = fitz.Matrix(scale, scale)
        thumb_pix = page.get_pixmap(matrix=thumb_matrix)
        thumb_path = doc_dir / f"page_{page_num:03d}_thumb.png"
        thumb_pix.save(str(thumb_path))

        async with db.async_session() as session:
            dp = DocumentPage(
                document_id=document_id,
                page_number=page_num,
                image_path=str(full_path),
                thumb_path=str(thumb_path),
                rendered_at=now,
            )
            session.add(dp)
            await session.commit()

        pages_rendered += 1

    pdf.close()
    return {"document_id": document_id, "pages_rendered": pages_rendered, "skipped": False}


async def render_all_new_pages(pages_dir: Path | None = None) -> dict:
    """Render pages for all PDF documents without existing DocumentPage rows."""
    if db.engine is None:
        await db.init_db()

    async with db.async_session() as session:
        all_docs = (await session.execute(
            select(MeetingDocument.id, MeetingDocument.filename)
        )).all()

    pdf_docs = [(did, fn) for did, fn in all_docs if fn.lower().endswith(".pdf")]

    docs_to_render = []
    for did, fn in pdf_docs:
        async with db.async_session() as session:
            count = (await session.execute(
                select(func.count(DocumentPage.id))
                .where(DocumentPage.document_id == did)
            )).scalar() or 0
            if count == 0:
                docs_to_render.append((did, fn))

    if not docs_to_render:
        print("  No new documents to render.")
        return {"total": 0, "rendered": 0, "failed": 0}

    print(f"  Rendering pages for {len(docs_to_render)} documents...")
    total_pages = 0
    failed = 0

    for did, fn in docs_to_render:
        result = await render_document_pages(did, pages_dir=pages_dir)
        if result.get("error"):
            failed += 1
        else:
            total_pages += result["pages_rendered"]

    print(f"  Done: {total_pages} pages rendered, {failed} documents failed")
    return {"total": len(docs_to_render), "rendered": total_pages, "failed": failed}
