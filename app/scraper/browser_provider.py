"""
Browser provider — Lightpanda-first with Chromium fallback.

Tries to connect to a running Lightpanda instance via CDP.
Falls back to launching Chromium if Lightpanda is unavailable
or the site is in the CHROMIUM_ONLY blocklist.

Usage:
    from browser_provider import launch_browser

    async with async_playwright() as pw:
        browser, context, page = await launch_browser(pw, site_id="GA")
"""

LIGHTPANDA_URL = "ws://127.0.0.1:9222"

# Sites that must use Chromium (add state codes or adapter names as needed).
# Use this when a site breaks on Lightpanda due to missing Web APIs or crashes.
CHROMIUM_ONLY: set[str] = set()


async def launch_browser(pw, *, site_id: str = "", headless: bool = True, slow_mo: int = 0):
    """Launch a browser — Lightpanda via CDP if available, else Chromium.

    Args:
        pw: Playwright instance (from async_playwright().__aenter__())
        site_id: Identifier for the target site (state code like "GA" or
                 adapter name like "seek"). Checked against CHROMIUM_ONLY.
        headless: Run Chromium in headless mode (ignored for Lightpanda).
        slow_mo: Milliseconds delay between Chromium actions (ignored for Lightpanda).

    Returns:
        (browser, context, page) tuple — same interface regardless of backend.
    """
    # Try Lightpanda unless this site is blocklisted
    if site_id not in CHROMIUM_ONLY:
        try:
            browser = await pw.chromium.connect_over_cdp(LIGHTPANDA_URL)
            browser._is_lightpanda = True
            context = browser.contexts[0] if browser.contexts else await browser.new_context()
            page = await context.new_page()
            return browser, context, page
        except Exception:
            pass  # Lightpanda not running or crashed — fall back to Chromium

    # Chromium fallback
    browser = await pw.chromium.launch(headless=headless, slow_mo=slow_mo)
    browser._is_lightpanda = False
    context = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 900},
    )
    page = await context.new_page()
    return browser, context, page


def is_lightpanda(browser) -> bool:
    """Check if the browser was connected via CDP (Lightpanda) vs launched (Chromium).

    Uses the _is_lightpanda flag set by launch_browser(). Returns False for
    browsers not created by launch_browser().
    """
    return getattr(browser, "_is_lightpanda", False)
