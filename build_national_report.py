"""Build self-contained HTML national landscape report with full-document exhibits.

Run with:
    cd Projects/boardpulse && source venv/bin/activate && python build_national_report.py
"""

import asyncio
import base64
import io
import re
import sys
from pathlib import Path

import markdown
from PIL import Image
from sqlalchemy import select

# ── path setup ───────────────────────────────────────────────────────────────
BASE = Path(__file__).parent
sys.path.insert(0, str(BASE))

import app.database as db
from app.database import init_db
from app.extractor.exhibits import parse_report_citations
from app.models import Board

REPORT_MD   = BASE / "data/reports/2026-03-31-board-landscape.md"
EXHIBITS_DIR = BASE / "data/exhibits"
OUTPUT_HTML  = BASE / "data/reports/2026-03-31-national-report-with-exhibits.html"

# JPEG quality for page images — balance size vs. readability
JPEG_QUALITY = 45

# For exhibits with more than this many pages, show only the highlight page
# ± CONTEXT_WINDOW surrounding pages (the rest exist but are omitted for size)
MAX_PAGES_FULL = 20
CONTEXT_WINDOW = 5


# ── database ─────────────────────────────────────────────────────────────────

async def get_board_map():
    await init_db()
    async with db.async_session() as session:
        boards = (await session.execute(select(Board))).scalars().all()
    return {b.code: {"name": b.name, "url": b.minutes_url or b.homepage or ""}
            for b in boards}


# ── image conversion ──────────────────────────────────────────────────────────

def png_to_b64_jpeg(png_path: Path, quality: int = JPEG_QUALITY) -> str:
    """Convert PNG to base64-encoded JPEG."""
    with Image.open(png_path) as img:
        # Convert RGBA → RGB for JPEG
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=quality, optimize=True)
        return base64.b64encode(buf.getvalue()).decode("ascii")


# ── exhibit block builder ─────────────────────────────────────────────────────

