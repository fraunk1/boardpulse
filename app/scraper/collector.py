"""Collect meeting documents from discovered board minutes pages.

Visits each board's minutes_url, takes a full-page screenshot, extracts
links, identifies meeting entries by date, and downloads associated
documents (PDFs, DOCX, etc.) for later text extraction.
"""
import asyncio
import base64
import hashlib
import logging
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse

import httpx
from playwright.async_api import async_playwright
from sqlalchemy import select

from app.scraper.browser_provider import launch_browser
from app.scraper.strategies import get_strategy
import app.database as db
from app.models import Board, Meeting, MeetingDocument
from app.config import SCRAPE_DELAY_SECONDS, SCREENSHOTS_DIR, DOCUMENTS_DIR, USER_AGENT

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Date patterns — ordered most-specific first
# ---------------------------------------------------------------------------

DATE_PATTERNS = [
    # "January 15, 2026" or "Jan 15, 2026" (comma optional)
    re.compile(
        r'((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?'
        r'|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?'
        r'|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4})',
        re.IGNORECASE,
    ),
    # "Apr 3 2026 8:30AM" — date-time format used by VA DHP calendar
    re.compile(
        r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{4})',
        re.IGNORECASE,
    ),
    # "2026-01-15"
    re.compile(r'(\d{4}-\d{2}-\d{2})'),
    # "2026_01_15" — embedded in filenames (e.g. AK board books)
    re.compile(r'(\d{4}_\d{2}_\d{2})'),
    # "01/15/2026" or "03/20/2026" or "12/04/25" (2-digit year)
    re.compile(r'(\d{1,2}/\d{1,2}/\d{2,4})'),
    # "01.15.2026" or "01.15.26" — e.g. HI Medical Board "01.16.25 Meeting Minutes"
    re.compile(r'(\d{1,2}\.\d{1,2}\.\d{2,4})'),
    # "8-7-2025" or "12-04-25" — dashes between M-D-Y (MI, OH boards)
    re.compile(r'(\d{1,2}-\d{1,2}-\d{2,4})'),
    # "_06182026_" — MMDDYYYY run embedded in filenames (UT PMN audio/PDF
    # names). Bounded by separators to avoid matching arbitrary numbers.
    re.compile(r'[_\-.](\d{2}\d{2}20\d{2})[_\-.]'),
    # "January 2026" or "Jan 2026" — month+year only (e.g. MS_MD "January 2026 Board Meeting Minutes")
    re.compile(
        r'((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?'
        r'|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?'
        r'|Dec(?:ember)?)\s+\d{4})',
        re.IGNORECASE,
    ),
]

# File extensions we consider downloadable documents
DOCUMENT_EXTENSIONS = {".pdf", ".docx", ".doc", ".xlsx", ".xls"}

# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------


def parse_date(text: str) -> date | None:
    """Try to extract a date from *text* using known patterns.

    Returns the first successfully-parsed date, or ``None``.
    """
    # Normalize ordinal suffixes: "30th" -> "30", "2nd" -> "2", "3rd" -> "3"
    # This handles PA boards that publish "January 30th, 2024" style dates.
    text = re.sub(r'(\d+)(?:st|nd|rd|th)\b', r'\1', text)
    for pattern in DATE_PATTERNS:
        m = pattern.search(text)
        if not m:
            continue
        raw = m.group(1).strip()
        # Try multiple strptime formats for the matched string
        for fmt in (
            "%B %d, %Y",   # January 15, 2026
            "%B %d %Y",    # January 15 2026
            "%b %d, %Y",   # Jan 15, 2026
            "%b %d %Y",    # Jan 15 2026
            "%Y-%m-%d",    # 2026-01-15
            "%Y_%m_%d",    # 2026_01_15 (filename-embedded dates)
            "%m/%d/%Y",    # 01/15/2026
            "%m/%d/%y",    # 12/04/25 (2-digit year, e.g. MI_DO)
            "%m.%d.%Y",    # 01.15.2026
            "%m.%d.%y",    # 01.15.26 (2-digit year, e.g. HI Medical Board)
            "%m-%d-%Y",    # 8-7-2025 (dashes, e.g. MI_DO filenames)
            "%m-%d-%y",    # 8-7-25 (dashes, 2-digit year)
            "%m%d%Y",      # 06182026 (MMDDYYYY filename runs, e.g. UT PMN)
            "%B %Y",       # January 2026 (month+year only — assign day=1)
            "%b %Y",       # Jan 2026 (month+year only)
        ):
            try:
                return datetime.strptime(raw, fmt).date()
            except ValueError:
                continue
    return None


