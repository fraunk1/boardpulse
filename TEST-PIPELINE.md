# Pipeline Test Runbook

> **Purpose:** Full end-to-end verification of the boardpulse pipeline.
> Follow every step in order. Mark each checkbox as you go. Do not skip ahead.

---

## Phase 1: Server + Dashboard Pages

- [ ] **1.1** Kill any running boardpulse server and restart
  ```bash
  pkill -f "cli.py serve" ; cd Projects/boardpulse && source venv/bin/activate && python cli.py serve &
  ```
  **Expected:** Server starts on port 8099, no errors

- [ ] **1.2** Open `http://localhost:8099/` in browser
  **Expected:** National overview page loads with stats, map, topic grid

- [ ] **1.3** Open `http://localhost:8099/pipeline/`
  **Expected:** Pipeline Runs page loads. Shows run history table (may have test runs from development). "Start Pipeline Run" button visible in top right.

- [ ] **1.4** Click into any existing pipeline run (if any exist)
  **Expected:** Detail page loads with stat cards, event timeline. No 404.

- [ ] **1.5** Verify "Pipeline" link appears in the top nav bar
  **Expected:** Refresh-cw icon + "Pipeline" text in nav, links to `/pipeline/`

---

## Phase 2: CLI Smoke Tests

- [ ] **2.1** Run `python cli.py pipeline --help`
  **Expected:** Shows all flags: `--boards`, `--skip-report`, `--finalize`, `--run-id`, `--digest-path`, `--report-path`, `--ingest-topics`, `--status`

- [ ] **2.2** Run `python cli.py pipeline --status`
  **Expected:** Table of pipeline runs (or "No pipeline runs found")

---

## Phase 3: Pipeline Run — Collection + Extraction + Delta

This is the real test. We'll run the pipeline against a small set of boards to keep it fast.

- [ ] **3.1** Pick 2-3 boards likely to have new content. Suggestion: `AL_MD,GA_MD,MO_MD`
  **Decision:** Which boards to test with: _______________

- [ ] **3.2** Run the pipeline
  ```bash
  python cli.py pipeline --boards AL_MD,GA_MD,MO_MD
  ```
  **Expected:**
  - "PIPELINE RUN #N" header prints
  - Stage 1 (Collection) runs — may find new meetings or report "no new"
  - Stage 2 (Extraction) runs
  - Stage 3 (Delta + Context File) prints path to context file
  - Summary shows new meetings/documents counts
  - **Record the run ID:** ___

- [ ] **3.3** Check the context file exists
  ```bash
  cat data/reports/run_{ID}_context.md
  ```
  **Expected:** Markdown file with Summary, Delta by Board (or "no new activity"), Instructions section with 7 numbered steps

- [ ] **3.4** Verify the run appears on the dashboard
  Open `http://localhost:8099/pipeline/`
  **Expected:** New run appears in table with status "running" or the stats filled in

- [ ] **3.5** Click into the run detail page
  **Expected:** Stat cards show correct counts. Event timeline shows collect/extract events.

---

## Phase 4: Topic Categorization

If the pipeline found new documents with extracted text, we categorize them.

- [ ] **4.1** Read the context file to identify new documents
  **Expected:** Context file lists boards with new content and prompt file paths. If no new content was found, skip to Phase 7 (finalize with no changes).

- [ ] **4.2** For each new document, read the extracted text and assign topic tags
  Write results to `data/reports/run_{ID}_topics.json`:
  ```json
  {
    "DOC_ID": ["licensing", "disciplinary"],
    "DOC_ID": ["telehealth", "rulemaking"]
  }
  ```
  **Expected:** JSON file written with document IDs as keys, topic tag arrays as values

- [ ] **4.3** Ingest topics
  ```bash
  python cli.py pipeline --ingest-topics --run-id {ID}
  ```
  **Expected:** "Tagged N documents, rolled up N meetings"

- [ ] **4.4** Verify topics in database
  ```bash
  python -c "
  import asyncio
  from app.database import init_db
  from app.models import MeetingDocument
  import app.database as db
  async def check():
      await init_db()
      async with db.async_session() as s:
          from sqlalchemy import select
          docs = (await s.execute(select(MeetingDocument).where(MeetingDocument.topics.isnot(None)).limit(5))).scalars().all()
          for d in docs:
              print(f'  Doc {d.id}: {d.topics}')
  asyncio.run(check())
  "
  ```
  **Expected:** Shows document IDs with their assigned topic tags

