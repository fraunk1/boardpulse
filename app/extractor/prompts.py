"""Prompt templates for AI summarization."""
from datetime import date

# Cap per-document text so a board's full prompt fits in a standard subagent
# context window with balanced coverage across all its meetings. Board minutes
# front-load the substantive actions (agenda, votes, disciplinary decisions),
# so this preserves summary quality while bounding the largest boards
# (e.g. VT_MD with 47 documents) to a workable size.
MAX_DOC_CHARS = 12_000

# Total per-board prompt budget (chars). Boards with many sub-committee meetings
# (e.g. NE_MD: 58 meetings / 142 docs in 12 months) can blow past a subagent's
# context window even with the per-doc cap. Meetings arrive newest-first, so we
# keep the most recent ones within this budget (~120K tokens).
MAX_PROMPT_CHARS = 480_000


def per_board_prompt(
    board_name: str,
    state: str,
    board_code: str,
    meetings: list[dict],
    minutes_url: str = "",
) -> str:
    """Build the per-board summary prompt.

    Args:
        board_name: Full name of the board (e.g., "Medical Board of California")
        state: Two-letter state code (e.g., "CA")
        board_code: Board code (e.g., "CA_MD")
        meetings: List of dicts with keys: meeting_date, title, documents.
                  Each document has keys: doc_type, filename, content_text.
                  A meeting MAY also carry keys ``already_summarized`` (bool)
                  and ``stored_summary`` (str). When ``already_summarized`` is
                  true the meeting is rendered as CONTEXT ONLY: its stored
                  summary is shown instead of raw document text, and the
                  authoring instructions tell the model NOT to emit a MEETING
                  block for it. Only unsummarized, text-bearing meetings are
                  TARGETS that require a new MEETING block.
    """
    meeting_sections = []
    running_chars = 0
    omitted_meetings = 0
    for m in meetings:
        header = f"### {m['meeting_date']} — {m.get('title') or 'Board Meeting'}"

        # Context-not-target: an already-summarized meeting renders as its
        # STORED summary under a header that forbids emitting a MEETING block.
        # It grounds the rollup narrative without re-consuming its full docs.
        if m.get("already_summarized"):
            stored = (m.get("stored_summary") or "").strip()
            body = stored or "*(previously summarized; summary text unavailable)*"
            section = (
                header
                + "\n\n**[ALREADY SUMMARIZED — context only; do NOT emit a "
                "MEETING block for this date]**\n\n"
                + body
            )
            if meeting_sections and running_chars + len(section) > MAX_PROMPT_CHARS:
                omitted_meetings = len(meetings) - len(meeting_sections)
                break
            meeting_sections.append(section)
            running_chars += len(section)
            continue

        doc_texts = []
        for doc in m.get("documents", []):
            if doc.get("content_text"):
                label = f"[{doc['doc_type'].upper()}] {doc['filename']}"
                text = doc["content_text"]
                if len(text) > MAX_DOC_CHARS:
                    text = text[:MAX_DOC_CHARS] + "\n\n*[document truncated for length]*"
                doc_texts.append(f"**{label}**\n\n{text}")
        if doc_texts:
            section = header + "\n\n" + "\n\n---\n\n".join(doc_texts)
        else:
            section = header + "\n\n*(No extracted text available)*"
        # Keep the most-recent meetings within a total budget so the prompt fits
        # a subagent context window (meetings arrive newest-first).
        if meeting_sections and running_chars + len(section) > MAX_PROMPT_CHARS:
            omitted_meetings = len(meetings) - len(meeting_sections)
            break
        meeting_sections.append(section)
        running_chars += len(section)

    all_meetings_text = "\n\n---\n\n".join(meeting_sections)
    if omitted_meetings:
        all_meetings_text += (
            f"\n\n---\n\n*[{omitted_meetings} older meeting(s) omitted to fit the "
            "context budget.]*"
        )

    # Build a meeting date reference table for citations. Already-summarized
    # meetings are flagged so the model knows they are context, not targets.
    meeting_refs = []
    target_dates = []
    for m in meetings:
        title = m.get("title") or "Board Meeting"
        if m.get("already_summarized"):
            meeting_refs.append(
                f"- `[{m['meeting_date']}]` — {title} "
                "*(already summarized — context only, no MEETING block)*")
        else:
            meeting_refs.append(f"- `[{m['meeting_date']}]` — {title}")
            target_dates.append(m["meeting_date"])
    meeting_ref_table = "\n".join(meeting_refs)

    return f"""You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **{board_name}** ({state}) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/{state}/{board_code}#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

{meeting_ref_table}

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: {board_code}
state: {state}
---

# {board_name} — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | {board_name} | [Minutes page]({board_code}_MINUTES_URL) |

=== MEETING: YYYY-MM-DD ===
topics: [tag1, tag2]

[80-200 words summarizing ONLY this meeting: what was discussed, decided,
or noted — no cross-meeting narrative, no citation links needed. Plain
prose or short bullets.]

=== MEETING: YYYY-MM-DD ===
topics: []

[...]

=== END ===
```

Rules for the per-meeting sections:
- One `=== MEETING: YYYY-MM-DD ===` block for EVERY meeting above whose text is present, using the exact dates from the reference table, newest first.
- OMIT blocks for meetings marked "(No extracted text available)".
- OMIT blocks for meetings marked "**[ALREADY SUMMARIZED — context only...]**" in the data below (and "*(already summarized — context only, no MEETING block)*" in the reference table). Those meetings already have stored summaries; their text is provided ONLY so you can ground the 12-month rollup narrative. Do NOT emit a `=== MEETING: date ===` block for them. Emit a MEETING block ONLY for the dates that carry full document text and are NOT flagged as already summarized.
- The `topics:` line uses ONLY tags from this standard set that genuinely appear in THAT meeting (an empty `[]` is fine):
  `AI`, `telehealth`, `opioids`, `IMLC`, `CME`, `scope-of-practice`, `disciplinary`, `rulemaking`, `workforce`, `patient-safety`, `controlled-substances`, `physician-wellness`, `licensing`, `legislation`, `public-health`
- The frontmatter `topics` list is the union of the per-meeting topics.
- End the file with `=== END ===`.

Sources-table URL: {minutes_url or 'N/A'}

## Meeting Minutes Data

Board: {board_name}
State: {state}
Code: {board_code}

{all_meetings_text}
"""


