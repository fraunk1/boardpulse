"""Per-board collection strategies.

Most boards work with the default collector behavior. Boards whose sites need
special handling (WAF bypass, deeper crawls, odd document-link shapes) get an
entry in STRATEGIES. Boards WITHOUT an entry get DEFAULT, which is inert —
their collection path is byte-identical to the stock collector. That contract
is pinned by tests/test_strategies.py::test_default_strategy_is_inert.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class BoardStrategy:
    """Knobs for one board's collection behavior. All defaults = stock path."""

    # Launch a visible (non-headless) Chromium for this board. Bypasses
    # Akamai-class WAFs that block headless fetches (proven on KS/NH).
    # Implies the Chromium path (Lightpanda has no headed mode).
    headed: bool = False

    # "chromium" forces the real-Chromium fallback even if Lightpanda is
    # running — required for boards whose documents must be downloaded
    # through the browser session (context.request over Lightpanda CDP
    # does not reliably share cookies).
    browser: str | None = None

    # 1 = after harvesting the index page, visit dated links that are NOT
    # documents and harvest doc links from those detail pages (attributed
    # to the parent link's date).
    depth: int = 0

    # Regexes (Python re, searched against the absolute href) that force
    # isDoc=True for links the extension/pattern heuristics miss.
    include_patterns: tuple[str, ...] = ()

    # Keep only links whose combined date-context text contains this
    # (case-insensitive) — for multi-board index pages like Iowa DIAL.
    filter_text: str | None = None

    # strftime URL templates probed against known/expected meeting dates
    # for boards with no usable index page (e.g. NJ agenda filenames).
    url_probes: tuple[str, ...] = ()

    # Follow ?page=2..N pagination on the index page.
    paginate: int = 0


DEFAULT = BoardStrategy()

# Populated task-by-task in Wave 3 (T3–T7). Codes must exist in seed_data.
STRATEGIES: dict[str, BoardStrategy] = {}


def get_strategy(code: str) -> BoardStrategy:
    """Return the board's strategy, or the inert DEFAULT when absent."""
    return STRATEGIES.get(code, DEFAULT)


def chromium_only_codes() -> set[str]:
    """Boards that must skip Lightpanda (headed or explicit chromium)."""
    return {
        code for code, s in STRATEGIES.items()
        if s.headed or s.browser == "chromium"
    }
