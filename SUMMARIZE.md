# boardpulse Summarization — Dispatch Guide

How to run AI summarization for boardpulse using Claude Code subagents.

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

> Read `data/reports/{board_code}_prompt.md`. Follow the summarization instructions
> in the file. Write your output to `data/reports/{board_code}_summary.md`.
> Use only the information provided in the prompt file.

Use `haiku` model for per-board summaries (cost-efficient, sufficient quality).

Dispatch all subagents in parallel — they are independent.

## Step 2: Ingest Summaries

After all subagents complete:

```bash
python cli.py summarize --ingest
```

This reads all `*_summary.md` files and stores them in the database.

## Step 3: National Landscape Report

```bash
python cli.py summarize --national
```

This creates `data/reports/national_synthesis_prompt.md`. Dispatch a single subagent:

> Read `data/reports/national_synthesis_prompt.md`. Follow the synthesis instructions.
> Write your output to `data/reports/YYYY-MM-DD-board-landscape.md` (use today's date).

Use `opus` or `sonnet` model for the synthesis (needs analytical depth).

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
