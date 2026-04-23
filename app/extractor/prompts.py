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


def per_meeting_summary_prompt(
    board_name: str,
    meeting_date: str,
    meeting_title: str,
    doc_sections: list[dict],
) -> str:
    """Build a prompt for generating a narrative meeting summary with page citations.

    Produces a 200-400 word prose recap with inline page citations like (p.3)
    that link to the source document page.

    Args:
        board_name: Full board name
        meeting_date: ISO date string
        meeting_title: Meeting title
        doc_sections: List of dicts with keys:
            - doc_id: Document ID
            - doc_type: "minutes", "agenda", etc.
            - filename: Document filename
            - pages: list of dicts with keys: page_number, text
    """
    # Build page-segmented text
    sections = []
    doc_count = len(doc_sections)
    for doc in doc_sections:
        label = doc["doc_type"].upper()
        if doc_count > 1:
            doc_header = f"=== DOCUMENT: [{label}] {doc['filename']} (doc_id={doc['doc_id']}) ==="
        else:
            doc_header = f"=== DOCUMENT: [{label}] {doc['filename']} ==="
        page_texts = []
        for pg in doc["pages"]:
            text = pg["text"].strip()
            if text:
                page_texts.append(f"--- PAGE {pg['page_number']} ---\n{text}")
        if page_texts:
            sections.append(doc_header + "\n\n" + "\n\n".join(page_texts))

    combined = "\n\n".join(sections) if sections else "(no document text available)"
    if len(combined) > 40000:
        combined = combined[:40000] + "\n\n[... truncated ...]"

    # Citation format depends on number of documents
    if doc_count <= 1:
        cite_instruction = 'Cite specific pages inline using the format (p.3) — just the page number.'
        cite_example = '"The board voted to adopt the rule amendment (p.7)."'
    else:
        cite_instruction = (
            'Cite specific pages inline using the format (Minutes p.3) or (Agenda p.2) — '
            'use the document type to disambiguate when the meeting has multiple documents.'
        )
        cite_example = '"The board voted to adopt the rule amendment (Minutes p.7), as outlined in the proposed agenda (Agenda p.2)."'

    return f"""Summarize this {board_name} meeting ({meeting_date}) as a narrative recap with page citations.

Write 200-400 words of prose. Cover:
- What was discussed and decided
- Specific actions taken (votes, rule adoptions, policy changes)
- Disciplinary cases (names, case numbers, outcomes if available)
- Committee reports or notable public comments
- Anything unusual or first-of-its-kind

Citation rules:
- {cite_instruction}
- Every factual claim should cite the page where it appears.
- Example: {cite_example}
- Only cite pages that actually contain the referenced content.

Writing rules:
- Past tense, third person, professional tone
- Plain prose paragraphs only — no bullet points, no headers, no markdown formatting
- Do not include the meeting date, board name, meeting type, or topic tags — those are stored separately
- Do not speculate or editorialize — only report what the documents say
- If the documents are mostly closed-session notices with little public content, say so briefly

## Document Text (page-segmented)

{combined}"""


def board_brief_prompt(
    board_name: str,
    board_code: str,
    state: str,
    period_label: str,
    meeting_summaries: list[dict],
) -> str:
    """Build a prompt for generating a period brief (quarter/half-year/year) with citations.

    Args:
        board_name: Full board name
        board_code: Board code (e.g., "CA_MD")
        state: Two-letter state code
        period_label: "quarter", "half-year", or "year"
        meeting_summaries: List of dicts with keys:
            meeting_id, meeting_date, title, summary,
            docs: list of {doc_id, doc_type}
    """
    meeting_lines = []
    ref_lines = []
    ref_num = 1

    for m in meeting_summaries:
        summary = m.get("summary") or "(no summary available)"
        date_str = m["meeting_date"]
        docs = m.get("docs", [])

        # Build reference entries for this meeting
        meeting_refs = []
        for doc in docs:
            ref_lines.append(
                f"[{ref_num}] {date_str} {doc['doc_type'].capitalize()} → "
                f"/meeting/{m['meeting_id']}#doc-{doc['doc_id']}-p{{PAGE}}"
            )
            meeting_refs.append(f"(ref {ref_num} = {doc['doc_type'].capitalize()})")
            ref_num += 1

        refs_label = " ".join(meeting_refs) if meeting_refs else ""
        meeting_lines.append(
            f"**{date_str}** — {m.get('title') or 'Board Meeting'} {refs_label}\n{summary}"
        )

    meetings_text = "\n\n---\n\n".join(meeting_lines)
    ref_table = "\n".join(ref_lines) if ref_lines else "(no references available)"
    count = len(meeting_summaries)

    return f"""Summarize the recent activity for {board_name} ({state}) over the past {period_label}.

You are given {count} meeting summaries below. Produce a brief overview in 3-5 sentences that:
- Highlights the most important actions or trends
- Notes any recurring themes
- Tells a regulatory affairs reviewer whether deeper investigation is warranted

## Citation Rules

Every factual claim MUST include a superscript citation number. Use the reference table below.

Format: Write the citation as {{N}} immediately after the claim, where N is the reference number.
Example: "The board voted to eliminate jurisprudence exams{{3}} and adopted a nutrition CME requirement{{4}}."

When citing a specific page, write {{N:p.X}} — for example {{3:p.4}} means reference 3, page 4.
When no specific page is needed, just use {{N}}.

## Reference Table

{ref_table}

## Writing Rules

- Plain text paragraphs only — no markdown, no bullet points, no headers
- Every factual claim needs a citation
- 3-5 sentences total

## Meeting Summaries ({period_label})

{meetings_text}"""


def per_meeting_tldr_prompt(
    board_name: str,
    meeting_date: str,
    meeting_title: str,
    doc_texts: list[str],
) -> str:
    """Build a prompt for generating a short TLDR meeting summary.

    Args:
        board_name: Full board name
        meeting_date: ISO date string
        meeting_title: Meeting title
        doc_texts: List of extracted document texts for this meeting
    """
    combined = "\n\n---\n\n".join(doc_texts) if doc_texts else "(no document text available)"
    # Truncate to avoid blowing context on huge docs
    if len(combined) > 15000:
        combined = combined[:15000] + "\n\n[... truncated ...]"

    return f"""Summarize this {board_name} meeting ({meeting_date}) in 2-3 sentences.

Focus on: what happened, any notable actions taken, and whether further review is warranted.
Write plain text only. No markdown, no bullet points, no headers, no citations.

## Meeting: {meeting_title or 'Board Meeting'} — {meeting_date}

{combined}"""


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
