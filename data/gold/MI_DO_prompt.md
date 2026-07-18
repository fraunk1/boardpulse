You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Michigan Board of Osteopathic Medicine and Surgery** (MI) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/MI/MI_DO#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-06-04]` — Michigan Board of Osteopathic Medicine and Surgery — June 04, 2026
- `[2026-04-02]` — Michigan Board of Osteopathic Medicine and Surgery — April 02, 2026
- `[2026-02-05]` — Michigan Board of Osteopathic Medicine and Surgery — February 05, 2026
- `[2025-12-04]` — Michigan Board of Osteopathic Medicine and Surgery — December 04, 2025
- `[2025-10-02]` — Michigan Board of Osteopathic Medicine and Surgery — October 02, 2025
- `[2025-08-07]` — Michigan Board of Osteopathic Medicine and Surgery — August 07, 2025

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: MI_DO
state: MI
---

# Michigan Board of Osteopathic Medicine and Surgery — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Michigan Board of Osteopathic Medicine and Surgery | [Minutes page](MI_DO_MINUTES_URL) |

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

Sources-table URL: https://www.michigan.gov/lara/bureau-list/bpl/health/hp-lic-health-prof/osteo/board/osteopathic-medicine-board-meeting-agendas-and-minutes

## Meeting Minutes Data

Board: Michigan Board of Osteopathic Medicine and Surgery
State: MI
Code: MI_DO

### 2026-06-04 — Michigan Board of Osteopathic Medicine and Surgery — June 04, 2026

**[MINUTES] 2026-06-04_6-4-2026-Osteopathic-Medicine-and-Surgery-Full-Board-Cancellation_.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

PUBLIC NOTICE

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE
AND SURGERY

ANNOUNCES A

CANCELLATION

OF THE

FULL BOARD AND DISCIPLINARY SUBCOMMITTEE
MEETING ON

JUNE 4, 2026.

All meetings are conducted in accordance with Public Act 267 of 1976, as amended,
and are open to the public. Further information concerning a specific meeting can be
obtained from the Board office.

Dated: June 4, 2026

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199
LARA is an equal opportunity employer/program

---

### 2026-04-02 — Michigan Board of Osteopathic Medicine and Surgery — April 02, 2026

**[AGENDA] 2026-04-02_4-2-2026-Osteo-DSC--Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND SURGERY
DISCIPLINARY SUBCOMMITTEE

APRIL 2, 2026

(Immediately following the full Board meeting which begins at 9:00 a.m.)

Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

Agenda

1.

2.

3.

4.

5.

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from Meeting of February 5, 2026

Regulatory Considerations

A.  Consent Orders and Stipulation

1.  Joel Michael Adelsberg, DO
2.  Joel Steven Jones, DO
3.  Billy Ralph Nordyke, DO (Conferee Rollinger)
4.  Forrest Dean Robart, DO
5.  Laurence Ernest Yung, DO

B.  Proposal for Decision – Administrative Complaint

•  David P. Jankowski, DO

6.

7.

Public Comment

Announcements

The  next  regularly  scheduled  meeting  will  be  held  June  4,  2026,  immediately
following  the  full  board  meeting  scheduled  to  begin  at  9:00  a.m.  at  611  West
Ottawa Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic
Medicine & Surgery
Disciplinary Subcommittee Agenda
April 2, 2026
Page 2 of 2

8.

Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/85684125059?pwd=FxGN8Y10wT2GLKlI0ZkluL5SqNxMil.1

Phone Number: (1) 408-961-3928

Meeting ID: 856 8412 5059

Passcode: 742258

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In the event of a disconnection caused by the meeting host, the Board will be in recess.
Every effort will be made to reestablish a publicly accessible connection. If the host is
unable to do so within a period of 30 minutes from the time of the disconnection, the
Board  will  adjourn  and  not  address  any  new  business  until  its  next  meeting.  Any
decisions made prior to the disconnection will be binding. The board will not recess or
adjourn  due  to  technical  or  other  issues  experienced  by  individual members  of  the
public that render them unable to attend or participate in the meeting.

the  public  who  require  accommodation

to
Members  of
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/en/mpsc/consumer/telecommunications/michigan-relay.

for  equal  access

Please contact the department at BPL-BoardSupport@Michigan.gov if you need other
accommodations or have questions.

---

**[AGENDA] 2026-04-02_4-2-2026-Osteopathic-Medicine-and-Surgery--Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND
SURGERY

APRIL 2, 2026
9:00 a.m.

Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

Agenda

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from meeting February 5, 2026

Regulatory Considerations

1.

2.

3.

4.

5.

None

6.

Old Business

None

7.

New Business

A.  Douglas Wigton – CE Waiver Request
B.  Chair Report
C.  Department Update

8.

9.

Public Comment

Announcements

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine
Agenda
April 2, 2026
Page 2 of 2

The next regularly scheduled meeting will be held June 4, 2026, at 9:00 a.m. at
611  W.  Ottawa  Street,  Upper-  Level  Conference  Center  Room  4,  Lansing,
Michigan 48933.

10.

 Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/85684125059?pwd=FxGN8Y10wT2GLKlI0ZkluL5SqNxMil.1

Phone Number: (1) 408-961-3928

Meeting ID: 856 8412 5059

Passcode: 742258

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In the event of a disconnection caused by the meeting host, the Board will be in recess.
Every effort will be made to reestablish a publicly accessible connection. If the host is
unable to do so within a period of 30 minutes from the time of the disconnection, the
Board  will  adjourn  and  not  address  any  new  business  until  its  next  meeting.  Any
decisions made prior to the disconnection will be binding. The board will not recess or
adjourn  due  to  technical  or  other  issues  experienced  by  individual  members  of  the
public that render them unable to attend or participate in the meeting.

the  public  who  require  accommodation

Members  of
to
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/en/mpsc/consumer/telecommunications/michigan-relay.

for  equal  access

Please contact the department at BPL-BoardSupport@Michigan.gov if you need other
accommodations or have questions.

---

### 2026-02-05 — Michigan Board of Osteopathic Medicine and Surgery — February 05, 2026

**[MINUTES] 2026-02-05_2-5-2026-Osteo-DSC-Approved-Minutes.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
 DIRECTOR

BOARD OF OSTEOPATHIC MEDICINE & SURGERY
DISCIPLINARY SUBCOMMITTEE

FEBRUARY 5, 2026, MEETING

APPROVED MINUTES

In  accordance  with  the  Open  Meetings  Act,  1976  PA  267,  as  amended,  the  Michigan
Board of Osteopathic Medicine & Surgery Disciplinary Subcommittee met on February 5,
2026, at 611 West Ottawa Street, Upper-Level Conference Room 4, Lansing, Michigan
48933.

CALL TO ORDER

Ayanna Neal, Public Member, Chairperson, called the meeting to order at 9:59 a.m.

Members Present:  Ayanna Neal, J.D., Public Member, Chairperson

Khawaja Ikram, D.O. (Alternate)
Ben Rimes, Public Member
Jeffrey Rosenbaum, D.O.

Members Absent:  Craig Glines, D.O., MSBA
Samantha Danek, PA-C

Staff Present:

Robert Payne, Senior Analyst, Compliance Section
Kimmy Darnell, Board Support Technician,
Boards and Committees Section

Weston MacIntosh, JD, Departmental Specialist,

Boards and Committees Section

Michele Wagner-Gutkowski, JD, Assistant Attorney General

APPROVAL OF AGENDA

MOTION by Rosenbaum, seconded by Ikram, to approve the agenda as presented.

A voice vote was held.

MOTION PREVAILED

