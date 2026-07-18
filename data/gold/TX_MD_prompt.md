You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Texas Medical Board** (TX) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/TX/TX_MD#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-08-19]` — Texas Medical Board — August 19, 2026
- `[2026-08-13]` — Texas Medical Board — August 13, 2026
- `[2026-06-29]` — Texas Medical Board — June 29, 2026
- `[2026-06-11]` — Texas Medical Board — June 11, 2026
- `[2026-05-13]` — Texas Medical Board — May 13, 2026
- `[2026-04-13]` — Texas Medical Board — April 13, 2026
- `[2026-03-26]` — Texas Medical Board — March 26, 2026
- `[2025-12-11]` — Texas Medical Board — December 11, 2025
- `[2025-10-16]` — Texas Medical Board — October 16, 2025
- `[2025-09-18]` — Texas Medical Board — September 18, 2025
- `[2025-08-14]` — Texas Medical Board — August 14, 2025

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: TX_MD
state: TX
---

# Texas Medical Board — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Texas Medical Board | [Minutes page](TX_MD_MINUTES_URL) |

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

Sources-table URL: https://www.tmb.texas.gov/about-us/boards-and-committees/events-agendas-and-meeting-minutes

## Meeting Minutes Data

Board: Texas Medical Board
State: TX
Code: TX_MD

### 2026-08-19 — Texas Medical Board — August 19, 2026

*(No extracted text available)*

---

### 2026-08-13 — Texas Medical Board — August 13, 2026

*(No extracted text available)*

---

### 2026-06-29 — Texas Medical Board — June 29, 2026

*(No extracted text available)*

---

### 2026-06-11 — Texas Medical Board — June 11, 2026

*(No extracted text available)*

---

### 2026-05-13 — Texas Medical Board — May 13, 2026

*(No extracted text available)*

---

### 2026-04-13 — Texas Medical Board — April 13, 2026

*(No extracted text available)*

---

### 2026-03-26 — Texas Medical Board — March 26, 2026

*(No extracted text available)*

---

### 2025-12-11 — Texas Medical Board — December 11, 2025

**[AGENDA] 2025-12-11_Agenda-Medical-2025-Dec-Executive.pdf**

Texas Medical Board

 EXECUTIVE COMMITTEE
1801 CONGRESS AVE #9.900 / VIDEOCONFERENCE
AUSTIN TEXAS
THURSDAY, DECEMBER 11TH, 2025
9:00 A.M.

This meeting will be open to the public at the above location and will proceed by
videoconference, as allowed under Texas Government Code Sec. 155.127.  The location above
shall have two-way audio video communication with each of the other locations during the
meeting.  The President or Presiding Officer of the board will be physically present at the
location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

12/11/2025 Executive –  https://bit.ly/121125DPRC
Or call in (audio only) +1 512-596-3865,,978696722# United States Austin

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to order and roll call.

2.  Committee member report.

3.  Adjourn.

Executive Sessions:  The Board may close the meeting to the public and continue in
executive session for the following reasons:

a.  Private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the
authority of the Open Meetings Act Section 551.071, Government Code.

b.  Deliberations concerning personnel matters under the authority of the Open Meetings Act
Section 551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote
with regard to any matter that may be considered or discussed.  A certified agenda of any
executive session will be made.

Persons requiring special accommodations, including the use of an interpreter, due to a
disability should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

Committee members:
Sherif Zaafran, MD, Chair
Kandace Farmer, DO
Michael Cokinos
Manuel “Manny” Quinones, Jr., MD
Robert Martinez, MD

12/4/2025

2

---

**[AGENDA] 2025-12-11_Agenda-Medical-2025-Dec-Finance.pdf**

Texas Medical Board

 FINANCE COMMITTEE
1801 CONGRESS AVE., #9.900/VIDEOCONFERENCE
AUSTIN TEXAS
THURSDAY, DECEMBER 11TH, 2025
9:05 A.M.

This meeting will be open to the public at the above location and will proceed by
videoconference, as allowed under Texas Government Code Sec. 155.127.  The location above
shall have two-way audio video communication with each of the other locations during the
meeting.  The President or Presiding Officer of the board will be physically present at the
location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

12/11/2025 Finance –  https://bit.ly/121125DPRC
Or call in (audio only) +1 512-596-3865,,978696722# United States Austin

 For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to order and roll call.

2.  Budget report

3.  Adjourn.

Executive Sessions:  The Board may close the meeting to the public and continue in executive
session for the following reasons:

a.
Private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the authority
of the Open Meetings Act Section 551.071, Government Code.

Deliberations concerning personnel matters under the authority of the Open Meetings Act

b.
Section 551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote with
regard to any matter that may be considered or discussed.  A certified agenda of any executive
session will be made.

Persons requiring special accommodations, including the use of an interpreter, due to a disability
should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

Committee members:
Michael Cokinos, Chair
Sharon Barnes
Kandace Farmer, DO
Sherif Zaafran, MD

12/4/2025

2

---

**[AGENDA] 2025-12-11_Agenda-Medical-2025-Dec-DPRC.pdf**

Texas Medical Board
DISCIPLINARY PROCESS REVIEW COMMITTEE
1801 CONGRESS AVE., # 9.900/ VIDEOCONFERENCE
AUSTIN, TEXAS
THURSDAY, DECEMBER 11TH, 2025
9:15 A.M.

This meeting will be open to the public at the above location and will proceed by videoconference,
as allowed under Texas Government Code Sec. 155.127.  The location above shall have two-way
audio video communication with each of the other locations during the meeting.  The President or
Presiding Officer of the board will be physically present at the location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

12/11/2025 DPRC –  https://bit.ly/121125DPRC
Or call in (audio only) +1 512-596-3865,,978696722# United States Austin

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to Order and Roll Call.

2.  Texas Physician Health Program (TXPHP):

A.  Discussion, recommendation, and possible action regarding referrals

i.  Accept referrals
ii.  Return to TXPHP

B.   Report on Emergent Referrals
C.  Other discussion items – Program Activity Report

3.  Reports and discussion regarding the Investigation, Litigation and Compliance Departments.

A.  Enforcement Activity Report
B.  Warning Letters Report
C.  Criminal Review Report
D.  Reports Regarding Files Over One Year

4.  Consideration and approval of membership of the Expert Physician Panel.

5.  Discussion and Possible Action Regarding Review of Probationers’ Appearances.

6.  Discussion, recommendation, and possible action regarding routine follow-up on files

previously referred from DPRC.

7.  Cases Recommended for Dismissal.
A. Non-Standard of Care Cases
B. Standard of Care Cases

8.  Review, discussion, and possible action regarding appeals of dismissed complaints.

A.  Non-Standard of Care Cases
B.  Standard of Care Cases

9.  Review, discussion, and possible action regarding appearing appeals of dismissed

complaints.

10. Adjourn

EXECUTIVE SESSIONS:

The Texas Medical Board may close the meeting to the public and continue in executive session
for deliberations regarding disciplinary action or private consultation and advice of counsel.

This authority is provided under The Medical Practice Act Sections 152.009, 160.006 through
.008, 164.007(c), and 164.202 & .203, Occupations Code; and Open Meetings Act Section
551.071, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote with
regard to any matter that may be considered or discussed.  A certified agenda of any executive
session will be made.
---------------------------------------------------------------------------------------------------------------------
Persons requiring special accommodations, including the use of an interpreter, due to a disability
should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.state.tx.us at least five (5) working days prior to the Board meeting.

Committee Members (10)

Manuel Quinones, Jr., M.D., Chair
Sharon Barnes
Devinder S. Bhatia, M.D.
James S. Distefano, D.O.
Mary “Kelly” Green, M.D.
Zachary “Zach” Jones, M.D.
LuAnn Morgan
Jason K. Tibbels, M.D.
Linda Troncoso
Sherif Z. Zaafran, M.D

