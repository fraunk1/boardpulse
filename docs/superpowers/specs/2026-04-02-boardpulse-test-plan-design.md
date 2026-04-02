# boardpulse Test Plan — Product-Ready + Demo-Ready

**Date:** 2026-04-02
**Approach:** Top-down (route tests first, fix bugs as found, then backfill unit tests)
**Target:** 49 existing → ~129 total tests

---

## Context

boardpulse has 49 passing tests covering models and pipeline internals (~35-40% of critical code). Major gaps: zero web route tests, zero classifier tests, zero CLI tests. The dashboard could be silently 500ing and no test would catch it.

**Goal:** Prove every page loads with real data (demo-ready), then harden classification and data integrity (product-ready).

---

## 1. Test Infrastructure — Shared conftest.py

Create `tests/conftest.py` to replace duplicated `setup_db` fixtures across all 13 test files.

### Fixtures

**`db_session` (autouse)**
- In-memory SQLite via `db.init_db(url="sqlite+aiosqlite://")`
- Auto-used so every test gets a clean DB

**`client`**
- `httpx.AsyncClient` wrapping the FastAPI app via `httpx.ASGITransport`
- Usage: `response = await client.get("/")`
- **Important:** The app's `startup` event calls `init_db()` with no URL, which would create a file-based DB and overwrite the in-memory test DB. The fixture must patch `app.web.server.startup` to be a no-op (or remove the startup handler) since `db_session` already initialized the in-memory DB. Alternatively, set `db.engine` to a truthy value so `init_db` can short-circuit, but current `init_db` always reinitializes — so patching startup is the clean approach.

**`seed_board`**
- Factory fixture returning an async function: `board = await seed_board("TX_MD", "TX", "Texas Medical Board")`
- Creates a Board record with sensible defaults

**`seed_full_chain`**
- Factory fixture that creates a complete Board → Meeting → MeetingDocument → DocumentPage chain
- Includes: topics on meeting/doc/page, a summary on the meeting, a rendered page image (tiny 1x1 PNG written to tmp dir)
- Returns a dict: `{"board": Board, "meeting": Meeting, "doc": MeetingDocument, "page": DocumentPage}`
- This is the "golden path" fixture — every route test that needs data uses it

**`seed_empty_board`**
- Creates a board with zero meetings — for empty-state testing

**`tmp_pages_dir`**
- `tmp_path / "pages"` — overrides `PAGES_DIR` config so rendered images go to temp dir
- Patches `app.config.PAGES_DIR` for the test session

**Migration from existing tests:**
- Existing test files keep working — `conftest.py`'s `db_session` replaces each file's `setup_db`
- Remove the per-file `setup_db` fixtures and `sys.path.insert` hacks (conftest handles path)

### Dependencies

- `httpx` — async test client for FastAPI (add to dev requirements)
- `pytest-asyncio` — already used
- No new external deps needed

---

## 2. Route Smoke Tests — `tests/test_routes.py`

Every route hit with seeded data. Asserts status code + key content.

### Navigation Pages (HTML responses)

| Test | Route | Seed | Assert |
|------|-------|------|--------|
| `test_national_overview` | `GET /` | full chain | 200, board count in HTML, topic name present |
| `test_national_overview_empty` | `GET /` | empty board | 200, no crash (0 meetings) |
| `test_state_view` | `GET /state/TX` | full chain (TX) | 200, board name in HTML |
| `test_state_view_404` | `GET /state/ZZ` | none | 404 |
| `test_board_view` | `GET /board/TX_MD` | full chain | 200, board name, meeting date |
| `test_board_view_404` | `GET /board/NOPE` | none | 404 |
| `test_board_redirect` | `GET /board/TX/TX_MD` | none | 301, Location: `/board/TX_MD` |
| `test_meeting_view` | `GET /meeting/{id}` | full chain | 200, board name, document listed |
| `test_meeting_view_404` | `GET /meeting/99999` | none | 404 |
| `test_page_viewer` | `GET /page/{id}` | full chain + image file | 200, image tag, filmstrip |
| `test_page_viewer_404` | `GET /page/99999` | none | 404 |

