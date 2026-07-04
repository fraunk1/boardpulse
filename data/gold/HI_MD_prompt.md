You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Hawaii Medical Board** (HI) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/HI/HI_MD#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-03-12]` — Hawaii Medical Board — March 12, 2026
- `[2026-02-12]` — Hawaii Medical Board — February 12, 2026
- `[2026-01-15]` — Hawaii Medical Board — January 15, 2026
- `[2025-12-11]` — Hawaii Medical Board — December 11, 2025
- `[2025-11-13]` — Hawaii Medical Board — November 13, 2025
- `[2025-08-01]` — Hawaii Medical Board — August 01, 2025

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: HI_MD
state: HI
---

# Hawaii Medical Board — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Hawaii Medical Board | [Minutes page](HI_MD_MINUTES_URL) |

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

Sources-table URL: https://cca.hawaii.gov/pvl/boards/medical/board-meeting-minutes/

## Meeting Minutes Data

Board: Hawaii Medical Board
State: HI
Code: HI_MD

### 2026-03-12 — Hawaii Medical Board — March 12, 2026

*(No extracted text available)*

---

### 2026-02-12 — Hawaii Medical Board — February 12, 2026

**[MINUTES] 2026-02-12_PVL_Minutes_Medical_2026-02-12.pdf**

Hawaii Medical Board
Minutes of the Meeting of February 12, 2026

HAWAII MEDICAL BOARD
Professional and Vocational Licensing Division
Department of Commerce and Consumer Affairs
State of Hawaii

MINUTES OF MEETING

February 12, 2026

1:00 p.m.

PVL Exam Room 330
HRH King Kalakaua Building
335 Merchant Street, Third Floor
Honolulu, Hawaii 96813

Virtual Videoconference Meeting – Zoom Meeting
https://dcca-hawaii-
gov.zoom.us/j/86346269431?pwd=ZbV2W8ekQWHknbiYspPGrvt
GbpIMvc.1

Date:

Time:

In-Person
Meeting
Location:

Virtual
Participation:

Recording Link:

https://www.youtube.com/watch?v=_fZyqK5IvS0

Present:

Danny Takanishi Jr., M.D., Chairperson, Honolulu Member
Gary Belcher, Vice Chairperson, Public Member
Andrew “Rick” Fong, M.D., Hawaii Member
Angela Pratt, M.D., Honolulu Member
Elizabeth “Lisa Ann” Ignacio, M.D, Maui Member
Michael Jaffe, D.O., Osteopathic/Honolulu Member
Rebecca Sawai, M.D., Honolulu Member
Robert “Bob” Wotring, M.D. Kauai County Member
Wesley Mun, Public Member
Shari J. Wong, Deputy Attorney General (“DAG”)
Elizabeth Kor, Executive Officer (“EO”)
Young-Im Wilson, Supervisory Executive Officer
Breyanah Panzardi, Technical Support
Cortnie Tanaka, Administrative Assistant

Excused:

None

Zoom Guest(s):

Jaclyn Tolentino, D.O.
Nessa Seangmany, D.O.
Jim Seraj, M.D.
Timothy R. Taylor, M.D.
Wayne Tran, M.D.

Agenda:

The agenda for this meeting was posted to the State electronic
calendar as required by Hawaii Revised Statues (“HRS”) section
92-7(b).

Page 1 of 5

Hawaii Medical Board
Minutes of the Meeting of February 12, 2026

Call to Order:

The meeting was called to order at 1:09 p.m., at which time
quorum was established.

Chair’s
Announcements

Approval of
Minutes:

Applications for
Licensure/
Certification:

Chair Takanishi welcomed everyone to the meeting and
proceeded with a roll call of the Board members. All Board
members present confirmed that they were present and alone.

A.  Welcome new board member, Dr. Robert Wotring, M.D.

Chair Takanishi introduced and welcomed Dr. Robert Wotring to
the Board.

It was moved by Dr. Ignacio, seconded by Dr. Sawai, and
unanimously carried to approve the January 15, 2026, open
session and executive session meeting minutes. Due to technical
difficulties, Mr. Mun was not present.

A.

Applications

It was moved by Dr. Jaffe, seconded by Dr. Pratt, and
unanimously carried to enter into executive session at 1:11 p.m.,
pursuant to HRS §92-5(a)(1), to consider and evaluate personal
information relating to individuals applying for professional
licenses cited in HRS §26-9 and, pursuant to HRS §92-5 (a)(4), to
consult with the Board’s attorney on questions and issues
pertaining to the Board’s powers, duties, privileges, immunities
and liabilities. (Note: Board members and staff entered the Zoom
Breakout Room).

It was moved by Dr. Jaffe, seconded by Mr. Mun, and
unanimously carried to return to the open session meeting at 3:12
p.m. Board members and staff returned to the main Zoom
meeting room. Due to technical difficulties, Mr. Mun was not
present. All Board members present confirmed that they were
present and alone.

(i)  Osteopathic Physician & Surgeon (Permanent/Endorsement)

a.  Jaclyn Tolentino, D.O.

After due consideration of the information received, it was moved
by Chair Takanishi, seconded by Dr. Jaffe, and unanimously
carried to approve Dr. Tolentino’s application. Due to technical
difficulties, Mr. Mun was not present.

(ii)  Physician (Permanent/Non-Endorsement)

a.  Nessa Seangmany, D.O.

After due consideration of the information received, it was moved
by Dr. Jaffe, seconded by Dr. Ignacio, and unanimously carried to

Page 2 of 5

Hawaii Medical Board
Minutes of the Meeting of February 12, 2026

defer Dr. Seangmany’s application pending further information
providing an official honorable discharge from the military and a
copy of her military substance use disorder evaluation.

(iii) Physician (Permanent/Endorsement)

a.  Jim Seraj, M.D.

After due consideration of the information received, it was moved
by Chair Takanishi, seconded by Dr. Pratt, and unanimously
carried to approve Dr. Seraj’s application.

b.  Timothy R. Taylor, M.D.

After due consideration of the information received, it was moved
by Dr. Pratt, seconded by Dr. Ignacio, and unanimously carried to
approve Dr Taylor’s application.

(iv) Physician (Permanent/Non-Endorsement)

a.  Wayne Tran, M.D.

After due consideration of the information received, it was moved
by Vice Chair Belcher, seconded by Dr. Jaffe, and unanimously
carried to approve Dr. Tran’s application with the following
conditions;

1)  The Board must receive quarterly reports from the
California Medical Board Probationary Unit; and

2)  Should Dr. Tran relocate to Hawaii for in-person practice,
formal arrangements with the Hawaii Physicians Health
Program must be executed.

Mr. Mun was able to successfully re-enter the main Zoom room.

b.  Robert Matthew Bernstein, M.D

After due consideration of the information received, it was moved
by Dr. Fong, seconded by Dr. Pratt, and unanimously carried to
approve Robert Matthew Bernstein, M.D.’s application.

B.

Ratification List

(ii)

February 12, 2026, Ratification List