def is_within_window(d: date, months: int = 24) -> bool:
    """Return True if *d* is within the last *months* months from today,
    or a plausibly-scheduled future meeting (≤ ~13 months out). Guards
    against mis-parsed far-future dates (a source typo once yielded 2050,
    which sat on top of the dashboard's Latest Intelligence feed)."""
    today = date.today()
    cutoff = today - timedelta(days=months * 30)
    horizon = today + timedelta(days=400)
    return cutoff <= d <= horizon


# ---------------------------------------------------------------------------
# Link extraction JS — runs inside the browser page
# ---------------------------------------------------------------------------

_EXTRACT_LINKS_JS = """() => {
    const docExts = ['.pdf', '.docx', '.doc', '.xlsx', '.xls'];
    // Date patterns to detect whether an ancestor element contains a date
    const dateRe = /(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\\s+\\d{1,2}|\\d{1,2}[\\/.-]\\d{1,2}[\\/.-]\\d{2,4}|\\d{4}[-_]\\d{2}[-_]\\d{2}/i;
    const yearOnlyRe = /^\\s*(20\\d{2})\\s*$/;
    const results = [];
    for (const a of document.querySelectorAll('a[href]')) {
        const href = a.href || '';
        const text = (a.innerText || a.textContent || '').trim();
        const parentText = (a.parentElement ? a.parentElement.innerText || '' : '').trim();
        const lowerHref = href.toLowerCase();
        // Strip query string and fragment for extension check (CMS URLs
        // like ...minutes.pdf?rev=abc&hash=def must still match)
        const hrefPath = lowerHref.split('?')[0].split('#')[0];
        let isDoc = docExts.some(ext => hrefPath.endsWith(ext));
        // Portal endpoints carry the type in a query param instead of the path,
        // e.g. /document?filekey=ABC&filetype=pdf (Montana DLI and similar CMS viewers)
        if (!isDoc && /filetype=(pdf|docx?|xlsx?)(&|$)/i.test(lowerHref)) isDoc = true;
        // Known document-endpoint shapes with no file extension. Kept narrow:
        // a misclassified link is rejected at download by byte validation.
        if (!isDoc) {
            const docUrlPatterns = [
                /getfile\\.cfm/i,                              // VA townhall
                /download_resource\\.asp\\?/i,                 // ND/WV boards
                /\\/download-attachment\\//i,                  // WI publicmeetings
                /\\/(doc|document)s?\\/[^?#]*\\/download\\/?([?#]|$)/i,  // mass.gov, georgia.gov CMS
                /drive\\.google\\.com\\/(file\\/d\\/|open\\?id=|uc\\?)/i,   // IA (Drive-hosted)
                /docs\\.google\\.com\\/document\\/d\\//i,
            ];
            if (docUrlPatterns.some(re => re.test(href))) isDoc = true;
        }

        // Walk up to 8 ancestor levels to find context with a date.
        // Two strategies:
        //  1. Shallowest ancestor < 600 chars that contains a date pattern
        //  2. Nearest ancestor/sibling heading whose text is just a 4-digit year
        let ancestorText = '';
        let sectionYear = '';
        let el = a.parentElement;
        for (let i = 0; i < 8 && el && el.tagName !== 'BODY' && el.tagName !== 'HTML'; i++) {
            const t = (el.innerText || '').trim();
            // Strategy 1: short ancestor with a recognisable date
            if (!ancestorText && t.length < 600 && dateRe.test(t)) {
                ancestorText = t;
            }
            // Strategy 2: look for sibling headings/elements that are just a year
            // (covers sites like GA that use year-only accordion labels)
            if (!sectionYear) {
                const siblings = el.parentElement ? Array.from(el.parentElement.children) : [];
                for (const sib of siblings) {
                    const st = (sib.innerText || sib.textContent || '').trim();
                    const ym = yearOnlyRe.exec(st);
                    if (ym) { sectionYear = ym[1]; break; }
                }
            }
            el = el.parentElement;
        }
        // If we found a year section but no full date in ancestor, append year to context
        if (sectionYear && !ancestorText) {
            ancestorText = sectionYear;
        }

        results.push({href, text, parentText, ancestorText, isDoc});
    }
    return results;
}"""

# ---------------------------------------------------------------------------
# Document type inference
# ---------------------------------------------------------------------------


def _infer_doc_type(filename: str) -> str:
    """Guess document type from filename keywords."""
    lower = filename.lower()
    if "agenda" in lower:
        return "agenda"
    if "notice" in lower:
        return "notice"
    if "attachment" in lower or "exhibit" in lower:
        return "attachment"
    return "minutes"