---

**[AGENDA] 2025-12-11_Agenda-Medical-2025-Dec-Licensure.pdf**

TEXAS MEDICAL BOARD
 LICENSURE COMMITTEE
DECEMBER 11TH, 2025
9:15 a.m.
1801 CONGRESS AVE # 9.101 / VIDEOCONFERENCE

Austin, Texas

This meeting will be open to the public at the above location and will proceed by
videoconference, as allowed under Texas Government Code Sec. 155.127.  The location above
shall have two-way audio video communication with each of the other locations during the
meeting.  The President or Presiding Officer of the board will be physically present at the
location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

12/11/2025 Licensure – https://bit.ly/121125LIC
Dial in by phone +1 512-596-3865,,543522131# United States, Austin

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to order and roll call.

2.  Discussion, recommendation and possible action regarding applicants for licensure,

permits, and certification.

a.  Proposed orders offered by the Executive Director
b.  Physician licensure applicants to be licensed
c.  Surgical assistant licensure applicants to be licensed
d.  Acudetox applicants to be certified

3.  Report on physician licensure statistics

4.  Discussion, recommendation and possible action regarding Nonprofit Health

Organizations

a.  Applicants for initial certification
b.  Requests for biennial recertification
c.  Cancellation of organizations certified as Nonprofit Health Organizations

5.  Report on Renewals for Advertising Board Certification

6.  Discussion, recommendation and possible action regarding licensee requests

7.  Discussion, recommendation and possible action regarding Applicants appearing

concerning eligibility*

8.  Applicants for Advertising Board Certification

9.  Adjourn

*Some or all of the discussion on the agenda item may be held in Executive Session under the
authority of the Medical Practice Act and the Open Meetings Act, as noted below.   Executive
Sessions may also be conducted during discussion on other agenda items for one or more of the
reasons noted below.

 Executive Sessions:  The Texas Medical Board may close the meeting to the public and
continue in executive session for the following reasons:

a.  Deliberations concerning licensure applications and the character and fitness of

applicants under the authority of The Medical Practice Act Sections 152.009 and
155.058, Occupations Code.

b.  Deliberations concerning disciplinary action, investigative information, peer review
information, and possible rehabilitation orders under the authority of The Medical
Practice Act Sections 152.009, 160.006-160.008, and 164.007(c) Occupations Code.

c.  Private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the
authority of the Open Meetings Act Section 551.071, Government Code.

d.  Deliberations concerning personnel matters under the authority of the Open Meetings Act

Section 551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote
with regard to any matter that may be considered or discussed.  A certified agenda of any
executive session will be made.

Persons requiring special accommodations, including the use of an interpreter, due to a
disability should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

Committee Members:
Roberto “Robert” Martinez, MD, Chair
Michael Cokinos
Garry D. Crain
George De Loach, DO
Luisa del Rosal
Kandace Farmer, DO

Tomeka Herod
Jayaram B. Naidu, MD
David G. Vanderweide, M.D.

---

**[AGENDA] 2025-12-11_Agenda-Medical-2025-Dec-Full.pdf**

Texas Medical Board
1801 CONGRESS, AVE., # 9.900 / VIDEOCONFERENCE
AUSTIN, TEXAS
DECEMBER 11-12, 2025

This meeting will be open to the public at the above location and will proceed by
videoconference, as allowed under Texas Government Code Sec. 155.127.  The location above
shall have two-way audio video communication with each of the other locations during the
meeting.  The President or Presiding Officer of the board will be physically present at the
location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio links below.

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

THURSDAY, DECEMBER 11, 2025 COMMITTEES

  9:00 a.m.

  9:05 a.m.

Executive Committee, Room 9.900
12/11/25 Executive – https://bit.ly/121125DPRC
Dial in by phone +1 512-596-3865,,978696722# United States, Austin

Finance Committee, Room 9.900
12/11/25 Finance – https://bit.ly/121125DPRC
Dial in by phone +1 512-596-3865,,978696722# United States, Austin

  9:15 a.m.  Disciplinary Process Review Committee, Room 9.900

  9:15 a.m.

12/11/25 DPRC – https://bit.ly/121125DPRC
Dial in by phone +1 512-596-3865,,978696722# United States, Austin
Licensure Committee, Room 9.101
12/11/2025 Licensure – https://bit.ly/121125LIC
Dial in by phone +1 512-596-3865,,543522131# United States, Austin

Texas Medical Board
1801 CONGRESS, AVE., # 9.900/ VIDEOCONFERENCE
AUSTIN, TEXAS

8:00 a.m. FRIDAY, DECEMBER 12th, 2025, FULL BOARD MEETING

12/12/25 Full Board – https://bit.ly/121225FB

Dial in by phone (Audio only) +1 512-596-3865,,829257335# United States, Austin

1.  Full Board call to order, roll call, and Mission Statement

Our Mission is to protect and enhance the public’s health, safety, and welfare by establishing
and maintaining standards of excellence used in regulating the practice of medicine and ensuring
quality health care for the citizens of Texas through licensure, discipline, and education.

2.  Board Member Report.

3.  Consideration and possible action regarding dispositions below minimum guidelines

4.  Consideration and approval of Mediated Settlement Agreed Orders.

5.  Consideration and possible action for Remedial Plans.

6.  Consideration and possible action for Agreed Orders.

7.  Consideration and approval of Modification Request/Termination Request Orders.

8.  Consideration and approval of Modification Request/Termination Request of Non-

Public Rehabilitation Orders.

9.  Consideration and approval of Cease-and-Desist Orders.

10.  Consideration and approval of Revised, Vacated, or Amended Orders.

11.  Consideration and approval of Consent Orders.

12.  Consideration and approval of Determination of Default.

Agenda item #13 at 9:00 a.m.

13.  Consideration and possible action regarding Rehearing for Mary Talley Bowden, M.D.

SOAH Docket No 503-23-17769.MD

Agenda item #14 at 9:15 a.m.

14.  Consideration and approval of Proposal for Decision.

a.  Maria Dolores Chapa, M.D. SOAH Docket No. 503-24-12946.MD

15.  Executive Director Report.

16.  Medical Director Report.

17.  Public Information Update.

18.  Report Physician Assistant Liaison.

19.  Consideration and possible action regarding pending litigation.

20.  Reports on Automatic Orders.

21.  Consideration and approval of Orders to Show Cause.

22.  Discussion, recommendation, and possible action regarding Approval of Acudetox

Providers.

23.  Discussion, recommendation, and possible action regarding SB31 Continuing Medical

Education.

24.  Discussion, recommendation, and possible action regarding proposed rule amendments

to 22 T.A.C.

a.  Chapter 173, Office-Based Anesthesia Services, Subchapter B, concerning IV

Ketamine Therapy Standards, §§173.6-173.14.

25.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C.

a.  Chapter 161.48 Physician Graduates
b.  Chapter 161.53 Provisional License to Foreign Medical License Holders with

Offers of Employment

26.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 183. Physician Assistants.

27.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 184. Acupuncture.

28.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 186, Medical Radiologic Technology.

29.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 187, Respiratory Care.

30.  Discussion, recommendation, and possible action regarding rule review to 22 T.A.C.,

Part 9, Texas Medical Board.

Agenda Item #31 not before 9:30 a.m.

31.  Open Forum for Public Comment

32.  Discussion, recommendation, and possible action relating to personnel matters.

33.  Adjourn.

CONSENTAGENDA
Discussion/Action Items – to be considered at any time the full board is in session:

1.  Consideration and approval of the October 17, 2025, Medical Board Meeting

Minutes and action items.