It was moved by Dr. Sawai, seconded by Dr. Ignacio, and
unanimously carried to approve the February 12, 2026, ratification
list.

Page 3 of 5

Hawaii Medical Board
Minutes of the Meeting of February 12, 2026

New Business

Chair Takanishi asked if anyone from the public would like to
provide oral testimony on any of the items under New Business.
No testimony was offered.

A.  Continuing Medical Education Waiver/Modification Requests

(i)

Miles Wayne Howard, M.D.

It was moved by Vice Chair Belcher, seconded by Dr. Jaffe, and
unanimously voted to grant a three-month extension from the
official notification for Dr. Howard to complete his remaining
continuing education credits.

B.  2026 Legislative Session

(i)

Confirmation of 2026 Legislative Liaisons

It was moved by Dr. Pratt, seconded by Dr. Ignacio, and
unanimously moved to add Dr. Jaffe as a Board’s official
legislative liaison for the 2026 legislative session.

(ii)

Attached List of Measures

The Board provided a list of 2026 bills, using a color-coded
categorization system. Measures in blue include legislation that
falls directly within the Board’s statutory purview or affects its
administrative authority. Measures in red consist of general
health-related items that the Board monitors for situational
awareness and informational purposes, even though they do not
directly relate to the Board’s statutory authority.

It was moved by Dr. Jaffe, seconded by Dr. Ignacio, and
unanimously moved that the Board reaffirms its position that any
individual treating patients located within the State, regardless of
the modality (telehealth or in-person), must be licensed by the
Board.

It was moved by Dr. Ignacio, seconded by Mr. Mun, and
unanimously moved to delegate authority to its legislative liaisons.
These liaisons are authorized to work with the DAG and EOs to
provide timely testimony on behalf of the Board between
scheduled meetings.

C.  Comments on Federation of State Medical Board (FSMB)

Draft Reports

(i)

Report of the FSMB Ethics and Professionalism
Committee on Physician Collective Bargaining and
Unionization (Draft)

Page 4 of 5

Hawaii Medical Board
Minutes of the Meeting of February 12, 2026

(ii)

(iii)

Guidance on Recent Trends in Prescribing and
Dispensing (Draft)
Report of the FSMB Workgroup on Oversight of
Clinical Decision-Making (Draft)

Chair Dr. Takanashi noted the FSMB draft response process, and
members were encouraged to submit individual feedback to the
FSMB prior to the annual meeting.

D.  February 3, 2026, Department of Commerce and Consumers

Affair’s News Release regarding February 3, 2026,
Department of Commerce and Consumers Affair’s News
Release

The Board highlighted an ongoing scam phone call campaign
targeting medical professionals. The Board advised licensees to
verify the source of any inquiries and to never provide personal
information over the phone.

E.  FSMB’s 2026 Annual Meeting Scholarship Announcement

The Board recognized that active representation in national
discussions is essential to ensure Hawai?i can help shape medical
regulation and adopt emerging best practices.

For the FSMB Annual Meeting, scheduled to be held in Baltimore
from April 30 through May 2, 2026, the Board unanimously
selected its official delegates and scholarship recipients. Chair
Takanishi was selected as the Voting Delegate. His attendance is
particularly strategic this year as he is a candidate for the FSMB
Board of Directors. Vice Chair Belcher was selected as the Public
Member Scholarship recipient, and EO Kor was selected as the
Senior Staff Scholarship recipient.

Adjournment:

The meeting adjourned at 3:42 p.m.

Taken and Recorded by:

/s/ Young-Im Wilson
Young-Im Wilson
Supervisory Executive Officer

( x ) Minutes approved as is.
(   ) Minutes approved with changes, see minutes of

Page 5 of 5

---

### 2026-01-15 — Hawaii Medical Board — January 15, 2026

**[MINUTES] 2026-01-15_PVL_Minutes_Medical_2026-01-15.pdf**

Hawaii Medical Board
Minutes of the Meeting of January 15, 2026

HAWAII MEDICAL BOARD
Professional and Vocational Licensing Division
Department of Commerce and Consumer Affairs
State of Hawaii

MINUTES OF MEETING

January 15, 2026

1:00 p.m.

Queen Liliokalani Room
HRH King Kalakaua Building
335 Merchant Street, First Floor
Honolulu, Hawaii 96813

Virtual Videoconference Meeting – Zoom Meeting
https://dcca-hawaii-
gov.zoom.us/j/89970738078?pwd=OkqltIxfbnNfhcdDby6rwIr
VbSkeba.1

Date:

Time:

In-Person
Meeting
Location:

Virtual
Participation:

Recording Link:

https://youtu.be/Kz3jh_KKPxY

Present:

Danny Takanishi Jr., M.D., Chairperson, Honolulu Member
Gary Belcher, Vice Chairperson, Public Member
Andrew “Rick” Fong, M.D., Hawaii Member
Elizabeth “Lisa Ann” Ignacio, M.D, Maui Member
Rebecca Sawai, M.D., Honolulu Member
Angela Pratt, M.D., Honolulu Member
Shari J. Wong, Deputy Attorney General (“DAG”)
Elizabeth Kor, Executive Officer (“EO”)
Young-Im Wilson, Executive Officer
Breyanah Panzardi, Technical Support
Cortnie Tanaka, Administrative Assistant

Excused:

Michael Jaffe, D.O., Osteopathic/Honolulu Member
Wesley Mun, Public Member

Zoom Guest(s):

Jamey Hawk, M.D.
Jaclyn Tolentino, D.O.
Adlai Pappy, M.D

Agenda:

The agenda for this meeting was posted to the State electronic
calendar as required by Hawaii Revised Statues (“HRS”) section
92-7(b).

Call to Order:

The meeting was called to order at 1:08 p.m., at which time
quorum was established.

Chair Dr. Takanishi welcomed everyone to the meeting and

Page 1 of 8

Hawaii Medical Board
Minutes of the Meeting of January 15, 2026

Approval of
Minutes:

proceeded with a roll call of the Board members. All Board
members present confirmed that they were present and alone.

It was moved by Chair Dr. Takanishi, seconded by Vice Chair
Mr. Belcher, and unanimously carried to approve the December
15, 2025, open session and executive session meeting minutes,
with a correction reclassifying Dr. William Hatten from the member
list to the Zoom guest list.

Chair Dr. Takanishi asked if anyone from the public would like to
provide oral testimony on this agenda item. No testimony was
offered.

Chapter 91,
Adjudicatory
Matters:

Chair Dr. Takanishi called for a recess from the meeting at 1:12
p.m. to discuss and deliberate on the following adjudicatory
matters pursuant to Chapter 91, HRS. (Note: Board Members and
staff entered the Zoom Breakout Room.)

A.

In the Matter of the License to Practice Medicine of SAMUEL
E. FULLER, M.D.; MED 2023-2229-L; Settlement
Agreement Prior to Filing of Petition for Disciplinary Action
and Board’s Final Order.

