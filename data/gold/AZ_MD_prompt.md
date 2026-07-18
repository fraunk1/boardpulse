You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Arizona Medical Board** (AZ) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/AZ/AZ_MD#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-07-21]` — Arizona Medical Board — July 21, 2026
- `[2026-07-01]` — Arizona Medical Board — July 01, 2026
- `[2026-05-06]` — Arizona Medical Board — May 06, 2026
- `[2026-04-01]` — Arizona Medical Board — April 01, 2026
- `[2026-03-04]` — Arizona Medical Board — March 04, 2026
- `[2026-02-25]` — Arizona Medical Board — February 25, 2026
- `[2026-02-23]` — Arizona Medical Board — February 23, 2026
- `[2026-02-17]` — Arizona Medical Board — February 17, 2026
- `[2026-02-12]` — Arizona Medical Board — February 12, 2026
- `[2026-02-04]` — Arizona Medical Board — February 04, 2026
- `[2026-01-09]` — Arizona Medical Board — January 09, 2026
- `[2026-01-07]` — Arizona Medical Board — January 07, 2026
- `[2025-12-03]` — Arizona Medical Board — December 03, 2025
- `[2025-11-05]` — Arizona Medical Board — November 05, 2025
- `[2025-10-30]` — Arizona Medical Board — October 30, 2025
- `[2025-10-20]` — Arizona Medical Board — October 20, 2025
- `[2025-10-08]` — Arizona Medical Board — October 08, 2025
- `[2025-10-06]` — Arizona Medical Board — October 06, 2025
- `[2025-09-22]` — Arizona Medical Board — September 22, 2025
- `[2025-09-17]` — Arizona Medical Board — September 17, 2025
- `[2025-09-03]` — Arizona Medical Board — September 03, 2025
- `[2025-08-27]` — Arizona Medical Board — August 27, 2025
- `[2025-08-26]` — Arizona Medical Board — August 26, 2025
- `[2025-08-06]` — Arizona Medical Board — August 06, 2025
- `[2025-07-31]` — Arizona Medical Board — July 31, 2025
- `[2025-07-28]` — Arizona Medical Board — July 28, 2025
- `[2025-07-09]` — Arizona Medical Board — July 09, 2025

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: AZ_MD
state: AZ
---

# Arizona Medical Board — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Arizona Medical Board | [Minutes page](AZ_MD_MINUTES_URL) |

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

Sources-table URL: https://www.azmd.gov/BoardOps/BoardOps/board-meeting-and-minutes

## Meeting Minutes Data

Board: Arizona Medical Board
State: AZ
Code: AZ_MD

### 2026-07-21 — Arizona Medical Board — July 21, 2026

**[MINUTES] 2026-07-21_MD_202606180939_d0f929ffef2749f4a96d6dcbbbc428c1.pdf**

Wed

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

NOTICE OF ORAL PROCEEDING
Scheduled to begin at 4:30 p.m. on Tuesday, July 21, 2026
1740 W. Adams St., Phoenix, Arizona

In accordance with A.R.S. § 41-1023, the Arizona Medical Board hereby gives notice that it will hold a oral
proceeding via teleconference.

Google Meets information is provided below.

Americans  with  Disabilities  Act:  Persons  with  disabilities  may  request  reasonable  accommodations  by
contacting Michelle Butler at (480) 551-2714. Requests should be made as early as possible to allow time
to arrange the accommodation.

A.  CALL TO ORDER – 4:30 p.m.

B.  CALL FOR PUBLIC COMMENT

1.  Opportunity to provide comments and recommendations on the Board’s Notice of Proposed
Rulemaking  published  in  the  June  19,  2026  issue  of  the  Arizona  Administrative  Register.
Proposed revisions include rules contained in Article 2.

C.  ADJOURNMENT

Raquel Rivera, Executive Director

Google Meets Information

Article 2 - NPR - Public Comments meeting

Tuesday, July 21 · 4:30 – 5:30pm

Time zone: America/Phoenix

Google Meet joining info

Video call link: https://meet.google.com/nph-eusd-qjo

Or dial:

(US) +1 414
-

-792

9481

 PIN: 400 880 443#

More phone numbers: https://tel.meet/nph-eusd-qjo?pin=7042955424031

Agenda for the Thursday, July 21, 2026 Oral Proceedings
Page 2 of 2

---

### 2026-07-01 — Arizona Medical Board — July 01, 2026

**[MINUTES] 2026-07-01_MD_202606191114_185fd8bf567a41abb76b917c51590733.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

NOTICE & AGENDA FOR SPECIAL TELECONFERENCE MEETING
Scheduled to begin at 8:00 a.m. on Wednesday, July 1, 2026
1740 W. Adams St., • Phoenix, Arizona

Notice is hereby given to the general public and to the members of the Arizona Medical Board (Board), that
the Board will hold a teleconference meeting open to the public at the Board's offices located at 1740 W.
Adams St., Board Room A, Phoenix, Arizona. A.R.S. § 38-431.02. The Board will not provide a physical
location for this meeting. Board members, applicants, counsel and staff will participate either by
Google Meets or telephonic communication, according to the information appended to this agenda.
The Board, upon a majority vote of a quorum of the members, may hold an Executive Session on any of
the listed agenda items to obtain legal advice. A.R.S. § 38-431.03(A)(2) and (3). The Board may vote to go
into Executive Session to discuss and consider records exempt by law from public inspection, including the
receipt and discussion of information or testimony that is confidential by State or Federal law on agenda
items I through X pursuant to A.R.S. § 38-431.03(A)(2).

Register to Speak: Public Comments Form

The  Board  reserves  the  right  to  change  the  order  of  items  on  the  agenda,  except  for  matters  set  for  a
specific time. The formal interviews are scheduled to be heard during specific time blocks. However, the
Chairman  of  the  Board  reserves  the  right  to  call  cases  in  random  order.  Please  note  that  the
recommendations listed on the agenda are merely suggested Board actions. These recommendations do
not become final until adopted by the Board. The Board has the authority to accept, reject or modify any
recommendation listed on the agenda.

Americans  with  Disabilities  Act:  Person  with  disabilities  may  request  reasonable  accommodations  by
contacting Michelle Butler at (480) 551-2714. Requests should be made as early as possible to allow time
to arrange the accommodation.

THE BOARD WILL CONSIDER, DISCUSS AND MAY TAKE ACTION ON ANY AGENDA ITEM

Board Members
Gary R. Figge, M.D., Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P.

If you need to speak to a member of Board staff regarding agenda items,
please contact the Board Coordinator at (480) 551-2734.

Wednesday, July 1, 2026

GENERAL BUSINESS

A.  CALL TO ORDER – 8:00 a.m.

Gary R. Figge, M.D., Chair

B.  ROLL CALL

Laura Dorrell, R.N., Secretary

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA –

8:00 a.m.

This item will be limited to items on the agenda. Those wishing to address the Board need not request permission
in advance; however, the Board may limit the number of speakers to three (3) per side on any one agenda item.

D.  EXECUTIVE DIRECTOR’S REPORT

Raquel Rivera, Executive Director

•  Review, Discussion and Consideration of Request on Behalf of the University of Arizona

to Distribute a PCP Lung Screening Survey

•  Discussion of 2027 Meeting Calendar

E.  CHAIR’S REPORT

Gary R. Figge, M.D., Chair

•  Acknowledgement and Appreciation of Board Members and Staff

F.  LEGAL ADVISOR’S REPORT

Carrie Smith, Assistant Attorney General

G.  PHYSICIAN HEALTH PROGRAM (PHP) REPORT

Erinn Poteryaev, PHP Manager

H.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Gary R. Figge, M.D., Chair

I.  DISCUSSION  AND  POSSIBLE  ACTION  REGARDING  ELECTION  OF  VICE-

CHAIR
Raquel Rivera, Executive Director

J.  APPROVAL OF MINUTES

LEGAL MATTERS

K.  DISCUSSION,  CONSIDERATION  AND  POSSIBLE  ACTION  ON  THE

ADMINISTRATIVE LAW JUDGE’S RECOMMENDED DECISION.

Possible action includes, but is not limited to, adopting Findings of Fact, Conclusions of Law and
Order.

Pursuant to A.R.S. § 41- 1092.08(i), the Board may meet and confer for purposes of modifying the
recommended decision, including the Findings Of Fact, Conclusions Of Law and Recommended
Order set forth in the ALJ’s recommended decision issued in case no. 25A-37196-MDX involving
Dr. Jeffrey B. Monash and 26A-56915-MDX involving Dr. Jonathan W. Hemmert.
(Scheduled to begin at 9:00 a.m.)

The Board may only consider the official record when adjudicating a Formal Hearing Matter; therefore, the
Board cannot consider new testimony or evidence at this time.

1.  MD-20-0662A, JEFFREY B. MONASH, M.D., LIC. #37196

2.  MD-24-0788A, JONATHAN W. HEMMERT, M.D., LIC. #56915

Agenda for the July 1, 2026 AMB Teleconference Meeting
Page 2 of 7

L.  RESCIND  REFERRAL  TO  FORMAL  HEARING  AND  CONSIDERATION  OF

STAFF RECOMMENDATION
(Scheduled to begin at 9:10 a.m.)

The Board will review and may vote to take action on the following case(s).

1.  MD-21-0918A, MD-25-0743A, ASHANGA B. YATAWATTA, M.D., LIC. #56464

M.  FORMAL INTERVIEWS (Scheduled to begin at 9:15 a.m.)
The Board will review, discuss and may vote to take action on the following cases pursuant to A.R.S. § 32-1451(I).
The Board may also table for further investigation, postpone, and/or forward for administrative review.

1.  MD-25-0214B, COLLINS APPIAH, M.D., LIC. #40381

Staff: Ms. C. Garcia, Dr. O’Neal
Presenting Board Member: Dr. Beyer

N.  FORMAL INTERVIEWS (Scheduled to begin at 9:45 a.m.)
The Board will review, discuss and may vote to take action on the following cases pursuant to A.R.S. § 32-1451(I).
The Board may also table for further investigation, postpone, and/or forward for administrative review.

1.  MD-23-0503A, JUSTIN J. JORDAN, M.D., LIC. #41545

Staff: Ms. Poteryaev, Dr. Deschamps
Presenting Board Member: Dr. Farmer

O.  FORMAL INTERVIEWS (Scheduled to begin at 10:15 a.m.)
The Board will review, discuss and may vote to take action on the following cases pursuant to A.R.S. § 32-1451(I).
The Board may also table for further investigation, postpone, and/or forward for administrative review.

1.  THIS CASE HAS BEEN PULLED FROM THE AGENDA.

P.  FORMAL INTERVIEWS (Scheduled to begin at 10:45 a.m.)
The Board will review, discuss and may vote to take action on the following cases pursuant to A.R.S. § 32-1451(I).
The Board may also table for further investigation, postpone, and/or forward for administrative review.

1.  MD-22-02680A, ALBERT E. CARLOTTI, M.D., LIC. #29728

Staff: Ms. Poteryaev, Dr. Haas
Presenting Board Member: Ms. Dorrell

CONSENT AGENDA
The  Consent  Agenda  items  may  be  considered  for  approval  as  a  single  action  unless  a  Board  member  wishes  to
remove an item for discussion.

Q.  CASES RECOMMENDED FOR DISMISSAL
The Board will review and may vote to take action on the following case(s).

1.  MD-24-0588A, KYLE J. SANNIEC, M.D., LIC. #60973

Staff: Ms. C. Garcia

R.  CASES RECOMMENDED FOR ADVISORY LETTERS
The Board will review and may vote to take action on the following case(s).

1.  MD-25-0757A, BITA BADAKHSHAN, M.D., LIC. #54507

Staff: Ms. Hernandez

2.  MD-25-0452A, NEIL K. SINHA, M.D., LIC. #73009

Staff: Ms. Hernandez

3.  MD-25-0207A, TARPAN R. K. PATEL, M.D., LIC. #63204

Staff: Ms. Augugliaro, Dr. O’Neal

4.  MD-23-0570A, LOU V. IVANOVIC, M.D., LIC. #62323

Staff: Ms. Palacios, Dr. O’Neal

5.  MD-25-0201A, MICHAEL A. TREIMAN, M.D., LIC. #47566

Staff: Ms. C. Garcia, Dr. O’Neal

Agenda for the July 1, 2026 AMB Teleconference Meeting
Page 3 of 7

6.  MD-25-0535A, SAI S. RAPROLU, M.D., LIC. #R80737

Staff: Ms. Augugliaro, Dr. Haas

7.  MD-25-0397A, SEAN M. MITCHELL, M.D., LIC. #69669

Staff: Ms. Samaradellis, Dr. Haas

8.  MD-26-0064A, ATUL P. LALANI, M.D., LIC. #33131

Staff: Ms. Samaradellis

9.  MD-24-0836A, KURT E. HEILAND, M.D., LIC. #24997

Staff: Ms. Samaradellis, Dr. Haas

10.  MD-25-0807A, ATANU BISWAS, M.D., LIC. #46446

Staff: Ms. Dittlof, Dr. Sucher

11.  MD-23-1102A, NIDA K. LAURIN, M.D., LIC. #35284

Staff: Ms. Augugliaro, Dr. Sucher

12.  MD-25-0810A, RICHARD J. TEFF, M.D., LIC. #51781

Staff: Ms. Dittlof, Dr. Sucher

13.  MD-24-1081A, JOHN D. MARSHALL, M.D., LIC. #10961

Staff: Ms. Hernandez, Dr. Deschamps

14.  MD-25-0792A, RICHARD E. COOK, M.D., LIC. #74922

Staff: Ms. Hernandez

15.  MD-25-1164A, ELLIOT J. WAGNER, M.D., LIC. #40397

Staff: Ms. Dittlof, Dr. Medlen

16.  MD-25-1151A, KEVIN C. HYER, M.D., LIC. #26300

Staff: Ms. Hernandez

17.  MD-25-0736A, RUTH L. PAN, M.D., LIC. #68643

Staff: Ms. Hernandez

18.  MD-25-1202A, JEFFREY B. MONASH, M.D., LIC. #37196

Staff: Ms. Dittlof, Dr. Medlen

S.  CASES  RECOMMENDED  FOR  ADVISORY LETTERS WITH NON-DISCIPLINARY

CONTINUING MEDICAL EDUCATION ORDERS

The Board will review and may vote to take action on the following case(s).

1.  MD-25-0320A, KIMBERLY A. WEIDENBACH, M.D., LIC. #63867

Staff: Ms. C. Garcia, Dr. Haas

2.  MD-25-0869A, RON Y. MARK, M.D., LIC. #43845

Staff: Ms. Dittlof, Dr. Medlen

3.  MD-26-0096A, ADAM R. CORMAN, M.D., LIC. #54390

Staff: Ms. Dittlof, Dr. Medlen

4.  MD-25-0088A, IHTISHAM CHOUDHRY, M.D., LIC. #46421

Staff: Ms. Samaradellis, Dr. Haas

T.  REVIEW OF EXECUTIVE DIRECTOR DISMISSALS
The Board will review and may vote to take action on the following case(s).

1.  MD-23-0810A, FREDERICK T. WARNER, M.D., LIC. #31153

Staff: Ms. Samaradellis, Dr. Deschamps

2.  MD-23-0810B, BRIJESH V. REDDY, M.D., LIC. #64191

Staff: Ms. Samaradellis, Dr. Deschamps

3.  MD-23-0810C, CELINE MELITZ, M.D., LIC. #62185

Staff: Ms. Samaradellis, Dr. Deschamps

4.  MD-25-0725A, KEVIN D. HORN, M.D., LIC. #29390

Staff: Ms. Potter, Dr. Deschamps

Agenda for the July 1, 2026 AMB Teleconference Meeting
Page 4 of 7

5.  MD-25-1022A, CHIEN C. OH, M.D., LIC. #36440

Staff: Ms. Samaradellis, Dr. Haas

6.  MD-25-0870A, AYRN D. O’CONNOR, M.D., LIC. #33871

Staff: Ms. Samaradellis, Dr. O’Neal

7.  MD-25-0888A, RIMMA FINKEL, M.D., LIC. #35228

Staff: Ms. Augugliaro, Dr. Sucher

8.  MD-25-0968A, STEVEN P. PARKER, M.D., LIC. #29606

Staff: Ms. Augugliaro, Dr. Deschamps

9.  MD-25-0487A, JOHN J. COREY, M.D., LIC. #18509

Staff: Ms. Samaradellis, Dr. Deschamps

U.  PROPOSED CONSENT AGREEMENTS (Disciplinary)
The Board will review and may vote to take action on the following case(s).

1.  MD-25-1064A, DANIEL E. PARKS, M.D., LIC. #72260

Staff: Ms. Hernandez

2.  MD-25-0717A, FRANCISCO J. MELO, M.D., LIC. #33206

Staff: Ms. Dittlof

3.  THIS CASE HAS BEEN PULLED FROM THE AGENDA.

4.  MD-25-0588A, DARIO L. LIZARRAGA, M.D., LIC. #28322

Staff: Ms. Samaradellis

5.  MD-25-0853A, MORTON S. THOMAS, M.D., LIC. #4607

Staff: Ms. Poteryaev

6.  MD-26-0416A, RONALD C. MILLER, M.D., LIC. #43230

Staff: Ms. Poteryaev

7.  MD-23-1186A, ANAND P. LALAJI, M.D., LIC. #57793

Staff: Ms. Samaradellis

8.  MD-22-0538A, MD-22-1154A, MD-23-0523A, MD-23-0659A, MD-24-0539A, GEORGE M.

AVILES, M.D., LIC. #27288
Staff: Ms. Dittlof

V.  APPROVAL OF DRAFT FINDINGS OF FACT, CONCLUSIONS OF LAW AND

ORDER

1.  MD-25-0078A, KEVIN J. HOOKER, M.D., LIC. #37930

Legal Advisor: Carrie Smith, AAG

W. LICENSE APPLICATIONS
The Board will review and may vote to take action on the following applications.

i.  CONSIDERATION  AND  POSSIBLE  ACTION  TO  APPROVE  OR  DENY

LICENSE APPLICATION, OR TAKE OTHER ACTION

1.  MD-25-1098A, GRADY J. BAZZEL, M.D., LIC. #N/A

Staff: Ms. Hart

2.  MD-25-0640A, JERRY A. SPIVEY, M.D., LIC. #N/A

Staff: Ms. Hart

3.  MD-25-0932A, CHRISTOPHER S. SPENCER, M.D., LIC. #N/A

Staff: Ms. Cisneros

4.  MD-25-0924A, OSMANY DUANY, M.D., LIC. #N/A

Staff: Ms. Cisneros

5.  MD-25-0612A, ROBERT L. WEAVER, M.D., LIC. #N/A

Staff: Ms. Hart

Agenda for the July 1, 2026 AMB Teleconference Meeting
Page 5 of 7

ii.  CONSIDERATION  AND  POSSIBLE  ACTION  TO  APPROVE  OR  DENY
LICENSE  APPLICATION,  OR  TAKE  OTHER  ACTION  WITH  STAFF
RECOMMENDATION

1.  MD-25-0170A, DAVID L. GREENE, M.D., LIC. #N/A

Staff: Ms. Hart

2.  MD-25-1154A, KENNETH M. FISHER, M.D., LIC. #N/A

Staff: Ms. Cisneros

iii

*[document truncated for length]*

---

### 2026-05-06 — Arizona Medical Board — May 06, 2026

**[MINUTES] 2026-05-06_MD_202605041455_54f1813846394ff5a28a20cc42179cde.pdf**

Arizona Medical Board
1740 W Adams St, Suite 4000, Phoenix, AZ 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

NOTICE & AGENDA FOR SPECIAL TELECONFERENCE MEETING
Scheduled to begin at 5:00 p.m. on Wednesday, May 6, 2026
1740 W. Adams St., Phoenix, Arizona

Notice is hereby given to the general public and to the members of the Arizona Medical Board (Board), that
the Board will hold a special meeting open to the public at the Board's offices located at 1740 W. Adams
St., Board Room A, Phoenix, Arizona. A.R.S. § 38-431.02. The Board will not provide a physical location
for  this  meeting.  Board  members,  applicants,  counsel  and  staff  will  participate  either  by  Google
Meets  or  telephonic  communication,  according  to  the  information  appended  to  this  agenda.  The
Board, upon a majority vote of a quorum of the members, may hold an Executive Session on any of the
listed agenda items to obtain legal advice. A.R.S. § 38-431.03(A)(2) and (3). The Board may vote to go into
Executive  Session  to  discuss  and  consider  records  exempt  by  law  from  public  inspection,  including  the
receipt and discussion of information or testimony that is confidential by State or Federal law on agenda
items I through P pursuant to A.R.S. § 38-431.03(A)(2).

Register to Speak: Public Comments Form

The  Board  reserves  the  right  to  change  the  order  of  items  on  the  agenda,  except  for  matters  set  for  a
specific time. The formal interviews are scheduled to be heard during specific time blocks. However, the
Chairman  of  the  Board  reserves  the  right  to  call  cases  in  random  order.  Please  note  that  the
recommendations listed on the agenda are merely suggested Board actions. These recommendations do
not become final until adopted by the Board. The Board has the authority to accept, reject or modify any
recommendation listed on the agenda.

Americans  with  Disabilities  Act:  Persons  with  disabilities  may  request  reasonable  accommodations  by
contacting Michelle Butler at (480) 551-2714. Requests should be made as early as possible to allow time
to arrange the accommodation.

THE BOARD WILL CONSIDER, DISCUSS AND MAY TAKE ACTION ON ANY AGENDA ITEM

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P.

If you need to speak to a member of Board staff regarding agenda items,
please contact the Board Coordinator at (480) 551-2734.

GENERAL BUSINESS

A.  CALL TO ORDER – 5:00 p.m.

Gary R. Figge, M.D., Chair

B.  ROLL CALL

Laura Dorrell, R.N., Secretary

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA –

5:00 p.m.

This item will be limited to items on the agenda. Those wishing to address the Board need not request permission
in advance; however, the Board may limit the number of speakers to three (3) per side on any one agenda item.

D.  EXECUTIVE DIRECTOR’S REPORT

Raquel Rivera, Executive Director

•  Review, Discussion and Consideration of Chaperone Requirements in Other States
•  Update Regarding Board Appointments
•  Update Regarding License Portal
•  Update Regarding DOJ ADA Accessibility Mandate
•  Acknowledgement of Employee Appreciation Week
•  Update Regarding Return to In-Person meetings

E.  CHAIR’S REPORT

Gary R. Figge, M.D., Chair

•  Update on Federation of State Medical Board’s (FSMB) Annual Meeting

F.  LEGAL ADVISOR’S REPORT

Carrie Smith, Assistant Attorney General

G.  PHYSICIAN HEALTH PROGRAM (PHP) REPORT

Erinn Poteryaev, PHP Manager

H.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Gary R. Figge, M.D., Chair

I.  APPROVAL OF MINUTES

•  February 4, 2026 Teleconference
•  March 4, 2026 Special Teleconference, including Executive Session

CONSENT AGENDA
The  Consent  Agenda  items  may  be  considered  for  approval  as  a  single  action  unless  a  Board  member  wishes  to
remove an item for discussion.

J.  CASES RECOMMENDED FOR DISMISSAL
The Board will review and may vote to take action on the following case(s).

1.  MD-25-0124A, LAUREN T. BONNER, M.D., LIC. #31068

Staff: Ms. Samaradellis, Dr. Haas

2.  MD-25-0321A, BILL H. HALMI, M.D., LIC. #22591

Staff: Ms. Augugliaro, Dr. Sucher

K.  CASES RECOMMENDED FOR ADVISORY LETTERS
The Board will review and may vote to take action on the following case(s).

1.  MD-25-1213A, MARY T. JACOBSON, M.D., LIC. #61806

Staff: Ms. Hernandez

2.  MD-25-1139A, ROBERT J. TROELL, M.D., LIC. #41486

Staff: Ms. Hernandez

3.  MD-22-0623A, STANLET R. SMITH, M.D., LIC. #34173

Staff: Ms. Hart

Agenda for the Wednesday, May 6, 2026 AMB Special Teleconference Meeting
Page 2 of 6

4.  MD-24-1092A, KATHERINE A. LEITNER, M.D., LIC. #54430

Staff: Ms. Dittlof, Dr. Deschamps

5.  MD-25-0811A, TALAL ALSBIEI, M.D., LIC. #33701

Staff: Ms. Dittlof, Dr. Deschamps

6.  MD-23-0580A, BRYAN W. GAWLEY, M.D., LIC. #33914

Staff: Ms. Samaradellis

7.  MD-24-1200A, LE ROI A. BAEZ, M.D., LIC. #30154

Staff: Ms. Dittlof, Dr. Sucher

8.  MD-25-0084A, JOSHUA W. HUSTEDT, M.D., LIC. #58460

Staff: Ms. Garcia, Dr. Deschamps

9.  THIS CASE HAS BEEN PULLED FROM THE AGENDA.

10.  MD-25-0319A, SUMEET SACHDEV, M.D., LIC. #73314

Staff: Ms. Hernandez

11.  MD-25-0931A, DEREK B. KENNEDY, M.D., LIC. #70765

Staff: Ms. Cisneros

12.  MD-25-0510A, MANSOUR H. ASSAR, M.D., LIC. #23221

Staff: Ms. Dittlof, Dr. Ashby

L.  CASES  RECOMMENDED  FOR  ADVISORY LETTERS WITH NON-DISCIPLINARY

CONTINUING MEDICAL EDUCATION ORDERS

The Board will review and may vote to take action on the following case(s).

1.  MD-25-0088A, IHTISHAM CHOUDHRY, M.D., LIC. #46421

Staff: Ms. Samaradellis, Dr. Haas

2.  MD-25-0960A, ERIC S. HAZELRIGG, M.D., LIC. #20772

Staff: Ms. Dittlof, Dr. Ashby

3.  MD-23-0206A, SHEL-DON J. LEGARRETA, M.D., LIC. #25100

Staff: Ms. Hernandez, Dr. Ashby

M.  REVIEW OF EXECUTIVE DIRECTOR DISMISSALS
The Board will review and may vote to take action on the following case(s).

1.  MD-25-0208A, JONATHAN D’CUNHA, M.D., LIC. #58955

Staff: Ms. Samaradellis, Dr. Deschamps

2.  MD-25-1160A, A. MICHAEL BADRUDDOJA, M.D., LIC. #34762

Staff: Ms. Nunes, Dr. McClain

3.  MD-25-0446A, SIMON LAVOTSHKIN, M.D., LIC. #63440

Staff: Ms. Garcia, Dr. Sucher

4.  MD-25-0557A, LAKSHMAN GOLLAPALLI, M.D., LIC. #58632

Staff: Ms. Garcia, Dr. Ashby

5.  MD-25-0934A, ALLISON R. OPTICAN, M.D., LIC. #63612

Staff: Ms. Augugliaro, Dr. Deschamps

6.  MD-25-0524A, JUAN S. URIBE, M.D., LIC. #53935

Staff: Ms. Colvin, Dr. Medlen

7.  MD-25-0524B, JONATHAN J. LEE, M.D., LIC. #68386

Staff: Ms. Colvin, Dr. Medlen

8.  MD-25-0524C, JOSEPH M. ABBATEMATTEO, M.D., LIC. #75714

Staff: Ms. Colvin, Dr. Medlen

Agenda for the Wednesday, May 6, 2026 AMB Special Teleconference Meeting
Page 3 of 6

N.  PROPOSED CONSENT AGREEMENTS (Disciplinary)
The Board will review and may vote to take action on the following case(s).

1.  MD-25-0188A, NIKI L. POPP, M.D., LIC. #67064

Staff: Ms. Poteryaev

2.  MD-25-0863A, NOEL A. ZWEIG, M.D., LIC. #59778

Staff: Ms. Poteryaev

3.  MD-25-0601A, JASON J. EMER, M.D., LIC. #56784

Staff: Ms. Hernandez

4.  MD-24-1127A, PHILIP C. KACZAR, M.D., LIC. #26301

Staff: Ms. Hernandez

5.  MD-25-0033A, KHAWAJA S. H. BAIG, M.D., LIC. #72048

Staff: Ms. Hernandez

6.  MD-25-0977A, JEREMY M. ALVORD, M.D., LIC. #50936

Staff: Ms. Poteryaev

O.  LICENSE APPLICATIONS
The Board will review and may vote to take action on the following applications.

i.  REVIEW, DISCUSSION AND POSSIBLE ACTION REGARDING LICENSURE
BY  ENDORSEMENT  PURSUANT  TO  A.R.S.  §  32-1426(B)  AND  R4-16-
201(F), OR TAKE OTHER ACTION

1.  SHERIF A. A. DABASH, M.D., LIC. # N/A

Staff: Ms. Quinonez

2.  SHADY AL-HAYEK, M.D., LIC. # N/A

Staff: Ms. Callon

3.  SHALINI SINGH, M.D., LIC. # N/A

Staff: Ms. Corsi

ii.  CONSIDERATION  AND  POSSIBLE  ACTION  TO  APPROVE  OR  DENY

LICENSE APPLICATION, OR TAKE OTHER ACTION

1.  MD-25-0710A, INDERSUKHPREET S. RANDHAWA, M.D., LIC. # N/A

Staff: Ms. Hart

iii.  CONSIDERATION  AND  POSSIBLE  ACTION  TO  APPROVE  OR  DENY
LICENSE  APPLICATION,  OR  TAKE  OTHER  ACTION  WITH  STAFF
RECOMMENDATION

1.  MD-25-0250A, ABHAY GUPTA, M.D., LIC. # N/A

Staff: Ms. Hart

***END OF CONSENT AGENDA***

OTHER BUSINESS

P.  REQUEST FOR TERMINATION OF BOARD ORDER
The Board will review and may vote to take action on the following case(s).

1.  MD-23-0084A, PARVEZ M. FATTEH, M.D., LIC. #68224

Staff: Ms. DesMarais

Q.  GENERAL CALL TO THE PUBLIC
Those wishing to address the Board need not request permission in advance; however, the Board may limit those
persons  speaking  during  the  “General  Call  to  the  Public”  at  three  (3)  per  side  on  any  one  issue.  A.R.S.  §  38-
431.01(H).  The  Board  can  only  take  action  on  matters  listed  on  the  agenda  and  other  matters  related thereto.
A.R.S. § 38-431.02(H). If appropriate, actions on public comment matters that are not listed on the agenda will be
limited to directing staff to study the matter or schedule the matter for further discussion at a later date. A.R.S. §
38-4301.01(H).

Agenda for the Wednesday, May 6, 2026 AMB Special Teleconference Meeting
Page 4 of 6

R.  ADJOURNMENT

Raquel Rivera, Executive Director

Agenda for the Wednesday, May 6, 2026 AMB Special Teleconference Meeting
Page 5 of 6

GOOGLE MEETS INFORMATION

Time zone: America/Phoenix

Google Meet joining info

Video call link: https://meet.google.com/zig-mqem-kzb

Or dial:

(US) +1 385
-

-323

0042

PIN: 634 416 958#

More phone numbers: https://tel.meet/zig-mqem-kzb?pin=9404050407210

Agenda for the Wednesday, May 6, 2026 AMB Special Teleconference Meeting
Page 6 of 6

---

### 2026-04-01 — Arizona Medical Board — April 01, 2026

**[MINUTES] 2026-04-01_MD_202603271217_b2cfda14ba2040ff99f084c9178681f0.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

NOTICE & AGENDA FOR TELECONFERENCE MEETING
Scheduled to begin at 8:00 a.m. on Wednesday, April 1, 2026
1740 W. Adams St. • Phoenix, Arizona

Notice is hereby given to the general public and to the members of the Arizona Medical Board (Board), that
the Board will hold a special meeting open to the public at the Board's offices located at 1740 W. Adams
St., Board Room A, Phoenix, Arizona. A.R.S. § 38-431.02. The Board will not provide a physical location
for  this  meeting.  Board  members,  applicants,  counsel  and  staff  will  participate  either  by  Google
Meets  or  telephonic  communication,  according  to  the  information  appended  to this  agenda.  The
Board, upon a majority vote of a quorum of the members, may hold an Executive Session on any of the
listed  agenda  items  to  obtain  legal  advice.  A.R.S.  §  38-431.03(A)  (3).  The  Board  may  vote  to  go  into
Executive  Session  to  discuss  and consider  records exempt  by  law  from  public  inspection,  including  the
receipt and discussion of information or testimony that is confidential by State or Federal law on agenda
items D and I through U pursuant to A.R.S. § 38-431.03(A)(2).

To register for Public Statements please utilize the following link:
https://docs.google.com/forms/d/e/1FAIpQLSebXSrWy7ezqSvUJGjLw2tJSMrcrYRNsFpMGv9ecyzcmeox
7g/viewform?usp=header