APPROVAL OF MINUTES

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
February 5, 2026
Page 2 of 5

MOTION by Rimes, seconded by Ikram, to approve the December 4, 2025, meeting
minutes as presented.

A voice vote was held.

MOTION PREVAILED

Disciplinary Subcommittee Master Resolution

MacIntosh presented the resolution.

MOTION  by  Rosenbaum,  seconded  by  Rimes,  to  approve  the  Disciplinary
Subcommittee Master Resolution.

A roll call vote was taken:

MOTION PREVAILED

Yeas: Rosenbaum, Rimes, Ikram, Neal
Nays:  None

REGULATORY CONSIDERATIONS

Consent Orders and Stipulations

Jason Edward Brunt, DO

MOTION by Ikram, seconded by Rimes, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION  by  Rimes,  seconded  by  Rosebaum,  to  accept  the  Consent  Order  and
Stipulation.

A roll call vote was taken:

Yeas: Rosenbaum, Rimes, Ikram, Neal
Nays:  None

MOTION PREVAILED

Charles Mok, DO

MOTION by Ikram, seconded by Rosenbaum, to discuss the matter.

A voice vote followed.

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
February 5, 2026
Page 3 of 5

MOTION PREVAILED

Discussion held.

MOTION by Rosenbaum, seconded by Rimes, to accept the Consent Order and
Stipulation.

A roll call vote was taken:

Yeas: Rosenbaum, Rimes, Ikram, Neal
Nays:  None

MOTION PREVAILED

Annemarie Poleck, DO

MOTION by Ikram, seconded by Rimes, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

care

involving

non-malignant

pain  management

MOTION  by  Rosenbaum,  seconded  by  Ikram,  to  reject  the  Consent  Order  and
Stipulation with a counteroffer. Counteroffer terms include: Two year limitation of
Respondent’s license.  Limitation terms: Respondent is prohibited from providing
controlled
chronic
substances.   Upon  successful  completion  of,  and  compliance  with,  the  terms  of
probation set forth below, Respondent’s license shall be automatically reclassified
to  a  full  and  unencumbered  license  at  the  conclusion  of  the  limitation
the  period  of
period. Probation
limitation. Probation  terms:  1)  Within  one  year,  complete  15  hours  of  continuing
education  of  Category  1A  in  the  area  of  osteopathic  addiction  medicine  pre-
approved  by  the  board  chair  or  designee,  which  shall  not  count  towards  re-
licensure requirements.  2) Four chart reviews including a minimum of ten patient
charts by a board approved reviewer.  Chart reviews shall occur every six months,
and  shall  focus  on  Respondent’s  prescribing  practices,  and  be  submitted  to  the
department.  Additionally, a $4,000.00 fine is due within 90 days. Count II of the
complaint is dismissed.

to  run  concurrently  with

two  years

for

A roll call vote was taken:

MOTION PREVAILED

William John Powers, DO

Yeas: Rosenbaum, Rimes, Ikram, Neal
Nays:  None

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
February 5, 2026
Page 4 of 5

MOTION by Rosenbaum, seconded by Rimes, to accept the Consent Order and
Stipulation.

Discussion was held.

A roll call vote was taken:

MOTION PREVAILED

Craig Ivan Schwartz, DO

Yeas: Rosenbaum, Rimes, Ikram, Neal
Nays:  None

MOTION by Ikram, seconded by Rimes, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION by Rosenbaum, seconded by Rimes, to accept the Consent Order and
Stipulation.

A roll call vote was taken:

Yeas: Rosenbaum, Rimes, Ikram, Neal
Nays:  None

MOTION PREVAILED

Order of Dismissal

Gerard Joseph Mahoney, DO

MOTION by Ikram, seconded by Rosenbaum, to accept the Order of Dismissal.

A roll call vote was taken:

Yeas: Rosenbaum, Rimes, Ikram, Neal
Nays:  None

MOTION PREVAILED

PUBLIC COMMENT

None

ANNOUNCEMENTS

The  next  regularly  scheduled  meeting  is  on  April  2,  2026,  immediately  following  the
regularly  scheduled  Michigan  Board  of  Osteopathic  Medicine  and  Surgery  meeting
scheduled  to  begin  at  9:00  a.m.  at  611  West  Ottawa  Street,  Upper-Level  Conference
Center Room 4, Lansing, Michigan 48933.

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
February 5, 2026
Page 5 of 5

ADJOURNMENT

MOTION by Rosenbaum, seconded by Rimes, to adjourn the meeting at 10:36 a.m.

A voice vote was held.

MOTION PREVAILED

Minutes approved by the Board on April 2, 2026.

Prepared by:
Kimmy Darnell, Board Support Technician
Bureau of Professional Licensing

February 5, 2026

---

**[AGENDA] 2026-02-05_2-5-2026-Osteo-DSC-Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND SURGERY
DISCIPLINARY SUBCOMMITTEE

FEBRUARY 5, 2026

9:00 a.m.
Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

Agenda

1.

2.

3.

4.

5.

6.

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from Meeting of December 4, 2025

Master Disciplinary Subcommittee Resolution

Regulatory Considerations

A.  Consent Orders and Stipulation
1.  Jason Edward Brunt, DO
2.  Charles Mok, DO (Conferee Everett)
3.  Annemarie Poleck, DO (Conferee Rollinger)
4.  William John Powers, DO (Conferee Bell)
5.  Craig Ivan Schwartz, DO

B.  Order of Dismissal

  Gerard Joseph Mahoney, DO

7.

8.

Public Comment

Announcements

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic
Medicine & Surgery
Disciplinary Subcommittee Agenda
February 5, 2026
Page 2 of 2

The  next  regularly  scheduled  meeting  will  be  held  April  2,  2026,  immediately
following  the  full  board  meeting  scheduled  to  begin  at  9:00  a.m.  at  611  West
Ottawa Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.

9.

Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/85684125059?pwd=FxGN8Y10wT2GLKlI0ZkluL5SqNxMil.1

Phone Number: (1) 408-961-3928

Meeting ID: 856 8412 5059

Passcode: 742258

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In the event of a disconnection caused by the meeting host, the Board will be in recess.
Every effort will be made to reestablish a publicly accessible connection. If the host is
unable to do so within a period of 30 minutes from the time of the disconnection, the
Board  will  adjourn  and  not  address  any  new  business  until  its  next  meeting.  Any
decisions made prior to the disconnection will be binding. The board will not recess or
adjourn  due  to  technical  or  other  issues  experienced  by  individual  members  of  the
public that render them unable to attend or participate in the meeting.

the  public  who  require  accommodation

to
Members  of
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/en/mpsc/consumer/telecommunications/michigan-relay

for  equal  access

Please  contact  the  department  at  BPL-BoardSupport@michigan.gov  if  you  need
other accommodations or have questions.

---

**[MINUTES] 2026-02-05_2-5-2026-Osteo-Full-Board-Approved-Minutes.pdf**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

STATE OF  MICHIGAN
GRETCHEN  WHITMER   DEPARTMENT OF  LICENSING AND REGULATORY  AFFAIRS   MARLON  I.  BROWN,  DPA
| GOVERNOR   |     |     | LANSING   | DIRECTOR   |
| ---------- | --- | --- | --------- | ---------- |

MICHIGAN  BOARD  OF  OSTEOPATHIC
MEDICINE &  SURGERY

FEBRUARY 5,  2026,  MEETING

APPROVED  MINUTES

In  accordance  with  the  Open  Meetings Act,  1976  PA  267, as amended, the  Michigan
Board of Osteopathic Medicine  and  Surgery met on  February 5, 2026, at 611  West Ottawa
Street, Upper-Level Conference Room  4, Lansing, Michigan 48933.