After due consideration of the information received, it was moved
by Dr. Pratt, seconded by Dr. Sawai, and unanimously carried to
approve the aforementioned Settlement Agreement Prior to Filing
of Petition for Disciplinary Action and Board’s Final Order

Following the Board’s review, deliberation, and decision on this
matter pursuant to Chapter 91, HRS, Chair Dr. Takanishi
announced that the Board will reconvene to its Chapter 92, HRS,
meeting at 1:25 p.m. Board members and staff returned to the
main Zoom meeting room. All Board members confirmed that they
were present and alone.

Page 2 of 8

Hawaii Medical Board
Minutes of the Meeting of January 15, 2026

Applications for
Licensure/
Certification:

A.

Applications

It was moved by Vice Chair Mr. Belcher, seconded by Dr. Sawai,
and unanimously carried to enter into executive session at 1:27
p.m., pursuant to HRS §92-5(a)(1), to consider and evaluate
personal information relating to individuals applying for
professional licenses cited in HRS §26-9 and, pursuant to HRS
§92-5 (a)(4), to consult with the Board’s attorney on questions
and issues pertaining to the Board’s powers, duties, privileges,
immunities and liabilities. (Note: Board members and staff entered
the Zoom Breakout Room).

It was moved by Chair Dr. Takanishi, seconded by Dr. Sawai, and
unanimously carried to return to the open session meeting at 3:54
p.m. Board members and staff returned to the main Zoom
meeting room. All Board members present confirmed that they
were present and alone.

(i)  Osteopathic Physician & Surgeon (Permanent/Endorsement)

a.  Andrea Opalenik, D.O.

After due consideration of the information received, it was moved
by Dr. Ignacio, seconded by Dr. Swai, and unanimously carried to
defer Andrea Opalenik, D.O.’s application pending additional
information.

b.  Jaclyn Tolentino, D.O.

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Dr. Ignacio, and unanimously
carried to defer Jaclyn Tolentino, D.O.’s application pending
additional information.

(ii)  Physician (Permanent/Non-Endorsement)

a.  Jamey Joe Hawk, M.D.

After due consideration of the information received, it was moved
by Dr. Pratt, seconded by Dr. Ignacio, and unanimously carried to
approve Jamey Joe Hawk, M.D.’s application without restrictions.

(iii) Physician (Permanent/Endorsement)

a.  Robert Edward Bilbao, M.D.

After due consideration of the information received, it was moved
by Vice Chair Mr. Belcher, seconded by Dr. Ignacio, and
unanimously carried to defer Robert Edward Bilbao, M.D.’s
application pending receipt of the corrected materials.

Page 3 of 8

Hawaii Medical Board
Minutes of the Meeting of January 15, 2026

b.  Adlai Liburne Pappy, M.D.

After due consideration of the information received, it was moved
by Dr. Sawai, seconded by Dr. Ignacio, and unanimously carried
to approve Adlai Liburne Pappy, M.D.’s application without
restrictions.

c.  Michael Robert Schwartz, M.D

After due consideration of the information received, it was moved
by Dr. Fong, seconded by Dr. Ignacio, and unanimously carried to
approve Michael Robert Schwartz, M.D.’s application, pending
receipt of the corrected application.

B.

Ratification List

(ii)

January 15, 2026, Ratification List

It was moved by Dr. Sawai, seconded by Dr. Pratt, and
unanimously carried to approve the January 15, 2026, ratification
list.

New Business

December 11, 2025
Agenda:

Approval of Minutes

It was moved by Chair Dr. Takanishi, seconded by Vice Chair
Mr. Belcher, and unanimously carried to retroactively approve,
effective December 11, 2025, the November 15, 2025, open
session and executive session meeting minutes, with Dr. Pratt
recused because she did not attend the meeting.

Applications:

(i)  Restoration

a.  Diana Gliga, M.D.

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Dr. Sawai, and unanimously
carried to retroactively approve, effective December 11, 2025, the
restoration of Diana Gliga, M.D. with conditional reinstatement,
pending an evaluation of her clinical skills to be determined by the
Board.

(ii)  Physician (Permanent/Endorsement)

a.  Elias Elias, M.D.

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Dr. Pratt, and unanimously

Page 4 of 8

Hawaii Medical Board
Minutes of the Meeting of January 15, 2026

carried to retroactively approve, effective December 11, 2025, the
application of Elias Elias, M.D., without restrictions.

b.  Kamshad Raiszadeh, M.D.

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Dr. Sawai, and unanimously
carried to retroactively approve, effective December 11, 2025, the
application of Kamshad Raiszadeh, M.D., without restrictions.

(iii)

Physician (Permanent/Non-Endorsement)

a.  Frank Hiroshi Harris, M.D.

After due consideration of the information received, it was moved
by chair Dr. Takanishi, seconded by Dr. Pratt, and unanimously
carried to retroactively approve, effective December 11, 2025, the
application of Frank Hiroshi Harris, M.D., without restrictions.

b.  Kenneth Carl Russ, M.D.

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Dr. Sawai, and unanimously
carried to retroactively defer, effective December 11, 2025,
Kenneth Carl Russ, M.D.’s application pending additional
information.

c.  Alan Brewer, M.D.

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Dr. Sawai, and unanimously
carried to retroactively approve, effective December 11, 2025, the
application of Alan Brewer, M.D., without restrictions.

(iv)

EMT, EMT-A, EMT-P, EMT-1

a.  Zachariah Scott Johnson, EMT-1

After due consideration of the information received, it was moved
by chair Dr. Takanishi, seconded by Dr. Ignacio, and unanimously
carried to retroactively approve, effective December 11, 2025, the
application of Zachariah Scott Johnson’s EMT-1, without
restrictions.

New Business:

A.  Delegation to Executive Officer

It was moved by Chair Dr. Takanishi, seconded by Vice Chair
Mr. Belcher, and unanimously carried to retroactively approve,
effective December 11, 2025, delegating authority to the EO to
sign the Board’s final orders for decisions related to the Interstate

Page 5 of 8

Hawaii Medical Board
Minutes of the Meeting of January 15, 2026

Medical Licensure Compact (IMLC). The delegation is intended to
expedite the issuance of licenses through the IMLC.

B.  Request for Voluntary Surrender of License: Paul Dillaway,

DOS-2788

It was moved by Chair Dr. Takanishi, seconded by Dr. Pratt, and
unanimously carried to retroactively accept, effective December
11, 2025, the voluntary relinquishment of Paul Dillaway’s license.

C.  Rescinded Letter of Qualification from IMLC

i.
ii.
iii.

Dheeraj Makkar, M.D.
Sue Xuan Poon, M.D.
Paul E. Cox, M.D.

It was moved by Chair Dr. Takanishi, seconded by Dr. Pratt, and
unanimously carried to retroactively rescind, effective December
11, 2025, the licenses of Dheeraj Makkar, M.D., Sue Xuan Poon,
M.D., and Paul E. Cox, M.D in accordance with the rescinded
letters of qualification from the IMLC.

D.  Proposed Hawaii Medical Board Schedule for 2026