def build_exhibit_block(
    exhibit_num: int,
    board_code: str,
    meeting_date: str,
    claim_text: str,
    board_info: dict,
    exhibit_dir: Path,
    pdf_name: str = "",
) -> str:
    """Build an HTML exhibit block with all page images."""
    pages = sorted(exhibit_dir.glob("page_*.png"))
    if not pages:
        return ""

    board_name = board_info.get("name", board_code)
    board_url  = board_info.get("url", "")

    # Format display date
    try:
        from datetime import datetime
        dt = datetime.strptime(meeting_date, "%Y-%m-%d")
        display_date = dt.strftime("%B %-d, %Y")
    except Exception:
        display_date = meeting_date

    # Determine which page is the highlight — it has yellow annotations drawn
    # on it during rendering. We pick by looking at which page image differs
    # most from neighbours (i.e. has annotations), but since we can't easily
    # detect that from Python here, we rely on the fact that the exhibits
    # pipeline saves the highlight page as the one with yellow text boxes.
    # Simplest heuristic: page that is most "yellow" (high R, high G, low B).
    highlight_page_num = None
    best_yellow = -1
    for p in pages:
        try:
            with Image.open(p) as img:
                rgb = img.convert("RGB")
                # Sample the image at a lower resolution for speed
                small = rgb.resize((80, 100), Image.LANCZOS)
                pixels = list(small.getdata())
                # Yellow = high R, high G, low B
                score = sum(
                    1 for r, g, b in pixels
                    if r > 220 and g > 200 and b < 120
                )
                if score > best_yellow:
                    best_yellow = score
                    highlight_page_num = int(p.stem.split("_")[1])
        except Exception:
            pass

    # Determine which pages to actually render
    total_doc_pages = len(pages)
    omitted_note = ""
    if total_doc_pages > MAX_PAGES_FULL:
        # Show highlight page ± CONTEXT_WINDOW, clamped to doc bounds
        hl_idx = highlight_page_num - 1 if highlight_page_num else 0
        start = max(0, hl_idx - CONTEXT_WINDOW)
        end   = min(total_doc_pages, hl_idx + CONTEXT_WINDOW + 1)
        pages_to_show = pages[start:end]
        omitted_note = (
            f'<div class="omitted-note">'
            f'Showing pages {pages_to_show[0].stem.split("_")[1]}–'
            f'{pages_to_show[-1].stem.split("_")[1]} of {total_doc_pages} '
            f'(highlight ± {CONTEXT_WINDOW} context pages). '
            f'Full document available at source URL below.'
            f'</div>'
        )
    else:
        pages_to_show = pages

    # Build page rows
    page_rows_html = []
    for p in pages_to_show:
        page_num = int(p.stem.split("_")[1])
        is_highlight = (page_num == highlight_page_num)

        # Convert to base64 JPEG
        try:
            b64 = png_to_b64_jpeg(p, JPEG_QUALITY)
        except Exception as e:
            print(f"    Warning: could not convert {p}: {e}")
            continue

        badge = ""
        border_class = "page-normal"
        if is_highlight:
            badge = '<span class="cited-badge">CITED</span>'
            border_class = "page-highlight"

        page_rows_html.append(f"""
        <div class="page-row {border_class}" id="exhibit-{exhibit_num}-page-{page_num}">
          <div class="page-label">Page {page_num} {badge}</div>
          <img class="page-img" src="data:image/jpeg;base64,{b64}" alt="Page {page_num}" loading="lazy" />
        </div>""")

    pages_html = "\n".join(page_rows_html)

    source_link = (f'<a href="{board_url}" target="_blank" rel="noopener">'
                   f'{board_url}</a>' if board_url else "<em>URL not available</em>")

    pdf_label = f"<strong>Source file:</strong> {pdf_name}" if pdf_name else ""

    return f"""
<div class="exhibit-block" id="exhibit-{exhibit_num}">
  <div class="exhibit-header">
    <span class="exhibit-number">Exhibit {exhibit_num}</span>
    <span class="exhibit-meta">{board_name} &nbsp;·&nbsp; {display_date}</span>
    {f'<span class="exhibit-pdf">{pdf_name}</span>' if pdf_name else ""}
  </div>

  <div class="exhibit-claim">
    <em>"{claim_text}"</em>
  </div>

  <div class="page-count-note">{total_doc_pages} page{"s" if total_doc_pages != 1 else ""} in source document · {len(pages_to_show)} shown</div>

  {omitted_note}

  <div class="pages-container">
    {pages_html}
  </div>

  <div class="exhibit-footer">
    <div class="source-link">
      <strong>Source:</strong> {source_link}
    </div>
    <a class="back-link" href="#top">&#8593; Back to report</a>
  </div>
</div>"""


# ── citation link replacement ─────────────────────────────────────────────────

def build_report_with_links(report_text: str, citations: list[dict], exhibit_map: dict) -> str:
    """Replace citation links with #exhibit-N anchors or plain text."""

    # Pattern matches: ([Board Label](/board/STATE/CODE#DATE))
    # We need to replace the full markdown link with either an anchor or plain text
    link_pattern = re.compile(
        r'\(\[([^\]]+)\]\(/board/(\w{2})/(\w+_\w+)#(\d{4}-\d{2}-\d{2})\)\)'
    )

    # Build lookup: (board_code, date) → (exhibit_num, has_pages)
    cite_lookup = {}
    for c in citations:
        key = (c["board_code"], c["meeting_date"])
        cite_lookup[key] = c["exhibit_number"]

    def replace_link(m):
        label     = m.group(1)
        board_code = m.group(3)
        date      = m.group(4)
        key = (board_code, date)
        exhibit_num = cite_lookup.get(key)

        if exhibit_num and exhibit_num in exhibit_map:
            # Has rendered pages — link to exhibit
            return f'(<a href="#exhibit-{exhibit_num}" class="exhibit-link">{label} →&nbsp;Ex.&nbsp;{exhibit_num}</a>)'
        else:
            # No pages — just show label without link
            return f'({label})'

    return link_pattern.sub(replace_link, report_text)