CALL TO ORDER

Stephen Bell, D.O., Chairperson, called  the meeting to order at 9:04  a.m.

| Members Present:   | Stephen Bell, D.O., Chairperson    |     |     |     |
| ------------------ | ---------------------------------- | --- | --- | --- |
|                    | Ronald Bishop, D.O.                |     |     |     |
|                    |  John Everett, D.O.                |     |     |     |
|                    | Khawaja Ikram, D.O.                |     |     |     |
|                    | Delores Mitchell, Public Member    |     |     |     |
|                    | Ayanna Neal, J.D., Public Member   |     |     |     |
                                 Ben Rimes, Public Member
Jeffrey Rosenbaum, D.O.
|                                 |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- |
Members Absent:      Craig Glines, D.O., MSBA, Vice-Chairperson
|     | Samantha Danek, PA-C       |     |     |     |
| --- | -------------------------- | --- | --- | --- |
|     | Kathleen Rollinger, D.O.   |     |     |     |
|     |                            |     |     |     |
Staff Present:   Robert Payne, Senior Analyst, Compliance Section
|     | Weston MacIntosh,  JD,  Departmental Specialist,           |                                 |     |     |
| --- | ---------------------------------------------------------- | ------------------------------- | --- | --- |
|     |                                                            | Boards and Committees Section   |     |     |
|     | Michele Wagner-Gutkowski, JD, Assistant Attorney General   |                                 |     |     |
 Kimmy Darnell,  Board Support  Technician,
|     |     | Boards  and Committees Section   |     |     |
| --- | --- | -------------------------------- | --- | --- |

APPROVAL OF AGENDA

MOTION by  Ikram, seconded by  Rosenbaum, to approve the  agenda  as presented.

BUREAU  OF  PROFESSIONAL  LICENSING
611  W.  OTTAWA  •   P.O.  BOX  30670  •   LANSING,  MICHIGAN 48909
www.michigan.gov/bpl  •   517-241-0199

LARA  is  an  equal opportunity  employer/program

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
February 5, 2026
Page 2 of 5
A voice vote was held.
MOTION PREVAILED
APPROVAL OF MINUTES
MOTION by Ikram, seconded by Bishop, to approve the December 4, 2025, meeting
minutes as written.
A voice vote was held.
MOTION PREVAILED
REGULATORY CONSIDERATIONS
Proposal for Decision - Reinstatement
John Patrick Swan, D.O.
Bishop recused himself from the matter.
MOTION by Mitchell, seconded by Ikram, to discuss.
A voice vote was held.
MOTION PREVAILED
Discussion was held.
MOTION by Neal, seconded by Rosenbaum, to grant reinstatement with a five year
limitation prohibiting the Petitioner. Limitation terms: 1) Petitioner shall not obtain,
possess, prescribe, dispense, or administer any drug designated as a controlled
substance under the Michigan Public Health Code or under federal law, unless the
controlled substance is prescribed or dispensed by a licensed physician for Petitioner as
a patient. 2) Petitioner shall not obtain, possess, prescribe, dispense, or issue any
physician certification to any person seeking to become a registered patient or caregiver
of the Michigan Medical Marihuana Program. Reclassification of the license is not
automatic, and Petitioner must petition for reclassification of the license at the conclusion
of the limitation period. Probation for five years to run concurrently with the period of
limitation. Probation terms: 1) Within 45 days of the Order’s effective date, Petitioner shall
contact the Health Professional Recovery Program (HPRP) for an evaluation to determine
eligibility for the program. If HPRP determines that Petitioner is appropriate for
monitoring, Petitioner shall promptly enter into and comply with the terms of a disciplinary
monitoring agreement with HPRP. 2) Petitioner must submit satisfactory quarterly
employer reports when employed as a physician and reports of non-employment during
periods of unemployment. 3) No violation of the Michigan Public Health

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
February 5, 2026
Page 3 of 5
Code. Additionally, the $30,000.00 fine ordered in file number 51-24-001180 is brought
forth into this Order and is due within one year from this Order’s effective date.
A roll call vote was taken: Yeas: Everett, Ikram, Mitchell, Neal, Rimes, Rosenbaum, Bell
Nays: None
Recuse: Bishop
MOTION PREVAILED
OLD BUSINESS
None
NEW BUSINESS
Elections
MacIntosh ran the election for chairperson.
MOTION by Rosenbaum, seconded by Ikram, to re-elect Bell as chairperson.
A roll call vote was taken: Yeas: Bishop, Everett, Ikram, Mitchell, Neal, Rimes,
Rosenbaum, Bell
Nays: None
MOTION PREVAILED
MacIntosh ran the election for vice chairperson.
MOTION by Bell, seconded by Rosenbaum, to elect Ikram as vice-chairperson.
A roll call vote was taken: Yeas: Bishop, Everett, Ikram, Mitchell, Neal, Rimes,
Rosenbaum, Bell
Nays: None
MOTION PREVAILED
Committee Assignments
Bell made the following committee assignments:
Disciplinary Subcommittee
Neal – Public Chairperson
Rimes – Public
Danek - Professional
Glines – Professional
Rosenbaum – Professional
Rollinger – Professional Alternate

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
February 5, 2026
Page 4 of 5
Mitchell – Public Alternate
Board Review Panel
Bell
Bishop
Everett
Ikram – Alternate
Rules
Bell
Glines
Neal
Ikram
HPRP Annual Report
MacIntosh provided an overview of the HPRP program. MacIntosh presented the HPRP
Executive Summary: October 1, 2024, through September 30, 2025.
Master Resolution Review
MacIntosh provided an overview of the Board of Osteopathic Medicine and Surgery
Master Resolution. No changes were made.
Conflict of Interest
MacIntosh helped the members with completion of the Disclosure of Interest form (C-46).
Chair Report
Bell and Ikram thanked the board for electing them to chair and vice chair.
Department Update
MacIntosh reminded the board to check their state e-mail at least once a week.
MacIntosh informed the board that there will be new member board training via Zoom on
March 11, 2026. All are welcome to attend.
Payne reminded the board that any egress/email issues should be directed to Board
Support as soon as possible.
PUBLIC COMMENT
None

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
February 5, 2026
Page 5 of 5
ANNOUNCEMENTS
The next regularly scheduled meeting is April 2, 2026, at 9:00 a.m. at 611 West Ottawa
Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.
ADJOURNMENT
MOTION by Rosenbaum, seconded by Ikram, to adjourn the meeting at 9:41 a.m.
A voice vote was held.
MOTION PREVAILED
Minutes approved by the Board on April 2, 2026.
Prepared by:
Kimmy Darnell, Board Support Technician February 5, 2026
Bureau of Professional Licensing

---

**[AGENDA] 2026-02-05_2-5-2026-Osteopathic-Medicine-and-Surgery-Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND
SURGERY

FEBRUARY 5, 2026
9:00 a.m.

Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

Agenda

1.

2.

3.

4.

5.

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from meeting December 4, 2025

Regulatory Considerations

Proposal for Decision – Reinstatement

  John Patrick Swan, D.O.

6.

Old Business

None

7.

New Business

A.  Elections
B.  Committee Assignments
C.  HPRP Annual Report
D.  Master Resolution Review
E.  Conflict of Interest
F.  Chair Report
G.  Department Update

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine
Agenda
February 5, 2026
Page 2 of 2

8.

9.

Public Comment

Announcements

The next regularly scheduled meeting will be held April 2, 2026, at 9:00 a.m. at
611  W.  Ottawa  Street,  Upper-  Level  Conference  Center  Room  4,  Lansing,
Michigan 48933.