2.  Committee reports and the consideration and approval of minutes and action items

of committees meeting during the board meeting.

Executive Session:
The Board may close the meeting to the public and continue in executive session for the
following reasons:
*Deliberations concerning licensure applications and the character and fitness of applicants
under the authority of The Medical Practice Act Sections 152.009 and 155.058, Occupations
Code.
*Deliberations concerning disciplinary action, investigative information, peer review
information, and possible rehabilitation orders under the authority of The Medical Practice
Act Sections 152.009, 160.006-160.008, 164.007(c), and 165.202-165.203, Occupations
Code.
*Private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the
authority of the Open Meetings Act Section 551.071, Government Code.
*Deliberations concerning personnel matters under the authority of the Open Meetings Act
Section 551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote
with regard to any matter that may be considered or discussed.  A certified agenda of any
executive session will be made.

Persons requiring special accommodations, including the use of an interpreter, due to a
disability should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

---

**[MINUTES] 2025-12-11_Minutes-Medical-2025-Dec-Executive.pdf**

Texas Medical Board

EXECUTIVE COMMITTEE
THURSDAY DECEMBER 11, 2025

The meeting was called to order on Thursday December 11, 2025, at 9:07 a.m. by Board
President Sherif Zaafran, M.D. Board members present were Michael Cokinos; Robert Martinez,
M.D.; and Manuel “Manny” Quinones, Jr., M.D. Kandace Farmer, D.O. did not attend. Staff
members present were Brint Carlton, Executive Director; Chris Palazola, J.D., Director of
Operations; and various other staff.

Agenda Item #2, Committee member report.   Dr. Zaafran gave a report on recent

changes to the DPRC and Licensure committee member and possibility of future changes.

Agenda Item #3, Adjourn. After discussion, Dr. Quinones moved, Dr. Martinez

seconded, and the motion passed to adjourn the meeting at 9:12 a.m.

---

**[MINUTES] 2025-12-11_Minutes-Medical-2025-Dec-Finance.pdf**

TEXAS MEDICAL BOARD
FINANCE COMMITTEE MEETING MINUTES
December 11, 2025

Finance Committee Chair, Mr. Michael Cokinos called the meeting to order at 9:12 a.m.
Committee members present were Mr. Michael Cokinos, Chair; Sherif Z. Zaafran, M.D.; and Ms.
Sharon Barnes. Staff members present included Mr. Brint Carlton, Executive Director, and Mr.
Joey Estrada, Deputy Executive Director/Chief Financial Officer.

Agenda Item #1, Call to order, roll call.

Agenda Item #2, Budget Report. Mr. Estrada gave an update on the agency’s budget and
projected  expenditures  and revenues  through  November  30,  2025,  for  fiscal  year  2026.  A  brief
discussion was had on the agency’s 90th Texas legislative appropriations request for the 2028-29
biennium. No concerns or issues to report.

Agenda Item #3, the meeting adjourned at 9:19 a.m.

---

**[MINUTES] 2025-12-11_Minutes-Medical-2025-Dec-DPRC.pdf**

TEXAS MEDICAL BOARD
MINUTES OF THE
DISCIPLINARY PROCESS REVIEW COMMITTEE
December 11, 2025 9:28 am
Manuel Quinones, Jr., M.D., Committee Chair, called the meeting to order at 9:28 a.m. Other
members present were Sharon Barnes, Devinder S. Bhatia, M.D., James S. Distefano, D.O.
(arrived at 9:47 am), Kelly Green, M.D.; Zach Jones, M.D. (arrived at 10:05 am), LuAnn
Morgan, Jason K. Tibbles, M.D.; Linda Troncoso, and Sherif Z. Zaafran, M.D.
Staff members present were Stephen Brint Carlton, J.D., Executive Director; Chris Palazola,
J.D., Director of Operations; and various other staff.
Agenda Item #2. Texas Physician Health Program (TXPHP).
A. Discussion, recommendation, and possible action regarding referrals.
Dr. Quinones moved and Dr. Bhatia seconded that Case No. 24-0309 MD remain under the
management of TXPHP. The motion carried.
B. Report on Emergent Referrals.
There were no emergent referrals.
C. Other Discussion Items – Program Report
Dr. Emily Doyle presented the Program Activity Report. These were information items only, and
no vote was necessary.
Agenda Item #3. Reports and discussion regarding Investigation, Litigation and Compliance
Departments.
A. Enforcement Activity Report Mr. Palazola presented the Enforcement Activity Report.
This was an informational item only, and no vote was necessary.
B. Warning Letters Report Mr. Palazola presented the Warning Letters Report. This was an
informational item only, and no vote was necessary.
C. Criminal Case Review Report Mr. Palazola presented the Criminal Case Review Report.
This was an informational item only, and no vote was necessary.
D. Report Regarding Cases Over One Year Mr. Palazola presented the Report Regarding
Cases Over One Year. This was an informational item only, and no vote was necessary.
Agenda Item #4. Consideration and approval of membership of the Expert Physician Panel.
Ms. Barnes moved and Ms. Morgan seconded to grant the approval of 7 appointments on the
Expert Panel members list. The motion carried.
Agenda Item #5. Discussion and Possible Action Regarding Review of Probationers’
Appearances. There were none.

Agenda Item #6. Discussion, recommendation and possible action regarding routine follow-
up on files previously referred from DPRC.
Dr. Bhatia moved and Ms. Barnes seconded that follow-up file 25-2872 be dismissed as
recommended. The motion carried.
Dr. Quinones moved and Dr. Bhatia, Ms. Barnes seconded that follow-up file 25-2884 be
dismissed with a warning letter. The motion carried.
Dr. Bhatia moved and Dr. Distefano seconded that follow-up files 25-7824 (25-7825) and 25-7825
(25-7824) be dismissed as recommended. The motion carried. Dr. Jones recused.
Dr. Zaafran moved and Ms. Morgan seconded that follow-up file 25-8647 be dismissed as
recommended. The motion carried. The board directed staff to review board rule 169.26 and
analyze possible amendments.
There was a break from 10:21 to 10:33 am.
Ms. Morgan moved and Ms. Barnes seconded that follow-up file 25-9358 be dismissed as
recommended. The motion carried.
Ms. Troncoso moved and Dr. Distefano seconded that follow-up file 25-9367 be dismissed with a
warning letter. The motion carried.
Dr. Green moved and Ms. Barnes seconded that follow-up file 25-9383 be dismissed as
recommended. The motion carried.
Agenda Item #7. Cases Recommended for Dismissal.
A. Non Standard of Care Cases.
25-2870, 26-0641, 26-0741, 26-0749, 26-0823, 26-0849, 26-0994, 22-2561, 25-1099, 25-7638,
25-8811, 26-0033, 24-0428, 25-0220, 26-0050, 25-2481 (25-3480), 26-0740, 26-1037, 26-1056,
26-1128, 26-1196, 26-1302, 25-7517, 25-8342, 25-0638, 25-7409, 26-1049, 26-1101, 26-1169,
26-1200, 26-1290, 26-1310, 25-5107, 25-5523, 25-5934, 25-7198, 25-0628, 26-0010, 25-0540,
B. Standard of Care Cases.
24-7742, 26-0555, 26-0599, 26-0636, 26-0710, 26-0735, 26-0773, 26-0806, 26-1165, 26-1295,
25-3222, 25-4610, 25-4987, 25-5488, 25-6084, 25-6983, 25-6985, 25-6988 (3 COMPANIONS),
25-6989 (3 COMPANIONS), 25-7656, 25-7737, 25-7797, 25-8029, 25-8094, 25-8552, 25-8706,
25-8990, 25-9181, 25-9473, 25-2520, 25-6929, 25-7068, 25-8015, 26-0012, 25-0599, 25-3253,
26-0583, 26-0631, 26-0761, 26-0832, 26-1050, 26-1175, 26-1181, 26-1297, 26-1399, 26-1403,
22-1516, 24-8931 (24-8930), 24-9129, 25-4401, 25-4766, 25-5862, 25-7006, 25-7391, 25-7683,
25-7735, 25-7772, 25-8080, 25-8104 (3 COMPANIONS), 25-8106 (3 COMPANIONS), 25-8597,
25-9071, 25-9221, 25-9593, 25-4698, 25-7293, 25-7592, 25-8019, 25-0608, 26-0015, 25-7823,
26-0633, 26-0652, 26-0779, 26-0827, 26-0975, 26-1009, 26-1051, 26-1177, 26-1363, 24-9151,
25-3115, 25-5090 (25-5091), 25-6230 (25-8048), 25-7686, 25-6947, 25-7004, 25-7147, 25-7540,

