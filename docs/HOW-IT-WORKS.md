# How boardpulse Works — A Complete Process Guide

> boardpulse is a tool that collects, reads, organizes, and searches meeting minutes from every state medical board in the United States. Think of it like a search engine, but only for what medical boards are talking about.

---

## The Big Picture

There are 63 medical boards across all 50 states plus DC (some states have separate boards for MDs and DOs). Each board holds regular meetings — usually monthly — and publishes minutes (written records of what happened). These minutes are scattered across 63 different websites, in different formats, with different layouts.

boardpulse visits all of these websites, downloads the minutes, reads them, figures out what topics they cover, and puts everything into a searchable dashboard. Here's how each step works:

---

## Step 1: Know Where to Look (Seed + Bootstrap)

**What happens:** We build a directory of all 63 boards — their names, states, websites, and where their meeting minutes live.

**Where the data comes from:**
- A built-in list of all 63 boards (`app/scraper/seed_data.py`) with their official names, state codes (like `TX_MD` for Texas Medical Board), and homepage URLs
- The FSMB "Contact a Board" page (`fsmb.org/contact-a-state-medical-board/`) which has phone numbers, addresses, and links for every board

**How it's processed:**
- `python cli.py seed` loads the 63 boards into the SQLite database
- `python cli.py bootstrap` scrapes the FSMB contact page to fill in phone numbers, emails, and addresses

**What's stored:** A `boards` table in the database with one row per board (63 total).

**Command:** `python cli.py seed` then `python cli.py bootstrap`

---

## Step 2: Find the Minutes Pages (Discover)

**What happens:** For each board, we figure out which page on their website has the meeting minutes.

**Where the data comes from:** Each board's official website. Some boards have an obvious "Meeting Minutes" link. Others bury it under "About Us > Board Meetings > Archives."

**How it's processed:**
1. A browser (Playwright/Chromium) visits the board's homepage
2. It takes a screenshot of the page (saved to `data/screenshots/`)
3. It scans all the links on the page and scores them for relevance — links containing words like "minutes," "meetings," "agendas," "archives" score higher (`app/scraper/discoverer.py`)
4. The highest-scoring link is saved as the board's `minutes_url`
5. For boards where auto-discovery fails, URLs were found manually by a human

**What's stored:** The `minutes_url` column on each board record, plus discovery screenshots.

**Command:** `python cli.py discover`

---

## Step 3: Collect the Minutes (Collect)

**What happens:** We visit each board's minutes page, find all the meeting entries, and download the PDF/document files.

**Where the data comes from:** The `minutes_url` for each board. These pages typically list meetings by date with links to PDF files (minutes, agendas, attachments).

**How it's processed:**
1. A browser visits the board's minutes page
2. The collector (`app/scraper/collector.py`) parses the HTML to find:
   - **Meeting dates** — parsed from text using 8+ date format patterns (boards use everything from "March 15, 2026" to "03/15/26" to "2026-03-15")
   - **Document links** — PDF, DOCX, or HTML links near each date
   - **Document types** — classified as "minutes," "agenda," "notice," or "attachment" based on filename/link text
3. For each meeting found, a `meetings` row is created in the database
4. For each document link, the file is downloaded to `data/documents/{board_code}/` and a `meeting_documents` row is created
5. Collection looks back 24 months to catch boards that are slow to post

**What's stored:**
- `meetings` table — one row per meeting (date, title, board, type)
- `meeting_documents` table — one row per downloaded file (filename, file_path, source_url, doc_type)
- Actual PDF/document files in `data/documents/` (organized by board code)

**Command:** `python cli.py collect` (all boards) or `python cli.py collect --board TX_MD` (one board)

---

## Step 4: Read the Documents (Extract)

**What happens:** We extract the readable text from every downloaded PDF so we can search and classify it.

**Where the data comes from:** The PDF files sitting in `data/documents/`.

**How it's processed:**
1. The extractor (`app/extractor/extract.py`) loops through every document in the database
2. For PDFs: Uses PyMuPDF (a Python library) to extract all text from every page
3. For HTML files: Strips out navigation, scripts, and formatting to get clean text
4. The extracted text is saved back to the database on the document's `content_text` column