---

## Phase 5: Summarization

- [ ] **5.1** Check that prompt files exist for boards with new content
  ```bash
  ls data/reports/*_prompt.md
  ```
  **Expected:** Prompt files for the boards that had new content

- [ ] **5.2** For each board with a prompt file, read it and write a summary
  Read `data/reports/{CODE}_prompt.md`, follow instructions, write output to `data/reports/{CODE}_summary.md`
  **Expected:** Summary markdown files written for each board

- [ ] **5.3** Ingest summaries
  ```bash
  python cli.py summarize --ingest
  ```
  **Expected:** "Ingested N summaries" (or similar success message)

---

## Phase 6: Digest + Report

- [ ] **6.1** Write the "What's New" digest
  Read the context file + new summaries. Write the digest to `data/reports/run_{ID}_digest.md`
  **Format check:**
  - [ ] Has header with run date and stats
  - [ ] Has "Key Developments" section (3-5 bullets)
  - [ ] Has per-board sections with topic tags
  - [ ] Has "Topic Highlights" cross-board view
  **Expected:** Digest markdown file written

- [ ] **6.2** Prepare national synthesis prompt
  ```bash
  python cli.py summarize --national
  ```
  **Expected:** Writes `data/reports/national_synthesis_prompt.md`

- [ ] **6.3** Write the national landscape report
  Read the synthesis prompt, write output to `data/reports/YYYY-MM-DD-board-landscape.md` (use today's date)
  **Expected:** Full landscape report markdown file written

---

## Phase 7: Finalize

- [ ] **7.1** Finalize the pipeline run
  ```bash
  python cli.py pipeline --finalize --run-id {ID} \
    --digest-path data/reports/run_{ID}_digest.md \
    --report-path data/reports/YYYY-MM-DD-board-landscape.md
  ```
  **Expected:** "Pipeline run #N marked as completed (N boards summarized)."

- [ ] **7.2** Verify on dashboard
  Open `http://localhost:8099/pipeline/{ID}`
  **Expected:**
  - [ ] Status badge shows "Completed" (green)
  - [ ] Stat cards show correct counts (meetings, documents, boards summarized, duration)
  - [ ] "What's New Digest" section renders the digest inline
  - [ ] "National Landscape Report" link appears
  - [ ] Event timeline shows all events in order

- [ ] **7.3** Check `python cli.py pipeline --status`
  **Expected:** Run shows as "completed" in the table with correct stats

---

## Phase 8: Dashboard Trigger Test

- [ ] **8.1** Open `http://localhost:8099/pipeline/`
- [ ] **8.2** Click the "Start Pipeline Run" button
  **Expected:** Spinner message appears: "Pipeline run started. Refresh the page to track progress."

- [ ] **8.3** Wait 30-60 seconds, then refresh the page
  **Expected:** New run appears in the table with status "running" or "completed"

- [ ] **8.4** Click into the new run
  **Expected:** Detail page loads with event timeline showing collection progress

---

## Phase 9: Edge Cases

- [ ] **9.1** Run pipeline with no new content
  ```bash
  python cli.py pipeline --boards AL_MD
  ```
  (Same board we just collected — should find nothing new)
  **Expected:** "No new content found. Nothing to summarize."

- [ ] **9.2** Try finalizing a non-existent run
  ```bash
  python cli.py pipeline --finalize --run-id 99999
  ```
  **Expected:** "Error: run #99999 not found"

- [ ] **9.3** Try ingesting topics without --run-id
  ```bash
  python cli.py pipeline --ingest-topics
  ```
  **Expected:** "Error: --ingest-topics requires --run-id"

---

## Results Summary

| Phase | Description | Pass/Fail | Notes |
|-------|-------------|-----------|-------|
| 1 | Server + Dashboard Pages | | |
| 2 | CLI Smoke Tests | | |
| 3 | Pipeline Run (Collection) | | |
| 4 | Topic Categorization | | |
| 5 | Summarization | | |
| 6 | Digest + Report | | |
| 7 | Finalize | | |
| 8 | Dashboard Trigger | | |
| 9 | Edge Cases | | |

**Overall:** _____ / 9 phases passed

**Boards tested:** _______________
**Run ID tested:** _______________
**Date tested:** _______________
