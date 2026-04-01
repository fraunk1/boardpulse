"""Prompt templates for AI summarization."""
from datetime import date


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
    """
    meeting_sections = []
    for m in meetings:
        header = f"### {m['meeting_date']} — {m.get('title') or 'Board Meeting'}"
        doc_texts = []
        for doc in m.get("documents", []):
            if doc.get("content_text"):
                label = f"[{doc['doc_type'].upper()}] {doc['filename']}"
                doc_texts.append(f"**{label}**\n\n{doc['content_text']}")
        if doc_texts:
            meeting_sections.append(header + "\n\n" + "\n\n---\n\n".join(doc_texts))
        else:
            meeting_sections.append(header + "\n\n*(No extracted text available)*")

    all_meetings_text = "\n\n---\n\n".join(meeting_sections)

    # Build a meeting date reference table for citations
    meeting_refs = []
    for i, m in enumerate(meetings):
        meeting_refs.append(f"- `[{m['meeting_date']}]` — {m.get('title') or 'Board Meeting'}")
    meeting_ref_table = "\n".join(meeting_refs)

    return f"""You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **{board_name}** ({state}) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce a YAML frontmatter block with topic tags extracted from the meetings.
3. Produce a structured summary in Markdown with the sections listed below.
4. **Every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/{state}/{board_code}#YYYY-MM-DD))`. This creates a clickable link.
5. Keep the summary between 500-1500 words depending on volume of source material.
6. Write in a professional, neutral tone suitable for a regulatory affairs audience.

## Available Meeting Dates (for citations)

{meeting_ref_table}

## Output Format

Write the summary as a Markdown document with YAML frontmatter. The frontmatter MUST include a `topics` list — choose from these standard tags (use only tags that actually appear in the minutes):

`AI`, `telehealth`, `opioids`, `IMLC`, `CME`, `scope-of-practice`, `disciplinary`, `rulemaking`, `workforce`, `patient-safety`, `controlled-substances`, `physician-wellness`, `licensing`, `legislation`, `public-health`

```markdown
---
topics: ["tag1", "tag2", "tag3"]
board: {board_code}
state: {state}
---

# {board_name} — Meeting Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

## Key Topics Discussed
- Topic description ([YYYY-MM-DD](/board/{state}/{board_code}#YYYY-MM-DD))
- ...

## Notable Actions
- Specific action with date citation ([YYYY-MM-DD](/board/{state}/{board_code}#YYYY-MM-DD))
- ...

## Recurring Themes
- ...

## Noteworthy Items
- ...

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | {board_name} | [Minutes page]({board_code}_MINUTES_URL) |
```

For the Sources table, list each meeting date referenced in the summary. Use this URL as the source link: {minutes_url or 'N/A'}

## Meeting Minutes Data

Board: {board_name}
State: {state}
Code: {board_code}

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
8. Target 3000-5000 words depending on volume of source material.

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

## Recommendations for FSMB

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