### Search

| Test | Route | Seed | Assert |
|------|-------|------|--------|
| `test_search_all` | `GET /search?period=all` | full chain with topics | 200, result count > 0, topic pills |
| `test_search_by_topic` | `GET /search?topic=Discipline&period=all` | full chain | 200, only Discipline results |
| `test_search_by_state` | `GET /search?state=TX&period=all` | full chain | 200, only TX results |
| `test_search_fts` | `GET /search?q=telehealth&period=all` | full chain + FTS index | 200, matching results |
| `test_search_no_results` | `GET /search?q=xyznonexistent&period=all` | full chain | 200, "No results found" |
| `test_search_htmx` | `GET /search?period=all` + `HX-Request: true` | full chain | 200, no `<html>` wrapper |
| `test_search_empty_db` | `GET /search?period=all` | empty board | 200, "No results found" |

### File Serving

| Test | Route | Seed | Assert |
|------|-------|------|--------|
| `test_page_image` | `GET /page-image/{id}` | full chain + image file | 200, Content-Type: image/png |
| `test_page_image_404` | `GET /page-image/99999` | none | 404 |
| `test_page_thumb` | `GET /page-thumb/{id}` | full chain + thumb file | 200, Content-Type: image/png |
| `test_page_thumb_404` | `GET /page-thumb/99999` | none | 404 |

### Pipeline UI

| Test | Route | Seed | Assert |
|------|-------|------|--------|
| `test_pipeline_list` | `GET /pipeline/` | pipeline run record | 200, run ID in HTML |
| `test_pipeline_list_empty` | `GET /pipeline/` | none | 200, no crash |
| `test_pipeline_detail` | `GET /pipeline/{id}` | run + events | 200, event timeline |
| `test_pipeline_detail_404` | `GET /pipeline/99999` | none | 404 |
| `test_pipeline_start` | `POST /pipeline/start` | none | 202, spinner HTML |

### Redirects & Misc

| Test | Route | Seed | Assert |
|------|-------|------|--------|
| `test_topic_redirect` | `GET /topic/telehealth` | none | 301, Location contains `/search?topic=` |
| `test_collect_trigger` | `POST /collect/TX_MD` | board | 202 |
| `test_collect_trigger_404` | `POST /collect/NOPE` | none | 404 |

### Report

| Test | Route | Seed | Assert |
|------|-------|------|--------|
| `test_report_exists` | `GET /report` | report file in REPORTS_DIR | 200, report content |
| `test_report_missing` | `GET /report` | no report files | 200, "No report available" |

**Total: ~35 route tests**

---

## 3. Classifier Tests — `tests/test_classifier.py`

### classify_text unit tests

| Test | Input | Assert |
|------|-------|--------|
| `test_classify_discipline_text` | "The board issued a consent order and suspended the physician's license..." | `"Discipline"` in result |
| `test_classify_telehealth_text` | "Discussion of telehealth prescribing regulations and virtual care..." | `"Telehealth"` in result |
| `test_classify_ai_text` | "The use of artificial intelligence and machine learning in diagnosis..." | `"AI & Technology"` in result |
| `test_classify_licensing_text` | "License renewal applications and endorsement processing discussed..." | `"Licensing"` in result |
| `test_classify_rulemaking_text` | "Proposed rule amendments to administrative code section 22..." | `"Rulemaking"` in result |
| `test_classify_multiple_topics` | Text mentioning discipline + opioids + patient safety | Result contains all three |
| `test_classify_empty_text` | `""` | `[]` |
| `test_classify_short_text` | `"Minutes of meeting"` (< 50 chars) | `[]` |
| `test_classify_no_matches` | `"The weather today is sunny and warm."` | `[]` |
| `test_classify_min_matches_threshold` | Text with 1 mention of "license" | min_matches=2 → `[]`, min_matches=1 → `["Licensing"]` |
| `test_classify_results_sorted` | Multi-topic text | Result is alphabetically sorted |
| `test_all_16_topics_matchable` | One snippet per topic | Each of 16 topics can be triggered independently |