It was moved by Chair Dr. Takanishi, seconded by Dr. Sawai, and
unanimously carried to retroactively approve, effective December
11, 2025, the 2026 meeting schedule.

E.  Endorsement of Nomination of Danny M. Takanishi, Jr., M.D.,
for the Federation of State Medical Boards’ Board of Directors

It was moved by Vice Chair Mr. Belcher, seconded by Dr. Pratt,
and unanimously carried to retroactively approve, effective
December 11, 2025, the endorsement of Danny M. Takanishi, Jr.
M.D., for nomination to the Federation of State Medical Board’s
Board of Directors.

Chapter 91, Adjudicatory Matters

Chair Dr. Takanishi called for a recess from the meeting at 4:16
p.m. to discuss and deliberate on the following adjudicatory
matters pursuant to Chapter 91, HRS. (Note: Board Members and
staff entered the Zoom Breakout Room.)

A.  In the Matter of the Osteopathic Physician’s License of
AMAN K. PATEL, D.O., also known as NIMISHKUMAR
KANTILAL PATEL, also known as NIMISH KANTILAL
PATEL; MED 2025-26-L; Affidavit of Liza O. Canady in
Support of Entry of a Second Final Order Revoking
Respondent’s Now-Restricted License; Exhibits 1-4;

Page 6 of 8

Hawaii Medical Board
Minutes of the Meeting of January 15, 2026

Board’s Second Final Order Revoking Respondent’s Now-
Restricted License (Proposed); Exhibits 1-2.

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Vice Chair Mr. Belcher, and
unanimously carried to approve the aforementioned Affidavit of
Liza O. Canady in Support of Entry of a Second Final Order
Revoking Respondent’s Now-Restricted License; Exhibits 1-4;
Board’s Second Final Order Revoking Respondent’s Now-
Restricted License (Proposed); Exhibits 1-2.

B.

In the Matter of the Physician’s License of SINIKKA LIISA
GREEN, M.D.; MED 2025-475-L; Settlement Agreement
Prior to Filing of Petition for Disciplinary Action and Board’s
Final Order

After due consideration of the information received, it was moved
by Chair Dr. Takanishi, seconded by Vice Chair Mr.

*[document truncated for length]*

---

### 2025-12-11 — Hawaii Medical Board — December 11, 2025

**[MINUTES] 2025-12-11_PVL_Minutes_Medical_2025-12-11.pdf**

Hawaii Medical Board
Minutes of the Meeting of December 11, 2025

HAWAII MEDICAL BOARD
Professional and Vocational Licensing Division
Department of Commerce and Consumer Affairs
State of Hawaii

MINUTES OF MEETING

December 11, 2025

1:00 p.m.

PVL Exam Room 330
HRH King Kalakaua Building
335 Merchant Street, Third Floor
Honolulu, Hawaii 96813

Virtual Videoconference Meeting – Zoom Meeting
https://dcca-hawaii-
gov.zoom.us/j/83410433341?pwd=ao7npcC28B2t3wUYC7g6Qgy
IDSdqTK.1

Date:

Time:

In-Person
Meeting
Location:

Virtual
Participation:

Recording Link:

https://youtu.be/SUQe8SbFA64

Present:

Gary Belcher, Vice Chairperson, Public Member
Elizabeth “Lisa Ann” Ignacio, M.D, Maui Member
Michael Jaffe, D.O, Osteopathic/Honolulu Member
Rebecca Sawai, M.D., Honolulu Member
Angela Pratt, M.D., Honolulu Member
Shari J. Wong, Deputy Attorney General (“DAG”)
Liza Canady, Staff Attorney, Regulated Industries Complaints
Office
Elizabeth Kor, Executive Officer (“EO”)
Young-Im Wilson, Executive Officer
Breyanah Panzardi, Technical Support
Cortnie Tanaka, Administrative Assistant

Excused:

Danny M. Takanishi, Jr., M.D., Chairperson, Honolulu Member
Andrew “Rick” Fong, M.D., Honolulu Member
Wesley Mun, Public Member

Zoom Guest(s):

William Brian Hatten, D.O.
Diana A Gliga, M.D.
Kamshad Raiszadeh, M.D.
Kenneth Carl Russ, M.D.
Zachariah Johnson, EMT-1

Agenda:

The agenda for this meeting was posted to the State electronic
calendar as required by Hawaii Revised Statues (“HRS”) section
92-7(b).

Page 1 of 7

Hawaii Medical Board
Minutes of the Meeting of December 11, 2025

Call to Order:

The meeting was called to order at 1:06 p.m., at which time
quorum was established.

Vice Chair Belcher welcomed everyone to the meeting and
proceeded with a roll call of the Board members. All Board
members present confirmed that they were present and alone.

Approval of
Minutes:

It was moved by Dr. Jaffe, seconded by Dr. Sawai, and
unanimously carried to approve the November 13, 2025, open
session meeting minutes with Dr. Pratt recused because she did
not attend the meeting.

It was moved by Dr. Hatten, seconded by Dr. Sawai, and
unanimously carried to approve the November 13, 2025,
executive session meeting minutes with Dr. Pratt recused
because she did not attend the meeting.

Vice Chair Belcher asked if anyone from the public would like to
provide oral testimony on this agenda item. There was none.

Chapter 91,
Adjudicatory
Matters:

Vice Chair Belcher called for a recess from the meeting at 1:12
p.m. to discuss and deliberate on the following adjudicatory
matters pursuant to Chapter 91, HRS. (Note: Board Members and
staff entered the Zoom Breakout Room.)

A.

In the Matter of the Osteopathic Physician’s License of
AMAN K. PATEL, D.O., also known as NIMISHKUMAR
KANTILAL PATEL, also known as NIMISH KANTILAL
PATEL; MED 2025-26-L; Affidavit of Liza O. Canady in
Support of Entry of a Second Final Order Revoking
Respondent’s Now-Restricted License; Exhibits 1-4;
Board’s Second Final Order Revoking Respondent’s Now-
Restricted License (Proposed); Exhibits 1-2.

After due consideration of the information received, it was moved
by Dr. Hatten, seconded by Dr. Sawai, and unanimously carried
to approve the aforementioned Affidavit of Liza O. Canady in
Support of Entry of a Second Final Order Revoking Respondent’s
Now-Restricted License; Exhibits 1-4; Board’s Second Final Order
Revoking Respondent’s Now-Restricted License (Proposed);
Exhibits 1-2.

B.

In the Matter of the Physician’s License of SINIKKA LIISA
GREEN, M.D.; MED 2025-475-L; Settlement Agreement
Prior to Filing of Petition for Disciplinary Action and Board’s
Final Order

After due consideration of the information received, it was moved
by Dr. Jaffe, seconded by Dr. Sawai, and unanimously carried to
approve the aforementioned Settlement Agreement Prior to Filing
of Petition for Disciplinary Action and Board’s Final Order

Page 2 of 7

Hawaii Medical Board
Minutes of the Meeting of December 11, 2025