25-7593, 25-7912, 25-7922 (25-7923), 25-8120, 25-8204 (25-8205), 25-8579 (25-8580), 25-8952,
25-8989 (25-8988), 26-0059, 26-0514, 26-0539, 25-2822 (3 COMPANIONS), 25-5636, 25-7674
(25-6679; 25-7675), 25-8643, 25-9075, 25-0567, 26-0608, 26-0650, 26-0721, 26-0784, 26-0841,
26-0876, 26-0934, 26-0956, 26-0991, 25-4078, 25-4549, 25-5563, 25-6100, 25-6679 (25-7674);
25-7675), 25-6692, 25-7412, 25-7479, 25-7747, 25-7980, 25-8372(25-7268), 25-8681, 25-8748,
25-8950, 25-9301, 25-9425, 25-9493, 25-5484, 25-5622, 25-7938, 25-0625, 25-8437, 26-0626,
26-0799, 26-0830, 26-0969, 26-1004, 26-1062, 26-1246, 26-1320, 25-4676, 25-6047, 25-6160,
25-6341, 25-6611, 25-7872 (25-7873), 25-8348, 25-8536, 25-9019, 25-9409, 25-3953, 25-8708,
25-8953, 25-0587, 26-0564, 26-0584, 26-0640, 26-0656, 26-0661, 26-0731, 26-0791, 26-0854,
26-0919, 24-7702, 25-1713, 25-4209, 25-4785, 25-6340, 25-6867, 25-7033, 25-7214, 25-7873
(25-7872), 25-8105 (3 COMPANIONS), 25-8191, 25-8203, 25-8517, 25-8616, 25-8881, 25-9384,
25-9396, 25-9699, 26-0219, 25-0469 (3 COMPANIONS), 25-5094, 25-7653, 25-8594, 25-9050,
25-0596, 24-0468, 24-0620, 24-0718, 26-0625, 26-0805, 26-1000, 26-1027, 26-1137, 26-1178,
26-1267, 26-1300, 24-5603, 25-4312, 25-4455, 25-4951, 25-5358, 25-6048, 25-6810, 25-7070,
25-7684, 25-7731, 25-7816 25-7923 (25-7922), 25-8023, 25-8345, 25-9597, 25-3577, 25-3613,
25-6010, 25-7733, 25-9676, 25-0406, 25-0500, 25-0583
Dr. Quinones moved and Ms. Barnes seconded to dismiss all cases not pulled. The motion carried.
Ms. Barnes recused from case 25-1099.
Ms. Morgan moved and Dr. Quinones seconded to dismiss case 25-7517 with a custom letter to
the complainant. The motion carried.
Dr. Green moved and Dr. Quinones seconded to deny dismissal of case 26-0779 and send to
investigations for expert review by an ophthalmologist and an ENT. The motion carried.
Dr. Green moved Ms. Barnes seconded to dismiss case 26-1177 as recommended. The motion
passed.
Dr. Green moved and Ms. Morgan seconded to reconsider case 26-1051. The motion passed.
Dr. Green moved and Ms. Morgan seconded to dismiss case 26-1051 as recommended. The motion
passed.
Dr. Green moved and Dr. Jones seconded to deny dismissal of case 25-8204 and send to a second
panelist. The motion carried.
Dr. Green moved and Dr. Distefano seconded to dismiss case 26-0539 as recommended. The
motion carried.
Dr. Green moved and Ms. Morgan seconded to deny dismissal case 25-2822 and send to a second
panelist. The motion carried.
Dr. Green moved and Dr Zaafran seconded to deny dismissal for case 25-5636 and send to a second
panelist. The motion carried.

Dr. Quinones moved and Ms. Troncoso seconded to dismiss case 26-0830 as recommended. The
motion carried.
Dr. Quinones moved and Mr. Troncoso seconded to deny dismissal of case 26-1246 and send to
investigations for review. The motion carried.
Dr. Zaafran moved and Dr. Jones seconded to deny dismissal of case 25-7674 and send to an expert
panelist with specific questions. The motion carried.
Agenda Item #8. Review, discussion and possible action regarding appeals of dismissed
complaints.
A. Standard of Care
25-7574 (25-7643), 25-7084, 25-9234, 26-0810, 25-7084, 26-0712, 25-8665, 26-0713
B. Non-Standard of Care
24-2416, 25-3119, 25-4053, 25-6405 (25-6406), 25-6980, 25-7770, 25-9355, 25-9418, 25-9500,
25-9553, 25-9601, 26-0198, 25-0722, 25-3367, 25-7832, 25-8213, 25-8859, 25-9391, 25-9459,
25-9512, 25-9564, 25-9567, 24-7001, 25-3005, 25-7069, 25-5779, 25-7798, 25-8489, 25-9237,
25-9515, 26-0077, 26-0133, 26-0698, 26-0867, 25-0194, 25-1700, 25-4606, 25-5040, 25-8061,
25-8207, 25-9511, 25-9517, 25-9563, 25-9605, 26-1126, 25-0967, 25-3305, 25-5018, 25-6136,
25-8632, 25-9201, 25-9385, 25-9408, 25-9455, 25-9456, 25-9587, 25-9613, 26-0180, 26-0495,
26-0597, 26-0877, 25-2710, 25-5536, 25-8718, 25-9415, 26-0088, 25-4150, 25-5760, 25-8892,
25-8893, 25-9360, 25-9495, 26-0191, 26-0252
Ms. Morgan moved Ms. Barnes seconded and the motion passed to deny all appeals of dismissed
complaints not pulled.
Dr. Bhatia moved and Dr. Distefano seconded to grant the appeal of cases 25-3367 and 25-8207.
The motion passed.
Ms. Green moved Ms. Barnes seconded and the motion passed to deny the appeal for case 26-
0698 as recommended. The motion carried.
At 12:18 pm, Dr. Bhatia moved and Ms. Troncoso seconded to go into Executive Session for
deliberations concerning disciplinary action, investigative information, peer review
information, and rehabilitation orders under the authority of the Medical Practice Act Sections
152.009, 160.006 through 160.008, 164.007(c), and 164.202 & .203, Texas Occupations Code
and private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the authority
of the Open Meetings Act, Section 551.071, Texas Government Code.
Open session resumed at 4:49 pm, and it was announced that no action was taken during
executive session. A certified agenda of the executive session was made.
Agenda Item. #9, Review, discussion, and possible action regarding appearing appeals of
dismissed complaints.

