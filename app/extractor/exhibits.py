"""Exhibit generator — renders full PDF documents with page captions.

For each cited meeting, renders every page of the source minutes PDF
as an image, extracts a caption for each page, and marks the most
relevant page for the claim.
"""
import logging
import re
from pathlib import Path

import fitz  # PyMuPDF

from app.config import DOCUMENTS_DIR, EXHIBITS_DIR

logger = logging.getLogger(__name__)

HIGHLIGHT_COLOR = fitz.utils.getColor("yellow")


def _find_document(board_code: str, meeting_date: str) -> Path | None:
    """Find the PDF document for a board + meeting date."""
    doc_dir = DOCUMENTS_DIR / board_code
    if not doc_dir.exists():
        return None

    # Try exact date prefix first
    for pdf in sorted(doc_dir.glob(f"{meeting_date}*.pdf")):
        return pdf

    # Try underscore date
    date_underscore = meeting_date.replace("-", "_")
    for pdf in sorted(doc_dir.glob(f"*{date_underscore}*.pdf")):
        return pdf

    # Try year-month prefix
    for pdf in sorted(doc_dir.glob(f"{meeting_date[:7]}*.pdf")):
        return pdf

    return None


def _caption_for_page(page: fitz.Page) -> str:
    """Generate a brief caption summarizing a PDF page's content.

    Extracts headings, bold text, and first substantive line.
    """
    text = page.get_text("text").strip()
    if not text:
        return "No text content on this page."

    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if not lines:
        return "No text content on this page."

    # Look for heading-like lines (short, possibly uppercase or bold)
    headings = []
    topics = []
    for line in lines[:30]:
        # Skip very short lines (page numbers, dates alone)
        if len(line) < 5:
            continue
        # Headings tend to be short and may be uppercase
        if len(line) < 80 and (line.isupper() or line.istitle()):
            headings.append(line)
        # Look for agenda items, numbered items, topic indicators
        if re.match(r'^(I{1,3}V?|V?I{0,3}|[A-Z]|[0-9]+)[.)]\s+', line):
            topics.append(line)

    # Build caption from what we found
    parts = []
    if headings:
        parts.append(headings[0])
        if len(headings) > 1:
            parts.append(headings[1])
    elif topics:
        parts.append(topics[0])
        if len(topics) > 1:
            parts.append(topics[1])
    else:
        # Fall back to first substantive line
        for line in lines:
            if len(line) > 20:
                parts.append(line[:120])
                break

    caption = " — ".join(parts) if parts else lines[0][:120]
    return caption[:200]


def _find_best_page(doc: fitz.Document, claim_text: str) -> int:
    """Find the page index most relevant to the claim text."""
    # Extract significant words from the claim
    clean = re.sub(r'\[.*?\]\(.*?\)', '', claim_text)
    clean = re.sub(r'[*_`#"\']', '', clean)
    words = [w for w in clean.split() if len(w) >= 5]

    # Skip common filler words
    skip = {'board', 'meeting', 'state', 'medical', 'discussed', 'approved',
            'motion', 'action', 'noted', 'reported', 'members', 'present',
            'committee', 'which', 'their', 'about', 'would', 'could', 'should'}
    words = [w for w in words if w.lower() not in skip][:8]

    best_page = 0
    best_score = 0

    for idx in range(len(doc)):
        page_text = doc[idx].get_text("text").lower()
        score = sum(1 for w in words if w.lower() in page_text)
        if score > best_score:
            best_score = score
            best_page = idx

    return best_page


def render_full_document(
    board_code: str,
    meeting_date: str,
    claim_text: str,
    exhibit_number: int,
    dpi: int = 150,
) -> dict | None:
    """Render all pages of a minutes PDF with captions.

    Returns dict with:
        exhibit_number, board_code, meeting_date, claim_text,
        pages: [{page_num, image_path, caption, is_highlight}]
    """
    pdf_path = _find_document(board_code, meeting_date)
    if not pdf_path:
        logger.warning(f"No PDF found for {board_code} {meeting_date}")
        return None

    doc = fitz.open(str(pdf_path))
    best_page = _find_best_page(doc, claim_text)

    exhibit_dir = EXHIBITS_DIR / board_code / f"exhibit_{exhibit_number:03d}"
    exhibit_dir.mkdir(parents=True, exist_ok=True)

    pages = []
    for idx in range(len(doc)):
        page = doc[idx]
        is_highlight = (idx == best_page)

        # Add yellow highlights on the best-match page
        if is_highlight:
            clean = re.sub(r'\[.*?\]\(.*?\)', '', claim_text)
            clean = re.sub(r'[*_`#"\']', '', clean)
            words = [w for w in clean.split() if len(w) >= 5]
            skip = {'board', 'meeting', 'state', 'medical', 'discussed',
                    'approved', 'motion', 'their', 'about', 'which', 'would'}
            words = [w for w in words if w.lower() not in skip][:6]
            for word in words:
                rects = page.search_for(word)
                for rect in rects[:5]:
                    hl = page.add_highlight_annot(rect)
                    hl.set_colors(stroke=HIGHLIGHT_COLOR)
                    hl.update()

        # Render
        pix = page.get_pixmap(dpi=dpi)
        img_path = exhibit_dir / f"page_{idx + 1:03d}.png"
        pix.save(str(img_path))

        # Caption
        caption = _caption_for_page(page)

        pages.append({
            "page_num": idx + 1,
            "image_path": img_path,
            "caption": caption,
            "is_highlight": is_highlight,
        })

    doc.close()

    print(f"  Exhibit {exhibit_number:3d}: {board_code} {meeting_date} "
          f"— {len(pages)} pages (highlight: p{best_page + 1})")

    return {
        "exhibit_number": exhibit_number,
        "board_code": board_code,
        "meeting_date": meeting_date,
        "claim_text": claim_text,
        "pdf_name": pdf_path.name,
        "pages": pages,
    }


def parse_report_citations(report_path: Path) -> list[dict]:
    """Parse inline citations from a national landscape report."""
    text = report_path.read_text(encoding="utf-8")

    pattern = re.compile(
        r'([^.]*?)'
        r'\(\[.*?\]\(/board/(\w{2})/(\w+_\w+)'
        r'#(\d{4}-\d{2}-\d{2})\)\)',
        re.MULTILINE,
    )

    citations = []
    seen = set()

    for match in pattern.finditer(text):
        claim_text = match.group(1).strip().lstrip('- *')
        state = match.group(2)
        board_code = match.group(3)
        meeting_date = match.group(4)

        key = f"{board_code}_{meeting_date}"
        if key in seen:
            continue
        seen.add(key)

        citations.append({
            "board_code": board_code,
            "state": state,
            "meeting_date": meeting_date,
            "claim_text": claim_text,
            "exhibit_number": len(citations) + 1,
        })

    return citations


def generate_all_exhibits(report_path: Path) -> list[dict]:
    """Parse report and render full documents for all citations."""
    citations = parse_report_citations(report_path)
    print(f"Found {len(citations)} unique citations\n")

    results = []
    for cite in citations:
        result = render_full_document(
            board_code=cite["board_code"],
            meeting_date=cite["meeting_date"],
            claim_text=cite["claim_text"],
            exhibit_number=cite["exhibit_number"],
        )
        if result:
            results.append(result)
        else:
            print(f"  Exhibit {cite['exhibit_number']:3d}: "
                  f"{cite['board_code']} {cite['meeting_date']} — no PDF found, skipping")

    print(f"\nGenerated {len(results)}/{len(citations)} exhibits")
    return results
