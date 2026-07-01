"""Tests for collector download validation, filename derivation, and URL handling."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.scraper.collector import (  # noqa: E402
    validate_document_bytes,
    _doc_filename,
    _infer_doc_type,
)


# ---------------------------------------------------------------------------
# validate_document_bytes
# ---------------------------------------------------------------------------

# The literal Montana DLI portal stub that poisoned 53 downloads (95 bytes).
MT_STUB = (
    b"Unable to retrieve document. Please try downloading the document "
    b"from the board meetings page."
)


def _pdf_bytes(size: int = 2048) -> bytes:
    return b"%PDF-1.7\n" + b"0" * size


def test_validate_pdf_magic_accepts():
    valid, reason = validate_document_bytes(_pdf_bytes(), ".pdf")
    assert valid, reason


def test_validate_docx_pk_accepts():
    data = b"PK\x03\x04" + b"0" * 2048
    valid, _ = validate_document_bytes(data, ".docx")
    assert valid


def test_validate_ole_doc_accepts():
    data = b"\xd0\xcf\x11\xe0" + b"0" * 2048
    valid, _ = validate_document_bytes(data, ".doc")
    assert valid


def test_validate_rejects_mt_stub():
    valid, reason = validate_document_bytes(MT_STUB, ".pdf")
    assert not valid
    assert "small" in reason


def test_validate_rejects_html_disguised_as_pdf():
    data = b"<!DOCTYPE html><html><body>Access denied</body></html>" + b" " * 2048
    valid, reason = validate_document_bytes(data, ".pdf")
    assert not valid
    assert reason == "html body"


def test_validate_rejects_leading_whitespace_html():
    data = b"\n\r\t  <html><body>error</body></html>" + b" " * 2048
    valid, reason = validate_document_bytes(data, ".pdf")
    assert not valid
    assert reason == "html body"


def test_validate_rejects_tiny_file():
    valid, reason = validate_document_bytes(b"%PDF-1.7", ".pdf")
    assert not valid
    assert "small" in reason


def test_validate_rejects_wrong_signature_pdf():
    data = b"MZ" + b"0" * 2048  # not a PDF
    valid, reason = validate_document_bytes(data, ".pdf")
    assert not valid
    assert "signature" in reason


def test_validate_pdf_with_prefix_junk_accepts():
    data = b"\xef\xbb\xbfjunk%PDF-1.4\n" + b"0" * 2048
    valid, _ = validate_document_bytes(data, ".pdf")
    assert valid


def test_validate_unknown_extension_accepts_non_html():
    data = b"\x00\x01binarystuff" + b"0" * 2048
    valid, _ = validate_document_bytes(data, ".bin")
    assert valid


def test_validate_empty_rejects():
    valid, reason = validate_document_bytes(b"", ".pdf")
    assert not valid


# ---------------------------------------------------------------------------
# _doc_filename
# ---------------------------------------------------------------------------

def test_doc_filename_extension_passthrough():
    assert _doc_filename("https://x.gov/files/minutes.pdf?rev=abc") == "minutes.pdf"


def test_doc_filename_filetype_query_param():
    url = "https://boardmeetings.dli.mt.gov/boardmeetings/document?board=MED&filekey=321ZB68&filetype=pdf"
    assert _doc_filename(url) == "321ZB68.pdf"


def test_doc_filename_plain_path_no_extension():
    # No filetype hint: falls back to the path segment name
    assert _doc_filename("https://x.gov/documents/board-page") == "board-page"


# ---------------------------------------------------------------------------
# _infer_doc_type
# ---------------------------------------------------------------------------

def test_infer_doc_type():
    assert _infer_doc_type("2026-01-01_agenda.pdf") == "agenda"
    assert _infer_doc_type("meeting_notice.pdf") == "notice"
    assert _infer_doc_type("exhibit_a.pdf") == "attachment"
    assert _infer_doc_type("january_minutes.pdf") == "minutes"