Applications for
Licensure/
Certification:

C.

In the Matter of the Osteopathic Physician’s License of
STEPHEN A. FEIG, D.O., also known as STEPHEN
ABOULAFIA FEIG; Notice Prohibiting Practice in Hawaii
Pending Entry of a Final Order Imposing Disciplinary Action,
and Respondent’s Right to Request a Hearing; MED 2025-
491-L; Board’s Final Order (Proposed); Exhibit 1.

After due consideration of the information received, it was moved
by Dr. Sawai, seconded by Dr. Pratt, and unanimously carried to
approve the aforementioned Board’s Final Order (Proposed);
Exhibit 1.

Following the Board’s review, deliberation, and decision on these
matters pursuant to Chapter 91, HRS, Vice Chair Belcher
announced that the Board reconvenes to its Chapter 92, HRS,
meeting at 1:22 p.m. Board members and staff returned to the
main Zoom meeting room. All Board members confirmed that they
were present and alone.

A.

Applications

It was moved by Dr. Jaffe, seconded by Dr. Hatten, and
unanimously carried to enter into executive session at 1:25 p.m.,
pursuant to HRS §92-5(a)(1), to consider and evaluate personal
information relating to individuals applying for professional
licenses cited in HRS §26-9 and, pursuant to HRS §92-5 (a)(4), to
consult with the Board’s attorney on questions and issues
pertaining to the Board’s powers, duties, privileges, immunities
and liabilities. (Note: Board members and staff entered the Zoom
Breakout Room).

It was moved by Dr. Sawai, seconded by Dr. Jaffe, and
unanimously carried to return to the open session meeting at 3:53
p.m. Board members and staff returned to the main Zoom
meeting room. All Board members present confirmed that they
were present and alone.

(i)

Restoration:

a.  Diana Gliga, M.D.

After due consideration of the information received, it was moved
by Vice Chair Belcher, seconded by Dr. Hatten, and unanimously
carried to approve the restoration of Diana Gliga, M.D., with
conditional reinstatement, pending an evaluation of her clinical
skills to be determined by the Board.

(ii)

Physician (Permanent/Endorsement)

a.  Elias Elias, M.D.

Page 3 of 7

Hawaii Medical Board
Minutes of the Meeting of December 11, 2025

After due consideration of the information received, it was moved
by Vice Chair Belcher, seconded by Dr. Pratt, and unanimously
carried to approve the application of Elias Elias, M.D., without
restrictions.

b.  Kamshad Raiszadeh, M.D.

After due consideration of the information received, it was moved
by Dr. Sawai, seconded by Dr. Pratt, and unanimously carried to
approve the application of Kamshad Raiszadeh, M.D., without
restrictions.

(iii)

Physician (Permanent/Non-Endorsement)

a.  Frank Hiroshi Harris, M.D.

After due consideration of the information received, it was moved
by Dr. Pratt, seconded by Dr. Hatten, and unanimously carried to
approve the application of Frank Hiroshi Harris, M.D., without
restrictions.

b.  Kenneth Carl Russ, M.D.

After due consideration of the information received, it was moved
by Dr. Hatten, seconded by Vice Chair Belcher, and unanimously
carried to defer Kenneth Carl Russ, M.D.’s application pending
additional information.

c.  Alan Brewer, M.D.

After due consideration of the information received, it was moved
by Dr. Jaffe, seconded by Dr. Hatten, and unanimously carried to
approve the application of Alan Brewer, M.D., without restrictions.

(iv)

EMT, EMT-A, EMT-P, EMT-1

a.  Zachariah Scott Johnson, EMT-1

After due consideration of the information received, it was moved
by Dr. Ignacio, seconded by Dr. Jaffe, and unanimously carried to
approve the application of Zachariah Scott Johnson’s EMT-1,
without restrictions.

Page 4 of 7

Hawaii Medical Board
Minutes of the Meeting of December 11, 2025

New Business:

A.  Delegation to Executive Officer

It was moved by Vice Chair Belcher, seconded by Dr. Hatten, and
unanimously carried to approve delegating authority to the EO to
sign the Board’s final orders for decisions related to the Interstate
Medical Licensure Compact (IMLC). The delegation is intended to
expedite the issuance of licenses through the IMLC.

B.  Request for Voluntary Surrender of License: Paul Dillaway,

DOS-2788

DAG Wong clarified that the correct terminology for the action was
to “accept the voluntary relinquishment” of the license.

It was moved by Vice Chair Belcher, seconded by Dr. Sawai, and
unanimously carried to accept the voluntary relinquishment of
Paul Dillaway’s license.

C.  Rescinded Letter of Qualification from IMLC

i.
ii.
iii.

Dheeraj Makkar, M.D.
Sue Xuan Poon, M.D.
Paul E. Cox, M.D.

It was moved by Dr. Jaffe, seconded by Vice Chair Belcher, and
unanimously carried to rescind the licenses of Dheeraj Makkar,
M.D., Sue Xuan Poon, M.D., and Paul E. Cox, M.D in accordance
with the rescinded letters of qualification from the IMLC.

D.  Update on the IMLC on Hawaii State Licensure and Review of

current IMLC statistics, workflow, and benefits.

Dr. Jaffe provided an update on the IMLC (or “Compact”) on
Hawaii state licensure following his attendance at the IMLC
annual meeting in Denver, Colorado, on November 17 and 18. He
explained that the IMLC is an agreement among participating
states designed to offer a streamlined secondary pathway for
physicians to obtain a state medical license. It is not a single
license covering all states; rather, physicians select a principal
state of licensure (PSL), and once ratified, they can use that
license to expedite licensure in other participating states. Dr. Jaffe
reported that the IMLC has been operational for eight years,
currently involves 44 states, and has resulted in over 49,000
physicians obtaining licensure through this pathway. Nationally,
54% of these physicians provide services in rural or underserved
areas, and 51% receive licensure in seven days or less. The
Compact also facilitates the sharing of disciplinary actions among
state boards, enhancing transparency.

Page 5 of 7

Hawaii Medical Board
Minutes of the Meeting of December 11, 2025

Dr. Jaffe discussed Hawaii’s current challenge with the IMLC.
While Hawaii has been issuing licenses through the Compact
since January of the current year, it is not yet a PSL, meaning that
Hawaii physician licenses cannot serve as a physician’s primary
license to apply for other physician licenses through the Compact.
The primary obstacle to becoming a PSL is that the FBI (Federal
Bureau of Investigation) has not granted Hawaii access to
perform the required background checks. Dr. Jaffe noted that
although the Board requested approval directly from the FBI, the
request was denied. He highlighted the seemingly inconsistent
nature of the FBI’s approval process, noting that the Pennsylvania
Board of Registered Nurses received approval using similar
statutory language.

Regarding a path forward, Dr. Jaffe suggested coordinating with
executive medical board directors to secure the necessary FBI
certification. DAG Wong added that they are currently working
with the Hawaii Criminal Justice Data Center, the state agency
that liaises with the FBI and has successfully obtained
fingerprinting and FBI clearances for other DCCA (Department of
Commerce and Consumer Affairs) exemptions, such as for
nurses, to obtain approval. Dr. Jaffe concluded by thanking the
Board for the opportunity to represent Hawaii at the IMLC annual
meeting.

