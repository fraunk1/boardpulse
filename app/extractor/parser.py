"""Extract text from collected documents (PDF, DOCX, HTML)."""
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup


def _markitdown_cmd() -> str:
    """Prefer the markitdown that lives next to this interpreter (venv
    Scripts) so extraction works even when the venv isn't on PATH — a bare
    "markitdown" silently fails every document in that case."""
    exe = Path(sys.executable).parent / (
        "markitdown.exe" if sys.platform == "win32" else "markitdown")
    return str(exe) if exe.exists() else "markitdown"


MARKITDOWN = _markitdown_cmd()


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
            [MARKITDOWN, str(file_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
        if result.returncode == 0 and (result.stdout or "").strip():
            return result.stdout.strip()
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None
