"""Tests for collector download validation, filename derivation, and URL handling."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.scraper.collector import (  # noqa: E402
    validate_document_bytes,
    transform_download_url,
    _doc_filename,
    _infer_doc_type,
    _passes_filter,
    _should_visit_detail,
    _site_key,
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


def test_doc_filename_download_resource_asp():
    url = "https://www.ndbom.org/download_resource.asp?id=1234"
    assert _doc_filename(url) == "resource_1234.pdf"


def test_doc_filename_getfile_cfm_with_file_param():
    url = (r"https://townhall.virginia.gov/L/GetFile.cfm"
           r"?File=E:%5Ctownhall%5Cdocroot%5Cminutes%5C2024%5Cfeb_minutes.pdf")
    assert _doc_filename(url) == "feb_minutes.pdf"


def test_doc_filename_getfile_cfm_opaque_hashes_unique():
    a = _doc_filename("https://townhall.virginia.gov/L/GetFile.cfm?logid=1&fid=9")
    b = _doc_filename("https://townhall.virginia.gov/L/GetFile.cfm?logid=2&fid=7")
    assert a.endswith(".pdf") and b.endswith(".pdf")
    assert a != b  # distinct URLs must not collapse to one filename


def test_doc_filename_download_attachment_guid():
    url = "https://publicmeetings.wi.gov/download-attachment/285c4839-ab12-cd34"
    assert _doc_filename(url) == "285c4839-ab12-cd34.pdf"


def test_doc_filename_massgov_doc_download():
    url = "https://www.mass.gov/doc/borim-minutes-august-2024/download"
    assert _doc_filename(url) == "borim-minutes-august-2024.pdf"


def test_doc_filename_georgia_cms_document_download():
    url = ("https://medicalboard.georgia.gov/document/document/"
           "december-2024-minutes/download")
    assert _doc_filename(url) == "december-2024-minutes.pdf"


def test_doc_filename_drive_file():
    url = "https://drive.google.com/file/d/1YZknFrlLcjxzoEOeugO3ljZVaQbXlfio/view"
    assert _doc_filename(url) == "drive_1YZknFrlLcjxzoEOeugO3ljZVaQbXlfio.pdf"


# ---------------------------------------------------------------------------
# transform_download_url
# ---------------------------------------------------------------------------

def test_transform_drive_file_url():
    url = "https://drive.google.com/file/d/1AbC_dEf-123/view?usp=drive_link"
    assert transform_download_url(url) == (
        "https://drive.google.com/uc?export=download&id=1AbC_dEf-123"
    )


def test_transform_drive_open_url():
    url = "https://drive.google.com/open?id=1AbC_dEf-123"
    assert transform_download_url(url) == (
        "https://drive.google.com/uc?export=download&id=1AbC_dEf-123"
    )


def test_transform_docs_google_export():
    url = "https://docs.google.com/document/d/1XyZ/edit"
    assert transform_download_url(url) == (
        "https://docs.google.com/document/d/1XyZ/export?format=pdf"
    )


def test_transform_non_drive_url_unchanged():
    url = "https://www.ndbom.org/download_resource.asp?id=1234"
    assert transform_download_url(url) == url


# ---------------------------------------------------------------------------
# _passes_filter (strategy filter_text)
# ---------------------------------------------------------------------------

def test_filter_text_keeps_matching_rows():
    assert _passes_filter(
        "Iowa Board of Medicine — May 2, 2025 Minutes", "Board of Medicine"
    )


def test_filter_text_case_insensitive():
    assert _passes_filter("iowa BOARD OF MEDICINE minutes", "Board of Medicine")


def test_filter_text_drops_non_matching_rows():
    assert not _passes_filter(
        "Iowa Board of Nursing — May 2, 2025 Minutes", "Board of Medicine"
    )


def test_filter_text_none_keeps_all():
    assert _passes_filter("anything at all", None)


# ---------------------------------------------------------------------------
# Depth-1 guards
# ---------------------------------------------------------------------------

def test_site_key_strips_www_and_port():
    assert _site_key("https://www.tmb.texas.gov:443/x") == "texas.gov"
    assert _site_key("https://flboardofmedicine.gov/y") == "flboardofmedicine.gov"


def test_should_visit_detail_same_site():
    assert _should_visit_detail(
        "https://www.tmb.texas.gov/meetings/2024-june",
        "https://www.tmb.texas.gov/about-us/events", set(),
    )


def test_should_visit_detail_rejects_cross_site():
    assert not _should_visit_detail(
        "https://example.com/meeting",
        "https://www.tmb.texas.gov/about-us/events", set(),
    )


def test_should_visit_detail_rejects_junk_links():
    base = "https://www.tmb.texas.gov/events"
    assert not _should_visit_detail("https://www.zoomgov.com/j/123", base, set())
    assert not _should_visit_detail(
        "https://www.tmb.texas.gov/photo.jpg", base, set())


def test_should_visit_detail_rejects_visited():
    url = "https://www.tmb.texas.gov/meetings/2024-june"
    assert not _should_visit_detail(url, "https://www.tmb.texas.gov/", {url})


# ---------------------------------------------------------------------------
# URL-probe candidate generation
# ---------------------------------------------------------------------------

def test_url_probe_candidates_nj_pattern():
    from datetime import date
    from app.scraper.url_probe import candidate_urls
    out = candidate_urls(
        ("https://www.njconsumeraffairs.gov/bme/Agendas/bme-agenda-%m%d%y.pdf",),
        [date(2025, 1, 8), date(2024, 12, 4)],
    )
    urls = [u for _, u in out]
    assert urls[0].endswith("bme-agenda-010825.pdf")  # newest first
    assert urls[1].endswith("bme-agenda-120424.pdf")


def test_url_probe_candidates_mo_pattern_dedupes():
    from datetime import date
    from app.scraper.url_probe import candidate_urls
    out = candidate_urls(
        ("https://pr.mo.gov/boards/healingarts/meetings/%Y-%m-%d-Minutes.pdf",),
        [date(2025, 6, 2), date(2025, 6, 2)],  # duplicate date
    )
    assert len(out) == 1
    assert out[0][1].endswith("2025-06-02-Minutes.pdf")


def test_url_probe_daily_grid_bounded():
    from app.scraper.url_probe import daily_grid, WINDOW_DAYS
    grid = daily_grid()
    assert len(grid) == WINDOW_DAYS
    assert grid[0] > grid[-1]  # newest first


# ---------------------------------------------------------------------------
# Date parsing additions
# ---------------------------------------------------------------------------

def test_parse_date_mmddyyyy_filename_run():
    from datetime import date
    from app.scraper.collector import parse_date
    assert parse_date("Medical Board_06182026_Audio.mp3") == date(2026, 6, 18)


def test_parse_date_mmddyyyy_requires_separators():
    from app.scraper.collector import parse_date
    # A bare 8-digit number without separators must NOT parse as a date
    assert parse_date("case number 20250612345") is None


def test_parse_date_precise_accepts_day_precision():
    from datetime import date
    from app.scraper.collector import parse_date_precise
    assert parse_date_precise("Med Board Meeting 6-6-25 minutes draft.pdf") == date(2025, 6, 6)
    assert parse_date_precise("Jan 14 2026 - Executive Committee Minutes.pdf") == date(2026, 1, 14)


def test_parse_date_precise_rejects_month_only():
    from app.scraper.collector import parse_date_precise
    # "September 2025" parses to day=1 in parse_date — precise must reject it
    assert parse_date_precise("September 2025_Open Session Minutes.pdf") is None
    assert parse_date_precise("June 2026 Med Board Draft Agenda.pdf") is None


def test_parse_date_precise_accepts_explicit_first():
    from datetime import date
    from app.scraper.collector import parse_date_precise
    assert parse_date_precise("minutes 2026-06-01 workshop.pdf") == date(2026, 6, 1)


def test_filter_text_is_regex():
    assert _passes_filter("TMB Medical Board Meeting June 2026", r"medical\s+board")
    assert not _passes_filter("Acupuncture Board Meeting June 2026", r"medical\s+board")
    assert _passes_filter("050826medagenda.pdf row",
                          r"(\d{6}med[a-z]*\.pdf|medicine\s*(and|&)\s*surgery)")
    assert not _passes_filter("040826chirominutes.pdf row",
                              r"(\d{6}med[a-z]*\.pdf|medicine\s*(and|&)\s*surgery)")


def test_is_within_window_rejects_far_future():
    from datetime import date, timedelta
    from app.scraper.collector import is_within_window
    today = date.today()
    assert is_within_window(today)
    assert is_within_window(today + timedelta(days=200))   # scheduled meeting
    assert not is_within_window(date(2050, 3, 4))          # mis-parsed typo
    assert not is_within_window(today - timedelta(days=800))  # too old


# ---------------------------------------------------------------------------
# _infer_doc_type
# ---------------------------------------------------------------------------

def test_infer_doc_type():
    assert _infer_doc_type("2026-01-01_agenda.pdf") == "agenda"
    assert _infer_doc_type("meeting_notice.pdf") == "notice"
    assert _infer_doc_type("exhibit_a.pdf") == "attachment"
    assert _infer_doc_type("january_minutes.pdf") == "minutes"
