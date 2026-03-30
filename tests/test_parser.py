"""Test text extraction from documents."""
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.extractor.parser import extract_text_from_file, extract_text_from_html


def test_extract_text_from_html():
    html = """
    <html><body>
    <h1>Board Meeting Minutes</h1>
    <p>The board met on January 15, 2026.</p>
    <nav>Navigation stuff</nav>
    <script>var x = 1;</script>
    <p>The following items were discussed:</p>
    </body></html>
    """
    text = extract_text_from_html(html)
    assert "Board Meeting Minutes" in text
    assert "January 15, 2026" in text
    assert "Navigation stuff" not in text
    assert "var x" not in text


def test_extract_text_from_html_empty():
    assert extract_text_from_html("") == ""
    assert extract_text_from_html("<html></html>") == ""


def test_extract_text_from_file_nonexistent():
    result = extract_text_from_file(Path("/nonexistent/file.pdf"))
    assert result is None


@patch("app.extractor.parser.subprocess.run")
@patch("pathlib.Path.exists", return_value=True)
def test_extract_text_from_pdf(mock_exists, mock_run):
    mock_run.return_value = MagicMock(
        returncode=0,
        stdout="# Meeting Minutes\n\nDiscussion about AI policy.",
    )
    result = extract_text_from_file(Path("/tmp/test.pdf"))
    assert result is not None
    assert "Meeting Minutes" in result
    mock_run.assert_called_once()
