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
