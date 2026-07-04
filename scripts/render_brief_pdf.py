#!/usr/bin/env python3
"""Render a monthly delta brief's email HTML to a Letter-size PDF (offline).

Models on Projects/regulaitor/scripts/render_poster.py: launch a headless
Chromium, navigate to the local file:// URL, and use page.pdf() with
print_background=True. No network — the brief HTML is fully self-contained
(inline CSS + inline SVG, no CDN), so this renders deterministically offline.

Usage:
    python scripts/render_brief_pdf.py [YYYY-MM]

With no argument, renders the most recent brief on disk. The input is
data/reports/briefs/YYYY-MM.html (produced by
`app/reports/brief.ingest_brief_prose`), and the output is written next to it
as YYYY-MM.pdf.
"""
import asyncio
import sys
from pathlib import Path

# Make `app` importable when run as a bare script from the project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.reports.brief import BRIEFS_DIR, latest_brief_ym  # noqa: E402


async def render(ym: str) -> Path:
    html_path = BRIEFS_DIR / f"{ym}.html"
    if not html_path.exists():
        raise FileNotFoundError(
            f"Brief HTML not found: {html_path}. "
            f"Run `python cli.py brief --ingest` first to generate it."
        )
    pdf_path = BRIEFS_DIR / f"{ym}.pdf"

    from playwright.async_api import async_playwright

    file_url = f"file:///{html_path.resolve().as_posix()}"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            page = await browser.new_page()
            await page.goto(file_url)
            await page.wait_for_load_state("networkidle")
            # Brief up-front: give inline SVG/layout a beat to settle.
            await asyncio.sleep(0.5)
            await page.pdf(
                path=str(pdf_path),
                format="Letter",
                print_background=True,
                margin={"top": "0.5in", "right": "0.5in",
                        "bottom": "0.5in", "left": "0.5in"},
            )
        finally:
            await browser.close()

    return pdf_path


def main() -> int:
    ym = sys.argv[1] if len(sys.argv) > 1 else latest_brief_ym()
    if not ym:
        print("No brief found. Run `python cli.py brief` first.", file=sys.stderr)
        return 1
    pdf_path = asyncio.run(render(ym))
    print(f"[OK] Brief PDF: {pdf_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