Dr. Tibbels moved and Ms. Morgan seconded to grant the appeal of case 24-3457 (Legal 25-
0319) and issue a warning letter. The motion carried.
Dr. Distefano moved and Ms. Barnes seconded to grant the appeal of case 25-8724 and sent to
new panelist to review new information. The motion carried.
Dr. Zaafran moved and Dr. Bhatia seconded to grant the appeal of case 24-4736 (Legal 25-0051)
and send to another ISC. The motion carried.
Dr. Zaafran moved and Dr. Distefano seconded to grant the appeal of case 24-7003 (Legal 25-
0285) and send back to ISC. The motion carried.
Dr. Distefano moved and Dr. Green seconded to deny the appeal of case 24-8206. The motion
carried.
Dr. Quinones moved and Ms. Morgan seconded to deny the appeal of case 23-2397. The motion
carried.
Dr. Quinones moved and Dr. Jones seconded to deny the appeal of case 23-7508 (24-7086). The
motion carried.
Dr. Quinones moved and Dr. Bhatia seconded to deny the appeal of case 25-3121. The motion
carried.
Dr. Quinones moved and Ms. Morgan seconded to deny the appeal of case 25-6004. The motion
carried.
Dr. Quinones moved and Dr. Bhatia seconded to grant the appeal of case 25-7351 and issue a
strongly worded warning letter. The motion carried.
Agenda Item #8. Review, discussion and possible action regarding appeals of dismissed
complaints.
Ms. Morgan moved Dr. Bhatia seconded and the motion passed to deny the appeal for cases 26-
0712 and 26-0713 and send a letter to the complainant with additional information. The motion
carried.
Agenda Item. #10. Adjourn
Ms. Morgan moved and Dr. Jones seconded that the meeting adjourn.
The motion carried and the meeting adjourned at 5:04 p.m.

               Texas Medical Board
Disciplinary Process Review Committee
               TXPHP - Participant Case Review
|     |                      December 11, 2025  |     |     |
| --- | --------------------------------------- | --- | --- |

Case #      Remain with PHP     Accepted by TMB            Continue
| 1   | X   |     |     |
| --- | --- | --- | --- |

|     | Column1 | Column2 |     | Column3 |     | Column4 |     | Column5 |     |
| --- | ------- | ------- | --- | ------- | --- | ------- | --- | ------- | --- |
INVESTIGATIONS

*[document truncated for length]*

---

**[MINUTES] 2025-12-11_Minutes-Medical-2025-Dec-Licensure.pdf**

TEXAS MEDICAL BOARD

LICENSURE COMMITTEE MEETING MINUTES

December 11, 2025

The  meeting  was  called  to  order  at  9:27  a.m.  by  Roberto  D.  Martinez,  M.D.,  Chair.  Other  Committee

members  present  were  Michael  Cokinos,  Garry  D.  Crain,  George  De  Loach,  D.O.,  Luisa  del  Rosal,

Jayaram B. Naidu, M.D. and David G. Vanderweide, M.D.

Board members absent were Kandace B. Farmer, D.O. and Tomeka Herod.

Ms. Herod joined the meeting at 9:29 a.m.

Ms. del Rosal left the meeting at 10:58 a.m.

Ms. del Rosal returned to the meeting at 11:58 a.m.

Agenda Item 2a. Proposed orders offered by the Executive Director.

There are none.

Agenda Item 2b. Physician licensure applicants to be licensed.

Ms. Unterborn reported that there were 226 Physician Licensure applicants who met all the requirements to be

considered for permanent licensure by the full Board. Mr. Cokinos moved to recommend to the full Board

that all 226 Physician Licensure applicants that have been determined to meet eligibility requirements by

staff be approved. Dr. Vanderweide seconded the motion. All voted in favor and the motion passed.

Agenda Item 2c. Surgical Assistant licensure applicants to be licensed.

Ms.  Unterborn  reported  that  there  were  2  Surgical  Assistant  applicants  who  met  all  the  requirements  to  be

considered  for  licensure  by  the  full  Board.  Dr.  Naidu  moved  to  recommend  to  the  full  Board  that  the  2

Surgical  Assistant  applicants  that  have  been  determined  to  meet  eligibility  requirements  by  staff  be

approved. Ms. del Rosal seconded the motion. All voted in favor and the motion passed.

Agenda Item 2d. Acudetox applicants to be certified.

Ms. Unterborn reported that there were 15 Acudetox applicants who met all the requirements to be considered for

certification by the full Board. Mr. Cokinos moved to recommend to the full Board that the  15 Acudetox

applicants  that  have  been  determined  to  meet  eligibility  requirements  by  staff  be  approved.  Dr.

Vanderweide seconded the motion. All voted in favor and the motion passed.

Agenda Item 3. Report on Physician licensure statistics.

Non-Compact:

1

Ms.  Unterborn  reported  that  in  Quarter  1  of  FY25,  1023  new  physician  licenses  were  issued  in  an  average

processing time of 24 days. In Quarter 1 of FY26, 943 new physician licenses were issued in an average processing

time of 16 days.

Compact:

Ms. Unterborn reported that in Quarter 1 of FY25, 447 new Compact physician licenses were issued in an average

processing time of 10 days. In Quarter 1 of FY26, 705 new Compact physician licenses were issued in an average

processing time of 10 days.

Agenda Item 4a. Nonprofit Health Organizations - Applicants for Initial Certification.

Ms.  Unterborn reported  there  were  1 applicant for initial  certification  as a  Nonprofit  Health  Organization for

approval. Ms. del Rosal moved to recommend to the full Board that the 1 applicant that has been determined

by  staff  to  meet  eligibility  requirements  for  initial  certification  as  a  Nonprofit  Health  Organization  be

approved.  Mr. Cokinos seconded the motion.  All voted in favor and the motion passed.

Agenda Item 4b. Nonprofit Health Organizations - Requests for Biennial Recertification.

Ms. Unterborn reported there were 97 requests for biennial recertification as a Nonprofit Health Organization for

approval. Ms. Herod moved to recommend to the full Board that the 97 requests that have been determined

by staff to meet eligibility requirements for biennial recertification as a Nonprofit Health Organization be

approved.  Dr. Naidu seconded the motion.  All voted in favor and the motion passed.

Agenda Item  4c. Nonprofit Health Organizations  – Cancellation of organizations certified as Nonprofit

Health Organizations.

Ms. Unterborn reported there were 142 requests for cancellation as a Nonprofit Health Organization for approval.

Mr. Cokinos moved to recommend to the full Board that the 142 requests for cancellation as a Nonprofit

Health  Organization  be  approved.    Dr.  Vanderweide  seconded  the  motion.    All  voted  in  favor  and  the

motion passed.

Agenda Item 5. Report on renewal for Advertising Board Certification.

There are none.

Agenda Item 6. Licensee Requests.

There are none.

Dr. Martinez moved, and  Ms. Herod seconded, that the Committee close the meeting to the public and

continue  in  Executive  Session  for  deliberations  concerning  Agenda  Item  7.  The  motion  passed.  Dr.

Martinez announced that the meeting would be closed for deliberations at 9:38 a.m. concerning licensure

2

applicants and the character and fitness of applicants under the authority of The Medical Practice Act

Sections 152.009 and 155.058, Occupations Code, and that while in executive session, the Board would not

take any action, make any decision, or vote with regard to any matter that may be considered or discussed.

A certified agenda of any executive session will be made.

The  Executive  Session  ended  at  12:57  p.m.  The  Licensure  Committee  conducted  hearings  to  review

licensure applicants appearing concerning eligibility. The hearings were conducted in Executive Session.

Following the hearings, the Committee reconvened and considered the licensure applications.

Agenda Item 7. Applicants appearing concerning eligibility.

Applicant #2651 appeared before the Committee in executive session. In open session, Mr. Cokinos moved that

the committee recommend to the full Board that the applicant be determined ineligible for  a license due

to the applicant’s unprofessional conduct, medical malpractice history, action taken by a health care entity

and falsification of their application for a Texas license. Ms. del Rosal seconded the motion. All voted in

