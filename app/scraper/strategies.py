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
STRATEGIES: dict[str, BoardStrategy] = {
    # Iowa DIAL hosts ALL Iowa boards' meetings on one page, with minutes as
    # Google Drive links. Rows use board ACRONYMS — the medicine board is
    # "IBM" (e.g. "IBM Minutes 5/2/25"), not "Board of Medicine".
    "IA_MD": BoardStrategy(filter_text="IBM"),

    # Nebraska DHHS hosts EVERY profession's agendas/minutes on one page
    # (chiropractic, dentistry, APRN, veterinary...). Medicine & Surgery
    # rows/files carry "med" filename slugs (050826medagenda.pdf) or the
    # board name; without this filter 141/142 collected docs were other
    # professions'.
    # NOTE: med(?!rad) — Nebraska ALSO has a "Board of Medical Radiography"
    # whose files are NNNNNNmedrad*.pdf; a plain med[a-z]* matched them.
    "NE_MD": BoardStrategy(
        filter_text=r"(\d{6}med(?!rad)[a-z]*\.pdf|medicine\s*(and|&)\s*surgery)"),

    # Depth-1 boards: the index lists meetings; PDFs live on detail pages.
    # TX front page shows only UPCOMING events; past meetings (the ones with
    # minutes) live on ?page=1..3. The events calendar mixes ALL boards under
    # the TMB umbrella (acupuncture, respiratory care, radiologic tech, PA)
    # — keep only Medical Board rows. filter_text is a regex.
    "TX_MD": BoardStrategy(depth=1, paginate=4,
                           filter_text=r"medical\s+board"),
    "FL_MD": BoardStrategy(depth=1),
    "FL_DO": BoardStrategy(depth=1),
    "UT_MD": BoardStrategy(depth=1),   # utah.gov/pmn notice pages
    "NM_MD": BoardStrategy(depth=1),
    # mn.gov and commerce.alaska.gov serve an EMPTY page to headless browsers
    # (0 links rendered) — need a visible window like the WAF boards.
    "MN_MD": BoardStrategy(depth=1, headed=True),
    "DE_MD": BoardStrategy(depth=1),   # publicmeetings.delaware.gov SPA
    "AK_MD": BoardStrategy(depth=1, headed=True),
    "RI_MD": BoardStrategy(depth=1),   # OpenGov dashboard (attempt)
    "WA_MD": BoardStrategy(depth=1, paginate=3),
    # oregon.gov renders its minutes list only for real interactive sessions
    "OR_MD": BoardStrategy(depth=1, headed=True),

    # Headed Chromium: WAF-fronted sites that 403 headless/automated fetches
    # (this trick beat the KS/NH Akamai WAF in a prior incarnation). These
    # boards are skipped by unattended refresh runs (window pops up).
    "CO_MD": BoardStrategy(headed=True, depth=1),
    "KS_MD": BoardStrategy(headed=True, depth=1),
    "NH_MD": BoardStrategy(headed=True),
    "AZ_DO": BoardStrategy(headed=True),
    # mass.gov Akamai rejects both httpx and headless context.request
    "MA_MD": BoardStrategy(headed=True),

    # No usable index page — probe guessable dated URLs (url_probe.py)
    "NJ_MD": BoardStrategy(url_probes=(
        "https://www.njconsumeraffairs.gov/bme/Agendas/bme-agenda-%m%d%y.pdf",
    )),
    "TN_MD": BoardStrategy(url_probes=(
        "https://www.tn.gov/content/dam/tn/health/healthprofboards/"
        "medicalexaminers/BMEMIN%m%d%y.pdf",
    )),
    "MO_MD": BoardStrategy(url_probes=(
        "https://pr.mo.gov/boards/healingarts/meetings/%Y-%m-%d-Minutes.pdf",
        "https://pr.mo.gov/boards/healingarts/meetings/%Y-%m-%d-Notice.pdf",
    )),
}


def get_strategy(code: str) -> BoardStrategy:
    """Return the board's strategy, or the inert DEFAULT when absent."""
    return STRATEGIES.get(code, DEFAULT)


def chromium_only_codes() -> set[str]:
    """Boards that must skip Lightpanda (headed or explicit chromium)."""
    return {
        code for code, s in STRATEGIES.items()
        if s.headed or s.browser == "chromium"
    }