E.  Proposed Hawaii Medical Board Schedule for 2026

F.  Endorsement of Nomination of Danny M. Takanishi, Jr., M.D.,
for the Federation of State Medical Boards’ Board of Directors

It was moved by Vice Chair Belcher, seconded by Dr. Sawai, and
unanimously carried to approve the endorsement of Danny M.
Takanishi, Jr. M.D., for nomination to the Federation of State
Medical Board’s Board of Directors.

G.  Proposed Legislation Relating to the Physician Assistant (PA)

Compact.

EO Wilson reported that the Governor’s Office has been informed
of the Board’s general support for the proposed legislation, as the
Governor could not wait until the m

*[document truncated for length]*

---

### 2025-11-13 — Hawaii Medical Board — November 13, 2025

**[MINUTES] 2025-11-13_PVL_Minutes_Medical_2025-11-13.pdf**

Date

Time

In-Person
Meeting
Location

Virtual
Participation

November 13, 2025

1:00 p.m.

PVL Exam Room 330
HRH King Kalakaua Building
335 Merchant Street, Third Floor
Honolulu, Hawaii 96813

Virtual Videoconference Meeting – Zoom Meeting
https://dcca-hawaii-
gov.zoom.us/j/83410433341?pwd=ao7npcC28B2t3wUYC7g6Qgy
IDSdqTK.1

Recording Link

https://youtu.be/mV8VNAEZw48

Present

Danny M. Takanishi, Jr., M.D., Chairperson, Honolulu Member
Gary Belcher, Public, Vice Chairperson, Public Member
Andrew “Rick” Fong, M.D., Hawaii Member
William Brian Hatten, D.O., Osteopathic Member
Elizabeth “Lisa Ann” Ignacio, M.D, Maui Member
Michael Jaffe, D.O, Osteopathic/Honolulu Member
Wesley Mun, Public
Rebecca Sawai, M.D., Honolulu Member
Shari J. Wong, Deputy Attorney General (“DAG”)
Elizabeth Kor, Executive Officer (“EO”)
Young-Im Wilson, Executive Officer
Julie Halapio, Technical Support
Cortnie Tanaka, Administrative Assistant

Excused:

Angela Pratt, M.D., Honolulu Member

Zoom Guest(s):

Jacob Raymond Richard M.D.
Oren Ganor M.D.
Jonathan Kanevsky M.D.
Wayne Tran M.D.
Daniel Holbert M.D.

HAWAII MEDICAL BOARD Professional and Vocational Licensing Division Department of Commerce and Consumer Affairs State of Hawaii MINUTES OF MEETING Alexandria Rose Quiring

Agenda:

The agenda for this meeting was posted to the State electronic
calendar as required by Hawaii Revised Statues (“HRS”) section
92-7(b).

Call to Order

The meeting was called to order at 1:03 p.m., at which time
quorum was established.

Chair Takanishi welcomed everyone to the meeting and
proceeded with a roll call of the Board members. All Board
members present confirmed that they were present and alone.

Approval of Minutes

It was moved by Dr. Ignacio, seconded by Dr. Sawai, and
unanimously carried to approve the August 14, 2025, open
session meeting minutes, and August 14, 2025, executive session
meeting minutes with the spelling correction of the DAG’s name.

Chair Takanishi asked if anyone from the public would like to
provide oral testimony on this agenda item. There was none.

Chapter 91,
Adjudicatory
Matters

Chair Takanishi called for a recess from the meeting at 1:10 p.m.
to discuss and deliberate on the following adjudicatory matters
pursuant to Chapter 91, HRS.

A. In the Matter of the Physician’s License of DAVID NATHANIEL
SMITH, M.D., MED-2023-211-L; Hearing Officer’s Findings of
Fact, Conclusions of Law, and Recommended Order, Board’s
Final Order

After due consideration of the information received, it was moved
by Dr. Hatten, seconded by Dr. Jaffe, and unanimously carried to
approve the aforementioned Hearing Officer’s Findings of Fact,
Conclusions of Law, and Recommended Order, Board’s Final
Order.

B. In the Matter of the License to Practice Medicine of

ALEXANDER D. LEE, M.D., also known as ALEXANDER
DONG LEE, M.D., MED 2023-257-L; Settlement Agreement
Prior to Filing of Petition for Disciplinary Action and Board’s
Final Order; Exhibits “1”-“2”

After due consideration of the information received, it was moved
by  Dr. Jaffe, seconded by Dr. Sawai, and unanimously carried to
approve the aforementioned Settlement Agreement Prior to Filing
of Petition for Disciplinary Action and Board’s Final Order; Exhibits
“1”-“2”.

Applications for
License/
Certification

C. In the Matter of the Physician’s License of BERNARD K.

CHUN, M.D., MED 2024-143-L; Settlement Agreement After
Filing of Petition For Disciplinary Action and Board’s Final
Order, Petition for Disciplinary Action Against Physician’s
License; Demand for Disclosure

After due consideration of the information received, it was moved
by Dr. Sawai, seconded by Dr. Hatten, and unanimously carried
to approve the aforementioned Settlement Agreement After Filing
of Petition For Disciplinary Action and Board’s Final Order,
Petition for Disciplinary Action Against Physician’s License;
Demand for Disclosure with Mr. Belcher recusing himself from the
vote.

Chair Takanishi asked if anyone from the public would like to
provide oral testimony. There was none.

A.

Applications

It was moved by Dr. Jaffe, seconded by Mr. Belcher, and
unanimously carried to enter into executive session at 1:34 p.m.,
pursuant to HRS §92-5(a)(1), to consider and evaluate personal
information relating to individuals applying for professional
licenses cited in HRS §26-9 and, pursuant to HRS §92-5 (a)(4), to
consult with the Board’s attorney on questions and issues
pertaining to the Board’s powers, duties, privileges, immunities
and liabilities. (Note: Board members and staff entered the Zoom
Breakout Room).

It was moved by Dr. Sawai, seconded by Dr. Hatten, and
unanimously carried to return to the open session meeting at 4:15
p.m. Board members and staff returned to the main Zoom
meeting. All Board members present confirmed that they were
present and alone.

(i)

Physician (Permanent/Endorsement):

a. Christopher Braga, M.D.

After due consideration of the information received, it was moved
by Dr. Jaffe, seconded by Dr. Hatten, and unanimously carried to
approve the application of Christopher Braga, M.D., without
restrictions.

b. Jim Seraj, M.D.

After due consideration of the information received, it was moved
by Dr. Takanishi, seconded by Dr. Jaffe, and unanimously carried
to defer Dr. Jim Seraj’s application pending additional information.

c. Trey Lee Kamplain, M.D.