favor and the motion passed.

Applicant #2654 appeared before the Committee in executive session. In open session, Dr. De Loach moved

that the committee recommend to the full Board that the applicant be determined ineligible for a full license

due  to  professionalism  and  milestones  deficiencies  in  their  postgraduate  training  program  that  led  to

resignation from the program. Further, upon receipt within one calendar year of a request for a physician-

in-training permit for a training program in Texas of at least one year in length that the Executive Director

may grant a physician training permit. Dr. Vanderweide seconded the motion. All voted in favor and the

motion passed.

Applicant #2649 appeared before the Committee in executive session. In open session, Ms. Herod moved that

the committee recommend to the full Board that the applicant be determined ineligible for a license due to

unprofessional conduct including accessing inappropriate internet content and action taken by a health

care entity. Dr. De Loach seconded the motion. All voted in favor and the motion passed.

Agenda Item 8. Applicants for Advertising Board Certification.

There are none.

Agenda Item 9. Adjourn.

There being no further business, Mr. Cokinos moved to adjourn the meeting. Ms. Herod seconded the motion.

All voted in favor and the motion passed. The meeting was adjourned at 1:01 p.m.

3

COMPACT

Agenda Item 4a:  Applications for Initial Certification as a Nonprofit Health Organization

1.  STHS Kaizen

4b Applications for Recertification as a Nonprofit Health Organization

1)  Allele Healthcare, Inc.
2)  Ameripath Lubbock 5.01(a) Corporation
3)  Apollocare Partners of Texas 2
4)  Ark-La-Tex Health Network
5)  Aspire Fertility Clinic
6)  ATX Healthcare Solution Partners, Inc.
7)  Austin ARIA, Inc.
8)  BHS Physicians Network
9)  Brazos Valley Community Action Agency, Inc.
10) Capital Area Cardiology
11) Capital Area CareNow Physician Associates
12) Capital Area Multispecialty Providers
13) Capital Area Primary Care Providers
14) Capital Area Specialty Providers
15) Cardiovascular Care Providers, Inc.
16) Children’s Physician Services of South Texas
17) CHRISTUS Trinity Clinic of Texas
18) Clear Choice Laredo Hospital Physicians Group
19) Community Health Development Inc.
20) Community Medicine Associates
21) Critical Access Medical Group
22) Dallas Methodist Physicians Network
23) Dallas Physician Medical Services for Children Inc.
24) DFW 501A Corporation
25) Endeavor Health Services Board
26) Epic Orthopedics & Spine Inc.
27) Evolve Pain & Orthopedics Inc
28) Eyecare Consortium of Texas
29) FMC Medical Foundation Inc.
30) Frontera Healthcare Network
31) Grace Clinic of Lubbock
32) Granite Anesthesia d/b/a Granite Clinical Services
33) Greater Hill Country Healthcare Alliance
34) Guadalupe Family Clinic
35) Harlingen Physician Network
36) HBP Lone Star, Inc.
37) Health Hub Physicians Inc.
38) Hendrick Anesthesia Network
39) HHA Physician Associates
40) Hillcrest Family Health Center
41) Hillcrest Physicians Services
42) HNI Hospital Services of Texas Inc.
43) HNI Medical Services

44) Hood Medical Group
45) Hope Clinic
46) Houston Heart Physicians Network Inc
47) Hyperbaric Physicians of Texas
48) Lake Granbury Hospital-Based Professional Services
49) Local MD Network Inc.
50) Lone Star Circle of Care
51) Lone Star Mission Oncology Network
52) Longview Regional Hospital-Based Professional Services
53) Matagorda Episcopal Health Outreach Program
54) MCH Professional Care
55) Med Management Associates
56) Medplus Physician Group Inc.
57) Methodist CareNow Physician Associates
58) Methodist Physician Alliance
59) MMH Physicians
60) Montgomery County Clinical Services Inc.
61) MSI Health Organization of Texas Inc.
62) Mt. Enterprise Community Health Clinic
63) Multi-Specialty at Renaissance
64) Neuehealth Networks of Texas Inc.
65) NPPA Services
66) Occupational and Family Medicine South Texas
67) Pasadena Health Center
68) Path Alliance Inc.
69) People’s Community Clinic
70) Permian Cardiology Inc.
71) Peterson Medical Associates
72) PGT Medical Group Inc.
73) Primary Health Network of South Texas
74) Principle Med
75) Regional Employee Assistance Program
76) Renaissance Graduate Medical Foundation
77) RMI Clinic
78) Source 1 Medical Inc.
79) South Plains Rural Health Services, Inc.
80) South Texas Physician Alliance
81) South Texas PM&R Inc.
82) Southwest Psychiatric Services
83) Southwestern Health Resources Physicians Network
84) Stella Mattina Health Inc.
85) Synapse: Human Performance Centers Inc.
86) Texas CareNow Physician Associates
87) Texas Children’s Physician Group
88) Texas Health Foundation Inc.
89) Texas Health Physician Affiliates

90) Texas Institute of Medicine and Surgery
91) Texas Medical Management Partners Inc.
92) THN Physicians Association Inc.
93) TIOPA Inc.
94) Trinity Behavioral Rehabilitation
95) United Regional Physician Group
96) WellMed Networks Inc.
97) WellMed of Las Cruces Inc.

Agenda Item 4c: Cancellation of Organizations Certified as a Nonprofit Health Organization

24 Hour Physicians
3-C Neurosurgery, Inc.
Access Wellness Resources
Accountable Care Coalition of South East Texas, Inc.
Accuhealth, Inc.
ACO Triple Aim Providers
Advanced Metabolism Care Associates
Advantage Medical Clinic
All Care Physicians Group

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.  Altus Ace Network, Inc.
11.  Altus Physician Network
12.  Ameripath Pat 5.01(A) Corporation
13.  Ameripath San Antonio 5.01(A) Corporation
14.  Amore Medical Group
15.  Apex Clinic of Texas, Inc.
16.  Apex HPC, Inc.
17.  APN
18.  App Emergency Ed. Board, Inc.
19.  Baylor College of Medicine Radiology Associates
20.  BaylorMedCare
21.  BD Health, Inc.
22.  Brazos Valley Provider Group, Inc.
23.  Brazosport Health Alliance
24.  Brazosport Regional Physician Services
25.  Castle Hills Medical Group, Inc.
26.  Choice Care Clinic I, Inc.
27.  Choice Care II, Inc.
28.  Choice Care III Clinic, Inc.
29.  Choice Supportive Care Team, Inc.
30.  CLA Physicians Group, Inc.
31.  Cleveland Physicians Services, Inc
32.  Cleveland Specialty Group

*[document truncated for length]*

---

### 2025-10-16 — Texas Medical Board — October 16, 2025

**[AGENDA] 2025-10-16_Agenda-Medical-2025-Oct-Executive.pdf**

Texas Medical Board

 EXECUTIVE COMMITTEE
1801 CONGRESS AVE #4.300 / VIDEOCONFERENCE
AUSTIN TEXAS
THURSDAY, OCTOBER 16TH, 2025
9:00 A.M.

This meeting will be open to the public at the above location and will proceed by
videoconference, as allowed under Texas Government Code Sec. 155.127.  The location above
shall have two-way audio video communication with each of the other locations during the
meeting.  The President or Presiding Officer of the board will be physically present at the
location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

10/16/2025 Executive – https://bit.ly/101625DPRC
Or call in (audio only) +1 512-596-3865,,269765593# United States Austin

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to order and roll call.

2.  Committee member report.

3.  Adjourn.

Executive Sessions:  The Board may close the meeting to the public and continue in
executive session for the following reasons:

a.  Private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the
authority of the Open Meetings Act Section 551.071, Government Code.