# ── HTML template ─────────────────────────────────────────────────────────────

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>National Medical Board Landscape Report — March 2026</title>
  <style>
    /* ── reset & base ── */
    *, *::before, *::after {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: Georgia, 'Times New Roman', serif;
      font-size: 17px;
      line-height: 1.75;
      color: #1a1a2e;
      background: #f4f6fb;
      margin: 0;
      padding: 0;
    }}

    /* ── layout ── */
    #top {{
      background: linear-gradient(135deg, #1e3a5f 0%, #2E4A6E 60%, #1a2d4a 100%);
      color: #fff;
      padding: 3rem 2rem 2.5rem;
      text-align: center;
    }}
    #top h1 {{
      font-size: 2.2rem;
      margin: 0 0 0.5rem;
      letter-spacing: -0.02em;
      font-weight: normal;
    }}
    #top .subtitle {{
      font-size: 1.05rem;
      color: #a8c4e0;
      margin: 0;
    }}
    #top .meta-row {{
      margin-top: 1.2rem;
      font-size: 0.9rem;
      color: #c0d4e8;
      display: flex;
      gap: 2rem;
      justify-content: center;
      flex-wrap: wrap;
    }}
    #top .meta-pill {{
      background: rgba(255,255,255,0.12);
      border-radius: 20px;
      padding: 0.25rem 0.85rem;
    }}

    /* ── nav strip ── */
    .toc-strip {{
      background: #2E4A6E;
      border-bottom: 3px solid #F7941D;
      padding: 0.7rem 2rem;
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
      align-items: center;
    }}
    .toc-strip a {{
      color: #e0eaf4;
      text-decoration: none;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.82rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      white-space: nowrap;
    }}
    .toc-strip a:hover {{ color: #F7941D; }}

    /* ── main content ── */
    .main-wrap {{
      max-width: 900px;
      margin: 0 auto;
      padding: 3rem 2rem;
    }}

    /* ── markdown typography ── */
    .report-body h1 {{ display: none; }}  /* title already in header */
    .report-body h2 {{
      font-size: 1.55rem;
      color: #2E4A6E;
      border-bottom: 2px solid #F7941D;
      padding-bottom: 0.4rem;
      margin: 2.8rem 0 1rem;
      font-weight: normal;
    }}
    .report-body h3 {{
      font-size: 1.2rem;
      color: #1e3a5f;
      margin: 2rem 0 0.6rem;
    }}
    .report-body h4 {{
      font-size: 1rem;
      color: #2E4A6E;
      margin: 1.5rem 0 0.4rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-family: 'Helvetica Neue', Arial, sans-serif;
    }}
    .report-body p {{
      margin: 0 0 1.2rem;
    }}
    .report-body ul, .report-body ol {{
      margin: 0 0 1.2rem;
      padding-left: 1.6rem;
    }}
    .report-body li {{ margin: 0.3rem 0; }}
    .report-body strong {{ color: #1e3a5f; }}
    .report-body em {{ color: #4a4a6a; }}
    .report-body hr {{
      border: none;
      border-top: 1px solid #d0d8e8;
      margin: 2rem 0;
    }}
    .report-body blockquote {{
      border-left: 4px solid #F7941D;
      margin: 1.2rem 0;
      padding: 0.5rem 1.2rem;
      background: #fdf7ee;
      border-radius: 0 6px 6px 0;
      color: #3a3a5a;
    }}

    /* ── exhibit citation links ── */
    a.exhibit-link {{
      color: #2563EB;
      text-decoration: none;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.82em;
      font-weight: 600;
      background: #eff4ff;
      border: 1px solid #b8ccf8;
      border-radius: 4px;
      padding: 0.1em 0.45em;
      white-space: nowrap;
      transition: background 0.15s;
    }}
    a.exhibit-link:hover {{
      background: #dbeafe;
      border-color: #2563EB;
    }}

    /* ── exhibits section heading ── */
    .exhibits-heading {{
      font-size: 1.9rem;
      color: #2E4A6E;
      border-bottom: 3px solid #F7941D;
      padding-bottom: 0.5rem;
      margin: 4rem 0 0.5rem;
      font-weight: normal;
    }}
    .exhibits-intro {{
      color: #4a5a7a;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.95rem;
      margin-bottom: 2.5rem;
    }}

    /* ── exhibit block ── */
    .exhibit-block {{
      background: #fff;
      border: 1px solid #dde4f0;
      border-radius: 10px;
      margin-bottom: 3rem;
      overflow: hidden;
      scroll-margin-top: 70px;
      box-shadow: 0 2px 12px rgba(46,74,110,0.08);
    }}

    .exhibit-header {{
      background: linear-gradient(90deg, #1e3a5f 0%, #2E4A6E 100%);
      color: #fff;
      padding: 1rem 1.4rem;
      display: flex;
      align-items: center;
      gap: 1.2rem;
      flex-wrap: wrap;
    }}
    .exhibit-number {{
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      background: #F7941D;
      color: #fff;
      padding: 0.2em 0.7em;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .exhibit-meta {{
      font-size: 1rem;
      font-weight: normal;
      color: #d0e4f8;
      font-family: 'Helvetica Neue', Arial, sans-serif;
    }}
    .exhibit-pdf {{
      font-size: 0.78rem;
      color: #a0bcd4;
      font-family: 'Courier New', monospace;
      margin-left: auto;
    }}

    .exhibit-claim {{
      padding: 1rem 1.4rem 0.6rem;
      color: #2a2a4a;
      font-size: 0.97rem;
      border-bottom: 1px solid #edf0f8;
      background: #f8fafd;
    }}

    .page-count-note {{
      padding: 0.4rem 1.4rem;
      font-size: 0.8rem;
      color: #6a7a9a;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      background: #f8fafd;
      border-bottom: 1px solid #edf0f8;
    }}

    /* ── omitted pages note ── */
    .omitted-note {{
      margin: 0 1.4rem 0;
      padding: 0.5rem 0.8rem;
      background: #fff8e6;
      border: 1px solid #f0d070;
      border-radius: 5px;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.8rem;
      color: #705010;
    }}

    /* ── page images ── */
    .pages-container {{
      padding: 1rem 1.4rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .page-row {{
      border-radius: 6px;
      overflow: hidden;
      border: 2px solid #e0e8f0;
    }}
    .page-row.page-highlight {{
      border-color: #F7941D;
      box-shadow: 0 0 0 3px rgba(247,148,29,0.2);
    }}
    .page-label {{
      background: #f0f4f8;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.75rem;
      font-weight: 600;
      color: #4a5a7a;
      padding: 0.3rem 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .page-row.page-highlight .page-label {{
      background: #fff7ec;
      color: #a05000;
    }}
    .cited-badge {{
      background: #F7941D;
      color: #fff;
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      padding: 0.1em 0.5em;
      border-radius: 3px;
    }}
    .page-img {{
      display: block;
      width: 100%;
      height: auto;
    }}

    /* ── exhibit footer ── */
    .exhibit-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.8rem 1.4rem;
      background: #f8fafd;
      border-top: 1px solid #edf0f8;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}
    .source-link {{
      font-size: 0.82rem;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      color: #4a5a7a;
      word-break: break-all;
    }}
    .source-link a {{
      color: #2563EB;
    }}
    .back-link {{
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.82rem;
      color: #2E4A6E;
      text-decoration: none;
      font-weight: 600;
    }}
    .back-link:hover {{ color: #F7941D; }}

    /* ── footer ── */
    .page-footer {{
      background: #1e3a5f;
      color: #7090b0;
      text-align: center;
      padding: 2rem;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 0.82rem;
      margin-top: 4rem;
    }}

    /* ── print ── */
    @media print {{
      .toc-strip, .back-link {{ display: none; }}
      .exhibit-block {{ page-break-inside: avoid; }}
    }}

    /* ── responsive ── */
    @media (max-width: 600px) {{
      #top h1 {{ font-size: 1.5rem; }}
      .main-wrap {{ padding: 1.5rem 1rem; }}
      .exhibit-header {{ gap: 0.6rem; }}
      .exhibit-pdf {{ display: none; }}
    }}
  </style>
</head>
<body id="top">

<header id="top">
  <h1>National Medical Board Landscape Report</h1>
  <p class="subtitle">AI-synthesized intelligence from 34 state medical boards · 270+ documented meetings</p>
  <div class="meta-row">
    <span class="meta-pill">Date: March 31, 2026</span>
    <span class="meta-pill">States: 27 + DC</span>
    <span class="meta-pill">Exhibits: {exhibit_count}</span>
    <span class="meta-pill">Generated by BoardPulse</span>
  </div>
</header>

<nav class="toc-strip">
  <a href="#top">&#8679; Top</a>
  <a href="#section-app">APP Scope</a>
  <a href="#section-imlc">IMLC</a>
  <a href="#section-ai">AI</a>
  <a href="#section-telehealth">Telehealth</a>
  <a href="#section-opioid">Opioids</a>
  <a href="#section-wellness">Wellness</a>
  <a href="#section-trauma">Trauma-Informed</a>
  <a href="#section-exhibits" style="color:#F7941D;font-weight:700;">&#8595; Exhibits</a>
</nav>

<div class="main-wrap">

<div class="report-body">
{report_html}
</div>

<h2 class="exhibits-heading" id="section-exhibits">Source Exhibits</h2>
<p class="exhibits-intro">
  The following exhibits show full source documents from state medical board meeting minutes.
  Each document was retrieved from the board's public website. Highlighted pages (gold border)
  contain the content cited in the report above. Pages shown in each exhibit are rendered
  directly from the original PDF at 150 dpi.
</p>

{exhibits_html}

</div>

<footer class="page-footer">
  BoardPulse · National Medical Board Intelligence · Generated 2026-03-31<br/>
  Source documents retrieved from publicly available state medical board meeting records.
</footer>

</body>
</html>
"""


# ── main ──────────────────────────────────────────────────────────────────────

async def main():
    print("=" * 60)
    print("Building national report with exhibits")
    print("=" * 60)

    # 1. Load board metadata
    print("\n1. Loading board database...")
    board_map = await get_board_map()
    print(f"   {len(board_map)} boards loaded")

    # 2. Parse citations from report
    print("\n2. Parsing citations from report...")
    citations = parse_report_citations(REPORT_MD)
    print(f"   {len(citations)} unique citations found")

    # 3. Determine which citations have rendered exhibit pages
    exhibit_map = {}   # exhibit_num → metadata
    for c in citations:
        board_code  = c["board_code"]
        exhibit_num = c["exhibit_number"]
        exhibit_dir = EXHIBITS_DIR / board_code / f"exhibit_{exhibit_num:03d}"
        pages = sorted(exhibit_dir.glob("page_*.png"))
        if pages:
            exhibit_map[exhibit_num] = {
                "board_code":  board_code,
                "meeting_date": c["meeting_date"],
                "claim_text":   c["claim_text"],
                "exhibit_dir":  exhibit_dir,
                "pages":        pages,
                "board_info":   board_map.get(board_code, {"name": board_code, "url": ""}),
            }

    print(f"   {len(exhibit_map)} exhibits have rendered pages")

    # 4. Build report HTML with replaced citation links
    print("\n3. Converting report markdown to HTML...")
    report_text = REPORT_MD.read_text(encoding="utf-8")
    report_with_anchors = build_report_with_links(report_text, citations, exhibit_map)

    # Add id anchors to section headings for nav links
    section_anchors = {
        "Advanced Practice Provider": "section-app",
        "Interstate Medical Licensure Compact": "section-imlc",
        "Artificial Intelligence": "section-ai",
        "Telehealth": "section-telehealth",
        "Controlled Substances": "section-opioid",
        "Physician Wellness": "section-wellness",
        "Trauma-Informed": "section-trauma",
        "Regional Patterns": "section-regional",
        "FSMB Engagement": "section-fsmb",
        "Conclusions": "section-conclusions",
    }

    # Convert markdown → HTML
    md_extensions = ["extra", "tables", "toc", "sane_lists"]
    report_html = markdown.markdown(report_with_anchors, extensions=md_extensions)

    # Inject section anchors into headings
    for keyword, anchor_id in section_anchors.items():
        pattern = re.compile(
            rf'(<h[23][^>]*>)(.*?{re.escape(keyword)}.*?)(</h[23]>)',
            re.IGNORECASE,
        )
        def inject_id(m, aid=anchor_id):
            # Don't double-inject
            if 'id=' in m.group(1):
                return m.group(0)
            tag_open = m.group(1).replace("<h", f'<h').replace(">", f' id="{aid}">', 1)
            return tag_open + m.group(2) + m.group(3)
        report_html = pattern.sub(inject_id, report_html, count=1)

    print("   Done.")

    # 5. Build exhibit blocks
    print(f"\n4. Building {len(exhibit_map)} exhibit blocks (encoding images)...")
    exhibit_blocks = []
    total_pages_included = 0

    for exhibit_num in sorted(exhibit_map.keys()):
        meta = exhibit_map[exhibit_num]
        board_code   = meta["board_code"]
        exhibit_dir  = meta["exhibit_dir"]
        pages        = meta["pages"]

        print(f"   Exhibit {exhibit_num:3d}: {board_code} {meta['meeting_date']} "
              f"— {len(pages)} pages", end="", flush=True)

        # Find PDF name from parent board exhibit directory (thumbnail filename)
        pdf_name = ""
        board_dir = EXHIBITS_DIR / board_code
        thumbnail_candidates = sorted(board_dir.glob(f"exhibit_{exhibit_num:03d}_*.png"))
        if thumbnail_candidates:
            # Filename pattern: exhibit_013_2026-03-19.png → infer date
            pdf_name = thumbnail_candidates[0].stem.replace(f"exhibit_{exhibit_num:03d}_", "")

        block = build_exhibit_block(
            exhibit_num   = exhibit_num,
            board_code    = board_code,
            meeting_date  = meta["meeting_date"],
            claim_text    = meta["claim_text"],
            board_info    = meta["board_info"],
            exhibit_dir   = exhibit_dir,
            pdf_name      = pdf_name,
        )
        exhibit_blocks.append(block)
        total_pages_included += len(pages)
        print(" ✓")

    exhibits_html = "\n".join(exhibit_blocks)

    # 6. Assemble full HTML
    print("\n5. Assembling final HTML...")
    final_html = HTML_TEMPLATE.format(
        exhibit_count=len(exhibit_map),
        report_html=report_html,
        exhibits_html=exhibits_html,
    )

    # 7. Write output
    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(final_html, encoding="utf-8")

    size_mb = OUTPUT_HTML.stat().st_size / (1024 * 1024)
    print(f"\n{'=' * 60}")
    print(f"Output: {OUTPUT_HTML}")
    print(f"Size:   {size_mb:.2f} MB ({OUTPUT_HTML.stat().st_size:,} bytes)")
    print(f"Exhibits included: {len(exhibit_map)}")
    print(f"Total pages rendered: {total_pages_included}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    asyncio.run(main())
