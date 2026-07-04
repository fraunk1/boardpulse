# boardpulse Summarization — Dispatch Guide

How to run AI summarization for boardpulse using Claude Code subagents.

## Model Presets

The monthly loop dispatches Claude Code subagents to write the per-board
summaries, the structured facts, and the delta-brief prose. Pick the model by
preset — don't hard-code a model name anywhere:

| Job | Preferred | Fallback | Emergency (local) |
|-----|-----------|----------|-------------------|
| Per-board summaries | **opus** (Opus 4.8) | sonnet-class | Paste the prompt file into any local model, save its answer as the summary, then run `--ingest` and expect a couple of gate-retry rounds |
| Fact extraction | **opus** (Opus 4.8) | sonnet-class | same as above |
| Delta-brief prose | **opus** (Opus 4.8) | sonnet-class | same as above |
| National synthesis | **opus** (Opus 4.8) | — | If opus is unavailable, **skip national synthesis that month** and note the skip in the brief |

Opus 4.8 is the acceptance-tested model for this pipeline: 7 of 8 gold boards
passed clean and all 8 were gate-valid (see `data/gold/OPUS48-ACCEPTANCE.md`).
Anywhere older notes said "use sonnet" or "use opus", read that as **use the
current preferred preset (see Model Presets)**.

The quality gate protects the database regardless of which model wrote the file
— a weaker model just means more retry rounds, never bad data in the DB. The
gate is the safeguard, not the model.

## Gates & retry

`summarize --ingest` and `facts --ingest` run every file through a
deterministic quality gate before anything touches the database. A file that
fails is **rejected**, its problems are written to a plain-text errors file next
to it, and the command **exits 1** — a hard signal that a retry pass is needed.

- Per-board summary rejects → `data/reports/{code}_summary.errors.txt`
- Fact-file rejects → `data/reports/facts/{path}.errors.txt`

**On a rejected `{code}`, re-dispatch the SAME agent with this instruction:**

> Read `{code}_summary.errors.txt` and the original prompt file, then
> regenerate the ENTIRE file fixing every error listed. Never hand-patch the
> file to sneak past the gate — write it fresh and correct.

Re-run `--ingest`. If the same board is **rejected a second time, skip it** — it
keeps last month's good summary, which stays in the database untouched — and
note the skipped board in the run report. Never lower the gate to let a file
through.

## Prerequisites

- Run `python cli.py extract` to ensure all collected documents have extracted text
- Run `python cli.py summarize` to prepare data bundles (prompt files)

## Step 1: Per-Board Summaries (Parallel Subagents)

After `python cli.py summarize` creates prompt files in `data/reports/`, dispatch one
Claude Code subagent per board to process them.

### Single board (manual)

```bash
# Prepare the prompt
python cli.py summarize --board CA_MD

# Then in Claude Code, tell a subagent:
#   "Read data/reports/CA_MD_prompt.md, follow the instructions, and write
#    the output to data/reports/CA_MD_summary.md"
```

### All boards (parallel dispatch)

For each `*_prompt.md` file in `data/reports/`, dispatch a subagent with this task:

> Read the ENTIRE `data/reports/{board_code}_prompt.md` (page through with
> multiple Read calls). Follow its embedded Output Format EXACTLY — the
> contract is two-layer: a 300-600 word 12-month board ROLLUP first (with
> date-citation links + Sources table), then one `=== MEETING: YYYY-MM-DD ===`
> block per meeting that has extracted text (80-200 words + a `topics: [...]`
> line), ending `=== END ===`. The delimiters are machine-parsed — reproduce
> them exactly. OMIT blocks for meetings marked "(No extracted text
> available)". Use only the information provided in the prompt file.
> Write your output to `data/reports/{board_code}_summary.md`.

Use the current preferred preset for per-board summaries (see Model Presets) —
the delimiter contract + no-fabrication discipline are what the preset is chosen
for.

Dispatch all subagents in parallel — they are independent.

## Step 2: Ingest Summaries

After all subagents complete:

```bash
python cli.py summarize --ingest
```

This reads all `*_summary.md` files and stores them in the database. It runs
every file through the quality gate first: any rejected board leaves a
`{code}_summary.errors.txt` file and the command exits 1. When that happens, do
a retry pass (see **Gates & retry** above) before moving on.

## Step 3: National Landscape Report

```bash
python cli.py summarize --national
```

This creates `data/reports/national_synthesis_prompt.md`. Dispatch a single subagent:

> Read `data/reports/national_synthesis_prompt.md`. Follow the synthesis instructions.
> Write your output to `data/reports/YYYY-MM-DD-board-landscape.md` (use today's date).

Use the current preferred preset for the synthesis (see Model Presets — national
synthesis wants opus for the analytical depth). If opus is unavailable this
month, skip national synthesis and note the skip in the delta brief.

## Step 4: Convert to PDF (optional)

Use the md2pdf MCP tool to convert reports to PDF:

```
convert_md_to_pdf("data/reports/2026-03-29-board-landscape.md")
```

## Full Flow Summary

```
python cli.py summarize              # Prepare all per-board prompts
  -> dispatch parallel subagents     # Each reads prompt, writes summary
python cli.py summarize --ingest     # Store summaries in DB
python cli.py summarize --national   # Prepare national synthesis prompt
  -> dispatch synthesis subagent     # Reads prompt, writes landscape report
```