def _sanitize_name(raw: str, limit: int = 80) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", raw)[:limit]


def transform_download_url(url: str) -> str:
    """Rewrite viewer URLs to their direct-download form.

    Google Drive/Docs viewer links render an HTML page; the export endpoints
    return the file bytes. Non-matching URLs pass through unchanged.
    """
    m = re.search(r"drive\.google\.com/file/d/([A-Za-z0-9_-]+)", url)
    if m:
        return f"https://drive.google.com/uc?export=download&id={m.group(1)}"
    m = re.search(r"drive\.google\.com/open\?id=([A-Za-z0-9_-]+)", url)
    if m:
        return f"https://drive.google.com/uc?export=download&id={m.group(1)}"
    m = re.search(r"docs\.google\.com/document/d/([A-Za-z0-9_-]+)", url)
    if m:
        return (f"https://docs.google.com/document/d/{m.group(1)}"
                f"/export?format=pdf")
    return url


def _passes_filter(combined_text: str, filter_text: str | None) -> bool:
    """Strategy filter_text: keep only rows mentioning the board's name
    (case-insensitive) — for multi-board index pages like Iowa DIAL."""
    return not filter_text or filter_text.lower() in combined_text.lower()


def _site_key(url: str) -> str:
    """Coarse registrable-domain key (last two labels) for same-site checks."""
    host = urlparse(url).netloc.lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    labels = host.split(".")
    return ".".join(labels[-2:]) if len(labels) >= 2 else host


# Politeness limits: some boards' detail pages link entire document archives,
# which would attribute hundreds of files to every meeting and hammer the
# host (Florida DOH served 5,609 failed attempts in one run before these).
MAX_NEW_DOWNLOADS_PER_RUN = 200     # per board per run; refresh runs catch up
MAX_CONSECUTIVE_FAILURES = 25       # circuit breaker: stop the board's downloads
MAX_CHILD_DOCS_PER_MEETING = 15     # depth-1 doc links attributed to one date

# Links that are dated but never lead to documents — skip in depth-1 crawls.
_DETAIL_SKIP_RE = re.compile(
    r"(zoom(gov)?\.com|webex\.com|youtube\.com|facebook\.com|twitter\.com"
    r"|calendar\.google|maps\.google|mailto:|\.(?:jpg|jpeg|png|gif|mp3|mp4|m4a)$)",
    re.IGNORECASE,
)


def _should_visit_detail(url: str, base_url: str, visited: set[str]) -> bool:
    """Depth-1 guard: same site, not junk, not already visited."""
    if not url or url in visited:
        return False
    if _DETAIL_SKIP_RE.search(url):
        return False
    return _site_key(url) == _site_key(base_url)


def _doc_filename(full_url: str) -> str:
    """Derive a download filename with a real extension.

    Handles portal/viewer endpoints where the URL path has no extension —
    otherwise every such link collapses to the same name ("document") and
    only the first one survives the dedup check. When the type can't be
    known, .pdf is assumed; byte validation confirms or rejects at download.
    """
    parsed = urlparse(full_url)
    name = Path(parsed.path).name
    if name and Path(name).suffix.lower() in DOCUMENT_EXTENSIONS:
        return name

    qs = {k.lower(): v for k, v in parse_qs(parsed.query).items()}

    def _first(*keys):
        for k in keys:
            if qs.get(k):
                return qs[k][0]
        return ""

    # A query value that is itself a file path (e.g. townhall.virginia.gov
    # GetFile.cfm?File=E:\docroot\...\minutes.pdf) → use its basename.
    for values in qs.values():
        for v in values:
            v_name = Path(v.replace("\\", "/")).name
            if v_name and Path(v_name).suffix.lower() in DOCUMENT_EXTENSIONS:
                return _sanitize_name(v_name)

    # Explicit type in the query (e.g. Montana DLI ?filekey=ABC&filetype=pdf)
    ftype = _first("filetype", "type", "format").lower().lstrip(".")
    if ftype in {"pdf", "docx", "doc", "xlsx", "xls"}:
        key = _first("filekey", "file", "id", "documentid", "docid")
        stem = re.sub(r"[^A-Za-z0-9_-]", "", key)[:40] or hashlib.md5(
            full_url.encode()).hexdigest()[:10]
        return f"{stem}.{ftype}"

    path_lower = parsed.path.lower()

    # download_resource.asp?id=123 (ND/WV boards) → resource_123.pdf
    if "download_resource" in path_lower:
        rid = _first("id", "resourceid")
        if rid:
            return f"resource_{re.sub(r'[^A-Za-z0-9_-]', '', rid)[:40]}.pdf"

    # /download-attachment/<guid> (WI publicmeetings) → <guid>.pdf
    m = re.search(r"/download-attachment/([A-Za-z0-9-]+)", parsed.path, re.I)
    if m:
        return f"{m.group(1)[:60]}.pdf"

    # /doc/<slug>/download, /document/.../<slug>/download (mass.gov, georgia.gov)
    m = re.search(r"/(?:doc|document)s?/(?:[^?#]*/)?([^/?#]+)/download/?$",
                  parsed.path, re.I)
    if m:
        return f"{_sanitize_name(m.group(1), 60)}.pdf"

    # Google Drive file links → drive_<id>.pdf
    m = re.search(r"drive\.google\.com/(?:file/d/|open\?id=|uc\?.*\bid=)"
                  r"([A-Za-z0-9_-]+)", full_url, re.I)
    if m:
        return f"drive_{m.group(1)[:44]}.pdf"

    # Script endpoints (GetFile.cfm etc.) with nothing recognizable: hash the
    # URL so each distinct document gets a unique name; assume pdf.
    if Path(name).suffix.lower() in {".cfm", ".asp", ".aspx", ".php", ".jsp"}:
        return (f"{_sanitize_name(Path(name).stem, 20)}_"
                f"{hashlib.md5(full_url.encode()).hexdigest()[:10]}.pdf")

    return name or "document"