**What's stored:** The `content_text` column on each `meeting_documents` row — plain text version of the document.

**Tools used:** PyMuPDF (`fitz` library) for PDFs, BeautifulSoup for HTML

**Command:** `python cli.py extract`

---

## Step 5: Classify by Topic (Classify)

**What happens:** We read the extracted text and figure out what topics each document covers — things like "Discipline," "Telehealth," "Licensing," "AI & Technology."

**Where the data comes from:** The `content_text` stored in Step 4.

**How it's processed:**
1. The classifier (`app/pipeline/classifier.py`) has 16 topic categories, each with keyword patterns:
   - **Licensing** — matches words like "license," "renewal," "endorsement," "reciprocity"
   - **Discipline** — matches "consent order," "suspended," "probation," "misconduct"
   - **Telehealth** — matches "telehealth," "telemedicine," "virtual care"
   - **AI & Technology** — matches "artificial intelligence," "machine learning," "AI"
   - ... and 12 more topics
2. For each document, the classifier counts how many times each topic's keywords appear
3. If a topic's keywords appear 2+ times, that topic is assigned to the document
4. Topics "roll up" — if a document has ["Discipline", "Telehealth"], the meeting it belongs to gets those topics too. This means you can search at the meeting level.

**The 16 topics:**
AI & Technology, Board Operations, Budget & Finance, Continuing Education, Discipline, Ethics, Interstate Compact, Legal, Licensing, Opioids & Prescribing, Patient Safety, Public Health, Rulemaking, Scope of Practice, Telehealth, Workforce

**What's stored:**
- `topics` column on `meeting_documents` — list of matched topics per document
- `topics` column on `meetings` — union of all document topics for that meeting
- `topics` column on `document_pages` — per-page topic tags

**Command:** `python cli.py classify` (documents) or `python cli.py classify --pages` (page-level)

---

## Step 6: Render Every Page as an Image (Render)

**What happens:** Every page of every PDF gets converted into a PNG image — both a full-size version (for viewing) and a small thumbnail (for search results).

**Where the data comes from:** The PDF files in `data/documents/`.

**How it's processed:**
1. The renderer (`app/pipeline/renderer.py`) opens each PDF with PyMuPDF
2. For each page:
   - Renders at 150 DPI as a full-size PNG (clear enough to read)
   - Renders a ~200px wide thumbnail
3. Images are saved to `data/pages/{board_code}/{document_id}/page_001.png` (and `page_001_thumb.png`)
4. A `document_pages` row is created in the database tracking the image path, thumbnail path, page number, and any topics

**What's stored:**
- `document_pages` table — one row per page (20,234 total)
- PNG files in `data/pages/` — full-size + thumbnails (5 GB total)

**Command:** `python cli.py render`

---

## Step 7: Build the Search Index (FTS)

**What happens:** We build a full-text search index so you can type words and find matching meetings instantly.

**Where the data comes from:** The `summary` column on meetings (AI-generated summaries from Step 8, when available).

**How it's processed:**
1. The FTS module (`app/pipeline/fts.py`) creates an SQLite FTS5 virtual table
2. It loads every meeting summary into the index
3. When you search, SQLite's FTS5 engine finds matching text and returns highlighted snippets

**What's stored:** An FTS5 virtual table called `meeting_summaries_fts` inside the SQLite database.

**Limitation:** FTS only works on the 402 meetings that have AI-generated summaries. Topic-based filtering (from Step 5) works on all 1,151 meetings with topics.

**Command:** `python cli.py pipeline --rebuild-fts`

---

## Step 8: AI Summarization (Summarize — Optional)

**What happens:** An AI reads the extracted text from each board's meetings and writes a structured summary — what was discussed, key decisions, notable trends.

**Where the data comes from:** The extracted text from Step 4, bundled per board.

**How it's processed:**
1. `python cli.py summarize --board TX_MD` prepares a "prompt file" — a markdown document containing all of a board's meeting text
2. A human (or Claude Code subagent) reads the prompt file and writes a summary
3. `python cli.py summarize --ingest` loads the summary back into the database
4. `python cli.py summarize --national` prepares a synthesis prompt that combines all board summaries into a national landscape report