10.

Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/85684125059?pwd=FxGN8Y10wT2GLKlI0ZkluL5SqNxMil.1

Phone Number: (1) 408-961-3928

Meeting ID: 856 8412 5059

Passcode: 742258

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In the event of a disconnection caused by the meeting host, the Board will be in recess.
Every effort will be made to reestablish a publicly accessible connection. If the host is
unable to do so within a period of 30 minutes from the time of the disconnection, the
Board  will  adjourn  and  not  address  any  new  business  until  its  next  meeting.  Any
decisions made prior to the disconnection will be binding. The board will not recess or
adjourn  due  to  technical  or  other  issues  experienced  by  individual  members  of  the
public that render them unable to attend or participate in the meeting.

the  public  who  require  accommodation

Members  of
to
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/en/mpsc/consumer/telecommunications/michigan-relay

for  equal  access

Please  contact  the  department  at  BPL-BoardSupport@michigan.gov  if  you  need
other accommodations or have questions.

---

### 2025-12-04 — Michigan Board of Osteopathic Medicine and Surgery — December 04, 2025

**[MINUTES] 2025-12-04_12-4-2025-Osteo-DSC-Approved-Minutes.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
 DIRECTOR

BOARD OF OSTEOPATHIC MEDICINE & SURGERY
DISCIPLINARY SUBCOMMITTEE

DECEMBER 4, 2025, MEETING

APPROVED MINUTES

In  accordance  with  the  Open  Meetings  Act,  1976  PA  267,  as  amended,  the  Michigan
Board of Osteopathic Medicine & Surgery Disciplinary Subcommittee met on December
4, 2025, at 611 West Ottawa Street, Upper-Level Conference Room 4, Lansing, Michigan
48933.

CALL TO ORDER

Ayanna Neal, Public Member, Chairperson, called the meeting to order at 9:55 a.m.

Members Present:  Ayanna Neal, J.D., Public Member, Chairperson
Samantha Danek, PA-C
Khawaja Ikram, D.O. (Alternate)
Ben Rimes, Public Member

Members Absent:  Craig Glines, D.O., MSBA
Jeffrey Rosenbaum, D.O.

Staff Present:

Marshall Hooks, Senior Analyst, Compliance Section
Robert Payne, Senior Analyst, Compliance Section
Kimmy Darnell, Board Support Technician,
Boards and Committees Section

Weston MacIntosh, JD, Departmental Specialist,

Boards and Committees Section

Michele Wagner-Gutkowski, JD, Assistant Attorney General

APPROVAL OF AGENDA

MOTION by Ikram, seconded by Rimes, to approve the agenda as presented.

A voice vote was held.

MOTION PREVAILED

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
December 5, 2025
Page 2 of 4

APPROVAL OF MINUTES

MOTION  by  Ikram,  seconded  by  Rimes,  to  approve  the  October  2,  2025,  meeting
minutes as presented.

A voice vote was held.

MOTION PREVAILED

REGULATORY CONSIDERATIONS

Proposal for Decision

Reginald Sharpe, DO

MOTION by Danek, seconded by Rimes, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION by Danek seconded by Ikram, to accept the Proposal for Decision and
dismiss the complaint.

A roll call vote was taken:

MOTION PREVAILED

Yeas: Danek, Rimes, Ikram, Neal
Nays:  None

Consent Orders and Stipulations

Jon Michael Banas, DO

MOTION by Ikram, seconded by Danek, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION  by  Ikram,  seconded  by  Danek,  to  reject  the  Consent  Order  and
Stipulation with a counter- offer. The counter-offer terms include probation for one
(1)  year  with  a  minimum  of  four  (4)  quarterly  reviewer  reports  and  specified

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
December 5, 2025
Page 3 of 4

continuing  education  shall  be  completed  within  six  (6)  months  of  the  Order’s
effective date.  All remaining terms in the original COS remain the same.

A roll call vote was taken:

MOTION PREVAILED

Theresa Ann Kordish, DO

Yeas: Danek, Rimes, Ikram, Neal
Nays:  None

MOTION  by  Ikram,  seconded  by  Rimes,  to  accept  the  Consent  Order  and
Stipulation.

A roll call vote was taken:

MOTION PREVAILED

Joseph T. Naughton, DO

Yeas: Danek, Rimes, Ikram, Neal
Nays:  None

MOTION  by  Danek,  seconded  by  Ikram,  to  accept  the  Consent  Order  and
Stipulation.

A roll call vote was taken:

Yeas: Danek, Rimes, Ikram, Neal
Nays:  None

MOTION PREVAILED

Order of Dismissal

Ian Samuel Batson, DO

MOTION by Ikram, seconded by Rimes, to accept the Order of Dismissal.

A roll call vote was taken:

Yeas: Danek, Rimes, Ikram, Neal
Nays:  None

MOTION PREVAILED

PUBLIC COMMENT

A member of the public attempted to speak about a regulatory matter.

Wagner-Gutkowski  reminded  the  member,  that  regulatory  matters  cannot  be
discussed.

ANNOUNCEMENTS

The next regularly scheduled meeting is on February 5, 2026, immediately following the
regularly  scheduled  Michigan  Board  of  Osteopathic  Medicine  and  Surgery  meeting

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
December 5, 2025
Page 4 of 4

scheduled  to  begin  at  9:00  a.m.  at  611  West  Ottawa  Street,  Upper-Level  Conference
Center Room 4, Lansing, Michigan 48933.

ADJOURNMENT

MOTION by Rimes, seconded by Ikram, to adjourn the meeting at 10:14 a.m.

A voice vote was held.

MOTION PREVAILED

Minutes approved by the Board on February 5, 2026.

Prepared by:
Kimmy Darnell, Board Support Technician
Bureau of Professional Licensing

December 9, 2025

---

**[AGENDA] 2025-12-04_12-4-2025-Osteo-DSC--Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND SURGERY
DISCIPLINARY SUBCOMMITTEE

DECEMBER 4, 2025

9:00 a.m.
Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

Agenda

1.

2.

3.

4.

5.

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from Meeting of October 2, 2025

Regulatory Considerations

A.  Proposal for Decision

  Reginald D. Sharpe, D.O.

B.  Consent Orders and Stipulation

1.  Jon Michael Banas, D.O. (Conferee Rollinger)
2.  Theresa Ann Kordish, D.O. (Conferee Bell)
3.  Joseph T. Naughton, D.O. (Conferee Bishop)

C.  Order of Dismissal



Ian Samuel Batson, D.O. (Conferee Bishop)

6.

7.

Public Comment

Announcements

The next regularly scheduled meeting will be held February 5, 2026, immediately
following  the  full  board  meeting  scheduled  to  begin  at  9:00  a.m.  at  611  West
Ottawa Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic
Medicine & Surgery
Disciplinary Subcommittee Agenda
December 4, 2025
Page 2 of 2

8.

Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/85684125059?pwd=FxGN8Y10wT2GLKlI0ZkluL5SqNxMil.1

Phone Number: (1) 408-961-3928

Meeting ID: 856 8412 5059

Passcode: 742258

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In the event of a disconnection caused by the meeting host, the Board will be in recess.
Every effort will be made to reestablish a publicly accessible connection. If the host is
unable to do so within a period of 30 minutes from the time of the disconnection, the
Board  will  adjourn  and  not  address  any  new  business  until  its  next  meeting.  Any
decisions made prior to the disconnection will be binding. The board will not recess or
adjourn  due  to  technical  or  other  issues  experienced  by  individual  members  of  the
public that render them unable to attend or participate in the meeting.