After due consideration of the information received, it was moved
by Dr. Ignacio, seconded by Dr. Hatten, and unanimously carried
to approve the application of Trey Lee Kamplain, M.D., without
restrictions.

d. Jacob Raymond Richard, M.D.

After due consideration of the information received, it was moved
by Dr. Sawai, seconded by Mr. Mun, and unanimously carried to
approve the application of Jacob Raymond Richard, M.D., without
restrictions.

e. Oren Ganor, M.D.

After due consideration of the information received, it was moved
by Dr. Takanishi, seconded by Dr. Jaffe, and unanimously carried
to approve the application of Oren Ganor, M.D., without
restrictions.

f. Sujatha Murali, M.D.

After due consideration of the information received, it was moved
by Dr. Hatten, seconded by Dr. Sawai, and unanimously carried to
approve the application of Sujatha Murali, M.D., without
restrictions.

(ii)

Physician (Permanent/Non-Endorsement):

a. Jonathan Kanevsky, M.D.

After due consideration of the information received, it was moved
by Dr. Takanishi, seconded by Dr. Sawai, and unanimously
carried to approve the application of Jonathan Kanevsky, M.D.,
without restrictions.

b. Lida Zhen, M.D.

After due consideration of the information received, it was moved
by Dr. Fong, seconded by Dr. Hatten, and unanimously carried to
approve the application of Lida Zhen, M.D., without restrictions.

c. Wayne Tran, M.D.

After due consideration of the information received, it was moved
by Dr. Hatten, seconded by Mr. Mun, and unanimously carried to

defer Dr. Wayne Tran’s application pending additional
information.

d. Daniel Holbert, M.D.

After due consideration of the information received, it was moved
by Dr. Ignacio, seconded by Dr. Hatten, and unanimously carried
to approve the application of Daniel Holbert, M.D., without
restrictions.

(iii)

Physician Assistant

a. Adewale Adewumi Bakare, P.A.

After due consideration of the information received, it was moved
by Mr. Mun, seconded by Dr. Jaffe, and unanimously carried to
approve the application of Adewale Adewumi Bakare, P.A.,
without restrictions.

(iv)

EMT, EMT-A, EMT-P, EMT-1:

a. Alexandria Rose Quiring, EMT-P

After due consideration of the information received, it was moved
by Mr. Mun, seconded by Dr. Jaffe, and unanimously carried to
defer Alexandria Rose Quiring’s application pending additional
information.

(v)

Restoration

a. Diana Gliga, M.D.

Due to time constraints imposed by the Sunshine Law (requiring
adjournment by 4:30 p.m.), the Board deferred the matter of Dr.
Diana Gliga’s application to the next scheduled meeting to allow
for more time for discussion.

(vi)

Osteopathic Physician & Surgeon
(Permanent/Endorsement)

a. Frank Joseph Suppa, D.O.

Due to time constraints imposed by the Sunshine Law (requiring
adjournment by 4:30 p.m.), the Board deferred the matter of Dr.
Frank Joseph Suppa’s application to the next scheduled meeting
to allow for more time for discussion.

B. Ratification List (see attached List)

(i) October 9, 2025, Ratification List

It was moved by Dr. Jaffe, seconded by Mr. Mun, and
unanimously carried to ratify the attached lists of individuals for
licensure or certification from October 9, 2025.

New Business

Due to time constraints imposed by the Sunshine Law(requiring
adjournment by 4:30 p.m.), the Board deferred the matter of New
Business to the next scheduled meeting to allow for more time for
discussion.

Advisory
Committees

A.

(i)

Emergency Medical Service (EMS) Personnel

Reappointment to the EMS Personnel Advisory
Committee:

a. Dennis Ma’ele, Paramedic
b. Jeffery Zuckermick, Paramedic
c. Ronald Kuroda, MD
d. Elizabeth Char, MD

It was moved by Dr. Hatten, seconded by Mr. Mun, and
unanimously carried to approve the EMS Personnel Advisory
Committee.

Next Meeting

December 11, 2025

Virtual Videoconference Meeting – Zoom Webinar

In-Person
Meeting
Location:

  Queen Liliuokalani Conference Room
  King Kalakaua Building
  335 Merchant Street, First Floor
  Honolulu, HI 96813

Adjournment

The meeting adjourned at 4:28 p.m.

Taken and Recorded by:

/s/ Young-Im Wilson
Young-Im Wilson
Executive Officer

(x) Minutes approved as is.
(   ) Minutes approved with changes

---

### 2025-08-01 — Hawaii Medical Board — August 01, 2025

**[MINUTES] 2025-08-01_PVL_Minutes_Medical_2025-08-14.pdf**

Hawaii Medical Board
Minutes of the Meeting of August 14, 2025

HAWAII MEDICAL BOARD
Professional and Vocational Licensing Division
Department of Commerce and Consumer Affairs
State of Hawaii

MINUTES OF MEETING

August 14, 2025

1:00 p.m.

Queen Liliuokalani Conference Room
HRH King Kalakaua Building
335 Merchant Street, First Floor
Honolulu, Hawaii 96813

Virtual Videoconference Meeting – Zoom Meeting
https://dcca-
hawaii.gov.zoom.us/j/88309119412?pwd=g2wzgoYSxfcqmlrXc1Ae
gsF7IBz9uf.1

Date

Time

In-Person
Meeting
Location

Virtual
Participation

Recording Link

https://www.youtube.com/watch?v=b5WfQm2M3Oc

Present

Danny M. Takanishi, Jr., M.D., Chairperson, Honolulu Member
Gary Belcher, Public, Vice Chairperson, Public Member
Andrew “Rick” Fong, M.D., Hawaii Member
William Brian Hatten, D.O., Osteopathic Member
Elizabeth “Lisa Ann” Ignacio, M.D, Maui Member
Michael Jaffe, D.O, Osteopathic/Honolulu Member
Wesley Mun, Public
Angela Pratt, M.D., Honolulu Member
Rebecca Sawai, M.D., Honolulu Member
Shari J. Wong, Deputy Attorney General (“DAG”)
Reid Horimoto, Executive Officer
Young-Im Wilson, Executive Officer
Julie Halapio, Administrative Assistant
Johnny Li (Technical Support)

Excused:

None

In-Person
Guest(s):

Thomas Craig III M.D.

Zoom Guests:

Kieran Melody, M.D.
Jordon Post, M.D.

Page 1 of 6

Hawaii Medical Board
Minutes of the Meeting of August 14, 2025

Pola Chojecka, M.D.
Curtis Bekkum, M.D.

Agenda:

The agenda for this meeting was posted to the State electronic
calendar as required by Hawaii Revised Statues (“HRS”) section
92-7(b).

Call to Order

The meeting was called to order at 1:07 p.m. at which time quorum
was established.

Approval of
Minutes

Chair Takanishi welcomed everyone to the meeting and proceeded
with a roll call of the Board members. All Board members confirmed
that they were present and alone.

Chair Takanishi asked if anyone from the public would like to
provide oral testimony on this agenda item. There was none.