**What's stored:** The `summary` column on meetings, plus markdown files in `data/reports/`.

**Command:** `python cli.py summarize`

---

## Step 9: The Dashboard (Serve)

**What happens:** A web dashboard makes everything searchable and browsable.

**Where the data comes from:** Everything above — boards, meetings, documents, pages, topics, summaries — all served from the SQLite database and file system.

**How it's processed:** A FastAPI web server (`app/web/server.py`) serves HTML pages built with:
- **Jinja2** templates for page rendering
- **HTMX** for interactive updates without full page reloads (like search filters)
- **Alpine.js** for client-side interactivity (expanding accordions, topic pill toggles)
- **Tailwind CSS** for styling

**The pages:**

| Page | URL | What it shows |
|------|-----|---------------|
| **National Overview** | `/` | Stats, coverage map, topic breakdown |
| **State Drill-Down** | `/state/TX` | All boards in a state with meeting counts |
| **Board Detail** | `/board/TX_MD` | Full meeting timeline, topic breakdown, documents |
| **Meeting Detail** | `/meeting/123` | Inline PDF viewer, summary, document list |
| **Page Viewer** | `/page/456` | Full-size page image with filmstrip navigation |
| **Search** | `/search` | Topic filters, state/period dropdowns, FTS search, page thumbnails |
| **National Report** | `/report` | AI-generated landscape report with clickable citations |
| **Pipeline Runs** | `/pipeline/` | History of data collection runs |

**Command:** `python cli.py serve` (starts on port 8099)

---

## The Full Pipeline (All Steps Together)

The pipeline command runs Steps 3-7 in sequence:

```
python cli.py pipeline
```

This does: Collect → Extract → Render Pages → Calculate What's New → Rebuild Search Index

It creates a `PipelineRun` record in the database that tracks what was collected, how many new meetings/documents were found, and whether it succeeded or failed.

---

## Data Flow Diagram

```
Board Websites (63 sites)
    │
    ▼
[Step 1-2: Seed + Discover]
    │  Find minutes URLs
    ▼
[Step 3: Collect]
    │  Download PDFs
    │  ├─► data/documents/{board}/{file}.pdf
    │  └─► meetings + meeting_documents tables
    ▼
[Step 4: Extract]
    │  Read text from PDFs
    │  └─► content_text column
    ▼
[Step 5: Classify]          [Step 6: Render]
    │  Keyword matching          │  PDF → PNG images
    │  └─► topics columns        │  └─► data/pages/{board}/{doc}/
    ▼                            ▼
[Step 7: FTS Index]         [Step 8: Summarize]
    │  Full-text search          │  AI summaries
    ▼                            ▼
┌─────────────────────────────────────┐
│     [Step 9: Dashboard]             │
│     http://localhost:8099           │
│                                     │
│  National → State → Board → Meeting │
│  Search by topic, state, keywords   │
│  Page viewer with thumbnails        │
│  National landscape report          │
└─────────────────────────────────────┘
```

---

## Tech Stack Summary

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Database** | SQLite (WAL mode) | All structured data — boards, meetings, documents, pages, topics |
| **Web Server** | FastAPI (Python) | Serves the dashboard |
| **Templates** | Jinja2 + HTMX + Alpine.js | Page rendering and interactivity |
| **Styling** | Tailwind CSS | Dashboard design |
| **PDF Processing** | PyMuPDF (fitz) | Text extraction + page rendering |
| **Browser Automation** | Playwright + Chromium | Visiting board websites, downloading files |
| **Search** | SQLite FTS5 | Full-text search on meeting summaries |
| **Topic Classification** | Regex keyword matching | 16-topic taxonomy, no AI needed |
| **AI Summaries** | Claude/Ollama (external) | Board-level and national summaries |

---

## Storage Breakdown

| What | Size | Count |
|------|------|-------|
| Rendered page images | 5.0 GB | 20,234 pages |
| PDF documents | 1.1 GB | 1,686 files |
| Exhibit images | 115 MB | — |
| Reports + prompts | 83 MB | — |
| Discovery screenshots | 78 MB | — |
| SQLite database | 52 MB | 63 boards, 1,680 meetings, 1,772 docs |
| **Total** | **~6.7 GB** | — |
