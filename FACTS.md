# boardpulse Fact Extraction — Dispatch Guide

How to pull STRUCTURED FACTS out of board minutes with Claude Code subagents.
Where the per-meeting summaries (see `SUMMARIZE.md`) are prose, the facts are
small, checkable records — the rows that drive the `/trends` charts, the
watchlist, and the monthly delta brief.

For which model to use, see the **Model Presets** table in `SUMMARIZE.md`. Facts
run on the current preferred preset (Opus 4.8, acceptance-tested).

## What gets extracted — the four fact classes

Every fact belongs to one of four classes. Each class has a fixed set of fields,
and several fields can only hold a value from a controlled list — the exact
lists live in `app/quality/taxonomy.py` and are the single source of truth. If a
value isn't on the list, the ingest gate rejects the file. Every list includes
an `other` catch-all so the model is never forced to invent a value.

**1. Policy actions** — formal instruments the board moved on (rules, guidance,
policy statements, positions, resolutions).
- `instrument` — one of: rule, guidance, policy_statement, position, resolution, other
- `stage` — where in its life the action sits: discussed, proposed, comment_period, adopted, amended, repealed, effective, tabled, withdrawn
- `topic` — one of the 15 dashboard topics (licensing, telehealth, AI, rulemaking, …) plus `other`
- `title` (short name, ≤200 chars), `description` (the detail), `rule_reference` (a rule/code number, or null), `action_date` (YYYY-MM-DD, usually the meeting date), `quote` (verbatim, or null), `source_document`, `confidence` (high / medium / low)

**2. Legislation** — bills the board discussed.
- `bill_number` exactly as written in the minutes ("SB 123", "HB 4001")
- `bill_state` — two-letter state code, or "US" for a federal bill
- `subject` — plain description of what the bill does
- `topic` — a dashboard topic, or null
- `involvement` — the board's relationship to the bill: monitoring, supporting, opposing, neutral, testified, implementing, commented, other
- `status_note` (or null), `quote` (verbatim, or null), `source_document`, `confidence`

**3. Disciplinary** — per-meeting COUNTS of actions by outcome category. One row
per category, per meeting.
- `category` — revocation, suspension, probation, reprimand, fine, consent_order, surrender, reinstatement, denial, dismissal, other
- `count` — a non-negative whole number (`action_count` in the database)
- `quote` (verbatim, or null), `source_document`, `confidence`

**4. Emerging topics** — the FIRST time a board discusses a genuinely new
subject (not routine business). Use sparingly.
- `topic_slug` — a short lowercase-hyphen slug, ≤60 chars (e.g. `ai-scribes`)
- `subject` — what the new topic is
- `quote` — verbatim, and **required** here (it is the anchor that proves the
  topic is real), `source_document`, `confidence`

## The output shape (schema "facts-v1")

The agent writes ONE JSON object per chunk. It is organized by meeting: a
`meetings` array, and inside each meeting the four fact arrays. Empty arrays are
correct and expected — a routine, procedural meeting genuinely yields no facts.

```
{
  "schema_version": "facts-v1",
  "board_code": "XX_MD",
  "model": "<the model that wrote this>",
  "meetings": [
    {
      "meeting_date": "YYYY-MM-DD",
      "policy_actions": [ … ],
      "legislation":    [ … ],
      "disciplinary":   [ … ],
      "emerging_topics":[ … ]
    }
  ]
}
```

Rules the agent must follow (all enforced by the gate, not just advice):
- **Every covered meeting must appear** in `meetings` — with empty arrays if it
  yielded nothing. No extra meetings, no missing meetings.
- **Optional fields are `null`, never omitted and never `""`.**
- **Use only the controlled-vocabulary values** above.
- **Use only facts in the prompt file** — never invent a bill number, a count,
  or a rule number. When the text is ambiguous, prefer fewer facts at higher
  confidence over many at low confidence.
- **Output ONLY the JSON object** — no code fences, no commentary.