A motion was made to approve February 13, 2025, open session
meeting minutes, March 13, 2025, open session meeting minutes,
April 10, 2025, open session meeting minutes, March 13, 2025,
executive session meeting minutes, and April 10, 2025, executive
session meeting minutes. Mr. Mun abstained from the vote on the
February 13, 2025, minutes as he was not present. The motion
passed unanimously.

Chapter 91,
Adjudicatory
Matters

The board moved by Dr. Pratt, seconded by Mr. Belcher, and
unanimously carried to move the summary suspension of Paul
Dillaway, listed on the agenda as item 6C, to Chapter 91, HRS,
Adjudicatory Matters, number three.

The Board recessed into adjudicatory session at 1:17 p.m. to
address agenda items 3A, 3B, 3C, 3D, 3E, 3F, 3G, 3H, 3I, and 6C.

It was moved by Dr. Hatten, seconded by Dr. Pratt, and
unanimously carried to return to the open session meeting at 2:10
p.m. Board members and staff returned to the main Zoom meeting.
All Board members confirmed that they were present and alone.

A motion was made to approve the settlement agreement in the
matter of Joseph Palumbo, D.O. (MED 2024-4-L). The motion
passed unanimously.

Page 2 of 6

Hawaii Medical Board
Minutes of the Meeting of August 14, 2025

A motion was made to approve the settlement agreement in the
matter of Roy Matsuyama, M.D. (MED 2019-84-L). The motion
passed unanimously.

A motion was made to approve the settlement agreement in the
matter of William Dang, M.D. (MED 2024-140-L). The motion
passed unanimously.

A motion was made to approve the settlement agreement in the
matter of Franklin C.H. Lee, M.D. (MED 2023-172-L). The motion
passed unanimously.

A motion was made to approve the settlement agreement in the
matter of Qasem Noori, M.D. (MED 2025-51-L). The motion passed
unanimously.

A motion was made to approve the settlement agreement in the
matter of Henry Sakow, M.D. (MED 2024-0292-L). The motion
passed unanimously.

A motion was made to approve the settlement agreement in the
matter of Eesha Bhattacharyya, M.D. (MED 2024-0187-L). The
motion passed unanimously.

A motion was made to approve the settlement agreement in the
matter of Amir Qureshi, M.D. (MED 2025-0005-L). The motion
passed unanimously.

A motion was made to approve the Board's final order in the matter
of Aman Patel, D.O. (MED 2025-26-L). The motion passed
unanimously.

A motion was made to approve a summary suspension of the
license of Paul Dillaway, D.O. until the investigatory procedure in
the State of Wyoming concludes. The motion passed unanimously.

Chair Takanishi asked if anyone from the public would like to
provide oral testimony. There was none.

A.

Applications

It was moved by Dr. Hatten, seconded by Mr. Belcher, and
unanimously carried to enter into executive session at 2:15 p.m.,
pursuant to HRS §92-5(a)(1), to consider and evaluate personal

Page 3 of 6

Applications for
License/
Certification

Hawaii Medical Board
Minutes of the Meeting of August 14, 2025

information relating to individuals applying for professional licenses
cited in HRS §26-9 and, pursuant to HRS §92-5 (a)(4), to consult
with the Board’s attorney on questions and issues pertaining to the
Board’s powers, duties, privileges, immunities and liabilities. (Note:
Board members and staff entered the Zoom Breakout Room).

It was moved by Dr. Hatten, seconded by Dr. Pratt, and
unanimously carried to return to the open session meeting at 3:56
p.m. Board members and staff returned to the main Zoom meeting.
All Board members confirmed that they were present and alone.

Chair Takanishi proceeded with a roll call of the Board members in
the Zoom Breakout Room.  All members confirmed that they were
present and alone.

(i)

Physician (Permanent/Endorsement):

a.  Brian Joseph Allen, M.D.

After due consideration of the information received, it was moved by
Dr. Sawai, seconded by Dr. Hatten, and unanimously carried to
defer the application of Brian Joseph Allen, M.D. to allow him an
opportunity to appear before the Board to provide additional
testimony.

b.  Kieran Melody, M.D.

 After due consideration of the information received, it was moved
by Dr. Takanishi, seconded by Dr. Ignacio, and unanimously carried
to approve the application of Kieran Melody, M.D. pending receipt
of an updated application with correction to the applicant's response
to item six.

(ii)

Physician (Permanent/Non-Endorsement):

a.  Jordon Ryan Post, M.D.

After due consideration of the information received, it was moved by
Mr. Belcher, seconded by Dr. Sawai, and unanimously carried to
defer Dr. Jordon Post, M.D.’s application pending more information.

b.  Thomas Craig III, M.D.

After due consideration of the information received, it was moved by
Dr. Fong, seconded by Dr. Jaffe, and unanimously carried to defer

Page 4 of 6

Hawaii Medical Board
Minutes of the Meeting of August 14, 2025

Dr. Thomas Craig III, M.D.'s application pending completion of an
evaluation of competency from an organization of the board's
choosing and the submission of that evaluation to the board. Mr.
Mun abstained from the vote.

c.  Kerisimasi Reynolds, D.O.

After due consideration of the information received, it was moved by
Dr. Jaffe, seconded by Dr. Hatten, and unanimously carried to
approve the application of Kerisimasi Reynolds, D.O. without
contingencies or restrictions.

B.  Ratification List (see attached List)

(i)  Augst 14, 2025, Ratification List

It was moved by Dr. Ignacio, seconded by Dr. Sawai, and
unanimously carried to ratify the attached lists of individuals for
licensure or certification from August 14, 2025.

Request for
Removal of
License
Condition(s)

Pola Chojecka, MD-21525

It was moved by Mr. Belcher, seconded by Dr. Pratt, and
unanimously carried to remove condition(s) from Dr. Chojecka’s
license.

New Business

A. Approval of Regulated Industries Complaints Office (RICO)
Advisory Committee Member Appointees

It was moved by Dr. Hatten, seconded by Dr. Pratt, and
unanimously carried to approve RICO Advisory Committee Member
Appointees.

B. Reinstatement of License Request: Curtis Bekkum, M.D.

No action taken at this meeting, pending judiciary process.

Executive Officer
Report

A. 2025 Legislative Session – Bill Discussion & Updates

Informational only.

B. Reminder to complete Mandatory Ethics Training

Informational only.

Page 5 of 6

Hawaii Medical Board
Minutes of the Meeting of August 14, 2025

Chair Takanishi asked if anyone from the public would like to
provide oral testimony. There was none.

Next Meeting

October 9, 2025

Virtual Videoconference Meeting – Zoom Webinar

In-Person          Queen Liliuokalani Conference Room
Meeting             King Kalakaua Building
Location:           335 Merchant Street, First Floor
                          Honolulu, HI 96813

Adjournment

The meeting adjourned at 4:14 p.m.

Taken and Recorded by:

/s/ Young-Im Wilson
Young-Im Wilson
Executive Officer

(   ) Minutes approved as is.
( x ) Minutes approved with changes

Page 6 of 6