def archive_bundle_prompt(
    board_name: str,
    state: str,
    board_code: str,
    year: str,
    meetings: list[dict],
    minutes_url: str = "",
) -> str:
    """Build an ARCHIVE summary prompt for one board / calendar-year chunk.

    Archive files cover ONLY text-bearing meetings older than the rolling
    12-month window that have never been summarized. They are pure
    per-meeting blocks — NO 12-month rollup layer and NO Sources table — so
    the output starts at the first `=== MEETING: ===` block and ends with
    `=== END ===`. The per-meeting block rules are identical to
    per_board_prompt; only the rollup layer is dropped.

    Args:
        board_name: Full board name.
        state: Two-letter state code.
        board_code: Board code (e.g., "CA_MD").
        year: Calendar year label for this chunk (e.g., "2024").
        meetings: List of dicts with keys: meeting_date, title, documents
                  (each document has doc_type, filename, content_text). All
                  meetings passed here are text-bearing TARGETS.
        minutes_url: Board minutes URL (informational only; no Sources table).
    """
    meeting_sections = []
    running_chars = 0
    omitted_meetings = 0
    for m in meetings:
        header = f"### {m['meeting_date']} — {m.get('title') or 'Board Meeting'}"
        doc_texts = []
        for doc in m.get("documents", []):
            if doc.get("content_text"):
                label = f"[{doc['doc_type'].upper()}] {doc['filename']}"
                text = doc["content_text"]
                if len(text) > MAX_DOC_CHARS:
                    text = text[:MAX_DOC_CHARS] + "\n\n*[document truncated for length]*"
                doc_texts.append(f"**{label}**\n\n{text}")
        if doc_texts:
            section = header + "\n\n" + "\n\n---\n\n".join(doc_texts)
        else:
            section = header + "\n\n*(No extracted text available)*"
        if meeting_sections and running_chars + len(section) > MAX_PROMPT_CHARS:
            omitted_meetings = len(meetings) - len(meeting_sections)
            break
        meeting_sections.append(section)
        running_chars += len(section)

    all_meetings_text = "\n\n---\n\n".join(meeting_sections)
    if omitted_meetings:
        all_meetings_text += (
            f"\n\n---\n\n*[{omitted_meetings} meeting(s) from this chunk omitted "
            "to fit the context budget; they will be covered by the next "
            "chunk.]*"
        )

    meeting_refs = []
    for m in meetings:
        meeting_refs.append(
            f"- `[{m['meeting_date']}]` — {m.get('title') or 'Board Meeting'}")
    meeting_ref_table = "\n".join(meeting_refs)

    return f"""You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the ARCHIVED (older than 12 months) meeting minutes for **{board_name}** ({state}) covering the {year} meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE `=== MEETING: YYYY-MM-DD ===` block for every meeting that has extracted text — NOTHING ELSE. There is NO 12-month rollup and NO Sources table in an archive file.
3. Write in a professional, neutral tone suitable for a regulatory affairs audience.
4. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for section headers)

{meeting_ref_table}

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly). The file starts DIRECTLY with the first MEETING block — no frontmatter, no rollup, no Sources table:

```markdown
=== MEETING: YYYY-MM-DD ===
topics: [tag1, tag2]

[80-200 words summarizing ONLY this meeting: what was discussed, decided,
or noted — no cross-meeting narrative, no citation links needed. Plain
prose or short bullets.]

=== MEETING: YYYY-MM-DD ===
topics: []

[...]

=== END ===
```

Rules for the per-meeting sections:
- One `=== MEETING: YYYY-MM-DD ===` block for EVERY meeting above whose text is present, using the exact dates from the reference table, newest first.
- OMIT blocks for meetings marked "(No extracted text available)".
- The `topics:` line uses ONLY tags from this standard set that genuinely appear in THAT meeting (an empty `[]` is fine):
  `AI`, `telehealth`, `opioids`, `IMLC`, `CME`, `scope-of-practice`, `disciplinary`, `rulemaking`, `workforce`, `patient-safety`, `controlled-substances`, `physician-wellness`, `licensing`, `legislation`, `public-health`
- Do NOT write any 12-month rollup, board summary, YAML frontmatter, or `## Sources` table. The file is per-meeting blocks only.
- End the file with `=== END ===`.

## Meeting Minutes Data

Board: {board_name}
State: {state}
Code: {board_code}
Year: {year}

{all_meetings_text}
"""