# ---------------------------------------------------------------------------
# Download helpers — validation + escalation ladder
# ---------------------------------------------------------------------------

# Magic-byte signatures per extension. A download that doesn't match is an
# error page or portal stub (e.g. Montana's 95-byte "Unable to retrieve
# document" response) and must never be written to disk or the DB.
_MAGIC_SIGNATURES: dict[str, tuple[bytes, ...]] = {
    ".pdf": (b"%PDF",),
    ".docx": (b"PK\x03\x04",),
    ".xlsx": (b"PK\x03\x04",),
    ".doc": (b"\xd0\xcf\x11\xe0",),   # OLE compound file
    ".xls": (b"\xd0\xcf\x11\xe0",),
}

_MIN_DOCUMENT_BYTES = 500

# State file hosts with broken TLS chains (missing intermediates) that
# reject verified connections. Downloads from EXACTLY these hosts may
# retry without TLS verification — see the rung-1b comment in
# _download_document for the risk acceptance rationale.
TLS_RELAXED_HOSTS = {
    "ww10.doh.state.fl.us",   # Florida DOH document server (FL_MD, FL_DO)
}


def validate_document_bytes(data: bytes, ext: str) -> tuple[bool, str]:
    """Check that *data* plausibly IS a document of type *ext*.

    Returns (valid, reason). Rejects tiny bodies and HTML error pages;
    for known extensions, requires the file-format magic bytes.
    """
    if not data:
        return False, "empty body"
    if len(data) < _MIN_DOCUMENT_BYTES:
        return False, f"too small ({len(data)} bytes)"

    head = data[:1024].lstrip()
    if head[:1] == b"<":
        return False, "html body"

    sigs = _MAGIC_SIGNATURES.get(ext.lower())
    if sigs:
        if any(data.startswith(s) for s in sigs):
            return True, ""
        # Rare: PDFs with a byte-order mark or junk prefix before %PDF
        if ext.lower() == ".pdf" and b"%PDF" in data[:1024]:
            return True, ""
        return False, f"missing {ext} signature"

    return True, ""


async def _download_file(
    client: httpx.AsyncClient,
    url: str,
    dest: Path,
) -> bool:
    """Legacy plain-httpx download (kept for recollect_docs.py compat)."""
    try:
        resp = await client.get(url, follow_redirects=True, timeout=60)
        if resp.status_code != 200:
            logger.warning("HTTP %s downloading %s", resp.status_code, url)
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(resp.content)
        logger.info("Downloaded %s → %s", url, dest)
        return True
    except Exception as exc:
        logger.warning("Failed to download %s: %s", url, exc)
        return False