The  Board  reserves  the  right  to  change  the  order  of  items  on  the  agenda,  except  for  matters  set  for  a
specific time. The formal interviews are scheduled to be heard during specific time blocks. However, the
Chairman  of  the  Board  reserves  the  right  to  call  cases  in  random  order.  Please  note  that  the
recommendations listed on the agenda are merely suggested Board actions. These recommendations do
not become final until adopted by the Board. The Board has the authority to accept, reject or modify any
recommendation listed on the agenda.

Americans  with  Disabilities  Act:  Persons  with  disabilities  may  request  reasonable  accommodations  by
contacting Michelle Butler at (480) 551-2714. Requests should be made as early as possible to allow time
to arrange the accommodation.

THE BOARD WILL CONSIDER, DISCUSS AND MAY TAKE ACTION ON ANY AGENDA ITEM

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P.

If you need to speak to a member of Board staff regarding agenda items,
please contact the Board Coordinator at (480) 551-2734.

Wednesday, April 1, 2026

GENERAL BUSINESS

A.  CALL TO ORDER – 8:00 a.m.

Gary R. Figge, M.D., Chair

B.  ROLL CALL

Laura Dorrell, R.N., Secretary

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA –

8:00 a.m.

This item will be limited to items on the agenda. Those wishing to address the Board need not request permission
in advance; however, the Board may limit the number of speakers to three (3) per side on any one agenda item.

D.  EXECUTIVE DIRECTOR’S REPORT

Raquel Rivera, Executive Director

•  Update on Returning to In-Person Meetings

•  Review, Discussion and Consideration of Department of Justice ADA Compliance Mandate

•  Review, Discussion and Consideration of Revised FAQs

•  Update and Discussion on New Licensing Portal

•  Update and Discussion on Pending Legislation:

o  SB 1124
o  HB 2248
o  HB 2660
o  SB 1021
•  Update on AMB Newsletter

E.  CHAIR’S REPORT

Gary R. Figge, M.D., Chair

F.  LEGAL ADVISOR’S REPORT

Carrie Smith, Assistant Attorney General

G.  PHYSICIAN HEALTH PROGRAM (PHP) REPORT

Erinn Poteryaev, PHP Manager

H.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Gary R. Figge, M.D., Chair

LEGAL MATTERS

I.  REVIEW,  DISCUSSION  AND  POSSIBLE  ACTION  REGARDING  UPDATED
REPORT OF MEDICAL REVIEW OFFICER (MRO) AS IT RELATES TO A PRIOR
ACTION TO SUMMARILY SUSPEND (Scheduled to begin at 8:30 a.m.)

1.  MD-26-0023A, PAUL A. AUPPERLE, M.D., LIC. #30485

J.  DISCUSSION, CONSIDERATION AND POSSIBLE ACTION ON SETTLEMENT

OFFER IN LIEU OF FORMAL HEARING (Scheduled to begin at 8:45 a.m.)

1.  MD-18-1183A,  MD-20-0310A,  MD-21-0358A,  MD-22-0789A,  IRFAN  MIRZA,  M.D.,  LIC.

#28306

2.  MD-25-0012A, LAURA E. HARRINGTON, M.D., LIC. #24671

Agenda for the April 1, 2026 AMB Teleconference Meeting
Page 2 of 6

K.  DISCUSSION,  CONSIDERATION  AND  POSSIBLE  ACTION  ON  THE

ADMINISTRATIVE LAW JUDGE’S RECOMMENDED DECISION.

Possible action includes, but is not limited to, adopting Findings of Fact, Conclusions of
Law and Order.

Pursuant to A.R.S. § 41- 1092.08(i), the Board may meet and confer for purposes of modifying the
recommended decision, including the Findings Of Fact, Conclusions Of Law and Recommended
Order set forth in the ALJ’s recommended decision issued in case no. 25A-65760-MDX involving
Dr. Babar A. Khera.
(Scheduled to begin at 9:00 a.m.)

The Board may only consider the official record when adjudicating a Formal Hearing Matter; therefore, the
Board cannot consider new testimony or evidence at this time.

1.  MD-23-0352A, BABAR A. KHERA, M.D., LIC. #65760

L.  FORMAL INTERVIEWS (Scheduled to begin at 9:15 a.m.)
The Board will review, discuss and may vote to take action on the following cases pursuant to A.R.S. § 32-1451(I).
The Board may also table for further investigation, postpone, and/or forward for administrative review.

1.  MD-23-0064A, ROYA KARBAKHSH, M.D., LIC. #45781

Staff: Ms. Samaradellis, Dr. Haas
Presenting Board Member: Dr. Farmer

M.  FORMAL INTERVIEWS (Scheduled to begin at 9:45 a.m.)
The Board will review, discuss and may vote to take action on the following cases pursuant to A.R.S. § 32-1451(I).
The Board may also table for further investigation, postpone, and/or forward for administrative review.

1.  MD-23-0770A, GARY A. RADA, M.D., LIC. #4731

Staff: Ms. Shepherd, Dr. Ashby
Presenting Board Member: Ms. Dorrell

N.  FORMAL INTERVIEWS (Scheduled to begin at 10:15 a.m.)
The Board will review, discuss and may vote to take action on the following cases pursuant to A.R.S. § 32-1451(I).
The Board may also table for further investigation, postpone, and/or forward for administrative review.

1.  MD-25-0567A, MICHAEL P. ALBERTI, M.D., LIC. #24716

Staff: Ms. DesMarais, Dr. Dr. Haas
Presenting Board Member: Ms. Bain

CONSENT AGENDA
The  Consent  Agenda  items  may  be  considered  for  approval  as  a  single  action  unless  a  Board  member  wishes  to
remove an item for discussion.

O.  CASES RECOMMENDED FOR DISMISSAL
The Board will review and may vote to take action on the following case(s).

1.  MD-25-0186A, BRIGG W. BARSNESS, M.D., LIC. #68785

Staff: Ms. Hernandez

P.  CASES RECOMMENDED FOR ADVISORY LETTERS
The Board will review and may vote to take action on the following case(s).

1.  MD-25-1128A, NAMAN SUROYA, M.D., LIC. #R81273

Staff: Ms. Poteryaev

2.  MD-25-0363A, STEVEN E. KONG, M.D., LIC. #53966

Staff: Ms. Dittlof, Dr. O’Neal

3.  MD-25-0801A, ODINAKA P. MOGOR, M.D., LIC. #68016

Staff: Ms. Poteryaev

4.  MD-24-0443A, MOSAB A. FREFER, M.D., LIC. #60805

Staff: Ms. Hernandez, Dr. O’Neal

Agenda for the April 1, 2026 AMB Teleconference Meeting
Page 3 of 6

5.  MD-23-1151A, ROSALIE E. BANASIAK, M.D., LIC. #15037

Staff: Ms. Hernandez, Dr. Deschamps

Q.  CASES  RECOMMENDED  FOR  ADVISORY LETTERS WITH NON-DISCIPLINARY

CONTINUING MEDICAL EDUCATION ORDERS

The Board will review and may vote to take action on the following case(s).

1.  MD-25-0214B, COLLINS APPIAH, M.D., LIC. #40381

Staff: Ms. Garcia, Dr. O’Neal

2.  MD-23-0859A, ERNESTINA P. DE OLIVARES, M.D., LIC. #31109

Staff: Ms. Hernandez, Dr. Borhan

3.  MD-25-0537A, VALERIE J. SCHOLTEN, M.D., LIC. #25181

Staff: Ms. Samaradellis, Dr. Borhan

R.  PROPOSED CONSENT AGREEMENTS (Disciplinary)
The Board will review and may vote to take action on the following case(s).

1.  MD-24-0884A, NEERAJ B. CHEPURI, M.D., LIC. #49117

Staff: Ms. Hernandez

2.  MD-23-0856A, FRANK E. CIBULKA, M.D., LIC. #22921

Staff: Ms. Hernandez

3.  MD-25-0486A, GENE H. LEE, M.D., LIC. #58285

Staff: Ms. Hernandez

4.  MD-25-0543A, MICHAEL R. GRAY, M.D., LIC. #11623

Staff: Ms. DesMarais

S.  LICENSE APPLICATIONS
The Board will review and may vote to take action on the following applications.

i.  CONSIDERATION  AND  POSSIBLE  ACTION  TO  APPROVE  OR  DENY
LICENSE  APPLICATION,  OR  TAKE  OTHER  ACTION  WITH  STAFF
RECOMMENDATION

1.  MD-25-0253A, ALAAELDIN A. BABIKER, M.D., LIC. # N/A

Staff: Ms. Hart

***END OF CONSENT AGENDA***

OTHER BUSINESS

T.  REQUEST FOR TERMINATION OF BOARD ORDER
The Board will review and may vote to take action on the following case(s).

1.  MD-23-0238A, TIMOTHY R. DOOLEY, M.D., LIC. #27528

Staff: Ms. DesMarais

2.  MD-20-0010A, JAY V. SWANSON, M.D., LIC. #27669

Staff: Ms. DesMarais

U.  REQUEST FOR MODIFICATION OF BOARD ORDER
The Board will review and may vote to take action on the following case(s).

1.  MD-21-0691A,  MD-22-0055A,  MD-22-0082A,  JOHN  W.  MCGETTIGAN,  M.D.,  LIC.

#12606
Staff: Ms. DesMarais

V.  GENERAL CALL TO THE PUBLIC
Those wishing to address the Board need not request permission in advance; however, the Board may limit those
persons  speaking  during  the  “General  Call  to  the  Public”  at  three  (3)  per  side  on  any  one  issue.  A.R.S.  §  38-
431.01(H).  The  Board  can  only  take  action  on  matters  listed  on  the  agenda  and  other  matters  related  thereto.
A.R.S. § 38-431.02(H). If appropriate, actions on public comment matters that are not listed on the agenda will be

Agenda for the April 1, 2026 AMB Teleconference Meeting
Page 4 of 6

limited to directing staff to study the matter or schedule the matter for further discussion at a later date. A.R.S. §
38-4301.01(H).

W. ADJOURNMENT

Raquel Rivera, Executive Director

Agenda for the April 1, 2026 AMB Teleconference Meeting
Page 5 of 6

GOOGLE MEETS INFORMATION

AMB Teleconference Mtg

Wednesday, April 1 · 8:00am – 5:00pm

Time zone: America/Phoenix

Google Meet joining info

Video call link: https://meet.google.com/bsh-merf-owi

Or dial:

(US) +1 484

-420-

7614

 PIN: 149 732 369#

More phone numbers: https://tel.meet/bsh-merf-owi?pin=3829692610937

Agenda for the April 1, 2026 AMB Teleconference Meeting
Page 6 of 6

---

### 2026-03-04 — Arizona Medical Board — March 04, 2026

**[MINUTES] 2026-03-04_MD_202605071354_fb4f59a637cf4457b3cff3de77ea6a06.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SPECIAL TELECONFERENCE MEETING
Held on Wednesday, March 4, 2026
1740 W. Adams St., Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P.

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 5:08 p.m.

B.  ROLL CALL

