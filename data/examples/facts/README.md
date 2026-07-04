# Few-shot example bank (facts-v1)

Hand-verified worked examples for the monthly structured-facts extraction (Opus 4.8).

- **How injected:** `app/extractor/fact_prompts.py` (`_few_shot_block`) globs every `*.json`
  here in sorted order and embeds each verbatim inside the prompt under `## Examples`.
  Only files that parse as JSON are embedded; invalid JSON is silently skipped.
- **File shape:** `{"source_excerpt", "correct_facts": [<0-3 fact objects>], "commentary"}`.
  `source_excerpt` is a real minutes passage; `correct_facts` is the gold extraction.
- **Verbatim-quote rule:** every `quote` MUST be an exact substring of that file's
  `source_excerpt` (the ingest gate `app/quality/gates.check_facts` runs the same substring
  check and rejects mismatches). Preserve original bytes — curly apostrophes, `\n`
  line breaks from the source PDF, spacing — do not "clean up" quotes.
- **Enums:** every enum value must come from `app/quality/taxonomy.py`.
- **Negatives:** empty `correct_facts: []` teaches the model that routine/procedural
  excerpts yield nothing — as important as the positives.