async def _download_document(
    page,
    client: httpx.AsyncClient,
    url: str,
    dest: Path,
    referer: str | None = None,
) -> str:
    """Download *url* to *dest* with byte validation.

    Escalation ladder:
      1. plain httpx (fast, no session)
      2. the Playwright browser context's request client — carries the
         page's cookies/session, which portal sites (Montana DLI etc.)
         require. Skipped on Lightpanda (CDP cookie sync is unreliable).

    Returns "ok" (written), "rejected" (got bytes but they failed
    validation on every rung), or "error" (no response at all).
    """
    best_reason = "no response"
    got_bytes = False

    # Rung 1 — plain httpx
    data: bytes | None = None
    try:
        resp = await client.get(url, follow_redirects=True, timeout=60)
        if resp.status_code == 200:
            data = resp.content
    except Exception as exc:
        logger.debug("httpx download failed for %s: %s", url, exc)
        # Rung 1b — explicit allowlist of state file hosts with broken TLS
        # chains (incomplete intermediates). Verification is relaxed ONLY for
        # these named hosts — a deliberate, narrow risk acceptance: the files
        # are public records, magic-byte validation gates every write, and
        # the content is human-reviewed downstream. Never relax globally.
        host = urlparse(url).netloc.lower()
        if host in TLS_RELAXED_HOSTS:
            try:
                async with httpx.AsyncClient(
                    headers={"User-Agent": USER_AGENT},
                    follow_redirects=True, verify=False,
                ) as insecure:
                    resp = await insecure.get(url, timeout=60)
                    if resp.status_code == 200:
                        data = resp.content
                        logger.info("TLS-relaxed download (allowlisted host "
                                    "%s): %s", host, url)
            except Exception as exc2:
                logger.debug("TLS-relaxed download failed for %s: %s", url, exc2)

    if data is not None:
        got_bytes = True
        valid, reason = validate_document_bytes(data, dest.suffix)
        if valid:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            logger.info("Downloaded %s → %s", url, dest)
            return "ok"
        best_reason = reason

    # Rung 2 — browser-context request (session-carrying)
    browser = getattr(page.context, "browser", None)
    if not getattr(browser, "_is_lightpanda", False):
        try:
            headers = {"Referer": referer} if referer else {}
            r = await page.context.request.get(url, headers=headers, timeout=60_000)
            if r.ok:
                data2 = await r.body()
                got_bytes = True
                valid, reason = validate_document_bytes(data2, dest.suffix)
                if valid:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(data2)
                    logger.info("Downloaded (browser session) %s → %s", url, dest)
                    return "ok"
                best_reason = reason
        except Exception as exc:
            logger.debug("context.request download failed for %s: %s", url, exc)

    # Rung 3 — page-initiated fetch: runs inside the loaded page itself, so
    # it carries the complete browser fingerprint + cookies. Needed where
    # servers reject any non-page request (NH hotlink protection, mass.gov
    # Akamai). Same-origin only — cross-origin reads are CORS-blocked.
    try:
        page_host = urlparse(page.url).netloc.split(":")[0].lower()
        target_host = urlparse(url).netloc.split(":")[0].lower()
        if page_host and page_host.removeprefix("www.") == \
                target_host.removeprefix("www."):
            b64 = await page.evaluate(
                """async (u) => {
                    try {
                        const r = await fetch(u, {credentials: 'include'});
                        if (!r.ok) return null;
                        const buf = await r.arrayBuffer();
                        const bytes = new Uint8Array(buf);
                        let s = '';
                        const chunk = 0x8000;
                        for (let i = 0; i < bytes.length; i += chunk) {
                            s += String.fromCharCode.apply(
                                null, bytes.subarray(i, i + chunk));
                        }
                        return btoa(s);
                    } catch (e) { return null; }
                }""",
                url,
            )
            if b64:
                data3 = base64.b64decode(b64)
                got_bytes = True
                valid, reason = validate_document_bytes(data3, dest.suffix)
                if valid:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(data3)
                    logger.info("Downloaded (page fetch) %s → %s", url, dest)
                    return "ok"
                best_reason = reason
    except Exception as exc:
        logger.debug("page-fetch download failed for %s: %s", url, exc)

    if got_bytes:
        logger.warning("REJECT [%s] %s", best_reason, url)
        return "rejected"
    logger.warning("Download failed (no response): %s", url)
    return "error"


# ---------------------------------------------------------------------------
# collect_board — process one board
# ---------------------------------------------------------------------------


