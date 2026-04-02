# boardpulse Pipeline — AI Assistant Guide

This guide tells any AI assistant (Claude Code, Perplexity, etc.) how to run the boardpulse automated intelligence pipeline. Follow these steps in order.

## Prerequisites

- Python 3.11+ with venv activated (`source venv/bin/activate`)
- Playwright installed (`playwright install chromium`)
- The boardpulse database exists (`boardpulse.db`)

## Running the Pipeline

### Step 1: Collection + Extraction (Python CLI)

Run the pipeline CLI command to collect new meetings and extract text:

```bash
python cli.py pipeline
```

This will:
1. Scrape all 63 boards for new meetings
2. Download new documents (PDFs)
3. Extract text from new documents
4. Calculate what changed (delta)
5. Write a pipeline context file to `data/reports/run_{id}_context.md`

For specific boards only: `python cli.py pipeline --boards TX_MD,FL_MD`

### Step 2: Read the Context File

Read the context file printed at the end of Step 1. It contains:
- Which boards have new content
- How many meetings/documents were found
- Prompt file locations
- Step-by-step instructions

### Step 3: Categorize Document Pages

For each new document listed in the context file, read its extracted text and assign topic tags **per page** from this taxonomy:

`licensing`, `disciplinary`, `telehealth`, `scope-of-practice`, `rulemaking`, `legislation`, `opioids`, `controlled-substances`, `patient-safety`, `physician-wellness`, `AI`, `CME`, `IMLC`, `workforce`, `public-health`

Write results as JSON to `data/reports/run_{id}_topics.json`:

```json
{
    "document_42": {
        "1": ["licensing"],
        "3": ["telehealth", "AI"],
        "7": ["telehealth"],
        "14": ["opioids", "controlled-substances"]
    },
    "document_43": {
        "2": ["rulemaking", "legislation"]
    }
}
```

Keys are `document_{id}`. Values are objects mapping page numbers to topic tag arrays. Only include pages that have relevant topics — skip blank/procedural pages.

**Batching:** Process 10-20 documents per call to manage token usage.

Then ingest: `python cli.py pipeline --ingest-topics --run-id {id}`

### Step 4: Summarize Boards

For each board listed in the context file's Delta section:
1. Read the prompt file at `data/reports/{code}_prompt.md`
2. Follow the summarization instructions in the prompt
3. Write output to `data/reports/{code}_summary.md`

Then ingest all summaries: `python cli.py summarize --ingest`

**Note:** The FTS search index is rebuilt automatically during the pipeline. To rebuild manually: `python cli.py pipeline --rebuild-fts`

### Step 5: Write the "What's New" Digest

Generate a focused intelligence brief covering only changes from this run.

Write to: `data/reports/run_{id}_digest.md`

**Format:**
- **Header** — run date, period covered ("Activity since [last run date]"), stats
- **Key Developments** — 3-5 bullet executive summary of most significant findings
- **By Board** — for each board with new activity:
  - Board name + state
  - Meeting dates covered
  - Topic tags (from the taxonomy)
  - 2-3 sentence summary
  - Notable actions or decisions
- **Topic Highlights** — cross-board view by topic
- **Footer** — total coverage stats

### Step 6: Regenerate National Landscape Report

Read `data/reports/national_synthesis_prompt.md` (generate it first if needed: `python cli.py summarize --national`).

Write the full updated report to: `data/reports/{YYYY-MM-DD}-board-landscape.md`

### Step 7: Finalize

```bash
python cli.py pipeline --finalize --run-id {id} \
    --digest-path data/reports/run_{id}_digest.md \
    --report-path data/reports/{YYYY-MM-DD}-board-landscape.md
```

## Checking Pipeline History

```bash
python cli.py pipeline --status
```

Or visit the dashboard: `http://localhost:8099/pipeline/`

## Troubleshooting

- **Playwright not installed:** Run `pip install playwright && playwright install chromium`
- **Boards return 403:** Some boards (KS, NH) block automated requests. These are logged as failed events.
- **No new content found:** The collector skips already-known meetings. If a board hasn't published new minutes, there's nothing to collect.
- **Text extraction fails:** Some PDFs are image-only. These will have empty `content_text`.
