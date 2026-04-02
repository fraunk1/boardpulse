"""boardpulse configuration."""
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
SCREENSHOTS_DIR = DATA_DIR / "screenshots"
DOCUMENTS_DIR = DATA_DIR / "documents"
REPORTS_DIR = DATA_DIR / "reports"
EXHIBITS_DIR = DATA_DIR / "exhibits"
PAGES_DIR = DATA_DIR / "pages"
DB_PATH = PROJECT_ROOT / "boardpulse.db"

# Database
DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH}"

# Scraping
SCRAPE_DELAY_SECONDS = 2.0
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# FSMB
FSMB_CONTACT_URL = "https://www.fsmb.org/contact-a-state-medical-board/"

# Ensure data directories exist
for d in [SCREENSHOTS_DIR, DOCUMENTS_DIR, REPORTS_DIR, EXHIBITS_DIR, PAGES_DIR]:
    d.mkdir(parents=True, exist_ok=True)