the  public  who  require  accommodation

Members  of
to
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/mpsc/0,9535,7-395-93308_93325_93425_94040_94041--
-,00.html.

for  equal  access

Please  contact  the  department  at  BPL-BoardSupport@Michigan.gov
other accommodations or have questions.

if  you  need

---

**[MINUTES] 2025-12-04_12-4-2025-Osteo-Full-Board-approved-minutes.pdf**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

STATE OF MICHIGAN
GRETCHEN WHITMER  DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS  MARLON I. BROWN, DPA
| GOVERNOR  |     |     | LANSING  | DIRECTOR  |
| --------- | --- | --- | -------- | --------- |

MICHIGAN BOARD OF OSTEOPATHIC
MEDICINE & SURGERY

DECEMBER 4, 2025, MEETING

APPROVED MINUTES

In accordance with the Open Meetings Act, 1976 PA 267, as amended, the Michigan
Board of Osteopathic Medicine and Surgery met on December 4, 2025, at 611 West
Ottawa Street, Upper-Level Conference Room 4, Lansing, Michigan 48933.

CALL TO ORDER

Stephen Bell, D.O., Chairperson, called the meeting to order at 9:09 a.m.

| Members Present:  | Stephen Bell, D.O., Chairperson              |     |     |     |
| ----------------- | -------------------------------------------- | --- | --- | --- |
|                   | Craig Glines, D.O., MSBA, Vice-Chairperson   |     |     |     |
|                   | Ronald Bishop, D.O.                          |     |     |     |
|                   | Samantha Danek, PA-C                         |     |     |     |
|                   | Khawaja Ikram, D.O.                          |     |     |     |
|                   | Delores Mitchell, Public Member              |     |     |     |
|                   | Ayanna Neal, J.D., Public Member             |     |     |     |
                                 Ben Rimes, Public Member
                                 Kathleen Rollinger, D.O. (Arrived at 9:12 a.m.)
|                                 |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- |
Members Absent:    John Everett, D.O.
Jeffrey Rosenbaum, D.O.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Staff Present:  Marshall Hooks, Senior Analyst, Compliance Section
|     | Robert Payne, Senior Analyst, Compliance Section          |                                |     |     |
| --- | --------------------------------------------------------- | ------------------------------ | --- | --- |
|     | Weston MacIntosh, JD, Departmental Specialist,            |                                |     |     |
|     |                                                           | Boards and Committees Section  |     |     |
|     | Michele Wagner-Gutkowski, JD, Assistant Attorney General  |                                |     |     |
 Kimmy Darnell, Board Support Technician,
|     |     | Boards and Committees Section  |     |     |
| --- | --- | ------------------------------ | --- | --- |

APPROVAL OF AGENDA

MOTION by Bishop, seconded by Ikram, to approve the agenda as presented.

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199

LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
December 4, 2025
Page 2 of 4
A voice vote was held.
MOTION PREVAILED
APPROVAL OF MINUTES
MOTION by Glines, seconded by Bishop, to approve the August 7, 2025, meeting
minutes as written.
A voice vote was held.
MOTION PREVAILED
REGULATORY CONSIDERATIONS
Petition for Reinstatement
Bradley Wayne Bakotic, DO
MOTION by Glines, seconded by Bishop, to discuss.
A voice vote was held.
MOTION PREVAILED
Discussion was held.
MOTION by Ikram, seconded by Glines, to grant reinstatement of the license.
Respondent is placed on probation for 1 year with no violation of the Michigan Public
Health Code.
A roll call vote was taken: Yeas: Bishop, Danek, Ikram, Mitchell, Neal, Rimes, Rollinger,
Glines, Bell
Nays: None
MOTION PREVAILED
Proposal for Decision – Reinstatement
Joseph N. Hagen, DO
Neal recused herself from the matter.
MOTION by Mitchell, seconded by Ikram, to discuss.
A voice vote was held.

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
December 4, 2025
Page 3 of 4
MOTION PREVAILED
Discussion was held.
MOTION by Ikram, seconded by Mitchell, to grant reinstatement with a five (5) year
limitation prohibiting the Petitioner from engaging in billable telehealth visits and
automatic reclassification after five (5) years. The Petitioner is placed on probation for five
(5) years, to run concurrently with the limitation period. The terms of probation include
quarterly reviewer reports by a board approved reviewer, with a review of 10 charts to the
extent Petitioner engages in durable medical equipment referrals/prescriptions, and no
violation of the Michigan Public Health Code.
A roll call vote was taken: Yeas: Bishop, Danek, Ikram, Mitchell, Rimes, Rollinger,
Glines, Bell
Nays: None
Recuse: Neal
MOTION PREVAILED
OLD BUSINESS
None
NEW BUSINESS
HPRC Candidate Request
MacIntosh explained that under MCL 333.16165 of the Michigan Public Health Code,
each board created under Article 15 of the Code may appoint a member to the Health
Professional Recovery Committee (HPRC) to represent the profession. The HPRC
manages oversight of the Health Professional Recovery Program (HPRP).
MacIntosh stated that the representative slot for the Board of Osteopathic Medicine and
Surgery on the HPRC is currently vacant. MacIntosh asked for the board’s help in finding
a qualified candidate to serve as the board’s representative on the HPRC.
Chair Report
None
Department Update
MacIntosh reminded the board to check their state e-mail at least once a week.
Darnell reminded the Board to sign their vouchers.

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
December 4, 2025
Page 4 of 4
PUBLIC COMMENT
None
ANNOUNCEMENTS
The next regularly scheduled meeting is February 5, 2026, at 9:00 a.m. at 611 West
Ottawa Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.
ADJOURNMENT
MOTION by Glines, seconded by Bishop, to adjourn the meeting at 9:45 a.m.
A voice vote was held.
MOTION PREVAILED
Minutes approved by the Board on February 5, 2026.
Prepared by:
Kimmy Darnell, Board Support Technician December 9, 2025
Bureau of Professional Licensing

---

**[AGENDA] 2025-12-04_12-4-2025-Osteopathic-Medicine-and-Surgery--Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND
SURGERY

DECEMBER 4, 2025
9:00 a.m.

Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

1.

2.

3.

4.

5.

Agenda

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from meeting August 7, 2025

Regulatory Considerations

A. Petition for Reinstatement

  Bradley Wayne Bakotic, D.O.

B. Proposal for Decision – Reinstatement

  Joseph N. Hagen, D.O.

6.

Old Business

None

7.

New Business

A.  HPRC Candidate Request
B.  Chair Report
C.  Department Update

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine
Agenda
December 4, 2025
Page 2 of 2

8.

9.

Public Comment

Announcements

The next regularly scheduled meeting will be held February 5, 2026, at 9:00 a.m.
at  611  W.  Ottawa Street,  Upper-  Level  Conference  Center  Room 4,  Lansing,
Michigan 48933.

10.

Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/85684125059?pwd=FxGN8Y10wT2GLKlI0ZkluL5SqNxMil.1

Phone Number: (1) 408-961-3928

Meeting ID: 856 8412 5059

Passcode: 742258

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In the event of a disconnection caused by the meeting host, the Board will be in recess.
Every effort will be made to reestablish a publicly accessible connection. If the host is
unable to do so within a period of 30 minutes from the time of the disconnection, the
Board  will  adjourn  and  not  address  any  new  business  until  its  next  meeting.  Any
decisions made prior to the disconnection will be binding. The board will not recess or
adjourn  due  to  technical  or  other  issues  experienced  by  individual  members  of  the
public that render them unable to attend or participate in the meeting.

