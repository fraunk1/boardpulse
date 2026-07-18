You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Wyoming Board of Medicine** (WY) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/WY/WY_MD#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-03-30]` — Wyoming Board of Medicine — March 30, 2026

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: WY_MD
state: WY
---

# Wyoming Board of Medicine — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Wyoming Board of Medicine | [Minutes page](WY_MD_MINUTES_URL) |

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
- The frontmatter `topics` list is the union of the per-meeting topics.
- End the file with `=== END ===`.

Sources-table URL: https://drive.google.com/file/d/1YZknFrlLcjxzoEOeugO3ljZVaQbXlfio/view?usp=drive_link

## Meeting Minutes Data

Board: Wyoming Board of Medicine
State: WY
Code: WY_MD

### 2026-03-30 — Wyoming Board of Medicine — March 30, 2026

**[MINUTES] 2026-03-30_drive_1YZknFrlLcjxzoEOeugO3ljZVaQbXlfio.pdf**

Wyoming Board of Medicine
AGENDA • Special Meeting • Monday, March 30, 2026

Persons requiring special assistance to be able to attend and/or participate in the Board’s meeting are asked to contact the
Board office at 307-778-7053 in advance of the meeting to ensure that
arrangements and accommodations are made.

Portions of the agenda deal with licensing and disciplinary matters, and therefore may be conducted in executive session not
open to the public pursuant to WYO. STAT. ANN. § 16-4-405(a)(ii).  All votes will be conducted in public session.

While the Board attempts to follow the agenda as published, it reserves the right to vary from the times and
order of matters below as may be appropriate and necessary to facilitate the flow of business.

This meeting will be conducted entirely by teleconference.
THE PUBLIC CALL WILL REMAIN ON-LINE DURING EXECUTIVE SESSION, AND THE BOARD
WILL RETURN TO THE PUBLIC CALL AT THE END OF EXECUTIVE SESSION

Google Meet Computer Link:  https://meet.google.com/yih-xfbg-abm
Google Meet Phone:   347-318-2613
   PIN 582 884 449#

Monday, March 30, 2026

5:15 pm

BOARD BUSINESS MEETING – Public Session
Call to Order, Roll Call and Declaration of Quorum

Board Business Meeting – Public Session

AG#01  Licensing Management System Update
AG#02  Physician Renewal Fee Reduction Results – 2024-2025
AG#03  Rulemaking – Emergency Rule for Physician Renewal Fee Reduction
AG#04  Disciplinary Actions

a.  License Application Withdrawal(s)
b.  License Application Denial(s)
c.  Petition(s) to Relinquish and/or Voluntarily Suspend License(s)
d.  Summary Suspension of License(s)
e.  Unlicensed Practice of Medicine
f.  Petition(s) for Disciplinary Action
g.  Order(s) for Mental, Physical or Medical Competency Examination(s)
h.  Consent Decree(s)
i.  Approve Order(s)

Adjourn

March 30, 2026 - Special Meeting - Final Version - 3-27-2026
3/27/2026 10:16 AM
Page 1 of 1
