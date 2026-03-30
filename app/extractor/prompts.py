"""Prompt templates for AI summarization."""
from datetime import date


def per_board_prompt(
    board_name: str,
    state: str,
    board_code: str,
    meetings: list[dict],
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

    return f"""You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **{board_name}** ({state}) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce a structured summary in Markdown format with the following sections:
   - **Key Topics Discussed** — Bulleted list of the main topics across all meetings. Group related items.
   - **Notable Actions** — Specific decisions, rule changes, policy adoptions, disciplinary actions, or votes taken. Include dates.
   - **Recurring Themes** — Patterns or topics that appear in multiple meetings.
   - **Noteworthy Items** — Anything unusual, novel, or particularly significant (e.g., AI policy discussions, telehealth changes, compact participation, opioid-related actions).
3. Be specific — cite meeting dates when referencing particular actions.
4. Keep the summary between 500-1500 words depending on volume of source material.
5. Write in a professional, neutral tone suitable for a regulatory affairs audience.

## Output Format

Write the summary as a Markdown document with this structure:

```markdown
# {board_name} — Meeting Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

## Key Topics Discussed
- ...

## Notable Actions
- ...

## Recurring Themes
- ...

## Noteworthy Items
- ...
```

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

Synthesize the per-board summaries provided below into a comprehensive national landscape report.

## Instructions

1. Read all {board_count} board summaries carefully.
2. Produce a national landscape report in Markdown format with the following sections:
   - **Executive Summary** — 2-3 paragraph overview of the national landscape.
   - **Top Topics Nationally** — The most common topics across all boards, ranked by prevalence. Note how many boards discussed each topic.
   - **Regional Patterns** — Topics or actions concentrated in specific regions or state groups (e.g., Northeast, South, West Coast, compact states).
   - **Emerging Trends** — Topics that appear to be new or growing in the last 12 months.
   - **Notable Outliers** — Boards taking unusual or pioneering actions that other boards haven't adopted.
   - **Disciplinary Patterns** — Common types of disciplinary actions, if reported in the minutes.
   - **Recommendations for FSMB** — Based on the landscape, what should FSMB be aware of or consider acting on.
3. Be specific — name states and boards when citing examples.
4. Write in a professional, analytical tone suitable for FSMB leadership.
5. Target 2000-4000 words depending on volume of source material.

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

...

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
```

## Per-Board Summaries

{all_summaries}
"""