def national_synthesis_prompt(
    board_summaries: list[dict],
    report_date: date,
) -> str:
    """Build the national landscape synthesis prompt.

    Args:
        board_summaries: List of dicts with keys: board_name, state, board_code, summary_text.
        report_date: Date for the report header.
    """
    summary_sections = []
    for bs in board_summaries:
        summary_sections.append(
            f"## {bs['board_name']} ({bs['state']})\n\n{bs['summary_text']}"
        )

    all_summaries = "\n\n---\n\n".join(summary_sections)
    board_count = len(board_summaries)
    states = sorted(set(bs["state"] for bs in board_summaries))
    states_str = ", ".join(states)

    return f"""You are an expert analyst producing a national landscape report on state medical board activity.

## Task

Synthesize the per-board summaries provided below into a comprehensive national landscape report with full citations.

## Instructions

1. Read all {board_count} board summaries carefully.
2. Produce a national landscape report in Markdown format with the sections listed below.
3. **Every factual claim MUST include an inline citation** linking to the specific board and meeting. Use the citation links already present in the per-board summaries — preserve them in your synthesis.
4. When citing a board action, use the format: `([STATE Board, YYYY-MM-DD](/board/STATE/CODE#YYYY-MM-DD))` — these are clickable links in the boardpulse dashboard.
5. Include a **Bibliography** section at the end with numbered footnotes linking to the original board websites.
6. Be specific — name states and boards when citing examples.
7. Write in a professional, analytical tone suitable for FSMB leadership.
8. Be DESCRIPTIVE and analytical, NOT prescriptive. Do not write "FSMB should..." or issue directives. Frame the closing section as considerations and open questions the federation may wish to weigh — surface patterns, tensions, and questions for further discussion, never recommended actions.
9. Target 3000-5000 words depending on volume of source material.

## Output Format

Write the report as a Markdown document:

```markdown
# National Medical Board Landscape Report

**Date:** {report_date.isoformat()}
**Boards analyzed:** {board_count}
**States covered:** {states_str}

## Executive Summary

...

## Top Topics Nationally

1. **Topic** — *N boards.* Description with citations ([STATE, YYYY-MM-DD](/board/STATE/CODE#YYYY-MM-DD))...

## Regional Patterns

...

## Emerging Trends

...

## Notable Outliers

...

## Disciplinary Patterns

...

## Considerations and Open Questions for FSMB

*(Descriptive and analytical only — patterns, tensions, and questions for further discussion. No prescriptive "FSMB should..." directives.)*

...

---

## Bibliography

| # | Board | State | Source URL |
|---|-------|-------|-----------|
| 1 | Board Name | ST | [Minutes page](https://...) |
| 2 | ... | ... | ... |
```

List every board referenced in the report in the bibliography, with a link to their official minutes page.

## Per-Board Summaries

{all_summaries}
"""