b.  Deliberations concerning personnel matters under the authority of the Open Meetings Act
Section 551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote
with regard to any matter that may be considered or discussed.  A certified agenda of any
executive session will be made.

Persons requiring special accommodations, including the use of an interpreter, due to a
disability should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

Committee members:
Sherif Zaafran, MD, Chair
Kandace Farmer, DO
Michael Cokinos
Manuel “Manny” Quinones, Jr., MD
Robert Martinez, MD

10/9/2025

2

---

**[AGENDA] 2025-10-16_Agenda-Medical-2025-Oct-Finance.pdf**

Texas Medical Board

 FINANCE COMMITTEE
1801 CONGRESS AVE., #4.300 / VIDEOCONFERENCE
AUSTIN TEXAS
THURSDAY, OCTOBER 16TH, 2025
9:05 A.M.

This meeting will be open to the public at the above location and will proceed by
videoconference, as allowed under Texas Government Code Sec. 155.127.  The location above
shall have two-way audio video communication with each of the other locations during the
meeting.  The President or Presiding Officer of the board will be physically present at the
location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

10/16/2025 Finance –   https://bit.ly/101625DPRC
Or call in (audio only) +1 512-596-3865,,269765593# United States Austin

 For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to order and roll call.

2.  Budget report

3.  Adjourn.

Executive Sessions:  The Board may close the meeting to the public and continue in executive
session for the following reasons:

a.
Private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the authority
of the Open Meetings Act Section 551.071, Government Code.

Deliberations concerning personnel matters under the authority of the Open Meetings Act

b.
Section 551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote with
regard to any matter that may be considered or discussed.  A certified agenda of any executive
session will be made.

Persons requiring special accommodations, including the use of an interpreter, due to a disability
should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

Committee members:
Michael Cokinos, Chair
Sharon Barnes
Kandace Farmer, DO
Sherif Zaafran, MD

10/9/2025

2

---

**[AGENDA] 2025-10-16_Agenda-Medical-2025-Oct-DPRC.pdf**

Texas Medical Board
DISCIPLINARY PROCESS REVIEW COMMITTEE
1801 CONGRESS AVE., # 4.300/ VIDEOCONFERENCE
AUSTIN, TEXAS
THURSDAY, OCTOBER 16TH, 2025
9:15 A.M.

This meeting will be open to the public at the above location and will proceed by videoconference, as
allowed under Texas Government Code Sec. 155.127.  The location above shall have two-way audio video
communication with each of the other locations during the meeting.  The President or Presiding Officer of
the board will be physically present at the location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

10/16/2025 DPRC –  https://bit.ly/101625DPRC
Or call in (audio only) +1 512-596-3865,,269765593# United States Austin

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to Order and Roll Call.

2.  Texas Physician Health Program (TXPHP):

A.  Discussion, recommendation, and possible action regarding referrals

i.  Accept referrals
ii.  Return to TXPHP
B.  Report on Emergent Referrals
C.  Other discussion items – Program Activity Report

3.  Reports and discussion regarding the Investigation, Litigation and Compliance Departments.

A.  Enforcement Activity Report
B.  Warning Letters Report
C.  Criminal Review Report
D.  Reports Regarding Files Over One Year

4.  Consideration and approval of membership of the Expert Physician Panel.

5.  Discussion and Possible Action Regarding Review of Probationers’ Appearances.

6.  Discussion, recommendation, and possible action regarding routine follow-up on files

previously referred from DPRC.

7.  Cases Recommended for Dismissal.
A.  Non-Standard of Care Cases
B.  Standard of Care Cases

8.  Review, discussion, and possible action regarding appeals of dismissed complaints.

A.  Jurisdictional

i.  Investigations
ii.  Legal Files

B.  JNF
C.  NJ

9.  Review, discussion, and possible action regarding appearing appeals of dismissed

complaints.

A.  Jurisdictional

i.  Investigations
ii.  Legal Files

B.  JNF
C.  NJ

10. Adjourn

EXECUTIVE SESSIONS:

The Texas Medical Board may close the meeting to the public and continue in executive session
for deliberations regarding disciplinary action or private consultation and advice of counsel.

This authority is provided under The Medical Practice Act Sections 152.009, 160.006 through
.008, 164.007(c), and 164.202 & .203, Occupations Code; and Open Meetings Act Section
551.071, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote with
regard to any matter that may be considered or discussed.  A certified agenda of any executive
session will be made.
---------------------------------------------------------------------------------------------------------------------
Persons requiring special accommodations, including the use of an interpreter, due to a disability
should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.state.tx.us at least five (5) working days prior to the Board meeting.

Committee Members
Manuel Quinones, Jr., M.D., Chair
Sharon Barnes
Devinder S. Bhatia, M.D.
James S. Distefano, D.O.
Mary “Kelly” Green, M.D.
Zachary “Zach” Jones, M.D.
LuAnn Morgan
Jason K. Tibbels, M.D.
Linda Troncoso
Sherif Z. Zaafran, M.D

---

**[AGENDA] 2025-10-16_Agenda-Medical-2025-Oct-Licensure.pdf**

TEXAS MEDICAL BOARD
 LICENSURE COMMITTEE
OCTOBER 16TH, 2025
9:15 a.m.
1801 CONGRESS AVE # 9.900 / VIDEOCONFERENCE

Austin, Texas

This meeting will be open to the public at the above location and will proceed by
videoconference, as allowed under Texas Government Code Sec. 155.127.  The location above
shall have two-way audio video communication with each of the other locations during the
meeting.  The President or Presiding Officer of the board will be physically present at the
location and room listed above.

Please note that accommodation will be available for members of the public to physically attend
the meeting at the above location but will be subject to limitations set out by the Texas Facilities
Commission seating.  Members of the public are encouraged to attend the meeting by accessing
the videoconference or audio link below.

https://bit.ly/101625LICCOM
Dial in by phone
+1 512-596-3865,,544393562#

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

1.  Call to order and roll call.

2.  Discussion, recommendation and possible action regarding applicants for licensure,

permits, and certification

a.  Proposed orders offered by the Executive Director
b.  Physician licensure applicants to be licensed
c.  Surgical assistant licensure applicants to be licensed
d.  Acudetox applicants to be certified

3.  Report on physician licensure statistics

4.  Discussion, recommendation and possible action regarding cancellation of licenses by

request or for incomplete registration

a.  Surgical assistants
b.  Acudetox

5.  Discussion, recommendation and possible action regarding Nonprofit Health

Organizations

a.  Applicants for initial certification
b.  Requests for biennial recertification
c.  Cancellation of organizations certified as Nonprofit Health Organizations

6.  Report on Renewals for Advertising Board Certification

7.  Discussion, recommendation and possible action regarding licensee requests

8.  Discussion, recommendation and possible action regarding Applicants appearing

concerning eligibility*

9.  Applicants for Advertising Board Certification

10. Adjourn

*Some or all of the discussion on the agenda item may be held in Executive Session under the
authority of the Medical Practice Act and the Open Meetings Act, as noted below.   Executive
Sessions may also be conducted during discussion on other agenda items for one or more of the
reasons noted below.

 Executive Sessions:  The Texas Medical Board may close the meeting to the public and
continue in executive session for the following reasons:

a.  Deliberations concerning licensure applications and the character and fitness of

applicants under the authority of The Medical Practice Act Sections 152.009 and
155.058, Occupations Code.

b.  Deliberations concerning disciplinary action, investigative information, peer review
information, and possible rehabilitation orders under the authority of The Medical
Practice Act Sections 152.009, 160.006-160.008, and 164.007(c) Occupations Code.

