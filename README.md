# boardpulse

**State Medical Board Intelligence Platform**

boardpulse collects, indexes, and analyzes meeting minutes from state medical boards across the United States. It downloads the actual documents (PDFs), generates AI summaries with topic tags, and presents everything through a Palantir-style drill-down intelligence interface.

![National Overview](docs/screenshots/national-overview.png)

## What It Does

- **Collects** meeting minutes, agendas, and documents from 63 state medical boards (51 states + DC, MD and DO boards)
- **Downloads** the actual PDF documents — not just metadata
- **Summarizes** meetings and extracts structured facts using Claude Code subagents behind deterministic quality gates, with topic tagging
- **Generates** a national landscape report with citations linking to source documents
- **Renders** exhibit pages from cited PDFs with highlighted evidence passages

## Dashboard

The web dashboard provides a drill-down intelligence interface:

**National Overview** — coverage map, topic intelligence grid, key metrics, recent activity feed

**State Drill-Down** — board cards with meeting counts, document coverage, topic breakdown

![State Drill-Down](docs/screenshots/state-drilldown.png)

**Board Detail** — meeting timeline with document badges, expandable AI summaries

![Board Detail](docs/screenshots/board-detail.png)

**Topic Intelligence** — cross-board analysis by topic (licensing, telehealth, AI, disciplinary, etc.)

![Topic Intelligence](docs/screenshots/topic-intelligence.png)

**Meeting Detail** — embedded PDF viewer with tabbed documents, AI summary, source exhibits

![Meeting Detail](docs/screenshots/meeting-detail.png)

## Coverage

| Metric | Count |
|--------|-------|
| Boards monitored | 63 |
| Boards with documents | 61 |
| Meetings tracked | ~1,933 (back to 2021) |
| Documents on file | ~2,677 |
| Topics tracked | 15 |
| States covered | 46 |

## Quick Start

```bash
# Clone and set up
cd Projects/boardpulse
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium

# Re-scrape everything — the one command to run any time (incremental,
# idempotent, prints a per-board diff of what changed)
python refresh.py
python refresh.py --include-headed   # also run WAF boards (visible windows)
python refresh.py --board TX_MD      # one board only

# Start the dashboard
python cli.py serve
# → http://localhost:8099

# Run collection for a specific board
python cli.py collect --board AL_MD

# Generate AI summaries — prepares a prompt bundle, then a Claude Code subagent
# writes the summary and --ingest gates it into the DB (see SUMMARIZE.md)
python cli.py summarize --board AL_MD
python cli.py summarize --ingest       # gate + store summaries (exits 1 on any reject)
python cli.py summarize --archive      # back-history prompts for the 36-month view

# Extract structured facts (policy actions, legislation, discipline, emerging topics)
python cli.py facts --board AL_MD      # prep the fact-extraction prompt(s)
python cli.py facts --ingest           # gate + store facts JSON (exits 1 on any reject)
python cli.py facts --status           # per-board facts coverage

# Monthly delta brief ("what changed") + the /briefs page
python cli.py brief                     # compute the brief + writer prompt
python cli.py brief --ingest            # splice the two prose slots + build email HTML
python cli.py brief --pdf               # render the brief to a Letter PDF

# Generate national landscape report
python cli.py summarize --national

# Gold-standard model eval (proves a model still produces gate-valid summaries)
python cli.py eval prepare
python cli.py eval score <run> --model-label <model>

# Diagnostics
python cli.py coverage            # totals + per-board coverage
python cli.py boards              # coverage buckets + 63/63 done-math
python cli.py qa                  # data-quality audit
python cli.py ledger list         # verified no-minutes / blocked boards

# Reset + re-collect a board after fixing its URL or the collector
python _recollect.py TX_MD
```

## Architecture

```
boardpulse/
├── app/
│   ├── web/              # FastAPI dashboard (Jinja2 + HTMX + Alpine.js + Tailwind)
│   │   ├── server.py     # Routes: /, /state/, /board/, /meeting/, /topic/, /report
│   │   ├── templates/    # national, state, board, meeting, topic, exhibit, report
│   │   └── static/       # CSS + US map SVG
│   ├── scraper/          # Playwright-based collectors
│   │   ├── collector.py  # Main collection pipeline
│   │   ├── boards.py     # Board seed data (63 boards)
│   │   └── discoverer.py # Minutes URL discovery
│   ├── extractor/        # AI processing (prompt prep + gated ingest)
│   │   ├── summarizer.py # Per-board summary prompt bundles + gated ingest
│   │   ├── facts.py      # Structured-fact prompt chunks + gated ingest
│   │   ├── exhibits.py   # PDF page rendering with highlights
│   │   └── prompts.py    # Summary generation prompts
│   ├── quality/          # The deterministic quality layer
│   │   ├── gates.py      # Ingest gates (structure, citations, verbatim quotes)
│   │   ├── taxonomy.py   # Controlled vocabularies (single source of truth)
│   │   └── evalharness.py# Gold-standard model eval (prepare / score / judge)
│   ├── reports/
│   │   └── brief.py      # Monthly delta brief (build / ingest prose / PDF)
│   ├── web/
│   │   └── trends.py     # /trends charts + watchlist queries
│   ├── models.py         # SQLAlchemy models (Board, Meeting, MeetingDocument,
│   │                     #   PolicyAction, LegislationMention, DisciplinaryAction,
│   │                     #   EmergingTopic, WatchlistTerm)
│   ├── database.py       # Async SQLite (aiosqlite + WAL mode)
│   └── config.py         # Paths and settings
├── data/
│   ├── documents/        # Downloaded PDFs organized by board code
│   ├── screenshots/      # Board website screenshots
│   ├── reports/          # Per-board + national prompts and summaries
│   │   ├── facts/        # Fact-extraction prompts + JSON output
│   │   ├── archive/      # Back-history (out-of-window) summary prompts
│   │   └── briefs/       # Monthly delta briefs (md / json / html / pdf)
│   ├── examples/         # Few-shot worked examples injected into prompts
│   │   └── facts/        # Hand-verified fact-extraction examples
│   ├── gold/             # Frozen gold summary set + eval scorecards
│   └── exhibits/         # Rendered exhibit page images
├── SUMMARIZE.md          # Summary + facts + brief dispatch guide (model presets)
├── FACTS.md              # Structured-fact extraction dispatch guide
├── cli.py                # CLI entry point
├── recollect_docs.py     # Aggressive document recollector
└── boardpulse.db         # SQLite database
```

## Tech Stack

- **Backend**: FastAPI + SQLAlchemy 2.0 + aiosqlite
- **Frontend**: Jinja2 + HTMX + Alpine.js + Tailwind CSS
- **Icons**: Lucide
- **Scraping**: Playwright (headless Chromium)
- **AI**: Claude Code subagents produce summaries and structured facts behind deterministic quality gates (model-preset based — see SUMMARIZE.md)
- **PDF Processing**: PyMuPDF (exhibit rendering)
- **Database**: SQLite (WAL mode)

## Topics Tracked

The AI summarization pipeline extracts and tags meetings with these topics:

`licensing` `disciplinary` `telehealth` `scope-of-practice` `rulemaking` `legislation` `opioids` `controlled-substances` `patient-safety` `physician-wellness` `AI` `CME` `IMLC` `workforce` `public-health`

## License

Internal project — FSMB Federation of State Medical Boards.
