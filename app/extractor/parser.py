"""Extract text from collected documents (PDF, DOCX, HTML)."""
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup


def extract_text_from_html(html: str) -> str:
    """Extract readable text from HTML, stripping nav/script/style."""
    if not html or not html.strip():
        return ""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def _ocr_pdf(doc) -> str:
    """OCR a scanned PDF using Tesseract via pytesseract."""
    try:
        import io
        from PIL import Image
        import pytesseract
    except ImportError:
        return ""

    pages_text = []
    for page_idx in range(min(len(doc), 50)):  # cap at 50 pages
        page = doc[page_idx]
        pix = page.get_pixmap(dpi=200)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img)
        if text.strip():
            pages_text.append(text.strip())

    return "\n\n".join(pages_text)


def extract_text_from_file(file_path: Path) -> str | None:
    """Extract text from a file using markitdown.

    Uses the ``markitdown`` CLI tool to convert PDF, DOCX, XLSX, etc. to Markdown.
    Falls back to reading raw text for .txt and .html files.
    """
    if not file_path.exists():
        return None

    suffix = file_path.suffix.lower()

    if suffix in (".html", ".htm"):
        return extract_text_from_html(file_path.read_text(errors="ignore"))

    if suffix == ".txt":
        return file_path.read_text(errors="ignore")

    # Try PyMuPDF first for PDFs (most reliable)
    if suffix == ".pdf":
        try:
            import fitz
            doc = fitz.open(str(file_path))
            text = "\n\n".join(page.get_text() for page in doc)
            # If no text extracted but pages have images, try OCR
            if not text.strip() and len(doc) > 0 and len(doc[0].get_images()) > 0:
                text = _ocr_pdf(doc)
            doc.close()
            if text.strip():
                return text.strip()
        except Exception:
            pass

    # Fallback to markitdown for other formats
    try:
        result = subprocess.run(
            ["markitdown", str(file_path)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None