c.  Private consultation and advice of counsel concerning pending or contemplated litigation,
settlement offers, and/or legal matters subject to the attorney-client privilege under the
authority of the Open Meetings Act Section 551.071, Government Code.

d.  Deliberations concerning personnel matters under the authority of the Open Meetings Act

Section 551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote
with regard to any matter that may be considered or discussed.  A certified agenda of any
executive session will be made.

Persons requiring special accommodations, including the use of an interpreter, due to a
disability should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

Committee Members:
Roberto “Robert” Martinez, MD, Chair
Michael Cokinos
George De Loach, DO
Kandace Farmer, DO
Tomeka Herod
Jayaram B. Naidu, MD
Garry D. Crain
David G. Vanderweide, M.D.
Luisa del Rosal

---

**[AGENDA] 2025-10-16_Agenda-Medical-2025-Oct-Full.pdf**

Texas Medical Board
1801 CONGRESS, AVE., # 4.300 / VIDEOCONFERENCE
AUSTIN, TEXAS
OCTOBER 16-17, 2025

This meeting will be open to the public at the above location and will proceed by videoconference, as
allowed under Texas Government Code Sec. 155.127.  The location above shall have two-way audio video
communication with each of the other locations during the meeting.  The President or Presiding Officer of
the board will be physically present at the location and room listed above.

Please note that accommodation will be available for members of the public to physically attend the
meeting at the above location but will be subject to limitations set out by the Texas Facilities Commission
seating.  Members of the public are encouraged to attend the meeting by accessing the videoconference or
audio links below.

For instructions using Microsoft Teams, please go to

https://techhelp.tmb.state.tx.us/Documentation/Teams/Publicmeeting.aspx

THURSDAY, OCTOBER 16, 2025 COMMITTEES

  9:00 a.m.

  9:05 a.m.

Executive Committee, Room 4.300
10/16/25 Executive – https://bit.ly/101625DPRC
Dial in by phone +1 512-596-3865,,269765593# United States, Austin

Finance Committee, Room 4.300
10/16/25 DPRC – https://bit.ly/101625DPRC
Dial in by phone +1 512-596-3865,,269765593# United States, Austin

  9:15 a.m.  Disciplinary Process Review Committee, Room 4.300

10/16/25 DPRC – https://bit.ly/101625DPRC
Dial in by phone +1 512-596-3865,,269765593# United States, Austin

  9:15 a.m.

Licensure Committee, Room 9.900
10/16/25 Licensure – https://bit.ly/101625LICCOM
Dial in by phone +1 512-596-3865,,544393562# United States, Austin

Texas Medical Board
1801 CONGRESS, AVE., # 4.300 / VIDEOCONFERENCE
AUSTIN, TEXAS

8:00 a.m. FRIDAY, OCT 17th, 2025, FULL BOARD MEETING

10/17/25 Full Board – https://bit.ly/101725FULL

Dial in by phone (Audio only) +1 512-596-3865,,16301109# United States, Austin

Full Board call to order, roll call, and Mission Statement.

1.
Our Mission is to protect and enhance the public’s health, safety, and welfare by establishing and maintaining
standards of excellence used in regulating the practice of medicine and ensuring quality health care for
the citizens of Texas through licensure, discipline, and education.

2.  Board Member Report.

3.  Consideration and possible action regarding dispositions below minimum guidelines.

4.  Consideration and approval of Mediated Settlement Agreed Orders.

5.  Consideration and possible action for Remedial Plans.

6.  Consideration and possible action for Agreed Orders.

7.  Consideration and approval of Modification Request/Termination Request Orders.

8.  Consideration and approval of Modification Request/Termination Request of Non-Public

Rehabilitation Orders.

9.  Consideration and approval of Cease-and-Desist Orders.

10.  Consideration and approval of Revised , Vacated, or Amended Orders.

11.  Consideration and approval of Agreed Resolution Orders.

12.  Consideration and approval of Consent Orders.

Agenda item #13 at 8:05

13.  Consideration and approval of Determination of Default.

a.  Sheridan Diaz, M.D. SOAH Docket No. 503-25-23007.MD
b.  Karthik Sampath, M.D. SOAH Docket No. 503-25-26391.MD

Agenda item #14 at 8:15

14.  Consideration and approval of Proposal for Decision.

a.  Cosmin Dobrescu, M.D. SOAH Docket No 503-24-24976.MD

b.  Mary Talley Bowden, M.D. SOAH Docket No 503-23-17769.MD

15.  Executive Director Report.

16.  Medical Director Report.

17.  Public Information Update.

18.  Report Physician Assistant Liaison.

19.  Consideration and possible action regarding pending litigation.

20.  Reports on Automatic Orders.

21.  Consideration and approval of Orders to Show Cause.

22.  Discussion, recommendation, and possible action regarding Approval of Acudetox Providers.

23.  Discussion, recommendation, and possible action regarding proposed rule amendments to 22

T.A.C.

24.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C.

25.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 183. Physician Assistants.

26.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 184. Acupuncture.

27.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 186, Medical Radiologic Technology.

28.  Discussion, recommendation, and possible action regarding adoption of proposed rule

amendments to 22 T.A.C. Chapter 187, Respiratory Care.

29.  Discussion, recommendation, and possible action regarding rule review to 22 T.A.C., Part 9,

Texas Medical Board.

Agenda Item #30 not before 8:30 a.m.
30.  Open Forum for Public Comment

31.  Discussion, recommendation, and possible action relating to personnel matters.

32.  Adjourn.

CONSENTAGENDA
Discussion/Action Items – to be considered at any time the full board is in session:

1.  Consideration and approval of the August 15, 2025, Medical Board Meeting Minutes and

action items.

2.  Committee reports and the consideration and approval of minutes and action items of

committees meeting during the board meeting.

Executive Session:
The Board may close the meeting to the public and continue in executive session for the following
reasons:
*Deliberations concerning licensure applications and the character and fitness of applicants under the
authority of The Medical Practice Act Sections 152.009 and 155.058, Occupations Code.
*Deliberations concerning disciplinary action, investigative information, peer review information, and
possible rehabilitation orders under the authority of The Medical Practice Act Sections 152.009,
160.006-160.008, 164.007(c), and 165.202-165.203, Occupations Code.
*Private consultation and advice of counsel concerning pending or contemplated litigation, settlement
offers, and/or legal matters subject to the attorney-client privilege under the authority of the Open
Meetings Act Section 551.071, Government Code.
*Deliberations concerning personnel matters under the authority of the Open Meetings Act Section
551.074, Government Code.

While in executive session, the Board will not take any action, make any decision, or vote with regard
to any matter that may be considered or discussed.  A certified agenda of any executive session will be
made.

Persons requiring special accommodations, including the use of an interpreter, due to a disability
should contact Alicia Freeman at the Board office phone 512-971-7205 or
alicia.freeman@tmb.texas.gov at least five (5) working days prior to the Board meeting.

Board Members:
Sherif Z. Zaafran, M.D., President
Kandace B. Farmer, D.O., Vice-President
Michael Cokinos, Sec/Treasurer
Sharon Barnes
Devinder S. Bhatia, M.D.
Garry Crain
George L. De Loach, D.O.
Luisa del Rosal
James S. Distefano, D.O.
Kelly Green, M.D.
Tomeka Herod
Zachary S. “Zach” Jones, M.D.
Robert D. Martinez, M.D.
LuAnn R. Morgan
Jayaram B. Naidu, M.D.
Manuel “Manny” Quinones, Jr., M.D.
Jason K. Tibbels, M.D.
Linda C. Troncoso
David G. Vanderweide, M.D.

---

### 2025-09-18 — Texas Medical Board — September 18, 2025

*(No extracted text available)*

---

### 2025-08-14 — Texas Medical Board — August 14, 2025

*(No extracted text available)*