async def collect_board(board: Board, page) -> dict:
    """Collect meeting minutes and documents for a single board.

    Args:
        board: Board ORM instance (must have minutes_url set).
        page: Playwright page to reuse.

    Returns:
        Stats dict with keys: meetings_found, documents_downloaded, errors.
    """
    stats = {
        "meetings_found": 0,
        "documents_downloaded": 0,
        "errors": 0,
        "rejected": 0,
        "docs_registered_existing": 0,
    }

    strategy = get_strategy(board.code)

    if not board.minutes_url:
        logger.info("Skipping %s — no minutes_url", board.code)
        return stats

    logger.info("Collecting %s → %s", board.code, board.minutes_url)

    # 1. Navigate to the minutes page
    try:
        await page.goto(board.minutes_url, wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(3)  # Allow JS to render
    except Exception as exc:
        logger.error("Failed to load %s: %s", board.minutes_url, exc)
        stats["errors"] += 1
        return stats

    # The FINAL page URL — sites redirect to new domains (tmb.state.tx.us ->
    # tmb.texas.gov); same-site checks must use where we actually landed.
    base_url = page.url or board.minutes_url

    # 2. Full-page screenshot
    ss_dir = SCREENSHOTS_DIR / board.code
    ss_dir.mkdir(parents=True, exist_ok=True)
    ss_path = ss_dir / "minutes_page.png"
    try:
        await page.screenshot(path=str(ss_path), full_page=True)
        logger.info("Screenshot saved → %s", ss_path)
    except Exception as exc:
        logger.warning("Screenshot failed for %s: %s", board.code, exc)

    # 3. Expand year-based accordions/tabs (e.g. Georgia GCMB, some state sites
    #    use clickable year labels that reveal monthly meeting links beneath them).
    #    We try to click exact-text-match elements for the current and prior year.
    try:
        current_year = date.today().year
        expand_years = [str(current_year), str(current_year - 1)]
        for year_label in expand_years:
            # Use Playwright's locator to find and click year-text elements.
            # Filter to elements whose *exact* trimmed text is the year number.
            locator = page.locator(
                "button, summary, [role='button'], a, li, div, span"
            ).filter(has_text=re.compile(rf"^\s*{year_label}\s*$"))
            count = await locator.count()
            for i in range(count):
                try:
                    await locator.nth(i).click(timeout=2000)
                    await asyncio.sleep(0.5)
                except Exception:
                    pass
            if count:
                logger.debug("Clicked %s year accordion(s) for %s on %s", count, year_label, board.code)
                await asyncio.sleep(1)
    except Exception as exc:
        logger.debug("Accordion expansion failed for %s: %s", board.code, exc)

    # 4. Extract all links
    try:
        links = await page.evaluate(_EXTRACT_LINKS_JS)
    except Exception as exc:
        logger.error("Link extraction failed for %s: %s", board.code, exc)
        stats["errors"] += 1
        return stats

    # 4b. Pagination: harvest additional index pages (?page=1..N-1, Drupal
    # convention where page=0 is the first page — e.g. WA Medical Commission).
    if strategy.paginate > 1:
        sep = "&" if "?" in board.minutes_url else "?"
        for i in range(1, strategy.paginate):
            page_url = f"{board.minutes_url}{sep}page={i}"
            try:
                await page.goto(page_url, wait_until="domcontentloaded",
                                timeout=30000)
                await asyncio.sleep(2)
                links.extend(await page.evaluate(_EXTRACT_LINKS_JS))
                logger.info("[%s] pagination: harvested %s", board.code, page_url)
            except Exception as exc:
                logger.debug("[%s] pagination page %s failed: %s",
                             board.code, page_url, exc)

    # Per-board escape hatch: strategy include_patterns force isDoc for link
    # shapes the global heuristics miss (byte validation still gates writes).
    if strategy.include_patterns:
        pats = [re.compile(p, re.IGNORECASE) for p in strategy.include_patterns]
        for link in links:
            if not link.get("isDoc") and any(
                pat.search(link.get("href") or "") for pat in pats
            ):
                link["isDoc"] = True

    # 4. Identify meeting entries — group links by date
    #    Each link may carry date context in its text or parent text.
    meetings_map: dict[date, list[dict]] = {}

    for link in links:
        combined_text = (
            f"{link.get('text', '')} "
            f"{link.get('parentText', '')} "
            f"{link.get('ancestorText', '')} "
            f"{link.get('href', '')}"  # href often contains YYYY_MM_DD or YYYY-MM-DD
        )
        if not _passes_filter(combined_text, strategy.filter_text):
            continue
        d = parse_date(combined_text)
        if d is None:
            continue
        if not is_within_window(d):
            continue
        meetings_map.setdefault(d, []).append(link)

    if not meetings_map:
        logger.info("No dated meeting links found for %s", board.code)
        return stats

    # 4c. Depth-1: dated links that are NOT documents often lead to meeting
    # detail pages holding the PDFs (TX, FL, UT-PMN, MN, DE, AK...). Visit
    # them and attach harvested doc links to the PARENT link's date. Dates
    # whose meetings already have documents in the DB are skipped, so
    # repeated refresh runs work through the backlog within the cap.
    if strategy.depth >= 1:
        detail_cap = 40
        visited: set[str] = set()

        async with db.async_session() as session:
            rows = await session.execute(
                select(Meeting.meeting_date)
                .join(MeetingDocument, MeetingDocument.meeting_id == Meeting.id)
                .where(Meeting.board_id == board.id)
            )
            dates_with_docs = {r[0] for r in rows}

        for meeting_date in sorted(meetings_map, reverse=True):  # newest first
            if len(visited) >= detail_cap:
                break
            if meeting_date in dates_with_docs:
                continue
            for link in list(meetings_map[meeting_date]):
                if len(visited) >= detail_cap:
                    break
                if link.get("isDoc"):
                    continue
                detail_url = urljoin(
                    base_url, (link.get("href") or "")
                ).split("#")[0]
                if not _should_visit_detail(detail_url, base_url, visited):
                    continue
                visited.add(detail_url)
                try:
                    await page.goto(detail_url, wait_until="domcontentloaded",
                                    timeout=30000)
                    await asyncio.sleep(1.5)
                    child_links = await page.evaluate(_EXTRACT_LINKS_JS)
                except Exception as exc:
                    logger.debug("[%s] depth-1 visit failed %s: %s",
                                 board.code, detail_url, exc)
                    continue

                child_docs = [cl for cl in child_links if cl.get("isDoc")]
                if strategy.include_patterns:
                    pats = [re.compile(p, re.IGNORECASE)
                            for p in strategy.include_patterns]
                    for cl in child_links:
                        if not cl.get("isDoc") and any(
                            pat.search(cl.get("href") or "") for pat in pats
                        ):
                            child_docs.append(cl)
                if child_docs:
                    # Cap per meeting: some detail pages link entire archives
                    child_docs = child_docs[:MAX_CHILD_DOCS_PER_MEETING]
                    meetings_map[meeting_date].extend(child_docs)
                    logger.info("[%s] depth-1: +%d doc link(s) from %s",
                                board.code, len(child_docs), detail_url)

    # 5. Persist meetings and download documents
    async with db.async_session() as session:
        async with httpx.AsyncClient(
            headers={"User-Agent": USER_AGENT},
            follow_redirects=True,
        ) as client:
            downloads_this_run = 0
            consecutive_failures = 0
            budget_exhausted = False

            for meeting_date in sorted(meetings_map):
                if budget_exhausted:
                    break
                meeting_links = meetings_map[meeting_date]

                # Idempotent at the DOCUMENT level, not the meeting level:
                # boards post agendas first and minutes weeks later under the
                # same date, so an existing meeting must still have its links
                # processed. Existing docs are deduped by source_url/filename.
                existing = await session.execute(
                    select(Meeting).where(
                        Meeting.board_id == board.id,
                        Meeting.meeting_date == meeting_date,
                    )
                )
                meeting = existing.scalars().first()

                if meeting is not None:
                    doc_rows = (await session.execute(
                        select(MeetingDocument).where(
                            MeetingDocument.meeting_id == meeting.id
                        )
                    )).scalars().all()
                    known_urls = {d.source_url for d in doc_rows if d.source_url}
                    known_files = {d.filename for d in doc_rows}
                else:
                    meeting = Meeting(
                        board_id=board.id,
                        meeting_date=meeting_date,
                        title=f"{board.name} — {meeting_date.strftime('%B %d, %Y')}",
                        source_url=board.minutes_url,
                        screenshot_path=str(ss_path),
                    )
                    session.add(meeting)
                    await session.flush()  # get meeting.id
                    stats["meetings_found"] += 1
                    known_urls, known_files = set(), set()

                # Download document links associated with this date
                doc_dir = DOCUMENTS_DIR / board.code
                doc_dir.mkdir(parents=True, exist_ok=True)

                for link in meeting_links:
                    href = link.get("href", "")
                    if not link.get("isDoc"):
                        continue

                    # Resolve relative URLs
                    full_url = urljoin(board.minutes_url, href)
                    filename = _doc_filename(full_url)

                    # Prefix with date for uniqueness
                    safe_date = meeting_date.isoformat()
                    dest_filename = f"{safe_date}_{filename}"
                    dest_path = doc_dir / dest_filename

                    if full_url in known_urls or dest_filename in known_files:
                        continue

                    def _register(status_key: str):
                        doc = MeetingDocument(
                            meeting_id=meeting.id,
                            doc_type=_infer_doc_type(filename),
                            filename=dest_filename,
                            file_path=str(dest_path),
                            source_url=full_url,
                        )
                        session.add(doc)
                        stats[status_key] += 1
                        known_urls.add(full_url)
                        known_files.add(dest_filename)

                    if dest_path.exists():
                        # A file on disk without a DB row (post-reset state).
                        # Validate it: good file -> register the missing row;
                        # stub/corrupt -> delete and fall through to re-download.
                        valid, reason = validate_document_bytes(
                            dest_path.read_bytes(), dest_path.suffix
                        )
                        if valid:
                            _register("docs_registered_existing")
                            continue
                        logger.info(
                            "Replacing invalid on-disk file (%s): %s",
                            reason, dest_path.name,
                        )
                        dest_path.unlink(missing_ok=True)

                    if downloads_this_run >= MAX_NEW_DOWNLOADS_PER_RUN:
                        logger.warning(
                            "[%s] download budget (%d) reached — remaining "
                            "documents will be picked up by the next refresh",
                            board.code, MAX_NEW_DOWNLOADS_PER_RUN,
                        )
                        budget_exhausted = True
                        break
                    if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                        logger.warning(
                            "[%s] circuit breaker: %d consecutive download "
                            "failures — stopping this board's downloads",
                            board.code, MAX_CONSECUTIVE_FAILURES,
                        )
                        budget_exhausted = True
                        break

                    result = await _download_document(
                        page, client, transform_download_url(full_url),
                        dest_path, referer=board.minutes_url,
                    )
                    if result == "ok":
                        _register("documents_downloaded")
                        downloads_this_run += 1
                        consecutive_failures = 0
                    elif result == "rejected":
                        stats["rejected"] += 1
                        consecutive_failures += 1
                    else:
                        stats["errors"] += 1
                        consecutive_failures += 1

            await session.commit()

    return stats


# ---------------------------------------------------------------------------
# collect_all — run collection for all (or one) board
# ---------------------------------------------------------------------------


async def collect_all(
    board_code: str | None = None,
    exclude_codes: set[str] | None = None,
):
    """Run document collection for discovered boards.

    Args:
        board_code: If provided, only collect for this specific board.
                    Otherwise collect for all boards with discovery_status
                    in ('found', 'manual').
        exclude_codes: Board codes to skip (e.g. headed-strategy boards
                    during unattended refresh runs).
    """
    await db.init_db()

    # Query target boards
    async with db.async_session() as session:
        stmt = select(Board).where(Board.minutes_url.isnot(None))
        if board_code:
            stmt = stmt.where(Board.code == board_code)
        else:
            stmt = stmt.where(Board.discovery_status.in_(("found", "manual")))
        result = await session.execute(stmt)
        boards = list(result.scalars().all())

    if exclude_codes:
        skipped = [b.code for b in boards if b.code in exclude_codes]
        if skipped:
            print(f"Skipping (excluded): {', '.join(skipped)}")
        boards = [b for b in boards if b.code not in exclude_codes]

    if not boards:
        print("No boards ready for collection.")
        return

    print(f"Collecting documents for {len(boards)} board(s)...")

    async with async_playwright() as pw:
        browser, context, page = await launch_browser(pw, site_id="collector")

        for i, board in enumerate(boards):
            if i > 0:
                await asyncio.sleep(SCRAPE_DELAY_SECONDS)

            strategy = get_strategy(board.code)
            try:
                if strategy.headed or strategy.browser == "chromium":
                    # Dedicated browser: headed window (WAF bypass) and/or
                    # guaranteed real Chromium for session-carrying downloads.
                    b2, c2, p2 = await launch_browser(
                        pw, site_id=board.code, headed=strategy.headed,
                    )
                    try:
                        stats = await collect_board(board, p2)
                    finally:
                        await b2.close()
                else:
                    stats = await collect_board(board, page)
                extra = ""
                if stats.get("rejected"):
                    extra += f"  rejected={stats['rejected']}"
                if stats.get("docs_registered_existing"):
                    extra += f"  registered={stats['docs_registered_existing']}"
                print(
                    f"  [{board.code}] meetings={stats['meetings_found']}  "
                    f"docs={stats['documents_downloaded']}  "
                    f"errors={stats['errors']}{extra}"
                )
            except Exception as exc:
                logger.error("Unexpected error collecting %s: %s", board.code, exc)
                print(f"  [{board.code}] ERROR: {exc}")
                continue

            # Update last_scraped_at
            async with db.async_session() as session:
                db_board = await session.get(Board, board.id)
                if db_board:
                    db_board.last_scraped_at = datetime.now()
                    await session.commit()

        await browser.close()

    print("Collection complete.")
