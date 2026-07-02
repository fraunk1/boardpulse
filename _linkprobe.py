#!/usr/bin/env python3
"""Diagnose why a board's minutes page yields 0 documents.

Loads each given board's minutes_url, expands year accordions (same as the
collector), then dumps the links that LOOK like minutes/agendas but were NOT
classified as downloadable docs (no .pdf/.docx/... extension) — i.e. the ones
the collector silently skips.

Usage: python _linkprobe.py GA_MD TX_MD VA_MD UT_MD
"""
import asyncio
import re
import sqlite3
import sys
from pathlib import Path

from playwright.async_api import async_playwright

DB = Path(__file__).resolve().parent / "boardpulse.db"
DOC_EXTS = (".pdf", ".docx", ".doc", ".xlsx", ".xls")

EXTRACT_JS = """() => Array.from(document.querySelectorAll('a[href]')).map(a => ({
    href: a.href || '',
    text: (a.innerText || a.textContent || '').trim().slice(0, 80)
}))"""


def url_for(code):
    con = sqlite3.connect(DB)
    row = con.execute("SELECT minutes_url FROM boards WHERE code=?", (code,)).fetchone()
    con.close()
    return row[0] if row else None


async def probe(code, page):
    url = url_for(code)
    print(f"\n===== {code} =====\n{url}")
    if not url:
        print("  (no url)")
        return
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(2.5)
    except Exception as e:
        print(f"  LOAD FAILED: {e}")
        return
    # expand year accordions like the collector does
    for yr in ("2026", "2025"):
        try:
            loc = page.locator("button, summary, [role='button'], a, li, div, span").filter(
                has_text=re.compile(rf"^\s*{yr}\s*$"))
            for i in range(min(await loc.count(), 12)):
                try:
                    await loc.nth(i).click(timeout=1500)
                    await asyncio.sleep(0.3)
                except Exception:
                    pass
        except Exception:
            pass
    links = await page.evaluate(EXTRACT_JS)
    is_doc = [l for l in links if l["href"].split("?")[0].split("#")[0].lower().endswith(DOC_EXTS)]
    kw = re.compile(r"minute|agenda|meeting|packet|board", re.I)
    candidates = [l for l in links if not (l["href"].split("?")[0].lower().endswith(DOC_EXTS))
                  and kw.search(l["text"] + " " + l["href"])]
    print(f"  total links={len(links)}  isDoc(.pdf/.docx/...)={len(is_doc)}  "
          f"keyword-but-not-doc={len(candidates)}")
    print("  -- sample of skipped minute/agenda links (text -> href) --")
    seen = set()
    for l in candidates[:12]:
        if l["href"] in seen:
            continue
        seen.add(l["href"])
        print(f"    \"{l['text']}\"  ->  {l['href'][:120]}")


async def main():
    codes = sys.argv[1:] or ["GA_MD", "TX_MD", "VA_MD", "UT_MD"]
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 900})
        for code in codes:
            await probe(code, page)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