the  public  who  require  accommodation

Members  of
to
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/mpsc/0,9535,7-395-93308_93325_93425_94040_94041--
-,00.html.

for  equal  access

Please  contact  the  department  at  BPL-BoardSupport@Michigan.gov
other accommodations or have questions.

if  you  need

---

### 2025-10-02 — Michigan Board of Osteopathic Medicine and Surgery — October 02, 2025

**[MINUTES] 2025-10-02_10-2-2025-Osteo-DSC-Approved-Minutes.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
 DIRECTOR

BOARD OF OSTEOPATHIC MEDICINE & SURGERY
DISCIPLINARY SUBCOMMITTEE

OCTOBER 2, 2025, MEETING

APPROVED MINUTES

In  accordance  with  the  Open  Meetings  Act,  1976  PA  267,  as  amended,  the  Michigan
Board of Osteopathic Medicine & Surgery Disciplinary Subcommittee met on October 2,
2025, at 611 West Ottawa Street, Upper-Level Conference Room 4, Lansing, Michigan
48933.

CALL TO ORDER

Ayanna Neal, Public Member, Chairperson, called the meeting to order at 9:00 a.m.

Members Present:  Ayanna Neal, J.D., Public Member, Chairperson
Craig Glines, D.O., MSBA
Khawaja Ikram, D.O. (Alternate)
Ben Rimes, Public Member

Members Absent:  Samantha Danek, PA-C
Jeffrey Rosenbaum, D.O.

Staff Present:

Marshall Hooks, Senior Analyst, Compliance Section
Rob Payne, Analyst, Compliance Section
Kimmy Darnell, Board Support Technician,
Boards and Committees Section

Jason Werkema, JD, Assistant Attorney General

APPROVAL OF AGENDA

MOTION by Glines, seconded by Ikram, to approve the agenda as presented.

A voice vote was held.

MOTION PREVAILED

APPROVAL OF MINUTES

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
October 2, 2025
Page 2 of 3

MOTION  by  Ikram,  seconded  by  Glines,  to  approve  the  August  7,  2025,  meeting
minutes as presented.

A voice vote was held.

MOTION PREVAILED

REGULATORY CONSIDERATIONS

Administrative Complaint

Ronald David Dean, DO

MOTION by Ikram, seconded by Glines, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION  by  Ikram,  seconded  by  Rimes,  to  Dissolve  the  Order  of  Summary
Suspension  and  fine  the  Respondent  $1,500.00  due  prior  to  petitioning  for
reinstatement. The Respondent is reprimanded, and the license is revoked.

A roll call vote was taken:

MOTION PREVAILED

Yeas: Glines, Rimes, Ikram, Neal
Nays:  None

Consent Orders and Stipulations

John O. Wycoff, DO

MOTION by Glines, seconded by Ikram, to untable the matter.

A voice vote followed.

MOTION PREVAILED

MOTION by Glines, seconded by Ikram, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
October 2, 2025
Page 3 of 3

MOTION  by  Glines,  seconded  by  Rimes,  to  accept  the  Consent  Order  and
Stipulation.

A roll call vote was taken:

Yeas: Glines, Rimes, Ikram, Neal
Nays:  None

MOTION PREVAILED

Order of Dismissal

Mary Chao, DO

MOTION by Rimes, seconded by Ikram, to accept the Order of Dismissal.

A roll call vote was taken:

MOTION PREVAILED

Yeas: Glines, Rimes, Ikram, Neal
Nays:  None

PUBLIC COMMENT

None

ANNOUNCEMENTS

The next regularly scheduled meeting is on December 4, 2025, immediately following the
regularly  scheduled  Michigan  Board  of  Osteopathic  Medicine  and  Surgery  meeting
scheduled  to  begin  at  9:00  a.m.  at  611  West  Ottawa  Street,  Upper-Level  Conference
Center Room 4, Lansing, Michigan 48933.

ADJOURNMENT

MOTION by Rimes, seconded by Ikram, to adjourn the meeting at 9:18 a.m.

A voice vote was held.

MOTION PREVAILED

Minutes approved by the Board on December 4, 2025.

Prepared by:
Kimmy Darnell, Board Support Technician
Bureau of Professional Licensing

October 2, 2025

---

**[AGENDA] 2025-10-02_10-2-2025-Osteo-DSC--Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND SURGERY
DISCIPLINARY SUBCOMMITTEE

OCTOBER 2, 2025

9:00 a.m.
Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

Agenda

1.

2.

3.

4.

5.

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from Meeting of August 7, 2025

Regulatory Considerations

A.  Administrative Complaint

  Ronald David Dean, DO

B.  Consent Orders and Stipulation

  John O Wycoff, DO (Conferee Everett) (Tabled at 8-7-2025 meeting)

C.  Order of Dismissal
  Mary Chao, DO

6.

7.

Public Comment

Announcements

The next regularly scheduled meeting will be held December 4, 2025, immediately
following  the  full  board  meeting  scheduled  to  begin  at  9:00  a.m.  at  611  West
Ottawa Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.

8.

Adjournment

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic
Medicine & Surgery
Disciplinary Subcommittee Agenda
October 2, 2025
Page 2 of 2

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/82082788845?pwd=UlpodURrQkR0QURxYUp0bmxjL011Zz09

Password: 160447

Phone Number:
Dial: 888-684-8852
Conference code: 335451

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In the event of a disconnection caused by the meeting host, the Board will be in recess.
Every effort will be made to reestablish a publicly accessible connection. If the host is
unable to do so within a period of 30 minutes from the time of the disconnection, the
Board  will  adjourn  and  not  address  any  new  business  until  its  next  meeting.  Any
decisions made prior to the disconnection will be binding. The board will not recess or
adjourn  due  to  technical  or  other  issues  experienced  by  individual  members  of  the
public that render them unable to attend or participate in the meeting.

the  public  who  require  accommodation

Members  of
to
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/mpsc/0,9535,7-395-93308_93325_93425_94040_94041--
-,00.html.

for  equal  access

Please  contact  the  department  at  BPL-BoardSupport@Michigan.gov    if  you  need
other accommodations or have questions.

---

**[MINUTES] 2025-10-02_10-2-2025-Osteopathic-Full-Board-Cancellation.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

PUBLIC NOTICE

MICHIGAN BOARD OF OSTEOPATHIC
MEDICINE AND SURGERY

ANNOUNCES A

CANCELLATION

OF THE
FULL BOARD MEETING
ON
OCTOBER 2, 2025

The next regularly scheduled meetings will be held December 4, 2025, at 9:00 a.m. at
611 W. Ottawa Street, Upper-Level Conference Room 4, Lansing, Michigan.

All meetings are conducted in accordance with Public Act 267 of 1976, as amended, and
are open to the public.  Further information concerning a specific meeting can be obtained
from the Board office at 517-241-7500.

Dated: September 18, 2025

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

---

### 2025-08-07 — Michigan Board of Osteopathic Medicine and Surgery — August 07, 2025

**[MINUTES] 2025-08-07_8-7-2025-Osteo-DSC-Approved-Minutes.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
 DIRECTOR

BOARD OF OSTEOPATHIC MEDICINE & SURGERY
DISCIPLINARY SUBCOMMITTEE

AUGUST 7, 2025, MEETING

APPROVED MINUTES

In  accordance  with  the  Open  Meetings  Act,  1976  PA  267,  as  amended,  the  Michigan
Board of Osteopathic Medicine & Surgery Disciplinary Subcommittee met on August 7,
2025, at 611 West Ottawa Street, Upper-Level Conference Room 4, Lansing, Michigan
48933.