The following Board members participated virtually: Dr. Figge, Dr. Bethancourt, Ms. Dorrell, Dr.
Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps, M.D., Chief Medical Consultant; Nicole Samaradellis, Investigations Manager; and
Michelle Robles, Board Operations Manager. Carrie Smith, Assistant Attorney General (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT

•  Federation of State Medical Boards (FSMB) Request for Comment on Three Draft Reports:

o  Report  of  the  FSMB  Ethics  and  Professionalism  Committee  on  Physician

Collective Bargaining and Unionization

o  Guidance on Recent Trends in Prescribing and Dispensing
o  Report of the FSMB Workgroup on Oversight of Clinical Decision-Making

Ms. Rivera informed the Board that they can email her with any comments regarding the
drafts.

•  Review, Discussion and Consideration of Revised MA FAQs

Ms. Rivera reported that the JLRC directed her to revise the MA FAQs to clarify language
regarding  MA  administration  of    anesthetic  injections.  The  JLRC  draft  minutes  were

attached for consideration of the Committee discussion. Ms. Rivera also provided some
sample red-line wording for consideration.

Dr. Farmer noted that the dosage amount was not provided in the revision.

Ms.  Rivera  explained  that  the  dosage  was  not  included  based  on  the  Committee’s
discussion, but it can be added if the Board wishes.

Dr. Farmer explained that the intention of specifying the dosage was to clarify that MAs
should only administer small doses of anesthetics.

Ms. Smith noted that there isn’t a dosage limitation in statue, so one could not be imposed
by the Board without engaging in the rule-making process. Ms. Smith also noted that the
MA FAQs are meant to provide general clarification of procedures, not to amend rules or
policies already put in place.

Dr. Farmer opined that there should be a dosage suggestion included in the revision and
inquired what dosage amount was discussed previously.

Ms. Rivera noted the Committee previously discussed that the dosage should not exceed
3 ccs per injection, up to a maximum dose of 300 milligrams over a period of time.

Ms. Bain inquired about who qualifies as a supervisor for the injections.

Ms.  Smith  clarified  that  the  statue  allows  direct  supervision  by  a  supervising  physician,
physician assistant, or nurse practitioner.

MOTION: Dr. Bethancourt moved to approve the MA FAQs with the recommended
changes discussed in the dosing maximums.
SECOND: Dr. Gillard.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, and Dr. Gillard
The following Board Member was absent: Dr. Farmer
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

•  Update, Discussion, and Possible Action on Proposed Legislation, including but not limited

to:

o  HB 2248 – medical interventions, prohibition

Ms. Rivera informed the  Board that there  had been  multiple revisions to the  bill
since  their  last  discussion.  The  newest  amendment  proposed  a  provisional
licensure pathway. These individuals would work under indirect supervision with
direct  supervision  immediately  available.  After  four  years,  the  license  would
automatically convert to an Arizona license if requirements were met. Ms. Rivera
noted that after reviewing the bill, it would be the Board’s responsibility to adopt
rules for license and renewal fees like any other time a new license type is added.
The  Board  would  also  have  to  create  compliance  procedures  along  with
supervision,  reporting,  and  malpractice  coverage  requirements.  The  Board  will
have the ability to discipline or revoke the license. The bill also gives the licensee’s
employer  the  ability  to  require  them  to  undergo  a  competency  test.  Ms.  Rivera
opined  that  this  still  may  be  unnecessary  as  the  Board  does  have  an  existing
equivalency pathway that allows review of these individuals. The implementation
of various administrative requirements could limit the effectiveness of this model if
those
it's  creating  additional  administrative  and  compliance  burdens
supervising positions.

for

Dr. Bethancourt asked if applicants would be required to pass the ECFMG.

Final Minutes for the Wednesday, March 4, 2026 AMB Special Teleconference Meeting
Page 2 of 15

Ms. Rivera explained they only have to meet ECFMG pathway one requirements,
which does not assess English language skills.
Dr.  Bethancourt  opined  that  it  does  not  make  sense  to  grant  a  license  if  the
individual can’t pass the language competency test. Dr. Figge added it is typical
practice for licensees applying for a foreign license to obtain ECFMG certification
beforehand. However, this bill is geared towards individuals who were unable to
obtain  the  ECFMG  certification  and  will  allow  them  to  pass  some  sort  of
competency  test.  Dr.  Figge  opposed  the  bill  noting  that  this  would  create
unnecessary administrative burden.

The Board opposed this bill.

o  HB 2435 - internationally trained physicians; licensure

Ms. Rivera noted that this  bill  would prohibit certain  public health  mandates but
includes  broad  language  that  may  unintentionally  impair  the  Board’s  ability  to
protect the public in some cases. Specifically, it could restrict the ability to require
participation in the PHP and other medical necessary interventions as a condition
of licensure. Ms. Rivera provided the Board with a list of her concerns regarding
the broad language of the bill and how it would affect the investigation process and
the PHP program.

The Board opposed this bill.

E.  CHAIR’S REPORT
No report was given.

F.  LEGAL ADVISOR’S REPORT

•  Update on Atilla Mady, M.D., et al. v. Ramila De Souza Dias, et al. Maricopa County

Superior Court Case No. CV2025-032252

•  Update on Mady v. Arizona Medical Board, LC2025-000219-001

•  Update on Dworkin v. Arizona Medical Board, LC2024-000429

•  Update on Kelly v. Arizona Medical Board, U.S. District Court No. CV25-00513-PHX-KML

Ms. Smith noted that the Board has updates on the JRA cases for Dr. Mady and Dr. Kelly’s
cases. For Dr. Mady’s Superior Court case there may be a delay due to a change in the
judge.

Ms. Smith informed the Board that they would need to go into executive session for the
Dworkin update.

MOTION: Ms. Bain moved for the Board to enter into Executive Session pursuant to
A.R.S.  §  32-431.03(A)(2)  and  (3)  to  discuss  confidential  matters  and  obtain  legal
advice.
SECOND: Dr. Artz.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

The Board entered into Executive Session at 9:18 p.m.
The Board returned to Open Session at 9:36 p.m.
No legal action was taken by the Board during Executive Session.

G.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Dr.  Figge  inquired  if  the  Board  is  allowed  to  require  those  scheduled  for  a  settlement  offer
conference, to actually provide an offer. He noted that there have been multiple times where no
offer is given.

Final Minutes for the Wednesday, March 4, 2026 AMB Special Teleconference Meeting
Page 3 of 15

Ms. Smith explained that it is difficult to require a formalized offer to be made if it isn’t in statute or
rule. Without some formalized directive from the Board, negotiating a case or consent agreement
is a difficult ask.

Dr. Figge stated that this puts an undue burden on staff and Board members considering the time
is takes away when the task can’t be accomplished.

Mr. Hargraves noted that the notice letter informs individuals that the proposal has to be submitted
within a certain timeframe.

Dr. Farmer opined that this is a strategy used by attorneys as they have observed it creates Board
discussion, which provides helpful information to them. Dr. Farmer added that the Board should be
selective with how they engage in these instances in order to see a different result.

Ms. Rivera reiterated the difficulty that it presents procedurally if staff were to review every proposal.
Board staff should not be in a position where they’re coaching physicians as to what the proposal
should entail. Ms. Rivera opined that the onus should be on the attorneys and the licensees when
they request a settlement. They are notified about the need to include the proposal, and it should
come from the Board as to whether that proposal is adequate or not to even consider. If the Board
finds the settlement inadequate, they can table it or proceed to formal hearing.

Ms. Bain agreed that the responsibility of providing a settlement offer needs to be on the licensee
or their counsel, not on Board members or staff. Dr. Figge proposed that in the future, the Board
rejects  the  proposal  rather  than  guiding  them  through  the  process.  Dr.  Farmer  stated  that  the
proposal does need to specifically outline what the licensee wants and why they oppose the SIRC
recommendation.

Dr. Figge inquired about late submissions for supplemental material and noted one case on this
agenda that had material submitted late.

Ms. Rivera explained that the material was received within the appropriate timeframe for one of the
cases, however Board staff was out sick when it was received and unable to process it until the
following day. Board staff added that the Board had recently changed the deadline for supplemental
material to two business days before the Board meeting. The deadline can be adjusted if the Board
wishes.

Dr. Figge noted that this has been a discussion for some time and wanted to find a remedy that
benefits Board members and staff, as well as the physician and complainant. Ms. Bain suggested
that the deadline be moved to four or five business days before the Board meeting.

H.  DISCUSSION  REGARDING  REQUEST  FOR  CONSULTATION  FROM  THE
ARIZONA  REGULATORY  SANDBOX  ON  SANDBOX  APPLICATION
PURSUANT TO A.R.S. § 41-5604

MOTION: Dr. Farmer moved for the Board to enter into Executive Session pursuant to A.R.S.
§ 32-431.03(A)(2)(3) to discuss confidential matters and obtain legal advice.
SECOND: Dr. Gillard.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

The Board entered into Executive Session at 5:09 p.m.
The Board returned to Open Session at 5:48 p.m.
No legal action was taken by the Board during Executive Session.

I.  APPROVAL OF MINUTES

Final Minutes for the Wednesday, March 4, 2026 AMB Special Teleconference Meeting
Page 4 of 15

•  December 3, 2025 Regular Session Meeting
•
January 9, 2026 Summary Action Meeting


*[document truncated for length]*

---

### 2026-02-25 — Arizona Medical Board — February 25, 2026

**[MINUTES] 2026-02-25_MD_202604281311_1c067a9b3eaa4fce9bd0c6f1aaec8794.pdf**

Arizona Medical Board and Arizona Regulatory Board
of Physician Assistants
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

DRAFT MINUTES FOR THE BIANNUAL JOINT OFFICERS MEETING OF THE
ARIZONA MEDICAL BOARD AND ARIZONA REGULATORY BOARD OF
PHYSICIANS ASSISTANTS
Held on Wednesday, February 25, 2026
1740 W. Adams St. • Phoenix, Arizona

Arizona Medical Board Officers
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary

Arizona Regulatory Board of Physician Assistants
Officers
Susan Reina, P.A.-C, Chair
John J. Shaff, PA-C, D.F.A.A.P.A., Vice-Chair

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at 9:57 a.m.

B.  ROLL CALL

The  following  Board  members  were  present:  PA  Reina,  Dr.  Figge,  Dr.  Bethancourt  and  Ms.
Dorrell.

The following Officers were absent: PA Shaff.

ALSO PRESENT

The following Board staff were present: Raquel Rivera, Executive Director; Nicole Samaradellis,
Investigations  Manager;  and  Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,
Assistant Attorney General (“AAG”) were also present.

C.  CALL TO THE PUBLIC

No individuals addressed the Officers during Public Statements portion of the meeting.

D.  APPROVAL OF MINUTES

•  October 6, 2025 Bianual Joint Officers Meeting

MOTION:  PA  Reina  moved  to  approve  the  October  6,  2025  Joint  Officers’
Teleconference meeting.
SECOND: Dr. Bethancourt.
VOTE: The following Officers voted in favor of the motion: PA Reina, Dr. Figge, Dr.
Bethancourt and Ms. Dorrell. The following Officer was absent: PA Shaff.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

E.  DISCUSSION REGARDING NEXT JOINT OFFICERS’ MEETING

•  Discussion of Dates for Future Meeting

Ms. Rivera noted that the next meeting will be prior to the AMB August meeting.

•  Discussion of Topics for Future Meeting

Ms. Rivera informed the Officers that she will have discussion topics agendized for the
next meeting regarding general topics relating to both Boards.

F.  ADJOURNMENT

MOTION: PA Reina moved to adjourn.
SECOND: Dr. Bethancourt.
VOTE:  The  following  Officers  voted  in  favor  of  the  motion:  PA  Reina,  Dr.  Figge,  Dr.
Bethancourt and Ms. Dorrell. The following Officer was absent: PA Shaff.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

The meeting adjourned at 10:01 a.m.

Raquel Rivera, Executive Director

Draft Minutes for the February 25, 2026 Biannual Joint Officers Meeting of the AMB & ARBoPA
Page 2 of 2

---

### 2026-02-23 — Arizona Medical Board — February 23, 2026

**[MINUTES] 2026-02-23_MD_202604281313_660688f409a44c5b913a330700305b00.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

DRAFT MINUTES FOR THE MEETING OF THE EXECUTIVE DIRECTOR SELECTION
AND RETENTION COMMITTEE
Held on Monday, February 23, 2026
1740 W. Adams St., Phoenix, Arizona

Committee Members
Susan Reina, P.A.-C, Vice-Chair
Bruce A. Bethancourt, M.D., F.A.C.P.
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
John J. Shaff, PA-C, D.F.A.A.P.A

GENERAL BUSINESS

A.  CALL TO ORDER

Vice-Chair Reina called the Committee’s meeting to order at: 5:04 p.m.

B.  ROLL CALL

The following Committee members were present: PA Reina, Dr. Bethancourt, Dr. Beyer, Ms. Dorrell, Dr. Farmer,

The following Committee members were absent: Ms. Bain and Dr. Artz

ALSO PRESENT
The following Board staff participated in the meeting: Michelle Robles, Board Operations Manager. Carrie Smith,
Assistant Attorney General (“AAG”) also participated in the meeting

C.  GENERAL CALL TO THE PUBLIC

D.  APPROVAL OF MINUTES

•

•

July 9, 2025 ED Selection and Retention Committee Meeting

July 28, 2025 ED Selection and Retention Committee Meeting

MOVED: Dr. Beyer moved to approve the July 9, 2025 and July 28, 2025 ED Selection and Retention
Committee Meeting minutes.
SECOND: PA Shaff.
VOTE: The following Committee members voted in favor of the motion: PA Reina, Dr. Bethancourt,
Dr. Beyer, Ms. Dorrell, and Dr. Farmer.
The following Committee members were absent: Ms. Bain and Dr. Artz
VOTE: 5-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

E.  ELECTION OF EXECUTIVE DIRECTOR (ED) SELECTION AND RETENTION COMMITTEE

CHAIR

MOVED: Dr. Bethancourt moved to nominate Dr. Beyer as Chair.

SECOND: Dr. Gillard.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  PA  Reina,  Dr.  Bethancourt,  Dr.
Beyer, Ms. Dorrell, and Dr. Farmer.
The following Committee members were absent: Ms. Bain and Dr. Artz
VOTE: 5-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

F.  REVIEW,  DISCUSSION  AND  POSSIBLE  ACTION  REGARDING  EXECUTIVE  DIRECTOR
COMPENSATION INCLUDING PERFORMANCE INCENTIVE PAY (PIP) UNDER CURRENT
PIP STRUCTURE

Ms.  Rivera  informed  the  Committee  that  during  the  recent  PA  Sunset  Audit  the  Board  was  provided  with  a
recommendation regarding the current PIP structure. Ms. Rivera provided information for the Committee’s review
and a memo recommending that the ED no longer receives the PIP.

Dr. Bethancourt inquired about the goals.

Ms. Rivera clarified that the current goals have not been changed but noted that she will be revising all metrics for
the Committee’s review in the next couple of months.

MOVED: Dr. Bethancourt moved to cease PIP payments to the Executive Director effective immediately.
SECOND: Dr. Gillard.
PA Shaff inquired about the current PIP payments which have been in place since 2015.

Ms. Rivera confirmed that these are the same goals that have been in place but explained that this recommendation
is for the ED receiving PIP payments since it wasn’t approved when her salary was offered.

Dr. Beyer commented that a PIP incentive is appropriate but ceasing PIP payments to the ED for now is the first
step in making sure Ms. Rivera is properly compensated.

Ms. Rivera confirmed that PIP is allowed by statute but the goals that have been in place since 2015 will be updated.
This specific motion is regarding the ED receiving PIP payments at this time since it was not considered in the
discussion regarding her salary.

PA Shaff inquired if these PIP payments were given to previous Executive Directors. PA Reina commented that this
came about because Representative Bliss expressed concern regarding the difference in payment.

Ms. Rivera clarified that this was the first time the issue was brought to the Board’s attention as a result of the PA
Sunset Audit. Representative Bliss was more concerned with PIP payments being made even though investigations
were not being completed within 180 days. There was a question about the performance metrics being used to
support PIP payments.

PA Shaff agreed that the metrics can be updated but stated that current performance metrics were met, therefore
PIP should still be given. PA Shaff also opined that if stopping ED PIP payments is being based on failure to meet
performance metrics, then PIP payments should stop for everyone and not just the ED.

Ms. Rivera responded that this is solely her recommendation based on the previously mentioned factors regarding
the Executive Director’s approved salary and the Sunset Audit findings. Since there is a need to revise the PIP
performance metrics this would be a good opportunity to create specific goals for the ED. Ms. Rivera stated that
staff  are  meeting  the  necessary  performance  goals,  therefore  they  should  not  stop  receiving  PIP  payments.
Representative Bliss also brought to her attention that there wasn’t performance metrics put in place for every single
department of Board staff, so that will be a focal point in the metrics revision as well.

Dr. Gillard noted that since stepping into the Executive Director role, Ms. Rivera has also taken on lobbyist duties
and  should  be  receiving  compensation  for  such.  Therefore,  this  would  be  an  opportune  time  to  consider  when
approving the ED’s new salary after the revision of PIP metrics as well. Dr. Bethancourt agreed that metrics do
need to be changed but if the current metrics are being made the PIP should be compensated for.

Draft Minutes for the February 23, 2026 Executive Director Selection and Retention Committee Meeting
Agenda

Ms. Rivera clarified that she has been receiving PIP since she became the ED but is requesting that they cease
starting in March until the metrics are revised.

Dr. Beyer agreed with Ms. Rivera that they did not include the PIP when they previously discussed her salary. In
response to Dr. Gillard’s comment about the lobbyist duties, Dr. Beyer noted that those duties were a part of the
job description when recruiting the new Executive Director. Measurable goals should be put in place if additional
compensation is given in order to justify said payments.
MOTIN WITHDRAWN.

MOVED: Dr. Beyer moved to cease PIP payments to the Executive Director effective immediately.
SECOND: Dr. Farmer.
PA Shaff reiterated that since the PIP payments for the ED are legal, they were technically included in the pay
package approved by the committee, therefore Ms. Rivera should continue receiving said payments. Dr. Farmer
noted that this is Ms. Rivera’s request to make simpler when she brings
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  PA  Reina,  Dr.  Bethancourt,  Dr.
Beyer, Ms. Dorrell, and Dr. Farmer.
The following Committee members were absent: Ms. Bain and Dr. Artz
VOTE: 5-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

G.  REVIEW,  DISCUSSION  AND  CONSIDERATION  OF  SETTING  METRICS  AND  SCHEDULE

FOR ANNUAL ED PERFORMANCE EVALUATIONS

Ms. Rivera explained that she provided two forms for consideration and noted that since she is new to the position,
annual performance evaluations would be beneficial.

Dr. Figge commented that form 1 and 2 do the same thing but form 1 is more complicated, therefore Dr. Figge
recommended form 2.

MOVED: Dr. Figge moved to accept the second form.
SECOND: Dr. Bethancourt.
Ms. Rivera noted the form is in PDF format for this meeting but will be converted to a Google form in the future for
Committee member use.
VOTE: The following Committee members voted in favor of the motion: PA Reina, Dr. Artz, Dr. Bethancourt,
Dr. Beyer, Ms. Dorrell, and Dr. Farmer.
The following Committee members were absent: Ms. Bain.
VOTE: 6-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

H.  ADJOURNMENT

MOVED: Dr. Gillard moved to adjourn.
SECOND: Dr. Bethancourt.
VOTE: The following Committee members voted in favor of the motion: PA Reina, Dr. Artz, Dr. Bethancourt,
Dr. Beyer, Ms. Dorrell, and Dr. Farmer.
The following Committee members were absent: Ms. Bain.
VOTE: 6-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

The meeting adjourned at 5:32 p.m.

David C. Beyer, M.D., Chair

Draft Minutes for the February 23, 2026 Executive Director Selection and Retention Committee Meeting
Agenda

---

### 2026-02-17 — Arizona Medical Board — February 17, 2026

*(No extracted text available)*

---

### 2026-02-12 — Arizona Medical Board — February 12, 2026

**[MINUTES] 2026-02-12_MD_202603021518_44ecba6d28ea4a87aa495060fa7fe7d4.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

DRAFT MINUTES FOR ADMINISTRATIVE JOINT LEGISLATION AND RULES
COMMITTEE TELECONFERENCE MEETING
Held on Thursday, February 12, 2026
1740 W. Adams St., Phoenix, Arizona

Committee Members
Jodi A. Bain, M.A., J.D., LL.M., Chair
Katie S. Artz, M.D., M.S.
Bruce Bethancourt, M.D.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.

GENERAL BUSINESS

A.  CALL TO ORDER

Dr. Figge called the Committee’s meeting to order at 5:05 p.m.

B.  ROLL CALL

The following Committee members participated virtually: Dr. Bethancourt, Dr. Artz, Ms. Dorrell, Dr.
Farmer and Dr. Figge.

The following Committee member was absent: Ms. Bain.

The following Board staff participated in the virtual meeting: Raquel Rivera, Executive Director; and
Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,  Assistant  Attorney  General  (“AAG”)
was also present.

C.  GENERAL CALL TO THE PUBLIC

No individuals addressed the Committee during the Public Statements.

D.  APPROVAL OF MINUTES

•  September 22, 2025 Administrative Joint Legislation and Rules Committee

•  October 30, 2025 Administrative Joint Legislation and Rules Committee

MOTION: Dr. Bethancourt moved for adjournment.
SECOND: Dr. Artz.
VOTE: The following Committee members voted in favor of the motion: Dr. Bethancourt,
Dr. Artz, Ms. Dorrell, Dr. Farmer and Dr. Figge. The following Committee member was
absent: Ms. Bain.
VOTE: 5-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

E.  REVIEW OF AMB ALL MEETINGS CALENDAR

Ms. Rivera noted that the 2026 AMB All Meetings calendar has been provided for the Committee’s
review and reference. The Biannual Joint Officers’ Meeting will be on February 25th prior to the PA
Board Meeting and on August 5th prior to the AMB Meeting.

F.  REVIEW,  DISCUSSION  AND  POSSIBLE  RECOMMENDATION  REGARDING

FIVE YEAR REVIEW AND RULEMAKING CALENDAR
Ms. Rivera reported that she has not been able to add historical details to the rulemaking calendar;
however,  this  does  have  important  information  regarding  upcoming  deadlines  and  rulemaking
status. The next 5YRRs are not due until August 2027 for Article 4 – Medical Assistants and Article
1 – General Provisions.

G.  UPDATE ON FIVE YEAR REVIEW

1.  ARTICLE 2, LICENSURE – STATUS UPDATE REGARDING FIVE-YEAR REVIEW REPORT
Ms. Rivera reported that she submitted the 5YRR on September 26, 2025, well in advance of
the extension deadline of December 29, 2025. This was considered at GRRC’s November 25,
2025 study session then approved at their December 2, 2025 meeting.

H.  UPDATE ON RULEMAKING

1.  ARTICLE  7,  OFFICE  BASED  SURGERY  -  REVIEW,  DISCUSSION  AND  UPDATE

REGARDING RULEMAKING STATUS
Ms. Rivera reported that the Article 7 rules were considered at the GRRC council meeting on
November  4,  2025  and  approved.  The  rules  were  provided  to  the  Secretary  of  State  to  be
published in the Administrative Register to be effective within 60 days. Ms. Rivera provided the
Notice of Final Rulemaking posted  to  the  Arizona  Administrative Register on November  21,
2025. Ms. Rivera noted that the rules haven’t been updated yet and the rules editor reported
that the Code hasn’t been released yet but is being worked on.

2.  ARTICLE 2, LICENSURE -REVIEW, DISCUSSION AND CONSIDERATION OF PURSUING

RULEMAKING
Ms. Rivera reported that she obtained authorization to proceed with rulemaking on November
15, 2025. Ms. Rivera provided the Draft Article 2 Notice of Proposed Rulemaking changes as
described in the Article 2 5YRR. If approved by the committee, she will file the agency certificate
of notice of proposed rulemaking then hold a public comment meeting in March or April. The
comments related to the rule changes will come back to the committee for us to address before
we move to the next step of the rulemaking process.

I.  REVIEW, DISCUSSION AND CONSIDERATION OF MA SCOPE OF PRACTICE

INQUIRIES AND WHETHER TO PURSUE RULEMAKING
Dr. Joe Giancola, Dr. Michael Huether and Dr. Josh Tournas participated virtually.

Ms.  Rivera  reported  that  in  prior  meetings,  the  Committee  received  information  and  requests
related to scope  of practice for MAs and specifically, whether MAs are  authorized to administer
anesthetic injections. There was discussion about the potential need for rulemaking to address this
issue. At the last meeting, the Committee directed the AAG to review the questions posed by Dr.
Tournas regarding the lack of prohibition of MAs administering anesthetic injections in statute and
whether  rulemaking  was  required  or  if  the  MA  FAQs  could  be  amended  to  include  some  draft
language for the JLRC and stakeholder input. Ms. Rivera informed the Committee of other states
that she identified and provided sample wording for consideration.

Ms. Rivera read the sample language on the FAQ for the record. Ms. Rivera noted that the citation
may require some finesse by the Committee or stakeholders, but it does capture the discussion
and input from the last Committee meeting.

Dr. Huether stated that the parameters are agreeable and the language is appropriate. Dr. Giancola
agreed that the language is consistent with what was discussed with his anesthesia colleagues.
Dr. Tournas also agreed and appreciated the background research.

Dr. Farmer inquired if clarification need to be made that this is limited to adults only.

Dr. Huether agreed that it would be adults only.

Draft Minutes for the February 12, 2026 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 2 of 5

Dr. Artz inquired if the cut off age for “adults” is 18 or 13. Dr. Farmer stated that a weight and age
cut off can be set.

Dr.  Huether  noted  that  he  remembers  discussing  adults,  aged  18  up,  but  agreed  that  there  are
some adolescents who are higher in weight who can tolerate the dose.

Dr. Farmer opined that it is more of a weight issue and since we are making changes now should
include it.

Dr. Giancola noted that they discussed adults but for our general dermatology colleagues may use
it on adolescents.

Dr. Bethancourt commented that just doing a biopsy will not require that amount of dosage. Dr.
Farmer agreed that if it is a rare thing we can just identify an adult as age of 18 and with the rare
patients the physician can inject it themselves.

Ms. Smith clarified that this is a practice recommendation and should be phrased as such and not
a prohibition, and there is not rule or statute language that would support a prohibition. Ms. Smith
explained  that  this  is  not  a  rule  but  something  that  would  be  added  to  the  FAQs  as  a  general
recommendation.

Ms. Rivera noted that if the Board approves the language at the March meeting staff can update
the FAQs immediately on the Board’s website.

Dr. Huether inquired about whether the language is also mentioned in the third FAQ as well.

Dr. Farmer noted that this discussion is available to the public and the Committee has come to a
carefully thought out recommendation that the anesthesiologists and dermatologists have agreed
on.

Ms. Smith recommended that the Committee should revise the whole document to be consistent.

Ms. Rivera stated that she and Ms. Smith can draft suggested language when taking this to the full
Board.

MOTION: Dr. Farmer moved to approve the discussed modifications to the FAQs to the full
Board for consideration.
SECOND: Dr. Bethancourt.
VOTE: The following Committee members voted in favor of the motion: Dr. Bethancourt, Dr.
Artz, Ms. Dorrell, Dr. Farmer and Dr. Figge. The following Committee member was absent:
Ms. Bain.
VOTE: 5-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

J.  UPDATE  REGARDING  NEED  FOR  LEGISLATION  AND  DISCUSSION  ON

PENDING LEGISLATION
Ms. Rivera reported that the JLRC directed her to seek legislation this session to give the Board
the authority to perform Committee level formal interviews and take any of the actions the full Board
may  take  after  conducting  a  formal  interview.    At  this  current  time,  we  are  unable  to  conduct
Committee  level  formal  interviews  due  to  quorum  limitations.  Ms.  Rivera  reported  that  she  has
entered the Board’s positions on legislation as directed at last week’s Board meeting and continues
to be present at hearings to discuss the Board’s concerns and make herself available to legislative
staff to address their inquiries related to pending legislation. Ms. Rivera provided update on HB2687
and informed the Committee that the bill was not placed on the last committee agenda and will not
be moving forward. Ms. Rivera provided an update on HB2435, nothing that an amendment was
filed  on  February  6.  The  amendment  creates  a  provisional  licensure  pathway  that  would  allow
certain internationally trained physicians to obtain a provisional license, practice under supervision

Draft Minutes for the February 12, 2026 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 3 of 5

in counties with populations under one million and automatically convert to full licensure after four
years if specified conditions are met. Ms. Rivera noted that this framework may be unnecessary
because  the  existing  equivalency  pathway  already  allows  qualified  international  physicians  to
obtain full licensure following a thorough, individualized review. This would establish an automatic
conversion mechanism tied primarily to time in practice rather than the level of front-end evaluation
currently  applied  to  these  applicants.  Additionally,  the  amendments  allow  provisional  licensure
without  requiring  certification  processes  that  assess  English  language  and  communication
competency. Ms. Rivera expressed concern about the practical implementation of the supervision
requirements.  Rural  and  underserved  areas  already  experience  physician  workforce  shortages,
and  it  may  be  difficult  to  identify  supervising  physicians  who  are  both  available  and  willing  to
assume  supervisory  responsibility,  particularly  when  supervision  must  occur  within  the  same
specialty.  In  addition,  the  amendments  do  not  clearly  define  the  level,  frequency,  or  scope  of
required  supervision,  which  may  create  variability  in  oversight  and  uncertainty  for  supervising
physicians,  employers,  and  licensees.  These  implementation  challenges  could  limit  the
effectiveness  of  the  provisional  licensure  model  while  creating  additional  administrative  and
compliance burdens.

Dr. Figge agreed with the expressed concerns and noted that provisional licensees may not get
any additional education but will get a full license. Dr. Bethancourt agreed and noted that physicians
in  rural  communities  have  expressed  that  they  don’t  have  time  for  it  and  asked  how  these
individuals would get paid if they couldn’t bill insurance. Dr. Figge noted that most of these rural
physicians don’t have hospital privileges and their patients have Medicare, Medicaid and Tricare.
Otherwise, the person can’t see those patients.

Ms. Rivera noted that when this went to the hearing last week, Dr. Heap was concerned about the
lack of ECFMG certification. After she spoke, someone asked why is no one using this licensure
pathway if it was a reasonable option. Ms. Rivera confirmed that she will keep following this bill and
bring an update in March.

K.  REVIEW,  DISCUSSION  AND  UPDATE  REGARDING  FY27  FUNDING

REQUEST
Ms.  Rivera  reported  that  the  two  FY27  funding  requests  were  reviewed  by  OSPB  and  they
approved our request for $150,000 to modernize the MD and PA websites. Ms. Rivera reported
that  she  anticipated  starting  this  project  at  the  end  of  the  summer  in  alignment  with  FY27.  T

*[document truncated for length]*

---

### 2026-02-04 — Arizona Medical Board — February 04, 2026

**[MINUTES] 2026-02-04_MD_202605071353_7a0b48256ec545649fd4d12c3eecbb60.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR TELECONFERENCE MEETING
Held on Wednesday, February 4, 2026
1740 W. Adams St. • Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P.

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 8:04 a.m.

B.  ROLL CALL

The following Board members participated virtually: Dr. Figge, Dr. Bethancourt, Ms. Dorrell, Dr.
Artz, Dr. Beyer, Dr. Farmer and Dr. Gillard.

The following Board member was absent: Ms. Bain.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps, M.D., Chief Medical Consultant; Nicole Samaradellis, Investigations Manager; and
Michelle Robles, Board Operations Manager. Carrie Smith, Assistant Attorney General (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT

•  Review and Discussion of Google Meets Helpful Tips Pamphlets

Ms. Rivera noted that in light of the feedback from Board Members during our meeting in
January with Google Meets, and feedback from attendees, we have prepared and revised
our Tips sheet for Board members and the public outlining how to join the meeting; how to
register for call to public; instructions on how to join the meeting as a guest or using their
own google account; and steps to rename yourself on various devices. Ms. Rivera further
noted that staff will use this to notice our March meeting. Ms. Rivera informed the Board
that she and other EDs were informed of another board’s Zoom meeting being hacked so
we are pleased that we made the decision to transition; however, I believe this is a risk for
all teleconference meetings and we will continue to work with ADOA and Google to see if
there  is  any  ability  to  provide  Board  staff  with  more  control  parameters  during

teleconference meetings to reduce the possibility of open meeting law violations, patient
confidentiality concerns, and technological malfeasance.

Dr. Beyer approved the form and agreed that it should be used.

•  Upcoming scheduling of ED Selection and Retention Committee

Ms. Rivera requested that the ED Selection and Retention Committee be convened this
month  to  address  the  recommendations  related  to  PIP  and  the  ED  salary.  After  the
meeting, staff will send a calendar doodle to select a date in February to hold this meeting.

•  Update Regarding the ARBoPA Sunset Audit Presentation

Ms.  Rivera  reported  that  the  PA  Board  was  continued  for  two  years  and  despite  the
reported progress with implementation of the auditor’s recommendations, the Committee
of Reference remained concerned about the Board’s Performance Incentive Pay and PIP
payments made to the Executive Director. Ms. Rivera reported that she started to work on
responding  to  the  auditor’s  6  month  follow-up  requests  plans  address  the  PIP
recommendations by March when the follow-up audit is scheduled.

•  Reminder of Conflict of Interest (COI) Form

Ms. Rivera reminded the Board that Ms. Smith provided the Board with COI training at the
January teleconference and staff sent an  email with the annual training and COI Forms
required for Board member and staff. Ms. Rivera requested that all COI forms returned by
2/6/26.

•  Update on 1740 Remediation

Ms. Rivera informed the Board that limited staff who temporarily were working out of the
States  Connected  Workspace  at  1400  Washington  returned  to  the  office  this  week.
Remediation is complete pending vinyl flooring in the breakroom and storage rooms, which
is planned for this week after hours. We are coordinating with IT staff for a return plan and
timeline per department as we test the functionality of the outlets and devices that were
moved due to carpeting. Next week, she will be reviewing our Damaged Asset list to finalize
our  entries  and  ensure  there  weren’t  any  missed  items  to  submit  claims  for  damaged
laptops.

•  Update Regarding Board Appointments

Ms. Rivera informed the Board that she met with Boards and Commissions yesterday and
reviewed some potential applicants for consideration to add to a list to provide to Senator
Werner. We also discussed the status of reappointments and concern with not obtaining
senate confirmations for reappointments, resulting in those members having to leave the
Board  after  12  months  if  not  approved.  Ms.  Rivera  noted  that  there  is  a  lot  of  interest;
however, those individuals are located in Maricopa or Pima counties, where we already
have  representation  on  the  Board.  With  regard  to  public  interest,  a  few  pharmacists
applied, but they were also located in Maricopa or Pima counties.

•  Update, Discussion, and Possible Action on Proposed Legislation, including but not limited

to:
Ms. Rivera provided the Board with some bills that may impact the Board and requested
their positions on these bills so that she can prepare for upcoming  hearings collaborate
with different stakeholders based on any concerns.

o  HB 2435 - internationally trained physicians; licensure

Ms. Rivera stated that for internationally trained physicians the Board currently has
the ability to review the information to determine if it's equivalent training or not.
The  proposed  language  would  also  provide  an  alternative  pathway  for  foreign
medical graduates who hold valid licenses and immigration status to allow them to
work in an underserved area if they satisfy the ECFMG pathway one requirements.
Ms.  Rivera  informed  the  Board  that  she  met  with  Representative  Bliss  and  a
lobbyist  in  December  to  discuss  some  of  the  concerns.  They  noted  that  the  bill
Final Minutes for the February 4, 2026 AMB Regular Session Meeting
Page 2 of 27

aims to address the healthcare provider shortage in less populated areas and also
retain spots for newly trained physicians.

Dr. Beyer commented that the Board already has an efficient process to allow the
Board to license these physicians. Creating another pathway when the Board is
already efficient is not a good use of staff time. Dr. Gillard commented that he does
not want to see less qualified individuals brought into underserved communities.
Dr.  Figge  commented  that  this  isn’t  just  an  issue  in  Arizona  and  noted  that  just
because the bill is presented does not mean it will go into law. Dr. Farmer inquired
about what the status is on how we work with stakeholders.

Ms. Rivera requested the Board's position before she moves forward with ARMA
or other associations

Dr. Farmer suggested asking ARMA's lobbyists since it is unclear whether these
have  a  serious  consensus  to  move  them  forward.  Dr.  Artz  commented  that  the
Board  should  figure  out  whether  it  is  equivalent  training  and  determine  whether
individuals would safe to treat Arizona’s patients. Dr. Artz opined that Ms. Rivera
should emphasize that we already have an efficient process.

Ms.  Smith  explained  that  as  the  Board's  representative,  Ms.  Rivera  needs
authorization from the Board to take any particular position on any particular bill.
The Board could direct Ms. Rivera to support, opposed or be neutral on the bill,
but express concerns on behalf of the board. For each of these bills, the Board
needs to take a vote in order to approve whatever position she's taking. Ms. Smith
noted that on this particular bill, it appears it's on the House Health and Human
Services Committee agenda for February 9th.

Dr.  Figge  expressed  concern  that  about  the  language  would  not  necessarily
require ECFMG certification.

Ms. Rivera opined that that this legislation was created for individuals who aren't
going  to  go  through  an  ACGMA  platform,  and  may  not  qualify  for  ECFMG  .
Applicants  would  only  be  required  to  meet  the  pathway  one  requirements.  She
acknowledged the Board’s concerns regarding the lack of ECFMG requirement.

Dr. Bethancourt commented on how physicians will be reimbursed.

Ms. Rivera noted that she brought this concern up as well and noted language at
the end of the bill regarding health care employers. She noted that it would likely
be difficult for these individuals  to find employment, There was similar legislation
adopted in Tennessee. Ms. Rivera noted that she reached out to the FSMB who
reported that Tennessee  had only issued one license because doctors really can't
use it once they come here.

MOTION: Dr. Farmer moved to oppose the bill in its current form.
SECOND: Dr. Gillard.
VOTE: The following Board members voted in favor of the motion: Dr. Figge,
Dr. Bethancourt, Ms. Dorrell, Dr. Artz, Dr. Beyer, Dr. Farmer and Dr. Gillard.
The following Board Member was absent: Ms. Bain.
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

o  HB 2660 - health boards; licensure decisions; investigation

Ms. Rivera reported that this bill states that unless a health professional has been
criminally charged, this bill lets them keep working while they appeal a licensing
decision and places strict deadlines and oversight on boards that attempt to restrict
licenses. Ms. Rivera expressed some concerns with this bill as it would impact our

Final Minutes for the February 4, 2026 AMB Regular Session Meeting
Page 3 of 27

investigation process. If the criminal charges relate to the practice of medicine, the
Board has typically offered an ICA for PR while the criminal matter is pending, and
we await the outcome of the charges. The standard of evidence to support criminal
charges is significantly higher than clear and convincing or preponderance, which
are used in Board matters. Tying immediate action to whether someone has been
criminally charged disregards how healthcare works as some reasons for practice
restrictions may not involve crimes such as incompetence, dangerous prescribing,
boundary issues, substance use etc. Ms. Rivera opined that this would weaken the
Board’s authority to act quickly then places an unrealistic administrative burden on
staff to allow the licensee to appeal within 30 days.

MOTION: Dr. Gillard moved to oppose this bill at the legislature.
SECOND: Dr. Farmer.
Dr. Beyer noted that the vast majority of the Board’s summary action cases rarely
have a criminal conviction and this would tie the Board’s hands in an unintentional
way.
VOTE: The following Board members voted in favor of the motion: Dr. Figge,
Dr. Bethancourt, Ms. Dorrell, Dr. Artz, Dr. Beyer, Dr. Farmer and Dr. Gillard.
The following Board Member was absent: Ms. Bain.
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

o  SB 1124 - health boards; evaluations; notice

Ms. Rivera noted that before a board can require a psychological, psychiatric, or
physical evaluation, it must give 14 days notice, allow the professional to respond
and be heard, share the results, and reimburse the cost if no action is taken. Ms.
Rivera noted that she did speak at the Health and Human Services Committee on
January 21st with concerns she provided that statement for the Board’s review.

Dr. Figge noted that this would also tie the Board’s hands and would financially
penalize the Board. Dr. Gillard commented that it's already difficult for an applicant
to  submit  an  application.  Dr.  Beyer  commented  that  the  14-day  notice  isn’t  a
problem but inquired about what is meant by if the Board acts on the report and
dismiss  the  complaint  bas

*[document truncated for length]*

---

### 2026-01-09 — Arizona Medical Board — January 09, 2026

**[MINUTES] 2026-01-09_MD_202603051044_ab9e335021ee472189dc4ab8faf4bf73.pdf**

ARIZONA MEDICAL BOARD
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SUMMARY ACTION TELECONFERENCE MEETING
Held on January 9, 2026
1740 W. Adams St. • Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 5:07 p.m.

B.  ROLL CALL

The following Board members participated virtually: Dr. Figge, Dr. Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr.
Beyer, Dr. Farmer and Dr. Gillard.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude Deschamps, M.D.,
Chief Medical Consultant; Nicole Samaradellis, Investigations Manager; and Michelle Robles, Board Operations
Manager. Carrie Smith, Assistant Attorney General (“AAG”) also participated in the meeting.

C.  CALL TO THE PUBLIC

No individuals addressed the Board during the Public Statements portion of the meeting.

LEGAL MATTERS

D.  REVIEW, DISCUSSION AND POSSIBLE ACTION REGARDING SUMMARY ACTION

1.  MD-26-0023A, PAUL A. AUPPERLE, M.D., LIC. #30485

Dr. Aupperle participated virtually.

Board staff summarized that Dr. Aupperle’s violated his Board Order, a Decree of Censure with Probation
including PHP Monitoring. Based on the terms of his Decree of Censure, if he uses drugs in violation of his
probation, his license shall be summarily suspended pending a hearing for revocation or in the alternative
he may surrender his license if he agrees in writing to being impaired by drug abuse. Of note, Dr. Aupperle’s
Decree  of  Censure  was  effective  on  June  20,  2023.  On  July  13,  2023,  Dr.  Aupperle  tested  positive  for
methamphetamine  on  a  hair  test,  but  this  information  was  not  reported  to  the  Board  by  the  Monitor.
Additionally, on August 7, 2024, Dr. Aupperle tested positive for methamphetamine on another hair test and
again this was not reported to the Board. These two tests were discovered once Dr. Aupperle requested
early termination of his probation and PHP Monitoring on August 15, 2025 and records were reviewed from
his PHP Monitor to facilitate a PHP Assessment prior to consideration of his request. The independent PHP
Assessor did not support early termination for Dr. Aupperle and Dr. Aupperle withdrew his request.  On

the  methamphetamine  noting

December 11, 2025, Dr. Aupperle tested positive for methamphetamine again and this time, the Board was
advised and the test was confirmed positive. Dr. Aupperle’s PHP Monitor confirmed with a toxicologist that
environmental  exposure  is  unlikely  and  not  expected  with  Dr.  Aupperle’s  prescribed  medications.  The
toxicologist suggested that given the frequency of the urine tests, the urines may be negative because they
missed
that  both  Dr.  Aupperle’s  prescribed  medications  and
methamphetamine metabolize to amphetamine. Dr. Aupperle has a significant Board history. In 2009, he
completed one PHP Agreement, a Letter of Reprimand with Probation which was related to a DUI charge
involving  methamphetamine.  In  2019,  Dr.  Aupperle’s  employer  found  him  impaired  at  work,  with
methamphetamine and other drugs. Police were called and this resulted in Dr. Aupperle being charged with
felony  counts  for  possession  of  dangerous  drugs  and  drug  paraphernalia.  He  later  pleaded  guilty  to  a
reduced charge of drug paraphernalia, a class 6 undesignated felony. Dr. Aupperle entered into an Inactive
with  Cause  Order  for  this  case.  Subsequently,  Dr.  Aupperle  completed  treatment  and  then  requested
reactivation of his license. The Decree of Censure we are discussing today was the agreement entered into
by the Board to reactivate his license. Given Dr. Aupperle’s extensive history, Board staff finds sufficient
evidence of Dr. Aupperle’s positive hair test supporting a violation of his Board Order and requests that you
summarily suspend Dr. Aupperle’s license.

Dr. Aupperle stated that he was not notified about the positive hair test until earlier this month and that he
was never informed about the July 13th and the August test. Dr. Aupperle denied using methamphetamine
any of those times. Dr. Aupperle noted that he took two polygraph tests and they were both negative. Dr.
Aupperle  further  noted  that  a  positive  methamphetamine  result  could  be  secondary  to  environmental
exposure or ingestion. Dr. Aupperle explained that it has to be above a certain threshold to get a positive
test, and his ADHD prescriptions do not apply. In conclusion, Dr. Aupperle stated that he did not understand
why the tests are positive unless there had been environmental exposure and that he would be willing to
take another polygraph test and increase his urine drug screens.

Dr.  Gillard  inquired  about  a  past  allegation  of  purchasing  Adderall  on  the  street  that  turned  out  to
methamphetamine and if this was alleged or ever proven.

Board  staff  informed  the  Board  that  in  the  most  recent  PHP  assessment  report,  the  PHP  assessor
documented  a  conversation  with  the  psychiatrist  who  made  that  comment  that  there  had  been  some
purchasing of street Adderall.

Dr. Aupperle clarified that in 2004,
 he went to buy cocaine and bought methamphetamine. He has never bought Adderall on the street.

Dr. Beyer inquired whether there have there been any negative hair tests since the reactivation and whether
any of the medications the physician is taking are known to provide a false positive.

Board staff explained that the toxicologist was aware of the medications prescribed to Dr. Aupperle and he
said  definitively  that  they  do  not  metabolize  to  methamphetamine,  but  that  methamphetamine  will
metabolize to amphetamine.

Dr. Gillard noted that if  the Board votes for summary suspension at this meeting, the case will move forward
to a formal hearing and the physician will have a chance to bring in experts for toxicology to go over the
things that he's speaking about.

Ms. Rivera commented that the Board should consider that based on the records from the PHP monitor,
the  physician’s  explanation  regarding  environmental  exposure  and  the  treating  provider’s  report  of
purchasing street Adderall.

Dr. Figge noted the discrepancy in time between the incident described by Dr. Aupperle and his treating
provider, noting that the treating provider’s report was much more recent.  Dr. Figge stated that the Board
had to make a decision based on the information that is available.

Board staff confirmed that there has been at least one negative hair test dated 2-25-25. It was negative for
methamphetamine, but positive for amphetamine

Final Minutes for the January 9, 2026 AMB Summary Action Teleconference Meeting
Page 2 of 3

During  deliberation,  Dr.  Gillard  noted
methamphetamine.

the  report

that  amphetamine  does  not  metabolize  as

MOTION: Dr. Gillard moved to summarily suspend Dr. Aupperle’s license pending the outcome of a
formal hearing in this matter based on a finding that Dr. Aupperle violated A.R.S. § 32-1401(27)(s)
and that the public health safety and welfare imperatively requires emergency action.
SECOND: Dr. Farmer.
Dr.  Gillard  noted  that  the  monitor  opined  that  you  can  only  have  a  positive  test  by  ingestion,  and  not
exposure. Dr. Beyer commented that the negative hair test persuaded him that this isn’t a problem with the
testing, but with the results. Dr. Figge commented that the Board order itself states that if there is a violation,
then it warrants summary suspension.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Dr. Bethancourt, Ms.
Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

E.  ADJOURNMENT

MOTION: Dr. Beyer moved for adjournment.
SECOND: Dr. Artz.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Dr. Bethancourt, Ms. Dorrell,
Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

The meeting adjourned at 5:30 p.m.

Raquel Rivera, Executive Director

Final Minutes for the January 9, 2026 AMB Summary Action Teleconference Meeting
Page 3 of 3

---

### 2026-01-07 — Arizona Medical Board — January 07, 2026

**[MINUTES] 2026-01-07_MD_202602051020_9b07cbd80c6b49678bb165abbc47fb12.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SPECIAL TELECONFERENCE MEETING
Held on Wednesday, January 7, 2026
1740 W. Adams St., Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 5:06 p.m.

B.  ROLL CALL

The following Board members participated virtually: Dr. Figge, Dr. Bethancourt, Ms. Dorrell, Dr.
Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps, M.D., Chief Medical Consultant; Nicole Samaradellis, Investigations Manager; and
Michelle Robles, Board Operations Manager. Carrie Smith, Assistant Attorney General (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT

•  Update on Board Appointments

Ms. Rivera reported that she met with Senator Warner and supports getting appointments
and  requested  she  work  with  the  Governor’s  office.  Ms.  Rivera  noted  that  she  has  a
meeting scheduled with the Governor’s office regarding a list of potential appointments.

Dr. Gillard suggested that the gaps with no appointments be filled first.

•  FSMB Annual Meeting

Ms. Rivera reminded Board members of the annual meeting and requested that interested
members contact staff for scholarships.

•  Update on AMB Sunset Audit Status

Ms. Rivera reported that the audit remains in progress and the draft is anticipated to be
released in March and the final in April.

•  Optimization of Call to Public Process

Ms. Rivera reported that staff is utilizing a new registration process for the Call to Public
process to make it more efficient.

E.  CHAIR’S REPORT

•  Discussion on Upcoming Elections and Possible Leadership Transition

Dr. Figge noted that every February there is elections of the Chair, Vice-Chair or Secretary
and if anyone is interested let him or Ms. Rivera know.

F.  LEGAL ADVISOR’S REPORT

No report was given.

G.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Board Members discussed the nuances and differences of using Google Meets since this was the
first meeting on this new platform.

H.  BOARD MEMBER TRAINING ON CONFLICT OF INTEREST
Ms. Smith provided conflict of interest training for Board members and staff.

I.  APPROVAL OF MINUTES

There were no minutes to approve.

LEGAL MATTERS

J.  REVIEW, CONSIDERATION AND POSSIBLE ACTION ON PROPOSED BOARD
ORDER ARISING FROM ADMINISTRATIVE LAW JUDGE’S RECOMMENDED
DECISION

1.  THIS CASE HAS BEEN MOVED TO ITEM J.

K.  DISCUSSION,  CONSIDERATION  AND  POSSIBLE  ACTION  ON  THE

ADMINISTRATIVE LAW JUDGE’S CERTIFIED FINAL DECISION.

1.  MD-23-0694A, AMMAR ALSHEIKH, M.D., LIC. #34325

Seth  Hargraves,  AAG  participated  virtually  on  behalf  of  the  State.  Deannie  Reh,  AAG
participated as the Board’s Independent Legal Advisor.

Ms. Reh advised the Board that the Board needs to implement the CME Order as a final
Order.

Dr. Figge noted that the physician has accepted the ALJ’s recommended decision.

Mr.  Hargraves  clarified  that  the  Advisory  Letter  has  already  been  issued  and  is  not
appealable. The  CME Order was appealable, there  was a hearing  and the ALJ made a
decision. The other side accepted that decision and that order is now final. Mr. Hargraves
stated  that  it  is  the  State’s  position  that  the  Board  should  follow  up  and  issue  the  CME
Order as directed.

Ms.  Bain  and  Dr.  Figge  requested  clarification  on  whether  the  Board  needs  to  make  a
motion since the ALJ decision has been accepted and certified.

Ms. Reh confirmed that the Board does not need to do anything further other than to instruct
Board staff to issue the order.  Dr. Figge directed staff to issue the order.

Final Minutes for the January 7, 2026 AMB Special Teleconference Meeting
Page 2 of 10

L.  DISCUSSION, CONSIDERATION AND POSSIBLE ACTION ON SETTLEMENT

OFFER IN LIEU OF FORMAL HEARING

1.  MD-25-0012A, LAURA HARRINGTON, M.D., LIC. #24671

Dr.  Harrington  participated  virtually  with  counsel  Michael  Goldberg.  Carrie  Smith,  AAG
participated virtually on behalf of the State. Deannie Reh, AAG participated as the Board’s
Independent Legal Advisor.

Ms.  Smith  reported  there  was  a  motion  to  continue  the  settlement  conference  at  the
October  meeting  to  allow  Board  staff  to  complete  the  investigation  and  to  allow  Dr.
Harrington to consider the Board’s position on the Dr. Harrington’s request for approval of
an alternative program. Ms. Smith further noted that there has since been a change in Dr.
Harrington’s representation. Ms. Smith informed the Board that the investigation process
is almost completed and staff is expecting the final report for Respondent’s review shortly.
Then  the  case  will  be  set  for  SIRC  review.  Ms.  Smith  requested  an  additional  60  day
continuance to wrap up the process and allow the parties to see if a settlement is possible.
Otherwise, the State is ready to proceed to formal hearing.

Mr. Goldberg stated that he is hopeful that we can get to a point where Dr. Harrington can
get off suspension.

MOTION: Dr. Gillard moved to continue the Settlement Conference for sixty days in
lieu of Formal Hearing.
SECOND: Dr. Artz.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

CONSENT AGENDA

M.  CASES RECOMMENDED FOR DISMISSAL

1.  MD-23-0611A, KASHIF ALVI, M.D., LIC. #43978

MOTION: Dr. Gillard moved to dismiss.
SECOND: Dr. Bethancourt.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

N.  CASES RECOMMENDED FOR ADVISORY LETTERS

MOTION: Dr. Beyer moved to issue an Advisory Letter in item numbers 1, 3, 4, 6 and 7.
SECOND: Dr. Gillard.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

1.  MD-24-1072A, TODD L. JACKSON, M.D., LIC. #52840

RESOLUTION: Advisory Letter for action taken by the Nevada Board. While there is
insufficient  evidence  to  support  disciplinary  action,  the  board  believes  that
continuation of the activities that led to the investigation may result in further board
action against the licensee.

2.  MD-25-0497A, VIDALIA M. BUTLER-POKU, M.D., LIC. #33705

Dr. Butler-Poku addressed the Board during the Public Statements portion of the meeting.

Final Minutes for the January 7, 2026 AMB Special Teleconference Meeting
Page 3 of 10

Dr. Artz opined that this was not an emergent case and that the delay does not warrant an
Advisory Letter.

MOTION: Dr. Artz moved to dismiss.
SECOND: Dr. Bethancourt.
Dr. Bethancourt commented that there seemed to be a lot of confusion. When the physician
called to follow up, they didn’t know where the patient went. Dr. Figge stated that it appears
that the patient had left and it sounds like there was some level of a system failure. Dr.
Figge  noted  that  the  physician  has  taken  measures  to  ensure  that  this  doesn't  happen
again.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

3.  MD-25-0212A, SHAWN F. HERMENAU, M.D., LIC. #36539

RESOLUTION: Advisory Letter for failing to establish or maintain adequate records
to  support  a  valid  physician-patient  relationship  prior  to  prescribing  medications.
While there is insufficient evidence to support disciplinary action, the board believes
that continuation of the activities that led to the investigation may result in further
board action against the licensee.

4.  MD-24-0808A, DAVID A. PARRY, M.D., LIC. #35015

Dr. Artz and Dr. Farmer stated that they know the physician but that it would not affect their
ability to adjudicate the case. Dr. Figge stated he also knows of him, but it does not affect
his ability to adjudicate the case.

RESOLUTION:  Advisory  Letter  for  failing  to  timely  reevaluate  an  infant  with  the
diagnosis  of  moderate  laryngomalacia.  While  there  is  insufficient  evidence  to
support disciplinary action, the board believes that continuation of the activities that
led to the investigation may result in further board action against the licensee.

5.  MD-24-1144A, CHRISTOPHER A. IANNOTTI, M.D., LIC. #43972

Counsel  Ms.  Maxwell  addressed  the  Board  during  the  public  statements  portion  of  the
meeting on behalf of the physician.

Dr. Gillard questioned why SIRC would think that someone should have an Advisory Letter
for  not  using  anti-coagulation  on  a  patient  that  was  operated  on  for  a  hemorrhage.  Dr.
Gillard further commented that it was more than a couple months later the patient did have
the PE after this physician was totally off the case

MOTION: Dr. Gillard moved to dismiss.
SECOND: Dr. Bethancourt.
Dr. Bethancourt agreed and commented that this was a spinal surgical case that dealt with
hemorrhage. While it was under the neurosurgeon's care there was mechanical prevention
and a low dose of Heparin used. Two months later this event occurred and he may have
needed  something,  but  Dr.  Bethancourt  opined  that  the  neurosurgeon  is  not  the  one
responsible.

Dr.  Deschamps  commented  that  SIRC’s  discussion  was  about  who  was  responsible  to
order  and  communicate  the  need  for  anti-coagulation,  not  on  the  indication  for  anti-
coagulation.

Board staff noted that this was an A and B case, where staff recommended an Advisory
Letter in the B case as well but it has not come to the Board yet.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer and Dr. Gillard.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.

Final Minutes for the January 7, 2026 AMB Special Teleconference Meeting
Page 4 of 10

MOTION PASSED.

6.  MD-23-0615A, ALKESHKUMAR H. PATEL, M.D., LIC. #35747

RESOLUTION:  Advisory  Letter  for  non-compliance  with  dispensing  reporting
requirements  and  for  dispensing  without  a  registration.  While  the  licensee  has
demonstrated substantial compliance through rehabilitation or remediation that has
mitigated the need for disciplinary action, the board believes that repetition of the
activities that led to the investigation may result in further board action against the
licensee.

7.  MD-24-1171A, MICHAEL M. JOHNSON, M.D., LIC. #12960

RESOLUTION:  Advisory  Letter  for  failing  to  monitor  a  patient  for  potential  side
effects  and  intolerance  to  a  GLP-1  agonist  medication  and  inappropriate  patient
communication. While there is insufficient evidence to support disciplinary action,
the board believes that continuation of the activities that led to the investigation may
result in further board action against the licensee.

O.  CASES  RECOMMENDED 

*[document truncated for length]*

---

### 2025-12-03 — Arizona Medical Board — December 03, 2025

**[MINUTES] 2025-12-03_MD_202603051042_92fc8e651e8b4f77ae991c06a72c6073.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR REGULAR SESSION MEETING
Held on Wednesday, December 3, 2025
1740 W. Adams St., Board Room A • Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P.
Lois E. Krahn, M.D

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 8:12 a.m.

B.  ROLL CALL

The  following  Board  members  participated  virtually:  Dr.  Figge,  Dr.  Bethancourt,  Ms.  Dorrell,  Dr.
Artz, Dr. Beyer, Dr. Farmer and Dr. Gillard.

The following Board members were absent: Ms. Bain and Dr. Krahn.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps,  M.D.,  Chief  Medical  Consultant;  Nicole  Samaradellis,  Investigations  Manager;  and
Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,  Assistant  Attorney  General  (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT

•  Update regarding Board appointments

Ms. Rivera reported that the Governor’s office is at an impasse with the Senate regarding
appointments. Ms. Rivera noted that she will meet with Senator Warner, which will also be
a  good  opportunity  for  her  to  discuss  the  PA  Sunset  audit  results  with  her  and  any
legislative needs we have in addition to addressing Board appointments.

•

IMLCC Update
Ms. Rivera reported that the IMLC is funded primarily through licensing fees, but it's also
augmented by grants by HRSA and the FSMB. When an individuual applies for an IMLCC
license,  there's  a  $700  application  fee  with  the  IMLCC,  and  then  they  would  pay  the
application  fee  for  their  state  of  principal  licensure.  Applicants  also  pay  $100  for  any

additional letters of qualifications they want sent to other states once they are part of the
compact. Just for fiscal year 26, the revenue for the Board has been $839,750, based on
the IMLCC applications received. During this time, we processed over 1,800 applications.
That included 281 state of principal licensures and 683 letters of qualifications. The Board
has processed 855 renewals thus far, and there were 17 applicants who were ineligible to
get an IMLCC license based on the requirements.

•  Administrators in Medicine Update

Ms. Rivera discussed her recent AIM meeting and reported that the FSMB is doing some
initial research with how to responsibly and ethically incorporate AI into clinical practice as
well as how AI can be used to assist regulatory boards with communication and legislative
tracking. Ms. Rivera stated that she would like to include this in the next newsletter, as well
as consider using AI to convert the newsletter into a podcast format.

•  Legislative Update

Ms. Rivera reported on an upcoming meeting with Representative Bliss and the Majority
Health  Policy  Advisor  to  discuss  foreign  trained  physicians  and  a pathway  for  licensure
without the requirement for residency to allow open additional residency spots for newly
trained physicians. Ms. Rivera noted that she proactively provided them with the FSMB's
ACOM guidance, an overview of other legislation in other states that have enacted what
they are looking at.

•  ED Selection and Retention Committee 2026

Ms. Rivera reported that after the new year, the Board will need to convene an ED Selection
and Retention Committee, just to address the PA Sunset Audit findings that were specific
to the Medical Board, and their recommendations with regard to the ED compensation and
performance  incentive  payments,  and  then  consideration  of  an  ED  annual  performance
evaluation for myself. The PA follow-up audit will happen in March, so she would like to
have some working recommendations for how to address their findings on the PA side that
impacted the MD side.

•  Death Certificate Responsibility Update

Ms.  Rivera  reported  that  she  met  with  the  Director  of  the  Maricopa  Medical  Examiner's
Office and the Chief Medical Examiner, Dr. Johnston. They confirmed that they don't have
jurisdiction to accept cases where a current care provider has been identified. They did
explain that in cases where there is a question of care, ME staff including a pathologist
reviews all the death reports that are received. For some reports, they know that somebody
has a current care provider if they died with family, or pill bottles are placed somewhere
with the doctor's name. Sometimes they have to do informal inquiries when they get notified
of a patient death, and once a current care provider is listed they are not allowed to accept
jurisdiction or sign that death certificate by law. Ms. Rivera provided the Board with some
relevant statutes regarding when they decline to sign those death certificates, or when they
refuse. They also said that they receive around 14,000 direct reports, with around 3,600
that  identify  current  care  providers  after  some  portion  of  review,  and  then  they  end  up
signing around 8,000 certifications a year.

•  Update regarding 1740 building

Ms. Rivera reported that the building suffered extensive flood damage. The IT storage room
suffered extensive damage and therefore the Board will be unable to meet in person until
new equipment is obtained.

Dr. Figge inquired if the Board is insured and whether the repair coming out of the Board’s
budget.

Ms. Rivera confirmed that this will be a significant expense for the Board and she will be
submitting a risk management claim. Ms. Rivera reported that the Board will need to eat
initial costs to at least replace the laptops.

E.  CHAIR’S REPORT

Final Minutes for the December 3, 2025 AMB Regular Session Meeting
Page 2 of 19

•  Acknowledgment of Dr. Krahn’s Service to the Arizona Medical Board

Dr. Figge acknowledged Dr. Krahn's service to the Board and noted that she was on the
Board for ten years.

•  Appointment of PHP Committee Chair

Dr. Farmer stated that he can conduct meetings in the interim until a new chair is
appointed.

Ms. Rivera noted that she will be requesting a psychiatrist be appointed to the Board.

F.  LEGAL ADVISOR’S REPORT

No report was given.

G.  PHYSICIAN HEALTH PROGRAM (PHP) REPORT

Ms.  Downey  requested  to  schedule  a  PHP  subcommittee  meeting  to  address  some  pressing
issues, specifically the approval to allow DOs to conduct PHP assessments, as that would increase
the options provided to participants or licensees. Ms.  direction on the process on how the Board
would like us to onboard and offboard the PHP contractors, just so we have that information in
place.

H.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

There was no discussion.

I.  APPROVAL OF MINUTES

There were no minutes for approval.

LEGAL MATTERS

J.  FORMAL INTERVIEWS

1.  MD-23-0994A, RUSSELL E. WESTERFIELD, M.D., LIC. #17798

Dr.  Westerfield  and  counsel  Paul  Giancola  participated  virtually.  Dr.  Farmer,  Dr.
Bethancourt  and  Dr.  Figge  stated  that  they  know  the  physician’s  expert  opinion  author
personally, but it will not affect their ability to adjudicate this case.

Board  staff  summarized  that  on  October  11,  2023,  the  Board  received  a  complaint
regarding Dr. Westerfield’s care and treatment to patient PM for failure to obtain informed
consent  for  anesthesia  and  inappropriately  signing  the  anesthesia  consent  form.  On
September 04, 2024, the case was discussed during the regular session meeting, which
returned for further investigation to address the allegation that Dr. Westerfield administered
propofol at the bedside and walked away. On October 16, 2024, based on that, Board staff
sent  a  re-notice  letter  to  Dr.  Westerfield  for  inappropriate  administration  of  propofol  to
patient in preop, while performing peripheral nerve block. Further, Dr. Westerfield failed to
appropriately monitor PM after administration and performance of peripheral nerve block.

Board staff further summarized that SIRC reviewed the Board’s concern and the Medical
Consultant’s (MC) second report that Dr. Westerfield deviated from the standard of care
because the documentation did not list the dose of propofol administered, if there was any
ECG,  pulse  oximeter  or  blood  pressure  cuff  attached  to  the  patient  at  the  time  of  the
administration,  or  if  the  RN  had  been  involved  in  monitoring  the  patient.  The  MC
acknowledged Dr. Westerfield’s report that he administered 50mg in titrated doses. The
MC  opined  that  the  standard  of  care  set  by  the  American  Society  of  Anesthesiologists,
JCAHO,  the  package  insert  and  others  is  that  safe  administration  of  propofol  to  non-
ventilator-assisted  patients  is  limited  to  individuals  trained  the  administration  of  general
anesthesia who are not involved in the procedure. The MC determined that Dr. Westerfield
deviated from the standard of care based on the lack of documentation, as he was unable
to determine the amount of propofol administered, the way it was administered, or if vital
signs were monitored or their values. SIRC discussed the case and remained concerned
with the lack of documentation to aid in the Board’s review of the care rendered as there

Final Minutes for the December 3, 2025 AMB Regular Session Meeting
Page 3 of 19

was no dictated procedure note and no anesthetic record dedicated to the block procedure
under sedation. SIRC noted the MC’s comment that it could not be determined whether
the  RN  present  was  capable  or  prepared  to  monitor  an  anesthetic  potentially  leaving  a
freshly blocked, anesthetized patient unmonitored. SIRC acknowledged Dr. Westerfield’s
report that he no longer provides sedation when performing a regional block in the preop
area. SIRC recognized that despite no actual harm being identified, there was significant
potential risk to the patient. SIRC observed that Dr. Westerfield has no prior Board history;
however, SIRC considered the lack of documentation an aggravating factor in this case.

Dr.  Westerfeld  provided  an  opening  statement  to  the  Board  and  informed  them  of  the
procedure but noted that he did not obtain a signed consent agreement prior to the surgery.

During questioning, Dr. Westerfield took responsibility for signing the form and stated that
he  determined  that  they  could  resolve  it  in  recovery.  Dr.  Westerfield  opined  that  the
uncertainty with the nurses at the time this occurred could be due to him being new on staff
at the time. Regarding the administration of the propofol in the pre-op area, Dr. Westerfield
informed the Board of the order of the events and that by the time he did the block the
patient was awake again. The nurse was present the whole time. Dr. Westerfield confirmed
how he bolused the propofol. Dr. Westerfield confirmed that the patient met recovery status
before he left. Dr. Westerfield commented that if the nurse was uncomfortable, she could
have said something or did something at the time but waited to file an incident report. Dr.
Westerfield  informed  the  Board  that  there  he  used  a  standardized  Banner  form  to
document the block. Dr. Westerfield explained that he typically does not like to provide the
block in pre-op in case anything goes wrong but was instructed to by the nurse. Regarding
signing the patient’s name, Dr. Westerfield explained that he had never had a nurse put
the clipboard in front of him like th

*[document truncated for length]*

---

### 2025-11-05 — Arizona Medical Board — November 05, 2025

**[MINUTES] 2025-11-05_MD_202602051019_7f9d5119af724fc3a214991ced972806.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SPECIAL TELECONFERENCE MEETING
Held on Wednesday, November 5, 2025
1740 W. Adams St., Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Lois E. Krahn, M.D
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 5:08 p.m.

B.  ROLL CALL

The following Board members participated virtually: Dr. Figge, Dr. Beyer, Dr. Farmer, Ms. Dorrell,
Dr. Gillard, Dr. Krahn, Dr. Artz and Ms. Bain.

The following Board members were absent: Dr. Bethancourt and Ms. Leach.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps,  M.D.,  Chief  Medical  Consultant;  Nicole  Samaradellis,  Investigations  Manager;  and
Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,  Assistant  Attorney  General  (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT
•  Quarterly FSMB Update on USMLE

Ms. Rivera provided an update on upcoming changes.

•  FSMB 2026 Presentation Co-Presentation- Remedial CME Criteria

Ms. Rivera provided the presentation for the Board’ s review and requested the Board’s
approval to present at the meeting.

Ms. Bain inquired if the Board needs to give  permission to the  Executive Director to  do
these types of things.

Ms. Smith noted that there is nothing in statute that requires the Board’s approval.

Board members provided their support for this presentation.

•

IMLC Annual Report

Ms. Rivera provided the report for the Board’s review and stated that starting next year she
will  begin  providing  an  update  at  every  meeting.  Ms.  Rivera  noted  that  as  the  Board’s
Executive  Director  she  is  a  member  of  the  IMLC  commissioner  and  is  assigned  to  the
communications committee and will be attending the IMLC annual meeting and the AIM
fall meeting in Aurora, Colorado.

•  Request for Delegated Authority to Approve Pro Hac Vice Applications

Ms.  Rivera  requested  delegated  authority  to  approve  pro  hac  vice  applications  for
efficiency.

MOTION: Dr. Krahn moved to allow the ED to approve Pro Hac Vice Applications.
SECOND: Dr. Gillard.
Ms. Smith noted the out-of-state attorney who seeks admission must apply to the State
Bar. The State Bar runs a primary source review of credentials. In addition, the attorney
must have a local counsel who agrees to assist them.
VOTE: The following  Board members  voted in favor of the motion: Dr. Figge, Ms.
Dorrell,  Ms.  Bain,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Dr.  Krahn.  The  following
Board members were absent: Dr. Bethancourt, Dr. Artz and Ms. Leach.
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

•  Consideration of the Need for Legislation in Advance of Next Legislative Session

Ms. Rivera requested executive session for legal advice and review of confidential material.

MOTION: Ms. Bain moved for the Board to enter into Executive Session pursuant to
A.R.S.  §  32-431.03(A)(3)  and  (2)  to  obtain  legal  advice  and  to  discuss  confidential
matters.
SECOND: Dr. Beyer.
VOTE: The following  Board members  voted in favor of the motion: Dr. Figge, Ms.
Dorrell,  Dr.  Artz,  Ms.  Bain,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Dr.  Krahn.  The
following Board members were absent: Dr. Bethancourt, Dr. Artz and Ms. Leach.
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

The Board entered into Executive Session at 7:29 p.m.
The Board returned to Open Session at 7:54 p.m.
No legal action was taken by the Board during Executive Session.

Ms. Rivera requested that the Board allow her to proceed with legislative change.

Dr. Figge spoke on behalf of the Board and requested that she proceed.

•  Review of All Meetings Calendar

Ms. Rivera noted the 2026 calendar for the Board’s review.

MOTION: Dr. Gillard moved to approve the JLRC and Biannual Joint Officers meeting
calendars.

Final Minutes for the November 5, 2025 AMB Special Teleconference Meeting
Page 2 of 14

SECOND: Ms. Dorrell.
VOTE: The following  Board members  voted in favor of the motion: Dr. Figge, Ms.
Dorrell,  Ms.  Bain,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Dr.  Krahn.  The  following
Board members were absent: Dr. Bethancourt, Dr. Artz and Ms. Leach.
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

E.  CHAIR’S REPORT

•  2026 Annual FSMB Meeting

Dr. Figge informed the Board of the upcoming meeting and that interested board members
can contact staff to attend.

Dr. Figge thanked Ms. Leach for her time and service on the Board over the last year.

F.  LEGAL ADVISOR’S REPORT

•  Update  on  Atilla  Mady,  M.D.,  et  al.  v.  Ramila  De  Souza  Dias,  et  al.  Maricopa  County

Superior Court Case No. CV2025-032252

Michael Niederbaumer, AAG and Mathew Kelly, AAG introduced themselves to the Board.
Ms. Smith noted that substantive materials have been provided to the Board for review.

•  Update on Mady v. Arizona Medical Board, Case No. LC2025-000219-001

Ms. Smith reported that there was a motion for stay of the Board’s Order for Revocation.
That  motion  has  been  denied  by  the  court.  Ms.  Smith  has  filed  for  a  motion  of
Reconsideration.

G.  CONSIDERATION  AND  POSSIBLE  ACTION  ON  PRO  HAC  VICE

APPLICATION

Ms. Smith explained that the Board needs to approve the pending application.

MOTION: Dr. Gillard moved to approve the Pro Hac Vice application.
SECOND: Dr. Krahn.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Dr. Beyer, Dr.
Farmer,  Ms.  Dorrell,  Dr.  Artz,  Dr.  Gillard,  Dr.  Krahn,  and  Ms.  Bain.  The  following  Board
members were absent: Dr. Bethancourt and Ms. Leach.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

H.  PHYSICIAN HEALTH PROGRAM (PHP) REPORT

No report was given.

I.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Dr.  Gillard  acknowledged  Dr.  Krahn’s  service  to  the  Board  which  allowed  the  Board  to  keep  a
quorum and keep functioning.

Board staff requested that Board members confirm attendance for December.

Ms. Bain commented that she may need to attend virtually in December.

LEGAL MATTERS

J.  RESCIND  REFERRAL  TO  FORMAL  HEARING  AND  ACCEPT  PROPOSED

CONSENT AGREEMENT

Final Minutes for the November 5, 2025 AMB Special Teleconference Meeting
Page 3 of 14

1.  MD-20-1000B, MD-24-0118A, MARK J. RUBIN, M.D., LIC. #28310

Callie  Maxwell  participated  virtually  on  behalf  of  Dr.  Rubin.  Seth  Hargraves,  AAG
participated virtually on behalf of the State. Deanie Reh, AAG participated virtually as the
Board’s Independent Legal Advisor.

Ms. Maxwell stated that they agreed to the consent agreement as drafted and requested
that the Board accept it.

Mr.  Hargraves  agreed  that  after  the  settlement  conference  the  parties  put  together  the
consent agreement based on what the Board agreed upon. Mr. Hargraves requested that
the Board approve it.

MOTION: Dr. Gillard moved to rescind the referral to formal hearing and accept the
consent  agreement
for  a  Decree  of  Censure  and  Three-Year  Probation.
Respondent’s  practice  is  restricted  in  that  he  shall  not  return  to  treating  patient
and/or engaging in the clinical practice of medicine until authorized by the Board.
Prior  to  any  Board  consideration  for  termination  or  modification  of  this  Practice
Restriction,  Respondent  must  submit  a  written  request  to  the  Board.  Respondent
shall within six months of any request to return to active clinical practice, obtain no
less  than  15  hours  of  Board  Staff  pre-approved  Category  1  Continuing  Medical
Education  (CME)  in  an  intensive,  in-person/virtual  course  regarding  controlled
substance  prescribing.  Within  six  months  of  the  effective  date  of  this  Order,
Respondent  shall  complete  the  Professional/Problem-Based  Ethics  (ProBE)
program offered by CPEP for Ethics and Boundaries. Respondent shall obtain an
unconditional or conditionally passing grade. In the event that Respondent does not
receive  an  unconditional  or  conditionally  passing  grade,  Respondent  shall  follow
any  and  all  recommendations  made  for  further  education  and/or  remediation,
subject  to  approval  by  the  Board  or  its  staff.  Within  30  days  after  Respondent
successfully  completes  ProBE,  he  shall  enroll  in  ProBE  Plus.  Respondent  shall
successfully complete ProBE Plus as determined by the final report from the ProBE
faculty monitor and approved by Board staff. The CME hours shall be in addition to
the hours required for the renewal of licensure. The Probation shall not terminate
except upon affirmative request of Respondent and approval by the Board.
SECOND: Dr. Artz.
VOTE: The following  Board members  voted in favor of the motion: Dr. Figge, Ms.
Dorrell,  Dr.  Artz,  Ms.  Bain,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Dr.  Krahn.  The
following Board members were absent: Dr. Bethancourt and Ms. Leach.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

CONSENT AGENDA

K.  CASES RECOMMENDED FOR DISMISSAL

Dr. Gillard noted that the Board previously reviewed case number four and sent it back for further
review and had two medical consultants agree with dismissal.

MOTION: Dr. Gillard moved to dismiss item numbers 1-5.
SECOND: Dr. Artz.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Ms. Dorrell, Dr.
Artz,  Ms.  Bain,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Dr.  Krahn.  The  following  Board
members were absent: Dr. Bethancourt and Ms. Leach.
VOTE: 8-yay, 0-nay, 0-abstain, 0(Dr. Beyer recused from #4)-recuse, 2-absent.
MOTION PASSED.

1.  MD-24-0384A, JACK F. PERRONE, M.D., LIC. #55547

RESOLUTION: Dismissed.

2.  MD-24-0050A, STEVEN L. ROSINSKI, M.D., LIC. #53603

Final Minutes for the November 5, 2025 AMB Special Teleconference Meeting
Page 4 of 14

RESOLUTION: Dismissed.

3.  MD-23-0578A, CRAIG A. HOOVER, M.D., LIC. #21932

RESOLUTION: Dismissed.

4.  MD-23-1212A, ANDERSON A. BAUER, M.D., LIC. #46060

E.R.,  Dr.  Bauer,  and  counsel  Callie  Maxwell  addressed  the  Board  during  the  Public
Statements portion of the meeting. Dr. Beyer recused.

RESOLUTION: Dismissed.

5.  MD-24-1012A, POUYA MOHAJER, M.D., LIC. #42513

RESOLUTION: Dismissed.

L.  CASES RECOMMENDED FOR ADVISORY LETTERS

MOTION: Dr. Gillard moved to issue an Advisory Letter in item numbers 1-4 and 9-16.
SECOND: Dr. Beyer.
Dr.  Krahn  noted  a  typo  in  the  SIRC  report  for  case  #4,  it  should  state  postmortem  and  not
postpartum.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Ms. Dorrell, Dr.
Artz,  Ms.  Bain,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Dr.  Krahn.  The  following  Board
members were absent: Dr. Bethancourt and Ms. Leach.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

1.  MD-24-0682A, JOONHEE LIM, M.D., LIC. #55529

A.G. addressed the Board during the Public Statements portion of the meeting.

RESOLUTION:  Advisory  Letter  for  inadequate  communication  of  medication
discontinuation  and  for  failing  to  discuss  or  document  alternative  medications
insufficient  evidence  to  support
and/or  bridging  therapies.  While  there
disciplinary action, the board believes that continuation of the activities that led to
the i

*[document truncated for length]*

---

### 2025-10-30 — Arizona Medical Board — October 30, 2025

**[MINUTES] 2025-10-30_MD_202602191559_2cc6462aea72451287fb576c50c911b6.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR ADMINISTRATIVE JOINT LEGISLATION AND RULES
COMMITTEE TELECONFERENCE MEETING
Held on Thursday, October 30, 2025
1740 W. Adams St., Phoenix, Arizona

Committee Members
Jodi A. Bain, M.A., J.D., LL.M., Chair
Katie S. Artz, M.D., M.S.
Bruce Bethancourt, M.D.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.

GENERAL BUSINESS

A.  CALL TO ORDER

Chairwoman Bain called the Committee’s meeting to order at: 5:08 p.m.

B.  ROLL CALL

The following Committee members participated virtually: Dr. Bethancourt, Dr. Farmer, Ms. Bain,
Dr. Artz, Dr. Figge and Ms. Dorrell.

The following Board staff participated in the virtual meeting: Raquel Rivera, Executive Director; and
Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,  Assistant  Attorney  General  (“AAG”)
was also present.

C.  GENERAL CALL TO THE PUBLIC

Individuals who addressed the Committee during the Public Statements portion of the meeting are
listed under the topic.

D.  APPROVAL OF MINUTES

•
July 31, 2025 Administrative Joint Legislation and Rules Committee
•  August 26, 2025 Administrative Joint Legislation and Rules Committee

Dr. Artz and Dr. Bethancourt noted that their attendance is inaccurately captured in the minutes.

MOTION: Ms. Dorrell moved to approve the July 31, 2025 Administrative Joint Legislation
and Rules Committee minutes.
SECOND: Dr. Figge.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Dr. Artz and Ms. Dorrell.
The following Committee members were absent: Ms. Bain and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.

MOTION: Ms. Dorrell moved to approve the August 26, 2025 Administrative Joint Legislation
and Rules Committee minutes.

SECOND: Dr. Figge.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge and Ms.
Dorrell. The following Committee members abstained. Dr. Artz and Dr. Bethancourt.
The following Committee members were absent: Dr. Farmer and Ms. Bain.
VOTE: 2-yay, 0-nay, 2-abstain, 0-recuse, 2-absent.

E.  REVIEW OF AMB ALL MEETINGS CALENDAR

•  Proposed 2026 Meeting Dates

Ms. Rivera provided a calendar with all JLRC meetings, the AMB 2025 and 2026 All Meeting
calendar. Ms. Rivera commented that since  two members of the Committee have fallen off,
she will bring the calendar back for approval.

Dr. Figge requested that the calendar be placed on the full Board agenda for consideration and
inquired if there will be training.

Ms.  Rivera  informed  the  Committee  that  she  is  planning  for  next  year  to  include  training  in
regular Board meetings, and she would  also  like to  have an off-site meeting  that just solely
focuses on education.

F.  REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATION REGARDING

FIVE YEAR REVIEW AND RULEMAKING CALENDAR
Ms.  Rivera  reported  that  she  continues  to  work  on  adding  historical  details  to  the  rulemaking
calendar  and  that  there  have  been  no  major  changes  to  the  rulemaking  calendar  since  the  last
meeting.

G.  FIVE YEAR REVIEW

1.  ARTICLE 2, LICENSURE – STATUS UPDATE REGARDING FIVE-YEAR REVIEW REPORT

Ms. Rivera reported that she submitted the 5YRR on September 26, 2025, well in advance of
the extension deadline of December 29, 2025. This has not been scheduled for an upcoming
GRRC agenda. On October 21, 2025, she requested authorization to proceed with rulemaking
from  the  Governor’s  Office  pursuant  to  A.R.S.  §  41-1039(A)  for  the  proposed  rulemaking
changes identified in the 5YRR. Ms. Rivera noted that she did identify a rule she overlooked
that  requires  removal.  Specifically,  R4-16-201(D)(7)  requires  verification  of  all  hospital
affiliations for the last 5 years, which was a statutory requirement until the amendment of A.R.S.
§ 32-1422(11)(b) due to Senate Bill 1404, which became effective in April 2019, and since that
time has required the last 5 years of medical employment in lieu of hospital affiliations.  Since
this is no longer a statutory requirement, the rule should be amended  . Ms. Rivera provided
the revised Article 2 5YRR for reference.

H.  RULEMAKING

1.  ARTICLE  7,  OFFICE  BASED  SURGERY  -  REVIEW,  DISCUSSION  AND  UPDATE

REGARDING RULEMAKING STATUS

Ms. Rivera reported that on October 15, 2025, GRRC’s Staff Attorney reached out to her and
requested clarification of stakeholder’s comments and AMB responses from oral proceedings.
Subsequently, he requested she provide a revised Notice of Final Rulemaking (NFR) to include
a  response  to  all  stakeholder  comments.    The  Article  7  rules  were  discussed  at  the  GRRC
Study Session on October 28, 2025 and there were no reported concerns with the proposed
rulemakings.  A  GRRC  council  member  inquired  whether  the  Board  collaborated  with  the
Nursing  Board  on  the  rules  and  which  guidelines  were  considered  as  part  of  the  amended
language.  The  proposed  changes  will  now  be  considered  at  the  GRRC  council  meeting  on
November 4, 2025. If approved at GRRC, the Board would then file the rules with the Secretary
of State to be published in the Administrative Register to be effective within 60 days.

Final Minutes for the October 30, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 2 of 5

2.  ARTICLE 4, MEDICAL ASSISTANTS – REVIEW, DISCUSSION, AND CONSIDERATION OF

PURSUING RULEMAKING TO ADDRESS AUTHORIZED PROCEDURES FOR MAS

Dr.  Joe  Giancola  addressed  the  Committee  during  the  Public  Statements  portion  of  the
meeting.

Ms.  Rivera  reported  that  at  the  prior  meeting,  the  Committee  received  a  lot  of  information
related to authorized procedures for MAs and there was some discussion about the need for
rulemaking to address these issues. She attached her correspondence with our rule writer for
the Committee’s review and consideration. Ms. Rivera requested the Board’s input on whether
they would like her to request authorization to proceed with rulemaking on this issue so that
the Board can formally establish and codify any authorized procedures in rule. Additionally, Ms.
Rivera  requested  the  Board’s  approval  of  the  attached  revised  MA  FAQ  document  with
additional wording noting that these FAQs are intended solely to provide general clarification
regarding medical assistant procedures and does not create or amend any rule or policy of the
Board.

Dr.  Huether  stated  that  he  initially  found  the  FAQs  confusing  that  MAs  could  administer
injections of scheduled drugs but not local anesthetics and requested clarification.  Dr. Huether
stated that local anesthetic injections are done routinely throughout the country and safely by
MAs  under  physician  supervision  and  noted  this  approach  is  supported  by  the  American
Academy  of  Dermatology,  the  Mohs  College,  and  the  American  Society  of  Dermatologic
Surgery. Dr. Huether stated that they want to make sure it is done safely. Dr. Huether stated
that they worked hand-in-hand with the Arizona Anesthesia Society to develop guidelines of
what  that  safe  delegation  of  local  anesthetic  would  be,  and  requested  that  the  Committee
consider the recommendation.

Ms.  Bain  stated  that  her  understanding  was  that  the  issue  was  regarding  what  the  word
‘anesthetic’ and the word ‘supervision’ means.

Ms. Smith stated that this is a policy decision for the Board to make.

Ms. Rivera commented that with regard to the max of 300 milligrams and the 3 cc's of injections,
there needs to be additional research about whether this is something that could be addressed
in the FAQs without rulemaking, or whether it's something that requires rulemaking.

Dr. Bethancourt  noted that a  MA is  allowed to  do  anything that the  physician  overseas and
permits.

Ms. Rivera clarified that there are certain procedures that fall within an MA scope of practice,
so our rules outline what their training requirements are, and that a physician can provide that
training. Additionally, it says that the Board can prescribe any additional procedures that MAs
are authorized to do in rule.

Dr.  Figge  clarified  that  the  Committee  broke  down  the  language  to  specifically  address
lidocaine. Dr. Farmer commented that this is something that is amenable to rule making and
opined that Dr. Huether’s effort to work with the anesthesiology society was appropriate. Dr.
Bethancourt suggested just changing “anesthetic” to “local anesthetic”. Ms. Bain commented
that if it’s not in statute, there may be pushback from GRRC.

Ms. Smith noted that to administer injections is in the statute but it is incredibly broad language,
and the Board has authority to interpret its own statutes through rule. The fact that it is in statute
provides the Board with some basis for at least pursuing rulemaking in this arena.

Dr. Giancola suggested that a simple change would be to allow local anesthetics.

Dr. Bethancourt inquired whether this is limited to just lidocaine and asked if revision should be
focused on just that issue. Dr. Figge commented that the previous discussion was for lidocaine,
but agreed that local anesthetic would be fine.

Final Minutes for the October 30, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 3 of 5

Dr. Tournas highlighted that the restriction on injections were not in statute, but in the FAQs
and requested striking the restrictions that were inserted within the FAQs that are not in statute.

Ms. Bain suggested that Ms. Smith review Dr. Tournas’s comments.

Dr. Farmer opined that the Board has to be careful about what is endorsed and incrementally
injecting  over  a  period  of  time  to  a  dose  of  300  milligrams  is  very  different  than  potentially
injecting it immediately and maybe getting intravascular by accident or something. Dr. Farmer
opined that it’s important to expedite a solution as soon as possible. Dr. Bethancourt agreed
that  the  Board  has  done  due  diligence  and  that  the  dermatologist  and  the  anesthesiology
society have given their intent for safety and to do the right thing.

Ms. Smith recommended the Committee evaluate these issues, make a game plan, and that
can be referred to the Board.

Ms. Rivera confirmed that depending on Ms. Smith’s review and what her advice is at that time,
she can bring this back before the Board or the JLRC, depending on the timing. Ms. Rivera
noted that she will make sure to provide what that wording looks like, so the Committee will
have some options for decision making.

MOTION: Dr. Figge moved to approve the Executive Director amending the FAQs with
the suggestion red lined language.
SECOND: Dr. Artz.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge, Dr.
Bethancourt, Dr. Artz and Ms. Dorrell.
The following Committee members were absent: Ms. Bain and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.

I.  REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATIONS REGARDING

PA SUNSET AUDIT REPORT

Ms. Rivera provided the PA Sunset Audit for review and consideration. Ms. Rivera informed the
Committee  that  she  continues  to  work  through  the  recommendations  related  to  investigations,
managerial/departmental oversight and monitoring. Specific to the JLRC, the Committee will need
to discuss the recommendations related to performance metrics and related incentive payments.
Ms. Rivera noted the recommendations in the memo and stated that she will bring these back to
the committee for review at the end of the fiscal year.

J.  CONSIDERATION OF THE NEED FOR LEGISLATION IN ADVANCE OF NEXT

LEGISLATIVE SESSION

MOTION: Dr. Figge moved for the Board to enter into Executive Session pursuant to A.R.S.
§ 32-431.

*[document truncated for length]*

---

### 2025-10-20 — Arizona Medical Board — October 20, 2025

**[MINUTES] 2025-10-20_MD_202602051015_20dd54ca7cf64c4c9a5872ab2b0c8355.pdf**

ARIZONA MEDICAL BOARD
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SPECIAL TELECONFERENCE MEETING
Held on Monday, October 20, 2025
1740 W. Adams St., Board Room 4100 • Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Lois E. Krahn, M.D
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 4:35 p.m.

B.  ROLL CALL

The following Board members were present: Dr. Figge, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Gillard, Dr.
Krahn, and Ms. Leach.

The following Board members were absent: Dr. Bethancourt and Dr. Farmer.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude Deschamps, M.D.,
Chief  Medical  Consultant;  Nicole  Samaradellis,  Investigations  Manager;  and  Heather  Foster,  Public  Records
Coordinator. Carrie Smith, Assistant Attorney General (“AAG”) also participated in the meeting.

C.  CALL TO THE PUBLIC

Individuals who addressed the Board during the Public Statements portion of the meeting appear beneath the case.

LEGAL MATTERS

D.  REVIEW, DISCUSSION AND POSSIBLE ACTION REGARDING SUMMARY ACTION

1.  MD-23-1157A, JOSEF SIPOS M.D., LIC. #61852

Dr. Sipos and Counsel Jessica Miller were virtually present.

Board staff summarized that this case was initiated after receiving a complaint from KJ alleging that Dr.
Sipos gave her his cell phone number for the purpose of communicating about her medical issues and then
engaged  in  inappropriate  communications  and  retaliatory  behavior.  During  the  investigation,  Dr.  Sipos
denied the allegations and reported being homosexual, with a well-established gay identity. Dr. Sipos also
denied a history of complaints regarding his conduct with female staff. Dr. Sipos admitted to performing
home  visits  and  providing  his  cell  to  patients  and  reported  he  would  document  his  care  in  the  medical
records. Board staff did not identify his correspondence with KJ in her medical records. Board staff obtained

employment records from two prior employers which document multiple boundary complaints from female
staff as well as an Order of Protection issued in 2023 against Dr. Sipos on behalf of a female MA who had
alleged  retaliatory  behavior.  Board  staff  obtained  police  records  which  identified  a  June,  2025  domestic
violence assault charge filed by a female victim reporting that she was in a relationship with Dr. Sipos. Of
note, this charge is a reportable misdemeanor that was not reported to the Board but discovered during this
investigation. On October 3, 2025, Dr. Sipos was issued an Interim Order for Psychosexual Evaluation and
offered  an  Interim  Consent  Agreement  (ICA)  for  Practice  Restriction.  On  October  8,  2025,  Dr.  Sipos’
attorney declined the ICA citing the lack of imminent danger and his intention to comply with the Interim
Order. Dr. Sipos noted that he currently works in an all-male correctional setting and would arrange a 3-
month leave of absence and requested the Board decline summary action. On October 16, 2025, Dr. Sipos’
attorney provided a voluntary psychiatric evaluation performed on October 15, 2025. Board staff reviewed
the  letter,  which  appeared  to  only  reference  the  charges  in  June  2025.  It  remains  unclear  whether  the
evaluator had all the information currently being reviewed by the  Board to render an opinion. Dr. Sipos’
attorney reported that he is currently scheduled for a psychosexual evaluation.

Ms. Miller stated the questions about Dr. Sipos’ judgment and professional interactions will be answered
through the ongoing investigation and evaluation process. Ms. Miller noted that Dr. Sipos has completed a
psychiatric  evaluation  to  help  the  Board  make  a  determination  and  has  been  compliant  throughout  the
investigation process. Ms. Miller requested that the Board not summarily suspend Dr. Sipos’ license while
the investigation continues.

Dr. Sipos stated that he acknowledges he has made mistakes. He has crossed professional boundaries.
Dr. Sipos further stated he understood the conduct was inappropriate, even if he did not have sexual intent.
Dr. Sipos further acknowledged that professionals have made strict guidelines to keep safe boundaries at
work. Dr. Sipos acknowledged his actions were harmful and apologized for them. Dr. Sipos stated that he
understands  words  are  not  enough,  but  can  offer  transparency,  documentation  and  continuation  of
cooperation with the investigation process.

Dr. Beyer inquired about the timeline of the investigation process.

Board staff explained that this case has been working consistently over the years by coordinating records
requests, interviews, and new information coming to light.

Ms.  Rivera  stated  the  investigation  continued  based  on  new  information  coming  to  light  during  the
investigative process.

Dr. Krahn asked if she could see the information that the psychiatrist used to evaluate Dr. Sipos to come
up with the conclusion in the evaluation letter.

Ms.  Rivera  stated  the  evaluation  letter  was  only  provided  to  the  Board  and  that  no  supplemental
documentation was supplied with the evaluation letter.

Dr. Krahn opined the cover letter alone provided contradictory information.

Dr. Beyer opined that summary suspension is not needed at this time and that  the  investigation should
continue.

                          SECOND: Dr. Artz.

MOTION: Dr. Beyer motion to continue the investigation and not summarily suspended the license.

Ms. Leach is against the motion. Dr. Artz agrees with the motion and does not see a warrant to suspend
the license.

Final Minutes for the October 20, 2025 AMB Special Teleconference Meeting
Page 2 of 4

Board staff commented that there is a concern regarding a pattern of behavior with women and noted that
Dr. Sipos’ employment records indicate he requested leave for a health condition. Board staff expressed
concern regarding the physician’s honesty and truthfulness.

Dr. Krahn spoke against the motion given the pattern of lack of candor and the leave of absence from work
is due to health condition. Dr. Gillard spoke against the motion as he would have liked to see the physician
sign the practice restriction during the investigation process.

VOTE: The following Board members voted in favor of the motion: Dr. Artz, and Dr. Beyer,
The following Board members voted against the motion: Dr. Figge, Ms. Dorrell, Ms. Bain, Dr. Gillard,
Dr. Krahn, and Ms. Leach.
The following Board members were absent: Dr. Bethancourt and Dr. Farmer.
VOTE: 2-yay, 6-nay, 0-abstain, 0-recuse, 2-absent.
MOTION FAILED

MOTION:  Dr.  Gillard  motion  to  offer  Dr.  Sipos  an  Interim  Consent  Agreement  for  Practice
Restriction.  If  not  signed  by  5:00  p.m.  tomorrow,  summarily  suspend  Dr.  Sipos  from  practicing
medicine in the State of Arizona pending the outcome of a Formal Hearing based on a finding that
the public health, safety and welfare imperatively require emergency action.
SECOND: Dr. Krahn
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Ms. Dorrell, Ms. Bain,
Dr. Beyer, Dr. Gillard, Dr. Krahn, and Ms. Leach.
The following Board member voted against the motion: Dr. Artz
The following Board members were absent: Dr. Bethancourt and Dr. Farmer.
VOTE: 7-yay, 1-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

E.  LICENSE APPLICATIONS

i.  CONSIDERATION  AND  POSSIBLE  ACTION  TO  APPROVE  OR  DENY  LICENSE

APPLICATION FOR REACTIVATION, OR TAKE OTHER ACTION

1.  MD-25-1076A, WILLIAM G. CANCE, M.D., LIC. #53191

Dr. Cance addressed the Board during the Public Statements portion of the meeting.

MOTION: Dr. Krahn moved to grant approve the application for reactivation of license.
SECOND: Dr. Gillard.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Ms. Dorrell, Dr.
Artz, Ms. Bain, Dr. Beyer, Dr. Gillard, Dr. Krahn, and Ms. Leach.
The following Board members were absent: Dr. Bethancourt and Dr. Farmer.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

F.  ADJOURNMENT

MOTION: Gillard moved for adjournment.
SECOND: Leach.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Ms. Dorrell, Dr. Artz, Ms. Bain,
Dr. Beyer, Dr. Gillard, Dr. Krahn, and Ms. Leach.
The following Board members were absent: Dr. Bethancourt and Dr. Farmer.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

The meeting adjourned at: 5:12 pm

Final Minutes for the October 20, 2025 AMB Special Teleconference Meeting
Page 3 of 4

Raquel Rivera, Executive Director

Final Minutes for the October 20, 2025 AMB Special Teleconference Meeting
Page 4 of 4

---

### 2025-10-08 — Arizona Medical Board — October 08, 2025

**[MINUTES] 2025-10-08_MD_202510271303_d2b641c249e341dbb72a20a500d79d85.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

DRAFT MINUTES FOR BOARD REVIEW COMMITTEE B MEETING
Held on Wednesday, October 8, 2025
1740 W. Adams St. • Phoenix, Arizona

Committee Members
David C. Beyer, M.D., Chair
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Lois Krahn, M.D.
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chairman Beyer called the Committee’s meeting to order at: 4:33 p.m.

B.  ROLL CALL

The following Committee members were present virtually: Dr. Artz, Dr. Beyer and Dr. Gillard.

The following Committee members were absent: Dr. Krahn and Ms. Bain.

ALSO PRESENT
The  following  Board  staff  participated  in  the  meeting:  Raquel  Rivera,  Executive  Director;  Nicole
Samaradellis, Investigations Manager Amy Skaggs, SIRC Coordinator and Heath Foster, Public
Records Coordinator. Carrie Smith, Assistant Attorney General (“AAG”) was also present.

C.  OPENING STATEMENTS

D.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals  who  addressed  the  Committee  during  the  Public  Statements  portion  of  the  meeting
appear beneath the case.

E.  APPROVAL OF MINUTES

June 4, 2025 Review Committee B Minutes, including Executive Session

•
•  August 6, 2025 Review Committee B Minutes

MOTION: Dr. Gillard moved to approve the June 4, 2025 Review Committee B Minutes;
including Executive Session and the August 6, 2025 Review Committee A Minutes.
SECOND: Dr. Artz.
VOTE: The following Committee members voted in favor of the motion: Dr. Beyer, Dr.
Gillard,  Dr.  Artz  and  Ms.  Bain.  The  following  Committee  members  were  absent:  Ms.
Bain and Dr. Krahn.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.

MOTION PASSED.

CONSENT AGENDA

F.  APPROVAL OF DRAFT FINDINGS OF FACT, CONCLUSIONS OF LAW AND

ORDER

1.  MD-23-0991B, BRADLEY E. NEUMAN, M.D., LIC. #54062

Ms.  Petersen  addressed  the  Committee  during  the  Public  Statements  portion  of  the
meeting.

MOTION: Dr. Gillard  moved to approve the draft Findings of Fact, Conclusions of
Law  and  Order  for  a  Letter  of  Reprimand  and  Probation.  Within  six  months,
complete no less than 3 hours of Board staff pre-approved Category l CME in the
evaluation, diagnosis, and treatment of small bowel obstructions including closed
loop  obstruction,  mesenteric  obstruction,  small  bowel  tumors,  and  volvulus.  The
CME  hours  shall  be  in  addition  to  the  hours  required  for  license  renewal.  The
Probation  shall  terminate  upon  proof  of  successful  completion  of  the  CME
coursework.
SECOND: Ms. Leach.
VOTE: The following Committee members voted in favor of the motion: Dr. Beyer,
Dr. Gillard, Dr. Artz and Ms. Bain. The following Committee members were absent:
Ms. Bain and Dr. Krahn.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

GENERAL BUSINESS

G.  DISCUSSION REGARDING DEBRIEFING ON COMMITTEE PROCESSES

No discussion.

H.  ADJOURNMENT

MOTION: Dr. Gillard moved for adjournment.
SECOND: Dr. Artz.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Beyer,  Dr.
Gillard,  Dr.  Artz  and  Ms.  Bain.  The  following  Committee  members  were  absent:  Ms.  Bain
and Dr. Krahn.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

The meeting adjourned at 4:41 p.m.

Raquel Rivera, Executive Director

Draft Minutes for the October 8, 2025 AMB Committee B Meeting
Page 2 of 2

---

### 2025-10-06 — Arizona Medical Board — October 06, 2025

**[MINUTES] 2025-10-06_MD_202511200839_d5cd07beb633420b8b531c86a9f42d87.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

DRAFT MINUTES FOR BOARD REVIEW COMMITTEE A MEETING
Held on Monday, October 6, 2025
1740 W. Adams St., Board Room A• Phoenix, Arizona

Committee Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.R., F.A.S.T.R.O.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.

GENERAL BUSINESS

A.  CALL TO ORDER

Chairman Figge called the Committee’s meeting to order at: 2:00 p.m.

B.  ROLL CALL

The following Committee members were present: Dr. Figge, Dr. Bethancourt, Ms. Dorrell and Dr.
Farmer.

ALSO PRESENT
The  following  Board  staff  participated  in  the  meeting:  Nicole  Samaradellis,  Investigations
Manager  and  Michelle  Robles,  Board  Operations  Manager.  Seth  Hargraves,  Assistant  Attorney
General (“AAG”) was also present.

C.  OPENING STATEMENTS

D.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA –
No individuals addressed the Committee during the Public Statements portion of the meeting.

E.  APPROVAL OF MINUTES

•  August 6, 2025 Review Committee A Minutes

MOTION:  Dr.  Farmer  moved  to  approve  the  August  6,  2025  Review  Committee  A
Minutes.
SECOND: Ms. Dorrell.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge, Dr.
Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

CONSENT AGENDA

F.  APPROVAL OF DRAFT FINDINGS OF FACT, CONCLUSIONS OF LAW AND

ORDER

1.  MD-23-0494A, HERAMB K. SINGH, M.D., LIC. #55413

Counsel Steven Long was present on behalf of the physician.

Dr. Farmer noted that  the  discussion reflected all of the violations  identified  by  SIRC to
include  A.R.S.  §§  32-1401(27)(e),  (r)  and  (kk)  violations  however,  the  A.R.S.  §  32-
1401(27)(e) violation got left out of the motion.

Mr. Hargraves stated that staff went over the audio and found that the motion was to find
violations of A.R.S. §§ 32-1401(27)(r) and (kk), but the CME order is geared towards the
A.R.S.  §  32-1401(27)(e)  violation.  Mr.  Hargraves  stated  that  if  the  intent  was  to  include
the A.R.S. § 32-1401(27)(e) violation, there needs to be a motion to add it.

MOTION: Dr. Farmer moved to add the e violation to the Order.
SECOND: Ms. Dorrell
Mr.  Long  stated  that  from  the  physician’s  and  counsel’s  perspective  they  thought  the
A.R.S. § 32-1401(27)(e) violation was removed due to the physician’s inability to review
the  records  due  to  difficulty  contacting  the  other  party  that  holds  the  remainder  of  the
medical records.

Dr.  Bethancourt  noted  that  A.R.S.  §§  32-1401(27)(r)  and  (kk)  violation  was  all  that  was
voted  on.  Dr.  Farmer  commented  that  the  discussion  and  the  intent  was  to  include  the
A.R.S. § 32-1401(27)(e) violation as he was the one  who  made the motion.  Dr.  Farmer
opined that the records violation is supported.

Mr.  Hargraves  clarified  that  the  issue  is  that  the  CME  that  was  ordered  is  directed
towards  record  keeping  and  it  doesn’t  make  sense  without  the  A.R.S.  §  32-1401(27)(e)
violation.

Dr.  Farmer  agreed  that  the  CME  doesn’t  make  sense  without  the  records  violation
included. Dr. Figge noted that including the violation doesn’t change the final Order.

Mr.  Long  confirmed  that  once  the  order  is  filed  the  physician  intends  to  complete  the
CME.

Dr.  Figge  noted  that  including  the  violation  makes  the  most  sense  with  the  CME  order,
especially given that the physician is already aware of the CME and intends to complete
it once an order is given.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge,
Dr. Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

MOTION: Dr. Farmer moved to approve the draft Findings of Fact, Conclusions of
Law  and  Order  for  a  Letter  of  Reprimand  and  Probation  with  the  correction  that
just passed. Within six months, complete no less than 10 hours of Board staff pre-
approved  Category  l  CME  in  an  intensive,  in-person/virtual  course  regarding
medical recordkeeping. The CME hours  shall be in addition to the hours required
for  license  renewal.  The  Probation  shall  terminate  upon  proof  of  successful
completion of the CME coursework.
SECOND: Dr. Bethancourt.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge,
Dr. Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

2.  MD-22-0334A, RALPH E. MAYBERRY, M.D., LIC. #16890

MOTION:  Dr.  Bethancourt  moved  to  approve  the  draft  Findings  of  Fact,
Conclusions of Law and Order for a Letter of Reprimand and Probation. Within six
months,  complete  no  less  than  10  hours  of  Board  staff  pre-approved  Category  l
CME  in  an  intensive,  in-person  course  regarding  medical  recordkeeping;  and
complete no less than 15 hours of Board staff pre-approved Category l CME in an

Draft Minutes for the October 6, 2025 AMB Committee A Meeting
Page 2 of 3

intensive, in-person  course  regarding  controlled substance prescribing. The CME
hours shall be in addition to the hours required for license renewal. The Probation
shall terminate upon proof of successful completion of the CME coursework.
SECOND: Dr. Farmer.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge,
Dr. Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

GENERAL BUSINESS

G.  DISCUSSION REGARDING DEBRIEFING ON COMMITTEE PROCESSES

There was no discussion.

H.  ADJOURNMENT

MOTION: Dr. Farmer moved for adjournment.
SECOND: Ms. Dorrell.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

The meeting adjourned at 2:14 p.m.

Raquel Rivera, Executive Director

Draft Minutes for the October 6, 2025 AMB Committee A Meeting
Page 3 of 3

---

**[MINUTES] 2025-10-06_MD_202602251405_6a7f7d4519954c3aaf5d192232665e6b.pdf**

Arizona Medical Board and Arizona Regulatory Board
of Physician Assistants
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR THE BIANNUAL JOINT OFFICERS MEETING OF THE
ARIZONA MEDICAL BOARD AND ARIZONA REGULATORY BOARD OF
PHYSICIANS ASSISTANTS
Held on Monday, October 6, 2025
1740 W. Adams St., Board Room A • Phoenix, Arizona

Arizona Medical Board Officers
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary

Arizona Regulatory Board of Physician Assistants
Officers
Susan Reina, P.A.-C, Chair
John J. Shaff, PA-C, D.F.A.A.P.A., Vice-Chair

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at 8:00 a.m.

B.  ROLL CALL

The following Officers were present: Dr. Figge, Dr. Bethancourt and Ms. Dorrell.

The following Officers participated virtually: PA Reina.

The following Officer was absent: PA Shaff.

ALSO PRESENT

The following Board staff were present: Raquel Rivera, Executive Director; Nicole Samaradellis,
Investigations  Manager;  and  Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,
Assistant Attorney General (“AAG”) were also present.

C.  CALL TO THE PUBLIC –7:55 a.m.

No individuals addressed the Officers during Public Statements portion of the meeting.

D.  DISCUSSION REGARDING NEXT JOINT OFFICERS’ MEETING

•  Discussion of Dates for Future Meeting

Board staff informed the Officers that an agenda with proposed dates will be provided
later this year.

Dr. Figge acknowledged Physician Assistant’s Week.

•  Discussion of Topics for Future Meeting

E.  ADJOURNMENT

MOTION: PA Reina moved to adjourn.
SECOND: Dr. Bethancourt.
VOTE: The following Officers voted in favor of the motion: Dr. Figge, Dr. Bethancourt, Ms.
Dorrell and PA Reina. The Officer was absent: PA Shaff.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.
MOTION PASSED.

The meeting adjourned at 8:02 a.m.

Raquel Rivera, Executive Director

Final Minutes for the October 6, 2025 Biannual Joint Officers Meeting of the AMB & ARBoPA
Page 2 of 2

---

**[MINUTES] 2025-10-06_MD_202602051014_dfed6710b97c45d28e6234a289c72445.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR REGULAR SESSION MEETING
Held on Monday, October 6, 2025
1740 W. Adams St., Board Room A • Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Lois E. Krahn, M.D
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 8:02 a.m.

B.  ROLL CALL

The following Board members were present: Dr. Figge, Dr. Bethancourt, Ms. Dorrell, Dr. Beyer and
Dr. Gillard.

The following Board members participated virtually: Dr. Krahn and Dr. Farmer.

The following Board members were absent: Dr. Artz, Ms. Bain and Ms. Leach.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps,  M.D.,  Chief  Medical  Consultant;  Nicole  Samaradellis,  Investigations  Manager;  and
Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,  Assistant  Attorney  General  (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT
•  2024 CSPMP Annual Report

Ms. Rivera noted highlights of the report for the Board.

•  ARBoPA Sunset Audit Report

Ms. Rivera provided the PA Sunset Audit Report for review and consideration.

•  AMB Sunset Audit Status Update

Ms. Rivera provided an update on the current audit and stated that she will follow up with
any findings at the November meeting.

•  Update on AMB Draft Newsletter - October 2025

Ms. Rivera provided the draft newsletter for review which includes relevant topics the Board
has encountered since the last newsletter. Ms. Rivera noted that staff may add a quiz to
next year’s newsletter to obtain future topics from physicians.

Dr. Figge  opined that Ms.  Rivera did a good job on the newsletter, especially regarding
rulemaking.

E.  CHAIR’S REPORT
No report was given.

F.  LEGAL ADVISOR’S REPORT
•  Legislative Update

Ms. Smith provided an update for the Board’s review. Ms. Smith highlighted that SB1395
passed, which changed the minimum licensure requirements for graduates for unapproved
schools of medicine.  Previously, applicants had to complete an additional 24 months  of
training  at  an  approved  program,  now  applicants  are  only  required  to  be  enrolled  in  an
approved  program.  There  has  also  been  a  change  in  the  scope  of  practice  for  medical
assistants that allows an appropriately trained MA to place and remove urinary catheters
while  under  the  general  supervision  of  an  appropriate  supervisor.  Ms.  Smith  also
highlighted  that  there  is  a  change  in  the  way  the  Board  will  review  initial  licensure
applications.  HB2173  prohibits  agencies  from  including  questions  on  applications  that
request information on whether the received a mental heath diagnosis or sought mental
health treatment. Additionally, if an applicant is in a monitoring agreement in another state
that is confidential, they do not have to disclose that information.

Dr. Farmer inquired about a legal issue that was sent via email.

Ms. Smith noted that the matter is not agendized and she will contact Board members.

G.  PHYSICIAN HEALTH PROGRAM (PHP) REPORT

Ms. Downey provided a report for the Board’s review. Ms. Downey noted that staff has requested
a  PHP  committee  meeting  soon  and  that  the  Mayo  clinic  has  provided  information  for  the
Committee’s  consideration.  Staff  would  like  to  add  the  Federation  of  State  Physician  Health
Programs (FSPHP) video to the Board’s website and send an email to licensees. On October 3,
2025, the Executive Director, PHP Manager, and the Board’s PHP Assessors attended the 2025
Wellbeing Summit. Ms. Downey informed the Board that the FSPHP will be holding its education
conference  and  annual  meeting  from  April  29  to  May  2,  2026  in  Baltimore,  Maryland.  Board
members may consider attending to learn about the essentials of physician health programs and
healthcare professional treatment. Interested Board members may contact the Executive Director
for more information. Ms. Downey noted that there has been an agenda change for PHP matters
which has received positive feedback.

H.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Dr. Figge commented on the frustration regarding obtaining a quorum to hold meetings and waiting
on new assignments.

I.  APPROVAL OF MINUTES

•  September 3, 2025 Special Teleconference
•  September 17, 2025 Summary Action

MOTION:  Dr.  Bethancourt  moved  to  approve  the  September  3,  2025  Special
Teleconference Meeting, and the September 17, 2025 Summary Action Meeting.
SECOND: Dr. Gillard.

Final  Minutes for the October 6, 2025 AMB Regular Session Meeting
Page 2 of 20

VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Beyer, Dr. Farmer, Dr. Gillard and Dr. Krahn.
The following Board members were absent: Dr. Artz, Ms. Bain and Ms. Leach.
VOTE: 7-yay, 0-nay, 0 (Dr. Krahn abstained from the September 17th minutes)-abstain, 0-
recuse, 3-absent.
MOTION PASSED.

LEGAL MATTERS

J.  DISCUSSION, CONSIDERATION AND POSSIBLE ACTION ON SETTLEMENT

OFFER IN LIEU OF FORMAL HEARING

1.  MD-25-0012A, LAURA HARRINGTON, M.D., LIC. #24671

Counsel Melissa Cuddington was present on behalf of the physician. Carrie Smith, AAG
was  present  on  behalf  of  the  state.  Deannie  Reh,  AAG  was  present  as  the  Board’s
Independent Legal Advisor.

Ms. Cuddington requested executive session to discuss confidential matters.

MOTION: Dr. Farmer moved for the Board to enter into Executive Session pursuant
to A.R.S. § 32-431.03(A)(2) to discuss confidential matters.
SECOND: Dr. Krahn.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Beyer, Dr. Farmer, Dr. Gillard and Ms. Leach.
The following Board members were absent: Dr. Artz, Ms. Bain and Dr. Krahn.
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

The Board entered into Executive Session at 8:47 a.m.
The Board returned to Open Session at 9:05 a.m.
No legal action was taken by the Board during Executive Session.

Ms.  Cuddington  requested  that  the  Board  approve  the  alternative  treatment  solution  as
discussed in executive session. Ms. Cuddington noted that the Board investigation is not
complete and further requested that the matter be tabled for 60 days.

Ms. Smith agreed that continuance is appropriate. The medical records were provided, and
the Medical Consultant (“MC”) has issued a supplemental report that the physician has not
had an opportunity to respond to. Ms. Smith noted that the Board is aware of their stance
on the alternative treatment option requested by the physician given in executive session.
Ms. Smith stated that she is willing to be guided by the Board’s direction in this case.

MOTION:  Dr.  Krahn  moved  to  reject  the  settlement  proposal  regarding  alternative
outpatient program because it does not meet the Board’s requirements.
SECOND: Dr. Farmer.
Dr. Gillard inquired whether tabling the matter would affect the case.

Ms.  Reh  stated  that  if  the  Board  rejects  the  proposal,  it  would  not  be  tabling  for  further
investigation.

Dr. Figge asked for clarification of whether the case would move towards formal hearing if
the  Board  rejected  the  settlement  proposal.  Dr.  Krahn  stated  that  her  motion  was  only
intended to address the request to approve the alternative treatment solution. Dr. Beyer
stated that he understands where Dr. Krahn is coming from but spoke against the motion.
Dr. Beyer agreed that the recommended treatment program is better than the proposed
alternate, but commented that other things happening in Dr. Harrington’s life which may
make it a better fit for her recovery. Dr. Krahn expressed concern that the recommended
treatment  and  alternative  proposal  are  very  different,  and  given  the  longstanding  and
serious issue, the standard of care would not be met by the alternate proposal.

Final  Minutes for the October 6, 2025 AMB Regular Session Meeting
Page 3 of 20

Ms. Cuddington clarified that the physician did select the evaluating provider.

Dr. Bethancourt inquired whether the matter could be tabled if the motion passes.

Ms. Smith clarified that the parties  are requesting for  the  Board  to approve  or deny the
alternative program, and to table the matter.

Dr. Krahn stated that her motion is for the treatment program specifically and leaves the
tabling  issue  to  another  motion.  Dr.  Farmer  stated  that  he  shares  sympathies  for  the
physician’s  situation,  but  the  kindest  thing  would  be  for  this  physician  to  complete  the
treatment- recommendations that would have the best outcome. Dr. Figge inquired whether
this matter would come back to the Board prior to the formal hearing.

Ms. Reh explained the current motion would not affect whether or not the Board tables the
matter in a separate motion. If tabled, the case would not go to a formal hearing at this
time.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Farmer, Dr. Gillard and Dr. Krahn. The following Board
member voted  against the motion: Dr. Beyer. The following Board members were
absent: Dr. Artz, Ms. Bain and Ms. Leach.
VOTE: 6-yay, 1-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

MOTION:  Dr.  Gillard  moved  to  continue  the  case  for  sixty  days  in  lieu  of  Formal
Hearing.
SECOND: Dr. Bethancourt
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt,  Ms.  Dorrell,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Dr.  Krahn.  The
following Board members were absent: Dr. Artz, Ms. Bain and Ms. Leach.
VOTE: 7-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

2.  MD-20-1000B, MD-24-0118A, MARK J. RUBIN, M.D., LIC. #28310

Dr. Rubin and counsel Callie Maxwell were present. Seth Hargraves, AAG was present on
behalf  of  the  State.  Deanie  Reh,  AAG  was  present  as  the  Board’s  Independent  Legal
Advisor.

Dr.  Rubin  stated  that  regarding  the  MD-20-1000B  matter,  all  the  care  he  provided  was
appropriate,  within  the  standard  of  the  care,  and  well  documented.  He  expressed  his
confusion  as  to  why  there  are  claims  of  inadequate  record  keeping  regarding  the  care
provided to the other doctor in this case. Dr. Rubin claims to have provided all requested
medical documents to the Board and subsequently never received a deficiency notice over
the years. As for the MD-24-0118A matter, Dr. Rubin stated that he was uninformed of the
law and that ignorance led to a criminal investigation. Dr. Rubin requested a second chance
to practice.

Ms. Maxwell clarified that their alternative proposal is that Dr. Rubin would not return to
clinical practice until December 2027, and the Board would grant Dr. Rubin’s request to
serve as a doctor in the Navy if given the opportunity. Dr. Rubin would also notify the Board
of any job offers that require an active medical license to ensure compliance. Ms. Maxwell
noted  that  Dr.  Rubin  would  also  accept  the  previous  consent  agreement  for  practice
restriction, probation, and completion of CME with the understanding that noncompliance
will result in revocation.

Mr.  Hargraves  summarized  that  MD-20-1000B  was  initiated  

*[document truncated for length]*

---

### 2025-09-22 — Arizona Medical Board — September 22, 2025

**[MINUTES] 2025-09-22_MD_202602191601_b6f7baef103f4215ba0af578435a0828.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR ADMINISTRATIVE JOINT LEGISLATION AND RULES
COMMITTEE TELECONFERENCE MEETING
Held on Monday, September 22, 2025
1740 W. Adams St., Phoenix, Arizona

Committee Members
Jodi A. Bain, M.A., J.D., LL.M., Chair
Katie S. Artz, M.D., M.S.
Bruce Bethancourt, M.D.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.

GENERAL BUSINESS

A.  CALL TO ORDER

Chairwoman Bain called the Committee’s meeting to order at: 5:04 p.m.

B.  ROLL CALL

The following Committee members participated virtually: Ms. Bain, Dr. Artz, Dr. Figge and Dr. Farmer.

The following Committee members were absent: Dr. Bethancourt and Ms. Dorrell.

The following  Board staff participated in the virtual  meeting:  Raquel Rivera,  Executive Director; and
Michelle Robles, Board Operations Manager. Carrie Smith, Assistant Attorney General (“AAG”) was
also present.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals  who  addressed  the  Committee  during  the  Public  Statements  portion  of  the  meeting  are
listed under the topic.

D.  REVIEW,  DISCUSSION  AND  POSSIBLE  RECOMMENDATION  REGARDING

AMB ALL MEETINGS CALENDAR
Ms.  Rivera  informed  the  Committee  that  the AMB  2025 All  Meeting  calendar  has  been  provided  for
your  review  and  reference.  This  will  be  placed  on  all  JLRC  agendas  going  forward.  Starting  in
November  2025,  the  2026  All  Meeting  Calendar  will  also  be  included.  Ms.  Rivera  requested  the
Committee’s  input  on  whether  the  calendars  should  be  included  under  the  ED  report  for  all  Board
meetings so Board members can quickly review and reference future meeting dates and advise staff
of any potential absences in advance of the meeting dates at the time of the Board meeting.

Board staff confirmed that the calendar can be updated as meetings are added.

Ms. Bain requested that the proposed dates for 2026 be circulated prior to the next meeting.

E.  REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATION REGARDING FIVE

YEAR REVIEW AND RULEMAKING CALENDAR

Ms.  Rivera  reported  that  a  draft  version  has  been  provided  for  the  Committee’s  review  and
consideration.    This  includes  a  5YRR  calendar  with  future  deadlines  and  monitoring
mechanisms such as color coding with red to indicate areas where action will be needed. The
2nd tab will include rulemaking and 5YRR details. Ms. Rivera stated she plans to review prior
5YRRs to ensure accurate historical information is added to the spreadsheet.

F.  FIVE YEAR REVIEW

1.  ARTICLE

2,

LICENSURE

-

REVIEW,

DISCUSSION

AND

POSSIBLE

RECOMMENDATIONS WITH DRAFT FIVE-YEAR REVIEW REPORT
Ms.  Rivera  reported  that  the  draft  Article  2  5YRR  has  been  provided  for  the  Committee’s
review incorporating the changes discussed at the last JLRC meeting. If approved, this will be
submitted  to  GRRC  for  their  consideration.  Additionally,  there  will  be  a  request  for
authorization to proceed from the Governor's Office pursuant to A.R.S. § 41-1039(A) for the
proposed rulemaking changes identified in the 5YRR with the plan to complete rulemaking by
June 2026.

G.  RULEMAKING

1.  ARTICLE  7,  OFFICE  BASED  SURGERY  -  REVIEW,  DISCUSSION  AND  UPDATE

REGARDING RULEMAKING STATUS
Ms. Rivera reported that as of this morning, the Governor’s Office reported that they would be
sending an approval email today for the Board’s Notice of Final Rulemaking related to Article
7 Office Based Surgery rules. Once received, Ms. Rivera will submit the information to GRRC
for  their  consideration  at  an  upcoming  study  session  and  council  meeting.  If  approved  at
GRRC, the Board would then file the rules with the Secretary of State to be published in the
Administrative Register.

H.  REVIEW,  DISCUSSION  AND  CONSIDERATION  OF  CHANGES  TO  MA  SCOPE

OF PRACTICE FAQS
Ms. Rivera reported that the 2025 Legislative Memo has been provided for review. HB 2025 expands
the  scope  of  practice  for  medical  assistants  to  allow  them  to  place  and  remove  urinary  catheters  if
they  are  appropriately  trained  and  working  under  the  ‘general  supervision’  of  a  physician,  nurse
practitioner,  clinical  nurse  specialist,  certified  nurse  midwife  or  physician  assistant  (approved
provider’).  “General supervision” is defined to mean that the procedure or service is under the overall
direction  and  control  of  an  approved  provider,  but  that  the  approved  provider  is  not  required  to  be
present during the procedure or service.  The law goes into effect on September 26, 2025. Based on
this change, Ms. Rivera requested that the JLRC consider changes to the MA FAQs which currently
indicate that MAs may not insert urinary catheters. A draft version with suggested language has been
provided for your review and input. If approved, the revised FAQs will be uploaded to the website. Ms.
Rivera reported that she will follow up on whether a rule is needed regarding the discussion that was
had under item I.

Ms. Smith confirmed that that the definition of General Supervision came from statute.

I.  REVIEW,  DISCUSSION  AND  CONSIDERATION  OF  MA  SCOPE  OF  PRACTICE

INQUIRIES
Dr. Huether and Dr. Hammon addressed the Committee during the Public Statements portion of the
meeting.

Ms. Rivera noted that the correspondence from physicians is provided for the committee’s reference
of their original inquires. Ms. Rivera noted that she obtained input from the ASA and AZNB based on
the Committee’s request. Ms. Rivera noted that she also received additional correspondence from the
Arizona Medical Association (ARMA) and The American College of Mohs Surgery (ACMS).

Dr. Farmer stated that when this inquiry first came up he was hesitant, but this is very different from
what was originally presented and is regarding something specific.

Final Minutes for the September 22, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 2 of 3

Committee  members  questioned  Dr.  Huether  regarding  possible  volumes  of  lidocaine  in  these
scenarios.

Dr. Farmer and Dr. Figge  opined that specific volumes mg/kg or cc’s should be listed. If carved out
specifically for lidocaine, Dr. Figge opined that this is reasonable.

Ms. Smith stated that the Board’s only enforceable method is if something is in statute or rule and that
FAQs  provide  information  only.  Ms.  Smith  noted  that  the  Board  is  currently  in  the  information
gathering stage.

Dr. Farmer commented that the specificity of the request makes it very clear going forward. It is our
job now to figure out the legalities on how to make it happen.

Ms.  Smith  confirmed  that  the  Board  would  need  to  engage  in  the  normal  rulemaking  process  since
MAs can administer injections in statute already.

Dr.  Tournas  addressed  the  Committee  regarding  injections  and  noted  that  his  company’s  legal
department is taking the Board’s FAQs as rules to go by. Commented that the restriction about any
anesthetic agent is not found in rules and statutes but layered in the FAQ. Questioned, can the FAQs
be modified.

Ms.  Smith  stated  that  these  FAQs  have  been  around  for  a  while  and  there  have  been  attempts  to
modify them from time to time. Ms. Smith noted that since this has to do with practice issues and not
legal issues, this has been mainly a practice -guided and physician-guided process. Ms. Smith further
explained  how  MAs  putting  in  catheters  was  not  in  statute  so  stakeholders  requesting  this  were
directed towards the legislature. In this case, it’s different because administering injections is already
in  statute.  The  Board  has  authority  to  interpret  its  statute  and  the  clearest  possible  way  to  do  that
would be through the rulemaking process.

Dr. Tournas further clarified that they are requesting that the FAQs not include prohibiting it.

Dr. Farmer opined that this is not a standard of care problem, and that it is somewhat urgent because
this  is  happening  in  the  real  world  and  we  want  to  keep  things  within  safe  parameters.  Dr.  Farmer
requested an expeditious path forward and offered to help craft language.

J.  DISCUSSION OF FUTURE TOPICS

Ms. Rivera suggested discussion of the PA Audit as some findings are related to the AMB.

Ms. Bain requested a list of programs the Board has in place that may be helpful to avoid confusion
regarding programs in place, for example the PHP, at a future meeting.

K.  ADJOURNMENT

MOTION: Dr. Figge moved for adjournment.
SECOND:  Dr. Farmer.
VOTE: The following Board members voted in favor of the motion:
The following Board member was absent: Ms. Dorrell and Dr. Bethancourt.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.

The meeting adjourned at: 6:10 p.m.

Raquel Rivera, Executive Director

Final Minutes for the September 22, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 3 of 3

---

### 2025-09-17 — Arizona Medical Board — September 17, 2025

**[MINUTES] 2025-09-17_MD_202510071258_18ccd4b863a942e486222897b3f98e31.pdf**

ARIZONA MEDICAL BOARD
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SUMMARY ACTION TELECONFERENCE MEETING
Held on September 17, 2025
1740 W. Adams St., Board Room 4100 • Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Lois E. Krahn, M.D
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 4:44 p.m.

B.  ROLL CALL

The following Board members participated virtually: Dr. Figge, Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Beyer, Dr. Farmer,
Dr. Gillard and Ms. Leach.

The following Board members were absent: Dr. Bethancourt and Dr. Krahn.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude Deschamps, M.D.,
Chief Medical Consultant;  Nicole Samaradellis, Investigations Manager;  and Michelle Robles, Board Operations
Manager. Carrie Smith, Assistant Attorney General (“AAG”) also participated in the meeting.

C.  CALL TO THE PUBLIC

No individuals addressed the Board during the Public Statements portion of the meeting.

LEGAL MATTERS

D.  REVIEW, DISCUSSION AND POSSIBLE ACTION REGARDING SUMMARY ACTION

1.  MD-25-0059A, RICHARD R. WARRINGTON, M.D., LIC. #19666

Dr. Warrington was not present.

Board  staff  summarized  that  the  Board  initiated  case  number  MD-25-0059A  based  on  Dr.  Warrington’s
October 2024, medical license renewal application indicating he had a medical condition that could impair
his ability to practice medicine.  Dr. Warrington indicated that he was not currently practicing but hoped to
return  to  practice  if  and  when  the  medical  condition  improved.    Medical  records  from  March  28,  2024,
indicate Dr. Warrington was experiencing symptoms that would impair his ability to safely practice medicine.
Dr.  Warrington’s  medical  records  also  indicate  he  was  terminated  from  employment  in  2016  and  2019.
Board staff requested a response from Dr. Warrington.  Dr. Warrington has not provided a response to his

initial Notice Letter nor subsequent Re-Notice Letter, emails or voicemails.  As a result, Board staff offered
Dr. Warrington an Interim Consent Agreement for Practice Restriction, but he has not provided Board staff
with  a  signed  copy.    Board  staff  sent  the  Interim  Consent  Agreement  for  Practice  Restriction  to  Dr.
Warrington via email and FedEx. As of today’s date, Dr. Warrington has not provided any response. Board
staff is concerned that Dr. Warrington’s health condition impairs his ability to safely practice medicine and
he has not responded to multiple requests for contact. Therefore, this case is before the Board to consider
the summary suspension of Dr. Richard Warrington’s medical license.

Dr. Gillard inquired if there was a signed receipt from FedEX.

Board staff stated that they requested a signature for receipt but FedEx did not obtain a signature upon
delivery.

Ms. Smith clarified that FedEx did confirm delivery, but did not obtain a signature. Ms. Smith stated that
there is proof that the Interim Practice Restriction was delivered, and opined that this is sufficient.

Dr. Beyer inquired if he has not been practicing since 2019.

Board staff stated that there is documentation that he was employed in 2021 but nothing since.

MOTION: Dr. Beyer moved to summarily suspend Dr. Warrington’s license pending the outcome of
a  formal  hearing  in  this  matter  based  on  a  finding  that  the  public  health  safety  and  welfare
imperatively requires emergency action.
SECOND: Ms. Leach.
Dr. Beyer commented that it is unfortunate that a medical condition is affecting his ability to practice but it
does pose a risk, including the gaps in practice this is warranted. Dr. Artz opined that Board staff did try to
communicate  and  get  ahold  of  the  physician  and  he  has  not  responded.  Dr.  Figge  agreed  that  the
physician’s actions deem him unregulable. Dr. Gillard noted that there is a statute that states that physicians
must keep their contact information up to date. Dr. Figge noted that there was at lease one letter that he
signed for certified mail.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Ms. Dorrell, Dr. Artz,
Ms.  Bain,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Ms.  Leach.  The  following  Board  members  were
absent: Dr. Bethancourt and Dr. Krahn.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

E.  ADJOURNMENT

MOTION: Dr. Gillard moved for adjournment.
SECOND: Ms. Leach.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Ms. Dorrell, Dr. Artz, Ms. Bain,
Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard  and  Ms.  Leach.  The  following  Board  members  were  absent:  Dr.
Bethancourt and Dr. Krahn.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

The meeting was adjourned at 4:58 p.m.

Raquel Rivera, Executive Director

Final Minutes for the September 17, 2025 AMB Summary Action Teleconference Meeting
Page 2 of 2

---

### 2025-09-03 — Arizona Medical Board — September 03, 2025

**[MINUTES] 2025-09-03_MD_202510071258_aa76c6a42dfc4d0f97c99d2837612003.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SPECIAL TELECONFERENCE MEETING
Held on Wednesday, September 3, 2025
1740 W. Adams St., Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Lois E. Krahn, M.D
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 5:03 p.m.

B.  ROLL CALL

The following Board members were present: Dr. Figge, Dr. Beyer, Dr. Bethancourt, Ms. Dorrell, Dr.
Artz, Ms. Bain, Dr. Farmer, Dr. Gillard, Dr. Krahn, and Ms. Leach.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps,  M.D.,  Chief  Medical  Consultant;  Nicole  Samaradellis,  Investigations  Manager;  and
Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,  Assistant  Attorney  General  (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT

•  Review, Discussion and Consideration of FSMB Training - Trauma Informed Investigation

Ms. Rivera informed the Board that the FSMB is hosting a Trauma Informed Regulation
training  in  February  2026  in  New  Orleans  focusing  on  integrating  trauma-informed
practices into medical regulation. Two representatives from the Board, one Board member
and one Senior Staff may attend on scholarship to cover travel, lodging, and meals. The
deadline to register is in January; however, the scholarships may not be available by that
time. Ms. Rivera noted that if Board members are interested, please reach out to Dr. Figge
or Alicia.

•  Review, Discussion, and Consideration of Annual Report

Ms. Rivera reported that the Annual Report for the MD Board has been provided for your
review. We have revitalized the report, with a refreshed visual design aimed at improving
readability,  accessibility,  and  overall  engagement.  Along  with  our  updated  logos  and
content, the new format reflects our ongoing efforts to communicate more effectively with
stakeholders and the public.

•  Review, Discussion and Consideration of FY27 Executive Budget Package

Ms. Rivera reported that the strategic plan has been provided for the Board’s review. There
are  4  issues  identified  in  the  Board’s  5  year  plan.  One  is  to  investigate  and  resolve
complaints within 180 days. For FY27, we are requesting additional funding to obtain three
investigative  aides  to  offset  the  administrative  burden  for  Investigators  to  allow  them  to
move cases more efficiently. The Nursing Board who has more licensees and complaints
opened utilized legal secretaries to perform the duties we are proposing these aides would
perform. The second issue is to improve data retrieval tools and access to Board data. The
third  issue  is  to  continue  to  cooperate  with  agency  partners  to  disseminate  healthcare
related data. The fourth issue is to modernization of Agency public facing websites. For
FY27, we are requesting additional funding to modernize the MD/PA websites. Ms. Rivera
noted that the Budget Book contains the detailed requests for funding for the 2 items stated.

Dr. Figge commented that he liked the readability of the report.

E.  CHAIR’S REPORT
No report was given.

F.  LEGAL ADVISOR’S REPORT

•  Update on Mady v. Arizona Medical Board, LC2025-000219-001

Ms. Smith  provided  the Board with the Motion to Stay that's  been filed  and  the  Board’s
response. The reply was just filed yesterday evening, so the judge has not ruled on that
yet. The next steps in the case would be the judge's ruling on the Motion to Stay, and then
the briefing on the JRA.

G.  PHYSICIAN HEALTH PROGRAM (PHP) REPORT

Ms. Downey provided a report for the Board’s review.

H.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Dr. Figge inquired about a script regarding item P for future use.

Ms. Smith confirmed that there is a script.

I.  APPROVAL OF MINUTES

July 9, 2025 Special Teleconference meeting; including Executive Session

•
•  August 6, 2025 Regular Session meeting; including Executive Session

MOTION:  Dr.  Artz  moved  to  approve  the  July  9,  2025  Special  Teleconference
Meeting,  including  Executive  Session  and  the  August  6,  2025  Regular  Session
Meeting; including Executive Session.
SECOND: Dr. Bethancourt.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Beyer, Dr. Bethancourt,  Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Farmer, Dr. Gillard, Dr.
Krahn, and Ms. Leach.
VOTE: 10-yay, 0-nay, 0-abstain, 0(Dr. Krahn and Ms. Bain recused from the August
minutes)-recuse, 0-absent.

Final Minutes for the September 3, 2025 AMB Special Teleconference Meeting
Page 2 of 9

MOTION PASSED

LEGAL MATTERS

J.  DISCUSSION, CONSIDERATION AND POSSIBLE ACTION ON SETTLEMENT

OFFER IN LIEU OF FORMAL HEARING

1.  MD-25-0657A, SCOTT M. BRANNAN, M.D., LIC. #45866

Dr.  Brannan  and  counsel  Adam  Anderson  participated  virtually.  Seth  Hargraves,  AAG
participated on behalf of the State. Deanie Reh, AAG participated virtually as the Board’s
Independent Legal Advisor.

Mr. Anderson stated that Dr. Brannan’s license has been summarily suspended and was
not able to respond due to medical concerns. He then obtained counsel and has signed an
Inactive with Cause agreement.

Dr. Brannan apologized for not responding to the Board due to health issues and has since
contacted  his  attorney.  Dr.  Brannan  requested  that  the  Board  accept  his  Inactive  with
Cause.

Mr. Hargraves stated that on July 9th the Board considered this matter. A complaint had
been  received  in  June  regarding  Dr.  Brannan’s  ability  to  safely  practice  medicine.  Dr.
Brannan previously participated in a PHP agreement with this Board and statute required
him  to  enter  into  an  Inactive  with  Cause  if  there  was  another  event.  Dr.  Brannan  was
summarily suspended since he did not enter into the  Inactive with Case. Mr. Hargraves
requested that the Board accept the Inactive with Cause and rescind the referral to formal
hearing.

Dr. Gillard opined that this protects the public and noted that the physician cannot practice
until the Board allows it.

MOTION: Dr. Gillard moved to accept the Inactive with Cause and rescind the referral
to formal hearing.
SECOND: Dr. Bethancourt.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Beyer, Dr. Bethancourt,  Ms. Dorrell, Dr. Artz, Ms. Bain, Dr. Farmer, Dr. Gillard, Dr.
Krahn, and Ms. Leach.
VOTE: 10-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

CONSENT AGENDA

K.  CASES RECOMMENDED FOR DISMISSAL

MOTION: Dr. Bethancourt moved to dismiss item numbers 1-3.
SECOND: Dr. Gillard.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Dr. Beyer, Dr.
Bethancourt,  Ms.  Dorrell,  Dr.  Artz,  Ms.  Bain,  Dr.  Farmer,  Dr.  Gillard,  Dr.  Krahn,  and  Ms.
Leach.
VOTE: 10-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

1.  MD-23-0861A, MOHAMED I. RAMADAN, M.D., LIC. #33565

RESOLUTION: Dismiss.

2.  MD-24-1234A, SCOTT D. BORUCHOV, M.D., LIC. #61528

RESOLUTION: Dismiss.

Final Minutes for the September 3, 2025 AMB Special Teleconference Meeting
Page 3 of 9

3.  MD-24-0828A, VISHAL S. SHAH, M.D., LIC. #55180

RESOLUTION: Dismiss.

L.  CASES RECOMMENDED FOR ADVISORY LETTERS

MOTION: Dr. Beyer moved to issue an Advisory Letter in item numbers 1, 2 and 4-7.
SECOND: Ms. Leach.
VOTE: The following Board members voted in favor of the motion: Dr. Figge, Dr. Beyer, Dr.
Bethancourt,  Ms.  Dorrell,  Dr.  Artz,  Ms.  Bain,  Dr.  Farmer,  Dr.  Gillard,  Dr.  Krahn,  and  Ms.
Leach.
VOTE: 10-yay, 0-nay, 0-abstain, 0 (Dr. Krahn recused from Case #6)-recuse, 0-absent.
MOTION PASSED.

1.  MD-23-0713A, DAX K. TRUJILLO, M.D., LIC. #31549

RESOLUTION: Advisory Letter for failing to investigate a possible false positive on
a urinary drug  screen. While there is insufficient  evidence to  support disciplinary
action,  the  board  believes  that  continuation  of  the  activities  that  led  to  the
investigation may result in further board action against the licensee.

2.  MD-24-1000A, MICHAEL A. MUSCI, M.D., LIC. #36785

Dr. Musci and counsel Matthew Cates addressed the Board during the Public Statements
portion of the meeting.

RESOLUTION:  Advisory  Letter  for  misdiagnosing  a  patient  with  recurrent  breast
cancer  without  pathologic  confirmation.  While  the  licensee  has  demonstrated
substantial compliance through rehabilitation or remediation that has mitigated the
need for disciplinary action, the board believes that repetition of the activities that
led to the investigation may result in further board action against the licensee.

3.  MD-23-1149A, MAZIYAR A. KALANI, M.D., LIC. #55731

Dr.  Kalani  and  counsel  Tracy  Olsen  addressed  the  Board  during  the  Public  Statements
portion of the meeting.

Dr. Bethancourt commented he does not disagree with the advisory letter but noted that it
appears that the patient went to the ED because he perceived that he had a neurologic
problem that needed to be attended to, and he went to see a physician and repeatedly saw
a  PA.  Dr.  Bethancourt  questioned  whether  the  whole  pathology  was  explained
appropriately to the patient. Dr. Beyer opined that having four repetitive visits for the same
problem clearly said that this patient did not get the message. Dr. Beyer stated that it's our
job to make sure the patient understands what we can and cannot do. Dr. Beyer spoke in
favor of the recommended advisory letter.

MOTION: Dr. Bethencourt moved to issue an Advisory Letter for failing to evaluate
and communicate a treatment plan for a patient with non-emergent back pain and
neurologic  symptoms.  While  there  is  insufficient  evidence  to  support  disciplinary
action,  the  board  believes  that  continuation  of  the  activities  that  led  to  the
investigation may result in further board action against the licensee.
SECOND: Dr. Beyer.
Dr. Krahn commented that our PA colleagues were involved in this patient’s care and PAs
involved in neurosurgery tend to be highly skilled and the Board needs to recognize their
role in a situation like this. Dr. Krahn further commented that some patients, regardless of
who relays the information, will not understand or accept the message. Dr. Figge noted, as
an emergency physician, we do have certain patients that return multiple times with the
same  complaint,  and  one  of  the  most  common,  if  not  the  most  common,  of  returning
patients with same complaints is actually back pain.  Dr. Figge explained that you had to
check  the  CSPMP  for  back  pain  complaint  in  the  emergency  department  and  urgent
situations 100 percent of the time, because it was that common of a complaint. Dr. Figge
noted that the neurosurgical PA did see the patient and opined that the information was

Final Minutes for the September 3, 2025 AMB Special Teleconference Meeting
Page 4 of 9

review by the physician. The patient had a follow up appointment scheduled at the end of
the  month  to  see  the  neurosurgeon  but  the  situation  escalated.  On  the  fourth  visit  the
patient  left  the  emergency  department  and  didn’t  get  any  discharge  instructions,
medications  and  with  because  of  the  alleged  aggressive  behavior  with  staff  the
appointment was canceled. Dr. Figge stated that he can understand how this could happen
and  und

*[document truncated for length]*

---

### 2025-08-27 — Arizona Medical Board — August 27, 2025

**[MINUTES] 2025-08-27_MD_202508221111_d6b1c109e4bb493fa296ce808cb74e5f.pdf**

Arizona Medical Board and Arizona Regulatory Board
of Physician Assistants
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

NOTICE & AGENDA FOR THE BIANNUAL JOINT OFFICERS MEETING OF THE
ARIZONA MEDICAL BOARD AND ARIZONA REGULATORY BOARD OF
PHYSICIANS ASSISTANTS
Scheduled to begin at 9:55 a.m. on Wednesday, August 27, 2025
1740 W. Adams St., Board Room A • Phoenix, Arizona

Notice is hereby given to the general public and to the Officers of the Arizona Medical Board (“AMB”) and
Arizona Regulatory Board of Physician Assistants (“ARBOPA”) that the AMB and ARBOPA Officers will
hold a Meeting open to the public at the Board’s offices located at 1740 W. Adams St., Board Room A,
Phoenix, Arizona. A.R.S. § 38-431.02. The AMB and ARBOPA Officers, upon a majority vote of a quorum
of the members, may hold an Executive Session on any of the listed agenda items to obtain legal advice.
A.R.S. § 38-431.03(A)(3).

The AMB and ARBOPA reserve the right to change the order of items on the agenda, except for matters
set for a specific time.

Americans  with  Disabilities  Act:  Person  with  disabilities  may  request  reasonable  accommodations  by
contacting Michelle Butler at (480) 551-2714. Requests should be made as early as possible to allow time
to arrange the accommodation.

THE AMB AND ARBOPA WILL CONSIDER, DISCUSS AND MAY TAKE ACTION ON ANY AGENDA
ITEM

Arizona Medical Board Officers
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary

Arizona Regulatory Board of Physician Assistants
Officers
Susan Reina, P.A.-C, Chair
John J. Shaff, PA-C, D.F.A.A.P.A., Vice-Chair

If you need to speak to a member of Board staff regarding agenda items,
please contact the Board Coordinator at (480) 551-2734.

GENERAL BUSINESS

A.  CALL TO ORDER – 9:55 a.m.

Gary R. Figge, M.D., Chair

B.  ROLL CALL

Susan Reina, P.A.-C, ARBoPA Chair

C.  CALL TO THE PUBLIC –9:55 a.m.
Those  wishing  to  address  the  Board  need  not  request  permission  in  advance;  however,  the  Board  may  limit
those  persons  speaking  during  the  “Call  to  the  Public”  at  three  (3)  per  side  on  any  one  issue.  A.R.S.  §  38-
431.01(H).  The  Board  can  only  take  action  on  matters  listed  on  the  agenda  and  other  matters  related  thereto.
A.R.S. § 38-431.02(H). If appropriate, actions on public comment matters that are not listed on the agenda will
be limited to directing staff to study the matter or schedule the matter for further discussion at a later date. A.R.S.
§ 38-4301.01(H).

D.  APPROVAL OF MINUTES

•  December 4, 2024 Joint Officers’ Teleconference Meeting

E.  DISCUSSION REGARDING NEXT JOINT OFFICERS’ MEETING

•  Discussion of Dates for Future Meeting
•  Discussion of Topics for Future Meeting

F.  ADJOURNMENT

Raquel Rivera, Executive Director

Agenda for the August 27, 2025 Biannual Joint Officers Meeting of the AMB & ARBoPA
Page 2 of 3

Zoom Dial-In Information

Join Zoom Meeting
https://us02web.zoom.us/j/81957242396?pwd=sKlUbD5agIQ4EeToH4VKuXD4ufAgbb.

1

Meeting ID: 819 5724 2396
Passcode: 417282

---

One tap mobile
+16699006833,,81957242396#,,,,*417282# US (San Jose)
+17193594580,,81957242396#,,,,*417282# US

Join instructions
https://us02web.zoom.us/meetings/81957242396/invitations?signature=F1CxdCBNQ1k

Y5suDbxQR6XokJKk5W8jUH4T2M7jNF8Q

Agenda for the August 27, 2025 Biannual Joint Officers Meeting of the AMB & ARBoPA
Page 3 of 3

---

### 2025-08-26 — Arizona Medical Board — August 26, 2025

**[MINUTES] 2025-08-26_MD_202511060952_31f0dcbd126d417db886cde92556f753.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR ADMINISTRATIVE JOINT LEGISLATION AND RULES
COMMITTEE TELECONFERENCE MEETING
Held on Tuesday, August 26, 2025
1740 W. Adams St., Phoenix, Arizona

Committee Members
Jodi A. Bain, M.A., J.D., LL.M., Chair
Katie S. Artz, M.D., M.S.
Bruce Bethancourt, M.D.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.

GENERAL BUSINESS

A.  CALL TO ORDER

Chairwoman Bain called the Committee’s meeting to order at 4:11 p.m.

B.  ROLL CALL

The  following  Committee  members  participated  virtually:  Ms.  Bain,  Dr.  Bethancourt,  Dr.  Artz,  Ms.
Dorrell, Dr. Farmer and Dr. Figge.

The following Board staff participated in the virtual meeting: Raquel Rivera, Executive Director; Claude
Deschamps, Chief Medical Consultant and Michelle Robles, Board Operations Manager. Carrie Smith,
Assistant Attorney General (“AAG”) was also present.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

No individuals addressed the Committee during the Public Statements.

D.  REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATIONS REGARDING THE

ANNUAL REPORT
Ms. Rivera provided the draft annual report for the Committee’s review and noted the changes she has
made and what she has now included in the report.

Committee members approved of the new look.

Ms. Rivera noted that this is due September 2nd to the Governor’s office.

Ms. Bain stated that she has some feedback to provide prior to the submission.

E.  REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATION REGARDING THE

FY27 EXECUTIVE BUDGET PACKAGE
Ms.  Rivera  provided  the  package  for  the  Committee’s  review.  Ms.  Rivera  noted  that  it  includes  two
Decision Packages. Decision Package 1 is for modernization of websites and Decision Package 2 is to
request funding for three investigation aids. Ms. Rivera noted that the strategic issues the same with

the exception of adding Issue #4 to support the Board’s request for additional funding for modernization
of the MD/PA websites.

Dr. Figge noted that the report mentions one open public member spot but should note that there is an
open physician spot as well.

Ms. Brain inquired about the acronyms in the letter and if the Governor’s office knows what they mean.

Ms.  Rivera  confirmed  that  they  know  what  the  terms  are.  Ms.  Rivera  confirmed  that  these  decision
packages reflect where the Board is at now. The websites need to be updated and there will always be
a need for additional investigators given the caseload.

F.  REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATION REGARDING FIVE

YEAR REVIEW AND RULEMAKING CALENDAR
Ms. Rivera reported that the calendar has been provided for review.

G.  FIVE YEAR REVIEW

1.  ARTICLE 2, LICENSURE - REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATIONS

WITH DRAFT FIVE-YEAR REVIEW REPORT
Ms.  Rivera  provided  the  draft  5  YRR  for  Article  2,  which  captured  the  proposed  changes
discussed  and  considered  in  the  last  meeting  based  on  statutory  changes  and  increased
efficiency. In reviewing the rules, Ms. Rivera noted that there are three additional items for the
Committee’s.  A.R.S. § 32-1403(A)(12) requires the Board to issue registrations to licensees
who  have  completed  residency  training  in  anesthesiology  to  administer  anesthesia  and
sedation in a dental office.  This bill included a rulemaking exemption for only the Dental Board;
however, the Board can pursue regular rulemaking, if we would like to more thoroughly verify
completion  of  residency  training.  To  date,  the  Board  has  received  and  approved  14
applications.  The  current  process  requires  that  the  physician  provide  an  attestation  of  their
completion of anesthesia residency training on their application. If a rule is created, the Board
could include a process to more thoroughly verify residency training, such as review of PGT
verifications.

Committee members agreed that since there have been no issues with the current process to
keep it as is.

Ms. Rivera noted that currently, if an MD or PA was issued an initial license over 3 months prior
and requests a duplicate license, we would require them to submit a duplicate license form with
the associated fees. Requests for duplicate licenses due to a name change, are provided free
of charge. Starting in November of 2025, a licensee will be able to print a PDF license certificate
and  wallet  card  from  their  Board  portal.  Eliminating  this  fee  should  have  a  small  economic
impact on the Board. In FY25, the Board obtained $750 through collection of duplicate license
fees. Ms. Rivera stated she is open to the Committee’s thoughts on whether this fee should be
eliminated. Ms. Rivera noted that the fee to request a duplicate license is $50.

Dr. Figge commented that licensees should not have to request a duplicate license if they can
print it off the website.

Ms. Rivera stated that staff can direct the to the website to print it for free or they can request
a duplicate for the $50 fee if they need it from the Board.

Committee members agreed with keeping the duplicate licensee request option available.

Ms. Bain requested that a column be added to the calendar regarding what is coming up or is
due next.

Ms.  Rivera  reported  that  when  the  Board  determines  a  change  is  needed  in  a  license
application  form,  the  detailed  description  of  application  form  information  in  the  rules  may
become  inconsistent  with  the  application  form.  Therefore,  other  boards  have  minimized  the

Final Minutes for the August 26, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 2 of 4

application details from their rules to prevent the rules being inconsistent with the application
by simply referencing the submittal of an application on the Board’s website. Ms. Rivera noted
that she provided the  Board of  Psychologists  Examiners Licensure rules as  an  example for
your reference. Ms. Rivera explained that she brought this forward more for the Committee’s
information since it appears other boards may be taking this route.

Ms. Bain commented that for historical purposes there was an attempt to put more detail to
limit the burden of having additional questions.

Ms.  Rivera  explained  that  she  thinks  the  current  process  is  appropriate  and  the  detail  but
brought it to the Committee for review and to see if there is any interest.

2.  ARTICLE 3, DISPENSING - REVIEW, DISCUSSION AND UPDATE ON STATUS OF FIVE-

YEAR REVIEW REPORT
Ms. Rivera reported that the Article 3 Five Year Review Report (YRR) was submitted to GRRC
on June 5, 2025 with no changes proposed. GRRC approved the 5YRR on August 5, 2025.

3.  ARTICLE 6, DISCIPLINARY ACTION - OFFICE BASED SURGERY - REVIEW, DISCUSSION

AND UPDATE REGARDING RULEMAKING CONSIDERATIONS
Ms. Rivera reported that the Article 6 Five Year Review Report (YRR) was submitted to GRRC
on April 28, 2025 with no changes proposed. GRRC approved the 5YRR on August 5, 2025.

H.  RULEMAKING

1.  ARTICLE  7,  OFFICE  BASED  SURGERY  -  REVIEW,  DISCUSSION  AND  UPDATE

REGARDING RULEMAKING STATUS
Ms. Rivera reported that she continues to follow-up with the Governor’s Office for approval to
proceed with the Notice of Final Rulemaking.

Ms. Bain requested updating the calendar  to  include  the  month  and date  of  approval and  if
there will be any or no rule making anticipated.

I.  REVIEW,  DISCUSSION  AND  CONSIDERATION  OF  MA  SCOPE  OF  PRACTICE

INQUIRIES
Ms. Rivera reported that the Board has received two inquiries from physicians relating to MA scope of
practice and a physician’s ability to delegate administration of local anesthetics. Due to the subsequent,
similar request received, requested the Committee’s input and opinion. Ms. Rivera noted that she has
also provided the Board’s current Medical Assistant FAQs, which clearly outline that an MA may not
inject anesthetic agents.

Committee  members  discussed  various  concerns  regarding  MAs  administering  local  anesthetics.
Committee members acknowledged Dr. Deschamps and Dr. McClain’s and noted that it gave insight
on how often this is already being done.

Ms. Smith noted for the record that Direct Supervision is defined by statute in A.R.S. § 32-1401 and
that in order to be appropriate direct supervision, they have to be within the same room or office suite.

Committee members requested that Board staff request opinions from the State Anesthesia Society
and the Nursing Board to obtain more information. Dr. Farmer clarified that staff should ask whether or
not MAs should be allowed to administer local anesthetics, and if so under what circumstances and
delineations.  For  the  Nursing  Board,  staff  should  ask  how  the  administration  of  local  anesthetics  is
regulated.

J.  DISCUSSION OF FUTURE TOPICS

Ms. Rivera requested that at the next meeting will bring back the MA’s scope of practice regarding local
anesthetics, ED annual evaluation, annual board member training and the annual COI disclosures.

Ms. Bain suggested an offsite meeting for training prior to the February meeting.

Final Minutes for the August 26, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 3 of 4

Ms. Rivera acknowledged that suggestion and will bring it to the next meeting. Ms. Rivera commented
that the PA Audit may be available by the next meeting for discussion.

Ms. Bain requested including the meeting calendar at every meeting.

K.  ADJOURNMENT

MOTION: Dr. Bethancourt moved for adjournment.
SECOND: Ms. Bain.
VOTE: The following Board members voted in favor of the motion: Ms. Bain, Dr. Bethancourt,
Dr. Artz, Dr. Farmer, Dr. Figge and Ms. Dorrell.
VOTE: 6-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.

The meeting adjourned at: 5:15 p.m.

Raquel Rivera, Executive Director

Final Minutes for the August 26, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 4 of 4

---

### 2025-08-06 — Arizona Medical Board — August 06, 2025

**[MINUTES] 2025-08-06_MD_202510071259_9ec00c437cf8475b94aa9c29604874b3.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR BOARD REVIEW COMMITTEE A MEETING
Held on Wednesday, August 6, 2025
1740 W. Adams St., Board Room B• Phoenix, Arizona

Committee Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.R., F.A.S.T.R.O.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.

GENERAL BUSINESS

A.  CALL TO ORDER

Chairman Figge called the Committee’s meeting to order at: 12:35 p.m.

B.  ROLL CALL

The following Committee members were present: Dr. Figge, Dr. Bethancourt, Ms. Dorrell and Dr.
Farmer.

ALSO PRESENT
The  following  Board  staff  participated  in  the  meeting:  Nicole  Samaradellis,  Investigations
Manager  and  Michelle  Robles,  Board  Operations  Manager.  Seth  Hargraves,  Assistant  Attorney
General (“AAG”) was also present.

C.  OPENING STATEMENTS

Chairman Figge read the civility policy for the record.

D.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals  who  addressed  the  Committee  during  the  Public  Statements  portion  of  the  meeting
will appear under the case.

E.  APPROVAL OF MINUTES

•

June 4, 2025 Review Committee A Minutes

MOTION:  Dr.  Bethancourt  moved  to  approve  the  June  4,  2025  Review  Committee  A
Minutes.
SECOND: Dr. Farmer.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge, Dr.
Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

LEGAL MATTERS

F.  FORMAL INTERVIEWS

1.  MD-23-0494A, HERAMB K. SINGH, M.D., LIC. #55413
Dr. Singh was present with Counsel Steven Long.

Board  Staff  summarized  that  the  Board  initiated  case  number  MD-23-0494A  after
receiving  notification  of  a  malpractice  settlement  regarding  Dr.  Singh’s  care  and
treatment  of  a  25-year-old  female  patient  (“AM”)  alleging  improper  performance  of  a
cervical  epidural  steroid  injection  resulting  in  right  foot  drop  and  right  upper  extremity
weakness.  On  December  18,  2020,  patient  AM  presented  to  Dr.  Singh’s  office  for
complaints of headaches, neck pain, low back pain, and right ankle pain. AM reported the
injuries  were  sustained  during  a  motor  vehicle  accident  in  November  2020.  After  an
exam, Dr. Singh administered lumbar trigger point injections and ordered a cervical and
lumbar MRI. On December 23, 2020, the cervical MRI demonstrated “straightening of the
spine  with  mild  levoscoliosis,  consistent  with  post-traumatic  muscle  spasm.  At  both  C4-
C5 and C5-C6, a posterior disc herniation with impingement on the thecal sac is noted,
along  with  mild  spinal  stenosis.  At  C6-C7,  there  is  severe  narrowing  of  the  right  neural
foramina with impingement of the right exiting C7  nerve root.” On January  5, 2021,  AM
underwent cervical epidural steroid injection (CESI) at C5-C6 and lumbar epidural steroid
injection  (LESI)  performed  by  Dr.  Singh.  The  “procedure  room  notes”  documented  that
the LESI went well, and that AM started to move following the needle placement for the
CESI,  despite  the  provider  instructing  her  to  not  move.  Post-procedure,  AM  reported
right-sided  numbness and  tingling.  An ice  pack was applied, and  AM was placed in the
patient waiting room for observation. AM requested that EMS be called for transfer to the
hospital.  AM  presented  to  University  Hospital  and  was  diagnosed  with  a  C2-T7
intramedullary hematoma. AM was noted to have 0/5 strength in the right upper extremity
and no sensation to the right side. AM was admitted to the ICU for intravenous steroids.
AM’s  hospital  course  was  complicated  by  a  code  blue  that  occurred  during  a  possible
seizure  or  vasovagal  response.  AM  was  discharged  with  outpatient  physical  therapy  on
January  13,  2021.  On  March  31,  2021,  AM  was  seen  by  a  physical  medicine  and
rehabilitation physician who noted that she was ambulatory with significant effort using a
front-wheeled walker and was still experiencing neuropathic pain with occasional electric
shock  sensations  to  the  right  upper  extremity.  The  Board’s  Medical  Consultant  (“MC”)
reviewed the case and determined that Dr. Singh deviated from the standard of care by
failing to timely recognize and address post-procedure complications. The MC stated that
the patient suffered a C2-C7 intramedullary hematoma because of the CESI resulting in
right  sided  hemiplegia  requiring  hospitalization.  The  MC  expressed  concern  that  the
patient was placed in the waiting room for observation and that the patient had to request
that  EMS  be  called.  The  MC  noted  that  there  was  not  an  actual  procedure  note  that
included  the  name  and  specific  spinal  levels  of  the  procedure,  type  of  anesthesia,  type
and  amount  of  medication,  evaluation  of  injection  site  and  focused  neurological  exam,
immediate  complications  with  treatment  and  outcome.  The  MC  also  noted  that  the
imaging  for  the  procedures  was  not  provided.  The  licensee  stated  that  the  patient  was
told not to move during the procedure but was uncooperative. He stated that the patient
was  immediately  transferred  to  the  hospital  and  discharged  from  the  hospital  after  two
weeks no longer requiring assistive devices for walking. SIRC recognized that Dr. Singh
blamed  the  complication  on  the  fact  that  the  patient  was  not  cooperative  and  moved
during  the  procedure.  However,  SIRC  noted  that  Dr.  Singh  did  not  provide  additional
documentation  and/or  the  requested  images  to  support  his  statements.  SIRC  also
discussed  the  MC’s  supplemental  report  wherein  it  was  noted  that  despite  Dr.  Singh’s
statement  that  the  patient  was  immediately  transported  to  the  hospital  and  was
discharged after two weeks without assistive devices needed, the MC expressed concern
that the patient was placed in the waiting room for observation and that the patient had to
request that EMS be called and the patient still required a walker until March 2021. SIRC
remained  troubled  by  the  false  statements  provided  by  Dr.  Singh  as  well  as  the  lack  of
documentation  and  images  noting  that  the  patient  suffered  a  C2-C7  intermedullary
hematoma  resulting  in  right-sided  hemiplegia  and  without  the  images,  the  Board  is
unable to fully investigate the care rendered.

Mr.  Long  provided  an  opening  statement  to  the  Committee,  where  he  clarified  that  the
patient was never put into a waiting room on her own and that she was in an exam room
with someone watching her for two hours after the procedure. Mr. Long stated that when
the patient continued to report pain and numbness, it was Dr. Singh who suggested that
she go to the hospital. Dr. Singh did not intend to misrepresent anything to the Board and

Final Minutes for the August 6, 2025 AMB Committee A Meeting
Page 2 of 8

acknowledges the medical records, not including the dosage, were an error and will not
happen again. Mr. Long requested dismissal in this case.

Dr.  Singh  stated  that  this  case  was  litigated  and  settled.  Mr.  Singh  informed  the
Committee that he was with the patient the whole time and that he does check in on his
patients regularly.

During questioning, Dr. Singh confirmed that he had a conversation with the patient pre-
operative,  and  he  had  staff  translate  the  risks  and  benefits.  Dr.  Singh  confirmed  that  a
consent form is signed every time they do a procedure. Dr. Singh noted that a lot of the
records  were  not  provided  by  CareFor,  who  is  the  keeper  of  the  records.  Dr.  Singh
explained that CareFor is an outpatient pain management clinic that he was covering. Dr.
Singh explained that he had met the patient before for a trigger point injection. Dr. Singh
confirmed that he evaluated the patient preoperatively  and that the  patient is  monitored
during  the  procedure  by  the  nurse.  Dr.  Singh  stated  that  images  were  taken,
unfortunately the images that he submitted in this record are totally black, not diagnostic.
Dr. Singh stated that for some patients they give fentanyl and versed to take the edge off
before  doing  the  procedure.  Dr.  Singh  stated  that  the  procedure  went  well  and  that  the
pain was relieved. Dr. Singh informed the Committee he completed the procedure under
fluoroscopy  with  a  local  anesthetic  given.  Dr.  Singh  described  the  needle  placement
when the patient jumped and that they asked her to stay still. When she could not sit still
he pulled the needle out. The patient then complained of numbness and pain. The nurse
took  her  vitals  and  they  were  stable  so  she  was  taken  to  the  recovery  room  for
observation.  Dr.  Singh  explained  that  he  called  the  ER  and  requested  imaging  for  the
patient.  The  patient  had  been  in  recovery  between  one  and  two  hours  and  he  did
examine the patient, but it was not documented.

Dr. Singh confirmed that there were records available during the pre-trial but that he was
not  able  to  obtain  records  from  the  attorney  who  represented  him  during  the  pre-trial
investigation and settlement. Dr. Singh noted that the insurance company recommended
that  he  settle  given  the  patient’s  young  age.  Dr.  Singh  confirmed  that  the  handwritten
incident report was written by him and acknowledged that he did inject the steroids after
the patient moved. Dr Singh agreed that if the patient was moving the needle placement
was incorrect and in hindsight continuing with the injection was not appropriate.

Mr. Long requested that the case be dismissed or at most an Advisory Letter be issued.

MOTION: Dr. Farmer moved for a finding of unprofessional conduct in violation of
A.R.S. § 32-1401(27), (r) and (kk).
SECOND: Dr. Bethancourt.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge,
Dr. Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

Dr. Farmer commented that the outcome was bad and very serious. Dr. Farmer agreed
that there is a mitigating factor of no prior board history however, the aggravating factors
outweigh this. The records are inaccurate and egregiously there are false and misleading
statements.  Dr.  Farmer  stated  that  the  discussion  regarding  the  procedure  was
inaccurate  and  there  is  scanty  records.  Dr.  Farmer  opined  that  if  there  were  mixed
reports  from  the  nurses  he  should  go  see  the  patient  himself.  Dr.  Farmer  found  it
egregious to make an injection on a patient who is moving and expressing discomfort. Dr.
Farmer  opined  that  given  the  disingenuous  responses  a  Decree  of  Censure  may  be
appropriate, but it is hard to prove given the lack of record.

MOTION:  Dr.  Farner  moved  for  a  draft  Findings  of  Fact,  Conclusions  of  Law  and
Order  for  a  Letter  of  Reprimand  and  Probation.  Within  six  months,  complete  no
less than 10 hours of Board staff pre-approved Category l CME in an intensive, in-
person/virtual course regarding medical recordkeeping. The CME hours shall be in

Final Minutes for the August 6, 2025 AMB Committee A Meeting
Page 3 of 8

addition  to  the  hours  required  for  license  renewal.  The  Probation  shall  terminate
upon proof of successful completion of the CME coursework.
SECOND: Dr. Bethancourt.
Dr.  Figge  agreed  given  the  retractions,  records  and  some  unsettling  comments  there  is
cause for concern.
VOTE: The following Committee members voted in favor of the motion: Dr. Figge,
Dr. Bethancourt, Ms. Dorrell and Dr. Farmer.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 0-absent.
MOTION PASSED.

G.  FORMAL INTERVIEWS

1.  MD-24-0721A, ROXANNE K. RICK, M.D., LI

*[document truncated for length]*

---

**[MINUTES] 2025-08-06_MD_202509041134_2b09bcad0f444b758cf10c21fc79a43a.pdf**

Arizona Medical Board
1740 W. Adams St., Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR REGULAR SESSION MEETING
Held on Wednesday, August 6, 2025
1740 W. Adams St., Board Room A • Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Lois E. Krahn, M.D
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 8:04 a.m.

B.  ROLL CALL

The following Board members were present: Dr. Figge, Dr. Bethancourt, Ms. Dorrell, Dr. Artz, Dr.
Farmer, Dr. Gillard and Ms. Leach.

The following Board member appeared virtually: Dr. Beyer.

The following Board members were absent: Ms. Bain and Dr. Krahn.

ALSO PRESENT
The following Board staff participated in the meeting: Raquel Rivera, Executive Director; Claude
Deschamps,  M.D.,  Chief  Medical  Consultant;  Nicole  Samaradellis,  Investigations  Manager;  and
Michelle  Robles,  Board  Operations  Manager.  Carrie  Smith,  Assistant Attorney  General  (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT

•  Review, Discussion and Consideration of CCME/PARS CME Passport

Ms.  Rivera  reported that  as  part  of  Dr.  Krahn’s  work  in  the  FSMB Accreditation  Review
Committee, she informed Ms. Rivera of ACCME PARS which is a repository for verified,
primary  source  physician  CME  completion  data.  This  is  a  web-based  portal  where
accredited  CME  providers  can  submit  data  about  their  educational  activities  and  the
physician learners who participate in them. We met with ACCME and have been provided
logins to review the system. This is a free service and no cost to the Board. The handout

ACCME  provided  outlines  that  over  10,000  MDs  are  already  in  their  system  with  CME
credit; of those 10,000 MDs they have earned over 875,000 CME credits and completed
over  21,500  CME  activities  in  PARS.  Ms.  Rivera  stated,  if  the  Board  is  agreeable,  she
would like to partner with ACCME and promote the CME Passport on the Board’s website
and newsletters to see if we can benefit from the services and eventually be able to more
efficiently audit CME compliance. Ms. Rivera confirmed that it is free for all physicians.

Dr. Figge opined that it would be important for physicians to sign up as the Board already
completes random audits of 20 percent of physicians.

•  Review, Discussion and Update on AMB Outreach Activities

Ms. Rivera reported that the Board continues to receive requests for presentations from
both boards. In July, Ms. Rivera and the PHP Manager did a PHP Presentation at BUMC
Phoenix to residents. BUMC Phoenix reported being one of the first medical schools in the
country  with  a  non-technical  curriculum  preparing  medical  students  for  issues  that  may
arise throughout their career. Staff may return for a presentation specific to investigations
and best practice when under board investigation.

•  Review, Discussion and Consideration of Annual ED Performance Evaluation

Ms. Rivera thanked the Board for selecting her as the Executive Director of the Board. As
part of this new role, she requested the Board’s input on instituting an annual evaluation of
my performance as the ED.  This was not something that was formalized in the past and it
would  be  beneficial  to  obtain  feedback  on  an  annual basis  for  continuous  improvement,
alignment, and accountability. Ms. Rivera provided two sample evaluation forms for review
and consideration.

Ms. Smith clarified that the ED Selection and Retention Committee has the authority to
make the decision on which plan.

Dr. Farmer congratulated Ms. Rivera on the position and noted that the Committee can
take input from the Board. Dr. Farmer opined that this is a good idea.

•  Report on Physician Health Program (PHP)

Ms. Rivera reported that in the future, Erinn Downey will be providing the PHP Updates to
the  Board.  The  PHP  is  a  Board  sponsored  program,  authorized  by  statute  to  assist
individuals who may be impaired due to the following: substance abuse, dependence, or
psychiatric, psychological or behavioral health disorders. The PHP guides the rehabilitation
of potentially impaired and impaired practitioners consistent with the needs of public safety.
A PHP Memo has been uploaded to the file for your review containing the # of individuals
in confidential monitoring. There are currently 50 licensees whose participation in the PHP
is public. The Board has two PHP Monitors, CBI and GRI. The Board utilized four Board
approved Assessors who perform PHP Assessments.

E.  CHAIR’S REPORT

•  Discussion regarding Board collaboration with physician stakeholders

Dr.  Figge  noted  that  the  Board  is  not  alone  when  it  comes  to  issues  coming  before  the
legislature and that other organizations are willing to collaborate with the Board.

•  Discussion regarding reports on PHP for Board meetings

Dr. Figge noted the FSMB webinar trainings which led to his suggestion of having a PHP
report every month so that the Board is aware of what is going on.

•  Discussion regarding aging physicians and physician use of marijuana

Final Minutes for the August 6, 2025 AMB Regular Session Meeting
Page 2 of 18

The  Board  discussed  various  issues  regarding  aging  physicians  and  physicians  using
marijuana.  The  Board  agreed  that  it  can  be  difficult  to  capture  and  evaluate  an  aging
physician’s  ability  to  safely  practice  and  that  things  regarding  licensure  is  a  legislative
issue. The Board agreed that these two topics need to be investigated further.

F.  LEGAL ADVISOR’S REPORT

No report was provided.

G.  DISCUSSION REGARDING DEBRIEFING ON BOARD PROCESSES

Board staff informed the Board of how the 411 is built but if there is a GLS update that may cause
issues, or it randomly stops working it is helpful when Board members are reviewing materials and
come across an issue they let staff know so that we can address it. Board staff further noted that
when it comes to old cases, we are limited to what documents are available and how they were
uploaded at that time.

H.  APPROVAL OF MINUTES

•  April 1, 2025 Regular Session, including Executive Session
•
June 4, 2025 Regular Session, including Executive Session

Dr.  Figge  noted  some  corrections  in  the  minutes.  He  and  Dr.  Farmer  were  recused  in  Dr.
Monash’s case and that the motion in the June 4th minutes was to grant the termination.

MOTION:  Dr.  Gillard  moved  to  approve  the  April  1,  2025  Regular  Session;  including
Executive Session and the June 4, 2025 Regular Session; including Executive Session.
SECOND: Dr. Bethancourt.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Dr. Beyer, Dr. Farmer, Dr. Gillard and Ms. Leach.
The following Board members were absent: Ms. Bain and Dr. Krahn.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

LEGAL MATTERS

I.  DISCUSSION, CONSIDERATION AND POSSIBLE ACTION ON SETTLEMENT

OFFER IN LIEU OF FORMAL HEARING

1.  MD-25-0012A, LAURA HARRINGTON, M.D., LIC. #24671

Dr.  Harrington  and  counsel  Melissa  Cuddington  were  present.  Carrie  Smith,  AAG  was
present  on  behalf  of  the  State.  Lynette  Evans,  AAG  was  present  as  the  Board’s
Independent Legal Advisor.

Ms. Cuddington requested executive session for confidential medical information.

Ms. Smith stated that she had no objection to the discussion of confidential documents in
executive session.

Ms. Evans agreed and noted that the Board would need to limit that executive session just
to those matters and then, if it goes beyond that, we'll have to come back to open session.

MOTION: Dr. Gillard moved for the Board to enter into Executive Session pursuant
to A.R.S. § 32-431.03(A)(3) to obtain legal advice.
SECOND: Dr. Farmer.
VOTE:  The  following  Board  members  voted  in  favor  of  the  motion:  Dr.  Figge,  Dr.
Bethancourt, Ms. Dorrell, Dr. Artz, Dr. Beyer, Dr. Farmer, Dr. Gillard and Ms. Leach.
The following Board members were absent: Ms. Bain and Dr. Krahn.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

The Board entered into Executive Session at 8:33 a.m.
The Board returned to Open Session at 8:42 a.m.

Final Minutes for the August 6, 2025 AMB Regular Session Meeting
Page 3 of 18

No legal action was taken by the Board during Executive Session.

Dr. Harrington stated that regarding patient A, there is an exchange of text messages, and
agreed that she did engage in reckless text messages with her. Dr. Harrington requested
that  the  Board  consider  that  the  successful  practice  of  psychiatry,  and  in  particular
psychotherapy, requires a unique manner of communication. Regarding patient B, he is a
distinguished professor of psychiatry, holding tenured positions at Princeton University of
Pennsylvania,  and  Johns  Hopkins.  He  is  definitively  opposed  to  the  disclosure  of  his
psychiatric records to any third party, including the Board. Dr. Harrington stated that at no
time did patient B provide her with any medication whatsoever. Dr. Harrington stated that
she is receptive to the Board’s suggestions about ways to improve her practice and her
goal  is  to  provide  the  best  care  possible  to  her  patients.  Dr.  Harrington  stated  that  she
would fully comply with any Board recommendations.

Ms.  Smith  requested  clarification  on  what  the  actual  settlement  proposal  was  for
consideration.

Ms. Cuddington stated that the proposal is for a reprimand in conjunction with a monitoring
agreement as stated in Respondent’s Settlement Conference memorandum.

Ms. Smith stated that this case arose out of complaint regarding Respondent’s interactions
with patient A. Respondent, based on the investigative information, was offered an inactive
with  cause  agreement  which  she  declined,  and  for  that  reason  the  Board  instituted  a
summary  suspension.  During  the  course  of  the  Board's  investigation,  Patient  B  was
identified, and Board Staff requested those records.. To this date the Board still has not
received  the  records,  and  it's  for  that  reason  that  the  staff  position  on  this  case  has
remained  at  revocation.  There's  no  valid  basis  to  continue  to  withhold  those  records,
including  the  patient’s  objection.  The  patient's  objection  is  immaterial  to  the  Board’s
statutes.  Ms.  Smith  read  A.R.S.  §  32-1451.01(D)  that  this  section,  and  any  other  law
making communications between a physician and the physician's patient privileged, does
not apply to investigations or proceedings conducted pursuant to this chapter. Ms. Smith
stated that the State will abide by whatever recommendation that the Board feels is most
appropriate in this case, be it a continuation of the deadlines to a continued pause in the
litigation process to allow the Respondent to obtain treatment or for the parties to negotiate
a  consent  agreement.  The  State  does  request  that  any  resolution  of  this  case  involve
production of Patient B’s records in full, so that the Board can adequately review the care
provided. Ms. Smith stated that if the Respondent wants to continue to have a license with
this Board, the Board needs to have a full understanding of her safety to practice medicine.

Ms.  Cuddington  stated  that  with  regards  to  the  records  issue,  the  patient  at

*[document truncated for length]*

---

### 2025-07-31 — Arizona Medical Board — July 31, 2025

**[MINUTES] 2025-07-31_MD_202511060953_d79f4712f7d9486f9e79851b095d0ecd.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR ADMINISTRATIVE JOINT LEGISLATION AND RULES
COMMITTEE TELECONFERENCE MEETING
Held on Thursday, July 31, 2025
1740 W. Adams St., Phoenix, Arizona

Committee Members
Jodi A. Bain, M.A., J.D., LL.M., Chair
Katie S. Artz, M.D., M.S.
Bruce Bethancourt, M.D.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.

GENERAL BUSINESS

A.  CALL TO ORDER

Chairwoman Bain called the Committee’s meeting to order at: 4:03 p.m.

B.  ROLL CALL

The  following  Committee  members  participated  virtually:  Ms.  Bain,  Dr.  Bethancourt,  Dr.  Artz,  Ms.
Dorrell, Dr. Farmer and Dr. Figge.

The following Committee member was absent: Dr. Artz.

The  following  Board  staff  participated  in  the  virtual  meeting:  Raquel  Rivera,  Executive  Director;
Pushpa  Gregor,  IT  Manager;  Michelle  Butler,  Chief  Operations  Officer  and  Michelle  Robles,  Board
Operations Manager. Carrie Smith, Assistant Attorney General (“AAG”) was also present.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

No individuals addressed the Board during the Public Statements portion of the meeting.

D.  APPROVAL OF MINUTES

•

June 27, 2025 Administrative Joint Legislation and Rules Committee

MOTION: Dr. Farmer moved to approve the June 27, 2025 Administrative JLRC Meeting
Minutes.
SECOND: Ms. Dorrell.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.
Bethancourt, Ms. Dorrell, Dr. Farmer and Dr. Figge. The following Committee member
was absent: Dr. Artz.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.

E.  REVIEW,  DISCUSSION  AND  POSSIBLE  RECOMMENDATIONS  REGARDING
APPROPRIATION

POTENTIAL

BUDGET

AND

AMB
FY25/FY26
CONSIDERATIONS

Ms.  Rivera  provided  the  Committee  with  the  budget  and  staffing  spreadsheets  for  FY25  and
projections for FY26.  Ms. Rivera reported that the Board remains in neutral revenue. Staff hopes to
refresh  the  MD  and  PA  websites  and  did  receive  a  quote  for  $150,000  through  ADOA.  Ms.  Rivera
reported  that  since  this  project  is  scheduled  to  start  July  26th,  she  plans  to  request  special
appropriations  for  FY27  to  help  cover  this  expense.  Ms.  Rivera  requested  that  the  JLRC  meet  in
August to review and provide feedback on the annual reports.

F.  REVIEW,  DISCUSSION  AND  POSSIBLE  RECOMMENDATIONS  REGARDING

AMB IT BUDGET
Ms. Rivera reported that the Board received grant funding through FSMB to aid in its IT projects. She
stated that staff is  limited to working on two projects at one time and there is a staggered plan for the
initial  four  projects.  Staff  continue  to  work  on  cost  savings  by  entering  a  three  month  contract  with
Zoom versus an annual contract. Ms. Rivera noted that the goal is to transition from Zoom to Google
Meets.

Ms. Butler confirmed that it would be about a $17,000 saving.

Ms.  Rivera  confirmed  that  there  are  similar  features  available  through  Google  Meets.  Ms.  Rivera
noted that the Board is moving from Constant Contact to ADOA for email blasts. It will be significantly
cheaper  at  $160  a  month  in  lieu  of  the  $8,000  for  Constant  Contact.  Ms.  Rivera  also  reported  that
staff will be moving away from Survey Monkey and start using Google surveys, which is a free service
through Gmail. These can be added to employee’s signatures and allow us to get responses in terms
of customer satisfaction feedback.

G.  REVIEW, DISCUSSION AND POSSIBLE RECOMMENDATION REGARDING FIVE

YEAR REVIEW AND RULEMAKING CALENDAR
Ms. Rivera reported that the calendar is available for review.

H.  FIVE YEAR REVIEW

1.  ARTICLE

2,

LICENSURE

-

REVIEW,

DISCUSSION

AND

POSSIBLE

RECOMMENDATIONS WITH UPDATE ON STATUS OF FIVE-YEAR REVIEW REPORT
Ms.  Rivera  reported  that  Article  2  rules  are  up  for  review  and  inquired  if  the  Committee  is
interested  in  making a change to the Board’s current  practice with regard to there being  no
timeframe on malpractice disclosures for initial applicants or if the Board would be interested
in putting a 10-year parameter on those malpractice disclosures.

Dr. Figge commented that when you're getting privileges and renewing your privileges, they
have a 10-year limit. Dr. Figge opined that it is acceptable.

Committee members agreed that it seems reasonable.

Ms. Bain stated that as a public member she had a concern that putting a five-year limit on
looking  into  a  malpractice  case  was  not  protecting  the  public.  Dr.  Figge  stated  that  for
privileging there has been a ten-year limit and that for something older than 10 years, there’s
not  likely  to  be  any  information.  Dr.  Farmer  agreed  that  it  would  not  affect  what  the  Board
does for public protection.

Ms. Rivera  noted  that typically the Federal  medical record retention requirements, and they
will  change  by  state,  is  usually  around  six  to  seven  years.  Even  if  we  have  that  10-year
practice parameter, there are going to be some cases where we will make the attempt to try
to get those records, but I think 10 will at least limit some of those investigations and for them
to go through the process a bit more efficiently.

Ms. Rivera confirmed that she can reach out to ARMA and a few other professional societies.
Ms. Rivera opined that this is something that they're going to be supportive of, because it will
help get individuals licensed quicker because if they have an old malpractice case, that could
stall the application process.

Final Minutes for the July 31, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 2 of 4

Ms. Bain opined that GRRC may have some problems with this.

Ms. Smith  explained that  obtaining malpractice settlements  is  used to evaluate  whether the
licensee  meets  A.R.S.  §  32-1422(a)(3)  which  is  whether  the  physician  can  safely  practice
medicine  and  (4)  which  is  having  a  professional  record  that  indicates  the  applicant  has  not
committed  or  engaged  in  conduct  that  would  contribute  to  grounds  for  disciplinary  action
against  the  licensee.  There  is  not  a  specific  statutory  requirement  regarding  malpractice.  If
there is a malpractice settlement that might indicate that there's some sort of a professional
conduct or medical quality of care issue, the Board needs to evaluate and determine whether
or not the issue been remediated and resolved in some way.

Ms. Rivera informed the Committee that potential language was provided in the June memo.

Ms. Bain explained that GRRC might have a problem with it if the timeframe is not in statute.

Dr. Bethancourt noted that the statute for medical records is seven years.

Ms. Smith confirmed that record retention is seven years for adults and seven years after the
18th birthday for children.

Ms. Rivera confirmed that the requirement for malpractice claims is in rule, not in statute. Ms.
Rivera noted that the Committee should see the red line version by September.

2.  ARTICLE 3, DISPENSING - REVIEW, DISCUSSION AND UPDATE ON STATUS OF FIVE-

YEAR REVIEW REPORT
Ms.  Rivera  stated  that  this  review  went  to  GRRC  on  July  29th  and  it  was  passed  with  the
recommendation  to  approve.  Representative  Member  Thornwall  had  asked  how  many
inspections  that  we  were  doing  for  dispensing  regulators,  and  Ms.  Rivera  let  him  know  that
the  Board  is  a  complaint  driven  agency  and  that  does  not  have  the  authority  to  go  on  site
without  a  complaint  to  review  record  keeping  practices.  Ms.  Rivera  noted  that  it  has  to  go
back to GRRC for their final approval on August 5th. At that time, Ms. Rivera reported that she
will  proved  the  data  that  we  have  around  32,373  physicians  and  of  those  433  have
dispensing registrations. That is about 1.3% of our licensee population.

I.  RULEMAKING

1.  ARTICLE  6,  DISCIPLINARY  ACTION  -  OFFICE  BASED  SURGERY  -  REVIEW,

DISCUSSION AND UPDATE REGARDING RULEMAKING CONSIDERATIONS
Ms. Rivera reported that the Five Year Rule Review for Article 6 was considered at that same
meeting  on  July  29th.  It  was  passed  with  the  recommendation  to  approve.  There  were  no
questions, comments, or concerns by GRRC. The 5 Year Review will now be considered at
their August 5th meeting.

2.  ARTICLE  7,  OFFICE  BASED  SURGERY  -  REVIEW,  DISCUSSION  AND  UPDATE

REGARDING RULEMAKING CONSIDERATIONS
Ms.  Rivera  reported  that  she  provided  the  notice  of  final  rulemaking  and  economic  impact
statement  for  the  Committee’s  review  with  the  changes  made  at  our  meeting  in  June.  This
was also sent to Dr. Merrill and the Arizona Society of Anesthesiologists, as requested. Ms.
Rivera  noted  that  she  hadn’t  received  any  feedback  from  them.  These  were  sent  to  the
Governor's office for their approval, and the plan is to submit these by the August 19th GRRC
submission deadline.

J.  DISCUSSION OF FUTURE TOPICS

Ms.  Rivera  requested  that  the  Committee  meet  around  August  18th  for  review  discussion  and
consideration of the draft annual reports, including the budget and strategic plan.  Ms. Rivera further
reported that the Board also received a request from a physician for clarification on an MA's ability to
provide anesthetic injections. Ms. Rivera noted that there was a previous inquiry sent to Ms. McSorley
as well that she would like to get the Committee’s input on.

Final Minutes for the July 31, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 3 of 4

Dr. Figge commented on MAs injecting aesthetic. They can give vaccinations but giving injections for
anesthesia is really next level. Dr. Farmer opined that he does not see a circumstance where an MA
should do local anesthetic injections. Dr. Farmer stated that it is problematic and he don’t see where
the need would be. Ms. Dorrell noted that the MA is working under the physician’s license, so it is the
physician's license at risk. Dr. Bethancourt noted that having overseen 300 physicians and 400 MAs,
they did an evaluation of each MA with their ability to drop the correct amount in a syringe and exactly
where the syringe is supposed to go. They found so much variation that it was frightening, and they
all had to be re-educated and retested. Dr. Bethancourt spoke highly against it.

Dr. Figge noted the FSMB training webinar and recommended having PHP updates in our meetings.

Ms. Rivera suggested data points that can be included in the report.

K.  ADJOURNMENT

MOTION: Dr. Bethancourt moved for adjournment.
SECOND: Dr. Farmer.
VOTE: The following Committee members  voted  in favor of the motion:  Dr. Bethancourt, Ms.
Dorrell, Dr. Farmer and Dr. Figge. The following Committee member was absent: Dr. Artz.
VOTE: 4-yay, 0-nay, 0-abstain, 0-recuse, 1-absent.

The meeting adjourned at: 4:47 p.m.

Raquel Rivera, Executive Director

Final Minutes for the July 31, 2025 AMB Administrative Joint Legislative and Rules Committee Teleconference Meeting
Page 4 of 4

---

### 2025-07-28 — Arizona Medical Board — July 28, 2025

**[MINUTES] 2025-07-28_MD_202602241012_2ea4b72d16974d2daaaddb3cb72be1ae.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR THE MEETING OF THE EXECUTIVE DIRECTOR SELECTION
AND RETENTION COMMITTEE
Held on Monday, July 28, 2025
1740 W. Adams St., Phoenix, Arizona

Committee Members
Lois E. Krahn, M.D., Chair
Susan Reina, P.A.-C, Vice-Chair
Bruce A. Bethancourt, M.D., F.A.C.P.
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Gail Guerrero-Tucker, M.D., M.P.H., F.A.A.F.P., D.A.B.F.M.
Jessyca Leach
John J. Shaff, PA-C, D.F.A.A.P.A

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Krahn called the Committee’s meeting to order at: 4:09 p.m.

B.  ROLL CALL

The  following  Committee  members  were  present:  Dr.  Krahn,  Ms.  Bain,  Dr.  Beyer,  Ms.  Dorrell,  Dr.  Farmer,  Dr.
Figge, Dr. Gillard, Ms. Leach, and PA Shaff.

The following Committee members were absent: PA Reina, Dr. Bethancourt, Dr. Artz, and Dr. Guerrero-Tucker .

ALSO PRESENT
The following Board staff participated in the meeting: Michelle Robles, Board Operations Manager. Carrie Smith,
Assistant Attorney General (“AAG”) and Michelle Kunzman, AAG also participated in the meeting.

C.  APPROVAL OF MINUTES

•

•

June 12, 2025 Executive Director Selection and Retention Committee Minutes

June 12, 2025 Executive Director Selection and Retention Committee Executive Session Minutes

MOVED: Dr. Farmer moved to approve the June 12, 2025 Regular Session and Executive Session
minutes.
SECOND: Dr. Beyer.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.
Beyer,  Ms.  Dorrell,  Dr.  Farmer,  Dr.  Figge,  Dr.  Gillard,  Ms.  Leach  and  PA  Shaff.  The  following
Committee members were absent: PA Reina, Dr. Bethancourt, Dr. Artz and Dr. Guerrero-Tucker.
VOTE: 9-yay, 0-nay, 0-abstain, 0-recuse, 4-absent.
MOTION PASSED.

D.  INTERVIEW CANDIDATES FOR THE EXECUTIVE DIRECTOR’S POSITION

MOVED: Dr. Krahn moved for the Board to enter into Executive Session to obtain legal advice pursuant to
A.R.S. § 38-431.03(A)(3) regarding the meeting format.
SECOND: Dr. Gillard.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.  Beyer,
Ms.  Dorrell,  Dr.  Farmer,  Dr.  Figge,  Dr.  Gillard  and  Ms.  Leach.  The  following  Committee  members  were
absent: PA Reina, Dr. Bethancourt, Dr. Artz, Dr. Guerrero-Tucker and PA Shaff.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 5-absent.
MOTION PASSED.

The Board entered into Executive Session at 4:11 p.m.
The Board returned to Open Session at 4:24 p.m.
No legal action was taken by the Board during Executive Session.

•  Frank V. DiMaggio

MOVED: Dr. Figge moved for the Board to enter into Executive Session pursuant to A.R.S. § 38-
431.03(A)(1) to conduct an interview.
SECOND: Dr. Gillard.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.
Beyer,  Ms.  Dorrell,  Dr.  Farmer,  Dr.  Figge,  Dr.  Gillard  and  Ms.  Leach.  The  following  Committee
members were absent: PA Reina, Dr. Bethancourt, Dr. Artz, Dr. Guerrero-Tucker and PA Shaff.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 5-absent.
MOTION PASSED.

The Board entered into Executive Session at 5:03 p.m.
The Board returned to Open Session at 5:30 p.m.
No legal action was taken by the Board during Executive Session.

•  Anthony Jusevitch

MOVED:  Dr.  Figge  moved  for  the  Board  to  enter  into  Executive  pursuant  to  A.R.S.  §  38-
431.03(A)(1) to conduct an interview.
SECOND: Ms. Leach.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.
Beyer,  Ms.  Dorrell,  Dr.  Farmer,  Dr.  Figge,  Dr.  Gillard  and  Ms.  Leach.  The  following  Committee
members were absent: PA Reina, Dr. Bethancourt, Dr. Artz, Dr. Guerrero-Tucker and PA Shaff.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 5-absent.
MOTION PASSED.

The Board entered into Executive Session at 4: 27 p.m.
The Board returned to Open Session at 4:53 p.m.
No legal action was taken by the Board during Executive Session.

•  Raquel Rivera

MOVED:  Ms.  Bain  moved  for the  Board  to  enter into  Executive  Session  pursuant to A.R.S.  §  38-
431.03(A)(1) and (3)to conduct an interview.
SECOND: Ms. Leach.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.
Beyer,  Ms.  Dorrell,  Dr.  Farmer,  Dr.  Figge,  Dr.  Gillard  and  Ms.  Leach.  The  following  Committee
members were absent: PA Reina, Dr. Bethancourt, Dr. Artz, Dr. Guerrero-Tucker and PA Shaff.
VOTE: 8-yay, 0-nay, 0-abstain, 0-recuse, 5-absent.
MOTION PASSED.

The Board entered into Executive Session at 5:39 p.m.
The Board returned to Open Session at 6:06 p.m.
No legal action was taken by the Board during Executive Session.

Final Minutes for the July 28, 2025 Executive Director Selection and Retention Committee Meeting

E.  DELIBERATION  AND  POSSIBLE  SELECTION  OF  EXECUTIVE  DIRECTOR  INCLUDING

DISCUSSION OF COMPENSATION

MOVED:  Dr.  Gillard  moved  for  the  Board  to  enter  into  Executive  Session  to  to  discuss  employment
matters and obtain legal advice pursuant to A.R.S. §§ 38-431.03(A)(1) and (3),
SECOND: Ms. Leach.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.  Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Ms. Leach and PA Shaff. The following Committee members
were absent: PA Reina, Dr. Bethancourt, Dr. Artz and Dr. Guerrero-Tucker.
VOTE: 9-yay, 0-nay, 0-abstain, 0-recuse, 4-absent.
MOTION PASSED.

The Board entered into Executive Session at 6:15 p.m.
The Board returned to Open Session at 7:36 p.m.
No legal action was taken by the Board during Executive Session.

MOTION: Dr. Farmer moved to offer the Executive Director appointment to Raquel Rivera and to authorize
Dr.  Krahn  to  consult  with  ADOA  and  make  an  offer  for  salary  as  discussed  by  the  Committee  during
executive session..
SECOND: Ms. Leach.
Dr. Figge requested clarification on who is legally required to sign off on salary issues.

Ms.  Smith  clarified  that  the  statute  allows  the  Committee  to  decide  on  the  salary  and  the  Committee  can
designate  someone  to  negotiate  that.  Ms.  Smith  recommended  the  chair  of  the  Committee  would  be  the  most
appropriate designee.

Dr. Krahn confirmed that she will negotiate the salary in consultation with the appropriate staff.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.  Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Ms. Leach and PA Shaff. The following Committee members
were absent: PA Reina, Dr. Bethancourt, Dr. Artz and Dr. Guerrero-Tucker.
VOTE: 9-yay, 0-nay, 0-abstain, 0-recuse, 4-absent.
MOTION PASSED.

Dr.  Krahn  thanked  the Committee  for the  thoughtful  process.  Ms.  Bain  acknowledged  the process and thanked
the candidates for their effort and time.

F.  ADJOURNMENT

MOTION: Dr. Beyer moved for adjournment.
SECOND: Dr. Gillard.
VOTE:  The  following  Committee  members  voted  in  favor  of  the  motion:  Dr.  Krahn,  Ms.  Bain,  Dr.  Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Ms. Leach and PA Shaff. The following Committee members
were absent: PA Reina, Dr. Bethancourt, Dr. Artz and Dr. Guerrero-Tucker.
VOTE: 9-yay, 0-nay, 0-abstain, 0-recuse, 4-absent.
MOTION PASSED.

The meeting adjourned at: 7:42 p.m.

 David C. Beyer, M.D., Chair

Final Minutes for the July 28, 2025 Executive Director Selection and Retention Committee Meeting

---

### 2025-07-09 — Arizona Medical Board — July 09, 2025

**[MINUTES] 2025-07-09_MD_202602241009_b2e7ae17618a450f90064a3139d2c9a0.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR THE MEETING OF THE EXECUTIVE DIRECTOR SELECTION
AND RETENTION COMMITTEE
Held on Wednesday, July 9, 2025
1740 W. Adams St., Phoenix, Arizona

Committee Members
Lois E. Krahn, M.D., Chair
Susan Reina, P.A.-C, Vice-Chair
Katie S. Artz, M.D., M.S.
Bruce A. Bethancourt, M.D., F.A.C.P.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
Laura Dorrell, M.S.N., R.N.
R. Screven Farmer, M.D.
Gary R. Figge, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Gail Guerrero-Tucker, M.D., M.P.H., F.A.A.F.P., D.A.B.F.M.
Jessyca Leach
John J. Shaff, PA-C, D.F.A.A.P.A

GENERAL BUSINESS

A.  CALL TO ORDER

Chairwoman Krahn called the Committee’s meeting to order at: 4:05 p.m.

B.  ROLL CALL

The following Committee members participated virtually: Dr. Krahn, PA Reina, Dr. Beyer, Ms. Dorrell, Dr. Farmer,
Dr. Figge, Dr. Gillard, Dr. Guerrero-Tucker, Ms. Leach and PA Shaff.

The following Committee members were absent: Dr. Bethancourt, Dr. Artz, and Ms. Bain.

ALSO PRESENT
The following Board staff participated in the meeting: Michelle Robles, Board Operations Manager. Carrie Smith,
Assistant Attorney General (“AAG”) and Michelle Kunzman, AAG also participated in the meeting.

C.  UPDATE,  DISCUSSION  AND  POSSIBLE  ACTION  REGARDING  THE  RESULTS  OF
INCLUDING  POTENTIAL  SELECTION  OF  TOP  THREE

INTERVIEWS

CANDIDATE
CANDIDATES

Dr. Krahn noted that the new candidates have been interviewed, and the goal is to narrow them down to the top
three.

MOVED:  Dr.  Krahn  moved  for  the  Committee  to  enter  into  Executive  Session  pursuant  to  A.R.S.  §  38-
431.03(A)(1) and (3) to discuss the consideration of employment information and legal advice.
SECOND: Dr. Farmer.
VOTE: The following Committee members voted in favor of the motion: Dr. Krahn, PA Reina, Dr. Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Dr. Guerrero-Tucker, Ms. Leach and PA Shaff.
The following Committee members were absent: Dr. Bethancourt, Dr. Artz, and Ms. Bain.
VOTE: 10-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.

MOTION PASSED.

The Committee entered into Executive Session at 4:07 p.m.
The Committee returned to Open Session at 4:40 p.m.
No legal action was taken by the Board during Executive Session.

MOVED: Dr. Figge moved to reduce this list of five to three candidates.
SECOND: PA Reina.
VOTE: The following Committee members voted in favor of the motion: Dr. Krahn, PA Reina, Dr. Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Dr. Guerrero-Tucker, Ms. Leach and PA Shaff.
The following Committee members were absent: Dr. Bethancourt, Dr. Artz, and Ms. Bain.
VOTE: 10-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

MOVED: PA Reina moved to elect candidates A, B and D to the short list of candidates.
SECOND: PA Shaff.
Dr. Krahn noted that these letters have been identified to specific candidates in the executive session. Dr. Beyer
commented  that  he  would  have  selected  three  different  candidates.  Dr.  Beyer  suggested  having  all  Committee
members  vote  on  all  candidates  and  the  top  three  candidates  are  chosen  based  on  votes.  Dr.  Gillard  agreed
regarding selecting a different three and noted candidate C’s experience. Dr. Figge opined that there was equal
discussion on all candidates. Dr. Beyer suggested a roll call vote so that it is fair and clear.

Ms. Smith expressed no concerns regarding the roll call but advised that the motion would need to be withdrawn.
Ms. Kunzman expressed caution that the Committee members may be swayed by others.

Dr. Beyer and Dr. Farmer opined that Committee members already have their three candidates in mind.

Mr. McNeely agreed the Committee could do a roll call vote on the top three candidates.
MOTION WITHDRAWN.

MOVED: Dr. Beyer moved for a roll call vote for each Committee member to name their top three.
SECOND: Dr. Figge.
Ms. Kunzman inquired about the intent of the motion.

Dr. Beyer stated that it is to reach a consensus of the top three candidates.
VOTE: The following Committee members voted in favor of the motion: Dr. Krahn, PA Reina, Dr. Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Dr. Guerrero-Tucker, Ms. Leach and PA Shaff.
The following Committee members were absent: Dr. Bethancourt, Dr. Artz, and Ms. Bain.
VOTE: 10-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

Roll Call Vote for Top Three Candidates: Dr. Krahn (A, B, C), PA Reina (A, B, D), Dr. Beyer (B, C, D), Ms.
Dorrell  (A,  B,  D),  Dr.  Farmer  (A,  B,  D),  Dr.  Figge  (A,  C,  D),  Dr.  Gillard  (A,  B,  C),  Dr.  Guerrer-Tucker
abstained, Ms. Leach (B, C, D) and PA Shaff (A, B, D)

Dr. Krahn stated that staff will notify the candidates and a zoom meeting will be scheduled.

Ms. Smith noted that the interview questions need to still be created, and the previous process will be used.

Dr. Farmer agreed that the previous process should be followed.

D.  DISCUSSION  AND  POSSIBLE  ACTION  REGARDING  NEXT  STEPS  IN  THE  HIRING
PROCESS,  INCLUDING  BUT  NOT  LIMITED  TO  UPCOMING  MEETINGS  AND  DECISION
MAKING TIMELINE

Dr.  Krahn  informed  the  Committee  that  there  are  no  funds  available  in  the  budget  to  reimburse  candidates  for
travel for an interview or to meet staff in person. Dr. Krahn suggested that the delegates could have a meeting to
work  with  the  selection  available  and  choose  the  strongest  candidate  or  have  a  zoom  meeting  with  the  full
Committee  to  interview  the  top  three  candidates.  Dr.  Gillard  spoke  in  favor  of  the  Committee  meeting  the
Final Minutes for the July 9, 2025 Executive Director Selection and Retention Committee Meeting Agenda

candidates  via  Zoom.  Dr.  Krahn  noted  that  questions  would  need  to  be  agreed  upon  and  provided  to  the
candidates.

PA  Shaff  agreed  that  there  should  be  a  Zoom  meeting  to  put  faces  to  names  and  give  those  who  were  not
involved in the interview group a better understanding of the candidates. Dr. Krahn confirmed that the Committee
has received the reference letters for the candidates.

Mr. McNeely informed the Committee that references are normally done after a verbal offer has been extended to
the selected candidate.

Dr.  Farmer  spoke  against  waiting  until  after  the  selection  to  obtain  references  and  spoke  in  favor  of  the  Zoom
meeting.

Mr. McNeely confirmed that references can be obtained regarding the top candidates.

MOVED:  Dr.  Farmer  moved  for  the  final  three  candidates  to  solicit  references,  which  would  be  made
available  to  the  full  committee,  and  then  schedule  a  Zoom  meeting  with  the  candidates  and  the
committee.
SECOND: Dr. Gillard.
VOTE: The following Committee members voted in favor of the motion: Dr. Krahn, PA Reina, Dr. Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Dr. Guerrero-Tucker, Ms. Leach and PA Shaff.
The following Committee members were absent: Dr. Bethancourt, Dr. Artz, and Ms. Bain.
VOTE: 10-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

E.  ADJOURNMENT

MOTION: Dr. Figge moved for adjournment.
SECOND: Dr. Farmer.
VOTE: The following Committee members voted in favor of the motion: Dr. Krahn, PA Reina, Dr. Beyer,
Ms. Dorrell, Dr. Farmer, Dr. Figge, Dr. Gillard, Dr. Guerrero-Tucker, Ms. Leach and PA Shaff.
The following Committee members were absent: Dr. Bethancourt, Dr. Artz, and Ms. Bain.
VOTE: 10-yay, 0-nay, 0-abstain, 0-recuse, 3-absent.
MOTION PASSED.

The meeting adjourned at: 5:06 p.m.

David C. Beyer, M.D., Chair

Final Minutes for the July 9, 2025 Executive Director Selection and Retention Committee Meeting Agenda

---

**[MINUTES] 2025-07-09_MD_202509041135_99475abc5a094d95a17df5ce4a029536.pdf**

Arizona Medical Board
1740 W. Adams St, Suite 4000 • Phoenix, Arizona 85007
Home Page: http://www.azmd.gov
Telephone (480) 551-2700 • Fax (480) 551-2705 • In-State Toll Free (877) 255-2212

FINAL MINUTES FOR SPECIAL TELECONFERENCE MEETING
Held on Wednesday, July 9, 2025
1740 W. Adams St., Phoenix, Arizona

Board Members
Gary R. Figge, M.D., Chair
Bruce A. Bethancourt, M.D., F.A.C.P., Vice-Chair
Laura Dorrell, M.S.N., R.N., Secretary
Katie S. Artz, M.D., M.S.
Jodi A. Bain, M.A., J.D., LL.M.
David C. Beyer, M.D., F.A.C.R., F.A.S.T.R.O.
R. Screven Farmer, M.D.
James M. Gillard, M.D., M.S., F.A.C.E.P., F.A.A.E.M.
Gail Guerrero-Tucker, M.D., M.P.H., F.A.A.F.P., D.A.B.F.M.
Lois E. Krahn, M.D
Jessyca Leach

GENERAL BUSINESS

A.  CALL TO ORDER

Chair Figge called the meeting to order at: 5:14 p.m.

B.  ROLL CALL

The following Board members were present: Dr. Figge, Dr. Bethancourt, Ms. Dorrell, Dr. Artz, Ms.
Bain, Dr. Beyer, Dr. Farmer, Dr. Gillard, Dr. Guerrero-Tucker, Dr. Krahn and Ms. Leach.

ALSO PRESENT
The following  Board  staff  participated  in  the  meeting: Raquel  Rivera,  Interim Executive  Director;
Claude Deschamps, M.D., Chief Medical Consultant; Nicole Samaradellis, Investigations Manager;
and Michelle Robles, Board Operations Manager. Carrie Smith, Assistant Attorney General (“AAG”)
also participated in the meeting.

C.  PUBLIC STATEMENTS REGARDING MATTERS LISTED ON THE AGENDA

Individuals who addressed the Board during the Public Statements portion of the meeting appear
beneath the case.

D.  EXECUTIVE DIRECTOR’S REPORT

•  Review, Discussion and Possible Recommendations Regarding Joint Educational Meeting

with DO Board

Ms. Rivera reported that she continues to work with the DO Board Executive Director on
the  Joint  Educational  Meeting  with  our  Boards.  Last  week  at  our  JLRC  meeting,  we
discussed  Item  G  and  it  was  requested  that  in  addition  to  the  topics  of  med  spas,  PA
supervision, and AI’s incorporation into clinical practice, that we add some education on
the  Educational  Commission  for Foreign  Medical  Graduates  (ECFMG)  and  International
Medical Graduates (IMGs). Ms. Rivera reported that there was a good presentation at the
FSMB this year titled IMG 101 presented by the ECFMG. The presenters have tentatively
agreed to present during the joint meeting but dates need to be coordinated with the DO
Board. Ms. Rivera noted that she provided the AMB Calendar and would like some dates
in  September  or  October  that  would  work  for  the  Board  and  requested  the  Board’s

preference  for  in-person,  virtual,  or  both  to  be  flexible  with  Board  member  scheduling.
Fridays reported working best for DO Board staff.

Board members spoke in favor of a virtual meeting.

•  Review, Discussion and Consideration of FSMB Board Member Training Webinars

Ms. Rivera reported that she wanted to highlight the FSMB Free Board Member Training
webinars  scheduled  for  7/21  and  8/20  related  to  discipline,  board  member  roles,  and
effective governance and ethics. Ms. Rivera request Board member’s feedback from the
courses. Ms.  Rivera  noted  that  once  new  Board  members  are  appointed  she  plans  to
include these webinars as part of the New Board Member Orientation.

•  Recognition of Dr. Krahn’s Service on USMLE Composite Committee

Ms. Rivera acknowledged Dr. Krahn’s participation in the USMLE Composite Committee
and  provided  the  Board  with  her  Volunteer  Spotlight.   The  composite  committee  was
established by the FSMB and NBME to provide oversight and direction of the USMLE. The
Composite Committee is responsible for approval of examination objectives and blueprints;
test  formats  and  changes  in  test  length;  score  reporting  policies;  test  administration
policies;  and  policies  for  examination  security  and  integrity,  irregular  behavior,  score
validity and anomalous performance. Additionally, Dr. Krahn was nominated by the FSMB
to serve on the Accreditation Review Committee for the Accreditation Counsel for CME,
which is great as the Board starts to evaluate services to simplify CME maintenance and
auditing compliance. Ms. Rivera thanked Dr. Krahn for her service and representation of
the Arizona Medical Board in these important roles within the FSMB.

•  Consideration  and  Discussion  Regarding  Petition  to  the  Governor’s  Regulatory  Review

Council

Ms.  Rivera  reported  that  on  5/29/25  she  was  notified  by  GRRC  of  a  Petition  filed  by  a
licensee for consideration at the 6/24/25 GRRC Study Session to determine if a hearing
was warranted. The Petition and her response were submitted to GRRC on 6/12/25. The
Petition and the Board’s response was considered on 6/24/25. GRRC counsel staff opined
that the matter was outside the scope of their review. On 7/1/25, GRRC voted and denied
the Petition for review.

Ms. Rivera provided an update to the Board with regard to the FSMB Grant we applied for.
The FSMB approved funding in the amount of $35, 235 to address our IT needs such as
updating our websites and License verification pages for all license types, increasing the
Board’s  Data  Sharing  Capability,  updating  the  Board  meeting  website,  and  Licensing
Portability (IMLCC compact) tracking and reporting. Ms. Rivera noted that the one project
that didn't get funded, for unlicensed practitioners, she plans to request through our aim
funding.

E.  CHAIR’S REPORT

•  Appointment of New Review Committee B Chair

Dr. Figge recommended Dr. Beyer as chair.

Dr. Beyer accepted the new role but noted that he would need to appear virtually for the
August meeting.

•  Acknowledgement of Board Members’ Service

Dr. Figge noted that we have 11 out of 12 positions filled and have several people whose
terms have expired, and are continuing to serve. We have 2 members who were appointed
and not confirmed by the Senate, which were told they're not going to be confirmed. This
means  their  appointment  ends  after  12  months,  and  they  can’t  come  to  meetings

Final Minutes for the AMB July 9, 2025 AMB Special Teleconference Meeting
Page 2 of 15

afterwards. Dr. Figge thank those people for serving and thanked Dr. Guerrero-Tucker and
Ms. Leach for serving. Dr. Guerrero Tucker has let us know that she'll not be able to be at
August meeting so this will be her last meeting. Dr. Krahn commented that the service that
Dr. Guerrero-Tucker provided has been very impressive, and it's incredibly important that
we have a member who has a primary care perspective, as well as a rural primary care
perspective. Dr. Krahn stated that our public members are incredibly valuable, and that the
amount of work involved for a public member is greater than for a physician member. Dr.
Figge further noted that we only have 11 out of 12 positions, and 7 out of those 11 that we
have serving are not Senate approved current and appointed positions. If everybody that's
not required to be here because they're appointed and confirmed by the Senate left, we
would have four members on the board right now and could not meet. Dr. Figge opined
that it is important for the public to hear that we need action. We need to get this board
back  on  track  where  we  have  active,  appointed,  confirmed  members,  and  don't  have to
worry about a quorum for every meeting.

F.  LEGAL ADVISOR’S REPORT

•  Update and Discussion on Dworkin v. Arizona Medical Board, LC2024-000429

Mr. Hargraves provided an update to the Board and noted that there was a hearing before
the  judge  last  month  and  the  judge  has  directed  the  parties  to  meet  and  confer.  Mr.
Hargraves  requested  that  the  Board  go  into  executive  session  for  the  purpose  of  legal
advice and ad to discuss the Board's position, and to instruct counsel regarding the Board's
position and settlement discussions to resolve that pending matter.

MOVED:  Dr.  Beyer  moved  for  the  Board  to  enter  into  Executive  Session  to  obtain
legal  advice  pursuant  to  A.R.S.  §  38-431.03(A)(4)  to  discuss  the  Board’s  position
regarding settlement discussions.
SECOND: Dr. Artz.
VOTE: The following Board members voted in favor of the motion: Dr. Bethancourt,
Ms.  Dorrell,  Dr.  Artz,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard,  Dr.  Guerrero-Tucker,  Dr.
Krahn and Ms. Leach. The following Board members were absent: Dr. Figge and Ms.
Bain.
VOTE: 9-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

The Board entered into Executive Session at 7:39 p.m.
The Board returned to Open Session at 7:45 p.m.
No legal action was taken by the Board during Executive Session.

MOTION: Dr. Krahn moved for Mr. Hargraves to proceed as instructed in executive
session.
SECOND: Dr. Beyer.
VOTE: The following Board members voted in favor of the motion: Dr. Bethancourt,
Ms.  Dorrell,  Dr.  Artz,  Dr.  Beyer,  Dr.  Farmer,  Dr.  Gillard,  Dr.  Guerrero-Tucker,  Dr.
Krahn and Ms. Leach. The following Board members were absent: Dr. Figge and Ms.
Bain.
VOTE: 9-yay, 0-nay, 0-abstain, 0-recuse, 2-absent.
MOTION PASSED.

G.  REVIEW,  DISCUSSION  AND  CONSIDERATION  OF  FSMB  DRAFT
RECOMMENDATIONS  FROM  ADVISORY  COMMISSION  ON  ADDITIONAL
LICENSING MODELS

Ms. Rivera reported that recent trends show a shift towards easing licensure pathways for IMGs  in
the  US,  with  several  states  enacting  or  considering  legislation  to  bypass  traditional  residency
requirements including proposed legislation the last year in Arizona. Ms. Rivera provided the Board
with the FSMB State-by-State Overview of Enacted and Proposed Additional Licensure Pathways
for reference.

Final Minutes for the AMB July 9, 2025 AMB Special Teleconference Meeting
Page 3 of 15

Ms.  Rivera  reported  that  SB1395  changed  the  requirement  from  successfully  complete  to  be
enrolled in an approved 24 month hospital internship, residency, or clinical fellowship in addition to
the  12  month  requirement  for  basic  licensure  as  outlined  under  A.R.S.  32-1422  to  successfully
complete  an  approved  internship,  residency,  or  fellowship  program,  for  a  total  of  36  months  of
training unless the applicant completed a 5th pathway or served as an assistant professor for 36
months. The Board submitted a neutral position to this bill. SB1395 was signed by the Governor
on May  7,  2025. SB  1108  was  proposed  this session and  did  not  pass;  however,  it  would  have
authorized the Board to grant a provisional license to an international medical licensee who has a
medical  doctorate  or  substantially  similar  degree  from  an  international  medical  program  in  good
standing; completed a residency or substantially similar PGT; “basic fluency” in English; practiced
at least 60 months (five years) within the last six years in Australia, Canada, Hong Kong, Ireland,
Ireland,  Israel,  New  Zealand,  Singapore,  South  Africa,  Switzerland,  the  UK,  or  any  additional
country  added  by  the  Board;  practiced  for  at  least  five  years  after  completing  the  residency  or
training program; an offer of employment at any health care provider serving a population less than
1 million; shall convert to a full license after 4 years. HB 2148 also did not pass but would have
established  a  program  to  grant  provisional  licenses  to  foreign  medical  graduates  and  nurses,
allowing them to practice under supervision in designated healthcare shortage areas in Arizona.
Applicants  must  have  completed  relevant  medical  or  nursing  education  outside  the  U.S.,
demonstrate legal presence, pass an English-language proficiency test, and undergo a background
check.  Following  successful  completion  of  supervised  practice  and  examinations,  these
professionals may obtain full licensure, with a requirement to work in underserved areas for two to
four  years. The  Arizona medical  and  nursing  boards would  have  to  provide  orientation,  training,
and support services to facilitate their i

*[document truncated for length]*
