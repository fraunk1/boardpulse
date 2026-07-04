You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Osteopathic Medical Board of California** (CA) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/CA/CA_DO#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-04-23]` — Osteopathic Medical Board of California — April 23, 2026
- `[2026-01-22]` — Osteopathic Medical Board of California — January 22, 2026
- `[2025-11-13]` — Osteopathic Medical Board of California — November 13, 2025
- `[2025-08-14]` — Osteopathic Medical Board of California — August 14, 2025

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: CA_DO
state: CA
---

# Osteopathic Medical Board of California — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Osteopathic Medical Board of California | [Minutes page](CA_DO_MINUTES_URL) |

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

Sources-table URL: https://www.ombc.ca.gov/activity/meetings.shtml

## Meeting Minutes Data

Board: Osteopathic Medical Board of California
State: CA
Code: CA_DO

### 2026-04-23 — Osteopathic Medical Board of California — April 23, 2026

**[AGENDA] 2026-04-23_20260423_agenda.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 |F (916) 928-8392 | www.ombc.ca.gov

MEMBERS OF THE BOARD
President
Denise Pines, MBA
Vice President
Hemesh Patel, D.O.
Secretary
Gor Adamyan

John M. Cummins, J.D.
Brett Lockman, D.O.
Negeen Mirreghabie, Esq.
Faisal Qazi, D.O.
Matthew Swain, D.O.

 QUARTERLY BOARD MEETING AGENDA

Western University of Health Sciences

521 E. 3rd Street
Amphitheater I - HPC
Pomona, CA 91766
(916) 928-8390 Office Main Line

Thursday, April 23, 2026
8:00 a.m. – 5:00 p.m.
(or until the conclusion of business)

Public WebEx/Telephone Access – See Attached
Meeting Information

MEETING TIMES AND ORDER OF AGENDA ITEMS ARE
SUBJECT TO CHANGE

Action may be taken on
any item listed on the
agenda

While the Board intends to
webcast this meeting, it
may not be possible to
webcast the entire open
meeting due to limitation
on resources or technical
difficulties.

Please see Meeting
Information section for
additional information on
public participation.

The Osteopathic Medical Board of California (Board) will meet in-person and via
Webex in accordance with Government Code section 11123.2.

Discussion may be had and action may be taken on any item on the agenda

OPEN SESSION

1.

2.

3.

Call to Order/Roll Call/ Establishment of a Quorum- Machiko Chong, Licensing
Program Manager

Reading of the Board’s Mission Statement– Erika Calderon, Executive Director

Hearing on Petition for Early Termination of Probation, Jeff Douglas Lester, DO
(20A 5421)

   CLOSED SESSION

4. Deliberation on disciplinary matters, including proposed decisions, non-adopt
proposed decisions, and stipulations (Government Code section 11126 (c)(3).)

   RECONVENE IN OPEN SESSION

5.

Public  Comment  on  Items  Not  on  the  Agenda  -Denise  Pines,  MBA.
The  Board  may  not discuss  or  take  action  on  any  matter  raised  during  this
public comment section except to decide whether to place the matter on
the  agenda  of  a  future  meeting.  (Government  Code  sections  11125,
11125.7(a).)

6.  Western  University  Health  Sciences  Student  Questions  &  Answers  Session,

Western Students and Board Members

7.

Review  and  Possible  Action  to  Approve  Board  Meeting  Minutes  –  Erika
Calderon, Executive Director

A.  November 13, 2025, Amended Board Meeting Minutes

B.  January 22, 2026, Board Meeting Minutes

8.

9.

President’s Report - Denise Pines, MBA

Board Member Communications with Interested Parties -  Denise Pines, MBA

10.

Intergovernmental Relations Reports and Administrative Services Update

A.  DCA Update – Shelly Jones, Assistant Deputy Director, Board and Bureau

Relations, DCA

B.  Budget Update –  Kaila  Van  Lindt,  Staff  Services  Analyst,  Budget  Office,

DCA

11.

Presentation  on  Corporate  Practice  of  Medicine,  John  Gatschet,  Deputy
Attorney General, Attorney General’s Office

LUNCH RECESS AND RECONVENE IN OPEN SESSION

12.

13.

14.

15.

Executive Director’s Report- Erika Calderon, Executive Director
Administrative  Services,  including  administrative  services,  personnel,  and
technology updates

Licensing/Admin  Program  Summary,
and  statistics- Machiko Chong, Licensing Program Manager

including  licensing  unit  updates,

Enforcement  and  Probation  Program  Summaries,
updates, and statistics- Cristy Livramento, Enforcement Program Manager

including  program

Presentation  from  the  Accreditation  Council  for  Continuing  Medical
Education  (ACCME),  Graham  McMahon  M.D.,  President  and  Chief
Executive Officer, ACCME

BREAK RECONVENE IN OPEN SESSION

16.

Rulemaking  Update  -  Report  on  Pending  or  Proposed  Regulations  -  Terri
Thorfinnson,  J.D.,  Legislative  and  Regulatory  Specialist  and  Erika  Calderon,
Executive Director

17.  Discussion and Possible Action on Pending Legislation – Terri Thorfinnson, J.D.

Legislative and Regulatory Specialist

A.  Discussion and Possible Action on Pending Legislation

AB 1703 (Hart) Title Protection: Osteopath

SB 1002 (Niello) License Exemption: Out of State Physicians: Non-Life-Threatening
Condition

AB 2398 (Alvarez) Alternative Pathway for Residency Training for M.D.s & D.O.s

AB 1587 (Ta) Pharmacist Prescription Authority: Life-Threatening Conditions

AB 2575 (Ortega) A.I. in Health Care

SB 903 (Padilla) A.I. consent: Mental Health Professionals

AB 2164 (Bauer-Kahan) Reproductive Health Protection: Prohibits extradition

Menopause Trailer Bill Language, 2026-27 Governor’s Budget-- version Published
February 2, 2026

Governor Newsom’s Press Release Announcement -- Published February 2, 2026

AB 2256 (Chen) Radiology Assistant Act: No Regulatory Oversight for
Act/Profession

B.  2026 Informational Bill “Watch” List

AB 2386 (Alvarez) Alternative Pathway to Residency Training: M.D.s,

SB 1179 (Menjivar) Physicians from El Salvador

AB 1558 (Arambula) Emergency Physician Volunteer Health Act

AB 2140 (Johnson) Mandatory Reporting: Settlements, Arbitration, Judgments:
Fine increase

SB 849 (Weber-Pierson) Sexual Misconduct

AB 1637 (Caloza) Physician: Medical Records

AB 2311 (Schiavo) Health Facilities Hiring Physicians

AB 1598 (Quirk-Silva) Behavioral Sciences

AB 408 (Berman)MBC Wellness Program (2025)

AB 485 Labor Commissioner: Unsatisfied Judgments: non-payment of wages (2025)

AB 967 (Valencia) Physician Expedite Fee (2025)

SB 626 (Smallwood-Cuevas) Prenatal Care screening and treatment (2025)

AB 2195 (Rodriguez) Child Support: Suspension of License

18.

Solicitation of Future Agenda Items - Denise Pines, MBA

   CONVENE IN CLOSED SESSION

19.  Annual Performance Evaluation of the Executive Director

•  Pursuant to Government Code section 11126, subdivision (a)(1), the Board
will conduct the annual performance evaluation and consider the salary
of its the Executive Director.

   RECONVENE IN OPEN SESSION

20.  Adjournment

Online Access to Meeting

The Osteopathic Medical Board of California will also broadcast the public portion
of its meeting via WebEx Events. To participate in the WebEx Events meeting, please
log on to this website on the day of the meeting:

Click Here to Join Meeting

If joining by phone
+1-415-655-0001 US Toll
Access code: 2494 803 3761
Passcode: 26622423

Experiencing issues joining the Meeting?

Copy and paste the link text below into an internet browser:

https://dca-meetings.webex.com/dca-
meetings/j.php?MTID=m9f8722dde8444903d46f0cb83a1c08b9

Members of the public may but are not obligated to provide their names or personal
information as a condition of observing or participating in the meeting. When signing
into  the  WebEx  platform,  participants  may  be  asked  for  their  name  and  email
address. Participants who choose not to provide their names will need to provide  a
unique  identifier  such  as  their  initials  or  another  alternative,  so  that  the  meeting

moderator can identify individuals who wish to make public comment; participants
who choose not to provide their email address may utilize a fictitious email address
like in the following sample format: XXXXX@mailinator.com.

Please Note: Because there is an audio delay, if you are participating by phone and
simultaneously watching the Webcast, the Board requests you turn off the sound to
the Webcast for improved clarity.

For further information about this meeting, please contact Machiko Chong at 916-928-
7636 or in writing at 1300 National Drive, Suite 150, Sacramento, CA 95834. This notice
and agenda, and any available Board meeting materials, can be accessed on the
Board’s website at www.ombc.ca.gov

In accordance with the Bagley-Keene Open Meeting Act, all meetings of the Board,
including any teleconference sites when the meeting is a teleconference meeting,
are open to the public. Government Code section 11125.7 provides the opportunity
for  the  public  to  address  each  agenda item  during  discussion  or  consideration  by
the Board prior to the Board taking any action on said item. Members of the public
will  be  provided  appropriate  opportunities  to  comment  on  any  issue  before  the
Board, but the Board President, at his or her discretion, may apportion available time
among those who wish to speak. Individuals may appear before the Board to discuss
items not on the  agenda;  however,  the Board can neither discuss  nor take official
action on these items at the time of the same meeting. (Government Code sections
11125, 11125.7(a).)

Board  meetings  are  held  in  barrier  free  facilities  that  are  accessible  to  those  with
physical disabilities in accordance with the Americans with Disabilities Act (ADA). If
you  are  a  person  with  a  disability  requiring  disability-related  modifications  or
accommodations to participate in the meeting, including auxiliary aids or services,
please  contact  Machiko  Chong,  ADA  Liaison,  at  (916)  928-7636  or  e-mail  at
Machiko.Chong@dca.ca.gov or send  a written request to the Board’s office at 1300
National Drive, Suite 150, Sacramento, CA 95834-1991.  Providing your request at least
five  (5)  business  days  before  the  meeting  will  help  to  ensure  availability  of  the
requested accommodation. Requests should be made as soon as possible, but at
least five (5) working days prior to the scheduled meeting. You may also dial a voice
TTY/TDD Communications Assistant at (800) 322-1700 or 7-1-1.

---

**[MINUTES] 2026-04-23_20260423_mat_2.pdf**

OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA

MISSION STATEMENT

To protect the public by requiring
competency, accountability, and integrity
in the safe practice of medicine by
osteopathic physicians and surgeons.

---

**[MINUTES] 2026-04-23_20260423_mat_7a.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390

|  www.ombc.ca.gov

|  F (916) 928-8392

MEMBERS
PRESENT:

STAFF
PRESENT:

Osteopathic Medical Board of California

AMENDED Board Meeting Minutes

November 13, 2025

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Brett Lockman, D.O.
Matthew Swain, D.O.

Erika Calderon, Executive Director
Machiko Chong, Licensing Program Manager
Cristy Livramento, Enforcement Program Manager
Terri Thorfinnson, Legislative/Regulatory Specialist
Shelly Jones, Asst. Deputy Director, DCA
Kaila Van Lint, Budget Analyst, DCA
Suzanne Balkis, Budget Manager, DCA
Marcy Larson, Administrative Law Judge, OAH
Matthew Fleming, Deputy Attorney General
Beth Clark, Associate Governmental Program Analyst
Ralph Correa, Probation Monitor
Yuping Lin, Board Counsel
Kristy Schieldge, Regulations Counsel

MEMBERS OF
THE AUDIENCE:

Holly Macriss, Executive Director, OPSC
Michelle Monserratt-Ramos, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Kimberly Turbin, Consumer Watchdog
Tracy Dominguez, Consumer Watchdog

Board Meeting Minutes – November 13, 2025

Agenda Item 1

Call to Order/Roll Call/Establishment of a Quorum

The Quarterly Board Meeting of the Osteopathic Medical Board of California (OMBC)
was called to order by President Denise Pines at 9:00 a.m.

Machiko Chong called roll and determined a quorum was present. The meeting was
held at the Department of Consumer Affairs, Hearing Room HQ1, in Sacramento, CA.

Agenda Item 2

Reading of the Board’s Mission Statement

Executive Director Erika Calderon read the Board’s mission statement: "to protect the
public by requiring competency, accountability, and integrity in the safe practice of
medicine by osteopathic physicians and surgeons"

Agenda Item 3

Public Comment on Items Not on the Agenda

President Pines opened the floor for public comments.

The WebEx moderator checked for online requests; no public comments were made for
items not on the agenda.

Agenda Item 4

Review and Possible Approval of Board Meeting Minute

Beth Clark presented the minutes from the August 14, 2025, Board Meeting.

Public Comment: Holly Macriss (OPSC) requested a correction on page 11 to clarify
that she stated she would be updating the Board on the upcoming osteopath bill, rather
than requesting updates from the Board.

Motion to adopt the August 14, 2025, minutes as amended.

Motion – Dr. Patel Second – Mr. Cummins

•  Aye – Adamyan, Cummins, Lockman, Patel, Pines, Swain
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie

Motion carried to approve the minutes as amended.

Board Meeting Minutes – November 13, 2025

Agenda Item 5:

Hearing on Petition for Early Termination of Probation

Administrative Law Judge (ALJ) Marcy Lawson presided over the hearing for Eman
Abdallah, D.O.

Deputy Attorney General Matthew Fleming represented the People. Dr. Abdallah
represented herself and was sworn in.

Deputy AG Fleming provided a history of the case, noting Dr. Abdallah’s license was
placed on five years of probation in June 2023 for gross negligence and aiding
unlicensed practice at med spas.

Dr. Abdallah testified regarding her rehabilitation, her current ownership of a private
practice where she performs all medical treatments herself, and her improved record-
keeping systems. Deputy AG Fleming recommended the Board continue the probation,
noting it was the earliest possible time for a petition and that the public interest is best
served by allowing the term to play out. The Board took the matter under submission for
deliberation in closed session.

Agenda Item 6:

President’s Report

President Denise Pines reported on:

•  Personnel Changes: Recognition of Andrew Moreno for seven years of service;

welcome to new member Negeen Mirreghabie (spectator online, joining in person in
January).

•  Events: Announcement of "Hill Day" on January 21, 2026, to meet with legislators.

•

International/National: Updates on the Federation of State Medical Boards (FSMB)
meeting in Dublin regarding medical racism standards and the emerging licensing
pathway for "assistant physicians".

•  DCA Leadership: Acknowledgment of DCA Director Kimberly Kirchmeyer’s

upcoming retirement.

•  Public Comment: Representatives from Consumer Watchdog criticized the use of
clinical terminology such as "cradle to the grave" and requested that enforcement
committee meetings be held in public.

Agenda Item 7:

Board Member Communications with Interested Parties

President Pines requested disclosures. No board members reported communications.

Board Meeting Minutes – November 13, 2025

Agenda Item 8:
Services Update

Intergovernmental Relations Reports and Administrative

•  DCA Update: Shelly Jones reported on the appointment of Lucy Saldivar as Deputy
Director of Board and Bureau Relations and provided updates on mandatory training
(Sexual Harassment Prevention and Unconscious Bias).

•  Budget Update: Kaila Van Lindt reported the Board ended FY 24/25 with

approximately 12.4 months in reserve. However, future expenditures are projected to
increase by 3% annually while revenues remain static.

Agenda Item 9:

Executive Director’s Report

Erika Calderon introduced new staff members Rachel Molina (Enforcement Analyst)
and Yvonne Almazan (Special Investigator).

She noted that enforcement staff have returned to the office three days per week for
onboarding and collaboration.

Agenda Item 10:  Licensing/Admin Program Summary

Machiko Chong reported a total population of 17,012 licensed D.O.s. Total applications
are up 17% overall.

Revisions were made to FNP applications to clarify requirements for various filing types.

Agenda Item 11:  Enforcement Program Summary

Cristy Livramento reported 320 complaints received this quarter, a 33% increase from
the previous year.

Referred cases to the AG doubled compared to the same quarter last year.

Public Comment: Consumer Watchdog volunteers shared personal stories regarding
the impact of physician negligence and requested transparency in case management.

Agenda Item 12:  Probation Program Summary

Ralph Correa reported 31 active probationers.

Board Meeting Minutes – November 13, 2025

He detailed field monitoring efforts, including unannounced visits to ensure compliance
with cease practice orders.

Agenda Item 13:  Rulemaking Update

Terri Thorfinnson confirmed that the prior regulatory package became effective October
1, 2025.

The Fee and License Status package and Disciplinary Guidelines are currently in
progress

Agenda Item 14:  Discussion and Possible Action to Consider Initiation of a
Rulemaking to Amend Sections 1630, 1636, 1646, 1647, 1656, 1658, and 1690,
and to Adopt Section 1648 in Division 16 of Title 16 of the California Code of
Regulations (CCR) (Retired License, Petitions and Fees)

Terri Thorfinnson presented an overview of the proposed regulatory changes, which are
set forth in the meeting materials. For this package, the Board reviewed a trimmed
down version of a prior approved rulemaking package from August of 2025. The focus
of this rulemaking is solely fee increases, specifically to raise fees to the statutory
maximums authorized by law, set a retired license status, and set petition fees to
include adjudication fees previously not considered by the Board.

Board staff noted that in the prior version adopted by the Board in August of 2025, staff
was overly ambitious and diverted the attention from the fees and priority of the
increase of these fees to also focus on making some amendments to application
language. However, it was noted that further changes in the application language were
needed after the compilation of the package. The Board’s Executive Director did not
want further delays to this critical fee rulemaking and recommended removing
amendments that did not otherwise relate to fee increases or address the Board’s long-
standing goal of establishing a retired license and establish its petition fees, so it was
decided to present the Board with this trimmed down version; application amendments
will be addressed in a separate package at a later time. This proposed language is the
result of that recommendation.

Action Requested: The Board should review the proposed regulatory text and the
attachments and consider whether they would support the proposed text as written or if
there are suggested changes to the proposed text. After review, the staff requested that
the Board consider one of the motions as set forth in the meeting materials.

Ms. Thorfinnson presented the key details of the proposed amendments as set forth in the
meeting materials in her memorandum to the Board.

Board Discussion: Dr. Lockman raised concerns about CME and the lack of available AOA
category 1A CME specific to specialties. Regulations Counsel clarified that the Board is not
addressing CME with this regulatory package and suggested that Dr. Lockman raise the
concern regarding dedicated CME and Category 1A CME issues for a possible future meeting
and agenda item.

Board Meeting Minutes – November 13, 2025

Dr. Lockman raised concerns about financial hardship for petitioners. Counsel Schieldge
explained that under this proposal, petition fees would shift the cost burden from the general
licensee population (since all costs by the Board are currently paid out of one Fund) to the
individual requesting to petition the Board.  Furthermore, the Board supported the legislation to
recover costs for petitions, so staff are simply trying to implement the policy supported by the
Board.

Dr. Lockman raised additional concerns stating that Board staff is arguing that the collection of
the adjudication fees will prevent the Board from requesting a fee increase however the Board
is already seeking a fee increase to get its fees statutorily capped out, but the Board may also
need an additional statutory fee increase down the road. The question was raised as to when
we will know how to stop asking for increases.

Counsel Schieldge indicated that the Board has never requested petition fees so the Board’s
staff are unable to determine where the Board’s budget will be if it starts collecting those
petition fees. What the Board knows now is that the Board is spending more than the Board is
bringing in and the Board currently has a structural imbalance. The goal of this proposal is to
raise all fees to current statutory caps to see if further fee increases are necessary. Executive
Director Calderon also noted that the Board has not raised fees since 1994 and that the Board
is projected to be in deficit (one month in reserve) in 2027. Ms. Thorfinnson stressed that the
Board needs to raise fees under its current authority first before asking for any further
legislative assistance to correct any continuing structural imbalance.

Mr. Cummins asked a clarifying question about the adjudication fee. He asked if the petition
costs are more than $20,000.00 what happens. Ms. Thorfinnson responded by saying that the
Board would absorb the costs. Counsel Schieldge further explained that the Board could
revaluate this cost at a later time after obtaining data showing the need for an increase, and
consider doing another rulemaking to raise the fee.

Motion – Dr. Swain Second – Mr. Cummins to:
Approve the proposed regulatory text in Attachments 1-5 including the adoption and repeal of
the forms incorporated by reference in Attachments 2-5 and to submit the text to the Director of
the Department of Consumer Affairs and the Business, Consumer Services, and Housing
Agency for review and if no adverse comments are received, authorize the Executive Director
to take all steps necessary to initiate the rulemaking process, make any non-substantive
changes to the text and the package and set the matter 

*[document truncated for length]*

---

**[MINUTES] 2026-04-23_20260423_mat_7b.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390    |    F (916) 928-8392    |    www.ombc.ca.gov

Osteopathic Medical Board of California

 Teleconference Minutes

January 22, 2026

MEMBERS
PRESENT:

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Brett Lockman, D.O.

STAFF
PRESENT:

Erika Calderon, Executive Director
Yuping Lin, Esq., Legal Counsel
Machiko Chong, SSM I, Licensing Unit
Cristy Livramento, SSM I, Enforcement Unit
Terri Thorfinnson, SSM I, Legislative and Regulatory Specialist
Beth Clark, Analyst II
Ralph Correa, Probation Monitor
Shelley Jones, Assistant Deputy Director, Board and Bureau
Relations, DCA
Kayla Van Lint, Budget Analyst, DCA Budget Office
Brad Lencioni, Budget Manager, DCA

MEMBERS OF
THE AUDIENCE:

Holly Macriss, Executive Director, OPSC
Michele Monserratt-Ramos, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Tracy Dominguez, Consumer Watchdog
Sarah Irani, Analyst II, DCA Moderator

Board and Committee Meeting Minutes – January 22, 2025

Agenda Item 1

Call to Order and Roll Call/Establishment of a Quorum

The Quarterly Board Meeting of the Osteopathic Medical Board of California (OMBC)
was called to order by President Denise Pines at 9:03 a.m. on Thursday, January 22,
2026, in the Hearing Room of the Department of Consumer Affairs (DCA)
Headquarters, 1740 N. Market Blvd., Sacramento, California, and via Webex. President
Pines reviewed meeting protocols under the Bagley-Keene Open Meeting Act, including
public comment procedures and time limits. Machiko Chong called roll. A quorum of
Board members was established.

Agenda Item 2

Reading of the Board’s Mission Statement

Executive Director Erica Calderon read the Board’s mission statement: "to protect the
public by requiring competency, accountability, and integrity in the safe practice of
medicine by osteopathic physicians and surgeons".

Agenda Item 3

Public Comment for Items not on the Agenda

President Pines opened the floor for public comments regarding items not listed on the
agenda.

The Webex moderator provided instructions for submitting comments online.

No requests for public comment were made online or in person.

Agenda Item 4

Review and Possible Approval of Minutes

Beth Clark presented the draft minutes from November 13, 2025, Board Meeting. Ms.
Clark walked through the document page-by-page and invited corrections and
clarifications. One correction was noted to the subtitle to read "teleconference minutes".
After discussion, the Board considered approval of the minutes as amended.

Motion to approve November 13, 2025, minutes as amended.

Motion – Dr. Patel Second – Mr. Cummins

•  Aye – Adamyan, Cummins, Lockman, Patel, Pines
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie, Matthew Swain

Motion carried to approve the November 13, 2025, minutes as amended.

No public comments were made on this item.

Board and Committee Meeting Minutes – January 22, 2025

Agenda Item 5

President’s Report

President Pines provided an overview of Board activities during the past quarter and
noted ongoing coordination with Executive Director Calderon to advance Board
priorities. She announced her reappointment by the Governor and expressed
appreciation for the continued opportunity to serve.

Key updates included:

o  Reappointment: President Pines announced her reappointment by the
Governor to serve another term on the Board and expressed her sincere
appreciation for the continued trust and opportunity to serve in her role.

o

Inaugural Hill Day: On January 21, 2026, the Board held its first "Hill
Day." A delegation consisting of Dr. Patel, Mr. Adamyan, and Mr.
Cummins met with state legislators to provide an overview of the D.O.
profession and build support for future legislation to protect the
professional designation.

o  FSMB Updates: Ms. Pines will attend a Federation of State Medical

Boards (FSMB) meeting in late February, following a working session in
New Orleans focused on trauma-informed care. She also noted that the
FSMB Office of AI Innovation continues to monitor evolving artificial
intelligence regulations.

No public comments were made.

Agenda Item 6

Board Member Communications with Interested Parties

President Pines requested disclosures regarding Board member communications with
interested parties, including meetings with legislators or other external engagements
related to OMBC matters. No Board members reported communications requiring
disclosure.

No public comments were made.

Agenda Item 7
Services Update

Intergovernmental Relations Reports and Administrative

7A. Department of Consumer Affairs (DCA) Update
Shelly Jones, Assistant Deputy Director of Board and Bureau Relations, provided the
Department of Consumer Affairs (DCA) update and congratulated President Pines on
her reappointment.

Board and Committee Meeting Minutes – January 22, 2025

Ms. Jones reported on the following:

o  Leadership: Christine Lally has been appointed Acting Director of the DCA

following the retirement of Kimberly Kirchmeyer.

o  Governor’s 2026–27 Budget: The proposed budget is balanced.

o  Agency Reorganization: The former Business, Consumer Services and

Housing Agency is being divided into two entities. DCA will transition to the
newly established Business and Consumer Services Agency, with
implementation anticipated July 1, 2026.

o  Wildfire Executive Order: A one-year renewal fee postponement was

authorized for licensees impacted by the Los Angeles wildfires.

o  Compliance and Administrative Reminders:

  Form 700 filings are due April 1 through the FPPC e-filing system.
  Required trainings include Unconscious Bias and Board Member

Orientation.

  Travel and operational spending remain subject to Department of

Finance guidance.

No public comment was received.

7B. Budget Office Update

Budget Status:
Kaila Van Lindt and Brad Lencioni presented the Board’s fiscal status and projections.

  Authorized Budget: $4.333 million
  Projected Expenditures: $4.915 million
  Projected Reversion: 0.78% (after AG and HQIU cost augmentations)

Fund Condition:

o  Fiscal Year 2024–25 year-end reserve: $4.943 million (approximately 10.5

months).

o  Current year projected reserve: approximately 7.4 months.

Staff confirmed ongoing monitoring of expenditures to ensure fiscal stability and
compliance with state financial directives.

Board and Committee Meeting Minutes – January 22, 2025

Agenda Item 8

Executive Director’s Report

Executive Director Erika Calderon provided a comprehensive update on Board
operations, personnel matters, and ongoing interagency efforts.
Ms. Calderon began by recognizing Acting DCA Director Christine Lally and expressing
appreciation for her leadership and mentorship. She also announced the retirement of
Kathleen Nicholls, former Chief of the Department’s Division of Investigation,
acknowledging her more than 30 years of service in enforcement and investigative
work, including her prior leadership role within the Health Quality Investigation Unit
(HQIU).

Personnel and Organizational Updates
Ms. Calderon reported on recent statewide classification changes that took effect in
January 2026, including the consolidation of analyst and managerial classifications:

o  Staff Services Manager (SSM) classifications were converted to Manager I and

Manager II.

o  Associate Governmental Program Analysts (AGPA) were reclassified as Analyst II.

o  Staff Services Analysts (SSA) were reclassified as Analyst I.

She reviewed the Board’s authorized staffing levels and discussed operational
considerations, including the use of a limited-term Special Investigator to support
enforcement functions. She noted that resource constraints continue to impact workload
distribution and case processing timelines.

Enforcement and Interagency Coordination
Ms. Calderon emphasized ongoing coordination with the Attorney General’s Office and
HQIU to prioritize high-risk cases and matters approaching statute-of-limitations
deadlines. She reported that she and Enforcement Manager Cristy Livramento continue
to meet regularly with enforcement partners to ensure timely case review and
appropriate resource allocation.

Additionally, she referenced a joint forum held on December 17, 2025, with other
prescribing boards to discuss access to controlled substances and related regulatory
considerations. She also noted continued engagement with Consumer Watchdog
representatives to receive stakeholder input regarding enforcement practices and
consumer protection priorities.

Public Comment
Michelle Monserratt-Ramos (Consumer Watchdog) congratulated President Pines on
her reappointment, expressed appreciation for the Board’s continued focus on

Board and Committee Meeting Minutes – January 22, 2025

consumer protection, and recognized Kathleen Nicholls for her longstanding service and
retirement.

Holly Macriss (Osteopathic Physicians and Surgeons of California – OPSC) also
congratulated President Pines and thanked Board leadership for its ongoing outreach
and collaboration with licensees and association members. She noted that OMBC
leadership is anticipated to participate in an upcoming OPSC convention panel
addressing professional identity and the practice of medicine.

Agenda Item 9

Possible Action to Revise the 2024-2028 Strategic Plan

Executive Director Erika Calderon and staff presented proposed revisions to the
Osteopathic Medical Board of California’s 2024–2028 Strategic Plan. The proposed
updates included clarifying strategic objectives, refining language for improved
readability, and updating Board member information to ensure the document accurately
reflects the Board’s current composition and priorities.

Ms. Calderon explained that the revision process included review by the Executive
Committee and consideration of stakeholder input. The updates were intended to
enhance public-facing clarity while ensuring the Strategic Plan remains consistent with
the Board’s statutory authority and does not imply responsibilities beyond its regulatory
mandate.

Board members discussed the importance of clearly articulating OMBC’s mission,
consumer protection role, and enforcement authority. Particular attention was given to
ensuring that terminology accurately reflects the Board’s jurisdiction and responsibilities,
and that the final document is accessible and understandable to non-board audiences.

Public comments were received as follows:

•  Michelle Monserratt-Ramos (Consumer Watchdog) expressed appreciation for

the emphasis on public safety and consumer protection throughout the Strategic
Plan.

•  Holly Macriss (Osteopathic Physicians and Surgeons of California – OPSC)

raised questions regarding specific wording and requested that final language be
carefully reviewed to ensure clarity for stakeholders and licensees. She noted
that reviewing the text visually during the meeting was helpful and thanked staff
for the opportunity to provide input.

•  Tracy Domingues (Consumer Watchdog) requested clarification regarding the

sequencing of the agenda items.

Staff confirmed that, upon Board approval, the Strategic Plan would be finalized to
reflect the discussion and published on the Board’s website for public access.

Board and Committee Meeting Minutes – January 22, 2025

Motion to approve the proposed updates to the OMBC 2024–2028 Strategic Plan
and authorize the Executive Director to finalize and publish the revised plan.

Motion – Mr. Cummins Second – Dr. Patel

•  Aye – Adamyan, Cummins, Lockman, Patel, Pines
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie, Matthew Swain

Motion carried to approve the Strategic Plan updates and authorize publication of the
revised plan.

Agenda Item 10   Licensing Program

*[document truncated for length]*

---

**[MINUTES] 2026-04-23_20260423_mat_10b.pdf**

Department of Consumer Affairs

Expenditure Projection Report
Osteopathic Medical Board
Reporting Structure(s): 11112600 Support
Fiscal Month: 8
Fiscal Year: 2025 - 2026
Run Date:  03/13/2026

PERSONAL SERVICES

Fiscal Code

Line Item

5100  PERMANENT POSITIONS
5100  TEMPORARY POSITIONS
5105-5108  PER DIEM, OVERTIME, & LUMP SUM
5150  STAFF BENEFITS
PERSONAL SERVICES

PY Budget
$1,180,000
$0
$3,000
$766,000
$1,949,000

PY FM13
$1,226,342
$68,022
$1,800
$731,495
$2,027,660

Budget
$1,206,000
$0
$3,000
$811,000
$2,020,000

Current Month
$104,016
$8,856
$2,200
$66,425
$181,497

YTD
$817,931
$52,111
$2,200
$528,212
$1,400,454

Encumbrance  YTD + Encumbrance

$0
$0
$0
$0
$0

$817,931
$52,111
$2,200
$528,212
$1,400,454

Projections to Year End
$1,256,075
$86,550
$3,000
$815,122
$2,160,746

Balance
-$50,075
-$86,550
$0
-$4,122
-$140,746

OPERATING EXPENSES & EQUIPMENT

Fiscal Code

Line Item

5301  GENERAL EXPENSE
5302 PRINTING
5304 COMMUNICATIONS
5306 POSTAGE
53202-204  IN STATE TRAVEL
53206-208  OUT OF STATE TRAVEL
5322 TRAINING
5324  FACILITIES
53402-53403  C/P SERVICES (INTERNAL)

5340310000

Legal - Attorney General

53404-53405  C/P SERVICES (EXTERNAL)
5342  DEPARTMENT PRORATA

5342500092

Invest Svs-HQIU

Fiscal Code

Line Item

5342  DEPARTMENTAL SERVICES
5344 CONSOLIDATED DATA CENTERS
5346 INFORMATION TECHNOLOGY
5362-5368  EQUIPMENT
54  SPECIAL ITEMS OF EXPENSE
OPERATING EXPENSES & EQUIPMENT

PY Budget
$127,000
$28,000
$24,000
$10,000
$22,000
$0
$9,000
$128,000
$1,094,000
$741,000
$205,000
$555,000
$0

PY Budget
$3,000
$15,000
$10,000
$30,000
$0
$2,260,000

PY FM13
$28,107
$18,708
$1,907
$11,337
$28,467
$2,048
$1,000
$76,454
$844,337
$674,865
$187,985
$1,003,064
$530,194

PY FM13
$864
$1,275
$18,311
$36,507
$680
$2,261,050

Budget
$127,000
$28,000
$24,000
$10,000
$22,000
$0
$9,000
$128,000
$800,000
$741,000
$178,000
$984,000
$294,000

Budget
$3,000
$15,000
$10,000
$28,000
$0
$2,366,000

Current Month
$98
$55
$229
$10,000
$3,188
$0
$0
$5,997
$83,454
$81,002
$10,125
$0
$0

Current Month
$24
$0
$6,152
$6,366
$389
$126,077

YTD
$13,080
$1,495
$2,256
$10,016
$12,516
$0
$0
$46,856
$447,503
$431,054
$85,364
$795,764
$269,264

YTD
$432
$0
$14,938
$7,367
$389
$1,437,976

Encumbrance  YTD + Encumbrance

$2,471
$14,244
$0
$585
$0
$0
$0
$23,168
$0
$0
$27,292
$0
$0

$15,552
$15,739
$2,256
$10,601
$12,516
$0
$0
$70,025
$447,503
$431,054
$112,657
$795,764
$269,264

Encumbrance  YTD + Encumbrance

$0
$0
$1,866
$27,263
$0
$96,890

$432
$0
$16,804
$34,630
$389
$1,534,866

Projections to Year End
$28,662
$15,739
$3,722
$11,375
$29,000
$4,000
$0
$71,072
$797,249
$770,351
$190,456
$1,643,367
$953,367

Projections to Year End
$1,000
$1,275
$22,632
$51,972
$700
$2,872,221

Balance
$98,338
$12,261
$20,278
-$1,375
-$7,000
-$4,000
$9,000
$56,928
$2,751
-$29,351
-$12,456
-$659,367
-$659,367

Balance
$2,000
$13,725
-$12,632
-$23,972
-$700
-$506,221

OVERALL TOTALS

$4,209,000

$4,288,710

$4,386,000

$307,574

$2,838,430

$96,890

$2,935,320

$5,032,967

-$646,967

REIMBURSMENTS
OVERALL NET TOTALS

-$53,000
$4,156,000

-$108,000
$4,180,710

-$53,000
$4,333,000

$307,574

$2,838,430

$96,890

$2,935,320

-$53,000
$4,979,967

-$646,967

-14.93%

Includes the following options
Overall net total
AG Augmentation
HQIU Augmentation

$  (646,967)
29,351
$
659,367
$
41,751
$

Department of Consumer Affairs

Expenditure Projection Report
Osteopathic Medical Board
Reporting Structure(s): 11112600 Support
Fiscal Month: 8
Fiscal Year: 2025 - 2026
Run Date:  03/13/2026

PERSONAL SERVICES

Fiscal Code

Line Item

5100  PERMANENT POSITIONS
5100  TEMPORARY POSITIONS
5105-5108  PER DIEM, OVERTIME, & LUMP SUM
5150  STAFF BENEFITS
PERSONAL SERVICES

PY Budget
$1,180,000
$0
$3,000
$766,000
$1,949,000

PY FM13
$1,226,342
$68,022
$1,800
$731,495
$2,027,660

Budget
$1,206,000
$0
$3,000
$811,000
$2,020,000

Current Month
$104,016
$8,856
$2,200
$66,425
$181,497

YTD
$817,931
$52,111
$2,200
$528,212
$1,400,454

Encumbrance  YTD + Encumbrance

$0
$0
$0
$0
$0

$817,931
$52,111
$2,200
$528,212
$1,400,454

Projections to Year End
$1,256,075
$86,550
$3,000
$815,122
$2,160,746

Balance
-$50,075
-$86,550
$0
-$4,122
-$140,746

OPERATING EXPENSES & EQUIPMENT

Fiscal Code

Line Item

5301  GENERAL EXPENSE
5302 PRINTING
5304 COMMUNICATIONS
5306 POSTAGE
53202-204  IN STATE TRAVEL
53206-208  OUT OF STATE TRAVEL
5322 TRAINING
5324  FACILITIES
53402-53403  C/P SERVICES (INTERNAL)

5340310000

Legal - Attorney General

53404-53405  C/P SERVICES (EXTERNAL)
5342  DEPARTMENT PRORATA

5342500092

Invest Svs-HQIU

5342  DEPARTMENTAL SERVICES
5344 CONSOLIDATED DATA CENTERS
5346 INFORMATION TECHNOLOGY
5362-5368  EQUIPMENT
54  SPECIAL ITEMS OF EXPENSE
OPERATING EXPENSES & EQUIPMENT

PY Budget
$127,000
$28,000
$24,000
$10,000
$22,000
$0
$9,000
$128,000
$1,094,000
$741,000
$205,000
$555,000
$0
$3,000
$15,000
$10,000
$30,000
$0
$2,260,000

PY FM13
$28,107
$18,708
$1,907
$11,337
$28,467
$2,048
$1,000
$76,454
$844,337
$674,865
$187,985
$1,003,064
$530,194
$864
$1,275
$18,311
$36,507
$680
$2,261,050

Budget
$127,000
$28,000
$24,000
$10,000
$22,000
$0
$9,000
$128,000
$830,000
$771,000
$178,000
$1,643,000
$953,000
$3,000
$15,000
$10,000
$28,000
$0
$3,055,000

Current Month
$98
$55
$229
$10,000
$3,188
$0
$0
$5,997
$83,454
$81,002
$10,125
$0
$0
$24
$0
$6,152
$6,366
$389
$126,077

YTD
$13,080
$1,495
$2,256
$10,016
$12,516
$0
$0
$46,856
$447,503
$431,054
$85,364
$795,764
$269,264
$432
$0
$14,938
$7,367
$389
$1,437,976

Encumbrance  YTD + Encumbrance

$2,471
$14,244
$0
$585
$0
$0
$0
$23,168
$0
$0
$27,292
$0
$0
$0
$0
$1,866
$27,263
$0
$96,890

$15,552
$15,739
$2,256
$10,601
$12,516
$0
$0
$70,025
$447,503
$431,054
$112,657
$795,764
$269,264
$432
$0
$16,804
$34,630
$389
$1,534,866

Projections to Year End
$28,662
$15,739
$3,722
$11,375
$29,000
$4,000
$0
$71,072
$797,249
$770,351
$190,456
$1,643,367
$953,367
$1,000
$1,275
$22,632
$51,972
$700
$2,872,221

Balance
$98,338
$12,261
$20,278
-$1,375
-$7,000
-$4,000
$9,000
$56,928
$32,751
$649
-$12,456
-$367
-$367
$2,000
$13,725
-$12,632
-$23,972
-$700
$182,779

OVERALL TOTALS

$4,209,000

$4,288,710

$5,075,000

$307,574

$2,838,430

$96,890

$2,935,320

$5,032,967

$42,033

REIMBURSMENTS
OVERALL NET TOTALS

-$53,000
$4,156,000

-$108,000
$4,180,710

-$53,000
$5,022,000

$307,574

$2,838,430

$96,890

$2,935,320

-$53,000
$4,979,967

$42,033

0.84%

Department of Consumer Affairs

Revenue Projection Report

Reporting Structure(s): 11112600 Support
Fiscal Month:
Fiscal Year: 2025 - 2026
Run Date:  03/13/2026

Revenue

Line Item

Fiscal Code
Delinquent Fees
Other Regulatory Fees
Other Regulatory License and Permits
Other Revenue
Renewal Fees
Revenue

Budget
$24,000
$70,000

July
$1,925
$5,150

$1,127,000  $177,414
$139,000
$2,451,000  $313,729
$3,811,000  $498,782

$564

August
$2,550
$2,175
$87,598
$25
$296,600
$388,948

September
$1,025
$1,788
$85,224
$25
$217,430
$305,492

October
$2,525
$4,900
$78,011
$55,204
$209,365
$350,005

November  December

$2,075
$1,625
$54,979
$2,444
$219,075
$280,198

$2,375
$4,525
$80,514
$0
$138,686
$226,100

January
$2,375
$3,450
$85,711
$55,058
$253,659
$400,253

April
$2,200
$3,575

February
$1,975
$4,425
$77,950
$365

June
March
$2,000
$1,600
$3,300
$4,050
$73,400  $71,738  $75,588  $71,850

Year to Date
$16,825
$28,038
$727,401
$113,685
$204,182  $160,600  $151,400  $189,200  $150,300  $1,852,726
$288,897  $239,650  $273,913  $270,613  $227,450  $2,738,675

May
$1,700
$3,700

$45,000

$425

$0

$0

Projection To Year End

$24,325
$42,663
$1,019,977
$159,110
$2,504,226

$3,750,301

0264 - Osteopathic Medical Board of California Fund
Analysis of Fund Condition
(Dollars in Thousands)
2026-27 Governor's Budget with FM 8 Projections + Anticipated Augmentations

Column1

BEGINNING BALANCE

Prior Year Adjustment
Adjusted Beginning Balance

REVENUES, TRANSFERS AND OTHER ADJUSTMENTS

Revenues

4121200 - Delinquent fees
4127400 - Renewal fees
4129200 - Other regulatory fees
4129400 - Other regulatory licenses and permits
4163000 - Income from surplus money investments
4171400 - Escheat of unclaimed checks and warrants
4171500 - Escheat Unclaimed Property

Prepared 03.20.2026

 Actuals
2024-25

CY
2025-26

BY
2026-27

 BY +1
2027-28

$  5,050  $  4,943  $  3,637  $
$
-
$
$  5,098  $  4,943  $  3,637  $

48  $

$

-

28  $

24  $

22  $

$
25  $
$  2,737  $  2,504  $  2,983  $
107  $
$
$  1,096  $  1,020  $  1,161  $
131  $
$
$
-
$
$
-
$

233  $
2  $
1  $

157  $
2  $
$

43  $

-

3,105
-
3,105

25
2,983
107
1,161
101
-
-

Totals, Revenues

$  4,119  $  3,750  $  4,407  $

4,377

TOTALS, REVENUES, TRANSFERS AND OTHER ADJUSTMENTS

$  4,119  $  3,750  $  4,407  $

4,377

TOTAL RESOURCES

Expenditures:

1111 Department of Consumer Affairs (State Operations)
2025-26 AG and HQIU Augmentations
9892 Supplemental Pension Payments (State Operations)
9900 Statewide General Administrative Expenditures (Pro Rata) (State Operations)

$  9,217  $  8,693  $  8,044  $

7,482

-

$  4,057  $  4,126  $  4,556  $
$
$
-
-
$
$
383  $
$

689  $
-
$
241  $

$
12  $
205  $

4,693
-
-
383

TOTALS, EXPENDITURES AND EXPENDITURE ADJUSTMENTS

$  4,274  $  5,056  $  4,939  $

5,076

FUND BALANCE

Reserve for economic uncertainties

Months in Reserve

$  4,943  $  3,637  $  3,105  $

2,406

11.7

8.8

7.3

5.5

NOTES:
1. Assumes workload and revenue projections are realized in BY+1 and ongoing.
2. Expenditure growth projected at 3% beginning BY+1.

---

**[MINUTES] 2026-04-23_20260423_mat_12.pdf**

Osteopathic Medical Board of California

Agenda Item 12

DATE REPORT ISSUED:
ATTENTION:
SUBJECT:
STAFF CONTACT:

  April 23, 2026
Members, Osteopathic Medical Board of California
Executive Report
Erika Calderon, Executive Director

REQUESTED ACTION:

This report provides an update on personnel, administrative functions, and ongoing projects for
the  Osteopathic  Medical  Board  of  California  (OMBC).  No  action  is  required  from  the  Board
Members.

Board Member Appointment

On  March  20,  2026,  Dr.  Faisal  Qazi  of  Fullerton  was  appointed  to  the  Osteopathic  Medical
Board.

Dr. Qazi's extensive experience in the field of neurology includes his roles as:

Institutional Officer for the TNG Neurology Residency Program in Pomona since 2021.

•
• Co-Founder of the Neurology Group since 2012.
• Assistant Professor at Western University since 2008.
•

Founder  of  Inland  Neurological  Consultants  Inc.,  since  2006,  where  he  practiced  as  a
Sole Practitioner from 2006 to 2012.

• Associate Professor at the University of California, Riverside from 2018 to 2024.

Dr.  Qazi  is  a  member  of  the  California  Neurology  Society.  He  holds  a  Doctor  of  Osteopathic
Medicine degree from Touro University and a Bachelor of Science degree in Neuroscience from
the University of California, Los Angeles.

Personnel:

The OMBC maintains 15.9 authorized positions, with no current vacancies.

Please refer to the Board’s Organizational Chart for detailed staffing information.

Administrative Functions/Projects:

•  Delinquent  Physician  and  Surgeon  Licenses:  OMBC  staff  are  actively  addressing  delinquent
physician and  surgeon  licenses.  A  comprehensive update will be  provided during  the  licensing
program report.

•  Delinquent  Fictitious  Name  Permits  (FNPs):  Efforts  are  underway  to  resolve  delinquent  FNP

licenses. An update will be presented during the licensing program report.

•  Newsletter:  The  next  edition  of  the  OMBC  newsletter  is  in  production  and  is  scheduled  for

release in September 2026.

Outreach Update:

•  The  OMBC  continues  to  regularly  disseminate  content  across  its  social  media  platforms,
including Facebook, LinkedIn, and X. The Board's website is consistently updated with relevant
legislation, frequently asked questions, publications, and enforcement actions.

•  From February 26 to March 1, 2026, Executive Director Calderon and staff attended OPSC’s 65th
Annual Convention in Carlsbad, California. Director Calderon moderated a panel discussion titled
"Navigating Professional Identity in Medicine," exploring physician self-perception, core values,
ethics,  skills,  and  belonging,  as  well  as  challenges  such  as  diversity,  work-life  integration,  and
evolving roles.

•  Director  Calderon  will  represent  the  OMBC  as  a  voting  delegate  at  the  Federation  of  State
Medical Boards (FSMB) Annual Meeting in Baltimore, Maryland, from April 30 to May 2, 2026.
She  also  plans  to  attend  the  American  Society  of  Osteopathic  Medical  Regulators  (ASOMR)
Annual Meeting on May 1, 2026.

•  Director Calderon and enforcement staff will attend the 5th Annual Latina Maternal Health Fair
in Kern County on May 9, 2026. This event aims to empower Latina mothers through advocacy
and education to promote safe pregnancies and deliveries, addressing high maternal mortality
and morbidity rates in regions like California's Central Valley.

Communication

•  Director Calderon continues to represent the prescribing Boards on the CURES Executive
Stakeholder Committee and maintains regular communication with leadership at the
Department of Consumer Affairs (DCA) and the Department of Justice (DOJ).

•  Ms. Calderon remains an active participant in the DCA’s Med Spa and IV Hydration

taskforce.

•  Ms. Calderon joined the DCA’s Diversity, Equity, Inclusion, and Accessibility (DEIA) steering
committee in December 2025. This committee, established to advance DEIA initiatives
within the Department, comprises departmental leaders and spearheads in efforts to build
a diverse workforce and foster an equitable and inclusive work environment.

•  Director Calderon has engaged in calls and email exchanges with Board President Denise

Pines to discuss pending and ongoing projects and meeting agendas.

•  Periodic meetings with the Board’s Attorney General Liaison, Ms. Karolyn Westfall, and
frequent communication with Senior Assistant Attorney General Ms. Gloria Castro are
ongoing.

•  Director Calderon continues to meet periodically with representatives from the Consumer
Watchdog group to solicit input on improving enforcement practices and procedures.

•  Enforcement staff conduct monthly meetings with the DCA’s Division of Investigations HQIU

office to review the progress of pending investigations.

•  Committee  meetings  have  commenced,  with  Board  leadership  meeting  frequently  with
designated committee members. Staff have also participated in meetings with various local,
state, and national organizations to discuss and establish regulatory measures pertinent to
the OMBC and other similar entities. These organizations include, but are not limited to, the
Office  of  the  Attorney  General  (AGO),  Department  of  Justice  (DOJ),  Department  of
Consumer Affairs (DCA), other healing arts Boards (MBC, BRN, BOP, PAC, PTBC), California
Department  of  Public  Health  (CDPH),  Department  of  Health  Care  Services  (DHCS),  the
Federation  of  State  Medical  Boards  (FSMB),  the  National  Board  of  Osteopathic  Medical
Examiners  (NBOME),  the  International  Association  of  Medical  Regulatory  Authorities
(IAMRA), Osteopathic Physicians and Surgeons of California (OPSC), the American College of
Osteopathic  Family  Physicians  of  California  (ACOFPCA),  and  Premier  Health  (which  now
manages the Board’s diversion program).

---

**[MINUTES] 2026-04-23_20260423_mat_13.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS  •  OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390    |    F (916) 928-8392    |    www.ombc.ca.gov

DATE

TO

FROM

April 23, 2026

Board Members

Machiko Chong
Licensing Program Manager

SUBJECT

Agenda Item #13 – Licensing Program
Summary Attachments 13a & 13b

Licensing Statistics & Program Review

Attachments 12a & 12b reflect the licensing population and application stats for the
first quarter of the 2025/26 Fiscal Year. Currently, there are 17,407 licensed osteopathic
physicians and surgeons; 1,629 postgraduate training licensees (PTL); 1,489  fictitious
name  permits;  and  no  Temporary  Osteopathic  physician  and  surgeon  license.
Overall,  the  Board  has  seen  a  32%  increase  in  applications  received.  There  are
currently  365  pending  initial  applications,  with  44  of  those  requesting  expedited
services. The application breakdown is as follows:

Application Stats

• Postgraduate Training License (44 applications)
• Osteopathic physician and surgeon (313 applications)
•

Fictitious Name Permits (8 applications)

Expedite Service Requests

• Medically Underserved Area (32 applications)
• Military Veteran/Spouse (9 applications)
• Abortion Services (3 applications)

Over  the  past  few  months,  licensing  staff  have  been  working  with  the  BreEZe  Agile
team to either add/remove/amend aspects of the features within the database or
request updates to applicant/licensee transactions with the online BreEZe portal.

At the January Board meeting, I reported that the Board planned to reintroduce its
revised electronic Fictitious Name Permits (FNP) application, which had gone live in
the Fall of 2024. However, the application was removed shortly thereafter for issues
related to the business corporation/shareholder data captured at the time of request,

resulting  in  incorrect  information  being  displayed  in  the  DCA  license  search  when
queried. The revised application went live on February 18th as anticipated and is now
working  as  expected.  Since  that  date,  the  Board  has  received  and  issued  over  79
permits, and transactions have been running smoothly. As a result, we have decided
to  cease  accepting  paper-based  applications,  which  will  in  turn  increase  the
efficiency  of  the  review  process,  enhance  security,  and  reduce  costs  and  our
environmental footprint.

As  we  continue  our  preparation  efforts  to  begin  conducting  licensure  and  permit
auditing  within  the  Licensing  Unit.  Director  Calderon  and  Ms.  Livramento,
Enforcement  Program  Manager,  were  gracious  enough  to  sit  with  a  few  of  the
licensing analysts in March to train us on the citation and fine process and data entry
for  the  Enforcement  tabs  within  BreEZe.  Staff  were  introduced  to  the  citation
documents  and  educated  on  the  internal  referral  and  complaint  creation  process
from beginning to end.

Lastly,  at  the  January  board  meeting,  it  was  reported  that  the  Board  had
approximately  1,946  licensees  that  were  reflected  as  being  in  a  delinquent  status.
Meaning that renewal fees have not been paid by physicians listed in the report for
a period upwards of five (5) years. Upon subsequent review of the data, the reports
indicated that:

Out-Of-State
• 1, 058 – Out-of-state address.

o 171 – Licensees over the age of 70.

In State
• 888 – In-state address.

o 122 – Licensees over the age of 70

As of the current date, the Board has successfully renewed over 294 licenses that had
appeared on the delinquent list. However, an additional 110 licenses have gone into
a  delinquent  status  since  the  last  report  was  run  at  the  beginning  of  February.  The
Board  will  continue  its  efforts  to  address  the  delinquent  licensure  status  of  the  547
physicians  who  still  reside  in  California. We  will  continue  to  provide  updates  on our
progress.

Osteopathic Medical Board of California
Current Licensee Population
Agenda Item 13 (A) -Application Services Stats
Stats FY 25-2026 Q1-Q3

Osteopathic Physician and Surgeon

License Status

Total Licensees

Active
Delinquent/Expired
Inactive
Total:

15,050
1,929
428
17,407

Postgraduate Training License (PTL)

License Status

Total Licensees

Active
Delinquent/Expired
Inactive
Total:

1,625
4
0
1,629

Temporary License

License Status

Total Licensees

Temp Osteopathic Physician and Surgeon
Temp Postgraduate Training License (PTL)
Total:

0
0
0

Fictitious Name Permit

License Status

Total Licensees

Active
Delinquent/Expired
Total:
Total Number of Licensees/Permit Holders

1,127
362
1,489
20,525

---

**[MINUTES] 2026-04-23_20260423_mat_14.pdf**

Briefing Paper Agenda Item 14
Date: April 23, 2026
Prepared for: OMBC Members
Prepared by: Cristy Livramento, Enforcement Program Manager
Subject: Enforcement Program Updates
Purpose: Update on Enforcement Program
Attachments: 14(A) Enforcement Q1-Q3 Stats 2025/2026
Background:
This report provides an overview of the Enforcement Program's activities and
performance for the first three quarters of Fiscal Year 2025-2026, with comparative data
from Fiscal Year 2024-2025.
Please refer to Attachment 14(A) for detailed statistical comparisons.
Analysis:
Despite the temporary absence of an enforcement analyst on leave since early July 2025
(expected return July 2026), the program continues to operate diligently.
Key Activities and Statistics (Q3 FY 2025-2026):
• Complainant Interviews: Thirteen (13) complainant interviews were offered this
quarter. Five (5) were completed, three (3) resulted in no response, and five (5)
are pending due to late mailing of interview notices.
• 805 Reports Received: Three (3) Form 805 reports were received this quarter.
One report was submitted twice, leading to the closure of that case. The remaining
two are under investigation. Year-to-date, thirteen (13) Form 805 reports have
been received, compared to fourteen (14) received during the entirety of the
previous fiscal year.
• Educational Letters Issued: Educational letters are issued for minor violations,
such as record-keeping or communication issues, that do not warrant
administrative citations or disciplinary action. Year-to-date, thirty-nine (39)
educational letters have been issued, a significant increase from the eighteen (18)

issued during the previous fiscal year.
Overall Performance Measures:
• Performance Measure 1 (PM1 - Consumer Complaints, Arrests, and Convictions):
The program has received a total of 913 complaints and 24 arrest/conviction
notices, totaling 937 cases. This represents a 22% increase from the previous
fiscal year's total of 768 cases. This rise is attributed to enhanced outreach efforts
and an expanding licensee population.
• Performance Measure 2 (PM2 - Complaint Initiation and Acknowledgment): The
target for initiating and acknowledging complaints is ten (10) days. The year-to-
date average is five (5) days, exceeding the target.
• Performance Measure 3 (PM3 - Investigation and Enforcement Completion - Non-
AG Referral): The target for completing investigations and enforcement actions for
cases NOT referred to the Attorney General's Office is 360 days. The current year-
to-date average is 223 days, meeting the performance measure. Fluctuations in
this metric are influenced by the inclusion of both desk and formal investigations,
with complex cases potentially skewing the average.
• Performance Measure 4 (PM4 - Investigation and Enforcement Completion - AG
Referral): The target for completing investigations and enforcement actions
referred to the Attorney General's Office is 540 days. The year-to-date average is
616 days, a 33% decrease from 925 days last fiscal year. This measure is
influenced by timelines beyond the Board's direct control, including those of the
Attorney General's Office, respondents’ legal representatives, and the Office of
Administrative Hearings.
Case Inventory:
• Overall Pending Cases: The Board currently has 788 pending enforcement cases,
including 136 pending formal investigations and 21 pending formal discipline.
• Formal Investigations: There has been a 48% increase in pending formal
investigations compared to the previous year.
• Caseload Average: With an analyst on leave, the average caseload per analyst is
currently 262 cases.
Formal Discipline Actions:
Year-to-date, the Board has taken the following actions:
• Filed fifteen (15) accusations (an 88% increase, or seven more, compared to the
previous FY).

• Filed one (1) accusation and petition to revoke probation.
• Issued four (4) public letters of reprimand.
• Placed four (4) licenses on probation.
• Accepted four (4) license surrenders.
• Revoked three (3) licenses.
• Issued twelve (12) administrative citations under the expanded citation authority.
It is noteworthy that while the volume of probation cases has not increased, enforcement
actions, including license surrenders and revocations, have doubled compared to the
previous year.
Action Requested: No Action Required

Osteopathic Medical Board of CA
14 (A) Attachment
Enforcement Performance Measures Q1-3
Enforcement Statistics Report
Complaints
|     |     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Year  →  Year
|                                    |     |     |      |            | Q1   | Q2                     | Q3   | Q4         |     |      |         |      |
| ---------------------------------- | --- | --- | ---- | ---------- | ---- | ---------------------- | ---- | ---------- | --- | ---- | ------- | ---- |
|                                    |     |     | YTD  |            |      |                        |      |            |     | YTD  | Change  |      |
|                                    |     |     |      | Jul - Sep  |      | Oct  - Dec  Jan - Mar  |      | Apr - Jun  |     |      |         |      |
| PM1:  Complaints Received          |     |     | 749  |            | 320  | 310                    | 283  |            |     | 913  |         | 22%  |
| PM1:  Convictions/Arrest Received  |     |     | 19   |            | 7    | 5                      |      | 12         |     | 24   |         | 26%  |
| PM1:  Total Received               |     |     | 768  |            | 327  | 315                    | 295  |            | 0   | 937  |         | 22%  |
Complaint Intake
Fiscal Year 25/26
|                         |                   | FY 24/25  |      |            |     |                        |     |            |     |      | Year  →  Year  |      |
| ----------------------- | ----------------- | --------- | ---- | ---------- | --- | ---------------------- | --- | ---------- | --- | ---- | -------------- | ---- |
|                         | Target:  10 Days  |           |      |            | Q1  | Q2                     | Q3  | Q4         |     |      |                |      |
|                         |                   |           | YTD  |            |     |                        |     |            |     | YTD  | Change         |      |
|                         |                   |           |      | Jul - Sep  |     | Oct  - Dec  Jan - Mar  |     | Apr - Jun  |     |      |                |      |
| PM2:  Intake/Avg. Days  |                   |           | 4    |            | 5   | 5                      |     | 6          |     |      | 5              | 33%  |
Investigations
|                                 |                   | FY 24/25  |      |            |      | Fiscal Year 25/26      |      |            |     |      | Year  →  Year  |       |
| ------------------------------- | ----------------- | --------- | ---- | ---------- | ---- | ---------------------- | ---- | ---------- | --- | ---- | -------------- | ----- |
|                                 | Target: 360 Days  |           |      |            | Q1   | Q2                     | Q3   | Q4         |     |      |                |       |
|                                 |                   |           | YTD  |            |      |                        |      |            |     | YTD  | Change         |       |
|                                 |                   |           |      | Jul - Sep  |      | Oct  - Dec  Jan - Mar  |      | Apr - Jun  |     |      |                |       |
| PM3: Volume                     |                   |           | 694  |            | 315  | 276                    | 271  |            |     | 862  |                | 24%   |
| PM3a:  Intake Only              |                   |           | 3    |            | 5    | 4                      |      | 5          |     |      | 5              | 56%   |
| PM3b:  Investigation Only       |                   |           | 176  |            | 221  | 204                    | 219  |            |     | 215  |                | 22%   |
| PM3c:  Post Investigation Only  |                   |           | 10   |            | 2    | 9                      |      | 2          |     |      |                | -57%  |
4
PM3:  Cycle Time-Investigation  191  228  216  226  223  17%
| ***Pending Formal Investigations  |     |     | 92  | x   |     | x x  |     |     |     | 136  |     | 48%  |
| --------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | ---- |
Transmittals to Attorney General (AG)
|     |     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Year  →  Year
Target:  540 Days
|              |     |     |      |            | Q1  | Q2                     | Q3  | Q4         |     |      | Change  |       |
| ------------ | --- | --- | ---- | ---------- | --- | ---------------------- | --- | ---------- | --- | ---- | ------- | ----- |
|              |     |     | YTD  |            |     |                        |     |            |     | YTD  |         |       |
|              |     |     |      | Jul - Sep  |     | Oct  - Dec  Jan - Mar  |     | Apr - Jun  |     |      |         |       |
| PM4: Volume  |     |     | 13   |            | 8   | 7                      |     | 17         |     |      |         | 146%  |
32
| PM4a: Intake Only           |     |     | 6    |     | 7    | 3    |      | 4   |     |      | 5   | -22%  |
| --------------------------- | --- | --- | ---- | --- | ---- | ---- | ---- | --- | --- | ---- | --- | ----- |
| PM4b:  Investigation Only   |     |     | 490  |     | 460  | 326  | 219  |     |     | 335  |     | -32%  |
| PM4c:  Pre-AG Transmittal   |     |     | 3    |     | 1    | 1    |      | 3   |     |      | 2   | -44%  |
| PM4d:  Post-AG Transmittal  |     |     | 426  |     | 390  | 383  | 105  |     |     | 293  |     | -31%  |
| PM4: Cycle Time-AG          |     |     | 925  |     | 804  | 713  | 332  |     |     | 616  |     | -33%  |
| ***Pending Cases at AGO     |     |     | 21   | x   |      | x x  |      |     |     | 21   |     | 0%    |

Osteopathic Medical Board of CA
14 (A) Attachment
Enforcement Performance Measures Q1-3
Other Legal Actions
|     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |
| --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Year  →  Year
|                                 |      |     | Q1         |     | Q2  Q3                 | Q4         |      |     | Change  |       |
| ------------------------------- | ---- | --- | ---------- | --- | ---------------------- | ---------- | ---- | --- | ------- | ----- |
|                                 | YTD  |     |            |     |                        |            | YTD  |     |         |       |
|                                 |      |     | Jul - Sep  |     | Oct  - Dec  Jan - Mar  | Apr - Jun  |      |     |         |       |
| PC 23 Ordered                   |      | 0   |            | 0   | 0                      | 0          |      | 0   |         | 0%    |
| ISO-Interim Suspension Order    |      | 4   |            | 0   | 0                      | 1          |      | 1   |         | -75%  |
| ASO-Automatic Suspension Order  |      | 0   |            | 0   | 1                      | 0          |      | 1   |         | 0%    |
Actions
|     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |
| --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Year  →  Year
|                                        |      |     | Q1         |     | Q2  Q3                 | Q4         |      |     | Change  |    

*[document truncated for length]*

---

**[MINUTES] 2026-04-23_20260423_mat_14b.pdf**

Osteopathic Medical Board of California

Agenda Item 14(B)

DATE REPORT ISSUED:

April 23, 2026

ATTENTION:
SUBJECT:

Members, Osteopathic Medical Board of California
Executive Report

STAFF CONTACT:

Ralph Correa, Probation Monitor

REQUESTED ACTION:
This report is intended to provide the Members of the Osteopathic Medical Board
of  California  (OMBC)  with  an  update  on  the  probation  program.  No  action  is
needed.

Total Numbers of physicians on probation

As of today’s date, there are 30 licensees on active probation.

• 4 are tolling out of state and are not receiving credit towards completion

of probation.

• 27  active  probationary  cases  are  being  monitored  and  are  practicing

medicine in California.

• 4  physicians  have  received  public  letters  of  reprimand  and  are  being

monitored for course activity completion and or fines.

Review of cases

Quarterly  reviews  are  conducted  both  in  person,  via  zoom  or  telephone  with
each physician to discuss their specific terms and conditions.  All information and
all  documents  are  being  analyzed,  recorded  and documented  in  a  full  report.
The Osteopathic Medical Board’s Probation unit has maintained an effective and
thorough accountability of our physicians on probation.

Non-Compliance

Two (2) cease practice orders have been placed on licensees and petitions for
revocation have been submitted to the Attorney General’s office.

---

**[MINUTES] 2026-04-23_20260423_mat_16.pdf**

DATE April 23, 2026
TO OMBC Board Members, Osteopathic Medical Board of California
Terri Thorfinnson, J.D.
FROM
Legislative and Regulatory Specialist
Agenda Item 16-Rulemaking Update
RE:
Rulemaking Update Summary
The Board has (3) three regulatory packages moving along in the rulemaking process.
The Retired License, Petitions, and Fees:
This regulatory package remains a Board priority. This proposal would: (1) add new renewal and
application requirements and requirements for payment of associated fees that include fee increases,
(2) adopt a new application process and fees for placing a license in retired status and restoring a
retired license to active status, and, (3) adopt new requirements for filing petitions for reinstatement
and modification of penalty (petitions for penalty relief) and set the associated application and
adjudication fees for each type of petition. The Board approved the proposed regulatory language at
the November 13, 2025, Board meeting.
Staff first submitted preliminary drafts of the required rulemaking documents to the Budget and Legal
Offices on December 22, 2025, as part of the review process required by the Director of the
Department of Consumer Affairs (Director) in accordance with Business and Professions Code section
313.1. Section 313.1 requires that any regulation or fee change proposed by departmental boards
(except those about licensing exams/qualifications) must be submitted to the Director for review
before it can be filed with the Office of Administrative Law (OAL). The Director must receive all
required rulemaking documents and has 30 days to disapprove a proposal if it would harm public
health, safety, or welfare.
Over the next two months, the Budget Office staff and Regulations Counsel worked with staff to
complete the package. Regulations Counsel completed her review on February 6, 2026, and the
Budget Office completed their review and approval on February 27, 2026. On March 3, 2026, this
package (currently totaling over one hundred pages) was submitted to the Acting Director for review
and possible approval. This package was split off from the earlier Licensing Updates package, whose
multiple revisions extended the timeline for getting these changes implemented.

Licensing Updates:
This regulatory package is currently on hold pending completion of the Disciplinary Guidelines. The
licensing provisions were previously included within the Retired License, Petitions, and Fees package
but were later separated into a standalone rulemaking action.
Disciplinary Guidelines:
The Disciplinary Guidelines rulemaking package is in the early stages of development. Regulations
Counsel provided staff with a preliminary draft in July 2025, which has been undergoing continuous
revisions in meetings between management, staff, and Regulations Counsel. While progress has taken
longer than anticipated due to the age of the Board’s Guidelines (last updated in 1996) and other
regulations priorities, staff are working to address as many issues as possible before the package is
presented for Enforcement Committee and Board review in the coming months.

| A   | B   | C   | D   | E   | F   | G   | I  J  | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Board/BureauA1:Q1  Rulemaking Title                      S tatus / Location  Concept Date Reg Text   Production   GENERAL NOTES  INITIAL   INITIAL To/From   INITIAL To/From  INITIAL   INITIAL To/From   FINAL Package  FINAL To/From   FINAL To/From   FINAL To/From   FINAL To/From   FINAL to OAL for   OAL One-Year   EFFECTIVE DATE
31  and File No.  Approved  Docs  to/from   Budget                     E  x  e c                     T o   / From   OAL                       S  u  b  m    i s s  i o  n            Attorney                B  u  d  g   e  t        Exec  Agency  review (DOF)             F  il i n  g     D  e  adline         U  p   o  n    F  i l in   g with
Date  Submitted   Attorneys  Agency               P  u  blication   OAL Due Date  GC § 11346.4      SOS
1  Date   Date    (Decision)                  CRITICAL DATES
|                                                                                                        |              |        |            |     |                                     |     |     |     |     |     |     |     |     |     | Withd  | (   |   tifi  ti  |     |
| ------------------------------------------------------------------------------------------------------ | ------------ | ------ | ---------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------- | --- |
| Osteopathic Medical  Disciplinary Guidelines •            C  o  n  c  e  p  t   •    B  o  a  r d      |              |        | 1.31.2020  |     | 9.19-29.23 Board locating 1997      |     |     |     |     |     |     |     |     |     |        |     |             |     |
|                                                                                                        | 16 CCR 1663  | /KS    |            |     | version of reg in order to amend•   |     |     |     |     |     |     |     |     |     |        |     |             |     |
Board
10.9.23 Board text to KS•
11.16.23 KS examples to Board•
3.8.24 Board & KS• 4.16.24
pending fees text approval & CME
pkg submission to Exec• 1.9.25
Board past pkg to KS• 3.5-6.25
KS to Board• 7.4.25 KS to Board•
7.16-17.25 Board & KS•9.12.25
KS to Board•9.22.25 KS to Board
for 9.24.25 mtg•9.24.25 KS to
Board for 9.29.25 mtg• 10.3.25
KS to Board• 10.7.25 KS to Board
for 10.13.25 mtg
141
| Osteopathic Medical   | Licensing Updates (fka                       | ON HOLD               | 1.1.2024  8.14.25  Board  | 5.8.2025•  | 2.1.24 kick-off set for 2.15.24      |     | 2.27-28.2024       |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | -------------------------------------------- | --------------------- | ------------------------- | ---------- | ------------------------------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Board                 | "Applications, Fees and                      | (2.24.26) until DGs   | approved                  |            | including Board, KS & Budgets•       |     | Budgets & Board•   |     |     |     |     |     |     |     |     |     |     |     |
|                       | Processing Times", and                       | completed•            | revised text•             |            | 2.16.24 per kick-off Board to        |     | 6.5.2024 &         |     |     |     |     |     |     |     |     |     |     |     |
|                       | “Application Fees, Retired                   | Concept•  /KS         |                           |            | conduct desk audit & confer w/ KS    |     | 7.10.2024 to       |     |     |     |     |     |     |     |     |     |     |     |
|                       | License and Processing                       |                       |                           |            | in April• 2.28.24 Board to KS• 4.12- |     | Budgets• 7.16-     |     |     |     |     |     |     |     |     |     |     |     |
|                       | Times") (Merged - Includes                   |                       |                           |            | 17.24 KS & Board for 8.15.24         |     | 18.2024 Budgets    |     |     |     |     |     |     |     |     |     |     |     |
|                       | License Renewal & Retired                    |                       |                           |            | Board mtg• 6.5.24 Board drafts to    |     | & Board• 1.10-     |     |     |     |     |     |     |     |     |     |     |     |
|                       | License & Mod of Penalty                     |                       |                           |            | KS• 7.16.24 missing docs to KS•      |     | 22.2025 Board &    |     |     |     |     |     |     |     |     |     |     |     |
|                       | Fee above)•                                  |                       |                           |            | 7.22.24 KS & Board• 7.26.24 KS       |     | Budgets• 5.8.2025  |     |     |     |     |     |     |     |     |     |     |     |
|                       | 16 CCR 1609, 1610,1611,                      |                       |                           |            | to Board• 8.2-12.24 Board & KS•      |     | to Budgets• 6.19-  |     |     |     |     |     |     |     |     |     |     |     |
|                       | 1612, 1613, 1615, 1628,                      |                       |                           |            | 1.21-22.25 KS & Board• 5.8.25        |     | 20.2025 Budgets    |     |     |     |     |     |     |     |     |     |     |     |
|                       | 1630, 1637, 1646, 1647,                      |                       |                           |            | Board to KS• 7.8-10.25 KS &          |     | & Board• 7.8-      |     |     |     |     |     |     |     |     |     |     |     |
|                       | 1648, 1650, 1651, 1656,                      |                       |                           |            | Board• 7.23.25 KS & Board•           |     | 23.2025 Budgets,   |     |     |     |     |     |     |     |     |     |     |     |
|                       | 1658, 1678, 1690, 1691                       |                       |                           |            | 7.29.25 KS to Board• 8.14.25         |     | KS & Board•        |     |     |     |     |     |     |     |     |     |     |     |
|                       |                                              |                       |                           |            | Board approved revised text•         |     | 10.28.25 Board &   |     |     |     |     |     |     |     |     |     |     |     |
Budgets mtg•
2.4.26 Board to
Budgets•
142
| Osteopathic Medical   | Retired License, Petitions &   | Production•  Exec   | 9.10.25  11.13.25 Board  |     | 9.10.25 mtg. with Board, Budgets                |     | 2.6.26 KS to 10.27.25 Initial to  | 3.3.26 to Exec•  |     |     |     |     |     |     |     |     |     |     |
| --------------------- | ------------------------------ | ------------------- | ------------------------ | --- | ----------------------------------------------- | --- | --------------------------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Board                 | Fees •                         |  16  /KS            | approved text            |     | & KS• 10.13.25 KS revised text to Board (full   |     | Budgets• 10.28.25                 |                  |     |     |     |     |     |     |     |     |     |     |
|                       | CCR 1630, 1637, 1646,          |                     |                          |     | Board• 10.14.25 Board to KS•                    |     | re-write)•   mtg with Budgets•    |                  |     |     |     |     |     |     |     |     |     |     |
|                       | 1647, 1648, 1656, 1658,        |                     |                          |     | 10.15.25 Board & KS for 10.17.25 2.20.26 KS     |     | 10.29.25 Budgets                  |                  |     |     |     |     |     |     |     |     |     |     |
|                       | 1690                           |                     |                          |     | mtg•  10.17.25 KS to Board for                  |     | to Board•  to Board• 11.4.25      |                  |     |     |     |     |     |     |     |     |     |     |
|                       |                                |                     |                          |     | 10.21.25 mtg• 10.21.25 Board &                  |     | Budgets tables to                 |                  |  

*[document truncated for length]*

---

**[MINUTES] 2026-04-23_20260423_mat_17.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM, GOVERNOR
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390

|   www.ombc.ca.gov

|   F (916) 928-8392

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA

DATE

TO

FROM

RE:

April 23, 2026

Board Members

Terri Thorfinnson, J.D. Legislative and Regulatory Specialist

Agenda Item 17-Discussion and Possible Action on Pending Legislation

Recommendations for Possible Positions for 2026 Legislation

AB 1703 (Hart) Title Protection: Osteopath

Summary: This bill is a title protection bill that restricts the usage for the title
“Osteopath” to licensed Osteopathic Physicians and Surgeons. The bill adds Osteopathic
Manipulation Treatment” (OMT) to the scope of practice for licensed physicians and
surgeons.

Discussion: The purpose of this bill is to clarify that the title “Osteopath” can only be
used by a licensed physician and surgeon. It also adds Osteopathic Manipulation
Treatment (OMT) to the scope of practice section for licensed physicians and surgeons.
This bill is sponsored by the Osteopathic Physicians and Surgeons of California (OPSC).
Several years ago, there was a failed attempt for a mega title protection bill that added a
list of titles recognized by the American Medical Association (AMA) whose intent was to
codify existing titles to clarify for consumers what title is legitimate and requires licensed
professionals to wear that title on their name badge while treating patients to remove
confusion. While that bill ultimately failed, before it failed the title “Osteopath” was
removed from the list of titles to be protected in statute. Attempts to restore the title
failed as well.

The problem this bill is trying to solve is to close the loophole in the use of the title
Osteopath from being used by unlicensed foreign trained osteopaths who do not have
sufficient training to be licensed as an osteopathic physician and surgeon. Current
statutory language is vague about the title Osteopath precisely because it does not exist
in the statute. Historically, the title “Osteopath” has been used by American Osteopathic
Association (AOA), Osteopathic Physicians and Surgeons of California (OPSC) and the
Osteopathic Medical Board of California (OMBC) interchangeably to refer to licensed
Osteopathic Physicians and Surgeons. This bill clarifies and protects that title in statute to

be continued to be used to refer to licensed Osteopathic Physicians and Surgeons
exclusively.

Additionally, by adding Osteopathic Manipulation Treatment (OMT) to the scope of
practice for licensed physicians and surgeons, it clarifies that only licensed physicians and
surgeons can perform OMT. Yes, M.D.s are authorized to perform OMT, and some do; so,
it is an appropriate addition to the scope of practice for physicians and surgeons.

Historically, the Board has instructed foreign trained Osteopaths that they lack the
required training to become licensed and as a result cannot use the title “Osteopath.”
However, it has come to the Board’s attention through the years that foreign trained
Osteopaths are using the title “Osteopaths” in advertising their services in California. The
main public safety concern is that foreign trained Osteopaths misrepresent their skills to
consumers and lack licensure and perform Osteopathic Manipulation Treatment (OMT)
on their patients. The U.S. is the only country in the world that trains Osteopaths in
allopathic clinical medicine and comprehensive osteopathic skills. Additionally, there is
no standardized osteopathic training or standards throughout the world, which causes
significant variation in the skills among foreign trained osteopaths. For this reason, only
U.S. trained osteopaths are eligible for licensure in California and the United States.

Existing law prohibits the performance of OMT by an unlicensed physician and surgeon,
but the law does not mention the use of the title “Osteopath.” This bill protects public
safety and prevents misrepresentation of skills, competence, and licensure for an
osteopath. This bill will provide the board with the enforcement authority needed to
bring enforcement actions against advertising, misrepresentation and unlicensed activity.

It is worth noting that the statute has a general provision that allows unlicensed health
practitioners to notify their patients that they are not licensed and provide wellness care.
However, these foreign trained Osteopaths are not using or complying with this provision
to the detriment of their patients and the public.

Recommendation: Support.

SB 1002 ( Niello) License Exemption: Out of State Physicians: Non- Life Threatening
Condition

Summary: SB 1002, as introduced, Niello. Out-of-state physicians and surgeons:
telehealth: license exemption.

OMBC 2026 LEGISLATIVE REPORT: BILL LIST

2

Existing law generally prohibits the practice of medicine without a physician’s and
surgeon’s certificate issued by the board. Existing law authorizes a health care provider
to deliver health care via telehealth to a patient pursuant to specified protocols and
conditions. Existing law defines “telehealth” as the delivery of health care services and
public health via information and communication technologies to facilitate the diagnosis,
consultation, treatment, education, care management, and self-management of a
patient’s health care, and that telehealth includes synchronous interactions and
asynchronous store and forward transfers.

Existing law authorizes an eligible out-of-state physician and surgeon, as defined, to
deliver health care via telehealth to an eligible patient. Existing law defines “eligible
patient” as a person who, among other requirements, has a life-threatening disease or
condition, as defined, and has not been accepted to participate in the clinical trial
nearest to their home for the immediately life-threatening disease or condition, as
specified, or in the medical judgment of a physician and surgeon, as defined, it is
unreasonable for the patient to participate in that clinical trial due to the patient’s
current condition and state of disease.

This bill would also include within the definition of “eligible patient” a patient who’s
immediately life-threatening disease or condition is in remission, and the patient is
continuing care with the previously established eligible out-of-state physician and
surgeon, and would provide that those patients are not subject to the clinical trial
requirement, as specified.

Discussion: This bill is similar to a bill last year SB 508 that tried to expand the out of
state telemedicine licensure exemption to create an exemption for patients in remission
from life threatening conditions, which the Board opposed. That bill did not advance and
received concerns by Legislative committee staff about the slippery slope of expanding
the license exemption for out of state physicians for non- life-threatening conditions and
treatment. The original exemption was created narrowly only in cases of life-threatening
conditions or disease, which is not true for this proposal. This bill is a second attempt to
expand the licensure exemption to patients with non-life-threatening conditions that are
in remission. There is no policy justification for this expansion. This exemption begs the
practical question why the patient doesn’t move to the state in which their preferred
physician is licensed to continue to receive care or why a California physician care is not
adequate?

OMBC 2026 LEGISLATIVE REPORT: BILL LIST

3

Policy wise, the Board opposes licensure exemptions and in particular license exemptions
for telemedicine and out of state physicians that are not otherwise licensed in California
treating California patients. This bill poses a significant risk of harm to public safety. This
exemption removes the Board’s jurisdiction to protect California patients seeking care
through this exemption leaving patients without any enforcement or legal remedy
against the out of state unlicensed physician. In fact, this licensure exemption means that
there is no oversight of this exemption for compliance and eligibility—none. This
exemption creates a huge loophole in licensure that is totally unregulated. Patients
harmed under this provision have no legal recourse in California nor in the state in which
the physician is licensed because they are not a resident of the state. Their limbo status
places them in peril if there is harm. For this reason, this proposed license exemption
policy is irresponsible and a risk to public safety.

Recommendation: Oppose.

AB 2398 ( Alvarez) Alternative Pathway for Residency Training for M.D.s & D.O.s

Summary: This bill has two major parts: Part I related to the Mexico Pilot Program under
the Medical Board of California; Part II proposes an alternative pathway to residency and
licensure for graduates of U.S. medical schools and for M.D.s graduates of international
medical schools who are not able to get into U.S. residency programs. The first part does
not apply to OMBC licensure since all foreign trained osteopaths are ineligible for
licensure. The Mexico Pilot Program only applies to M.D.s who are graduates of Mexican
medical schools and participate in the pilot program. Part II does apply to OMBC.

Discussion: This bill proposes to create an alternative pathway to residency for graduate
of U.S. medical schools and international medical schools. The proposed pathway
consists of supervision by any licensed physician in California. There is no proposed
curriculum that would even attempt to mirror the comprehensive topics and skills taught
in residency training. Nor does it require any accreditation requirement or otherwise
curriculum—simply supervision by any licensed physician.

This proposal lacks any accreditation requirement or curriculum requirement and
rotations, or quality control requirement or variety of training by different specialties
such as internal medicine, OBGYN, pediatrics, etc. that occurs as part of standardized
residency training. After this unaccredited, supervised training by a single physician, the
applicant would be eligible for full licensure to go out and practice without the detailed
and specific training of accredited residency training. This proposed alternative pathway
to residency training is inferior training that would not provide comprehensive training
that occurs in residency training and as such would be a risk to public safety.

OMBC 2026 LEGISLATIVE REPORT: BILL LIST

4

Additionally, the board would take on the verification of training and, although not
specified, the evaluation and monitoring of the supervised training to ensure quality
control, competency and the fact there is training going on. These trainees would
eventually be licensed to join their peers but would lack the vast majority of the training
and skills of their peers who finished accredited residency training.

The role of residency training is both hands on training for physicians, but from a public
safety perspective, it is also the competency evaluation that cannot be left to an exam
alone. The 3 levels of competency exams in addition to the residency training is the
mechanism to ensure all physicians and surgeons have the same training, the same
competence and are in fact deemed competent to practice medicine safely. This
alternative residency falls short of residency training and competency evaluation—the
exact role of residency training. Additionally, without accreditation or required
curriculum, there is no standardization of training nor quality control assurance that
training is competently performed and that the competence of the trainee can be relied
upon for public safety reasons.

This alternative pathway creates a patchwork of pre-licensure training that is different
for foreign trained physicians than their U.S. trained counterparts, which raises
competency and public safety concerns with this proposal.

The drive behi

*[document truncated for length]*

---

### 2026-01-22 — Osteopathic Medical Board of California — January 22, 2026

**[AGENDA] 2026-01-22_20260122_agenda.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 |F (916) 928-8392 | www.ombc.ca.gov

MEMBERS OF THE BOARD
President
Deni   se Pines, MBA
V ice President
Hem esh Patel, D.O.
Secretary
Gor Adamyan

Joh n M. Cummins, J.D.
Brett Lockman, D.O.
Negeen Mirreghabie, Esq.
Ma tthew Swain, D.O.

 AMENDED-QUARTERLY BOARD MEETING AGENDA

Department of Consumer Affairs – HQ2
Hearing Room

1747 North Market Blvd.
Sacramento, CA 95834
(916) 928-8390 Office Main Line

Thursday, January 22, 2026
9:00 a.m. – 5:00 p.m.
(or until the conclusion of business)

Public WebEx/Telephone Access – See Attached
Meeting Information

MEETING TIMES AND ORDER OF AGENDA ITEMS ARE
SUBJECT TO CHANGE

Action may be taken on
any item listed on the
agenda

While the Board intends to
webcast this meeting, it
may not be possible to
webcast the entire open
meeting due to limitation
on resources or technical
difficulties.

Please see Meeting
Information section for
additional information on
public participation.

The Osteopathic Medical Board of California (Board) will meet in-person in
accordance with Government Code section 11123, subdivision (a).

Discussion may be had and action may be taken on any item on the agenda

OPEN SESSION

1.

2.

3.

4.

5.

6.

7.

Call to Order/Roll Call/ Establishment of a Quorum- Machiko Chong, Licensing
Program Manager

Reading of the Board’s Mission Statement– Erika Calderon, Executive Director

Public  Comment  on  Items  Not  on  the  Agenda  -Denise  Pines,  MBA.
The  Board  may  not  discuss  or  take  action  on  any  matter  raised  during  this
public  comment section  except  to  decide  whether  to  place  the  matter  on
the  agenda  of  a  future  meeting.  (Government  Code  sections  11125,
11125.7(a).)

Review  and  Possible  Approval  of  Board  Meeting  Minutes  -  Beth  Clark,
Associate Governmental Program Analyst

A. November 13, 2025, Board Meeting Minutes

President’s Report- Denise Pines, MBA

Board Member Communications with Interested Parties-   Denise Pines, MBA

Intergovernmental Relations Reports and Administrative Services Update

A. DCA Update – Shelly Jones, Assistant Deputy Director Board and Bureau

Relations, DCA

B. Budget Update – Kaila Van Lindt, Budget Office, DCA

Executive Director’s Report- Erika Calderon, Executive Director
Administrative  Services,  including  administrative  services,  personnel,  and
technology updates

Discussion and Possible Action to Revise the Board’s 2024-2028 Strategic Plan-
Erika Calderon, Executive Director

8.

9.

  LUNCH AND RECONVENE IN OPEN SESSION

10.

11.

12.

13.

Licensing/Admin  Program  Summary,  including  licensing  unit  updates,  and
statistics- Machiko Chong, Licensing Program Manager

Enforcement  Program  Summary,  including  enforcement  unit  updates,  and
statistics- Cristy Livramento, Enforcement Program Manager

Probation Program Summary, including probation unit updates and statistics-
Ralph Correa, Probation Monitor

Rulemaking  Update-Report  on  Pending  or  Proposed  Regulations-Terri
Thorfinnson, J.D., Legislative and Regulatory Specialist

14. Osteopathic Medical Board of California Lobby Day Update – Terri Thorfinnson,

J.D., Legislative and Regulatory Specialist

15.

Election of Officers-Erika Calderon, Executive Director

16.

17.

Solicit Future Agenda Items-Denise Pines, MBA

Adjournment

Online Access of Meeting

The Osteopathic Medical Board of California will also broadcast the public portion
of its meeting via WebEx Events. To participate in the WebEx Events meeting, please
log on to this website on the day of the meeting:

Click Here to Join Meeting

If joining by phone
+1-415-655-0001 US Toll
Access code: 2495 180 4069
Passcode: 6622122

Experiencing issues joining the Meeting?

Copy and paste the link text below into an internet browser:

https://dca-meetings.webex.com/dca-
meetings/j.php?MTID=mbc0bb9143d180b82ea0bc1e1e7f8a4bc

Members of the public may but are not obligated to provide their names or personal
information  as  a  condition  of  observing  or  participating  in  the  meeting.  When
signing  into  the  WebEx  platform,  participants  may  be  asked  for  their  name  and
email  address.  Participants  who  choose  not  to  provide  their  names  will  need  to
provide  a unique identifier  such  as  their  initials  or  another  alternative,  so  that  the
meeting  moderator  can  identify  individuals  who  wish  to  make  public  comment;
participants who choose not to provide their  email  address  may  utilize  a  fictitious
email address like in the following sample format: XXXXX@mailinator.com.

Please Note: Because there is an audio delay, if you are participating by phone and
simultaneously watching the Webcast, the Board requests you turn off the sound to
the Webcast for improved clarity.

For further information about this meeting, please contact Machiko Chong at 916-
928- 7636 or in writing at 1300 National Drive, Suite 150, Sacramento, CA 95834. This
notice and agenda, and any available Board meeting materials, can be accessed
on the Board’s website at www.ombc.ca.gov

In accordance with the Bagley-Keene Open Meeting Act, all meetings of the Board,
including any teleconference sites when the meeting is a teleconference meeting,
are open to the public. Government Code section 11125.7 provides the opportunity
for the public to address each agenda item during discussion or consideration by
the Board prior to the Board taking any action on said item. Members of the public
will  be  provided  appropriate  opportunities  to  comment  on  any  issue  before  the
Board, but the Board President, at his or her discretion, may apportion available time
among those who wish to speak. Individuals may appear before the Board to discuss
items not on the agenda; however, the Board can neither discuss nor take official
action on these items at the time of the same meeting. (Government Code sections
11125, 11125.7(a).)

Board  meetings  are  held  in  barrier  free  facilities  that  are  accessible  to  those  with
physical disabilities in accordance with the Americans with Disabilities Act (ADA). If
you  are  a  person  with  a  disability  requiring  disability-related  modifications  or
accommodations to participate in the meeting, including auxiliary aids or services,
please  contact  Machiko  Chong,  ADA  Liaison,  at  (916)  928-7636  or  e-mail  at
Machiko.Chong@dca.ca.gov or send  a written request to the Board’s office at 1300
National Drive, Suite 150, Sacramento, CA 95834-1991.  Providing your request at least
five  (5)  business  days  before  the  meeting  will  help  to  ensure  availability  of  the
requested accommodation. Requests should be made as soon as possible, but at
least five (5) working days prior to the scheduled meeting. You may also dial a voice
TTY/TDD Communications Assistant at (800) 322-1700 or 7-1-1.

---

**[MINUTES] 2026-01-22_20260122_mat_2.pdf**

OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA

MISSION STATEMENT

To protect the public by requiring
competency, accountability, and integrity
in the safe practice of medicine by
osteopathic physicians and surgeons.

---

**[MINUTES] 2026-01-22_20260122_mat_4.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390    |    F (916) 928-8392    |    www.ombc.ca.gov

Osteopathic Medical Board of California

 Teleconference Minutes

November 13, 2025

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Brett Lockman, D.O.
Matthew Swain, D.O.

Erika Calderon, Executive Director
Machiko Chong, Licensing Program Manager
Cristy Livramento, Enforcement Program Manager
Terri Thorfinnson, Legislative/Regulatory Specialist
Shelly Jones, Asst. Deputy Director, DCA
Kaila Van Lint, Budget Analyst, DCA
Suzanne Balkis, Budget Manager, DCA
Marcy Larson, Administrative Law Judge, OAH
Matthew Fleming, Deputy Attorney General
Beth Clark, Associate Governmental Program Analyst
Ralph Correa, Probation Monitor

MEMBERS
PRESENT:

STAFF
PRESENT:

MEMBERS OF
THE AUDIENCE:

Holly Macriss, Executive Director, OPSC
Michelle Monserratt-Ramos, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Kimberly Turbin, Consumer Watchdog
Tracy Dominguez, Consumer Watchdog

Board Meeting Minutes – November 13, 2025

Agenda Item 1

Call to Order/Roll Call/Establishment of a Quorum

The Quarterly Board Meeting of the Osteopathic Medical Board of California (OMBC)
was called to order by President Denise Pines at 9:00 a.m.

Machiko Chong called roll and determined a quorum was present. The meeting was
held at the Department of Consumer Affairs, Hearing Room HQ1, in Sacramento, CA.

Agenda Item 2

Reading of the Board’s Mission Statement

Executive Director Erika Calderon read the Board’s mission statement: "to protect the
public by requiring competency, accountability, and integrity in the safe practice of
medicine by osteopathic physicians and surgeons"

Agenda Item 3

Public Comment on Items Not on the Agenda

President Pines opened the floor for public comments.

The WebEx moderator checked for online requests; no public comments were made for
items not on the agenda.

Agenda Item 4

Review and Possible Approval of Board Meeting Minute

Beth Clark presented the minutes from the August 14, 2025, Board Meeting.

Public Comment: Holly Macriss (OPSC) requested a correction on page 11 to clarify
that she stated she would be updating the Board on the upcoming osteopath bill, rather
than requesting updates from the Board.

Motion to adopt the August 14, 2025, minutes as amended.

Motion – Dr. Patel Second – Mr. Cummins

•  Aye – Adamyan, Cummins, Lockman, Patel, Pines, Swain
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie

Motion carried to approve the minutes as amended.

Board Meeting Minutes – November 13, 2025

Agenda Item 5:   Hearing on Petition for Early Termination of Probation

Administrative Law Judge (ALJ) Marcy Lawson presided over the hearing for Eman
Abdallah, D.O.

Deputy Attorney General Matthew Fleming represented the People. Dr. Abdallah
represented herself and was sworn in.

Deputy AG Fleming provided a history of the case, noting Dr. Abdallah’s license was
placed on five years of probation in June 2023 for gross negligence and aiding
unlicensed practice at med spas.

Dr. Abdallah testified regarding her rehabilitation, her current ownership of a private
practice where she performs all medical treatments herself, and her improved record-
keeping systems. Deputy AG Fleming recommended the Board continue the probation,
noting it was the earliest possible time for a petition and that the public interest is best
served by allowing the term to play out. The Board took the matter under submission for
deliberation in closed session.

Agenda Item 6:   President’s Report

President Denise Pines reported on:

•  Personnel Changes: Recognition of Andrew Moreno for seven years of service;

welcome to new member Negeen Mirreghabie (spectator online, joining in person in
January).

•  Events: Announcement of "Hill Day" on January 21, 2026, to meet with legislators.

•

International/National: Updates on the Federation of State Medical Boards (FSMB)
meeting in Dublin regarding medical racism standards and the emerging licensing
pathway for "assistant physicians".

•  DCA Leadership: Acknowledgment of DCA Director Kimberly Kirchmeyer’s

upcoming retirement.

•  Public Comment: Representatives from Consumer Watchdog criticized the use of
clinical terminology such as "cradle to the grave" and requested that enforcement
committee meetings be held in public.

Agenda Item 7:   Board Member Communications with Interested Parties

President Pines requested disclosures. No board members reported communications.

Board Meeting Minutes – November 13, 2025

Agenda Item 8:
Services Update

Intergovernmental Relations Reports and Administrative

•  DCA Update: Shelly Jones reported on the appointment of Lucy Saldivar as Deputy
Director of Board and Bureau Relations and provided updates on mandatory training
(Sexual Harassment Prevention and Unconscious Bias).

•  Budget Update: Kaila Van Lindt reported the Board ended FY 24/25 with

approximately 12.4 months in reserve. However, future expenditures are projected to
increase by 3% annually while revenues remain static.

Agenda Item 9:   Executive Director’s Report

Erika Calderon introduced new staff members Rachel Molina (Enforcement Analyst)
and Yvonne Almazan (Special Investigator).

She noted that enforcement staff have returned to the office three days per week for
onboarding and collaboration.

Agenda Item 10:   Licensing/Admin Program Summary

Machiko Chong reported a total population of 17,012 licensed D.O.s. Total applications
are up 17% overall.

Revisions were made to FNP applications to clarify requirements for various filing types.

Agenda Item 11:   Enforcement Program Summary

Cristy Livramento reported 320 complaints received this quarter, a 33% increase from
the previous year.

Referred cases to the AG doubled compared to the same quarter last year.

Public Comment: Consumer Watchdog volunteers shared personal stories regarding
the impact of physician negligence and requested transparency in case management.

Agenda Item 12:   Probation Program Summary

Ralph Correa reported 31 active probationers.

Board Meeting Minutes – November 13, 2025

He detailed field monitoring efforts, including unannounced visits to ensure compliance
with cease practice orders.

Agenda Item 13:   Rulemaking Update

Terri Thorfinnson confirmed that the prior regulatory package became effective October
1, 2025.

The Fee and License Status package and Disciplinary Guidelines are currently in
progress

Agenda Item 14:   Discussion and Possible Action to Consider Initiation of a
Rulemaking (Retired License, Petitions and Fees)

Terri Thorfinnson and Kristy Schieldge presented a trimmed-down regulatory package
focused on increasing fees to statutory maximums to address a structural budget
imbalance. Staff noted that fees have not been raised since 1994.

Key details include:

•  Conviction Reporting (Section 1630): Updated to require disclosure of crimes
in foreign countries while excluding minor traffic infractions of $500 or less
(unless involving drugs/alcohol).

•  Retired Status (Section 1648): Established a new status with an application fee

of $200 (OMB.31) and a restoration fee of $400 (OMB.32).

•  Petitions (Section 1656): Review time increased to 120 days. New non-

refundable fees of $2,800 for reinstatement and $1,500 for modification of
penalty were established.

•  Adjudication Fee: Implementation of a $20,000 upfront adjudication fee to
recover reasonable costs for the ALJ, court reporters, and DAG. A refund
mechanism was added if actual costs are lower than the upfront fee.

•  Board Discussion: Dr. Lockman raised concerns about financial hardship for
petitioners. Staff clarified that cost recovery shifts the burden from the general
licensee population to the individual utilizing the service.

Board Meeting Minutes – November 13, 2025

Motion to approve the proposed regulatory text in attachments one through five
and authorize the Executive Director to initiate the rulemaking process.

•  Motion – Dr. Lockman Second – Mr. Adamyan
•  Aye – Mr. Adamyan, Mr. Cummins, Dr. Lockman, Dr. Patel, Ms. Pines, Dr. Swain
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie

Motion carried to move the rulemaking process forward.

Agenda Item 15:   Discussion on Legislation

Terri Thorfinnson reviewed the status of several bills:

•  AB 489 (AI Deception) was signed into law.

•  AB 460 (Radiologist Telemedicine) was signed into law.

•  AB 432 (Menopause CME) and AB 742 (Expedited Licensure) were

vetoed by the Governor.

Agenda Item 16:   Future Agenda Items and Meeting Dates

The Board requested a future presentation on the administrative law process and a
panel discussion on CME requirements.

The next meeting is scheduled for January 22, 2026.

Agenda Item 17:   Adjournment

The meeting was adjourned by President Denise Pines.

---

**[MINUTES] 2026-01-22_20260122_mat_7b.pdf**

Department of Consumer Affairs

Expenditure Projection Report
Osteopathic Medical Board
Reporting Structure(s): 11112600 Support
Fiscal Month: 5
Fiscal Year: 2025 - 2026
Run Date:  01/02/2026

Department of Consumer Affairs

Expenditure Projection Report
Osteopathic Medical Board
Reporting Structure(s): 11112600 Support
Fiscal Month: 5
Fiscal Year: 2025 - 2026
Run Date:  01/02/2026
Estimated AG & HQIU Augmentations

Department of Consumer Affairs

Revenue Projection Report

Reporting Structure(s): 11112600 Support
Fiscal Month:
Fiscal Year: 2025 - 2026
Run Date:  01/02/2026

---

**[MINUTES] 2026-01-22_20260122_item_7b.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390    |    F (916) 928-8392    |    www.ombc.ca.gov

Osteopathic Medical Board of California

 Board Meeting Minutes

January 22, 2026

MEMBERS
PRESENT:

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Brett Lockman, D.O.

STAFF
PRESENT:

Erika Calderon, Executive Director
Yuping Lin, Esq., Legal Counsel
Machiko Chong, SSM I, Licensing Unit
Cristy Livramento, SSM I, Enforcement Unit
Terri Thorfinnson, SSM I, Legislative and Regulatory Specialist
Beth Clark, Analyst II
Ralph Correa, Probation Monitor
Shelley Jones, Assistant Deputy Director, Board and Bureau
Relations, DCA
Kayla Van Lint, Budget Analyst, DCA Budget Office
Brad Lencioni, Budget Manager, DCA

MEMBERS OF
THE AUDIENCE:

Holly Macriss, Executive Director, OPSC
Michele Monserratt-Ramos, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Tracy Dominguez, Consumer Watchdog
Sarah Irani, Analyst II, DCA Moderator

Board and Committee Meeting Minutes – January 22, 2025

Agenda Item 1

Call to Order and Roll Call/Establishment of a Quorum

The Quarterly Board Meeting of the Osteopathic Medical Board of California (OMBC)
was called to order by President Denise Pines at 9:03 a.m. on Thursday, January 22,
2026, in the Hearing Room of the Department of Consumer Affairs (DCA)
Headquarters, 1740 N. Market Blvd., Sacramento, California, and via Webex. President
Pines reviewed meeting protocols under the Bagley-Keene Open Meeting Act, including
public comment procedures and time limits. Machiko Chong called roll. A quorum of
Board members was established.

Agenda Item 2

Reading of the Board’s Mission Statement

Executive Director Erica Calderon read the Board’s mission statement: "to protect the
public by requiring competency, accountability, and integrity in the safe practice of
medicine by osteopathic physicians and surgeons".

Agenda Item 3

Public Comment for Items not on the Agenda

President Pines opened the floor for public comments regarding items not listed on the
agenda.

The Webex moderator provided instructions for submitting comments online.

No requests for public comment were made online or in person.

Agenda Item 4

Review and Possible Approval of Minutes

Beth Clark presented the draft minutes from November 13, 2025, Board Meeting. Ms.
Clark walked through the document page-by-page and invited corrections and
clarifications. One correction was noted to the subtitle to read "teleconference minutes".
After discussion, the Board considered approval of the minutes as amended.

Motion to approve November 13, 2025, minutes as amended.

Motion – Dr. Patel Second – Mr. Cummins

•  Aye – Adamyan, Cummins, Lockman, Patel, Pines
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie, Matthew Swain

Motion carried to approve the November 13, 2025, minutes as amended.

No public comments were made on this item.

Board and Committee Meeting Minutes – January 22, 2025

Agenda Item 5

President’s Report

President Pines provided an overview of Board activities during the past quarter and
noted ongoing coordination with Executive Director Calderon to advance Board
priorities. She announced her reappointment by the Governor and expressed
appreciation for the continued opportunity to serve.

Key updates included:

o  Reappointment: President Pines announced her reappointment by the
Governor to serve another term on the Board and expressed her sincere
appreciation for the continued trust and opportunity to serve in her role.

o

Inaugural Hill Day: On January 21, 2026, the Board held its first "Hill
Day." A delegation consisting of Dr. Patel, Mr. Adamyan, and Mr.
Cummins met with state legislators to provide an overview of the D.O.
profession and build support for future legislation to protect the
professional designation.

o  FSMB Updates: Ms. Pines will attend a Federation of State Medical

Boards (FSMB) meeting in late February, following a working session in
New Orleans focused on trauma-informed care. She also noted that the
FSMB Office of AI Innovation continues to monitor evolving artificial
intelligence regulations.

No public comments were made.

Agenda Item 6

Board Member Communications with Interested Parties

President Pines requested disclosures regarding Board member communications with
interested parties, including meetings with legislators or other external engagements
related to OMBC matters. No Board members reported communications requiring
disclosure.

No public comments were made.

Agenda Item 7
Services Update

Intergovernmental Relations Reports and Administrative

7A. Department of Consumer Affairs (DCA) Update
Shelly Jones, Assistant Deputy Director of Board and Bureau Relations, provided the
Department of Consumer Affairs (DCA) update and congratulated President Pines on
her reappointment.

Board and Committee Meeting Minutes – January 22, 2025

Ms. Jones reported on the following:

o  Leadership: Christine Lally has been appointed Acting Director of the DCA

following the retirement of Kimberly Kirchmeyer.

o  Governor’s 2026–27 Budget: The proposed budget is balanced.

o  Agency Reorganization: The former Business, Consumer Services and

Housing Agency is being divided into two entities. DCA will transition to the
newly established Business and Consumer Services Agency, with
implementation anticipated July 1, 2026.

o  Wildfire Executive Order: A one-year renewal fee postponement was

authorized for licensees impacted by the Los Angeles wildfires.

o  Compliance and Administrative Reminders:

  Form 700 filings are due April 1 through the FPPC e-filing system.
  Required trainings include Unconscious Bias and Board Member

Orientation.

  Travel and operational spending remain subject to Department of

Finance guidance.

No public comment was received.

7B. Budget Office Update

Budget Status:
Kaila Van Lindt and Brad Lencioni presented the Board’s fiscal status and projections.

  Authorized Budget: $4.333 million
  Projected Expenditures: $4.915 million
  Projected Reversion: 0.78% (after AG and HQIU cost augmentations)

Fund Condition:

o  Fiscal Year 2024–25 year-end reserve: $4.943 million (approximately 10.5

months).

o  Current year projected reserve: approximately 7.4 months.

Staff confirmed ongoing monitoring of expenditures to ensure fiscal stability and
compliance with state financial directives.

Board and Committee Meeting Minutes – January 22, 2025

Agenda Item 8

Executive Director’s Report

Executive Director Erika Calderon provided a comprehensive update on Board
operations, personnel matters, and ongoing interagency efforts.
Ms. Calderon began by recognizing Acting DCA Director Christine Lally and expressing
appreciation for her leadership and mentorship. She also announced the retirement of
Kathleen Nicholls, former Chief of the Department’s Division of Investigation,
acknowledging her more than 30 years of service in enforcement and investigative
work, including her prior leadership role within the Health Quality Investigation Unit
(HQIU).

Personnel and Organizational Updates
Ms. Calderon reported on recent statewide classification changes that took effect in
January 2026, including the consolidation of analyst and managerial classifications:

o  Staff Services Manager (SSM) classifications were converted to Manager I and

Manager II.

o  Associate Governmental Program Analysts (AGPA) were reclassified as Analyst II.

o  Staff Services Analysts (SSA) were reclassified as Analyst I.

She reviewed the Board’s authorized staffing levels and discussed operational
considerations, including the use of a limited-term Special Investigator to support
enforcement functions. She noted that resource constraints continue to impact workload
distribution and case processing timelines.

Enforcement and Interagency Coordination
Ms. Calderon emphasized ongoing coordination with the Attorney General’s Office and
HQIU to prioritize high-risk cases and matters approaching statute-of-limitations
deadlines. She reported that she and Enforcement Manager Cristy Livramento continue
to meet regularly with enforcement partners to ensure timely case review and
appropriate resource allocation.

Additionally, she referenced a joint forum held on December 17, 2025, with other
prescribing boards to discuss access to controlled substances and related regulatory
considerations. She also noted continued engagement with Consumer Watchdog
representatives to receive stakeholder input regarding enforcement practices and
consumer protection priorities.

Public Comment
Michelle Monserratt-Ramos (Consumer Watchdog) congratulated President Pines on
her reappointment, expressed appreciation for the Board’s continued focus on

Board and Committee Meeting Minutes – January 22, 2025

consumer protection, and recognized Kathleen Nicholls for her longstanding service and
retirement.

Holly Macriss (Osteopathic Physicians and Surgeons of California – OPSC) also
congratulated President Pines and thanked Board leadership for its ongoing outreach
and collaboration with licensees and association members. She noted that OMBC
leadership is anticipated to participate in an upcoming OPSC convention panel
addressing professional identity and the practice of medicine.

Agenda Item 9

Possible Action to Revise the 2024-2028 Strategic Plan

Executive Director Erika Calderon and staff presented proposed revisions to the
Osteopathic Medical Board of California’s 2024–2028 Strategic Plan. The proposed
updates included clarifying strategic objectives, refining language for improved
readability, and updating Board member information to ensure the document accurately
reflects the Board’s current composition and priorities.

Ms. Calderon explained that the revision process included review by the Executive
Committee and consideration of stakeholder input. The updates were intended to
enhance public-facing clarity while ensuring the Strategic Plan remains consistent with
the Board’s statutory authority and does not imply responsibilities beyond its regulatory
mandate.

Board members discussed the importance of clearly articulating OMBC’s mission,
consumer protection role, and enforcement authority. Particular attention was given to
ensuring that terminology accurately reflects the Board’s jurisdiction and responsibilities,
and that the final document is accessible and understandable to non-board audiences.

Public comments were received as follows:

•  Michelle Monserratt-Ramos (Consumer Watchdog) expressed appreciation for

the emphasis on public safety and consumer protection throughout the Strategic
Plan.

•  Holly Macriss (Osteopathic Physicians and Surgeons of California – OPSC)

raised questions regarding specific wording and requested that final language be
carefully reviewed to ensure clarity for stakeholders and licensees. She noted
that reviewing the text visually during the meeting was helpful and thanked staff
for the opportunity to provide input.

•  Tracy Domingues (Consumer Watchdog) requested clarification regarding the

sequencing of the agenda items.

Staff confirmed that, upon Board approval, the Strategic Plan would be finalized to
reflect the discussion and published on the Board’s website for public access.

Board and Committee Meeting Minutes – January 22, 2025

Motion to approve the proposed updates to the OMBC 2024–2028 Strategic Plan
and authorize the Executive Director to finalize and publish the revised plan.

Motion – Mr. Cummins Second – Dr. Patel

•  Aye – Adamyan, Cummins, Lockman, Patel, Pines
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie, Matthew Swain

Motion carried to approve the Strategic Plan updates and authorize publication of the
revised plan.

Agenda Item 10   Licensing Program 

*[document truncated for length]*

---

**[MINUTES] 2026-01-22_20260122_mat_8.pdf**

Agenda Item 8
Osteopathic Medical Board of California
DATE REPORT ISSUED: January 22, 2026
ATTENTION: Members, Osteopathic Medical Board of California
SUBJECT: Executive Report
STAFF CONTACT: Erika Calderon, Executive Director
REQUESTED ACTION:
This report is intended to provide the Members of the Osteopathic Medical Board of
California (OMBC) with an update on personnel, and other administrative
functions/projects occurring at the OMBC.
No action is needed.
Board Member Reappointment and DCA Leadership Update
The OMBC is pleased to announce the reappointment of Madame Board President
Denise Pines. President Pines has served the OMBC since April of 2021 as a public
member and for the past two years as our president.
As previously reported the Department of Consumer Affair’s (DCA) prior Director
Kimberly Kirchmeyer retired at the end of the year. The OMBC is pleased to announce
that the department’s Deputy Director Ms. Christine Lally who had been in that position
since April 2020 has officially taken on the role of Acting Director effective January 1st,
2026. Director Lally previously served at the Medical Board of California as Deputy
Director in 2017 until she became the Interim Executive Director in 2019. Director Lally
was Deputy Director of Board and Bureau Relations at the DCA from 2013 to 2017, and
prior to that was Assistant Secretary of Communications and Legislation at the California
Technology Agency from 2011 to 2013 and Deputy Secretary of Legislative Affairs at the
State and Consumer Services Agency in 2011.
Kathleen Nicholls who served as the chief of DCA’s Division of Investigation also retired
at the end of this year. Ms. Nicholls had nearly 30 years of enforcement and
investigations experience. Prior to her role as Chief, she has served as the Deputy Chief
of the Health Quality Investigation Unit.

Personnel:

The OMBC continues to have 15.9 authorized positions.

On August 11, 2025, the State Personnel Board (SPB) approved the California
Department of Human Resources’ (CalHR) proposal to consolidate multiple service-wide
and department-specific classifications into one streamlined “generalist” classification
series. The classification changes were implemented in January 2026.

The approved proposal includes:

•  Revise, retitle, and amend current service-wide staff services classifications as follows:

|        |                 |              | Current       | Proposed      |
| ------ | --------------- | ------------ | ------------- | ------------- |
| Class  | Current Class   | Proposed     |               |               |
|        |                 |              | Probationary  | Probationary  |
| Code   | Title           | Class Title  |               |               |
|        |                 |              | Period        | Period        |
| 4802   | Staff Services  | Manager      | 12 Months     | 12 Months     |
Manager III  II
| 4969  | Staff Services  | Manager  | 12 Months  | 12 Months  |
| ----- | --------------- | -------- | ---------- | ---------- |
Manager II  I
(Managerial)
| 4801  | Staff Services  | Supervisor  | 12 Months  | 12 Months  |
| ----- | --------------- | ----------- | ---------- | ---------- |
Manager II  II
(Supervisory)
| 4800  | Staff Services  | Supervisor  | 12 Months  | 12 Months  |
| ----- | --------------- | ----------- | ---------- | ---------- |
Manager I  I
| 5393  | Associate  | Analyst II  | 6 Months  | 12 Months  |
| ----- | ---------- | ----------- | --------- | ---------- |
Governmental
Program
Analyst
| 5157  | Staff Services  | Analyst I  | 12 Months  | 12 Months  |
| ----- | --------------- | ---------- | ---------- | ---------- |
Analyst
(General)

•  Establish two new rank-and-file analyst levels as follows:

|     | Class  | Class    | Probationary  |     |
| --- | ------ | -------- | ------------- | --- |
|     | Code   | Title    | Period        |     |
|     | 5402   | Analyst  | 12 Months     |     |
III
|     | 5403  | Analyst  | 12 Months  |     |
| --- | ----- | -------- | ---------- | --- |
IV

•  Update Alternate Range Criteria (ARC) 069.

It is anticipated that employees in the classifications listed above will be reallocated to
the newly revised classifications in January 2026. The new classifications of Analyst III
and Analyst IV were created based on existing non-DCA department-specific concepts

and will be available for DCA use, with OHR approval, in January 2026. Once all
affected employees have been successfully reallocated to the appropriate new
classifications, the old classifications will be abolished. This process will not negatively
impact employees, as salaries and assigned day-to-day tasks will remain unchanged.
Additionally, CalHR is maintaining the existing examinations for the current generalist
classifications and is working to create the examinations for the two new Analyst III and
Analyst IV classifications.
The only other staff update that the OMBC has this quarter is the internal promotion from
the classification Analyst I to Analyst II of Ms. Dina Ruprecht. In addition to handling all
post graduate applications Dina will be processing all Fictitious Name Permits and
issuing administrative citations and fines to those businesses who fail to renew their
permits on an annual basis and continue to operate.
Please refer to the Board’s Organizational Chart
State Budget/ OMBC Budget and Travel Restrictions:
OMBC is still operating under the Department of Finances issued budget letters. OMBC
must monitor overall expenses and limit out of state travel to essential operational needs. All
out of state travel requests must be approved by the governor’s office and approval will be
limited to mission critical only. Discretionary trips will not be considered this year.
In terms of OMBC’s Budget, the Board continues to work closely with DCA’s Budget office to
monitor the Board’s expenditures and request budget augmentations in areas where these

have been needed, such as enforcement. Later today during our regulation update you will
hear more about Board’s staff efforts to help increase OMBC revenue through application
fee increases and the petition fees.
Communication
Director Calderon represents the prescribing Boards as part of the CURES Executive
Stakeholder Committee and continues to meet regularly with DCA’s leadership staff and
the Department of Justice (DOJ).
Director Calderon had calls and email exchanges with Board President Denise Pines to
discuss pending and ongoing projects and meeting agendas.
Director Calderon continues to meet periodically with the Board’s Attorney General
Liaison Ms. Karolyn Westfall and communicates frequently with Senior Assistant Attorney
General Ms. Gloria Castro.
Director Calderon continues to meet periodically with members of the Consumer
Watchdog group to gather their input on improving enforcement practices and
procedures.
Enforcement staff continue to meet monthly with the DCA’s Division of Investigations HQIU
office to discuss progress of pending investigations.
Lastly for communications, our committee meetings have started, and Board leadership
will continue to meet frequently with our designated committee members, additionally
staff participated in meetings with other local, state, and national organizations in
discussing and deciding regulatory measures common to OMBC and others. These
organizations include but are not limited to; Office of Attorney General (AGO),
Department of Justice (DOJ), Department of Consumer Affairs (DCA), other healing art
Boards such as (MBC, BRN, BOP, PAC, PTBC), California Department of Public Health
(CDPH), Department of Health Care Services (DHCS), the Federation of State Medical
Board (FSMB), the National Board of Osteopathic Medical Examiners (NBOME),
International Association of Medical Regulatory Authorities (IAMRA), Osteopathic
Physicians and Surgeons of California (OPSC), American College of Osteopathic Family
Physicians of California (ACOFPCA), and lastly Premier Health who is now handling the
Board’s diversion program.
Outreach Update:
The OMBC continues to post Board content regularly on all of its social media platforms
such as Facebook, Linkedin, and X. The Board continues to keep its website current which
includes positing relevant legislation, frequently ask questions, publications, and
enforcement actions.
This past quarter OMBC did not attend any outreach events, as previously mentioned due
to concerns with the overall state budget travel has been limited to mission critical.
This concludes the Executive Director’s update.

---

**[MINUTES] 2026-01-22_20260122_mat_9.pdf**

Osteopathic Medical Board of California

Agenda Item 9

DATE REPORT ISSUED:
ATTENTION:
SUBJECT:
STAFF CONTACT:

January 22, 2026
Members, Osteopathic Medical Board of California
Strategic Plan Update and Proposed Revisions
Erika Calderon, Executive Director

REQUESTED ACTION:

This report is intended to provide the Members of the Osteopathic Medical Board of California
(OMBC) with an update on OMBC’s 2024-2028 Strategic Plan and have the members review
and approve suggested updates from the OMBC’s Executive Committee.

Requested Action:

Motion  to  approve  the  proposed  changes  to  the  Board’s  2024-2028  Strategic  Plan  and
authorize the Executive Director to amend the plan as proposed or further amended by the
Board  members  and  work  with  the  Department  of  Consumer  Affairs  publication  office  to
publish a new version.

Annual Review: 2024-2028 Strategic Plan

The  OMBC  adopted  its  2024-2028  strategic  plan  on  September  23,  2023.  As  we  know  a
strategic  plan  is  a  written  document  that  outlines  an  organization's  long-term  goals,  the
strategies it will use to achieve them, and the actions needed to implement those strategies,
essentially in our case serving as a roadmap for the OMBC's future direction over a defined
period of 4 years; it includes elements like our vision, mission, core values, objectives, and
specific action plans to measure our success. DCA’s Solid Team has provided this OMBC with
an  action  plan  tracker  that  allows  the  OMBC  to  track  its  progress  through  and  excel
spreadsheet allowing us to have a visual of the completed objectives.

The  chart  listed  below  shows  that  OMBC  staff have  already  completed  100%  of  its  overall
Administrative  Objectives,  67%  of  its  Regulations  and  Legislative  Objectives,  100%  of  its
Enforcement  Objectives,  74%  of  its  Licensure  Objectives,  and  56%  of  its  Outreach  and
Communication Objects in each goal item within the first year of the strategic plan.

Goal (completed percentage):

Updates:

Page 3:

Update #1-Updating Board member names and positions.
Update #2-Updating DCA’s directors name.

Page 5:

Update #1-Include the words Board “OMBC’s amended” strategic plan, include the word “shall”
and update the Board presidents message.

Page 7:

Update #1-Adding 1.6-update the Board members with a monthly newsletter on office projects.
Update #2-Updating 2.3.-replace the words and establish a process for the regular review of
regulations  in  the  future  with  “and  establish  a  process  for  the  regular  review  of  legislation
impacting the Board on a state and federal level.”

 Page 9:

Update#1-Change the word statutory with regulatory.

---

**[MINUTES] 2026-01-22_20260122_mat_9a.pdf**

Table of Contents

Board Members ....................................................................... 3

Osteopathic Medical Board of California .................................. 4

Message from the President .................................................... 5

Board Mission, Vision, and Values ........................................... 6

Goal 1: Board Administration ...................................................... 7

Goal 2: Regulation and Legislation ........................................... 7

Goal 3: Enforcement ................................................................. 8

Goal 4: Licensure ...................................................................... 9

Goal 5: Outreach and Communication ................................... 10

Strategic Planning Process .................................................... 11

Osteopathic Medical Board of California

About the Board

The Osteopathic Medical Board of California (OMBC) was established
in 1922 when the Osteopathic Initiative Act was passed. Initially, the
Board was comprised of five Osteopathic Physicians appointed by the
governor to staggered three-year terms. In 1991, two public members
were added to the Board, also serving three-year terms.

In 2002, the Board volunteered to be included under the umbrella of
the California Department of Consumer Affairs (DCA). The affiliation with
DCA and access to its resources has strengthened OMBC. To publish
the Board’s longevity in 2023, the Board added its establishment year
to its logo.

OMBC is charged with a mission of public protection as defined in the
Medical Practice Act. This charge is met through the Board functions of
licensing and enforcement.

OMBC is a fully functioning regulatory board within DCA with the
responsibility and sole authority to issue licenses to Doctors of
Osteopathy (D.O.s) to practice osteopathic medicine as a physician
and surgeon or training licenses for residents and fellows in California.
OMBC is also responsible for ensuring the enforcement of legal
and professional standards to protect California consumers from
incompetent, negligent, or unprofessional D.O.s.

D.O.s are fully licensed to prescribe medication and practice in all
medical and all surgical specialty areas, just as their M.D. counterparts.
D.O.s are trained to consider the health of the whole person and use
their hands in an integrated approach to help diagnose and treat their
patient.

4

Osteopathic Medical Board of California

Message from the President

On behalf of the Osteopathic Medical Board of California (OMBC), it is my
sincere pleasure to present the OMBC’s amended 2024–2028 Strategic
Plan.  I  want  to  thank  the  California  Department  of  Consumer  Affairs’
SOLID unit for their leadership in the process, all Board members, the
executive  director,  Board  managers,  Board  staff,  and  the  public  for
putting together this plan.

The  primary  function  of  the  Board  remains  consumer  protection.  The
mission of the Board is to protect the public by requiring competency,
accountability,  and  integrity  in  the  safe  practice  of  medicine  by
osteopathic physicians and surgeons.

The Board’s mission is a commitment to California consumers about the
practice  of  osteopathic  medicine.  The  Board  stands  by  our  oath  to
protect the public from hurt or harm through the practice of medicine. It
is  our  duty  to  uphold  principles  to  ensure  that  we  honor  the  mission
statement. Those principles make sure that there is proper evaluation of
applicants  when  it  comes  to  licensure,  enforcing  and  administering
investigations,  disciplinary  actions  when  appropriate,  and  providing
consumer outreach by sharing information with all regarding the practice
of  medicine.  Our  dedication  to  protecting  consumers  from  unsafe
practices  is  highly  regarded  and  each  Board  member  takes  that
responsibility seriously.

Our physicians and surgeons shall give the highest quality of care for all,
striving for excellence in public protection.

The  Board  continually  strives  to  attain  meaningful  improvement  to
service  our  physicians,  protect  the  public,  and  maintain  the  highest
standards in health care.

The  success  of  this  strategic  plan  depends  on  an  ever-evolving
relationship  with  all  the  stakeholders  in  California.  The  Board  is
committed  to
its  licensure,  enforcement,  outreach  and
communication,  regulation  and  legislation,  and  Board  administration
efforts.

improve

Denise Pines, MBA
President, Osteopathic Medical Board of California

2024–2028  Strategic  Plan

5

 public by requiring
competency, accountability,
and integrity in the safe
practice of medicine by
osteopathic physicians and
surgeons.

VISION

Our physicians and
surgeons give the highest
quality of care for all, striving
for excellence in public
protection.

VALUES

Accountability
Consumer Protection
Collaboration
Competency
Diversity, Equity, and Inclusion
Effective Leadership
Innovation

6

Osteopathic Medical Board of California

Goal 1: Board Administration
Build an excellent organization through proper Board
governance, effective leadership, technology, and responsible
management.

1.1  Establish a process for conducting an annual evaluation of the
Board’s strategic plan and achieved objectives to maintain
accountability and effectiveness.

1.2  Establish licensing, education, and outreach advisory committees

to support the advancement of the Board’s efforts.

1.3  Conduct licensee salary, fee, and growth analyses to inform a

regulatory proposal to increase application fees, address licensee
population growth, and staffing needs.

1.4  Explore methods to utilize automated emails and maximize

BREEZE functionality to increase consistency, timeliness, and
accessibility of communication.

1.5  Register staff for customer service training to improve interactions

between staff and licensees.

1.6  Update the Board members with a monthly newsletter on office

projects.

           Goal 2: Regulation and Legislation

Monitors and upholds the law and participates in the regulatory and
legislative process.

2.1  Create a dedicated legislation and regulation staff position to

effectively track legislation that affects the Board, ensure the Board
has a voice in the legislation process, and align regulations with
statutory requirements necessary for the Board to carry out its
mission.

2.2  Establish a legislative day for board staff to meet with legislators

and inform legislators and the public of OMBC’s role and to protect
the scope of practice.

2.3  Conduct a comprehensive review of the Board’s regulations and
ensure they are up to date and communicated, and establish a
process for the regular review of regulations in the future. and
establish a process for the regular review of legislation
impacting the Board on a state and federal level.

   2024–2028  Strategic  Plan       7

Goal 3: Enforcement

Protects the health and safety of consumers through the enforcement
of laws and regulations governing the practice of osteopathic
medicine.

3.1  Publish disciplinary actions in the Board newsletter to keep the

public informed of enforcement actions.

3.2  Create brochures, as well as complaint status letters and

newsletter articles, to increase transparency and understanding of
the complaint process.

3.3

Fully implement Senate Bill 815, including obtaining additional
resources.

3.4  Recruit an additional investigator to improve communication, and

allow for more effective enforcement.

3.5  Acquire specialty subject matter experts for the expert review

program to improve efficiency and create a robust team of expert
reviewers.

8

Osteopathic Medical Board of California

Goal 4: Licensure

Requires that only qualified individuals are licensed as osteopathic
doctors.

4.1  Communicate online application options to applicants and students

to reduce processing times.

4.2  Seek statutory regulatory changes to establish a continuing education
self-certification and follow-up audit to decrease license renewal
processing times.

4.3  Conduct an annual assessment of staff workload and performance
metrics to ensure proper staffing and workload management.

4.4  Pursue legislation that will require licensees to provide an email

address to the Board to improve communication and renewal
updates.

2024–2028  Strategic  Plan

9

Goal 5: Outreach and Communication

Consumers and licensees are making informed decisions regarding the
safe practice of osteopathic medical services.

5 .1  Regularly manage the Board’s social media accounts to keep the
public informed of Board activities and increase public awareness.

5.2  Attend more school events and promote best practices to increase

outreach to students and aid in the accurate completion of
applications.

5.3  Create an awareness campaign and partner with other healing arts

boards to increase consumer knowledge of osteopathic doctors.

5.4  Partner with other healing arts boards within DCA on common
issues facing the healing art professions to encourage
collaboration and promote visibility.

Create a dedicated outreach position to improve outreach to the
public.

Update the Board’s logo to include the establishment year to
publicize its longevity.

10  Osteopathic Medical Board of California

Strategic Planning Process

To understand the environment in which the Board operates as well
as identify factors that could impact the Board’s success in carrying
out its regulatory duties, the DCA’s SOLID Planning Unit conducted an
environmental scan of the Board’s internal and external environments
by collecting information through the following methods:

• Interviews with the executive director and Board management in

June and July 2023.

• Interviews conducted with Board members in June and July 2023.

• Online surveys were distributed to staff and external stakeholders

in June and July 2023.

The most significant themes and trends identified from the
environmental scan were discussed by Board members and the
executive director, licensing manager, and administrative manager
during a strategic planning session facilitated by SOLID on September
28, 2023. This information guided the Board in the development of its
strategic objectives outlined in this strategic plan.

2024–2028  Strategic  Plan

11

---

**[MINUTES] 2026-01-22_20260122_mat_10.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM, GOVERNOR
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov
DATE January 22, 2026
TO Board Members
Machiko Chong
FROM
Licensing Program Manager
Agenda Item #10 – Licensing Program Summary
SUBJECT
Attachments 10a & 10b
Licensing Statistics & Program Review
Attachments 10a & 10b reflect the licensing population and application stats for the
first quarter of the 2025/26 Fiscal Year. Currently, there are 17,164 licensed osteopathic
physicians and surgeons; 1,695 postgraduate training licensees (PTL); 1,701 fictitious
name permits; and no Temporary Osteopathic physician and surgeon license.
Overall, the Board has seen a 27% increase in applications received. There are
currently 264 pending initial applications, with 19 of those requesting expedited
services. The application breakdown is as follows:
Application Stats
• Postgraduate Training License (3 applications)
• Osteopathic physician and surgeon (261 applications)
Expedite Service Requests
• Medically Underserved Area (16 applications)
• Military Veteran (3 applications)
• Abortion Services (0 applications)
In December, the Board’s Postgraduate Training Licenses (PTL) Coordinator, Dina
Ruprecht, was offered and accepted a promotional opportunity to become an
Analyst II (formerly classified as an Associate Governmental Program Analyst (AGPA))
within the Licensing Unit. In addition to issuing PTLs, Ms. Ruprecht will now be
responsible for issuing and canceling fictitious name permits, auditing permit holders
within the FNP program, drafting citation and fine documents, and scheduling appeal
hearings to remediate permit issues. At the beginning of 2025, Enforcement staff
assisted in auditing FNP records that were identified as being non-compliant. Permit
holders were also educated on maintenance requirements and informed of their

options to either terminate or renew permits that had been issued by the Board. FNPs
are set to expire annually on December 31st, and notification of expiration is sent to
permit holders 90 days before expiration of licensure. Yet, numerous applications tend
to remain out of compliance. Moving forward, Ms. Ruprecht will conduct annual
audits of delinquent permits in February to ensure that permits are brought into
compliance.
At the last board meeting, I highlighted the proposed BreEZe VO/VR changes that
were requested, which would revise the initial application for Fictitious Name Permits
(FNP) and update the physician and surgeon renewal application to accommodate
licensee self-certification and the audit of Continuing Medical Education. Both
projects and their corresponding BMO (BreEZe Maintenance and Operations)
requests have been added to the current project schedule, which is set for release
on February 18th. Many of the requested updates had been made and tested during
the last project period; however, there were a couple of items that needed tweaking,
and in the interest of time, it was agreed that it was best not to rush the release of the
final product until the updates requested were properly applied.

Osteopathic Medical Board of California
Current Licensee Population
Agenda Item 10 (A) -Application Services Stats
Stats FY 25-2026 Q1-Q2
Osteopathic Physician and Surgeon
License Status Total Licensees
Active 14,761
Delinquent/Expired 1,988
Inactive 415
Total: 17,164
Postgraduate Training License (PTL)
License Status Total Licensees
Active 1,697
Delinquent/Expired 4
Inactive 0
Total: 1,701
Temporary License
License Status Total Licensees
Temp Osteopathic Physician and Surgeon 0
Temp Postgraduate Training License (PTL) 0
Total: 0
Fictitious Name Permit
License Status Total Licensees
Active 900
Delinquent/Expired 464
Inactive 0
Total: 1,364
Total Number of Licensees/Permit Holders 20,229

Osteopathic Medical Board of California
Application Renewal Services
Agenda Item 10(B) - Application Services Q1-Q2 Program Stats
Application Services Statistics Report
Total Applications Received
|                               | FY 2024/25  |      | FY 25/26  |        | Year  →  Year  |      |
| ----------------------------- | ----------- | ---- | --------- | ------ | -------------- | ---- |
|                               |             | YTD  |           | YTD    | Change         |      |
| Physician and Surgeon         |             | 584  |           | 670    |                | 13%  |
| Postgraduate Traning License  |             | 259  |           | 300    |                | 16%  |
| Fictitious Name Permits       |             | 78   |           | 201    |                | 61%  |
| Total                         |             | 921  |           | 1,171  |                | 27%  |
Applications Approved
|                               | FY 2024/25  |        | FY 25/26  |        | Year  →  Year  |       |
| ----------------------------- | ----------- | ------ | --------- | ------ | -------------- | ----- |
|                               |             | YTD    |           | YTD    | Change         |       |
| Physician and Surgeon         |             | 748    |           | 613    |                | -18%  |
| Postgraduate Traning License  |             | 680    |           | 674    |                | -1%   |
| Fictitious Name Permits       |             | 67     |           | 117    |                | 75%   |
| Total                         |             | 1,495  |           | 1,404  |                | -6%   |
Renewals
|                          | FY 2024/25  |        | FY 25/26  |        | Year  →  Year  |      |
| ------------------------ | ----------- | ------ | --------- | ------ | -------------- | ---- |
|                          |             | YTD    |           | YTD    | Change         |      |
| Physician and Surgeon    |             | 3,407  |           | 3,794  |                | 11%  |
| Ficticious Name Permits  |             | 862    |           | 812    |                | -6%  |

---

**[MINUTES] 2026-01-22_20260122_mat_11.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM, GOVERNOR
DEPT. OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov
Briefing Paper Agenda Item 11
Date: January 22, 2026
Prepared for: OMBC Members
Prepared by: Cristy Livramento, Enforcement Program Manager
Subject: Enforcement Program Updates
Purpose: Update on Enforcement Program
Attachments: 11 (a) Enforcement and Probation Performance
Measures Q2, 2025/2026
Background:
This is a report on the updates involving the Board’s Enforcement Unit for Q2, FY
2025/2026.
Please also refer to attachment 11(a), which encompasses the Enforcement Program
statistics.
Analysis:
Enforcement staff continue to work hard on all enforcement related matters. During Q2,
enforcement staff focused on aged cases meeting regularly with me and Executive
Director Erika Calderon. During these meetings, we focused on sending quality of care
cases for review to a medical consultant, and forwarding to HQIU as necessary, based
on the medical consultant’s review. In addition to focusing on aged cases, statistics report
an increase from Q1 to Q2 in administrative actions and complainant interviews
conducted.
Effective October 1, 2025, the Board was granted additional citation authority for all
violations of the practice act. This additional authority will allow the Board to issue more
administrative citations after enforcement review of complaints, which in the past may
have been closed without action because the Board did not have authority to issue
citations for certain violations, and the violations did not rise to the level of formal
discipline. Eight (8) administrative citations were issued just in quarter 2.
Twenty-two (22) complainant interviews were offered. Eleven (11) were completed, six
(6) had no response, and the remaining five (5), are pending, as the interview notice was

mailed in December.
Board Program Statistics:
For statistics, please refer to attachment 11(a) which covers the Enforcement Program’s
total numbers report out by the end of Q2, fiscal year 2025/2026.
Performance Measure 1 (PM1): covers the amount of consumer complaints, arrests,
and convictions received. So far this fiscal year the Board has received a total of 630
complaints and 12 arrest/conviction notices. A significant increase of an overall 25% of
total complaints and arrest/convictions in comparison to last fiscal year. The increase
in complaints received can still be attributed to the Board’s outreach efforts and the
increase in licensee population.
Performance Measure 2 (PM2): is the average number of days it takes for our analysts
to initiate complaints and acknowledge receipt. The target for this performance measure
is ten (10) days and we are at five (5) days year to date.
Performance Measure 3 (PM3): is the average number of days it takes to complete
investigations and enforcement action for cases that are not referred to the Attorney
General’s Office for formal discipline. Case aging here fluctuates greatly because it
takes an average of all cases, and one or two very complicated cases can skew these
numbers drastically. These number include the timeline for desk and formal
investigation timelines. The target for PM3 is 360 days. Our average is at 222 days.
Although this average is a bit higher than last fiscal year, this slight increase can be
attributed to an increase in formal investigations. Last year around this time the Board
had 91 formal investigations pending. This year the Board is at 134 active formal
investigations. This is a 47% increase.
Performance Measure 4 (PM4): is the average number of days it takes to complete
investigations and enforcement actions that are transmitted to the Attorney General’s
Office for formal disciplinary action. Case aging in this category is at 759 days, which is
down from 1027 days, a 26% decrease.
For Q2 2025/2026, the Board continues to be well under its performance measure
targets for three (3) of its performance measures. As previously reported PM4 is the
measure that unfortunately the Board has less control over as this measure takes into
consideration the timeline from the Attorney General’s Office, respondent’s legal
representatives, and the Office of Administrative Hearings.
The Board currently has 733 pending enforcement cases, with 134 of those cases
pending formal investigations, and 20 of those pending cases at the Attorney General’s
Office. The remaining 599 cases are split between enforcement analysts.
YTD the Board has filed nine (9) accusations, one (1) petition to revoke probation,
issued four (4) public letters of reprimand, placed three (3) licensees on probation,
issued three (3) cease practice orders, and issued one (1) automatic suspension order.
Additionally, five (5) probationers completed probation, and the Board issued two (2)
orders accepting the surrender of a license and ordered three (3) revocations of license.
Nine (9) administrative citations have been issued as well.

      Five (5)- Year Comparison Chart of Complaints Received/Discipline Imposed
|     |                                       | 2020/2021 | 2021/2022 | 2022/2023 | 2023/2024 | 2024/2025 |      |
| --- | ------------------------------------- | --------- | --------- | --------- | --------- | --------- | ---- |
|     | Complaints and Arrest Received        |           | 596       | 650       | 669       | 889       | 1041 |
|     | Accusations/Amended Accusations Filed |           | 9         | 21        | 16        | 14        | 13   |
|     | Accusation and Petition to Revoke     |           | 0         | 0         | 0         | 1         | 1    |
|     | Citations                             |           | 3         | 3         | 11        | 7         | 3    |
|     | PR/PLR                                |           | 1         | 4         | 0         | 12        | 4    |
|     | Probation                             |           | 9         | 3         | 5         | 11        | 10   |
|     | Surrender                             |           | 1         | 4         | 3         | 2         | 2    |
|     |                                       |           |           |           | 4         | 2         | 3    |
|     | Revocation                            |           | 1         | 2         |           |           |      |

Action Requested: No Action Required

---

**[MINUTES] 2026-01-22_20260122_mat_11a.pdf**

Osteopathic Medical Board of CA
11 (a) Attachment
Enforcement Performance Measures Q2

Osteopathic Medical Board of CA
11 (a) Attachment
Enforcement Performance Measures Q2

PM1: Complaint Intake- Complaints and Convictions Received
PM2: Cycle Time - Intake - Average number of days from the date the complaint was received to the date the complaint was closed or
assigned for investigation (assigned to staff).
PM3: Cycle Time - Investigations - Average number of days to complete the entire enforcement process for complaints not transmitted to
the AG for formal discipline.  (includes intake and investigation days)

PM3a: Intake Only - Of the cases included in PM3, the average number of days from the date the complaint was received to the date the
complaint was assigned for investigation.
PM3b: Investigation Only - Of the cases included in PM3, the average number of days from the date the complaint was assigned for
investigation to the date the investigation was completed.  (without intake)

PM3c: Post Investigation Only - Of the cases included in PM3, the average number of days from the date the investigation was completed
to the date of the case outcome or non-AG formal discipline effective date.
PM4:Cycle Time-AG Transmittal - Average number of days to complete the enforcement process for cases investigated and transmitted to
the AG for formal discipline. (includes intake & investigation to final outcome of cases transmitted to the AG - includes withdraws, dismissals,
etc.)

PM4a: AG Transmittal - Intake Only - Of the cases included in PM4, the average number of days from the date the complaint was received
to the date the complaint was assigned for investigation.

PM4b: AG Transmittal - Investigation Only - Of the cases in PM4, the average number of days from the date the complaint was assigned for
investigation to the date the investigation was completed.
PM4c: AG Transmittal - Pre AG Transmittal - Of the cases in PM4, the average number of days from the date the investigation was
completed to the date the case was transmitted to the AG.
PM4d: AG Transmittal - Post AG Transmittal - Of the cases in PM4, the average number of days from the date the case is transmitted to
the AG to the date of the case outcome or formal discipline effective date.  (AG days only)

---

**[MINUTES] 2026-01-22_20260122_mat_12.pdf**

Agenda Item 12

Osteopathic Medical Board of California

DATE REPORT ISSUED:

January 22, 2026

ATTENTION:

Members, Osteopathic Medical Board of California

SUBJECT:

Probation Program Update

STAFF CONTACT:

Ralph Correa, Probation Monitor

REQUESTED ACTION:
This report is intended to provide the Members of the Osteopathic Medical Board
of California (OMBC) with an update on the probation program.

No action is needed.

Total Numbers of physicians on probation

As of today’s date, there are 31 licensees on active probation.

Five (5) are tolling out of state and are not receiving credit towards completion
of  probation,  26  are  actively  being  monitored  and  are  practicing  medicine  in
California.

There are also Two (2) physicians who have received public letters of reprimand
and are being monitored by the probation unit for course activity completion.

Review of cases

Intake  and  quarterly  reviews  are  conducted  both  in  person,  via  zoom  or
telephone with each physician to discuss their specific terms and conditions.  All
information and all documents are analyzed, recorded and documented in a full
report.  The  Osteopathic  Medical  Board’s  Probation  unit  has  maintained  an
effective and thorough accountability of our physicians on probation.

Non-Compliance

Three cease practice orders have been placed on licensees that have violated
their probation. In addition, the Board has filed two petitions for revocation due
to probationary issues.

---

**[MINUTES] 2026-01-22_20260122_mat_13.pdf**

DEPARTMENT OF CONSUMER AFFAIRS BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM GOVERNOR
OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
(916) 928-8390 | F (916) 928-8392 www.ombc.ca.gov
DATE January 22, 2025
TO OMBC Board Members, Osteopathic Medical Board of California
Terri Thorfinnson, J.D.
FROM
Legislative and Regulatory Specialist
Agenda Item 13 -- Rulemaking Update – 2026 Rulemaking for Pending or
RE:
Proposed Regulations
Rulemaking Update Summary
The Board has two regulatory packages moving along in the rulemaking process. The Fees and License
Status rulemaking documents are still pending review within DCA. This rulemaking package is being split
into two separate rule making packages: fees only that was approved by the Board at the November 13,
2025, Board meeting and the rest of the language that updates other regulatory sections. The fees’
rulemaking package is the one moving forward with the Board approved language. The new rulemaking
package made up of regulatory updates for other sections will be put together to be reviewed by the Board
at a later date. The fees’ rulemaking package is the priority for meeting the deadlines for the Oversight
Report, which the Board will review and approve the fall 2026.
The Disciplinary Guidelines rulemaking package and language is in the initial stages. Preliminary draft of the
proposed language was reviewed by Regulatory Counsel and that draft is being reviewed and further
revised. OMBC staff has been working closely with the Regulatory Attorney to revise and finalize the
proposed language. This process has taken longer than expected and is continuing. The Board staff is trying
to anticipate as many of the changes needed upfront before the Enforcement Committee and Board review
it. It is anticipated that more input and revisions will be made in the coming months and once staff finishes
its revisions, then the document will be presented to the Enforcement Committee of the Board for further
review and input. After the Enforcement Committee finishes their review, it will go back to DCA for further
review. The soonest this rulemaking package could go to the Board for their review is the May board
meeting in 2026. This is another large rulemaking package that is complex because it is creating a new
Disciplinary Guidelines document that has not been amended since 1996 and includes the Uniform
Standards for Substance Abusing Licensees.

Rulemaking Status: Fees and License Status

Concept/  DCA pre-review   Board  Draft  DCA   Agency  DOF   Filing
| Draft      |     | approval  |             |            |            |            |               |
| ---------- | --- | --------- | ----------- | ---------- | ---------- | ---------- | ------------- |
|            |     |           | Regulatory  | Director   | Approval   | Approval   | regulatory    |
| language   |     | of        |             |            |            |            |               |
|            |     |           | documents/  | Approval   |            |            | package with  |
Language
|     |     |     | review   |     |     |     | OAL   |
| --- | --- | --- | -------- | --- | --- | --- | ----- |
1/1/2024   2/1/24,2/15/24   8/15/2024,  8/16/2024,
2/28/24, 4/12/24,
|     |                    | November   | 7/8/2025,   |     |     |     |     |
| --- | ------------------ | ---------- | ----------- | --- | --- | --- | --- |
|     | 4/12/24,5/9/24,    | 13, 2025   | Legal and   |     |     |     |     |
|     | 6/5/24,7/10/24,    |            | Budgets     |     |     |     |     |
|     | 7/22/24, 7/26/24   |            | review and  |     |     |     |     |
approval
pending
| 45-day    | Board Respond  | Final   | Submit to      | OAL         | Effective    |     |     |
| --------- | -------------- | ------- | -------------- | ----------- | ------------ | --- | --- |
|           |                |         |                |             |              |     |     |
| comment   |                | review  |                |             |              |     |     |
|           | to comments    |         | DCA Director,  | approval    | Date         |     |     |
| period    |                | with    |                |             |              |     |     |
|           |                |         | OAL for        | or denial   |              |     |     |
Regulatory
approval
Attorney
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Rulemaking Status: Disciplinary Guidelines

| Concept/  | DCA pre-review  |        |        |       |         |       |         |
| --------- | --------------- | ------ | ------ | ----- | ------- | ----- | ------- |
|           |                 | Board  | Draft  | DCA   | Agency  | DOF   | Filing  |
Draft  approval  Regulatory  Director   Approval  Approval  regulatory
| language   |           | of        | documents/  | Approval  |     |     | package   |
| ---------- | --------- | --------- | ----------- | --------- | --- | --- | --------- |
|            |           | Language  | review      |           |     |     | with OAL  |
| 1/31/2020  | 9/19/23,  |           |             |           |     |     |           |
10/9/23,
11/16/23,
3/8/24, 4/16/24,
pending
45-day  Board Respond  Final  Submit to  OAL  Effective
| comment   | to comments  | review       | DCA        | approval   | Date  |     |     |
| --------- | ------------ | ------------ | ---------- | ---------- | ----- | --- | --- |
| period    |              | with         | Director,  | or denial  |       |     |     |
|           |              | Regulatory   | OAL for    |            |       |     |     |
|           |              | Attorney     | approval   |            |       |     |     |
|           |              |              |            |            |       |     |     |

---

### 2025-11-13 — Osteopathic Medical Board of California — November 13, 2025

**[AGENDA] 2025-11-13_20251113_agenda.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 |F (916) 928-8392 | www.ombc.ca.gov

MEMBERS OF THE BOARD
President
Deni   se Pines, MBA
V ice President
Hem esh Patel, D.O.
Secretary
Gor Adamyan

 QUARTERLY BOARD MEETING AGENDA

Department of Consumer Affairs – HQ1
Hearing Room

1625 North Market Blvd.
Sacramento, CA 95834
(916) 928-8390 Office Main Line

Thursday, November 13, 2025
9:00 a.m. – 5:00 p.m.
(or until the conclusion of business)

Joh n M. Cummins, J.D.
Brett Lockman, D.O.
Negeen Mirreghable,Esq.
Ma tthew Swain, D.O.

Public WebEx/Telephone Access – See Attached
Meeting Information

MEETING TIMES AND ORDER OF AGENDA ITEMS ARE
SUBJECT TO CHANGE

Action may be taken on
any item listed on the
agenda

While the Board intends to
webcast this meeting, it
may not be possible to
webcast the entire open
meeting due to limitation
on resources or technical
difficulties.

Please see Meeting
Information section for
additional information on
public participation.

The Osteopathic Medical Board of California (Board) will meet in-person in
accordance with Government Code section 11123, subdivision (a).

Discussion may be had and action may be taken on any item on the agenda

OPEN SESSION

1.

2.

3.

4.

5.

Call to Order/Roll Call/ Establishment of a Quorum- Machiko Chong, Licensing
Program Manager

Reading of the Board’s Mission Statement– Erika Calderon, Executive Director

Public  Comment  on  Items  Not  on  the  Agenda  -Denise  Pines,  MBA.
The  Board  may  not  discuss  or  take  action  on  any  matter  raised  during  this
public  comment section  except  to  decide  whether  to  place  the  matter  on
the  agenda  of  a  future  meeting.  (Government  Code  sections  11125,
11125.7(a).)

Review  and  Possible  Approval  of  Board  Meeting  Minutes  -  Beth  Clark,
Associate Governmental Program Analyst

A. August 14, 2025, Board Meeting Minutes

Hearing on Petition for Early Termination of Probation, Abdallah Youssef Eman, DO
(20A 14213)

Deliberation and possible action on disciplinary matters, including petitions,
proposed  decision,  non-adopt  proposed  decisions,  and  stipulations
(Government Code section 11126 (c)(3).)

OPEN SESSION

6.

7.

8.

9.

10.

11.

12.

President’s Report- Denise Pines, MBA

Board Member Communications with Interested Parties-   Denise Pines, MBA

Intergovernmental Relations Reports and Administrative Services Update

A. DCA Update – Shelly Jones, Staff Services Manager II, SOLID, DCA
B. Budget Update  –  Kaila  Van  Lindt  and  Harmony  DiFilippo,  Budget  Office,

DCA

Executive Director’s Report- Erika Calderon, Executive Director
Administrative  Services,  including  administrative  services,  personnel,  and
technology updates

Licensing/Admin  Program  Summary,  including  licensing  unit  updates,  and
statistics- Machiko Chong, Licensing Program Manager

Enforcement  Program  Summary,  including  enforcement  unit  updates,  and
statistics- Cristy Livramento, Enforcement Program Manager

Probation Program Summary, including probation unit updates and statistics-
Ralph Correa, Probation Monitor

  BREAK AND RECONVENE IN OPEN SESSION

13.

14.

Rulemaking  Update-Report  on  Pending  or  Proposed  Regulations-Terri
Thorfinnson, Legislative and Regulatory Specialist

Discussion and Possible Action to Consider Initiation of a Rulemaking to
Amend  Sections 1630, 1636, 1646, 1647, 1656, 1658, and 1690, and to Adopt
Section 1648 in Division 16 of Title 16 of the California Code of Regulations
(Retired License, Petitions and Fees) - Terri Thorfinnson, Legislative and
Regulatory Specialist and Kristy Schieldge, Attorney IV, Legal Affairs Division’s
Regulations Unit, DCA

15.

Discussion on Legislation – Terri Thorfinnson, Legislative and Regulatory
Specialist

• AB 54 Keep Abortion Pill Safe

• AB 260 Sexual and Reproductive Freedom

• AB 360 Menopause Survey

• AB 432 Mandatory CME: Menopause: Treatment

• AB 742 License Application Expedite: Descendants of Slaves

• AB  489  Prohibition  of  AI:  Deception  use:  posing  as  licensed

professionals

• AB  667  Board  Paid  Interpreters  for  State  Exams  and  License

Applications

• AB 876 Nurse Anesthetists; Expansion of Scope of Practice

• AB 1215 Hospital Membership: Non-physician expansion.

• SB 508 License Exemption for Out of State Telemedicine Physicians

• SB 641 State of Emergency: Board Authority to waiver or exempt

• AB 460 (Chen)Radiologic Technologists: Telemedicine

Supervision: Scope of Practice

• AB 967 Expedited Processing Fee

16.

2025 Informational Bill “Watch” List

• AB 50 Pharmacies furnishing contraception

• AB 346 Home Health Care Workers

• AB 408 (MBC) Physician Health and Wellness Program

• AB 447 E.R. Dispense Unused Prescription

• AB 479 Criminal Procedure: Vacatur Relief: Harm Findings

• AB 485 (Ortega) Discipline: Unsatisfied Judgment: Non-payment

of Wages

• AB 511 Radiologist Assistants

•  SB 679 Health Facilities 805 Reporting: 805 by race and gender

•  AB  1037  (Elhawary)  Public  Health:  Overdoes  Treatment  by  Non-

Physicians

•  AB 1186 Demographics data

•  AB 1501 (Berman) P.A. Supervision Scope of Practice

•  SB 387 Residency Accreditation Eligibility Revision

•  SB 470 Open Meetings Law

•  SB 518 Descendants of Slaves Certification

16.

Solicit Future Agenda Items and Meeting Dates-Denise Pines, MBA

17.  Adjournment

Online Access of Meeting

The Osteopathic Medical Board of California will also broadcast the public portion
of its meeting via WebEx Events. To participate in the WebEx Events meeting, please
log on to this website on the day of the meeting:

Click Here to Join Meeting

If joining by phone
+1-415-655-0001 US Toll
Access code: 2495 877 3144
Passcode: 66221113

Experiencing issues joining the Meeting?

Copy and paste the link text below into an internet browser:

https://dca-meetings.webex.com/dca-
meetings/j.php?MTID=m6e701368ddc920571f295fa36d52dfcf

Members of the public may but are not obligated to provide their names or personal
information  as  a  condition  of  observing  or  participating  in  the  meeting.  When
signing  into  the  WebEx  platform,  participants  may  be  asked  for  their  name  and
email  address.  Participants  who  choose  not  to  provide  their  names  will  need  to
provide  a unique identifier  such  as  their  initials  or  another  alternative,  so  that  the
meeting  moderator  can  identify  individuals  who  wish  to  make  public  comment;
participants who choose not to provide their  email  address  may  utilize  a  fictitious
email address like in the following sample format: XXXXX@mailinator.com.

Please Note: Because there is an audio delay, if you are participating by phone and

simultaneously watching the Webcast, the Board requests you turn off the sound to
the Webcast for improved clarity.

For further information about this meeting, please contact Machiko Chong at 916-
928- 7636 or in writing at 1300 National Drive, Suite 150, Sacramento, CA 95834. This
notice and agenda, and any available Board meeting materials, can be accessed
on the Board’s website at www.ombc.ca.gov

In accordance with the Bagley-Keene Open Meeting Act, all meetings of the Board,
including  the  teleconference  sites,  are  open  to  the  public.  Government  Code
section  11125.7  provides  the  opportunity  for  the  public  to  address  each  agenda
item during discussion or consideration by the Board prior to the Board taking any
action  on  said  item.  Members  of  the  public  will  be  provided  appropriate
opportunities to comment on any issue before the Board, but the Board President,
at  his  or  her  discretion,  may  apportion  available  time  among  those  who  wish  to
speak. Individuals may appear before the Board to discuss items not on the agenda;
however, the Board can neither discuss nor take official action on these items at the
time of the same meeting. (Government Code sections 11125, 11125.7(a).)

Board  meetings  are  held  in  barrier  free  facilities  that  are  accessible  to  those  with
physical disabilities in accordance with the Americans with Disabilities Act (ADA). If
you  are  a  person  with  a  disability  requiring  disability-related  modifications  or
accommodations to participate in the meeting, including auxiliary aids or services,
please  contact  Machiko  Chong,  ADA  Liaison,  at  (916)  928-7636  or  e-mail  at
Machiko.Chong@dca.ca.gov or send  a written request to the Board’s office at 1300
National Drive, Suite 150, Sacramento, CA 95834-1991.  Providing your request at least
five  (5)  business  days  before  the  meeting  will  help  to  ensure  availability  of  the
requested accommodation. Requests should be made as soon as possible, but at
least five (5) working days prior to the scheduled meeting. You may also dial a voice
TTY/TDD Communications Assistant at (800) 322-1700 or 7-1-1.

---

**[MINUTES] 2025-11-13_20251113_item_4a.pdf**

MEMBERS
PRESENT:

STAFF
PRESENT:

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390    |    F (916) 928-8392    |    www.ombc.ca.gov

Osteopathic Medical Board of California

 Teleconference Minutes

August 14, 2025

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Andrew Moreno, Esq.
Brett Lockman, D.O.
Matthew Swain, D.O.

Erika Calderon, Executive Director
Machiko Chong, Licensing Program Manager
Cristy Livramento, Enforcement Program Manager
Terri Thorfinnson, Legislative and Regulatory Specialist
Ralph Correa, Probation Monitor
Beth Clark, Associate Governmental Program Analyst
Yuping Lin, Board Counsel
Arthur Babakhan, OIO Manager, Department of Consumer Affairs
Kalia Van Lint, Budget Analyst, DCA Budget Office
Julia E. Cox, Administrative Law Judge, OAH
Christopher Young, Deputy Attorney General
Maryam Ahmad, Deputy Attorney General
Kaila Vanlint, DCA Budget Analyst
Nicole Dragu, DCA Budget

MEMBERS OF
THE AUDIENCE:

Chris, Student Government President
David, Student Governing Body
Darra, OMS II
Arnold Kim, OMS II
Cameron Quill, OMS II
Holly Macriss, Executive Director, OPSC
Michelle Monserratt-Ramos, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Tracy Dominguez, Consumer Watchdog

Board Meeting Minutes – August 14, 2025

Agenda Item 1

Call to Order and Roll Call/Establishment of a Quorum

The Board Meeting of the Osteopathic Medical Board of California (OMBC) was called
to order by Madame President Denise Pines at 09:03 a.m.

Machiko Chong called roll and determined a quorum was present. The meeting was
held at Touro University College of Osteopathic Medicine. Board guidelines for
conducting the meeting under the Open Meetings Act were reviewed, including rules for
public comment and remote board member visibility.

Agenda Item 2

Reading of the Board’s Mission Statement

Executive Director Erika Calderon read the Board’s mission statement: "to protect the
public by requiring competency, accountability, and integrity in the safe practice of
medicine by our osteopathic physicians and surgeons".

Agenda Item 3

Public Comment for Items not on the Agenda

President Denise Pines opened the floor for public comments on items not explicitly on
the agenda.

The host requested online comments; no public comments were made in the meeting
room or online.

Agenda Item 4 & 5

Petition for Early Termination of Probation

Administrative Law Judge (ALJ) Juliet E. Cox presided over two hearings for early
termination of probation petitions.

The Board was advised that deliberations and decisions would occur later in closed
session, and petitioners would receive written decisions.

Petition for Early Termination of Probation, Steven Duane Western, D.O.

The hearing opened for Dr. Western's petition for early termination of his four-
year probation, effective October 10, 2022.

Deputy Attorney General Christopher Young outlined the disciplinary order
stemming from allegations admitted by Dr. Western, including practicing
psychiatry on a family member (which he agreed constituted gross negligence)
and inadequate electronic health record (EHR) keeping (lacking BMI metrics). Dr.

Board Meeting Minutes – August 14, 2025

Western testified he has corrected all issues and would now refer complex
psychiatric cases to a psychiatrist. He noted he is in full compliance with all
probation terms. The Board took the matter under submission for closed session
deliberation.

Dr. Western was placed on four years of probation effective October 10, 2022,
and was petitioning for early termination after serving approximately three years.
Dr. Western stipulated that allegations in the accusation were deemed true,
correct, and fully admitted, with the exception of one paragraph regarding
Percocet prescription. The misconduct involved gross negligence related to
treating a family member (Patient A) for Dissociative Identity Disorder (DID) and
inadequate medical record keeping (lacking BMI index). Dr. Western agreed that
practicing psychiatry on a family member constituted gross negligence. He
affirmed he had corrected the issues and complied with all required probation
terms. The Attorney General’s office noted that the petitioner has the burden to
show rehabilitation by presenting clear and convincing evidence.

Petition for Early Termination of Probation, James Michael Lally, D.O.

The hearing opened for Dr. Lally's petition for early termination of his three-year
probation, which became final on July 31, 2023.

Deputy Attorney General Maryam Ahmad detailed the underlying allegations
admitted by Dr. Lally in the stipulated settlement, including sexual harassment,
gender and national origin discrimination, creating a hostile work environment,
misuse of his board position to intimidate residents, and failure to disclose
conflicts of interest while serving as a medical consultant. Dr. Lally testified he
separated from the hospital environment in 2018, completed ethics and civility
courses, and now lectures on safeguarding emotional stability for the
International Olympic Committee. Board member Dr. Patel questioned how the
board could ensure the protection of future medical professionals moving
forward. The AG noted that Dr. Lally appeared to still struggle with fully accepting
responsibility for his role in creating the hostile environment. The Board took the
matter under submission.

Pursuant to section 11126(c)(3) of the Government Code, the Board met in closed
session for discussion and to take action on disciplinary matters, including the above
petitions.

CLOSED SESSION

Board Meeting Minutes – August 14, 2025

Agenda Item 7

Review and Possible Approval of Minutes

Associate Governmental Program Analyst Beth Clark presented the minutes from the
February May 15, 2025, Teleconference Board Meeting.

Edits or corrections were identified after review:

Agenda Item 2: The mission statement should be corrected to read "osteopathic
physicians" (correcting "positions").

Agenda Item 15 (Legislation): The motion to support AB 489 (Prohibition of AI:
Deception use) was mistakenly referenced as AB 742 (Expedite License
Applications for Descendants of Slaves) on Page 11 of the draft minutes.

Motion to adopt the minutes as amended by the board members’
recommendations

Motion – Dr. Patel Second – Mr. Cummins
•  Aye – Mr. Adamyan, Mr. Cummins, Dr. Lockman, Mr. Moreno, Dr. Patel, Ms.

Pines, Dr. Swain

•  Nay – None
•  Abstention – None
•  Absent – None

Motion carried to approve the May 15, 2025 minutes as amended.

No public comments were made online or in the meeting room

Agenda Item 8

President’s Report

Madame President Denise Pines reported on the OMBC's activities:

Planning a "Hill Day" in January 2026 before the board meeting to meet with
legislators, share an overview of the DO profession, and build support for a future
bill to protect the DO name/identity.

Board Meeting Minutes – August 14, 2025

The Federation of State Medical Boards (FSMB) has convened a work group on
prescribing and dispensing trends, focusing on the growth of IV hydration and
ketamine clinics.

The FSMB is monitoring federal developments regarding telemedicine and
license portability.

The FSMB launched an Office of AI innovation.

The FSMB launched a digital campaign with three videos, viewed over 7 million
times, leading consumers to the website carematters.org for information on
medical boards.

Ms. Pines announced upcoming speaking engagements: September 3rd in
Dublin, Ireland, at the International Association of Medical Regulatory Authorities
(presenting guidance on medical racism and discrimination standards), and
September 25th at the Congressional Black Caucus Legislative Meeting (on
menopause and healthcare disparities)

.
No public comments were made online or in the meeting room.

Agenda Item 6
Answer Forum

Osteopathic Physician and Surgeon Student Question and

This item was addressed following the President's Report.

Five students from Toro University College of Osteopathic Medicine participated.

Addressing Mistakes:
Board members advised students to uphold humility, seek counsel, own up to
mistakes, and prioritize the patient over system demands (volume, machine
needs). Dr. Lockman referred to DOs as "MD+" and stressed using the
osteopathic structural exam to differentiate practice.

Protecting the DO Role:
Members strongly encouraged students to join professional organizations
(OPSC, AOA, OIA) to guide legislators and ensure their voice is heard.

Licensure:

Board Meeting Minutes – August 14, 2025

OMBC currently does not license international osteopaths; training must be
completed at a COCA-approved school in the United States.

Residency/Advocacy:
Students voiced concerns over federal policy shifts, medical school debt, and
residency spots.

Board members noted that residency funding is a national political question (CMS
policy). OMBC staff noted that awareness outreach helps increase patient demand for
DOs, which could open up residency opportunities. Board members encouraged
students to be active, advocate, and consider academic medicine (GME).

Agenda Item 9

Board Member Communications with Interested Parties

Madame President Denise Pines requested disclosures.

No board members had disclosures. No public comments were made online or in the
meeting room.

Agenda Item 10
Services Update

Intergovernmental Relations Reports and Administrative

DCA Update Arthur Babakhanyan, OIO Manager, reported that Governor Newsom’s
reorganization plan was enacted on July 5th, splitting the Business, Consumer Services
and Housing Agency.

New rules include:

•  The DCA will be housed in the new Business and Consumer Services Agency, effective

July 1, 2026.

•  The return-to-office requirement (four days in-office per week, per Executive Order N-22-

25) was postponed until July 1, 2026, due to labor union negotiations.

•  Out-of-state travel is restricted to "mission critical" needs and requires eight weeks'

advance notice to the DCA budget office.

•  Public comment: Holly Macriss (OPSC ED) requested that OMBC staff and leaders

continue to be allowed to travel to OPSC meetings to interact with DOs.

Budget Update Kalia Van Lint, Budget Analyst, reported the FY 2024-25 projected
ending balance is $4.61 million (11.9 months in reserve).

Board Meeting Minutes – August 14, 2025

The fund condition statement includes a conservative ongoing 3% interest
applied to expenditures to account for future personnel adjustments (salary,
retirement).

Agenda Item 11   Executive Director’s Report

Executive Director Erika Calderon provided personnel and administrative updates.

•  Personnel Updates: Public board members Gor Adamyan and John Cummins were

reappointed.

The board has hired a Special Investigator, Yvonne Nathad, scheduled to
start September 8, 2025. This position is projected to handle 60% of overall
field investigations and achieve a minimum cost savings of $150,000 per
fiscal year in DFI costs.

•  Subpoena Authority: OMBC is obtaining subpoena enforcement authority to handle

administrative record requests in-house.

•  Purge Project/Retention Schedule: The retention schedule was revised in July

2025.

The "purge project" addresses decades of backlog. Retention for a "quality of
care, no violation complaint involving patient death" was extended to five
years.

•  Budget Mitigation: OMBC projects an annual revenue increase of approximately
$694,000 from DFI cost savings ($150k), new CME/Cite and Fine regulations
($120k), and proposed fee increases (Applications/Petitions/Retired License)
($424k).

•  Outreach: The board is working on the 4th edition of the OsteoScope newsletter and

creating a consumer complaint video.

Due to budget constraints (mission critical t

*[document truncated for length]*

---

**[MINUTES] 2025-11-13_20251113_item_7a.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390

|  www.ombc.ca.gov

|  F (916) 928-8392

MEMBERS
PRESENT:

STAFF
PRESENT:

Osteopathic Medical Board of California

AMENDED Board Meeting Minutes

November 13, 2025

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Brett Lockman, D.O.
Matthew Swain, D.O.

Erika Calderon, Executive Director
Machiko Chong, Licensing Program Manager
Cristy Livramento, Enforcement Program Manager
Terri Thorfinnson, Legislative/Regulatory Specialist
Shelly Jones, Asst. Deputy Director, DCA
Kaila Van Lint, Budget Analyst, DCA
Suzanne Balkis, Budget Manager, DCA
Marcy Larson, Administrative Law Judge, OAH
Matthew Fleming, Deputy Attorney General
Beth Clark, Associate Governmental Program Analyst
Ralph Correa, Probation Monitor
Yuping Lin, Board Counsel
Kristy Schieldge, Regulations Counsel

MEMBERS OF
THE AUDIENCE:

Holly Macriss, Executive Director, OPSC
Michelle Monserratt-Ramos, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Kimberly Turbin, Consumer Watchdog
Tracy Dominguez, Consumer Watchdog

Board Meeting Minutes – November 13, 2025

Agenda Item 1

Call to Order/Roll Call/Establishment of a Quorum

The Quarterly Board Meeting of the Osteopathic Medical Board of California (OMBC)
was called to order by President Denise Pines at 9:00 a.m.

Machiko Chong called roll and determined a quorum was present. The meeting was
held at the Department of Consumer Affairs, Hearing Room HQ1, in Sacramento, CA.

Agenda Item 2

Reading of the Board’s Mission Statement

Executive Director Erika Calderon read the Board’s mission statement: "to protect the
public by requiring competency, accountability, and integrity in the safe practice of
medicine by osteopathic physicians and surgeons"

Agenda Item 3

Public Comment on Items Not on the Agenda

President Pines opened the floor for public comments.

The WebEx moderator checked for online requests; no public comments were made for
items not on the agenda.

Agenda Item 4

Review and Possible Approval of Board Meeting Minute

Beth Clark presented the minutes from the August 14, 2025, Board Meeting.

Public Comment: Holly Macriss (OPSC) requested a correction on page 11 to clarify
that she stated she would be updating the Board on the upcoming osteopath bill, rather
than requesting updates from the Board.

Motion to adopt the August 14, 2025, minutes as amended.

Motion – Dr. Patel Second – Mr. Cummins

•  Aye – Adamyan, Cummins, Lockman, Patel, Pines, Swain
•  Nay – None
•  Abstention – None
•  Absent – Negeen Mirreghabie

Motion carried to approve the minutes as amended.

Board Meeting Minutes – November 13, 2025

Agenda Item 5:

Hearing on Petition for Early Termination of Probation

Administrative Law Judge (ALJ) Marcy Lawson presided over the hearing for Eman
Abdallah, D.O.

Deputy Attorney General Matthew Fleming represented the People. Dr. Abdallah
represented herself and was sworn in.

Deputy AG Fleming provided a history of the case, noting Dr. Abdallah’s license was
placed on five years of probation in June 2023 for gross negligence and aiding
unlicensed practice at med spas.

Dr. Abdallah testified regarding her rehabilitation, her current ownership of a private
practice where she performs all medical treatments herself, and her improved record-
keeping systems. Deputy AG Fleming recommended the Board continue the probation,
noting it was the earliest possible time for a petition and that the public interest is best
served by allowing the term to play out. The Board took the matter under submission for
deliberation in closed session.

Agenda Item 6:

President’s Report

President Denise Pines reported on:

•  Personnel Changes: Recognition of Andrew Moreno for seven years of service;

welcome to new member Negeen Mirreghabie (spectator online, joining in person in
January).

•  Events: Announcement of "Hill Day" on January 21, 2026, to meet with legislators.

•

International/National: Updates on the Federation of State Medical Boards (FSMB)
meeting in Dublin regarding medical racism standards and the emerging licensing
pathway for "assistant physicians".

•  DCA Leadership: Acknowledgment of DCA Director Kimberly Kirchmeyer’s

upcoming retirement.

•  Public Comment: Representatives from Consumer Watchdog criticized the use of
clinical terminology such as "cradle to the grave" and requested that enforcement
committee meetings be held in public.

Agenda Item 7:

Board Member Communications with Interested Parties

President Pines requested disclosures. No board members reported communications.

Board Meeting Minutes – November 13, 2025

Agenda Item 8:
Services Update

Intergovernmental Relations Reports and Administrative

•  DCA Update: Shelly Jones reported on the appointment of Lucy Saldivar as Deputy
Director of Board and Bureau Relations and provided updates on mandatory training
(Sexual Harassment Prevention and Unconscious Bias).

•  Budget Update: Kaila Van Lindt reported the Board ended FY 24/25 with

approximately 12.4 months in reserve. However, future expenditures are projected to
increase by 3% annually while revenues remain static.

Agenda Item 9:

Executive Director’s Report

Erika Calderon introduced new staff members Rachel Molina (Enforcement Analyst)
and Yvonne Almazan (Special Investigator).

She noted that enforcement staff have returned to the office three days per week for
onboarding and collaboration.

Agenda Item 10:  Licensing/Admin Program Summary

Machiko Chong reported a total population of 17,012 licensed D.O.s. Total applications
are up 17% overall.

Revisions were made to FNP applications to clarify requirements for various filing types.

Agenda Item 11:  Enforcement Program Summary

Cristy Livramento reported 320 complaints received this quarter, a 33% increase from
the previous year.

Referred cases to the AG doubled compared to the same quarter last year.

Public Comment: Consumer Watchdog volunteers shared personal stories regarding
the impact of physician negligence and requested transparency in case management.

Agenda Item 12:  Probation Program Summary

Ralph Correa reported 31 active probationers.

Board Meeting Minutes – November 13, 2025

He detailed field monitoring efforts, including unannounced visits to ensure compliance
with cease practice orders.

Agenda Item 13:  Rulemaking Update

Terri Thorfinnson confirmed that the prior regulatory package became effective October
1, 2025.

The Fee and License Status package and Disciplinary Guidelines are currently in
progress

Agenda Item 14:  Discussion and Possible Action to Consider Initiation of a
Rulemaking to Amend Sections 1630, 1636, 1646, 1647, 1656, 1658, and 1690,
and to Adopt Section 1648 in Division 16 of Title 16 of the California Code of
Regulations (CCR) (Retired License, Petitions and Fees)

Terri Thorfinnson presented an overview of the proposed regulatory changes, which are
set forth in the meeting materials. For this package, the Board reviewed a trimmed
down version of a prior approved rulemaking package from August of 2025. The focus
of this rulemaking is solely fee increases, specifically to raise fees to the statutory
maximums authorized by law, set a retired license status, and set petition fees to
include adjudication fees previously not considered by the Board.

Board staff noted that in the prior version adopted by the Board in August of 2025, staff
was overly ambitious and diverted the attention from the fees and priority of the
increase of these fees to also focus on making some amendments to application
language. However, it was noted that further changes in the application language were
needed after the compilation of the package. The Board’s Executive Director did not
want further delays to this critical fee rulemaking and recommended removing
amendments that did not otherwise relate to fee increases or address the Board’s long-
standing goal of establishing a retired license and establish its petition fees, so it was
decided to present the Board with this trimmed down version; application amendments
will be addressed in a separate package at a later time. This proposed language is the
result of that recommendation.

Action Requested: The Board should review the proposed regulatory text and the
attachments and consider whether they would support the proposed text as written or if
there are suggested changes to the proposed text. After review, the staff requested that
the Board consider one of the motions as set forth in the meeting materials.

Ms. Thorfinnson presented the key details of the proposed amendments as set forth in the
meeting materials in her memorandum to the Board.

Board Discussion: Dr. Lockman raised concerns about CME and the lack of available AOA
category 1A CME specific to specialties. Regulations Counsel clarified that the Board is not
addressing CME with this regulatory package and suggested that Dr. Lockman raise the
concern regarding dedicated CME and Category 1A CME issues for a possible future meeting
and agenda item.

Board Meeting Minutes – November 13, 2025

Dr. Lockman raised concerns about financial hardship for petitioners. Counsel Schieldge
explained that under this proposal, petition fees would shift the cost burden from the general
licensee population (since all costs by the Board are currently paid out of one Fund) to the
individual requesting to petition the Board.  Furthermore, the Board supported the legislation to
recover costs for petitions, so staff are simply trying to implement the policy supported by the
Board.

Dr. Lockman raised additional concerns stating that Board staff is arguing that the collection of
the adjudication fees will prevent the Board from requesting a fee increase however the Board
is already seeking a fee increase to get its fees statutorily capped out, but the Board may also
need an additional statutory fee increase down the road. The question was raised as to when
we will know how to stop asking for increases.

Counsel Schieldge indicated that the Board has never requested petition fees so the Board’s
staff are unable to determine where the Board’s budget will be if it starts collecting those
petition fees. What the Board knows now is that the Board is spending more than the Board is
bringing in and the Board currently has a structural imbalance. The goal of this proposal is to
raise all fees to current statutory caps to see if further fee increases are necessary. Executive
Director Calderon also noted that the Board has not raised fees since 1994 and that the Board
is projected to be in deficit (one month in reserve) in 2027. Ms. Thorfinnson stressed that the
Board needs to raise fees under its current authority first before asking for any further
legislative assistance to correct any continuing structural imbalance.

Mr. Cummins asked a clarifying question about the adjudication fee. He asked if the petition
costs are more than $20,000.00 what happens. Ms. Thorfinnson responded by saying that the
Board would absorb the costs. Counsel Schieldge further explained that the Board could
revaluate this cost at a later time after obtaining data showing the need for an increase, and
consider doing another rulemaking to raise the fee.

Motion – Dr. Swain Second – Mr. Cummins to:
Approve the proposed regulatory text in Attachments 1-5 including the adoption and repeal of
the forms incorporated by reference in Attachments 2-5 and to submit the text to the Director of
the Department of Consumer Affairs and the Business, Consumer Services, and Housing
Agency for review and if no adverse comments are received, authorize the Executive Director
to take all steps necessary to initiate the rulemaking process, make any non-substantive
changes to the text and the package and set the matter 

*[document truncated for length]*

---

**[MINUTES] 2025-11-13_20251113_item_8b.pdf**

Department of Consumer Affairs

Expenditure Projection Report
Osteopathic Medical Board
Reporting Structure(s): 11112600 Support
Fiscal Month: 3
Fiscal Year: 2025 - 2026
Run Date:  10/23/2025

PERSONAL SERVICES

Fiscal Code

Line Item

5100  PERMANENT POSITIONS
5100  TEMPORARY POSITIONS
5105-5108  PER DIEM, OVERTIME, & LUMP SUM
5150  STAFF BENEFITS
PERSONAL SERVICES

PY Budget
$1,180,000
$0
$3,000
$766,000
$1,949,000

PY FM13
$1,226,342  $1,207,000

Budget

$0
$68,022
$3,000
$1,800
$731,495
$773,000
$2,027,660  $1,983,000

Current Month
$101,425
$6,843
$0
$68,675
$176,943

YTD
$299,955
$7,830
$0
$195,029
$502,814

Encumbrance  YTD + Encumbrance

$0
$0
$0
$0
$0

$299,955
$6,843
$986
$195,029
$502,814

Projections to Year End
$1,211,849
$68,435
$3,986
$813,865
$2,098,135

Balance
-$4,849
-$68,435
-$986
-$40,865
-$115,135

OPERATING EXPENSES & EQUIPMENT

Fiscal Code

Line Item

5301  GENERAL EXPENSE
5302 PRINTING
5304 COMMUNICATIONS
5306 POSTAGE
53202-204  IN STATE TRAVEL
53206-208  OUT OF STATE TRAVEL
5322 TRAINING
5324  FACILITIES
53402-53403  C/P SERVICES (INTERNAL)
53404-53405  C/P SERVICES (EXTERNAL)
5342  DEPARTMENT PRORATA
5342  DEPARTMENTAL SERVICES
5344 CONSOLIDATED DATA CENTERS
5346 INFORMATION TECHNOLOGY
5362-5368  EQUIPMENT
54  SPECIAL ITEMS OF EXPENSE
OPERATING EXPENSES & EQUIPMENT

PY Budget
$127,000
$28,000
$24,000
$10,000
$22,000
$0
$9,000
$128,000
$1,094,000
$253,000
$573,000
$3,000
$15,000
$10,000
$30,000
$0
$2,326,000

Budget
PY FM13
$127,000
$28,107
$28,000
$18,708
$24,000
$1,907
$10,000
$11,337
$22,000
$28,467
$0
$2,048
$9,000
$1,000
$128,000
$76,454
$1,094,000
$844,337
$187,985
$226,000
$1,003,064  $1,002,000

$864
$1,275
$18,311
$36,507
$680

$3,000
$15,000
$10,000
$28,000
$0

$2,261,050  $2,726,000

Current Month
$0
$739
$5
$13
$4,442
$0
$0
$4,742
$63,916
$12,779
$296,943
$22
$0
$1,455
$0
$0
$385,055

YTD
$21
$739
$10
$13
$4,442
$0
$0
$14,301
$115,859
$18,035
$472,443
$22
$0
$3,255
$0
$0
$629,138

Encumbrance  YTD + Encumbrance

$11,544
$13,199
$0
$0
$0
$0
$0
$44,180
$0
$23,404
$0
$0
$0
$0
$0
$0
$92,326

$11,564
$13,938
$10
$13
$4,442
$0
$0
$58,481
$115,859
$41,439
$472,443
$22
$0
$3,255
$0
$0
$721,465

Projections to Year End
$25,953
$18,030
$2,472
$11,375
$29,000
$0
$0
$60,660
$813,688
$197,324
$1,278,673
$1,000
$1,275
$18,141
$36,507
$680
$2,494,779

Balance
$101,047
$9,970
$21,528
-$1,375
-$7,000
$0
$9,000
$67,340
$280,312
$28,676
-$276,673
$2,000
$13,725
-$8,141
-$8,507
-$680
$231,221

OVERALL TOTALS

$4,275,000

$4,288,710  $4,709,000

$561,998

$1,131,953

$92,326

$1,224,279

$4,592,914

$116,086

REIMBURSMENTS
OVERALL NET TOTALS

-$53,000
$4,222,000

-$108,000
$4,180,710  $4,656,000

-$53,000

$561,998

$1,131,953

$92,326

$1,224,279

-$53,000
$4,539,914

$116,086

ESTIMATED TOTAL NET ADJUSTMENTS
OVERALL NET TOTALS

$4,222,000

$4,180,710  $4,590,000

$561,998

$1,131,953

$92,326

$1,224,279

$4,539,914

$50,086

-$66,000

1.09%

Department of Consumer Affairs

Revenue Projection Report

Reporting Structure(s): 11112600 Support
Fiscal Month:
Fiscal Year: 2025 - 2026
Run Date:  10/23/2025

Revenue

Line Item

Fiscal Code
Delinquent Fees
Other Regulatory Fees
Other Regulatory License and Permits
Other Revenue
Renewal Fees
Revenue

Budget
$23,000
$52,000

July
$1,925
$5,150

$1,507,000  $177,414
$139,000
$2,259,000  $313,729
$3,980,000  $498,782

$564

August
$2,550
$2,175
$87,598
$25
$296,600
$388,948

September  October  November  December

Year to Date  Projection To Year End

$1,025
$1,788
$85,224
$25

$1,050
$3,125
$69,400
$40,050
$217,430  $197,700  $175,100
$305,492  $311,325  $254,875

$1,800
$3,825
$74,150
$0

$2,150
$3,800
$65,600
$0

January  February  March
$2,125
$1,750
$2,200
$6,600
$5,400
$4,700
$83,600
$74,900
$83,000  $83,400  $113,000  $135,650
$175
$46,000

$5,500
$9,113
$350,236
$614
$161,400  $177,700  $191,100  $209,000  $165,600  $208,500  $154,700
$827,759
$232,950  $305,500  $282,025  $300,725  $313,900  $331,600  $300,475  $1,193,222

April
$2,750
$7,150

June
$2,225
$7,900

May
$1,900
$8,200

$55,000

$0

$0

$0

$23,450
$59,813
$1,132,936
$141,839
$2,468,559
$3,826,597

0264 - Osteopathic Medical Board of California Fund
Analysis of Fund Condition
(Dollars in Thousands)
2025 Budget Act w/ FM 3

Column1

BEGINNING BALANCE

Prior Year Adjustment
Adjusted Beginning Balance

REVENUES, TRANSFERS AND OTHER ADJUSTMENTS

Revenues

4121200 - Delinquent fees
4127400 - Renewal fees
4129200 - Other regulatory fees
4129400 - Other regulatory licenses and permits
4163000 - Income from surplus money investments
4171400 - Escheat of unclaimed checks and warrants
4171500 - Escheat Unclaimed Property

Prepared 10.28.2025

 Actual
2024-25

CY
2025-26

BY
2026-27

 BY +1
2027-28

 BY +2
2028-29

$  5,050
$
48
$  5,098

$  4,943
$
$  4,943

-

$  3,990
$
$  3,990

-

$
$
$

3,092
-
3,092

$
$
$

1,945
-
1,945

22
$
$  2,737
$
28
$  1,096
233
$
2
$
1
$

23
$
$  2,469
$
60
$  1,133
140
$
$
2
$

-

23
$
$  2,259
$
52
$  1,507
139
$
-
$
-
$

$
$
$
$
$
$
$

23
2,259
52
1,507
29

-
-

$
$
$
$
$
$
$

23
2,259
52
1,507
9

-
-

Totals, Revenues

$  4,119  $  3,827  $  3,980  $

3,870  $

3,850

TOTALS, REVENUES, TRANSFERS AND OTHER ADJUSTMENTS

$  4,119  $  3,827  $  3,980  $

3,870  $

3,850

TOTAL RESOURCES

Expenditures:

$  9,217  $  8,770  $  7,970  $

6,962  $

5,795

1111 Department of Consumer Affairs (State Operations)
9892 Supplemental Pension Payments (State Operations)
9900 Statewide General Administrative Expenditures (Pro Rata) (State Operations)

$  4,057
12
$
205
$

$  4,502
37
$
241
$

$  4,637
$
$

-
241

$
$
$

4,776
-
241

$
$
$

4,919
-
241

TOTALS, EXPENDITURES AND EXPENDITURE ADJUSTMENTS

$  4,274  $  4,780  $  4,878  $

5,017  $

5,160

FUND BALANCE

Reserve for economic uncertainties

$  4,943  $  3,990  $  3,092  $

1,945  $

634

Months in Reserve

12.4

9.8

7.4

4.5

1.4

NOTES:
1. Assumes workload and revenue projections are realized in BY and ongoing.
2. Expenditure growth projected at 3% beginning BY.

---

**[MINUTES] 2025-11-13_20251113_item_9.pdf**

Agenda Item 9

Osteopathic Medical Board of California

DATE REPORT ISSUED:  November 13, 2025
ATTENTION:
SUBJECT:
STAFF CONTACT:

Members, Osteopathic Medical Board of California
Executive Report
Erika Calderon, Executive Director

REQUESTED ACTION:

This  report  is  intended  to  provide  the  Members  of  the  Osteopathic  Medical  Board  of
California (OMBC) with an update on personnel, and other administrative functions/projects
occurring at the OMBC.

No action is needed.

Board Member Fairwell and Appointment

The  OMBC  wishes  to  start  by  thanking  public  Board  member Andrew  Moreno  for  serving
on the Board for over 7 years. Mr. Moreno was appointed by the governor’s office on July
14, 2017, and completed his term on October 30, 2025. Mr. Moreno was a very dedicated
member having served the Board as Board secretary and most recently as vice president.
The OMBC wishes Andrew Moreno the very best in his future endeavors.

The  OMBC  is  pleased  to  announce  the  appointment  of  Board  member  Negeen
Mirreghabie,  of  La  Jolla,  who  was  appointed  to  the  OMBC  by  the  governor’s  office  on
October 30, 2025. Ms. Mirreghabie has been a Law Professor at University of San Diego
School of Law since 2017 and an Attorney and Mediator at Mirreghabie Law Group since
2011.  A  Law  Professor  at  California  Western  School  of  Law  and  The  Colleges  of  Law  in
2025. A  Law  Professor  at  Thomas  Jefferson  School  of  Law  from  2011  to  2012  and
Assistant  Director  of  Deposition,  Expert  Deposition,  and  Trial  Advocacy  Programs  at
National  Institute  for  Trial  Advocacy  from  2009  to  2011.    She  is  an  Arbitrator  and  Law
School  Council  Officer  for  the  State  Bar  of  California.  Ms.  Mirreghabie  earned  a  Juris
Doctor degree from University of San Diego School of Law and a Bachelor of Arts degree
in Political Science from University of California, San Diego.

Board Member Vacancies:

The  Board  currently  has  two  vacant  physician  member  positions.  The  OMBC  has  been
experiencing  some  challenges  in  filling  these  positions.  There  was  a  shift  with  a  new

secretary appointment at the Governors office and DCA had both of its Board and Bureau
Relations  positions  vacant  for  a  couple  of  months.  DCA  happily  announced  that  these
positions  have  since  been  filled.  Lucia  Saldivar  will  serve  as  BBR’s  Deputy  Director  and
Shelly Jones as the Assistant Deputy Director.

Before  joining  DCA,  Lucia  served  in  the  Office  of  Assemblymember  Lisa  Calderon,  most
recently  as  Chief  of  Staff  and  previously  as  Legislative  Director.  She  also  held  multiple
roles in the Office of Assembly member Jacqui Irwin, including a Legislative Assistant and
an Assembly Fellow.

Shelly  has  served  DCA  in  various  roles,  including  Staff  Services  Manager  and  most
recently  as  the  SOLID  Division  Chief.  She  was  also  a  Staff  Services  Manager  with  the
California  Department  of  Corrections  and  Rehabilitation  (CDCR)  Division  of  Juvenile
Justice and held other roles at the CDCR Juvenile Parole Board.

OMBC  welcomes our two  new  BBRs  and hope  that they  will  assist  OMBC  in  getting  our
two vacancies filled soon.

Personnel:

The OMBC continues to have 15.9 authorized positions.

OMBC is happy to announce that it has backfilled its vacant enforcement analyst position
reported at the last Board meeting. Ms. Rachel Molina joined the OMBC on September 22,
2025.  Rachel  has  over  10  years  of  experience  working  for  the  State  of  California  and
comes  to  the  OMBC  from  the  Department  of  General  Services,  Office  of  Administrative
Hearings.    Rachel  will  be  conducting  desk  investigations,  working  consumer  complaints
from intake all the way through discipline.

Update  on  Special  Investigator  (SI):  Mrs.  Yvonne  Almazan  (Natad)  joined  the  OMBC  on
September 8, 2025. Yvonne currently has over 20 pending active investigations assigned
and  is  monitoring  another  12  cases  awaiting  criminal  convictions.  Just  a  reminder  these
are assigned to Mrs. Almazan on a case-by-case basis depending on the complexity of the
allegations  and  at  any  point  the  case  can  be  transferred  to  a  sworn  investigator  to  take
over. Some examples of cases that the SI might handle are the following:

•  Subsequent arrest notifications that do not require a suspension (Penal Code

section 23 (PC23) action or interim suspension order (ISO) and DOI assistance

•  Failure to release records, recordkeeping violations, contract violations
•  False/misleading advertising – not unlicensed/not criminal
•  Continuing education violations
•  Some probation violations
•  Non-jurisdictional issues
•  General unprofessional conduct, negligence, incompetence resulting in

minor/potential harm

•  General work quality complaints, offensive behavior/conduct/speech (non-criminal)
•  Practicing with a delinquent license/not requiring an in-person undercover operation
•  Patient abandonment with no/minimal consumer harm (non-criminal, minor/potential

consumer harm, no major financial loss, minor/potential patient harm)

DOI will continue to support the Board with complaints alleging the following:

•  Practicing under the influence of drugs or alcohol, or mental or physical impairment

of the licensee

•  Unlicensed practice or practicing with a delinquent/revoked license resulting in great

bodily injury/death and/or requiring an in-person undercover operation

•  Aiding and abetting unlicensed practice resulting in great bodily injury/death and/or

requiring an in-person undercover operation

•  Acts of serious consumer harm, gross negligence, or incompetence by a licensee

resulting in great bodily injury/death

•  Obtaining licensure by selling/using fraudulent documents/transcripts
•  Felony criminal violations
•  Sexual misconduct

Please refer to the Board’s Organizational Chart.

Executive Order (N-22-25) – Return to Office

The  return  to  office  as  previously  reported  has  been  postponed  to  July  1,  2026.  Director
Calderon did identify a need to have enforcement staff return to the office at a minimum of
three days to  assist  with  the  onboarding  of  new  staff and  collaboration between  the unit.

Director Calderon has not identified a need to have anyone else come into the office more
days apart from the OMBC receptionist who is in the office every day.

State Budget/ OMBC Budget and Travel Restrictions:

OMBC is still operating under the Department of Finances issued budget letters. OMBC must
monitor overall expenses and limit out of state travel to essential operational needs. All out of
state travel requests must be approved by the governor’s office and approval will be limited to
mission critical only. Discretionary trips will not be considered this year.

In terms of OMBC’s Budget, the Board continues to work closely with DCA’s Budget office to
monitor  the  Board’s  expenditures  and  request  budget  augmentations  in  areas  where  these
have  been  needed  such  as  enforcement.  Later  today  during  our  regulation  update  you  will
hear more about Board’s staff efforts to help increase OMBC revenue through application fee
increases and the petition fees.

Board Program and Board Committee Updates:

Enforcement  Program:  The  Enforcement  program  recently  underwent  a  two-week
enforcement  academy  style  refresher  course  conducted  by  the  Executive  Director.  The
program met for two hours daily for two weeks and received extensive training on how to
handle  all  case  types and  perform  all  duties of  the  enforcement  process.  This  allows  for
cross training between staff and a refresher course of what is considered a very complex
caseload at the Board. In attendance was the Board’s Enforcement Program Manager, the
Board’s  Intake  Analyst,  the  three  Enforcement  Analysts,  the  Board’s  Probation  Monitor
and the Board’s Special Investigator.

Enforcement  staff  also  continue  to  work  extensively  with  the  Executive  Director  and  the
Department of Consumer Affairs (DCA’s) regulatory counsel to draft the language for the
Board’s  proposed  disciplinary  guidelines.  Board  staff  will  be  meeting  with  the  Board’s
Enforcement Committee in the next couple of weeks and eventually present the language
to the full Board in January of 2026.

Licensing  and  Administrative  Services  Program:  Implementation  is  under  full  force  right
now  to  establish  the  Board’s  CME  self-certification  and  audit  program.  So  far  the  Board
has  been  working  with  the  BreEze  team  to  turn  on  the  switch  of  the  self-certification
renewal  application  and  establish  our  annual  random  CME audit  list.  In addition,  the  unit
has  completed  all  audit  templates  and  had  them  approved  by  legal  counsel.  The  Board
hopes to have this process fully implemented at the next Board meeting.

Education  Committee  Update:  Board  staff  continue  to  work  with  DCA’s  communication
Team  on  its  “How  to  File  a  Consumer  Complaint”  video.  Production  of  the  video  has
started, and  we  hope  to  introduce  the  video  at  our  upcoming  Board  meeting  in  January.
Soon after the Board will be working on its application services educational video.

Legislative Committee Update: Board staff will be joining a couple of our Board members
on Hill Day which will be on January 21st , 2026. This is a milestone opportunity for the
Board to introduce OMBC to legislators, highlight the unique value of our Doctor of
Osteopathic licensees, and strengthen our voice in state policy conversations.

Communication

Director  Calderon  represents  the  prescribing  Boards  as  part  of  the  CURES  Executive
Stakeholder Committee and continues to meet regularly with DCA’s leadership staff and
the Department of Justice (DOJ).

Director Calderon had calls and email exchanges with Board President Denise Pines to
discuss pending and ongoing projects and meeting agendas.

Director Calderon continues to meet periodically with the Board’s Attorney General Liaison
Ms. Karolyn Westfall and communicates frequently with Senior Assistant Attorney General
Ms. Gloria Castro.

Director Calderon continues to meet periodically with members of the Consumer Watchdog
group to gather their input on improving enforcement practices and  procedures.

Enforcement staff continue to meet monthly with the DCA’s Division of Investigations HQIU
office to discuss progress of pending investigations.

Lastly  for  communications,  our  committee meetings  have  started, and  Board  leadership
will continue to meet frequently with our designated committee members, additionally  staff
participated  in  meetings  with  other  local,  state,  and  national organizations  in  discussing
and  deciding  regulatory  measures  common  to  OMBC  and  others.  These  organizations
include  but  are  not  limited  to;  Office  of  Attorney  General  (AGO),  Department  of  Justice
(DOJ), Department of Consumer Affairs (DCA), other healing art Boards such as (MBC,
BRN, BOP, PAC, PTBC), California Department of Public Health (CDPH), Department of
Health Care Services (DHCS), the Federation of State Medical Board (FSMB), the National
Board of Osteopathic Medical Examiners (NBOME), International Association of Medical
Regulatory  Authorities  (IAMRA),  Osteopathic  Physicians  and  Surgeons  of  California
(OPSC),  American  College  of  Osteopathic  Family  Physicians  of  California  (ACOFPCA),
and lastly Premier Health who is now handling the Board’s diversion program.

Outreach Update:

The OMBC continues to post Board content regularly on all of its social media platforms
such as Facebook, Linkedin, and X. The Board continues to keep its website current which
includes positing relevant legislation, frequently ask questions, publications, and
enfor

*[document truncated for length]*

---

**[MINUTES] 2025-11-13_20251113_item_10.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM, GOVERNOR
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov
DATE November 13, 2025
TO Board Members
Machiko Chong
FROM
Licensing Program Manager
Agenda Item #10 – Licensing Program Summary
SUBJECT
Attachments 10a & 10b
Licensing Statistics & Program Review
Attachments 10a & 10b reflect the licensing population and application stats for the
first quarter of the 2025/26 Fiscal Year. Currently, there are 17,012 licensed osteopathic
physicians and surgeons; 1,695 postgraduate training licensees (PTL); 1,369 fictitious
name permits; and no Temporary Osteopathic physician and surgeon license. With
the application process converting from paper to exclusive electronic submission in
the 2022/23 Fiscal Year, and the Board experiencing a parallel backlog as a result of
the manual keying of applicant data by Board staff. Prior fiscal year reports provided
a skewed picture of the Board’s application intake. However, with the recent
conclusion of the first quarter and the data entry of initial applications now
streamlined, we have a clearer picture of the variance between this and last fiscal
year. Overall, the Board is up 17% on total applications received. There are 269
pending initial applications, with 34 of those requesting expedited services. The
application breakdown is as follows:
Application Stats
• Postgraduate Training License (46 applications)
• Osteopathic physician and surgeon (223 applications)
Expedite Service Requests
• Medically Underserved Area (30 applications)
• Military Veteran (4 applications)
• Abortion Services (2 applications)
Over the past 2 months, the Licensing unit has worked with the BreEZe team to revise
the initial application for Fictitious Name Permits (FNP). Staff added context language
to application tabs, also known as Record Specific Data (RSDs), to clarify information

that the Board is requesting from applicants. Additional RSDs were created to ensure
that applicants understand the requirements for each of the three FNP (3) filing types,
the naming convention required for FNPs, and to explain the documents and/or
signatures that are needed. Board staff have also worked on additional BreEZe
Maintenance and Operations requests (BMOs) to cease the printing and delivery of
pocket ID cards for the Postgraduate Training License type, and update the physician
and surgeon renewal application to accommodate licensee self-certification and
the audit of Continuing Medical Education.
In October, I attended California Health Sciences University’s (CHSU) Residency Fair
in Clovis, CA. It is always a pleasure to interact with osteopathic students and educate
them on the requirements for licensure and the importance of establishing early
communication with the Board and staying in the know about items that might
impact the osteopathic medical profession.

Osteopathic Medical Boad of California
Current Licensee Population
Agenda Item 10 (A) -Application Services Stats
Stats FY 25-2026 Q1
Osteopathic Physician and Surgeon
License Status Total Licensees
Active 14,580
Delinquent/Expired 2011
Inactive 421
Total: 17,012
Postgraduate Training License (PTL)
License Status Total Licensees
Active 1,691
Delinquent/Expired 4
Inactive 0
Total: 1,695
Temporary License
License Status Total Licensees
Temp Osteopathic Physician and Surgeon 0
Temp Postgraduate Training License (PTL) 0
Total: 0
Fictitious Name Permit
License Status Total Licensees
Active 1,102
Delinquent/Expired 267
Inactive 0
Total: 1,369
Total Number of Licensees/Permit Holders 20,076

Osteopathic Medical Board of California
Application Renewal Services
Agenda Item 10(B) - Application Services Q1 Program Stats
Application Services Statistics Report
Total Applications Received
|     | FY 2024/25  |     | FY 25/26  |     |     |     |
| --- | ----------- | --- | --------- | --- | --- | --- |
Year  →  Year
|                               |     | YTD  |     | YTD  | Change  |      |
| ----------------------------- | --- | ---- | --- | ---- | ------- | ---- |
| Physician and Surgeon         |     | 438  |     | 462  |         | 5%   |
| Postgraduate Traning License  |     | 253  |     | 291  |         | 15%  |
| Fictitious Name Permits       |     | 82   |     | 150  |         | 45%  |
| Total                         |     | 773  |     | 903  |         | 17%  |
Applications Approved
|                               | FY 2024/25  |        | FY 25/26  |        | Year  →  Year  |       |
| ----------------------------- | ----------- | ------ | --------- | ------ | -------------- | ----- |
|                               |             | YTD    |           | YTD    | Change         |       |
| Physician and Surgeon         |             | 528    |           | 437    |                | -17%  |
| Postgraduate Traning License  |             | 562    |           | 617    |                | 10%   |
| Fictitious Name Permits       |             | 29     |           | 86     |                | 197%  |
| Total                         |             | 1,119  |           | 1,140  |                | 2%    |
Renewals
|                          | FY 2024/25  |        | FY 25/26  |        | Year  →  Year  |       |
| ------------------------ | ----------- | ------ | --------- | ------ | -------------- | ----- |
|                          |             | YTD    |           | YTD    | Change         |       |
| Physician and Surgeon    |             | 1,850  |           | 2,776  |                | 50%   |
| Ficticious Name Permits  |             | 132    |           | 274    |                | 108%  |

---

**[MINUTES] 2025-11-13_20251113_item_11.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR

DEPT. OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov

Briefing Paper

Agenda Item 11

Date:

October 22, 2025

Prepared for:  OMBC Members

Prepared by:

Cristy Livramento, Enforcement Program Manager

Subject:

Enforcement Program Updates

Purpose:

Update on Enforcement Program

Attachments:

11 (a) Enforcement and Probation Performance
Measures Q1, 2025/2026

Background:

This  is  a  report  on  the  updates  involving  the  Board’s  Enforcement  Unit  for  Q1,  FY
2025/2026.

Please also refer to attachment 11(a), which encompasses the Enforcement Program
statistics.

Analysis:

On September 22, 2025, the Board welcomed new Enforcement Analyst Rachel Molina.
Ms. Molina has over 10 years of experience working for the State of California, with all
10 years at the Department of General Services, Office of Administrative Hearings.  Prior
to State service, Ms. Molina was living and working in Colorado.  Since joining the OMBC,
Ms. Molina has participated in a two-week in-house enforcement training session, and
continues  to  receive  training  on  a  regular  basis.    Ms.  Molina  already  has  her  own
caseload, working cases from “cradle to grave” and has already worked cases at multiple
stages of the enforcement process.  Ms. Molina is happy to be at OMBC and is enjoying
her new assignments.  I’m so pleased to have had Ms. Molina join our unit.

In July 2025, the Board posted a limited term enforcement analyst position.  This position
has not been filled.  The Board hopes to fill this position soon.

Effective  October  1,  2025,  the  Board  was  granted  additional  citation  authority  for  all
violations  of  the  practice  act.    This  additional  authority  will  allow  the  Board  to  issue

administrative citations after enforcement review of complaints, which in the past may
have  been  closed  without  action  because  the  Board  did  not  have  authority  to  issue
citations, and the violations did not rise to the level of formal discipline.

During Q1, ten (10) complainant interviews were offered.  Eight (8) were completed, and
for the remaining two (2), the Board has not received a response from the complainant.

Board Program Statistics:

For statistics, please refer to attachment 11(a) which covers the Enforcement Program’s
Q1, fiscal year 2025/2026 in comparison to Q1, of last fiscal year, 2024/2025.

Performance  Measure  1  (PM1):  covers the amount of  consumer complaints, arrests,
and convictions received. The unit has received 320 complaints, and 7 arrest/conviction
notices.  A  significant  increase  of  33%  of  total  complaints  and  arrest/convictions  in
comparison to last year. The increase in complaints received can still be attributed to
the Board’s outreach efforts.

Performance Measure 2 (PM2): is the average number of days it takes for our analysts
to initiate complaints and acknowledge receipt. The target for this performance measure
is ten (10) days and we are at 5 days year to date.

Performance  Measure  3  (PM3):  is  the  average  number  of  days  it  takes  to  complete
investigations  and  enforcement  action  for cases  that  are  not  referred  to  the  Attorney
General’s  Office  for  formal  discipline.   Case aging here fluctuates greatly because it
takes an average of all cases, and one or two very complicated cases can skew these
numbers drastically.   These  number  include  the  timeline  for  desk  and  DOI’s  Health
Quality Investigation Unit (HQIU) investigations. The target for PM3 is 360 days.  Our
average for Q1 is at 221 days.  Although this average was higher than last fiscal year,
the Board still below the target of 360 days.   This increase can be attributed to the fact
that the unit was down one enforcement analyst, in comparison to Q1 of FY 2024/2025.

Performance  Measure  4  (PM4):  is  the  average  number  of  days  it  takes  to  complete
investigations and enforcement actions that are transmitted to the Attorney General’s
Office for formal disciplinary action. Case aging in this category is at 804 days, which is
down from 902 days for Q1, FY2024/2025.  The target for PM4 is 540 days, and although
we did not meet the target in this category, YTD, it did go down 11% in comparison to last
fiscal year.

For  FY  2025/2026,  the  Board  continues  to  be  well  under  its  performance  measure
targets for three  (3) of its performance  measures.   As  previously reported  PM4 is the
measure that unfortunately the Board has less control over as this measure takes into
consideration  the  timeline  from  the  Attorney  General’s  Office,  respondent’s  legal
representatives, and the Office of Administrative Hearings.

The  Board  currently  has  648  pending  enforcement  cases,  with  114  of  those  cases
pending at  HQIU, 21 assigned to our in-house special investigator,  and 19 of those
pending  cases  at  the  Attorney  General’s  Office.    The  remaining  494  cases  are  split

between the three enforcement analyst, with each analyst averaging 164 cases.

YTD the Board has filed one (1) accusation, issued two (2) public letters of reprimand,
placed  two  (2)  licensees  on  probation,  and  issued  one  (1)  cease  practice  order.
Additionally, two (2) probationers completed probation, and the Board issued two (2)
orders accepting the surrender of a license, and ordered two (2) revocations of license.
One (1) administrative citation has been issued as well.

Action Requested: No Action Required

---

**[MINUTES] 2025-11-13_20251113_item_11a.pdf**

Osteopathic Medical Board of CA
11 (a) Attachment
Enforcement Performance Measures Q1
Enforcement Statistics Report
Complaints
|     |     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Year → Year
|                                    |     |      |      |            | Q1   | Q2  Q3                  | Q4          |     |      |         |      |
| ---------------------------------- | --- | ---- | ---- | ---------- | ---- | ----------------------- | ----------- | --- | ---- | ------- | ---- |
|                                    |     | YTD  |      |            |      |                         |             |     | YTD  | Change  |      |
|                                    |     |      |      | Jul - Sep  |      | Oct  - Dec  Jan  - Mar  | Apr  - Jun  |     |      |         |      |
| PM1:  Complaints Received          |     |      | 241  |            | 320  |                         |             |     | 320  |         | 33%  |
| PM1:  Convictions/Arrest Received  |     |      | 5    |            | 7    |                         |             |     | 7    |         | 40%  |
| PM1:  Total Received               |     |      | 246  |            | 327  | 0                       | 0           | 0   | 327  |         | 33%  |
Complaint Intake
|     |     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Year → Year
Target:  10 Days
|                         |     |      |     |            | Q1  | Q2  Q3                  | Q4          |     |      | Change  |     |
| ----------------------- | --- | ---- | --- | ---------- | --- | ----------------------- | ----------- | --- | ---- | ------- | --- |
|                         |     | YTD  |     |            |     |                         |             |     | YTD  |         |     |
|                         |     |      |     | Jul - Sep  |     | Oct  - Dec  Jan  - Mar  | Apr  - Jun  |     |      |         |     |
| PM2:  Intake/Avg. Days  |     |      | 5   |            | 5   |                         |             |     | 5    |         | 0%  |
Investigations
|     |     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Year → Year
|                                 | Target: 360 Days  |      |      |            | Q1   | Q2  Q3                  | Q4          |     |      |         |       |
| ------------------------------- | ----------------- | ---- | ---- | ---------- | ---- | ----------------------- | ----------- | --- | ---- | ------- | ----- |
|                                 |                   | YTD  |      |            |      |                         |             |     | YTD  | Change  |       |
|                                 |                   |      |      | Jul - Sep  |      | Oct  - Dec  Jan  - Mar  | Apr  - Jun  |     |      |         |       |
| PM3: Volume                     |                   |      | 212  |            | 315  |                         |             |     | 315  |         | 49%   |
| PM3a:  Intake Only              |                   |      | 3    |            | 5    |                         |             |     | 5    |         | 67%   |
| PM3b:  Investigation Only       |                   |      | 159  |            | 221  |                         |             |     | 221  |         | 39%   |
| PM3c:  Post Investigation Only  |                   |      | 3    |            | 2    |                         |             |     | 2    |         | -33%  |
| PM3:  Cycle Time-Investigation  |                   |      | 165  |            | 228  |                         |             |     | 228  |         | 38%   |
| ***Pending Cases at HQIU        |                   |      | 69   |            | 114  |                         |             |     | 69   |         |       |
Transmittals to Attorney General (AG)
|     |     | FY 24/25  |     |     |     | Fiscal Year 25/26  |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Year → Year
Target:  540 Days
|                             |     |      |      |            | Q1   | Q2  Q3                  | Q4          |     |      |         |       |
| --------------------------- | --- | ---- | ---- | ---------- | ---- | ----------------------- | ----------- | --- | ---- | ------- | ----- |
|                             |     | YTD  |      |            |      |                         |             |     | YTD  | Change  |       |
|                             |     |      |      | Jul - Sep  |      | Oct  - Dec  Jan  - Mar  | Apr  - Jun  |     |      |         |       |
| PM4: Volume                 |     |      | 4    |            | 8    |                         |             |     | 8    |         | 100%  |
| PM4a: Intake Only           |     |      | 11   |            | 7    |                         |             |     | 7    |         | -36%  |
| PM4b:  Investigation Only   |     |      | 557  |            | 460  |                         |             |     | 460  |         | -17%  |
| PM4c:  Pre-AG Transmittal   |     |      | 16   |            | 1    |                         |             |     | 1    |         | -94%  |
| PM4d:  Post-AG Transmittal  |     |      | 319  |            | 390  |                         |             |     | 390  |         | 22%   |
| PM4: Cycle Time-AG          |     |      | 902  |            | 804  |                         |             |     | 804  |         | -11%  |
| ***Pending Cases at AGO     |     |      | 20   |            | 19   |                         |             |     | 20   |         | 0%    |

Osteopathic Medical Board of CA
11 (a) Attachment
Enforcement Performance Measures Q1
Other Legal Actions
Fiscal Year 25/26
|                                 | FY 24/25  |     |            |                         |             |      | Year → Year  |     |
| ------------------------------- | --------- | --- | ---------- | ----------------------- | ----------- | ---- | ------------ | --- |
|                                 |           |     | Q1         | Q2  Q3                  | Q4          |      |              |     |
|                                 | YTD       |     |            |                         |             | YTD  | Change       |     |
|                                 |           |     | Jul - Sep  | Oct  - Dec  Jan  - Mar  | Apr  - Jun  |      |              |     |
| PC 23 Ordered                   |           | 0   |            | 0                       |             | 0    |              | 0%  |
| ISO-Interim Suspension Order    |           | 0   |            | 0                       |             | 0    |              | 0%  |
| ASO-Automatic Suspension Order  |           | 0   |            | 0                       |             | 0    |              | 0%  |
Actions
Fiscal Year 25/26
|                                        | FY 24/25  |     |            |                         |             |      | Year → Year  |       |
| -------------------------------------- | --------- | --- | ---------- | ----------------------- | ----------- | ---- | ------------ | ----- |
|                                        |           |     | Q1         | Q2  Q3                  | Q4          |      |              |       |
|                                        | YTD       |     |            |                         |             | YTD  | Change       |       |
|                                        |           |     | Jul - Sep  | Oct  - Dec  Jan  - Mar  | Apr  - Jun  |      |              |       |
| Accusations/Amended Accusations Filed  |           | 1   |            | 1                       |             | 1    |              | 0%    |
| Accusation and Petition to Revoke      |           | 0   |            | 0                       |             | 0    |              | 0%    |
| Citations                              |           | 1   |            | 1                       |             | 1    |              | 0%    |
| PR/PLR                                 |           | 0   |            | 2                       |             | 2    |              | 100%  |
| Probation                              |           | 2   |            | 2                       |             | 2    |              | 0%    |
| Surrender                              |           | 0   |            | 2                       |             | 2    |              | 100%  |
| Revocation                             |           | 0   |            | 2                       |             | 2    |              | 100%  |
PM1: Complaint Intake- Complaints and Convictions Received
PM2: Cycle Time -Intake - Average number of days from the date the complaint was received to the date the complaint was closed or
assigned for investigation (assigned to staff).
PM3: Cycle Time -Investigations  - Average number of days to complete the entire enforcement process for complaints not transmitted to
the AG for formal discipline.  (includes intake and investigation days)
PM3a: Intake Only -Of the cases included in PM3, the average number of days from the date the complaint was received to the date the
complaint was assigned for investigation.
PM3b: Investigation Only -Of the cases included in PM3, the average number of days from the date the complaint was assigned for
investigation to the date the investigation was completed.  (without intake)
PM3c: Post Investigation Only -Of the cases included in PM3, the average number of days from the date the investigation was completed
to the date of the case outcome or non-AG formal discipline effective date.
PM4:Cycle Time-AG Transmittal -Average number of days to complete the enforcement process for cases investigated and transmitted to
the AG for formal discipline. (includes intake & investigation to final outcome of cases transmitted to the AG -includes withdraws, dismissals,
etc.)
PM4a: AG Transmittal - Intake Only -Of the cases included in PM4, the average number of days from the date the complaint was received
to the date the complaint was assigned for investigation.
PM4b: AG Transmittal - Investigation Only -Of the cases in PM4, the average number of days from the date the complaint was assigned
for investigation to the date the investigation was completed.
PM4c: AG Transmittal - Pre AG Transmittal - Of the cases in PM4, the average number of days from the date the investigation was
completed to the date the case was transmitted to the AG.
PM4d: AG Transmittal - Post AG Transmittal - Of the cases in PM4, the average number of days from the date the case is transmitted to
the AG to the date of the case outcome or formal discipline effective date.  (AG days only)

---

**[MINUTES] 2025-11-13_20251113_item_12.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPT. OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov

Briefing Paper

Agenda Item 12

Date:

October 29, 2025

Prepared for:  OMBC Members

Prepared by:

Ralph Correa, Probation Monitor

Subject:

Probation Unit Updates

Purpose:

Update on Probation Program Updates
Q1- FY 2025-2026

Attachments:       None

Background:

This is a report on the Board’s Probation Program for the first quarter of FY 2025-2026.

   Analysis:

Probation Program Updates:

The Board has thirty-one (31) current probationers who have been placed on probation
for  various  causes.  Of  the  31  probationers,  five  (5)  are  tolling  out  of  state  and  not
receiving credit towards the completion of probation.

Of  the  31  licensees  on  probation,  four  (4)  are  participating  in  the  Board’s  Diversion
Program.    In  addition to  the  four  Board  referrals  the diversion program  has three  (3)
other licensees participating in their program as self-referrals.

In this first quarter the Board referred a probationer to the Attorney General’s Office and
requested  a  new  Accusation  and  Petition  to  Revoke  Probation  to  be  filed.  This
probationer was placed on probation here in CA but has been tolling for several years.
Most  recently,  the  state  where  they  reside  took  disciplinary  action  against  them  for
similar  reasons  why  they  had  been  placed on  probation here  in  CA.  As  soon  as this
Board received notice of the out of state discipline, the Board took the necessary action
to refer the matter to the Attorney Generals Office.

In addition to monitoring the probationers, the Probation Program has been assisting
the Executive Director with drafting of the proposed language for the Board’s disciplinary
guidelines  and  the  regulatory  language  for  the  penalty  relief  fees  which  you  will  be
hearing about later today.

Action Requested: No Action Required

---

**[MINUTES] 2025-11-13_20251113_item_13.pdf**

DEPARTMENT OF CONSUMER AFFAIRS BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM GOVERNOR
OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
(916) 928-8390 | F (916) 928-8392 www.ombc.ca.gov
DATE November 13, 2025
TO OMBC Board Members, Osteopathic Medical Board of California
Terri Thorfinnson, J.D.
FROM
Legislative and Regulatory Specialist
Agenda Item 13 -- Rulemaking Update – 2025 Rulemaking for Pending or
RE:
Proposed Regulations
Rulemaking Update Summary
The CME/Audit and Cite and Fine package that was approved by the Office of Administrative Law (OAL) July
10, 2025 became effective October 1, 2025. This rulemaking package is completed.
The Board has two additional regulatory packages moving along in the rulemaking process. The Fees and
License Status rulemaking documents are still pending review within DCA. This rulemaking package is being
considered at this meeting to approve revised, stripped-down language that focuses on the fees and not
updating the various regulatory sections that need updating. The updating has proven more complex and
is holding up simply updating the fees from moving through the process. This version has removed the draft
regulatory section updates and focuses on the fees and new items with fees and applications.
After the Board reviews and approves this revised proposed language, it still needs Budgets, and the
Regulatory Attorney staff must sign-off and then it goes to the DCA Director for review and approval. The
Board must receive approval from DCA and Agency before it can be submitted to OAL for post for 45-day
comment period.
The Disciplinary Guidelines are in the initial stages. Preliminary draft of the proposed language was
reviewed by Regulatory Counsel and that draft is being reviewed and further revised. OMBC staff has been
working closely with the Regulatory Attorney to revise and finalize the proposed language. This process has
taken longer than expected and is continuing. The Board staff is trying to anticipate as many of the changes
needed upfront before the Enforcement Committee and Board review it. It is anticipated that more input
and revisions will be made over the next two months in preparation for the Board to review in the January
board meeting in 2026. This is another large rulemaking package that is complex because it is creating a
new Disciplinary Guidelines document that has not been amended since 1996.

Rulemaking Status: Fees and License Status

Concept/  DCA pre-review   Board  Draft  DCA   Agency  DOF   Filing
| Draft      |     | approval  |             |            |            |            |               |
| ---------- | --- | --------- | ----------- | ---------- | ---------- | ---------- | ------------- |
|            |     |           | Regulatory  | Director   | Approval   | Approval   | regulatory    |
| language   |     | of        |             |            |            |            |               |
|            |     |           | documents/  | Approval   |            |            | package with  |
Language
|     |     |     | review   |     |     |     | OAL   |
| --- | --- | --- | -------- | --- | --- | --- | ----- |
1/1/2024   2/1/24,2/15/24   8/15/2024,  8/16/2024,
2/28/24, 4/12/24,
|     |                   | November   | 7/8/2025,  |     |     |     |     |
| --- | ----------------- | ---------- | ---------- | --- | --- | --- | --- |
|     | 4/12/24,5/9/24,   | 13, 2025   |            |     |     |     |     |
budget
|     | 6/5/24,7/10/24,    |     | approval  |     |     |     |     |
| --- | ------------------ | --- | --------- | --- | --- | --- | --- |
|     | 7/22/24, 7/26/24   |     | pending   |     |     |     |     |
45-day  Board Respond  Final  Submit to  OAL  Effective
comment   to comments  review  DCA Director,  approval  Date
| period   |     | with         | OAL for    | or denial   |     |     |     |
| -------- | --- | ------------ | ---------- | ----------- | --- | --- | --- |
|          |     | Regulatory   | approval   |             |     |     |     |
Attorney
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Rulemaking Status: Disciplinary Guidelines

Concept/  DCA pre-review  Board  Draft  DCA   Agency  DOF   Filing
Draft
approval  Regulatory  Director   Approval  Approval  regulatory
| language  |     | of   |             |           |     |     |          |
| --------- | --- | ---- | ----------- | --------- | --- | --- | -------- |
|           |     |      | documents/  | Approval  |     |     | package  |
Language
|            |           |     | review  |     |     |     | with OAL  |
| ---------- | --------- | --- | ------- | --- | --- | --- | --------- |
| 1/31/2020  | 9/19/23,  |     |         |     |     |     |           |
10/9/23,
11/16/23,
3/8/24,
4/16/24,
pending
| 45-day    | Board       | Final   | Submit to  | OAL        | Effective    |     |     |
| --------- | ----------- | ------- | ---------- | ---------- | ------------ | --- | --- |
| comment   | Respond to  | review  | DCA        | approval   | Date         |     |     |
| period    |             | with    |            |            |              |     |     |
|           | comments    |         | Director,  | or denial  |              |     |     |
Regulatory
OAL for
Attorney
approval
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

---

**[MINUTES] 2025-11-13_20251113_item_14.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM, GOVERNOR
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
DATE November 13, 2025
TO Board Members, Osteopathic Medical Board of California
Terri Thorfinnson, J.D.
FROM
Legislative and Regulatory Specialist
Agenda Item 14 -- Discussion and Possible Action to Consider Initiation of a Rulemaking to
Amend Sections 1630, 1636, 1646, 1647, 1656, 1658, and 1690, and to Adopt Section
RE:
1648 in Division 16 of Title 16 of the California Code of Regulations (CCR) (Retired License,
Petitions and Fees)
Overview of Proposed Revisions to Rulemaking Text
The Board approved proposed language related to items in this rulemaking at the August 14, 2025, Board
meeting. Since that meeting, the Board’s Regulations Counsel and staff identified more issues that would
need to be addressed in the proposal, which would further delay the rulemaking. The original focus of the
rulemaking was fee increases—specifically to raise fees to the statutory maximums authorized by law.
However, along the way, we became perhaps overly zealous in adding various updates to the package
which in hindsight was overly ambitious and diverted the attention from the fees and priority of the
increase of these fees. The Board’s Executive Director does not want further delays to this critical fee
rulemaking and recommends removing amendments that did not otherwise relate to fee increases or
address the Board’s long-standing goal of establishing a retired license. This proposed language is the result
of that recommendation.
The timing for this rulemaking was to be completed in time for the Board’s next joint sunset review
oversight and hearing before the California Legislature, a process which begins next year . The Board must
prepare the Oversight Report during the summer of 2026 for submission in December 2026 with hearings
to be scheduled around March 2027. The Board must approve the Oversight Report prior to submission to
the Legislature.
The Board plans to request fee increases as part of the Board’s Oversight Report so having this rulemaking
package moving forward is critical to that timing. As a reminder, historically, boards are not successful in
requesting fee increases from the Legislature if their current fees are not currently set at the statutory
maximums authorized by law. The Board does need fee increases to bring the Board’s budget into alignment-
-so fees generate enough revenue to cover expenditures for a sustainable balanced budget. Consistent with
this objective, the staff and Regulations Counsel recommend the Board consider making the text and form
changes set forth in Attachments 1-5. The remainder of the licensing updates discussed at prior meetings
1

would be addressed in a future package anticipated to be brought back to the Board for consideration next
year.
Summary of Revised Amendments
Article 8. Active Practice Requirements
§ 1630. Good Standing Requirements.
This is the section that details the requirements for renewal and remaining in “good standing.” The Board is
proposing to repeal the outdated OMB.2 and OMB.2a (Rev. 11/94) renewal form cited in CCR section 1646
and propose new language that details the requirements for the renewal application. The underlined
language in CCR section 1630 is the content of the new proposed renewal application language for
applicants seeking to renew their license as active. This proposed language not only replaces the repealed
forms referenced in CCR section 1646, but it updates the Board’s current renewal requirements consistent
with statutory and other program changes that have been enacted since the renewal requirements were
last formally updated.
Clarifying wording is added to indicate applicants are only eligible for renewal in active status if they apply
for renewal “on or before the expiration date of their license or within five (5) years after the expiration
date of their license,” submit a completed application as set forth in this section, submit satisfactory
documentation of compliance with CME Rules and pay any applicable renewal fees. Further clarifying
language is added to indicate that that requirements in this section only apply to those renewing their
license in “active” status. CCR Section 1646 provides the requirements for renewing in an “inactive” status
and restoring the license to “active” status (see below).
Article 9. Continuing Medical Education
§ 1636. Continuing Medical Education Documentation.
This is the newly implemented continuing medical education (CME) section that became effective October
1, 2025. The minor amendments to this section clarify that this section only applies to applicants applying
for renewal in “active” status as distinguished from “inactive,” which are not required to complete CMEs. It
also adds clarifying language to cross-reference to the renewal requirements in CCR section 1630. There are
no further proposed amendments to this section.
Article 10. Inactive Practice and Retired Licenses
§ 1646. Procedure for Obtaining an Inactive Certificate or for Restoration to Active Status.
One of the key changes to this section is repealing the outdated OMB.2 and OMB.2a (Rev. 11/94) form
which was the renewal form that also included provisions for renewing both “active” and “inactive” status.
This section’s amendments add new language that details the requirements for applicants seeking to renew
2

their license in an inactive status. While much of the underlined language mirrors language amended into
above CCR section 1630, it differs with respect to the fact that licensees with inactive status licenses are
prohibited from practicing medicine and there is no continuing medical education requirement for those
applying for an inactive license. This proposed language not only replaces the repealed form, but it updates
the Board’s inactive renewal requirements consistent with statutory and other program changes occurring
since the renewal requirements were last formally updated.
A minor amendment is to delete “practice” from the title because inactive certificates do not authorize any
“practice” of medicine so that current title is misleading.
§ 1647. Inactive Certificate Issuance, Renewal and Fees.
This section provides additional requirements for inactive license status renewal but also details
requirements for fees and the deadlines for renewal. You will note that this section cross- references to CCR
section 1646 that provides the inactive renewal application requirements. The important amendments
include adding that the application fee is non-refundable and includes the “delinquent inactive certificate
renewal fee” (proposed to be added to CCR section 1690) for failure to renew the license prior to its
expiration. This section clarifies that the fee for an inactive renewal fee is set in CCR section 1690.
Additionally, there is a separate fee amount for delinquent inactive certificates set forth in section 1690.
Both of those fee amounts were approved by the Board at the August meeting; no change to those fee
amounts is proposed here.
This section also specifies the deadline for the license expiration that mirrors the language related to the
license expiration timeframes discussed above in CCR section 1630. This language is necessary to
distinguish between those licensees who are currently able to renew their license in an inactive status from
those who are not eligible (those licenses who have not been renewed for 5 years).
§ 1648. Retired License Status.
The proposed language in this section is similar to what the Board approved at the August meeting. There
are minor changes to the new forms OMB. 31 and OMB.32 which are proposed regulatory language to be
incorporated by reference. In addition, cross-references to the Board’s new fingerprinting authority in
Business and Professions Code (BPC) section 2042 have been added at subsection (f)(4) and the Note.
Article 12. Substantial Relationship and Rehabilitation Criteria; Petitions for Modification of Penalty or
Reinstatement
§ 1656. Petition for Reinstatement or Modification of Penalty.
3

There are new amendments to this section. The staff recommended a change in timeframe for petitions to
be filed prior to any Board meeting to increase review time to 120 days (currently set at 30 days) -- citing
insufficient time for the staff to gather the required documents and follow-up on additional documents.
There is clarifying language requirements that “at least” two verified recommendations are required to
subsection (c) (1). Subsection (c) has been expanded to include new subsections (2) (A) – (E) and additional
subsections (d), (e), (f), (g) that specify the requirements for completing fingerprinting (if seeking
reinstatement), paying required application and adjudication fees, the methods of paying such fees,
receiving a written notice of approval of petition, and specifying the “reasonable costs” required to be paid
to adjudicate a petition. There are also amendments to the OMB.7 form that include the regulatory
requirements for petitioning for reinstatement or modification of penalty or early termination of probation
and additional instructions to ensure that petitioners are fully notified of all fee and qualifying
requirements prior to submitting a petition.
Also new is the addition of an adjudication fee to be charged once the Board has accepted the petition
application as complete. BPC section 2307.5 (enacted by Senate Bill 815 -- Stats. 2023, Ch. 294) authorizes
the Board to “establish a fee to be paid by a person seeking a license reinstatement or modification of
penalty pursuant to Section 2307; and “(b) [t]he fee established shall not exceed the Board’s reasonable
costs to process and adjudicate a petition.”
The prior draft from August only covered the staff costs to process a petition, but staff forgot to add in the
Board’s other adjudicative costs that the Board incurs from the Attorney General’s Office and the Office of
Administrative Hearings, including costs for the Administrative Law Judge and court reporter(s). This fee
would be charged upfront once the petition application (Form OMB.7) is approved.
The fee is proposed to be set at $20,000, which is the current average cost (calculated as provided in
Attachment 6(H)) for a petition hearing within the last two years. Under this proposal, the Board would be
required to provide each petitioner (within 120 days of their hearing) with an itemized fee payment
statement detailing the reasonable costs (as defined, see p. 14, subsection (f)(2)) in adjudicating their
petition. If the costs incurred by the Board are less than initially required to be paid to adjudicate the
petition, the Board would be required to provide the petitioner a statement detailing the refund that will
be provided and the anticipated date when the refund will be issued.
§ 1658. Petitions for Reinstatement of Certificates Restricted or Revoked Due to Mental or Physical
Illness.
There are new amendments to this section that mirror new amendments to CCR section 1656 as noted
above.
Article 17. Fees
§ 1690. Fees.
4

The amendments to this section include removing the wording “nonrefundable” fees. The “nonrefundable
fees” are noted as such in the individual sections that provide for the renewal and various applications for
retired license status and for petitions that you have already reviewed. Other amendments include adding
clarifying wording that distinguishes “active” from “inactive” license fees including “active” and “inactive”
delinquent certificate fees. This proposal would add two new subsections (n) and (o) that specify the “final
fee” required to adjudicate a petition for reinstatement or modification of penalty, including how the Board
would prepare the itemized invoice and calculate the “final fee” to adjudicate a petition, and the process

*[document truncated for length]*

---

**[MINUTES] 2025-11-13_20251113_item_15.pdf**

Osteopathic Medical Board of California
Agenda Item #15   End of Session Legislative Update November 2025
Bills With Board Positions
| Bill No.  | Author  | Subject                     | Status          | Position  |
| --------- | ------- | --------------------------- | --------------- | --------- |
| AB 54     | Krell   | Access Safe Abortions Act:  | Ordered         | Support   |
|           |         | Protects Medical Abortions  | Inactive file.  |           |
and prohibits criminal and
civil penalties related to
providing abortion.
AB 260  Aguiar-Curry  Sexual and Reproductive  Signed  Support
|     |     | Health Care. Makes changes  | 9.26.2025,   |     |
| --- | --- | --------------------------- | ------------ | --- |
|     |     | that protect reproductive   | Chapter 136  |     |
health care services.
| AB 360  | Papan  | Menopause Survey.  | Held Under  | Support  |
| ------- | ------ | ------------------ | ----------- | -------- |
Submission- 2-
year bill
| AB 432  | Bauer-Kahan  | Mandatory CME:           | Vetoed      | Support  |
| ------- | ------------ | ------------------------ | ----------- | -------- |
|         |              | Menopause and Insurance  | 10.13.2025  |          |
Coverage for menopause
treatment.
| AB 742  | Elhawary  | Expedite License  | Vetoed      | Support  |
| ------- | --------- | ----------------- | ----------- | -------- |
|         |           | Applications for  | 10.13.2025  |          |
Descendants of Slaves.
| AB 489  | Bonta  | AI: Health Care               | Signed.      | Support  |
| ------- | ------ | ----------------------------- | ------------ | -------- |
|         |        | Professionals: deceptive      | 10.11.2025   |          |
|         |        | terms or letters and posting  | Chapter 615  |          |
as professionals
AB 667  Solache  Interpreters paid by Board:  Ordered to  Oppose Unless
|     |     | Exams and Application.  | Inactive file  | Amended  |
| --- | --- | ----------------------- | -------------- | -------- |
Note: no longer applies to
OMBC.
| AB 876  | Flora  | Nurse Anesthetists Scope of  | Signed.    | Oppose  |
| ------- | ------ | ---------------------------- | ---------- | ------- |
|         |        | Practice Expansion.          | 10.1.2025  |         |
Chapter 169
AB 1215  Flora  Hospital Membership: Peer  2-year bill  Oppose
|     |     | Review, Assessment  | Assembly  |     |
| --- | --- | ------------------- | --------- | --- |
Business and
1

|     |     | Expansion of Non- | Professions  |     |
| --- | --- | ----------------- | ------------ | --- |
|     |     | Physicians.       | Committee    |     |
SB 508  Valladares  Telemedicine License  Amended—no  Oppose
|         |        | Exemption Expansion         | longer relevant  |          |
| ------- | ------ | --------------------------- | ---------------- | -------- |
|         | Ashby  | States of Emergency:        | Vetoed. In       | Support  |
| SB 641  |        | Waivers and Exemptions:     | Senate           |          |
|         |        | Delegation of Authority to  | Considering      |          |
|         |        | Boards.                     | Veto             |          |
10.13.2025
| AB 460  | Chen  | Radiologic Technologists:  | Signed.      | Oppose  |
| ------- | ----- | -------------------------- | ------------ | ------- |
|         |       | direct supervision:        | 10.7.2025    |         |
|         |       | telemedicine               | Chapter 435  |         |
AB 967  Valencia  Physicians and Surgeons:  2-year bill  Oppose
Licensure: Expedited Fee.

WATCH LIST BILLS
| AB 50  | Bonta  | Pharmacists: Furnishing  | Signed.    | Watch  |
| ------ | ------ | ------------------------ | ---------- | ------ |
|        |        | Contraceptives           | 9.26.2025  |        |
Chapter 135
AB 346  Nguyen  In-Home Support Services:  Held Under  Watch
|     |     | Licensed Health Care         | Submission.   |     |
| --- | --- | ---------------------------- | ------------- | --- |
|     |     | Professionals Certification  |               |     |
AB 408  Berman  Physician Health and  Senate Judiciary  Watch
|         |           | Wellness Program (MBC  | Committee   |        |
| ------- | --------- | ---------------------- | ----------- | ------ |
|         |           | sponsored)             | 2 yr. bill  |        |
| AB 447  | Gonzalez  | Emergency Room (ER)    | Signed.     | Watch  |
|         |           | Patient Prescriptions  | 10.6.2025   |        |
Chapter 363
AB 479  Tangipa  Criminal Procedure: Vacatur  2-year bill  Watch
Relief: Findings of Harm.
| AB 485  | Ortega  | Labor Commissioner:     | Held Under  | Watch  |
| ------- | ------- | ----------------------- | ----------- | ------ |
|         |         | Unsatisfied Judgments:  | Submission  |        |
Nonpayment of Wages.

AB 511  Chen  Radiologist Assistants: Scope  Held Under  Watch
|         |          | of Practice: Supervision.  | Submission  |        |
| ------- | -------- | -------------------------- | ----------- | ------ |
| SB 679  | Weber-   | Requires Health            | Held Under  | Watch  |
|         | Pierson  | Facilities/Peer Review     | Submission  |        |
Committees 805 Reporting
to Include Race and Gender.
2

| AB 1037  | Elhawary  | Public Health: Overdose  | Signed.      | Watch  |
| -------- | --------- | ------------------------ | ------------ | ------ |
|          |           | Treatment by Non-        | 10.10.2025   |        |
|          |           | Physicians.              | Chapter 569  |        |
AB 1186  Patel  Data Collection: Race and  Held Under  Watch
|     |     | Ethnicity: Minimum Data  | Submission.  |     |
| --- | --- | ------------------------ | ------------ | --- |
Categories.
AB 1501  Berman  P.A. Scope of Practice: Direct  Signed.  Watch
|         |        | Supervision by Physician      | 10.1.2025    |        |
| ------- | ------ | ----------------------------- | ------------ | ------ |
|         |        | from 4 to 8 P.A.s.            | chapter 194  |        |
| SB 387  | Rubio  | Residency Accreditation       | Signed.      | Watch  |
|         |        | Eligibility: Faculty Permit.  | 10.13.2025   |        |
Chapter 752
| SB 470  | Laird    | Bagley-Keene Open              | Signed.      | Watch  |
| ------- | -------- | ------------------------------ | ------------ | ------ |
|         |          | Meetings Act: Extending        | 10.1.2025    |        |
|         |          | Hybrid Teleconferencing.       | Chapter 222  |        |
| SB 518  | Weber-   | Descendants of Enslaved        | Signed.      | Watch  |
|         | Pierson  | Persons: Reparations:          | 10.10.2025   |        |
|         |          | Certification of Descendants.  | Chapter 586  |        |

3

---

### 2025-08-14 — Osteopathic Medical Board of California — August 14, 2025

**[AGENDA] 2025-08-14_20250814_agenda.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 |F (916) 928-8392 | www.ombc.ca.gov

MEMBERS OF THE BOARD
President
Denise Pines, MBA Vice
President
Hemesh Patel, D.O.
Secretary
Gor Adamyan

John M. Cummins, J.D.
Andrew Moreno, Esq.
Brett Lockman, D.O. Matthew
Swain, D.O.

 QUARTERLY BOARD MEETING AGENDA

Touro University College of Osteopathic
Medicine – Mare Island

1310 Club Drive
Farragut Inn
Vallejo, CA 94592
(916) 928-8390 Office Main Line

Thursday, August 14, 2025
9:00 a.m. – 5:00 p.m.
(or until the conclusion of business)

Public WebEx/Telephone Access – See Attached
Meeting Information

MEETING TIMES AND ORDER OF AGENDA ITEMS ARE
SUBJECT TO CHANGE

Action may be taken on
any item listed on the
agenda

While the Board intends to
webcast this meeting, it
may not be possible to
webcast the entire open
meeting due to limitation
on resources or technical
difficulties.

Please see Meeting
Information section for
additional information on
public participation.

The Osteopathic Medical Board of California (Board) will meet via teleconference
in accordance with Government Code section 11123.2 with in-person participation
accessible at the above listed public location.

  OPEN SESSION

1.

2.

3.

4.

5.

Call to Order/Roll Call/ Establishment of a Quorum- Machiko Chong, Licensing
Program Manager

Reading of the Board’s Mission Statement– Erika Calderon, Executive Director

Public Comment on Items Not on the Agenda -Denise Pines, MBA The Board
may  not  discuss  or  take  action  on  any  matter  raised  during  this  public
comment  section  except  to  decide  whether  to  place  the  matter  on  the
agenda of a future meeting. (Government Code sections 11125, 11125.7(a).)

Petition for Early Termination of Probation, Steven D. Western, DO (20A 7125)

Petition for Early Termination of Probation, James M. Lally, DO (20A 6259)

      CLOSED SESSION/LUNCH

A.  Deliberation on disciplinary matters, including petitions, proposed

decision, non-adopt proposed decisions, and stipulations (Government
Code section 11126 (c)(3).)

    RECONVENE IN OPEN SESSION

6.

7.

8.

9.

Osteopathic Physician and Surgeon Student Question and Answer Forum

Review  and  Possible  Approval  of  Board  Meeting  Minutes  -  Beth  Clark,
Associate Governmental Program Analyst

A.   May 15, 2025, Board Meeting Minutes

President’s Report- Denise Pines, MBA

Board Member Communications with Interested Parties-   Denise Pines, MBA

10.

Intergovernmental Relations Reports and Administrative Services Update

A.  DCA Update – Shelly Jones, Staff Services Manager II, SOLID, DCA
B.  Budget Update  –  Kaila  Van  Lindt  and  Harmony  DiFilippo,  Budget  Office,

DCA

11.

12.

13.

14.

Executive Director’s Report- Erika Calderon, Executive Director
Administrative  Services  Including  (administrative  services,  personnel,  and
technology updates)

Licensing/Admin  Program  Summary,  including  licensing  unit  updates,  and
statistics- Machiko Chong, Licensing Program Manager

Enforcement  Program  Summary,  including  enforcement  unit  updates,  and
statistics- Cristy Livramento, Enforcement Program Manager

Probation Program Summary, including probation unit updates and statistics-
Ralph Correa, Probation Monitor

    BREAK AND RECONVENE IN OPEN SESSION

15.

Rulemaking  Update-Rulemaking  for  Pending  or  Proposed  Regulations-Terri
Thorfinnson, Legislative and Regulatory Specialist

16.  Discussion and Possible Action to Reconsider Previously Approved Text, and to
consider initiation of a Rulemaking to Amend  Sections 1609, 1610; 1611, 1612,
1613, 1615, 1628, 1630, 1637, 1646, 1647, 1650, 1651, 1656, 1658, 1678,and 1690,
and to adopt Section 1648, and to repeal Section 1691 in Division 16 of Title 16
of  the  California  Code  of  Regulations  (Applications,  Petitions,  Fees,  Retired
License  and  Processing  Times)  -  Terri  Thorfinnson,  Legislative  and  Regulatory
Specialist and Kristy Schieldge, Attorney IV, Legal Affairs Regulations Unit, DCA

17.

Legislative Report – Terri Thorfinnson, Legislative and Regulatory Specialist

A.  Discussion and Possible Action on Legislation

•  AB 54 Keep Abortion Pill Safe

•  AB 260 Sexual and Reproductive Freedom

•  AB 360 Menopause Survey

•  AB 432 Mandatory CME: Menopause: Treatment

•  AB 742 License Application Expedite: Descendants of Slaves

•  AB  489  Prohibition  of  AI:  Deception  use:  posing  as

licensed

professionals

•  AB  667  Board  Paid

Interpreters  for  State  Exams  and  License

Applications

•  AB 876 Nurse Anesthetists; Expansion of Scope of Practice

•  AB 1215 Hospital Membership: Non-physician expansion.

•  SB 508 License Exemption for Out of State Telemedicine Physicians

•  SB 641 State of Emergency: Board Authority to waiver or exempt

•  AB 460 Radiologic Technologists: Telemedicine    Supervision: Scope

of Practice

•  AB 967 Expedited Processing Fee

B.  2025 Informational Bill “Watch” List

•  AB 50 Pharmacies furnishing contraception

•  AB 346 Home Health Care Workers

•  AB 408 (MBC) Physician Health and Wellness Program

•  AB 447 E.R. Dispense Unused Prescription

•  AB 479 Criminal Procedure: Vacatur Relief: Harm Findings

•  AB 485 Discipline: Unsatisfied Judgment: Non-payment of Wages

•  AB 511 Radiologist Assistants

•  SB 679 Health Facilities 805 Reporting: 805 by race and gender

•  AB 1037 Public Health: Overdoes Treatment by Non-Physicians

•  AB 1186 Demographics data

•  AB 1501 (Berman) P.A. Supervision Scope of Practice

•  SB 387 Residency Accreditation Eligibility Revision

•  SB 470 Open Meetings Law

•  SB 518 Descendants of Slaves Certification

18.

Future Agenda Items and Meeting Dates-Denise Pines, MBA

19.  Adjournment

Online Access of Meeting

The Osteopathic Medical Board of California will also broadcast the public portion
of its meeting via WebEx Events. To participate in the WebEx Events meeting, please
log on to this website on the day of the meeting:

Click Here to Join Meeting

If joining by phone
+1-415-655-0001 US Toll
Access code: 2481 443 2648
Passcode: 6622814

Experiencing issues joining the Meeting?

Copy and paste the link text below into an internet browser:

https://dca-meetings.webex.com/dca-
meetings/j.php?MTID=m3708dcf5cd97032139fd886679bbfa29

Members of the public may but are not obligated to provide their names or personal
information  as  a  condition  of  observing  or  participating  in  the  meeting.  When
signing  into  the  WebEx  platform,  participants  may  be  asked  for  their  name  and
email  address.  Participants  who  choose  not  to  provide  their  names  will  need  to
provide  a unique identifier  such  as  their  initials  or  another  alternative,  so  that  the
meeting  moderator  can  identify  individuals  who  wish  to  make  public  comment;
participants who choose not to provide their  email  address  may  utilize  a  fictitious
email address like in the following sample format: XXXXX@mailinator.com.

Please Note: Because there is an audio delay, if you are participating by phone and
simultaneously watching the Webcast, the Board requests you turn off the sound to
the Webcast for improved clarity.

For further information about this meeting, please contact Machiko Chong at 916-
928- 7636 or in writing at 1300 National Drive, Suite 150, Sacramento, CA 95834. This
notice and agenda, and any available Board meeting materials, can be accessed
on the Board’s website at www.ombc.ca.gov

In accordance with the Bagley-Keene Open Meeting Act, all meetings of the Board,
including  the  teleconference  sites,  are  open  to  the  public.  Government  Code
section  11125.7  provides  the  opportunity  for  the  public  to  address  each  agenda
item during discussion or consideration by the Board prior to the Board taking any
action  on  said  item.  Members  of  the  public  will  be  provided  appropriate
opportunities to comment on any issue before the Board, but the Board President,
at  his  or  her  discretion,  may  apportion  available  time  among  those  who  wish  to
speak. Individuals may appear before the Board to discuss items not on the agenda;
however, the Board can neither discuss nor take official action on these items at the
time of the same meeting. (Government Code sections 11125, 11125.7(a).)

Board  meetings  are  held  in  barrier  free  facilities  that  are  accessible  to  those  with
physical disabilities in accordance with the Americans with Disabilities Act (ADA). If
you  are  a  person  with  a  disability  requiring  disability-related  modifications  or
accommodations to participate in the meeting, including auxiliary aids or services,
please  contact  Machiko  Chong,  ADA  Liaison,  at  (916)  928-7636  or  e-mail  at
Machiko.Chong@dca.ca.gov or send  a written request to the Board’s office at 1300
National Drive, Suite 150, Sacramento, CA 95834-1991.  Providing your request at least
five  (5)  business  days  before  the  meeting  will  help  to  ensure  availability  of  the
requested accommodation. Requests should be made as soon as possible, but at
least five (5) working days prior to the scheduled meeting. You may also dial a voice
TTY/TDD Communications Assistant at (800) 322-1700 or 7-1-1.

---

**[MINUTES] 2025-08-14_20250814_item_7.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390    |     F (916) 928-8392    |     www.ombc.ca.gov

Osteopathic Medical Board of California

Teleconference Minutes

May 15, 2025

MEMBERS
PRESENT:

STAFF
PRESENT:

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Andrew Moreno, Esq.
Brett Lockman, D.O.
Matthew Swain, D.O.

Machiko Chong, Licensing Program Manager
Erika Calderon, Executive Director
Beth Clark, Associate Governmental Program Analyst
Ralph Correa, Probation Monitor
Cristy Livramento, Enforcement Program Manager
Terri Thorfinnson, Legislative and Regulatory Specialist

MEMBERS OF
THE AUDIENCE:

Tracy Dominguez, Consumer Watchdog
Michele Monserratt-Ramos, Consumer Watchdog
Kimberly Turbin, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Monique Himes, Consumer Watchdog
Ryan Spencer, American College of Obgyn's district nine
Alicia Sanchez, California Medical Association (CMA)
Teyonna Bowman, Positive Outlook
Holly Macriss, Executive Director, OPSC

Agenda Item 1

Call to Order and Roll Call/Establishment of a Quorum

The Board Meeting of the Osteopathic Medical Board of California (OMBC) was called to
order by Madame President Denise Pines at 09:00 a.m. Machiko Chong, SSM I called
roll  and  determined  a  quorum  was  present.  Due  notice  was  provided  to  all  interested
parties.

Board Meeting Minutes – May 15, 2025

Agenda Item 2

Reading of the Board’s Mission Statement

Executive  Director  Erika  Calderon  read  the  Board’s  mission  statement:  "to  protect  the
public  by  requiring  competency,  accountability,  and  integrity  in  the  safe  practice  of
medicine by our osteopathic positions".

Agenda Item

3 Review and Possible Approval of Minutes

Associate  Governmental  Program  Analyst  Beth  Clark  presented  the  minutes  from  the
February 13, 2025, Teleconference Board Meeting.

No edits or corrections were identified after a page-by-page review. Public comment was
requested by the host; no requests were made online or in the meeting room.

Motion to approve the February 13, 2025, minutes with no corrections

Motion – Dr. Swain Second – Mr. Adamyan
•  Roll Call Vote was taken

•  Aye – Mr. Adamyan, Mr. Cummins, Dr. Lockman, Mr. Moreno, Dr. Patel, Ms.

Pines, Dr. Swain

•  Nay – None
•  Abstention – None
•  Absent – None

•  Motion carried to approve the February 13, 2025, minutes with no corrections.

Agenda Item 4
DO

Petition for Early Termination of Probation, Carlo G. Garibaldi,

The  Office  of  Administrative  Hearing  (OAH)  Administrative  Law  Judge  (ALJ)  Timothy
Aspinwall conducted the above hearing.

CLOSED SESSION

Pursuant to section 11126(c)(3) of the Government Code, the Board will meet in closed
session  for  discussion  and  to  take  action  on  disciplinary  matters,  including  the  above
petition.

Board Meeting Minutes – May 15, 2025

Agenda Item 5

Public Comment for Items not on the Agenda

President Denise Pines opened the floor for public comments on items not explicitly on
the agenda. No public comments were made in the meeting room or online.

Agenda Item 6

President’s Report

Madame  President  Denise  Pines  reported  on  the  OMBC's  ongoing  dedication  to
enhancing consumer protection objectives for the 2025-2026 fiscal year. She discussed
her participation in the Federation of State Medical Boards (FSMB) Hill Day on March 25,
2025, advocating for the SHARE Act, which aims for background check uniformity with
the interstate compact commission, though California is not currently part of the compact.

Ms.  Pines  reported  that  Executive  Director  Erika  Calderon  and  Dr.  Patel  attended  the
FSMB annual meeting in Seattle, where Dr. Patel ran for a board position and encouraged
others to  get  involved with  the  FSMB  due  to  its  forward-thinking  approach  on  medical
regulation challenges and guidelines (e.g., misconduct, DEI). Additionally, she noted that
the FSMB had established an Office of AI to explore technology for greater efficiencies
for boards, including smaller ones.

Ms.  Pines  advised  that  three  of  the  four  newly  established  OMBC  committees  have
already met.

No public comments were made online or in the meeting room.

Agenda Item 7

Board Member Communications with Interested Parties

Madame  President  Denise  Pines  disclosed  that  a  film  she  produced,  "The  M  factors
shedding  the  silence  on  menopause,"  was  screened  by  Assembly  Member  Rebecca
Borrower  Khan.  She  also  noted  communication  with  Assembly  Member  Diane  Pappin
regarding AB360.

No other board members had disclosures. No public comments were made online or in
the meeting room.

Agenda Item 8
Services Update

Intergovernmental Relations Reports and Administrative

•  A. DCA Update

Leslie  Barmby,  Associate  Governmental  Program  Analyst,  Board  and
Bureau  Relations,  provided  an  update  on  Governor  Newsom's  proposed
2025-26  State  Budget,  which  includes  a  reorganization  to  split  the

Board Meeting Minutes – May 15, 2025

Business,  Consumer  Services  and  Housing  Agency  into  two  agencies,
creating a dedicated Business and Consumer Services Agency where the
DCA  would  be  housed.  This  is  expected  to  strengthen  the  focus  on
consumer  protection.  The  plan  is  under  review  by  the  Little  Hoover
Commission and the Legislature.

Ms. Barmby advised that an executive order (N-22-25) was issued on March
3, 2025, requiring all state agencies to implement a hybrid telework policy
with a minimum of four days in-office per week starting July 1, 2025. OMBC
management  confirmed  that  sufficient  space  was  available  in  office  for
board staff.

Board  members  were  reminded  to  complete  their  Board  Member
Orientation  Training
(BMOT)  within  one  year  of  appointment  or
reappointment, with virtual sessions scheduled for June 18 and October 22,
2025.

Ms. Barmby also highlighted the fact that Public Service Recognition Week
was celebrated the first week of May.

No public comments were made.

•  B. Budget Update

Ryan Harrington, Budget Analyst, and Suzanne Bockus, Budget Manager,
from the DCA Budget Office provided the update.

It was noted that the board's fund condition statement showed a beginning
balance of $4.6 million in FY 2023-24, ending with $5 million (14.2 months
in reserve). For FY 2024-25, the projected fund balance is $4.5 million (11.7
months in reserve).

Expenditure projections for FY 2024-25 are approximately $4.15 million,
creating  a  reversion  of  $69,000  (1.64%).  Revenue  projections  for  FY
2024-25 are $3.74 million.

Executive  Director  Calderon  noted  that  a  regulatory  packet  to  increase
application fees is in the works to proactively address fund levels.

No public comments were made.

Agenda Item 9
Examiners (NBOME)

Update from the National Board of Osteopathic Medical

Dr. John Gimpel and Doug Murray presented updates on NBOME activities.

Board Meeting Minutes – May 15, 2025

Key exam changes were announced:

o  COMLEX Level 1 questions will be reduced from 352 to 320 (still 8 hours

testing time).

o  COMLEX Level 2 will also have reduced questions starting in June.

o  COMLEX Level 3 will transition from a two-day to a one-day exam.

o  Level 1 no longer provides numerical scores, only pass/fail.

o  Four attempts are allowed per COMLEX level; a fifth attempt can be

petitioned to the licensing authority.

An update on the C3DO (Core Competency Capstone Project) was provided. This project
explores campus-based clinical skills assessments, replacing the indefinitely suspended
Level 2 PE exam. The C3DO assesses communication, empathy, history-taking, physical
exam skills, and OMT across six stations at school campuses. California schools are not
currently participating in the pilot.

NBOME  continues  to  make  inroads  in  international  recognition;  US-trained  DOs  are
recognized  as  equivalent  to  MDs  in  various  countries,  including  Australia,  India,  and
Canada.

Doug Murray highlighted progress in electronic transcript sharing through FCVS and
efforts to establish direct data exchange with boards.

No public comments were made online.

Agenda Item 10  Executive Director’s Report

Executive Director Erika Calderon provided an update on personnel and administrative
functions.

Personnel  Updates:  The  OMBC  has  15.9  authorized  positions.  The  administrative
services and licensing programs have been merged under Licensing Program Manager
Machiko Chong, and Terri Thorfinnson is now the dedicated Legislative and Regulatory
Specialist.  Andrea  Harmon  (complaint  intake)  now  reports  directly  to  the  enforcement
manager.  Cristy  Livermento  was  promoted  to  Enforcement  Program  Manager  on  a
permanent basis, the first for the board. Rebecca Marco, retired annuitant, concluded her
two-year assignment assisting with regulatory packets.

Ralph Correa, the Probation Monitor, received the DCA Superior Accomplishment Award
for restructuring the probation program and creating electronic probationer folders and
templates.

Board Meeting Minutes – May 15, 2025

Executive  Order  N-15-25  deferred  renewal  fees  and  waived  duplicate/replacement
license fees for licensees impacted by the Los Angeles area fires, with minimal impact on
the Board's finances.

Executive  Order  N-22-25 mandates  a  return  to  four days  of  in-person  work per  week
starting July 1, 2025, which OMBC can accommodate.

The CURES fee increased from $9 to $15 yearly ($30 for a two-year cycle) on April 1,
2025.  Communications  efforts  include  regular  meetings  with  various  stakeholders,
including the CURES Executive Stakeholder Committee and Consumer Watchdog group.
The  third  edition  of  the  "OsteoScope"  newsletter  was  published,  and  social  media
platforms are actively used for outreach.

OMBC staff, including Madame President Pines and Dr. Patel, attended the OPSC 65th
Annual Convention and the FSMB Annual Meeting. The OMBC received the "Wellbeing
First Champion Badge for 2025" for removing overly broad and invasive mental health
questions from its licensing applications.

Staff  participated  in  the  4th  Annual  Latina  Maternal  Health  Fair  in  Bakersfield.  Public
comments praised the report and recognized the work of Cristy Livramento and Ralph
Correa.

Agenda Item 11

Licensing/Admin Program Summary

Machiko  Chong,  Licensing  Program  Manager,  presented  an  overview  of  licensing
statistics and program updates.

As  of  May  15,  2025,  there  are  16,565  licensed  osteopathic  physicians  and  surgeons,
1,174 postgraduate training licensees (PTL), and 1,269 fictitious name permits, and one
temporary  osteopathic  physician/surgeon  license.  There  are  312  pending  initial
applications, with 48 requesting expedite services. This includes 88 postgraduate training
license applications (growing) and 220 osteopathic physician and surgeon applications.
Ms. Chong noted that the Board experienced 51% decrease in Physician and Surgeon
applications  received  year-over-year  (Q1-Q3  FY  2023/24  vs  FY  2024/25)  was  noted,
attributed to a lack of new osteopathic schools in California.

The  Licensing  Unit  recently  integrated  three  additional  staff  members  as  part  of  a
reorganization.  Updates  have  been  made  to  CME  Compliance  and  Fictitious  Name
Permit documents, and BreEZe system transactions.

Staff will begin UAT testing for PTL and physician and surgeon applications, including the
removal  of a  postgraduate  training  modifier hold.  Review  and  revision  of  the  Fictitious
Name Permit application is also planned.

No public comments were made.

Board Meeting Minutes – May 15, 2025

Agenda Item 12  Enforcement Program

*[document truncated for length]*

---

**[MINUTES] 2025-08-14_20250814_item_10b.pdf**

Department of Consumer Affairs

Expenditure Projection Report
Osteopathic Medical Board
Reporting Structure(s): 11112600 Support
Fiscal Month: 12
Fiscal Year: 2024 - 2025
Run Date:  07/31/2025

PERSONAL SERVICES

Fiscal Code
5100  PERMANENT POSITIONS
5100  TEMPORARY POSITIONS
5105-5108  PER DIEM, OVERTIME, & LUMP SUM
5150  STAFF BENEFITS
PERSONAL SERVICES

OPERATING EXPENSES & EQUIPMENT

Line Item

PY Budget
$1,078,000
$0
$3,000
$685,000
$1,766,000

PY FM13
$978,367
$72,320
$13,278
$661,259
$1,725,224

Budget
$1,180,000
$0
$3,000
$766,000
$1,949,000

Current Month
$101,328
$7,693
$0
$60,284
$169,305

YTD
$1,225,012
$68,022
$1,800
$732,064
$2,026,899

Encumbrance  YTD + Encumbrance

$0
$0
$0
$0
$0

$1,225,012
$68,022
$1,800
$732,064
$2,026,899

Projections to Year End
$1,225,012
$75,715
$1,800
$736,420
$2,038,947

Balance
-$45,012
-$75,715
$1,200
$29,580
-$89,947

Fiscal Code

Line Item

5301  GENERAL EXPENSE
5302 PRINTING
5304 COMMUNICATIONS
5306 POSTAGE
5308 INSURANCE
53202-204  IN STATE TRAVEL
53206-208  OUT OF STATE TRAVEL
5322 TRAINING
5324  FACILITIES
53402-53403  C/P SERVICES (INTERNAL)
53404-53405  C/P SERVICES (EXTERNAL)
5342  DEPARTMENT PRORATA
5342  DEPARTMENTAL SERVICES
5344 CONSOLIDATED DATA CENTERS
5346 INFORMATION TECHNOLOGY
5362-5368  EQUIPMENT
5390 OTHER ITEMS OF EXPENSE
54  SPECIAL ITEMS OF EXPENSE
OPERATING EXPENSES & EQUIPMENT

OVERALL TOTALS

REIMBURSMENTS
OVERALL NET TOTALS

ESTIMATED TOTAL NET ADJUSTMENTS
OVERALL NET TOTALS

PY Budget
$138,000
$9,000
$20,000
$8,000
$0
$16,000
$0
$7,000
$114,000
$638,000
$212,000
$416,000
$294,000
$4,000
$4,000
$0
$0
$0
$1,880,000

PY FM13
$14,348
$23,732
$4,253
$43
$25
$14,263
$0
$0
$82,143
$557,181
$276,207
$825,607
$950
$14,346
$7,427
$5,086
$53
$674
$1,826,339

Budget
$127,000
$28,000
$24,000
$10,000
$0
$22,000
$0
$9,000
$128,000
$1,094,000
$253,000
$573,000
$3,000
$15,000
$10,000
$30,000
$0
$0
$2,465,000

Current Month
$4,170
$1,019
$140
$261
$0
$261
$0
$1,000
$5,177
$73,345
$16,425
$173,649
$0
$1,275
$1,429
$0
$0
$0
$278,151

YTD
$23,487
$3,271
$1,766
$11,335
$0
$25,694
$2,048
$1,000
$76,085
$832,874
$143,057
$992,818
$642
$1,275
$17,248
$32,839
$0
$680
$2,166,118

Encumbrance  YTD + Encumbrance

$4,581
$15,437
$0
$0
$0
$0
$0
$0
$150
$0
$30,591
$0
$0
$0
$0
$3,669
$0
$0
$54,427

$28,068
$18,708
$1,766
$11,335
$0
$25,694
$2,048
$1,000
$76,235
$832,874
$173,648
$992,818
$642
$1,275
$17,248
$36,507
$0
$680
$2,220,545

Projections to Year End
$28,434
$18,708
$2,642
$11,407
$25
$25,694
$2,048
$1,000
$79,050
$846,017
$178,342
$1,025,213
$1,000
$7,844
$22,292
$36,507
$0
$680
$2,286,903

Balance
$98,566
$9,292
$21,358
-$1,407
-$25
-$3,694
-$2,048
$8,000
$48,950
$247,983
$74,658
-$452,213
$2,000
$7,156
-$12,292
-$6,507
$0
-$680
$39,097

$3,646,000

$3,551,563

$4,414,000

$447,456

$4,193,017

$54,427

$4,247,444

$4,325,850

-$50,850

-$53,000
$3,593,000

-$108,000
$3,443,563

-$53,000
$4,361,000

$3,593,000

$3,443,563

-$66,000
$4,295,000

$447,456

$4,193,017

$54,427

$4,247,444

-$53,000
$4,272,850

$88,150

$447,456

$4,193,017

$54,427

$4,247,444

$4,272,850

$22,150

0.52%

Department of Consumer Affairs

Revenue Projection Report

Reporting Structure(s): 11112600 Support
Fiscal Month:
Fiscal Year: 2024 - 2025
Run Date:  08/01/2025

Revenue

Line Item

Fiscal Code
Delinquent Fees
Other Regulatory Fees
Other Regulatory License and Permits
Other Revenue
Renewal Fees
Revenue

Budget
$22,000
$51,000
$1,462,000
$74,000
$2,383,000
$3,992,000

July
$1,275
$3,125
$187,879
$856
$202,153
$395,288

August
$700
$2,632
$90,169
$0
$170,775
$264,276

September  October
$1,000
$2,275
$54,408
$62,243
$242,955
$362,881

$2,125
$2,275
$79,424
$49
$156,902
$240,775

November  December

$1,875
$1,900
$49,805
$0
$231,105
$284,685

$2,150
$1,300
$44,709
$0
$219,680
$267,839

January
$2,350
$1,350
$63,557
$61,919
$243,140
$372,316

February
$1,375
$4,200
$71,367
$175
$251,158
$328,275

March
$2,025
$2,600
$71,412
$181
$263,111
$339,329

April
$2,804
$2,152
$81,387
$56,876
$232,974
$376,193

May
$1,475
$2,705
$105,850
$0
$254,243
$364,273

June
$2,425
$1,325
$126,739
$0
$210,491
$340,980

Year to Date  Projection To Year End

$21,579
$27,839
$1,026,706
$182,299
$2,678,687
$3,937,110

$21,579
$27,839
$1,026,706
$182,299
$2,678,687
$3,937,110

0264 - Osteopathic Medical Board of California Fund
Analysis of Fund Condition
(Dollars in Thousands)

2025 Budget Act

PY w/ FM12 Projections

BEGINNING BALANCE

Prior Year Adjustment
Adjusted Beginning Balance

REVENUES, TRANSFERS AND OTHER ADJUSTMENTS

Revenues

4121200 - Delinquent fees
4127400 - Renewal fees
4129200 - Other regulatory fees
4129400 - Other regulatory licenses and permits
4163000 - Income from surplus money investments
4171400 - Escheat of unclaimed checks and warrants
4171500 - Escheat Unclaimed Property

Prepared 8.4.2025

PY
2024-25

CY
2025-26

BY
2026-27

BY +1
2027-28

BY +2
2028-29

$  5,050
$
$  5,050

-

$  4,614
$
$  4,614

-

$  3,960  $
$
$
-
$  3,960  $

3,119
-
3,119

$
$
$

2,129
-
2,129

$
21
$  2,679
28
$
$  1,027
143
$
1
$
1
$

$
23
$  2,259
52
$
$  1,507
139
$
-
$
-
$

$
23  $
$  2,259  $
52  $
$
$  1,507  $
46  $
$
$
$
$
$

-
-

23
2,259
52
1,507
31

-
-

$
$
$
$
$
$
$

23
2,259
52
1,507
15

-
-

Totals, Revenues

$  3,900  $  3,980  $  3,887  $

3,872  $

3,856

TOTALS, REVENUES, TRANSFERS AND OTHER ADJUSTMENTS

$  3,900  $  3,980  $  3,887  $

3,872  $

3,856

TOTAL RESOURCES

Expenditures:

$  8,950  $  8,594  $  7,847  $

6,991  $

5,985

1111 Department of Consumer Affairs (State Operations)
9892 Supplemental Pension Payments (State Operations)
9900 Statewide General Administrative Expenditures (Pro Rata) (State Operations)

$  4,094
$
37
205
$

$  4,356
37
$
241
$

$  4,487  $
-
$
$
241  $
$

4,621
-
241

$
$
$

4,760
-
241

TOTALS, EXPENDITURES AND EXPENDITURE ADJUSTMENTS

$  4,336  $  4,634  $  4,728  $

4,862  $

5,001

FUND BALANCE

Reserve for economic uncertainties

$  4,614  $  3,960  $  3,119  $

2,129  $

984

Months in Reserve

11.9

10.1

7.7

5.1

2.4

NOTES:
1. Assumes workload and revenue projections are realized in BY+1 and ongoing.
2. Expenditure growth projected at 3% beginning BY+1.

---

**[MINUTES] 2025-08-14_20250814_item_11.pdf**

Agenda Item 11
Osteopathic Medical Board of California
DATE REPORT ISSUED: August 14, 2025
ATTENTION: Members, Osteopathic Medical Board of California
SUBJECT: Executive Report
STAFF CONTACT: Erika Calderon, Executive Director
REQUESTED ACTION:
This report is intended to provide the Members of the Osteopathic Medical Board of
California (OMBC) with an update on personnel, and other administrative functions/projects
occurring at the OMBC.
No action is needed.
Please refer to attachment 11A-OMBC’s Organizational Chart.
Please refer to attachment 11B-OMBC’s Retention Schedule.
Board Member Reappointments:
The OMBC is happy to announce the reappointments of Gor Adamyan, Board Secretary
and John Cummings, JD and this past quarter.
State Budget and Travel Restrictions:
OMBC is still operating under the Department of Finances issued budget letters. OMBC must
monitor overall expenses and limit out of state travel to essential operational needs. All out of
state travel request must be approved by the governor’s office and approval will be limited to
mission critical only. Discretionary trips will not be considered this year.
Personnel:
The OMBC continues to have 15.9 authorized positions. There is one enforcement analyst
vacant position and there is another enforcement analyst out on maternity leave.
The Board has requested that we post to immediately backfill behind our vacant position
and requested a temporary limited term position to cover the desk for the analyst on leave.
Please refer to attachment 11A-OMBC’s Organizational Chart.
In June of 2025, OMBC advertised for a special investigator position through its blanket
authority and has made an offer. Ms. Yvonne Natad is scheduled to start with the Board on
Monday September 8, 2025. Ms. Natad has over 15 years of enforcement experience with
the last 10 years being a special investigator for the Medical Board of California. The Board
hopes that with this position the Board can reduce investigative costs and improve our
compliant processing times as it is projected that about 60% of overall field investigations
can be handled inhouse instead of sending them to the Division of Investigations (DOI).
Along with this update, Director Calderon has obtained subpoena enforcement authority

which will allow OMBC to request records through the administrative subpoena process
inhouse without having to request the assistance of DOI.
Executive Order N-22-25 – Return to Office
As previously report on March 3, 2025, Governor Newsom issued Executive Order N-22-25,
requiring all agencies and departments under his authority to implement a hybrid telework
policy with a default minimum of four in-person workdays per week, effective July 1, 2025.
The return to office has been postponed to July 1, 2026, through union negotiations. Just as
a reminder currently OMBC staff are coming into the office twice a week and at this time,
Director Calderon has not identified a need to have anyone coming into the office more days
with the exception of our reception desk which is a fulltime in office position.
Retention and Clarifications on “Purge Project”
On September 6, 2024, OMBC did a major revise of its retention schedule to be more
specific with all records across all programs and most recently revised its schedule in July
of 2025 to address two specific complaint closures for enforcement which were previously
not listed on the schedule. One being the non-jurisdictional closure which as a retention of
one (1) year. Secondly the Board separated its quality of care no violation closures involving
patient death and no patient death. A quality-of-care No Violation complaint involving patient
death will now have a retention of five (5) years. Allowing the Board to re-open the case
without having to recollect new records if new evidence is presented and the Board still finds
that the case has a statute of limitation timeframe to work with.
Last Board meeting during the enforcement program update the Board reported that the
office was working on a “purge project” causing questions and concerns, and OMBC wishes
to clarify the report. As reported in early 2023 OMBC was sharing office space with the
California Board of Naturopathic Medicine (CBNM). During the years that both Boards
shared office space OMBC organization suffered. Having one file room for both licensing
and enforcement, staff started to keep records in boxes, and it stop purging records for
several years to avoid any accidental purging. In addition, OMBC’s retention schedule was
very minimal, and Board staff felt uncomfortable purging anything, thus the Board had an
excessive number of records across all programs not only enforcement to purge. With
CBNM having their own office space now, OMBC has been working diligently for the past 2
years on getting the office organized which includes the purging records as previously stated
that had not been purge for at least two decades. Please refer to attachment 11B-OMBC’s
Retention Schedule.
OMBC’s Budget
Several questions have been asked by Board members about OMBC’s budget projections
in the next couple of fiscal years specifically about our months in reserves decreasing.
OMBC would like to address those concerns and address what Director Calderon has been
working on to increase the Boards revenue and address expenditures. Over the past two
years OMBC’s budget has been impacted by the additional leadership and staff positions
but most significantly because of its increase in consumer complaints which have resulted
in more disciplinary action taken by its enforcement program. In addition to an increase in
staffing levels, OMBC did a permanent Attorney General (AG) augmentation and just this
past quarter requested an augmentation in its expenditure authority for its office of
administrative hearing costs.

In addition to the AG’s costs one of the greatest enforcement expenditures is the Division of
Investigations (DOI). In fiscal year 2021-2022, OMBC’s total DOI costs were $270,116. This
past fiscal year 2024-2025 total costs nearly doubled to $491,153. With the onboarding of
OMBC’s special investigator which is projected to handle about 60 percent of overall cases
requiring  formal  investigations  OMBC  is  projecting  at  minimum  a  cost  savings  of
$150,000.00 per fiscal year in formal investigation costs. OMBC plans to continue to utilize
DOI services on cases that could result in criminal filings or may require search warrants,
however most cases will be handled in-house by the Board’s special investigator. Please
refer to the charts listed below:

Total number of cases referred to DOI by fiscal year for the past 5 years assigned to Sworn
and Non-Sworn
Total
|     | Assigned to  | Assigned  |     |     |     |     |
| --- | ------------ | --------- | --- | --- | --- | --- |
Referred to
|          | non-sworn  |     | to sworn  |     |     |     |
| -------- | ---------- | --- | --------- | --- | --- | --- |
|    HQIU  |            |     |           |     |     |     |
| 2020-21  | 37         | 0   | 37        |     |     |     |
| 2021-22  | 32         | 0   | 32        |     |     |     |
| 2022-23  | 48         | 20  | 28        |     |     |     |
| 2023-24  | 63         | 20  | 43        |     |     |     |
| 2024-25  | 78         | 14  | 64        |     |     |     |

Case study of complaint complexity for cases handled through formal investigations for the
past 5 fiscal years
Complaints by Complexity   2020-21  2021-22  2022-23  2023-24  2024-25
| Negligence Death Serious Injury     |     |     | 1   | 2   | 7  5    | 3   |
| ----------------------------------- | --- | --- | --- | --- | ------- | --- |
| Negligence                          |     |     | 5   | 3   | 4  12   | 31  |
| Excessive Prescribing               |     |     | 6   | 8   | 3  2    | 1   |
| Inappropriate Prescribing           |     |     | 0   | 1   | 3  4    | 3   |
| Impairment Mental/Physical          |     |     | 0   | 1   | 0  1    | 0   |
| Practice While Under the Influence  |     |     | 0   | 1   | 1  4    | 3   |
| Substance Abuse                     |     |     | 3   | 3   | 0  3    | 1   |
| Sexual Misconduct During Treatment  |     |     | 2   | 2   | 4  2    | 8   |
| Sexual Misconduct                   |     |     | 1   | 0   | 1  2    | 3   |
| Felony Arrest/Conviction            |     |     | 3   | 2   | 3  0    | 0   |
| Misdemeanor Arrest/Conviction       |     |     | 0   | 0   | 9  5    | 1   |
| Fraud                               |     |     | 0   | 1   | 0  0    | 2   |
| Unlicensed Practice                 |     |     | 4   | 2   | 5  7    | 11  |
| Unprofessional Conduct              |     |     | 12  | 6   | 8  16   | 11  |
| Totals                              |     |     | 37  | 32  | 48  63  | 78  |
*Field investigations increased over 50% in the past five years

Secondly, with the Board’s newly approved continuing medical education and cite and fine
regulations the Board projects issuing up to 68 citations per year with an average fine
amount of $1,500 per citation, which may result in a revenue increase of approximately
$120,000 per fiscal year.

Lastly, with the Board’s applications and petitions fees and retired license status regulation is
projecting another annual revenue of approximately $424,000 per year.

In total with all these changes, OMBC is projecting an annual revenue increase of approximately
$694,000.
Communication
Director Calderon represents the prescribing Boards as part of the CURES Executive
Stakeholder Committee and continues to meet regularly with DCA’s leadership staff and
the Department of Justice (DOJ).
Director Calderon had calls and email exchanges with Board President Denise Pines to
discuss pending and ongoing projects and meeting agendas.
Director Calderon continues to meet periodically with the Board’s Attorney General Liaison
Ms. Karolyn Westfall and communicates frequently with Senior Assistant Attorney General
Ms. Gloria Castro.
Director Calderon continues to meet periodically with members of the Consumer Watchdog
group to gather their input on improving enforcement practices and procedures.
Enforcement staff continue to meet monthly with the DCA’s Division of Investigations HQIU
office to discuss progress of pending investigations.
Lastly for communications, our committee meetings have started, and Board leadership
will continue to meet frequently with our designated committee members, additionally staff
participated in meetings with other local, state, and national organizations in discussing
and deciding regulatory measures common to OMBC and others. These organizations
include but are not limited to; Office of Attorney General (AGO), Department of Justice
(DOJ), Department of Consumer Affairs (DCA), other healing art Boards such as (MBC,
BRN, BOP, PAC, PTBC), California Department of Public Health (CDPH), Department of
Health Care Services (DHCS), the Federation of State Medical Board (FSMB), the National
Board of Osteopathic Medical Examiners (NBOME), International Association of Medical
Regulatory Authorities (IAMRA), Osteopathic Physicians and Surgeons of California
(OPSC), American College of Osteopathic Family Physicians of California (ACOFPCA),
and lastly Premier Health who is now handling the Board’s diversion program.
Outreach Update:
The OMBC is working on its 4th edition of its newsletter OsteoScope. This communication
tool is designed to keep applicants, licensees, and consumers informed by sharing Board
updates and relevant Board information such as changes in leadership and staff, our
applications, CME requirements, new legislation and regulations, and enforcement
processes and actions taken.
The OMBC continues to post Board content regularly on all of its social media platforms
such as Facebook, Linkedin, and X. The Board continues to keep its website current which
includes positing relevant legislation, frequently ask questions, publications, and
enforcement actions.
This past quarter OMBC

*[document truncated for length]*

---

**[MINUTES] 2025-08-14_20250814_item_11a.pdf**

PROPOSED
LEGEND
| Department of Consumer Affairs (DCA)  |     |     |     |     |     | OMBC STAFFING  |
| ------------------------------------- | --- | --- | --- | --- | --- | -------------- |
Red: Vacant
|     |     |     |     | Green: Blanket  |     | FY 2025/2026  |
| --- | --- | --- | --- | --------------- | --- | ------------- |
Osteopathic Medical Board of California (OMBC)
RA: Retired Annuitant
August 1, 2025
|     |     |     |     | +: CORI Designated  |     | Authorized Positions: 15.9  |
| --- | --- | --- | --- | ------------------- | --- | --------------------------- |
Blanket Positions: 2.0

TOTAL: 17.9

  Executive Director
Erika Calderon

608-110-5665-002

| Lic ensing Unit  |     | Enforcement Unit  |     |     |     | Legislation/Regulations  |
| ---------------- | --- | ----------------- | --- | --- | --- | ------------------------ |
Investigations  Probation
Staff S ervices Manager I
Staff Services Manager I  Special Investigator (LT)  Associate Governmental  Staff Services Manager I
Ma chiko Chong+
  Cristy Livramento  Yvonne Natad  Program Analyst  (Specialist)
608-110-4800-002   608-110-4800-003  608-110-8612-907  Ralph Correa  Terri Thorfinnson

|     |     |     |     | 608-110-5393-001  |     | 608-110-4800-001  |
| --- | --- | --- | --- | ----------------- | --- | ----------------- |

| Associate Governmental  |     | Associate Governmental  |     |     |     |     |
| ----------------------- | --- | ----------------------- | --- | --- | --- | --- |

| Pro gram Analyst  |     | Program Analyst  |     |     |     |     |
| ----------------- | --- | ---------------- | --- | --- | --- | --- |

| D avid Moran  |     | VACANT (1.0)  |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | --- | --- |
608 -110-5393-006
|     |     | 608-110-5393-002(.9)  |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- |

| Jamie Nichols  |     | Steve Ly  |     |     |     |     |
| -------------- | --- | --------- | --- | --- | --- | --- |
608 -110-5393-007
608-110-5393-003
|                          |     |                         |     |     |     |     |
| ------------------------ | --- | ----------------------- | --- | --- | --- | --- |
| Staff S ervices Analyst  |     | Elizabeth “Beth” Clark  |     |     |     |     |
Gab riela Gonzalez
608-110-5393-005
608 -110-5157-001

|     |     | Gloria Laughlin  |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- |

| Dina Ruprecht  |     | 608-110-5393-801  |     |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- | --- |
608 -110-5157-006

|     |     | VACANT  |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- |
 Mia Quinn
608-110-5393-907
608 -110-5157-008

|                        |     | Staff Services Analyst  |     |     |     |     |
| ---------------------- | --- | ----------------------- | --- | --- | --- | --- |
| Office Technician (T)  |     | Andrea Harmon           |     |     |     |     |

| Sanjay Naresh   |     | 608-110-5157-009  |     |     |     |     |
| --------------- | --- | ----------------- | --- | --- | --- | --- |

608-110-1139-005

|     |     |     | Executive Director or Designee         |     |     |   Date   |
| --- | --- | --- | -------------------------------------- | --- | --- | -------- |
|     |     |     |  Classification & Recruitment Analyst  |     |     |    Date  |

---

**[MINUTES] 2025-08-14_20250814_item_11b.pdf**

Docusign Envelope ID: 5A368975-CAA4-49BE-99EA-40FFB9F8FF36
STATE OF CALIFORNIA – SECRETARY OF STATE
STATE RECORDS PROGRAM
RECORDS RETENTION SCHEDULE
STD.73 (REV. 2/2015)
(1) DEPARTMENT* (2) AGENCY BILLING CODE IMS CODE (3) 1 14
Department of Consumer Affairs 57467 PAGE OF PAGES
(4) DIVISION / BRANCH / SECTION (5) ADDRESS
Osteopathic Medical Board of California 1300 National Drive, Suite 150, Sacramento CA 95834
CHECK THE APPROPRIATE BOX
(6) New schedule of records that have never been scheduled. [Complete boxes (9)–(12)]
(7) Revising a previous schedule. [Complete boxes (9)–(16)] (A new approval number will be assigned.)
(8) Amending some pages of a previous schedule. [Complete boxes (13) - (16)] (The original approval number will remain in effect.)
(9) SCHEDULE NUMBER (10) SCHEDULE DATE (11) NUMBER OF PAGES (12) CUBIC FEET (Total Schedule)
NEW SCHEDULE INFORMATION
(If applicable) OMB 2025 06/16/2025 14 244
(13) SCHEDULE NUMBER (14) APPROVAL NUMBER (15) APPROVAL DATE(S) (16) PAGE NUMBER(S) REVISED
PREVIOUS SCHEDULE INFORMATION
(If applicable) OMB 2024 2020-194A2 09/06/2024 ALL
(17) FUNCTIONAL STATEMENT
The purpose of the Osteopathic Medical Board of California is to help maintain professional and legal standards in the delivery of osteopathic medicine to the people of California by means of upholding the statutory provisions of the
Osteopathic Initiative Act, Laws and Regulations, and the Medical Practice Act, etc.
PART I – AGENCY STATEMENTS
As the program manager (or person authorized to sign for the program manager) directly responsible for the records listed on this records retention schedule, I certify that all records
listed are necessary and that each retention period is correct. For revisions, all items on the previous schedule are included or accounted for on the recapitulation. Vital records
identified by this schedule are protected. If protection is not currently provided but plans are underway, the details of such plans are shown in Column 48, Remarks.
(18) SIGNATURE - MANAGER RESPONSIBLE FOR THE RECORDS (19) TITLE NAME - (Printed or Typed) (20) PHONE NUMBER (21) DATE SIGNED
Executive Director Erika Calderon 916-928-7639 7/2/2025
In accordance with Government Code 12274, approval of this Records Retention Schedule by the Secretary of State is hereby requested. Retention periods shown have been established in
accordance with the criteria set forth by Section 1667 of the State Administrative Manual.
(22) SIGNATURE - RECORDS MANAGEMENT ANALYST (23) CLASSIFICATION (24) NAME - (Printed or Typed) (25) PHONE NUMBER (26) DATE SIGNED
DCA RMC/AGPA Mac Aguilar 2798951282 7/2/2025
PART II A – SECRETARY OF STATE APPROVAL (Per Government Code Section 12272)
(27) SIGNATURE - CalRIM CONSULTANT NAME - (Printed or Typed) (28) APPROVAL NUMBER (29) APPROVAL DATE (30) EXPIRATION DATE
Noel Mosqueda 2025-124 07/02/2025 07/02/2030
PART II B – ARCHIVAL SELECTION (Per Government Code Section 12223) FOR ARCHIVES' STAMP
THE ATTACHED RECORDS RETENTION SCHEDULE:
(31) Contains no material subject to further review by the California State Archives
Contains material subject to archival review. Items stamped “NOTIFY ARCHIVES” may not be destroyed without clearance by the
(32) California State Archives. (Per Section 1671 of the State Administrative Manual.)
(33) SIGNATURE - CHIEF OF ARCHIVES OR DESIGNATED REPRESENTATIVE NAME - (Printed or Typed) (34) DATE SIGNED
7/3/2025
Michael McNeil
*Department refers to any Agency, Department, Board, Commision, Office or Other

Docusign  Envelope  ID:  5A368975-CAA4-49BE-99EA-40FFB9F8FF36
STATE  RECORDS  PROGRAM
STATE  OF  CALIFORNIA  - SECRETARY  OF  STATE
RECORDS  RETENTION  SCHEDULE
STD.  73  (REV.  12/2020)

| (35)  APPROVAL  NUMBER   |     |     |     |     |     | (36)   |
| ------------------------ | --- | --- | --- | --- | --- | ------ |
2025-124   Page 2 of  14 Pages
ITEM  # CUBIC  FEET*   CA. STATE  TITLE  AND  DESCRIPTION  OF  RECORDS   MEDIA   VITAL   RETENTION   PRA   REMARKS
|     | ARCHIVES  USE   |                                    |     |                  |               | &  IPA    |
| --- | --------------- | ---------------------------------- | --- | ---------------- | ------------- | --------- |
|     |                 |                                    |     | OFFICE   DEPT.   | SRC   TOTAL   |           |
|     | ONLY            | (Double  spaces  between  items)   |     |                  |               |           |
|     |                 |                                    |     |                  |               |           |
(37)   (38)   (39)   (40)   (41)   (42)   (43)   (44)   (45)   (46)   (47)   (48)

FUNCTIONAL  STATEMENT
Unit:  Osteopathic  Medical  Board  of  California
Function: The purpose of the Osteopathic Medical Board of California is to help maintain professional and legal standards in the delivery
of osteopathic  medicine to the people of California by means of upholding the statutory  provisions  of the Osteopathic Initiative Act, Laws
and Regulations, and the Medical Practice Act,  etc.

ACRONYMS
|     | DCA    | Department  of  Consumer  Affairs   |     |     |     |     |
| --- | ------ | ----------------------------------- | --- | --- | --- | --- |
|     | HR     | Human  Resources                    |     |     |     |     |
|     | BPC    | Business  and  Professions  Code    |     |     |     |     |
|     | CCR    | California  Code  of  Regulations   |     |     |     |     |
|     | GC     | Government  Code                    |     |     |     |     |
|     | NOPA   | Notice of  Personnel  Action        |     |     |     |     |
|     | MSA    | Merit  Salary  Adjustment           |     |     |     |     |
|     | CC     | Civil  Code                         |     |     |     |     |
|     | STD    | Standard Form                       |     |     |     |     |
|     |        |                                     |     |     |     |     |
|     |        |                                     |     |     |     |     |

Docusign  Envelope  ID:  5A368975-CAA4-49BE-99EA-40FFB9F8FF36
STATE  RECORDS  PROGRAM
STATE  OF  CALIFORNIA  - SECRETARY  OF  STATE
RECORDS  RETENTION  SCHEDULE
STD.  73  (REV.  12/2020)

| (35)  APPROVAL  NUMBER   |     |     |     |     |     |     |     | (36)   |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | ------ |
2025-124   Page 3 of  14 Pages
ITEM  # CUBIC  FEET*   CA. STATE  TITLE  AND  DESCRIPTION  OF  RECORDS   MEDIA   VITAL   RETENTION   PRA   REMARKS
|     | ARCHIVES  USE   |     |                                    |     |          |               |         | &  IPA    |
| --- | --------------- | --- | ---------------------------------- | --- | -------- | ------------- | ------- | --------- |
|     |                 |     |                                    |     | OFFICE   | DEPT.   SRC   | TOTAL   |           |
|     | ONLY            |     | (Double  spaces  between  items)   |     |          |               |         |           |
|     |                 |     |                                    |     |          |               |         |           |
(37)   (38)   (39)   (40)   (41)   (42)   (43)   (44)   (45)   (46)   (47)   (48)

| (35)  APPROVAL  NUMBER   |     |     |     |     |     |     |     | (36)   |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | ------ |
ITEM  # CUBIC  FEET*   CA.  STATE   TITLE  AND  DESCRIPTION  OF  RECORDS   MEDIA   VITAL   PRA   REMARKS
RETENTION
|     |     |     |     |     |          |               |         |     |
| --- | --- | --- | --- | --- | -------- | ------------- | ------- | --- |
|     |     |     |     |     | OFFICE   | DEPT.   SRC   | TOTAL   |     |
|     |     |     |     |     |          |               |         |     |
|     |     |     |     |     |          |               |         |     |
(37)   (38)   (39)   (40)   (41)   (42)   (43)   (44)   (45)   (46)   (47)   (48)
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ADMINISTRATIVE  SERVICES
|     |     |                       |     |     |            |     |              |                                           |
| --- | --- | --------------------- | --- | --- | ---------- | --- | ------------ | ----------------------------------------- |
| 1   |     | Personnel  Records:   |     |     |            |     |              |                                           |
|     |     |                       |     |     |            |     |              |                                           |
|     |     |                       |     |     |            |     |              |   Active until  hired and RPA packet is   |
|     |     |                       |     |     | Active  +  |     | Active+  60  |                                           |
1A   Employee  Applicant  Files   E   XI   uploaded  in  ECOS,  purge  60  days  from
|     |     |     |     |     | 60 days   |     | days   |     |
| --- | --- | --- | --- | --- | --------- | --- | ------ | --- |
upload. GC 7927, 7928; IPA 1798
|     |     |     |     |     |              |     |              |                                           |
| --- | --- | --- | --- | --- | ------------ | --- | ------------ | ----------------------------------------- |
|     |     |     |     |     |              |     |              |   Active while employed with the Board.   |
|     |     |     |     |     | Active  +1   |     | Active  +1   |                                           |
1B   Employee Personnel  Folders   E   XI   Retain for 1 year after seperation and
|     |     |     |     |     | Year   |     | Year   |     |
| --- | --- | --- | --- | --- | ------ | --- | ------ | --- |
then  destroy.  GC  7927,  7928;  IPA  1798
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Active while Board member's
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
appointment (max 8 years). Retain for 1
|     |     |     |     |     |              |     |              |     |
| --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- |
|     |     |     |     |     | Active  +1   |     | Active  +1   |     |
1C   Board Member  Files   E   year after  Board member terms  out.
|     |     |     |     |     | Year   |     | Year   |     |
| --- | --- | --- | --- | --- | ------ | --- | ------ | --- |
(Records  include  all  documents  included
on the HR05 form)
|          |     |                               |     |     |             |     |           |                                                |
| -------- | --- | ----------------------------- | --- | --- | ----------- | --- | --------- | ---------------------------------------------- |
| 2        |     | Fiscal:                       |     |     |             |     |           |                                                |
|          |     |                               |     |     |             |     |           |                                                |
|          |     |                               |     |     | Active+  3  |     | Active+3  | Active  is  Current  Fiscal  Year,  retain  3  |
| 2A       |     | Report of  Collections        |     | E   |             |     |           |                                                |
|          |     |                               |     |     | Years       |     | Years     | years thereafter, then destroy                 |
|          |     |                               |     |     |             |     |           |                                                |
|          |     |                               |     |     |             |     |           |                                                |
|          |     |                               |     |     | Active+3    |     | Active+3  | Active  is  Current  Fiscal  Year,  retain  3  |
| 2B   

*[document truncated for length]*

---

**[MINUTES] 2025-08-14_20250814_item_12a.pdf**

Osteopathic Medical Boad of California
Current Licensee Population
Agenda Item 12A -Application Services Stats
Stats FY 24-2025 Q1,Q2,Q3,Q4
Osteopathic Physician and Surgeon
License Status Total Licensees
Active 14,375
Delinquent/Expired 1948
Inactive 421
Total: 16,744
Postgraduate Training License (PTL)
License Status Total Licensees
Active 1,212
Delinquent/Expired 4
Inactive 0
Total: 1,216
Temporary License
License Status Total Licensees
Temp Osteopathic Physician and Surgeon 0
Temp Postgraduate Training License (PTL) 0
Total: 0
Fictitious Name Permit
License Status Total Licensees
Active 1,013
Delinquent/Expired 277
Inactive 0
Total: 1,290
Total Number of Licensees/Permit Holders 19,250

Osteopathic Physician  and  Surgeon
|                     | License Status  | FY  2022-2023  | FY  2023-2024  |        | FY  2024-25  |                     |     |
| ------------------- | --------------- | -------------- | -------------- | ------ | ------------ | ------------------- | --- |
| Active              |                 |                | 12135          | 13495  |              | 14375               |     |
| Delinquent/Expired  |                 |                | 1708           | 1755   |              | 1948                |     |
| Inactive            |                 |                | 502            | 467    |              | 421 Growth in 3YRS  |     |
16.73%
| Total:  |     |     | 14345  | 15717  |     | 16744  |     |
| ------- | --- | --- | ------ | ------ | --- | ------ | --- |
Postgraduate Training  License (PTL)
|                     | License Status  | FY  2022-2023  | FY  2023-2024  |      | FY  2024-25  |        |     |
| ------------------- | --------------- | -------------- | -------------- | ---- | ------------ | ------ | --- |
| Active              |                 |                | 1185           | 906  |              | 1,212  |     |
| Delinquent/Expired  |                 |                | 2              | 4    |              | 4      |     |
0 Growth in 3YRS
| Inactive  |     |     | 0     | 0    |     |        |        |
| --------- | --- | --- | ----- | ---- | --- | ------ | ------ |
| Total:    |     |     | 1187  | 910  |     | 1,216  | 2.44%  |
Temporary  License
|                                          | License Status  | FY  2022-2023  | FY  2023-2024  |     | FY  2024-25  |     |     |
| ---------------------------------------- | --------------- | -------------- | -------------- | --- | ------------ | --- | --- |
| Temp Osteopathic  Physician and Surgeon  |                 |                | 0              | 2   |              | 0   |     |
Temp Postgraduate Training License (PTL)  0  0  0 Growth in 3YRS
0%
| Total:  |     |     | 0   | 2   |     | 0   |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
Fictitious Name Permit
|                     | License Status  | FY  2022-2023  | FY  2023-2024  |      | FY  2024-25  |        |     |
| ------------------- | --------------- | -------------- | -------------- | ---- | ------------ | ------ | --- |
| Active              |                 |                | 838            | 876  |              | 1,013  |     |
| Delinquent/Expired  |                 |                | 422            | 429  |              | 277    |     |
0 Growth in 3YRS
| Inactive  |     |     | 0     | 0   |     |        |        |
| --------- | --- | --- | ----- | --- | --- | ------ | ------ |
| Total:    |     |     | 1260  | 0   |     | 1,290  | 2.38%  |
14.63%
Total  Number  of  Licensees/Permit  Holders  16792  1305  19,250

---

**[MINUTES] 2025-08-14_20250814_item_12b.pdf**

Osteopathic Medical Board of California
Application Renewal Services
Agenda Item 12B - Application Services Q1 - Q4 Program Stats
Application Services Statistics Report
Total Applications Received
|                               | FY 2023/24  |        | FY 24/25  |        | Year  →  Year  |       |
| ----------------------------- | ----------- | ------ | --------- | ------ | -------------- | ----- |
|                               |             | YTD    |           | YTD    | Change         |       |
| Physician and Surgeon         |             | 1,707  |           | 1,196  |                | -43%  |
| Postgraduate Traning License  |             | 723    |           | 710    |                | -2%   |
| Fictitious Name Permits       |             | 146    |           | 217    |                | 33%   |
| Total                         |             | 2,576  |           | 2,123  |                | -18%  |
Applications Approved
|                               | FY 2023/24  |        | FY 24/25  |        | Year  →  Year  |       |
| ----------------------------- | ----------- | ------ | --------- | ------ | -------------- | ----- |
|                               |             | YTD    |           | YTD    | Change         |       |
| Physician and Surgeon         |             | 1,658  |           | 1,247  |                | -25%  |
| Postgraduate Traning License  |             | 583    |           | 694    |                | 19%   |
| Fictitious Name Permits       |             | 142    |           | 162    |                | 14%   |
| Total                         |             | 2,383  |           | 2,103  |                | -12%  |
Renewals
|                          | FY 2023/24  |        |     |        | Year  →  Year  |      |
| ------------------------ | ----------- | ------ | --- | ------ | -------------- | ---- |
|                          |             | YTD    |     | YTD    | Change         |      |
| Physician and Surgeon    |             | 5,511  |     | 6,473  |                | 17%  |
| Ficticious Name Permits  |             | 802    |     | 903    |                | 13%  |

---

**[MINUTES] 2025-08-14_20250814_item_13.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY  •  GAVIN NEWSOM, GOVERNOR

DEPT. OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov

Briefing Paper

Agenda Item 13

Date:

August 14, 2025

Prepared for:  OMBC Members

Prepared by:

Cristy Livramento, Enforcement Program Manager

Subject:

Enforcement Program Updates

Purpose:

Update on Enforcement Program

Attachments:

13 (A) Enforcement and Probation Performance
Measures Q1, Q2, Q3, and Q4 FY 2024/2025

Background:

This is a report on the updates involving the Board’s Enforcement Unit for Q1, Q2, Q3,
& Q4 of FY 2024/2025.

Please also refer to attachment 13(A), which encompasses the Enforcement Program
statistics.

Analysis:

During Q4 ,  nine  (9)  complaint  interviews  were  offered  by  staff.    Two  (2)  complainant
interviews were completed.  During Q3, thirty-two (32) complaint interviews were offered
by staff.  Eighteen (18) of them were completed.

Impact statements are an opportunity for patient’s, their families, and representatives to
describe the harm they experienced as a result of the subject’s care.  Impact statements
are  optional,  and  the  opportunity  is  provided  to  the  patient  when  a  complaint  case  is
referred to HQIU.  Upon receipt of the impact statement, enforcement staff will provide
the impact statement to the assigned investigator.  Impact statements should include the
subject’s  name,  case  number,  and  the  name  of  the  writer,  along  with  their  contact
information.  In addition, it should include a brief synopsis of the care provided by the
subject, and how the subject’s care has made an impact to those involved.  Additional
information  may  be  requested  by  the  assigned  investigator.    If  an  Accusation  is  filed
against the subject, the impact statement may be provided to the subject as part of the
discovery  process,  and  the  impact  writer  may  be  called  to  testify  as  a  witness  at  the
administrative hearing.

Board Program Statistics:

For statistics, please refer to attachment 12(a) which covers the Enforcement Program’s
Q1, Q2, Q3, and Q4 statistics for fiscal year 2024/2025 in comparison to Q1, Q2, Q3,
and Q4 of last fiscal year 2023/2024.

Performance  Measure  1  (PM1):  covers  the amount of  consumer  complaints, arrests,
and  convictions  received.  The  unit  has  received  1011  complaints,  and  24
arrest/conviction  notices.  A  significant  increase  of  26%  of  total  complaints  and
arrest/convictions in comparison to last year. The increase in complaints received can
still  be  attributed  to  the  fact  that  enforcement  is  now  initiating  enforcement  files  on
applications  with  prior  arrest  histories  in  addition  to  more  Board  awareness  that  the
Board is receiving through its outreach efforts.

Performance Measure 2 (PM2): is the average number of days it takes for our analysts
to initiate complaints and acknowledge receipt. The target for this performance measure
is ten (10) days and we are at 5 days year to date.

Performance  Measure  3  (PM3):  is  the  average  number  of  days  it  takes  to  complete
investigations  and  enforcement  action  for  cases that  are not  referred  to  the  Attorney
General’s  Office  for  formal  discipline.   Case aging here fluctuates greatly because it
takes an average of all cases, and one or two very complicated cases can skew these
numbers drastically.   These  number  include  the  timeline  for  desk  and  DOI’s  Health
Quality Investigation Unit (HQIU) investigations. The target for PM3 is 360 days our total
cycle time is at 189 days which is a decrease of 9% from last fiscal year. Not only is PM
3 being met, but this is also in addition to a larger workload in comparison to last fiscal
and the end of Q4.

Performance  Measure  4  (PM4):  is  the  average  number  of  days  it  takes  to  complete
investigations and enforcement actions that are transmitted to the Attorney General’s
Office for formal disciplinary action. Case aging in this category is at 955 days.  The target
for PM4 is 540 days, and although we did not meet the target in this category, YTD, it did go
down 20% in comparison to last fiscal year.

For  FY  2024/2025,  the  Board  continues  to  be  well  under  its  performance  measure
targets for three  (3) of its performance  measures.   As  previously  reported PM4 is the
measure that unfortunately the Board has less control over as this measure takes into
consideration  the  timeline  from  the  Attorney  General’s  Office,  respondent’s  legal
representatives, and the Office of Administrative Hearings.

The  Board  currently  has  669  pending  enforcement  cases,  with  81  of  those  cases
pending at  HQIU, and 24 of those pending cases at the Attorney General’s Office.

YTD the Board has filed four (4) Interim Suspension Orders, issued four (4) public letters
of reprimand, filed fourteen (14) Accusations, and one (1) Petition to Revoke Probation,
issued five (5) administrative citations, placed ten (10) licensees on probation, had two
(2) licensees surrender their license, and three (3) licenses were revoked.

Action Requested: No Action Required

---

**[MINUTES] 2025-08-14_20250814_item_13a.pdf**

Osteopathic Medical Board of CA
13 (A) Attachment
Enforcement Performance Measures Q1 Q2 Q3 Q4
Enforcement Statistics Report
Complaints
|     | FY 23/24  |      |            |     | Fiscal Year 24/25      |     |            |      |     | Year  →  Year  |     |
| --- | --------- | ---- | ---------- | --- | ---------------------- | --- | ---------- | ---- | --- | -------------- | --- |
|     |           |      |            | Q1  | Q2                     | Q3  | Q4         |      |     |                |     |
|     |           | YTD  |            |     |                        |     |            | YTD  |     | Change         |     |
|     |           |      | Jul - Sep  |     | Oct  - Dec  Jan - Mar  |     | Apr - Jun  |      |     |                |     |
PM1:  Complaints Received  803  241  255  251  264  1011  26%
| PM1:  Convictions/Arrest Received  |     | 22   |     | 7    | 4    |      | 8  5  |     | 24    |     | 9%   |
| ---------------------------------- | --- | ---- | --- | ---- | ---- | ---- | ----- | --- | ----- | --- | ---- |
| PM1:  Total Received               |     | 825  |     | 248  | 259  | 259  | 269   |     | 1035  |     | 25%  |
Complaint Intake
|     | FY 23/24  |     |     |     | Fiscal Year 24/25  |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Year  →  Year
Target:  10 Days
|                         |     |      |            | Q1  | Q2                     | Q3  | Q4         |      |     | Change  |      |
| ----------------------- | --- | ---- | ---------- | --- | ---------------------- | --- | ---------- | ---- | --- | ------- | ---- |
|                         |     | YTD  |            |     |                        |     |            | YTD  |     |         |      |
|                         |     |      | Jul - Sep  |     | Oct  - Dec  Jan - Mar  |     | Apr - Jun  |      |     |         |      |
| PM2:  Intake/Avg. Days  |     | 3    |            | 5   | 4                      |     | 4  6       |      |     |         | 58%  |
5
Investigations
Fiscal Year 24/25
|     | FY 23/24  |     |     |     |     |     |     |     |     | Year  →  Year  |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
Target: 360 Days
|                     |     |      |            | Q1   | Q2                     | Q3   | Q4         |      |      |         |       |
| ------------------- | --- | ---- | ---------- | ---- | ---------------------- | ---- | ---------- | ---- | ---- | ------- | ----- |
|                     |     | YTD  |            |      |                        |      |            | YTD  |      | Change  |       |
|                     |     |      | Jul - Sep  |      | Oct  - Dec  Jan - Mar  |      | Apr - Jun  |      |      |         |       |
| PM3: Volume         |     | 773  |            | 209  | 252                    | 233  | 181        |      | 875  |         | 13%   |
| PM3a:  Intake Only  |     | 5    |            | 3    | 4                      |      | 3  5       |      | 4    |         | -25%  |
PM3b:  Investigation Only  207  159  187  183  171  175  -15%
| PM3c:  Post Investigation Only  |     | 4   |     | 3   | 8   |     | 20  10  |     | 10  |     | 156%  |
| ------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ----- |
PM3:  Cycle Time-Investigation  208  165  201  206  183  189  -9%
| ***Pending Cases at HQIU  |     | 64  |     | x   | x   |     | x  x  |     | 81  |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Transmittals to Attorney General (AG)
|     | FY 23/24  |     |     |     | Fiscal Year 24/25  |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Year  →  Year
Target:  540 Days
|                    |     |      |            | Q1  | Q2                     | Q3  | Q4         |      |     | Change  |       |
| ------------------ | --- | ---- | ---------- | --- | ---------------------- | --- | ---------- | ---- | --- | ------- | ----- |
|                    |     | YTD  |            |     |                        |     |            | YTD  |     |         |       |
|                    |     |      | Jul - Sep  |     | Oct  - Dec  Jan - Mar  |     | Apr - Jun  |      |     |         |       |
| PM4: Volume        |     | 26   |            | 5   | 3                      |     | 5  11      |      | 24  |         | -8%   |
| PM4a: Intake Only  |     | 24   |            | 8   | 7                      |     | 3  15      |      | 8   |         | -66%  |
PM4b:  Investigation Only  787  567  429  475  307  445  -44%
| PM4c:  Pre-AG Transmittal  |     | 15  |     | 8   | 1   |     | 1  0  |     | 2   |     | -84%  |
| -------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
PM4d:  Post-AG Transmittal  373  398  624  256  537  454  22%
| PM4: Cycle Time-AG       |     | 1198  |     | 980  | 1060  | 735  | 1043  |     | 955  |     | -20%  |
| ------------------------ | --- | ----- | --- | ---- | ----- | ---- | ----- | --- | ---- | --- | ----- |
| ***Pending Cases at AGO  |     | 18    |     | x    | x     |      | x  x  |     | 24   |     |       |
Actions
|                                 | FY 23/24  |      |            |     | Fiscal Year 24/25      |     |            |      |     | Year  →  Year  |       |
| ------------------------------- | --------- | ---- | ---------- | --- | ---------------------- | --- | ---------- | ---- | --- | -------------- | ----- |
|                                 |           |      |            | Q1  | Q2                     | Q3  | Q4         |      |     |                |       |
|                                 |           | YTD  |            |     |                        |     |            | YTD  |     | Change         |       |
|                                 |           |      | Jul - Sep  |     | Oct  - Dec  Jan - Mar  |     | Apr - Jun  |      |     |                |       |
| PC 23 Ordered                   |           | 0    |            | 0   | 0                      |     | 0  0       |      | 0   |                | 0%    |
| ISO-Interim Suspension Order    |           | 0    |            | 0   | 3                      |     | 1  0       |      | 4   |                | 400%  |
| ASO-Automatic Suspension Order  |           | 0    |            | 0   | 0                      |     | 0  0       |      | 0   |                | 0%    |
Accusations/Amed Accusations Filed  19  1  3  4  6  14  -26%
| Accusation and Petition to Revoke  |     | 1   |     | 0   | 0   |     | 0  1  |     | 1   |     | 0%    |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
| Citations                          |     | 9   |     | 1   | 0   |     | 2  2  |     | 5   |     | -44%  |
| PR/PLR                             |     | 13  |     | 1   | 1   |     | 0  2  |     | 4   |     | -69%  |
| Probation                          |     | 11  |     | 1   | 2   |     | 4  3  |     | 10  |     | -9%   |
| Surrender                          |     | 2   |     | 0   | 2   |     | 0  0  |     | 2   |     | 0%    |

Osteopathic Medical Board of CA
13 (A) Attachment
Enforcement Performance Measures Q1 Q2 Q3 Q4
Revocation 2 0 1 0 2 3 50%
PM1: Complaint Intake- Complaints and Convictions Received
PM2: Cycle Time - Intake - Average number of days from the date the complaint was received to the date the complaint was closed or
assigned for investigation (assigned to staff).
PM3: Cycle Time - Investigations - Average number of days to complete the entire enforcement process for complaints not transmitted to
the AG for formal discipline. (includes intake and investigation days)
PM3a: Intake Only - Of the cases included in PM3, the average number of days from the date the complaint was received to the date the
complaint was assigned for investigation.
PM3b: Investigation Only - Of the cases included in PM3, the average number of days from the date the complaint was assigned for
investigation to the date the investigation was completed. (without intake)
PM3c: Post Investigation Only -Of the cases included in PM3, the average number of days from the date the investigation was completed
to the date of the case outcome or non-AG formal discipline effective date.
PM4:Cycle Time-AG Transmittal - Average number of days to complete the enforcement process for cases investigated and transmitted to
the AG for formal discipline. (includes intake & investigation to final outcome of cases transmitted to the AG - includes withdraws, dismissals,
etc.)
PM4a: AG Transmittal - Intake Only - Of the cases included in PM4, the average number of days from the date the complaint was received
to the date the complaint was assigned for investigation.
PM4b: AG Transmittal - Investigation Only - Of the cases in PM4, the average number of days from the date the complaint was assigned
for investigation to the date the investigation was completed.
PM4c: AG Transmittal - Pre AG Transmittal - Of the cases in PM4, the average number of days from the date the investigation was
completed to the date the case was transmitted to the AG.
PM4d: AG Transmittal - Post AG Transmittal - Of the cases in PM4, the average number of days from the date the case is transmitted to
the AG to the date of the case outcome or formal discipline effective date. (AG days only)

---

**[MINUTES] 2025-08-14_20250814_item_14.pdf**

Osteopathic Medical Board of California

Agenda Item 14

DATE REPORT ISSUED:

August 14, 2025

ATTENTION:
SUBJECT:

Members, Osteopathic Medical Board of California
Executive Report

STAFF CONTACT:

Ralph Correa, Probation Monitor

REQUESTED ACTION:
This report is intended to provide the Members of the Osteopathic Medical Board
of  California  (OMBC)  with  an  update  on  the  probation  program.  No  action  is
needed.

Total Numbers of physicians on probation

As of today’s date, there are 38 licensees on active probation.

5  are  tolling  out  of  state  and  are  not  receiving  credit  towards  completion  of
probation.

1 licensee have received Interim Orders pending disciplinary action.

Review of cases

Quarterly reviews are being conducted, all information and documents are being
recorded  and  documented  in  a  full  report.  As  a  result,  all  probationers  have
received  a  quarterly  review  to  discuss  their  specific  terms  and  conditions.  The
Osteopathic  Medical  Board’s  Probation  unit  has  maintained  an  effective  and
thorough accountability of our physicians on probation.

Non-Compliance

Two  cease  practice  orders  have  been  placed  on  licensees  and  will  remain  in
effect until compliance is met and or a petition for revocation is completed.

---

**[MINUTES] 2025-08-14_20250814_item_15.pdf**

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM, GOVERNOR
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD
OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov
DATE August 14, 2025
TO OMBC Board Members
FROM Terri Thorfinnson, J.D.
Administrative Services Program Manager
RE: Agenda Item- 15 Rulemaking Update – 2025 Rulemaking for Pending or
Proposed Regulations
Rulemaking Update Summary
Three regulatory packages are moving along in the rulemaking process. The CME/Audit and Cite and Fine
package was approved by the Office of Administrative Law (OAL) July 10, 2025. By law rulemaking does
not become effective upon approval of OAL, rather rulemaking becomes effective quarterly based on the
date approved. The CME and Audits and Cite and Fine rulemaking will become effective October 1, 2025.
This rulemaking package is completed.
The Fees and License Status rulemaking documents are still pending review within DCA. Budgets and
Regulator staff must sign-off and then it goes to the DCA Director for review and approval. The Board must
receive approval from DCA and Agency before it can be submitted to OAL for post for 45-day comment
period. July 10, 2025, Board staff was notified of the need for additional revisions to the already Board
approved language. The Board will be reviewing these revisions at this meeting. DCA budget staff has not
signed off, so we are still waiting for their approval in order to proceed to the next step of regulatory
counsel review prior to submitting to DCA Director and Agency for approval to submit to OAL. This first
submission to OAL starts the one-year regulatory clock during which the Board must complete the
regulatory process and receive approval, appeal for additional time or start over. This first submission is
when the Board receives permission to proceed to public comment.
The Disciplinary Guidelines are in the initial stages. Preliminary draft of the proposed language was
reviewed by Regulatory Counsel and that draft is being reviewed and revised. It is anticipated that more
input and revisions will be made over the summer and fall in preparation for the Board to review in the
November board meeting 2025. The Board staff is trying to anticipate as many of the changes needed
upfront before the Enforcement Committee and Board review it. This is another large rulemaking package
that is complex because it is creating a new Disciplinary Guidelines document that has not been amended
since 1996. Since Rebecca Marcos gracefully resumed retirement, I have become involved in both the
Licensing and Fees as well as the Disciplinary Guidelines rulemaking working closely with Erika.
1

Rulemaking Status: Continuing Medical Education and Cite and Fines
Concept/ DCA pre-review Board approval Draft DCA Agency DOF Filing
Draft of Language Regulatory Director Approval Approval regulatory
language documents/ Approval package
review with OAL
9.22.2018 3/5/18, 5/25/22, 5/16/19,1/14/21, 6/4/24, October approved approved Submitted
6/29/23,9/19/23, 1/19/23,8/17/23, 9/11/24 2024 and
6/4/24,9/11/24 8/15/24 approved
to release
for
comments
45-day Board Respond Final review with Submit to OAL Effective
comment to comments Regulatory DCA approval Date
period Attorney Director, or denial
OAL for
approval
Completed Board review/ 5.7.2025 from 5.19.205 July 10, October
January approval Regulatory to Director, 2025. 1, 2025
8th, 2025 2/13/2025 Attorney, 5.21.2025 OAL
Board meeting
Director posted
Approval. 7.18.2025
5.29.2025
Budget to
DOF.
Submission
to OAL
5.29.2025.
DOF
approval
7.1.205
2

Rulemaking Status: Fees and License Status

Concept/  DCA pre-review   Board  Draft  DCA   Agency  DOF   Filing
Draft  approval  Regulatory  Director   Approval   Approval   regulatory
| language   |     | of   | documents/  | Approval   |     |     | package with  |
| ---------- | --- | ---- | ----------- | ---------- | --- | --- | ------------- |
Language
|     |     |     | review   |     |     |     | OAL   |
| --- | --- | --- | -------- | --- | --- | --- | ----- |
1/1/2024   2/1/24,2/15/24   8/15/2024   8/16/2024,
2/28/24, 4/12/24,   7/8/2025, budget
4/12/24,5/9/24,   approval pending
6/5/24,7/10/24,
7/22/24, 7/26/24
45-day  Board Respond to  Final  Submit to DCA  OAL  Effective
comment   comments  review with  Director, OAL  approval  Date
| period   |     | Regulatory   |                |             |     |     |     |
| -------- | --- | ------------ | -------------- | ----------- | --- | --- | --- |
|          |     |              | for approval   | or denial   |     |     |     |
Attorney

Rulemaking Status: Disciplinary Guidelines

Concept/Draft  DCA Pre- Board  Draft  DCA  Agency  DOF  Filing
language  Review  Approval  Regulatory  Director  Approval  Approval  Regulatory
|            |           | of        | Documents  | Approval  |     |     | package   |
| ---------- | --------- | --------- | ---------- | --------- | --- | --- | --------- |
|            |           | Language  | Review     |           |     |     | with OAL  |
| 1/31/2020  | 9/19/23,  |           |            |           |     |     |           |
10/9/2023,
11/16/23,
3/8/2024,
4/16/24.
pending
| 45 Day Comment  | Board     | Final       | Submit to  | OAL        | Effective  |     |     |
| --------------- | --------- | ----------- | ---------- | ---------- | ---------- | --- | --- |
| Period          | Approved  | Review      | DCA        | Approval   | Date       |     |     |
|                 | Response  | with        | Director,  | or Denial  |            |     |     |
|                 | to        | Regulatory  | OAL        |            |            |     |     |
|                 | Comments  | Attorney    |            |            |            |     |     |

3

---

**[MINUTES] 2025-08-14_20250814_item_16.pdf**

Agenda Item 16
Discussion and Possible Action to Reconsider Previously Approved Text, and to Consider
Initiation of a Rulemaking to Amend Sections 1609, 1610; 1611, 1612, 1613, 1615, 1628,
1630, 1637, 1646, 1647, 1650, 1651, 1656, 1658, 1678,and 1690, and to adopt Section
1648, and to repeal Section 1691 in Division 16 of Title 16 of the California Code of
Regulations (Applications, Petitions, Fees, Retired License and Processing Times)
CONTENTS OF AGENDA ITEM 16
• Application, Retired License and Fees Memo (pp. 3-6)
• Revised Proposed Rulemaking Text (pp. 8-25)
• Attachment 2: Repealed Physician and Surgeon Application (pp. 27-30)
• Attachment 3: Petition for Penalty Relief Application OMB.7 Form (pp. 32-34)
• Attachment 4: Application for Retired License OMB.31 Form (pp. 36-37)
• Attachment 5: Application to Retired Restore Application OMB. 32 Form (pp. 39-40)
• Attachment 6: OMBC Fees Updated Workload Costs Analysis (pp. 42-48)

Agenda Item 16
Applications, License,
& Fees
Rulemaking Memo
August 14, 2025
Board Meeting

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY • GAVIN NEWSOM, GOVERNOR
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390 | F (916) 928-8392 | www.ombc.ca.gov
DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
DATE August 14, 2025
TO Board Members, Osteopathic Medical Board of California
Terri Thorfinnson, J.D.
FROM
Legislative and Regulatory Specialist
Agenda Item 16 - Discussion and Possible Action to Reconsider Previously
Approved Text, and to Consider Initiation of a Rulemaking to Amend Sections
1609, 1610; 1611, 1612, 1613, 1615, 1628, 1630, 1637, 1646, 1647, 1650, 1651,
RE:
1656, 1658, 1678,and 1690, and to adopt Section 1648, and to repeal Section
1691 in Division 16 of Title 16 of the California Code of Regulations
(Applications, Petitions, Fees, Retired License and Processing Times)
Background and Statement of the Issues: The Board reviewed and approved the
proposed rulemaking language for Applications, Petitions, Fees, Retired License and
Processing Times last August 15, 2024rulemaking. The August 15, 2024, rulemaking
meeting materials the board reviewed and approved are available at this link
https://www.ombc.ca.gov/activity/20240815_item_14.pdf. Last month the Board was
notified of further recommended changes from the DCA Budget Office and Regulations
Counsel related to the Board’s currently proposed fee language. Upon review, it appears
that the prior text did not cover all the Board’s existing authority to set fees and does not
accurately reflect the terminology used in Business and Professions Code sections 2455
and 2455.1.
Proposed changes to subsections (d) and (f) and the “Note” for title 16, California Code of
Regulations (CCR) section 1690 would correct the terminology errors and authority
references. The only new fee item that would be added to the Board’s current fee
schedule is new subsection (g), the “Delinquent Inactive Biennial License or Renewal
Fee,” which is proposed to be set at half the inactive certificate fee in accordance with
Business and Professions Code sections 2455(c) and (d).
In addition, as provided below, Regulations Counsel recommends an additional change
that would more specifically describe how an applicant would electronically upload their
photograph as part of their electronic initial license application in CCR section 1613.
Finally, all forms incorporated by reference in this proposal have been given a new
revision date of 08/2025 to reflect the date deliberate and acted on this proposal. These
issues have been addressed with this revised proposed rulemaking language. The
proposed regulatory language is included in Attachments 1-5.

As a reminder, the Board is projecting to need fee increases to its statutory caps to meet
increased workload and staffing in the future. So, any proposed fee increases in this
proposal, which are highlighted through use of underline in the proposed text below, will
address the current budget imbalance only in the short term.
Requested Changes to Proposed Language: The specific revisions for the Board
to review and consider are highlighted in yellow below. The rest of the unhighlighted
language was already approved by the Board at the August 15, 2024, Board meeting.
Staff and Regulations Counsel recommend the following additional edits to existing
language for these sections.
I. Additional Revisions to Title 16, California Code of Regulations (CCR), § 1690
§ 1690. Fees.
The nonrefundable fees charged by the Board are as follows:
(a)Physician and surgeon's original or reciprocity certificate application fee: $200$400
($100 shall be returned if applicant's credentials are insufficient).
(b)Physician and surgeon's reciprocity certificate application fee: $200 ($100 shall be
returned if applicant's credentials are insufficient).
1
(c)(b) Physician and surgeon's postgraduate training license non-refundable application
and processing fee: $491.
(d)(c) Duplicate certificate, name change, certification endorsement fee: $25.
(e)(d) Biennial License or Renewal fee: $400.
(f)(e) Biennial Inactive Certificate fee: $300$399.
(g)(f) Delinquent Active Biennial License or Renewal fee: $100$200.
(g) Delinquent Inactive Biennial License or Renewal fee: $199.50.
(h)Fictitious Name Permit fee: $100; Renewal fee: $50.
(i)Retired License fee: $200.
(j)Application to Restore Retired License to Active Status $400.
OMBC August 14, 2025 Board Meeting – Agenda Item 16 Page | 2

(k)Petition for Reinstatement application fee: $2800.
(l)Petition for Modification of Penalty application fee: $1500.
NOTE: Authority cited: Osteopathic Act (Initiative Measure, Stats. 1923, p. xciii), Section
1; and Sections 2018, 2064.5,2307.5, 2452, 2456.1 and 3600-1, Business and Professions
Code. Reference: Sections 2064.5, 2307.5, 2452, 2451, and2455, 2456, 2456.1 and
2456.2, Business and Professions Code.
II. Revisions to Title 16, California Code of Regulations (CCR), Section 1613. Photo and
Fingerprint Requirements.
(a)Photos. Two (2) photographs shall be submitted to the Board along with the
application by electronically uploading a copy of the photo as an electronic file
attachment through the Board’s online portal referenced in Section 1610 using
acceptable formats. “Acceptable formats” shall mean one of the following file
formats: .txt, .csv, .gif, .bmp, .tif, .tiff, .pdf, .doc, .docx, .rtf, .jpg, .jpeg, .jpe, .xls, .xlsx,
.msg, .xps, .docm, .htm, .html, .wpd, .wps, .odt, .png, .wma, .wav, or .mp3. They should
be approximately 32″ x 42″ and taken within the last sixty (60) days (head and shoulders).
Proof photos or negatives are not acceptable. All photos shall be signed by the applicant
across the base of the photo.
III. Future revisions to comply with newly approved regulations October 1, 2025.
As a reminder, there will need to be future revisions to conform to the text proposed in
this item to conform with the newly implemented CME and Audit and Cite and Fine
rulemaking changes that go into effect October 1, 2025. All changes required to conform
effective October 1, 2025, will be made as part of this rulemaking process and will not
need additional Board approval, but will be noted in the rulemaking documents. One
such example is § 1646; the current and proposed language is different than the yet to
become effective language.
Attachments:
• Attachment 1: Proposed Regulatory Language
• Attachment 2: Repeal of Form “Application for Physician’s and Surgeon’s
Certificate” OMB.1 Rev.01/92
• Attachment 3: Adoption of Form “Petition for Penalty Relief OMB.7 (New 08/2025)
• Attachment 4: Adoption of Form “Application for Retired License OMB.31 (New
08/2025)”
OMBC August 14, 2025 Board Meeting – Agenda Item 16 Page | 3

• Attachment 5: Adoption of Form “Application to Restore Retired License to Active
Status OMB.32 (New 08/2025)”
• Attachment 6: Fiscal Impact Workload Costs (Tables) for: (A) Physician and
Surgeon Original or Reciprocity Application Fee, (B) Physician and Surgeon
Biennial License or Renewal Active Fee; (C) Physician and Surgeon Biennial
Inactive Certificate Fee, (D) Physician and Surgeon Retired License Status, (E)
Physician and Surgeon Application to Restore Retired License to Active, (F)
Petition for Reinstatement, and (G) Petitions for Modification of Penalty.
Action Requested: The Board should review the proposed regulatory text and consider
whether they would support it as written or if there are suggested changes to the
proposed text. After review, the staff requests that the Board consider one of the
following motions:
Motion A: (The Board has no suggested changes for the proposed regulatory text.)
Approve the proposed regulatory text for 16 CCR sections 1609, 1610; 1611,
1612, 1613, 1615, 1628, 1630, 1637, 1646, 1647, 1648, 1650, 1651, 1656, 1658, 1678,
and 1690, and to repeal CCR section 1691 in Attachments 1-5 and to submit the text to the
Director of the Department of Consumer Affairs and the Business, Consumer Services,
and Housing Agency for review and if no adverse comments are received,
authorize the Executive Director to take all steps necessary to initiate the
rulemaking process, make any non-substantive changes to the text and the
package and set the matter for a hearing if requested. If after the 45-day
public comment period, no adverse comments are received, and no public
hearing is requested, authorize the Executive Director to take all steps necessary
to complete the rulemaking, and adopt the proposed regulations as noticed.
Motion B: (The Board has suggested changes for the proposed regulatory text.)
Approve the proposed regulatory text for 16 CCR sections 1609, 1610; 1611,
1612, 1613, 1615, 1628, 1630, 1637, 1646, 1647, 1648, 1650, 1651, 1656, 1658, 1678,
and 1690, and to repeal CCR section 1691 in Attachments 1-5, with the following changes.
(Describe the proposed changes to the noticed proposed text). In addition,
submit the text to the Director of the Department of Consumer Affairs and the
Business, Consumer Services, and Housing Agency for review and if no adverse
comments are received, authorize the Executive Director to take all steps
necessary to initiate the rulemaking process, make any non-substantive
changes to the text and the package, and set the matter for a hearing if
requested. If after the 45-day public comment period, no adverse comments
are received, and no public hearing is requested, authorize the Executive
Director to take all steps necessary to complete the rulemaking, and adopt the
proposed regulations as noticed.
OMBC August 14, 2025 Board Meeting – Agenda Item 16 Page | 4

Agenda Item 16 Attachment 1
Revised Proposed
Rulemaking Text
August 14, 2025
Board Meeting

DEPARTMENT OF CONSUMER AFFAIRS
Title 16. OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
PROPOSED REGULATORY LANGUAGE
Applications, Fees and Retired License
The amendment format is as follows: Existing language remains unchanged; proposed
additions to regulation text and of new text are indicated in single underline and single
strikethrough for deletions.
The Osteopathic Medical Board of California hereby proposes to amend its regulations
in Sections 1609 of Article 3, 1610, 1611, 1612 and 1613 of Article 4; 1615 of Article 5,
1628 of Article 7, 1630 of Article 8, 1637 of Article 9, 1646 and 1647 of Article 10, 1650
and 1651 of Article 11, 1656 and 1658 of Article 12; 1678 of Article 14, Section 1690 of
Article 17; and to adopt Section 1648 of Article 10; and, to repeal Section 1691 of Article
17 of Division 16 of Title 16 of the California Code of Regulations to read as follows:
Article 3. Postgraduate Training
§ 1609. Postgraduate Registration.
In order to engage in the practice of medicine for a limited period as part of an approved
postgraduate training program any graduate student upon whom a degree of Doctor of
Osteopathy (D.O.) has been conferred by a school approved by the Board, shall apply
for registration (Postgraduate Training Registration OMB.3 Rev.01/92)

*[document truncated for length]*

---

**[MINUTES] 2025-08-14_20250814_item_17.pdf**

Osteopathic  Medical Board  of California
Agenda Item #17    Bill Status List August 2025
Bills With Board Positions
| Bill No.   | Author   | Subject   | Status   | Position   |
| ---------- | -------- | --------- | -------- | ---------- |
AB 54   Krell   Access Safe  Abortions  Act:   Senate  Support
|     |     | Protects  Medical Abortions     | Appropriations   |     |
| --- | --- | ------------------------------- | ---------------- | --- |
|     |     | and  prohibits  criminal  and   | Committee        |     |
civil penalties  related  to
providing  abortion.
|          |                | Sexual and  Reproductive        |                  | Support   |
| -------- | -------------- | ------------------------------- | ---------------- | --------- |
| AB 260   | Aguiar-Curry   |                                 | Senate           |           |
|          |                | Health  Care.  Makes  changes   | Appropriations   |           |
|          |                | that protect reproductive       | Committee        |           |
health  care  services.
|     | Papan   | Menopause  Survey.   | Held  Under  | Support   |
| --- | ------- | -------------------- | ------------ | --------- |
AB 360
Submission- 2-
year bill
AB 432   Bauer-Kahan   Mandatory  CME:   Senate Health   Support
|     |     | Menopause  and Insurance   | Committee   |     |
| --- | --- | -------------------------- | ----------- | --- |
Coverage  for menopause
treatment.
| AB 742   | Elhawary   | Expedite License                  | Senate           | Support   |
| -------- | ---------- | --------------------------------- | ---------------- | --------- |
|          |            | Applications  for                 | Appropriations   |           |
|          |            | Descendants  of Slaves.           | Committee        |           |
| AB 489   | Bonta      | AI:  Health  Care                 | Senate           | Support   |
|          |            | Professionals:  deceptive         | Appropriations   |           |
|          |            | terms  or letters  and  posting   | Committee        |           |
as  professionals
AB 667   Solache   Interpreters  paid by  Board:   Senate  Oppose  Unless
|     |     | Exams  and  Application.   | Appropriations   | Amended   |
| --- | --- | -------------------------- | ---------------- | --------- |
Committee
1

Note: no  longer  applies  to
OMBC.
AB 876   Flora   Nurse  Anesthetists  Scope  of  Senate  Oppose
|     |     | Practice  Expansion.   | Appropriations   |     |
| --- | --- | ---------------------- | ---------------- | --- |
Committee
AB 1215   Flora   Hospital Membership:  Peer  2-year bill   Oppose
|     |     | Review,  Assessment   | Assembly       |     |
| --- | --- | --------------------- | -------------- | --- |
|     |     | Expansion of Non-     | Business and   |     |
|     |     | Physicians.           | Professions    |     |
Committee
SB 508   Valladares   Telemedicine  License   Assembly   Oppose
|     |     | Exemption  Expansion   | Business and   |     |
| --- | --- | ---------------------- | -------------- | --- |
Professions
Committee
|     | Ashby   | States  of  Emergency:      | Assembly          | Support   |
| --- | ------- | --------------------------- | ----------------- | --------- |
|     |         | Waivers  and  Exemptions:   | Appropriations    |           |
SB 641
Delegation of Authority  to
|     |     |     | Committee.  |     |
| --- | --- | --- | ----------- | --- |
Boards.
|     |     |     | Consent  |     |
| --- | --- | --- | -------- | --- |
Calendar
AB 460   Chen   Radiologic  Technologists:   Senate  Oppose
|     |     | direct  supervision:   | Appropriations    |     |
| --- | --- | ---------------------- | ----------------- | --- |
|     |     | telemedicine           | Committee         |     |
AB 967   Valencia   Physicians  and  Surgeons:   2-year bill   Oppose
Licensure: Expedited  Fee.

WATCH LIST BILLS
| AB 50   | Bonta   | Pharmacists:  Furnishing   | Senate            | Watch   |
| ------- | ------- | -------------------------- | ----------------- | ------- |
|         |         | Contraceptives             | Appropriations    |         |
Committee
AB 346   Nguyen   In-Home  Support  Services:   Senate  Watch
|     |     | Licensed  Health  Care         | Appropriations    |     |
| --- | --- | ------------------------------ | ----------------- | --- |
|     |     | Professionals  Certification   | Committee         |     |
AB 408   Berman   Physician  Health  and   Senate  Judiciary   Watch
|     |     | Wellness Program  (MBC   | Committee   |     |
| --- | --- | ------------------------ | ----------- | --- |
sponsored)
| AB 447   | Gonzalez   | Emergency  Room  (ER)   | Senate           | Watch   |
| -------- | ---------- | ----------------------- | ---------------- | ------- |
|          |            | Patient Prescriptions   | Appropriations   |         |
Committee,
Consent
Calendar
2

AB 479   Tangipa   Criminal Procedure:  Vacatur  2-year bill   Watch
Relief:  Findings  of  Harm.
| AB 485   | Ortega   | Labor Commissioner:      | Senate            | Watch   |
| -------- | -------- | ------------------------ | ----------------- | ------- |
|          |          | Unsatisfied Judgments:   | Appropriations    |         |
|          |          | Nonpayment of  Wages.    | Committee         |         |

AB 511   Chen   Radiologist  Assistants:  Scope   Held  Under  Watch
|          |           | of  Practice:  Supervision.   | Submission   |         |
| -------- | --------- | ----------------------------- | ------------ | ------- |
| SB 679   | Weber-    | Requires  Health              | Held  Under  | Watch   |
|          | Pierson   | Facilities/Peer  Review       | Submission   |         |
Committees  805 Reporting
to  Include  Race  and Gender.
AB 1037   Elhawary   Public  Health:  Overdose   Senate  Watch
|     |     | Treatment by  Non- | Appropriations    |     |
| --- | --- | ------------------ | ----------------- | --- |
|     |     | Physicians.        | Committee         |     |
AB 1186   Patel   Data Collection:  Race  and   Held  Under  Watch
|     |     | Ethnicity:  Minimum  Data   | Submission.   |     |
| --- | --- | --------------------------- | ------------- | --- |
Categories.
|           | Berman   | P.A.  Scope of  Practice: Direct   |                   | Watch   |
| --------- | -------- | ---------------------------------- | ----------------- | ------- |
| AB 1501   |          |                                    | Senate            |         |
|           |          | Supervision  by  Physician         | Appropriations    |         |
|           |          | from 4 to 8 P.A.s.                 | Committee         |         |
|           | Rubio    | Residency Accreditation            | Assembly          | Watch   |
SB 387
|     |     | Eligibility:  Faculty  Permit.   | Appropriations   |     |
| --- | --- | -------------------------------- | ---------------- | --- |
Committee.
Consent
Calendar.
| SB 470   | Laird     | Bagley-Keene Open                 | Assembly         | Watch   |
| -------- | --------- | --------------------------------- | ---------------- | ------- |
|          |           | Meetings  Act: Extending          | Appropriations   |         |
|          |           | Hybrid Teleconferencing.          | Committee.       |         |
| SB 518   | Weber-    | Descendants  of Enslaved          | Assembly         | Watch   |
|          | Pierson   | Persons: Reparations:             | Appropriations   |         |
|          |           | Certification  of  Descendants.   | Committee.       |         |

3

---

**[MINUTES] 2025-08-14_20250814_minutes.pdf**

MEMBERS
PRESENT:

STAFF
PRESENT:

BUSINESS, CONSUMER SERVICES AND HOUSING AGENCY   •   GAVIN NEWSOM, GOVERNOR

DEPARTMENT OF CONSUMER AFFAIRS • OSTEOPATHIC MEDICAL BOARD OF CALIFORNIA
1300 National Drive, Suite 150, Sacramento, CA 95834
P (916) 928-8390    |    F (916) 928-8392    |    www.ombc.ca.gov

Osteopathic Medical Board of California

 Teleconference Minutes

August 14, 2025

Denise Pines, MBA, President
Hemesh Patel, D.O., Vice President
Gor Adamyan, Secretary
John M. Cummins, J.D.
Andrew Moreno, Esq.
Brett Lockman, D.O.
Matthew Swain, D.O.

Erika Calderon, Executive Director
Machiko Chong, Licensing Program Manager
Cristy Livramento, Enforcement Program Manager
Terri Thorfinnson, Legislative and Regulatory Specialist
Ralph Correa, Probation Monitor
Beth Clark, Associate Governmental Program Analyst
Yuping Lin, Board Counsel
Arthur Babakhan, OIO Manager, Department of Consumer Affairs
Kalia Van Lint, Budget Analyst, DCA Budget Office
Julia E. Cox, Administrative Law Judge, OAH
Christopher Young, Deputy Attorney General
Maryam Ahmad, Deputy Attorney General
Kaila Vanlint, DCA Budget Analyst
Nicole Dragu, DCA Budget

MEMBERS OF
THE AUDIENCE:

Chris, Student Government President
David, Student Governing Body
Darra, OMS II
Arnold Kim, OMS II
Cameron Quill, OMS II
Holly Macriss, Executive Director, OPSC
Michelle Monserratt-Ramos, Consumer Watchdog
Maria Ibarra-Navarrette, Consumer Watchdog
Tracy Dominguez, Consumer Watchdog

Board Meeting Minutes – August 14, 2025

Agenda Item 1

Call to Order and Roll Call/Establishment of a Quorum

The Board Meeting of the Osteopathic Medical Board of California (OMBC) was called
to order by Madame President Denise Pines at 09:03 a.m.

Machiko Chong called roll and determined a quorum was present. The meeting was
held at Touro University College of Osteopathic Medicine. Board guidelines for
conducting the meeting under the Open Meetings Act were reviewed, including rules for
public comment and remote board member visibility.

Agenda Item 2

Reading of the Board’s Mission Statement

Executive Director Erika Calderon read the Board’s mission statement: "to protect the
public by requiring competency, accountability, and integrity in the safe practice of
medicine by our osteopathic physicians and surgeons".

Agenda Item 3

Public Comment for Items not on the Agenda

President Denise Pines opened the floor for public comments on items not explicitly on
the agenda.

The host requested online comments; no public comments were made in the meeting
room or online.

Agenda Item 4 & 5

Petition for Early Termination of Probation

Administrative Law Judge (ALJ) Juliet E. Cox presided over two hearings for early
termination of probation petitions.

The Board was advised that deliberations and decisions would occur later in closed
session, and petitioners would receive written decisions.

Petition for Early Termination of Probation, Steven Duane Western, D.O.

The hearing opened for Dr. Western's petition for early termination of his four-
year probation, effective October 10, 2022.

Deputy Attorney General Christopher Young outlined the disciplinary order
stemming from allegations admitted by Dr. Western, including practicing
psychiatry on a family member (which he agreed constituted gross negligence)
and inadequate electronic health record (EHR) keeping (lacking BMI metrics). Dr.

Board Meeting Minutes – August 14, 2025

Western testified he has corrected all issues and would now refer complex
psychiatric cases to a psychiatrist. He noted he is in full compliance with all
probation terms. The Board took the matter under submission for closed session
deliberation.

Dr. Western was placed on four years of probation effective October 10, 2022,
and was petitioning for early termination after serving approximately three years.
Dr. Western stipulated that allegations in the accusation were deemed true,
correct, and fully admitted, with the exception of one paragraph regarding
Percocet prescription. The misconduct involved gross negligence related to
treating a family member (Patient A) for Dissociative Identity Disorder (DID) and
inadequate medical record keeping (lacking BMI index). Dr. Western agreed that
practicing psychiatry on a family member constituted gross negligence. He
affirmed he had corrected the issues and complied with all required probation
terms. The Attorney General’s office noted that the petitioner has the burden to
show rehabilitation by presenting clear and convincing evidence.

Petition for Early Termination of Probation, James Michael Lally, D.O.

The hearing opened for Dr. Lally's petition for early termination of his three-year
probation, which became final on July 31, 2023.

Deputy Attorney General Maryam Ahmad detailed the underlying allegations
admitted by Dr. Lally in the stipulated settlement, including sexual harassment,
gender and national origin discrimination, creating a hostile work environment,
misuse of his board position to intimidate residents, and failure to disclose
conflicts of interest while serving as a medical consultant. Dr. Lally testified he
separated from the hospital environment in 2018, completed ethics and civility
courses, and now lectures on safeguarding emotional stability for the
International Olympic Committee. Board member Dr. Patel questioned how the
board could ensure the protection of future medical professionals moving
forward. The AG noted that Dr. Lally appeared to still struggle with fully accepting
responsibility for his role in creating the hostile environment. The Board took the
matter under submission.

Pursuant to section 11126(c)(3) of the Government Code, the Board met in closed
session for discussion and to take action on disciplinary matters, including the above
petitions.

CLOSED SESSION

Board Meeting Minutes – August 14, 2025

Agenda Item 7

Review and Possible Approval of Minutes

Associate Governmental Program Analyst Beth Clark presented the minutes from the
February May 15, 2025, Teleconference Board Meeting.

Edits or corrections were identified after review:

Agenda Item 2: The mission statement should be corrected to read "osteopathic
physicians" (correcting "positions").

Agenda Item 15 (Legislation): The motion to support AB 489 (Prohibition of AI:
Deception use) was mistakenly referenced as AB 742 (Expedite License
Applications for Descendants of Slaves) on Page 11 of the draft minutes.

Motion to adopt the minutes as amended by the board members’
recommendations

Motion – Dr. Patel Second – Mr. Cummins
•  Aye – Mr. Adamyan, Mr. Cummins, Dr. Lockman, Mr. Moreno, Dr. Patel, Ms.

Pines, Dr. Swain

•  Nay – None
•  Abstention – None
•  Absent – None

Motion carried to approve the May 15, 2025 minutes as amended.

No public comments were made online or in the meeting room

Agenda Item 8

President’s Report

Madame President Denise Pines reported on the OMBC's activities:

Planning a "Hill Day" in January 2026 before the board meeting to meet with
legislators, share an overview of the DO profession, and build support for a future
bill to protect the DO name/identity.

Board Meeting Minutes – August 14, 2025

The Federation of State Medical Boards (FSMB) has convened a work group on
prescribing and dispensing trends, focusing on the growth of IV hydration and
ketamine clinics.

The FSMB is monitoring federal developments regarding telemedicine and
license portability.

The FSMB launched an Office of AI innovation.

The FSMB launched a digital campaign with three videos, viewed over 7 million
times, leading consumers to the website carematters.org for information on
medical boards.

Ms. Pines announced upcoming speaking engagements: September 3rd in
Dublin, Ireland, at the International Association of Medical Regulatory Authorities
(presenting guidance on medical racism and discrimination standards), and
September 25th at the Congressional Black Caucus Legislative Meeting (on
menopause and healthcare disparities)

.
No public comments were made online or in the meeting room.

Agenda Item 6
Answer Forum

Osteopathic Physician and Surgeon Student Question and

This item was addressed following the President's Report.

Five students from Toro University College of Osteopathic Medicine participated.

Addressing Mistakes:
Board members advised students to uphold humility, seek counsel, own up to
mistakes, and prioritize the patient over system demands (volume, machine
needs). Dr. Lockman referred to DOs as "MD+" and stressed using the
osteopathic structural exam to differentiate practice.

Protecting the DO Role:
Members strongly encouraged students to join professional organizations
(OPSC, AOA, OIA) to guide legislators and ensure their voice is heard.

Licensure:

Board Meeting Minutes – August 14, 2025

OMBC currently does not license international osteopaths; training must be
completed at a COCA-approved school in the United States.

Residency/Advocacy:
Students voiced concerns over federal policy shifts, medical school debt, and
residency spots.

Board members noted that residency funding is a national political question (CMS
policy). OMBC staff noted that awareness outreach helps increase patient demand for
DOs, which could open up residency opportunities. Board members encouraged
students to be active, advocate, and consider academic medicine (GME).

Agenda Item 9

Board Member Communications with Interested Parties

Madame President Denise Pines requested disclosures.

No board members had disclosures. No public comments were made online or in the
meeting room.

Agenda Item 10
Services Update

Intergovernmental Relations Reports and Administrative

DCA Update Arthur Babakhanyan, OIO Manager, reported that Governor Newsom’s
reorganization plan was enacted on July 5th, splitting the Business, Consumer Services
and Housing Agency.

New rules include:

•  The DCA will be housed in the new Business and Consumer Services Agency, effective

July 1, 2026.

•  The return-to-office requirement (four days in-office per week, per Executive Order N-22-

25) was postponed until July 1, 2026, due to labor union negotiations.

•  Out-of-state travel is restricted to "mission critical" needs and requires eight weeks'

advance notice to the DCA budget office.

•  Public comment: Holly Macriss (OPSC ED) requested that OMBC staff and leaders

continue to be allowed to travel to OPSC meetings to interact with DOs.

Budget Update Kalia Van Lint, Budget Analyst, reported the FY 2024-25 projected
ending balance is $4.61 million (11.9 months in reserve).

Board Meeting Minutes – August 14, 2025

The fund condition statement includes a conservative ongoing 3% interest
applied to expenditures to account for future personnel adjustments (salary,
retirement).

Agenda Item 11   Executive Director’s Report

Executive Director Erika Calderon provided personnel and administrative updates.

•  Personnel Updates: Public board members Gor Adamyan and John Cummins were

reappointed.

The board has hired a Special Investigator, Yvonne Nathad, scheduled to
start September 8, 2025. This position is projected to handle 60% of overall
field investigations and achieve a minimum cost savings of $150,000 per
fiscal year in DFI costs.

•  Subpoena Authority: OMBC is obtaining subpoena enforcement authority to handle

administrative record requests in-house.

•  Purge Project/Retention Schedule: The retention schedule was revised in July

2025.

The "purge project" addresses decades of backlog. Retention for a "quality of
care, no violation complaint involving patient death" was extended to five
years.

•  Budget Mitigation: OMBC projects an annual revenue increase of approximately
$694,000 from DFI cost savings ($150k), new CME/Cite and Fine regulations
($120k), and proposed fee increases (Applications/Petitions/Retired License)
($424k).

•  Outreach: The board is working on the 4th edition of the OsteoScope newsletter and

creating a consumer complaint video.

Due to budget constraints (mission critical t

*[document truncated for length]*