### classify_all_documents integration tests

| Test | Setup | Assert |
|------|-------|--------|
| `test_classify_all_documents` | 3 docs with content_text | Docs get topics, meetings rolled up |
| `test_classify_skip_existing` | 1 doc with topics, 1 without | Only untagged doc classified (force=False) |
| `test_classify_force` | 1 doc with stale topics | force=True re-classifies |
| `test_classify_rollup_dedup` | 2 docs on same meeting, overlapping topics | Meeting topics = sorted union, no duplicates |
| `test_classify_no_text_skipped` | Doc with content_text=None | Skipped, no error |

### Taxonomy sync test

| Test | Assert |
|------|--------|
| `test_taxonomy_matches_classifier` | Every topic name in `TOPIC_PATTERNS` exists in `TOPIC_TAXONOMY` and vice versa |

**Total: ~20 classifier tests**

---

## 4. Data Integrity Tests — `tests/test_data_integrity.py`

| Test | What it validates |
|------|-------------------|
| `test_topic_rollup_mixed_json` | topics stored as `list` and `str` both handled in rollup |
| `test_topic_rollup_partial_pages` | Some pages tagged, some None — doc still gets partial topics |
| `test_topic_deduplication` | Rollup from 3 docs with overlapping topics → no duplicates on meeting |
| `test_path_resolution_relative` | Renderer resolves `data/documents/TX_MD/foo.pdf` via PROJECT_ROOT |
| `test_path_resolution_absolute` | Renderer handles `/full/path/to/foo.pdf` directly |
| `test_fts_special_characters` | Search for `"AI & Technology"`, `opioid "consent order"` → no crash |
| `test_fts_empty_query` | Search for `""` → empty results, no crash |
| `test_board_zero_meetings` | Board with 0 meetings → state view and board view still render |
| `test_meeting_no_documents` | Meeting with no docs → meeting view still renders |
| `test_document_no_pages` | Document with no DocumentPages → doesn't break search |

**Total: ~10 data integrity tests**

---

## 5. CLI Smoke Tests — `tests/test_cli.py`

Test CLI dispatch logic by calling the async handler functions directly (not via subprocess), using the in-memory test DB from conftest. This avoids hitting the real DB and is faster.

| Test | What it calls | Assert |
|------|---------------|--------|
| `test_cli_status` | `show_status()` | No exception, prints board table |
| `test_cli_classify` | `handle_classify(args)` with default args | Classifies seeded docs, no exception |
| `test_cli_classify_force` | `handle_classify(args)` with force=True | Re-classifies, no exception |
| `test_cli_pipeline_status` | `show_pipeline_status()` | No exception, handles empty run list |
| `test_cli_pipeline_rebuild_fts` | `handle_pipeline(args)` with rebuild_fts=True | Rebuilds index, no exception |
| `test_cli_argparse_help` | `main()` with `["--help"]` via `SystemExit(0)` catch | Exits 0 |
| `test_cli_argparse_unknown` | `main()` with `["notacommand"]` | Exits non-zero |

**Total: ~7 CLI tests**

---

## Bug Fix Protocol

When a route test fails (500, wrong content, template crash):
1. Identify the root cause (bad query, missing null check, template variable error)
2. Fix the source code
3. Add a targeted unit test for the specific bug
4. Re-run the route test to confirm the fix
5. Commit fix + test together

This means the test suite doubles as a bug-finding tool — every fix gets regression-protected.

---

## Execution Order

1. **conftest.py** — shared fixtures, httpx client
2. **test_routes.py** — route sweep (fix bugs as found)
3. **test_classifier.py** — classifier unit + integration tests
4. **test_data_integrity.py** — rollup, paths, edge cases
5. **test_cli.py** — CLI smoke tests
6. Clean up existing test files to use shared conftest

---

## Success Criteria

- All ~129 tests pass
- Every route returns 200 (or expected status) with seeded data
- Every route handles empty/missing data without 500
- Classifier correctly identifies all 16 topics
- Topic rollup produces correct, deduplicated, sorted results
- CLI commands exit 0 with a test DB