CALL TO ORDER

Ayanna Neal, Public Member, Chairperson, called the meeting to order at 9:32 a.m.

Members Present:  Ayanna Neal, J.D., Public Member, Chairperson

Samantha Danek, PA-C (left at 9:34 a.m.)
Craig Glines, D.O., MSBA
Jeffrey Rosenbaum, D.O.
Khawaja Ikram, D.O. (Alternate)

Members Absent:  Ben Rimes, Public Member

Staff Present:

Marshall Hooks, Senior Analyst, Compliance Section
Kim Smith, Board Support Technician,
Boards and Committees Section

Michele Wagner-Gutkowski, JD, Assistant Attorney General
Jason Werkema, JD, Assistant Attorney General

APPROVAL OF AGENDA

MOTION by Ikram, seconded by Rosenbaum, to approve the agenda as presented.

A voice vote was held.

MOTION PREVAILED

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
August 7, 2025
Page 2 of 4

APPROVAL OF MINUTES

MOTION by Glines, seconded by Ikram, to approve the June 5, 2025, meeting minutes
as presented.

A voice vote was held.

MOTION PREVAILED

REGULATORY CONSIDERATIONS

Administrative Complaint

George Edward Bonefeld, DO

MOTION by Glines, seconded by Ikram, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION by Glines, seconded by Rosenbaum, to suspend Respondent’s license
for 1  year.  The  Respondent  is fined  $5,000.00  to  be  paid  prior to  petitioning  for
reinstatement and Respondent must comply with all other terms of the prior order.

A roll call vote was taken:

MOTION PREVAILED

Yeas: Glines, Ikram, Rosenbaum, Neal
Nays:  None

Consent Orders and Stipulations

Michael A. Kia, DO

MOTION by Ikram, seconded by Rosenbaum, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION  by  Ikram,  seconded by  Rosenbaum, to accept  the  Consent Order and
Stipulation.

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
August 7, 2025
Page 3 of 4

A roll call vote was taken:

MOTION PREVAILED

Bruce D. Lawrence, DO

Yeas: Glines, Ikram, Rosenbaum, Neal
Nays:  None

MOTION  by  Glines,  seconded  by  Ikram,  to  accept  the  Consent  Order  and
Stipulation.

A roll call vote was taken:

MOTION PREVAILED

Billy Ralph Nordyke, DO

Yeas: Glines, Ikram, Rosenbaum, Neal
Nays:  None

MOTION by Rosenbaum, seconded by Ikram, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION by Ikram, seconded by Rosenbaum, to reject with a counteroffer. Terms
of  the  counteroffer  are:  suspension  for  a  minimum  of  1  day  until  Respondent
completes  the  PBI  continuing  education  and  pays  the  fine.   If  Respondent
completes the terms within 6 months and the license is automatically reinstated,
the remaining terms of probation apply.

A roll call vote was taken:

Yeas: Glines, Ikram, Rosenbaum, Neal
Nays:  None

MOTION PREVAILED

John O. Wycoff, DO

MOTION by Ikram, seconded by Glines, to discuss the matter.

A voice vote followed.

MOTION PREVAILED

Discussion held.

MOTION  by  Rosenbaum,  seconded  by  Ikram,  to  table  the  matter  and  discuss  with
Conferee Everett at the next meeting.

Michigan Board of Osteopathic Medicine & Surgery
Disciplinary Subcommittee Meeting Minutes
August 7, 2025
Page 4 of 4

PUBLIC COMMENT

None

ANNOUNCEMENTS

The next regularly scheduled meeting is on October 2, 2025, immediately following the
regularly  scheduled  Michigan  Board  of  Osteopathic  Medicine  and  Surgery  meeting
scheduled  to  begin  at  9:00  a.m.  at  611  West  Ottawa  Street,  Upper-Level  Conference
Center Room 4, Lansing, Michigan 48933.

ADJOURNMENT

MOTION by Glines, seconded by Rosenbaum, to adjourn the meeting at 10:11 a.m.

A voice vote was held.

MOTION PREVAILED

Minutes approved by the Board on October 2, 2025.

Prepared by:
Kim Smith, Board Support Technician
Bureau of Professional Licensing

August 11, 2025

---

**[AGENDA] 2025-08-07_8-7-2025-Osteo-DSC--Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND SURGERY
DISCIPLINARY SUBCOMMITTEE

AUGUST 7, 2025

(Immediately following the Full Board meeting which begins at 9:00 a.m.)

Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

Agenda

1.

2.

3.

4.

5.

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from Meeting of June 5, 2025

Regulatory Considerations

A.  Administrative Complaint

  George Edward Bonefeld, DO

B.  Consent Orders and Stipulation

1. Michael A Kia, DO (Conferee Rollinger)
2. Bruce D Lawrence, DO
3. Billy Ralph Nordyke, DO (Conferee Rollinger)
4. John O Wycoff, DO (Conferee Everett)

6.

7.

Public Comment

Announcements

The next regularly scheduled meeting will be held October 2, 2025, immediately
following  the  full  board  meeting  scheduled  to  begin  at  9:00  a.m.  at  611  West
Ottawa Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic
Medicine & Surgery
Disciplinary Subcommittee Agenda
August 7, 2025
Page 2 of 2

8.

Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/82082788845?pwd=UlpodURrQkR0QURxYUp0bmxjL011Zz09

Password: 160447

Phone Number:
Dial: 888-684-8852
Conference code: 335451

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In  the  event  of  a  disconnection  caused  by  the  meeting  host,  the  Board  will  be
considered  to  be  in  recess.  Every  effort  will  be  made  to  reestablish  a  publicly
accessible connection. If the host is unable to do so within a period of 30 minutes from
the  time  of  the  disconnection,  the  Board  will  adjourn  and  not  address  any  new
business until its next meeting. Any decisions made prior to the disconnection will be
binding.  The  board  will  not  recess  or  adjourn  due  to  technical  or  other  issues
experienced by individual members of the public that render them unable to attend or
participate in the meeting.

the  public  who  require  accommodations

Members  of
to
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/mpsc/0,9535,7-395-93308_93325_93425_94040_94041--
-,00.html.

for  equal  access

Please  contact  the  department  at  BPL-BoardSupport@Michigan.gov    if  you  need
other accommodations or have questions.

---

**[MINUTES] 2025-08-07_8-7-2025-Osteo-Full-Board-Approved-minutes.pdf**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |

STATE OF MICHIGAN
GRETCHEN WHITMER  DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS  MARLON I. BROWN, DPA
| GOVERNOR  |     |     | LANSING  | DIRECTOR  |
| --------- | --- | --- | -------- | --------- |

MICHIGAN BOARD OF OSTEOPATHIC
MEDICINE & SURGERY

AUGUST 7, 2025, MEETING

APPROVED MINUTES

In accordance with the Open Meetings Act, 1976 PA 267, as amended, the Michigan
Board of Osteopathic Medicine and Surgery met on August 7, 2025, at 611 West Ottawa
Street, Upper-Level Conference Room 4, Lansing, Michigan 48933.

CALL TO ORDER

Stephen Bell, D.O., Chairperson, called the meeting to order at 9:06 a.m.

| Members Present:  | Stephen Bell, D.O., Chairperson              |     |     |     |
| ----------------- | -------------------------------------------- | --- | --- | --- |
|                   | Craig Glines, D.O., MSBA, Vice-Chairperson   |     |     |     |
|                   | Samantha Danek, PA-C                         |     |     |     |
|                   | Khawaja Ikram, D.O.                          |     |     |     |
|                   | Delores Mitchell, Public Member              |     |     |     |
|                   | Ayanna Neal, J.D., Public Member             |     |     |     |
|                   | Jeffrey Rosenbaum, D.O.                      |     |     |     |
|                   |                                              |     |     |     |
Members Absent:     Ronald Bishop, D.O.
                                 John Everett, D.O.
                                 Ben Rimes, Public Member
                                 Kathleen Rollinger, D.O.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Staff Present:  Marshall Hooks, Senior Analyst, Compliance Section
