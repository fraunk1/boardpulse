#!/usr/bin/env python3
"""Capture verification screenshots of the running dashboard (headless Chromium).

Reliable alternative to the preview tool's screenshot (which stalls on this
page's idle-wait). Writes PNGs to data/_verify/.
"""
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8099"
OUT = Path(__file__).resolve().parent / "data" / "_verify"
OUT.mkdir(parents=True, exist_ok=True)

PAGES = {
    "01-dashboard": "/",
    "02-national-report": "/report",
    "03-board-OH": "/board/OH/OH_MD",
    "04-topic-AI": "/topic/AI",
}


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        for name, path in PAGES.items():
            try:
                await page.goto(BASE + path, wait_until="load", timeout=20000)
            except Exception as e:
                print(f"{name}: goto warning: {e}")
            await page.wait_for_timeout(2500)
            dest = OUT / f"{name}.png"
            await page.screenshot(path=str(dest), full_page=True)
            print(f"{name}  {path}  -> {dest.name}")
        await browser.close()
    print(f"\nScreenshots in: {OUT}")


if __name__ == "__main__":
    asyncio.run(main())