## The verbatim-quote rule (why quotes must be exact)

Every `quote` must be an **exact substring** of the source minutes — copied byte
for byte, including curly apostrophes, line breaks, and odd spacing from the
original PDF. Do not "clean up" a quote.

This is not a style preference. The ingest gate (`app/quality/gates.py`,
`check_facts`) runs the same exact-substring check against the source text, and a
quote that doesn't match verbatim gets the whole file rejected. The quote is how
the tool proves a fact was actually in the minutes and not made up — so it has
to be reproducible, not paraphrased.

## The few-shot example bank

To steer the model, each fact prompt has hand-verified worked examples baked into
it. They live in `data/examples/facts/` as small JSON files, each shaped
`{"source_excerpt", "correct_facts", "commentary"}` — a real minutes passage and
the gold extraction for it. The prompt builder
(`app/extractor/fact_prompts.py`, `_few_shot_block`) globs every `*.json` there
in sorted order and drops them into the prompt under `## Examples`. The bank
includes **negatives** — examples with `correct_facts: []` — which teach the
model that routine, procedural passages produce nothing, which is as important as
the positives. To improve extraction quality, add more verified examples to that
folder (the same verbatim-quote rule applies to the examples themselves).

## The loop: prep → dispatch → ingest → retry

1. **Prep.** `python cli.py facts --board <CODE>` builds one or more chunk
   prompts at `data/reports/facts/<CODE>_NN_facts_prompt.md` (a board with many
   meetings is split into numbered chunks so each prompt stays a manageable
   size). Each prompt names the exact JSON file to write and the exact meetings
   to cover. Omit `--board` to prep every board.

2. **Dispatch.** For each `*_facts_prompt.md`, dispatch one subagent (preferred
   preset):

   > Read the ENTIRE `data/reports/facts/<CODE>_NN_facts_prompt.md`. Follow its
   > embedded facts-v1 contract exactly and write ONLY the JSON object to the
   > sibling file it names (`data/reports/facts/<CODE>_NN_facts.json`), covering
   > exactly the meetings it lists. Every quote must be an exact substring of the
   > source; use only the controlled vocabulary and only facts in the file;
   > empty arrays are correct for routine meetings.

   Chunks are independent — dispatch them in parallel.

3. **Ingest.** `python cli.py facts --ingest` runs every
   `data/reports/facts/*_facts.json` through the gate and, on pass, writes it to
   the four fact tables in one transaction. Any rejected file leaves a
   `<...>_facts.json.errors.txt` next to it and the command **exits 1** — a hard
   signal that a retry pass is needed. (`facts --validate` runs the gate as a
   dry run without writing; `facts --status` prints per-board coverage.)

4. **Retry.** On a rejected file, re-dispatch the SAME chunk agent:

   > Read `<...>_facts.json.errors.txt` and the original chunk prompt, then
   > regenerate the ENTIRE JSON file fixing every error listed. Never hand-patch
   > the file to slip past the gate.

   Re-run `--ingest`. If the same chunk is rejected a second time, skip it and
   note it — never lower the gate to let a file through.

## Idempotency — safe to re-run

Ingest is designed so re-running a fixed file can only improve the record, never
corrupt it:

- **Per meeting, it's delete-and-replace.** Ingesting a meeting's facts first
  clears that meeting's existing policy / legislation / discipline rows, then
  writes the new ones. Re-running a corrected chunk cleanly replaces the old
  facts for those meetings — no duplicates, no stale rows.
- **Emerging topics upsert on earliest date.** Emerging topics are keyed per
  board on `topic_slug` and keep the **earliest** `first_mentioned_on`. So if a
  later run sees the same new subject again, the "first mentioned" date can only
  move earlier or stay put — re-extraction can only sharpen the timeline, never
  push a first-mention later.

This is why a retry pass is safe: fixing and re-ingesting one board or one chunk
never disturbs the others and never double-counts.