|     | Weston MacIntosh, JD, Departmental Specialist,            |                                |     |     |
| --- | --------------------------------------------------------- | ------------------------------ | --- | --- |
|     |                                                           | Boards and Committees Section  |     |     |
|     | Michele Wagner-Gutkowski, JD, Assistant Attorney General  |                                |     |     |
 Kim Smith, Board Support Technician,
|     |                                                | Boards and Committees Section  |     |     |
| --- | ---------------------------------------------- | ------------------------------ | --- | --- |
|     | Jason Werkema, JD, Assistant Attorney General  |                                |     |     |

APPROVAL OF AGENDA

MOTION by Glines, seconded by Ikram, to approve the agenda as presented.

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA • P.O. BOX 30670 • LANSING, MICHIGAN 48909
www.michigan.gov/bpl • 517-241-0199

LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
August 7, 2025
Page 2 of 4
A voice vote was held.
MOTION PREVAILED
APPROVAL OF MINUTES
MOTION by Rosenbaum, seconded by Ikram, to approve the April 3, 2025, meeting
minutes as written.
A voice vote was held.
MOTION PREVAILED
REGULATORY CONSIDERATIONS
Proposal for Decision – Reinstatement
Kameron Ravindra Budhram, DO
MOTION by Glines, seconded by Ikram, to discuss.
A voice vote was held.
MOTION PREVAILED
Discussion was held.
MOTION by Mitchell, seconded by Rosenbaum, to accept the Proposal for Decision and
deny reinstatement of the license.
A roll call vote was taken: Yeas: Danek, Ikram, Mitchell, Neal, Rosenbaum, Glines, Bell
Nays: None
MOTION PREVAILED
Petition for Reinstatement
Martin Facundo Quiroga, DO
MOTION by Glines, seconded by Rosenbaum, to accept the Proposal for Decision and
grant reinstatement of the license. Respondent is placed on probation for 1 year with no
violation of the Michigan Public Health Code.
A roll call vote was taken: Yeas: Danek, Ikram, Mitchell, Neal, Rosenbaum, Glines, Bell
Nays: None
MOTION PREVAILED

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
August 7, 2025
Page 3 of 4
OLD BUSINESS
None
NEW BUSINESS
HPRC Candidate Request
MacIntosh informed the board that Dr. Moss would like to be appointed as their HPRC
Representative.
MOTION by Danek, seconded by Rosenbaum to appoint Dr. Moss to the HPRC
Committee.
A roll call vote was taken: Yeas: Danek, Ikram, Mitchell, Neal, Rosenbaum, Glines, Bell
Nays: None
MOTION PREVAILED
2026 Public Notice
MacIntosh asked the board to note the 2026 meeting dates and to please let staff
know as soon as possible if there are dates they are unable to attend.
MacIntosh also asked the board to look at agendas when they come out to check for
any cases they may need to recuse and to please let staff know as soon as they can
to avoid loss of quorum.
Chair Report
Bell and the entire board congratulated Kimberly Catlin on her upcoming wedding.
Department Update
MacIntosh reminded the board to check their state e-mail at least once a week.
Wagner-Gutkowski introduced Jason Werkema to the board.
PUBLIC COMMENT
None
ANNOUNCEMENTS
The next regularly scheduled meeting is October 2, 2025, at 9:00 a.m. at 611 West Ottawa
Street, Upper-Level Conference Center Room 4, Lansing, Michigan 48933.

Michigan Board of Osteopathic Medicine & Surgery
Meeting Minutes
August 7, 2025
Page 4 of 4
ADJOURNMENT
MOTION by Ikram, seconded by Glines, to adjourn the meeting at 9:27 a.m.
A voice vote was held.
MOTION PREVAILED
Minutes approved by the Board on December 4, 2025.
Prepared by:
Kimberly Smith, Board Support Technician August 11, 2025
Bureau of Professional Licensing

---

**[AGENDA] 2025-08-07_8-7-2025-Osteopathic-Medicine-and-Surgery--Agenda.pdf**

GRETCHEN WHITMER
GOVERNOR

STATE OF MICHIGAN
DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS
LANSING

MARLON I. BROWN, DPA
DIRECTOR

MICHIGAN BOARD OF OSTEOPATHIC MEDICINE AND
SURGERY

AUGUST 7, 2025
9:00 a.m.

Ottawa Building, Conference Room 4
611 West Ottawa Street
Lansing, Michigan 48933

1.

2.

3.

4.

5.

Agenda

Welcome and Call to Order

Roll Call/Public Comment Reminder

Approval of Agenda

Approval of Minutes from meeting of April 3, 2025

Regulatory Considerations

A. Proposal for Decision – Reinstatement
  Kameron Ravindra Budhram, DO

B. Petition for Reinstatement

  Martin Facundo Quiroga, DO

6.

Old Business

None

7.

New Business

A.  HPRC Candidate Request
B.  2026 Public Notice
C.  Chair Report
D.  Department Update

BUREAU OF PROFESSIONAL LICENSING
611 W. OTTAWA  P.O. BOX 30670  LANSING, MICHIGAN 48909
www.michigan.gov/bpl  517-241-0199
LARA is an equal opportunity employer/program

Michigan Board of Osteopathic Medicine
Agenda
August 7, 2025
Page 2 of 2

8.

9.

Public Comment

Announcements

The next regularly scheduled meeting will be held October 2, 2025, at 9:00 a.m.
at  611  W.  Ottawa Street,  Upper-  Level  Conference  Center  Room 4,  Lansing,
Michigan 48933.

10.

 Adjournment

NOTE:

Members of the public are welcome to attend this meeting virtually using Zoom. The
information to log on to the meeting is listed below.

Web Link:
https://us06web.zoom.us/j/82082788845?pwd=UlpodURrQkR0QURxYUp0bmxjL011Zz09

Password: 160447

Phone Number:
Dial: 888-684-8852
Conference code: 335451

To minimize disruptions, until the time designated by the board for public comment,
members of the public will be muted.  During the public comment period, members of
the public will be unmuted to provide their comments as called on by the board chair.
All rules regarding public comment (including those designed to minimize disruptions
and allow for full public participation) apply.

In  the  event  of  a  disconnection  caused  by  the  meeting  host,  the  Board  will  be
considered  to  be  in  recess.  Every  effort  will  be  made  to  reestablish  a  publicly
accessible connection. If the host is unable to do so within a period of 30 minutes from
the  time  of  the  disconnection,  the  Board  will  adjourn  and  not  address  any  new
business until its next meeting. Any decisions made prior to the disconnection will be
binding.  The  board  will  not  recess  or  adjourn  due  to  technical  or  other  issues
experienced by individual members of the public that render them unable to attend or
participate in the meeting.

the  public  who  require  accommodations

Members  of
to
communication may attend and participate in this meeting by dialing 7-1-1 and using
the  Michigan  Relay  service.  More  information  about  this  service  may  be  found  at
https://www.michigan.gov/mpsc/0,9535,7-395-93308_93325_93425_94040_94041--
-,00.html.

for  equal  access

Please  contact  the  department  at  BPL-BoardSupport@Michigan.gov    if  you  need
other accommodations or have questions.
