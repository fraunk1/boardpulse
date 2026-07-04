You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Nebraska Board of Medicine and Surgery** (NE) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/NE/NE_MD#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-06-12]` — Nebraska Board of Medicine and Surgery — June 12, 2026
- `[2026-05-08]` — Nebraska Board of Medicine and Surgery — May 08, 2026
- `[2026-04-10]` — Nebraska Board of Medicine and Surgery — April 10, 2026
- `[2026-03-13]` — Nebraska Board of Medicine and Surgery — March 13, 2026
- `[2026-02-13]` — Nebraska Board of Medicine and Surgery — February 13, 2026
- `[2026-02-09]` — Nebraska Board of Medicine and Surgery — February 09, 2026
- `[2026-01-29]` — Nebraska Board of Medicine and Surgery — January 29, 2026
- `[2026-01-09]` — Nebraska Board of Medicine and Surgery — January 09, 2026

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: NE_MD
state: NE
---

# Nebraska Board of Medicine and Surgery — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Nebraska Board of Medicine and Surgery | [Minutes page](NE_MD_MINUTES_URL) |

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

Sources-table URL: https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx

## Meeting Minutes Data

Board: Nebraska Board of Medicine and Surgery
State: NE
Code: NE_MD

### 2026-06-12 — Nebraska Board of Medicine and Surgery — June 12, 2026

**[AGENDA] 2026-06-12_061226medagenda.pdf**

NOTICE OF MEETING OF THE
BOARD OF MEDICINE AND SURGERY
Date Posted June 1, 2026

       Hampton Inn & Suites
       Husker Conference Room
       7343 Husker Circle
       Lincoln, NE  68504-9816

Friday
June 12, 2026
9:00 am

This meeting will be held by WebEx conference and In-Person.  The public is welcome to attend any Open Session discussion
at the Hampton Inn & Suites.  A WebEx line has also been established for the public rather than visit the open meeting location.
If you wish to attend the meeting by WEBEX please let Jan Harris know by June 11, 2026 via email at janis.gadeken-
harris@nebraska.gov or you can join by using the below WebEx link:

https://sonvideo.webex.com/sonvideo/j.php?MTID=mcf2a2ee0ca49ca4e6160c368eb69b6de

or call in information is:  1-408-418-9388 using meeting number of:  2488 113 1471

Here is a link to the Open Meetings Act:

https://nebraskalegislature.gov/laws/display_html.php?begin_section=84-1407&end_section=84-1414

Here is a link to a copy of all the Open Session discussion items:

https://dhhs.ne.gov/licensure/Pages/Board-Meeting-Documents.aspx

For information, contact Jan Harris, Health Licensing Coordinator, at 402/471-2118, or Janis.Gadeken-Harris@nebraska.gov

1.  Roll Call

AGENDA

      Announcement:  There is a current copy of the Open Meetings Act posted near the door to the meeting room

2.  Adoption of Agenda

A.  Additions, Modification, Reordering and Adoption of Agenda
B.  Adoption of CONSENT Agenda(s)

(9A)  Physician and Osteopathic Physician Initial Application(s) (0) (CONSENT)
(9B)  Physician and Osteopathic Physician Reinstatement after Discipline Application(s) (0) (CONSENT)
(9C)  Physician and Osteopathic Physician Reinstatement Application(s) (0) (CONSENT)

     3.     Legislation Updates 2026
     4.     Regulations Updates
     5.    Approval of Minutes of the Meeting – May 8, 2026
     6.    Public Comments

7.     Investigational Reports – CLOSED SESSION pursuant to Neb. Rev. Stat. 38-1,105 (The Board will go into closed
session for the purpose of review and discussion of investigative reports, licensure applications, and other
confidential information, and for the prevention of needless injury to the reputation of the individuals).

(Approx. time to go into Closed Session: 9:30 am)

Investigation Cases

A.
B.    Compliance Monitoring Reports
C.    Proposed Agreed Settlement
D.    Discussion with Chief Medical Officer, Timothy Tesmer, MD

     8.

Application Review – CLOSED SESSION pursuant to Neb. Rev. Stat. 84-1410

     9.     Application Review – OPEN SESSION

(Approx. time to reconvene Open Session: 10:45 am)

     A.   Physician and Osteopathic Physician Initial Application(s) (0) (CONSENT)

                   B.   Physician and Osteopathic Physician Reinstatement after Discipline Application(s) (0) (CONSENT)
                   C.   Physician and Osteopathic Physician Reinstatement Application(s) (0) (CONSENT)
    10.  Email Ballot(s) since last meeting – ()
    11.     Discussion(s):

     A.  Letter to the Board regarding the Surgical First Assistant opinion from the Board on April 10, 2026
     B.  Ketamine use by a patient in therapy provided by a Licensed Mental Health Practitioner (LMHP)

    12.     Public Comments
    13.     Board of Medicine and Surgery 2026 Meeting Schedule – Next scheduled meeting August 14, 2026

***Board Break to allow for Hearing Room Setup***

     14.     Hearing before the Board of Medicne and Surgery – Daniel Martin Wik, MD – 12:00 Noon – OPEN SESSION CONT.

     15.     Hearing Review – CLOSED SESSION

     16.      Hearing Review – OPEN SESSION

     17.  Adjournment

***The Board will work through LUNCH***

All items known at time of distribution of this agenda are listed; a current agenda is available on the First Floor, State Office Building, 301
Centennial Mall South, Lincoln, Nebraska.

Notice: A tape recording of the meeting will be made for the purpose of preparing minutes of the meeting.  Said tape will not be transcribed but
will be available to the public until such time that the minutes of this meeting are approved by the Board.  In accordance with the records
retention schedule of the Licensure Unit as authorized by Nebraska Statute, the Division may dispose of the tapes ten (10) days after the
meeting; however, staff shall retain the tapes until the Board has approved the minutes.

Auxiliary aids or reasonable accommodations needed to participate in a meeting can be requested by calling (402) 471-2118.  Individuals who
are deaf or hard of hearing may call DHHS via the Nebraska Relay System at 711 or (800) 833-7352 TDD at least 2 weeks prior to the meeting.

---

**[MINUTES] 2026-06-12_061226medminutes.pdf**

THESE MINUTES HAVE NOT BEEN APPROVED BY THE BOARD OF MEDICINE AND SURGERY

NEBRASKA BOARD OF MEDICINE AND SURGERY

MEETING MINUTES
June 12, 2026

ROLL CALL

The meeting of the Board of Medicine and Surgery was called to order by Vice-Chairperson, Mark Goodman, MD,
at 9:05 a.m. on June 12, 2026, at the Hampton Inn & Suites, 7343 Husker Circle, Lincoln, Nebraska 68504.  The
meeting was conducted In-Person and by WebEx.  The following members answered the roll call:

Mark Goodman, MD, Vice-Chairperson
Jeffrey Howorth, Secretary
Rachel Blake, MD
Jodanne Hedrick, DO
Adam Kuenning, JD, LLM
John Massey, MD

Absent:

Brian Keegan, MD – (joined the meeting at 9:23am)
Wesley Zeger, DO, Chairperson

A quorum was present, and the meeting convened.

Also present to participate in the meeting: Vonda Apking, Program Manager and Jan Gadeken-Harris, Health
Licensing Coordinator with the Licensure Unit; Milissa Johnson-Wiles, Assistant Attorney General; Randy Clark,
Mark Meyerson and Hayle Alvarado, Investigators with the Investigation Unit; Ellie Rohr, DHHS Department
Attorney and Jeanette Peterson, RN, BSN with Compliance Monitoring.

Goodman announced that there is a copy of all the public documents being reviewed at this meeting available in
the meeting room pursuant to the Open Meetings Act.

In accordance with Neb. Rev. Stat. § 84-1411 of the Nebraska Open Meetings Act, copies of the agenda were e-
mailed to the Board members and other interested parties, posted on the DHHS web site at
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx and posted on the Bulletin Board at the entrance
to the Nebraska State Office Building June 1, 2026.

REVIEW OF AGENDA

Howorth moved, seconded by Hedrick, to approve adoption of the agenda with the Chair having the authority to
rearrange agenda items as needed.  Voting aye: Blake, Goodman, Hedrick, Howorth, Kuenning and Massey.
Voting nay: None.  Absent: Keegan, Zeger.  Abstain: None.  Motion carried.

ADOPTION OF THE APPLICATION(S) CONSENT AGENDA

There were no applications for review on the Consent Agenda for this meeting.

LEGISLATION UPDATES

Eric Sutton, JD, Director of Health Policy with the NMA (Nebraska Medical Association) was present via WebEx to
discuss and provide updates to the Board for the 109th Legislature.

LB527 - Adopt the Medicaid Access and Quality Act and change provisions relating to taxes on health
maintenance organizations, prepaid limited health service organizations, and insurance companies
To learn more, go to:  https://nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB527.pdf
The NMA is assisting with the implementation of this bill.

Currently there is a 407 Review that the NMA is supporting:
Credentialing Review (407) Certified Nurse Midwives – to learn more, go to:
https://dhhs.ne.gov/licensure/Pages/Credentialing-Review-(407)-Certified-Nurse-Midwives.aspx

Board of Medicine and Surgery
Minutes of the Meeting – June 12, 2026
Page 2

REGULATIONS UPDATE

LB 1212 - Provide for licensure of internationally trained physicians under the Uniform Credentialing Act and
change provisions of the Engineers and Architects Regulation Act
To learn more, go to:  https://nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB1212.pdf

Due to the passing of this Bill, the Regulations will need to be opened for updates.

APPROVAL OF MINUTES OF THE MEETING

Kuenning moved, seconded by Hedrick to approve May 8, 2026, meeting minutes as written.  Voting aye: Blake,
Goodman, Hedrick, Kuenning and Massey.  Voting nay: None.  Absent: Keegan, Zeger.  Abstain: Howorth.
Motion carried.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

INVESTIGATIONAL REPORTS, DISCIPLINARY REPORTS, APPLICATION REVIEW – CLOSED SESSION

Blake moved, seconded by Howorth, to go to closed session at 9:10 a.m. for the purpose of review and
discussion of investigative reports, disciplinary reports, licensure applications, and other confidential information,
and for the prevention of needless injury to the reputation of the individuals.  Voting aye: Blake, Goodman,
Hedrick, Howorth, Kuenning and Massey.  Voting nay: None.  Absent: Keegan, Zeger.  Abstain: None.  Motion
carried.

Dr. Keegan joined the meeting at 9:23 a.m.

Dr. Blake recused herself at 9:58 a.m.
Dr. Blake returned at 10:05 a.m.

Board Break 10:25 a.m.
Board Returned 10:45 a.m.

The Board members returned to Open Session at 10:55 a.m.

APPLICATION REVIEW – OPEN SESSION

BOARD RECOMMENDATIONS ON APPLICATIONS FOR LICENSURE AND REGISTRATION

There were no applications for review for this meeting.

EMAIL BALLOTS SINCE LAST MEETING

There were no Email Ballots to present for this meeting.

DISCUSSION(S)

A.  Letter to the Board regarding the Surgical First Assistant opinion from the Board of Medicine and Surgery
meeting on April 10, 2026.

It is the opinion of the Board that according to Nebraska Statutes closure of a surgical site needs the personal
supervision of the physician.

https://dhhs.ne.gov/licensure/Pages/Surgical-First-Assistant.aspx#docaccess-
ab6db8cff029471f549b84972078643d

Board of Medicine and Surgery
Minutes of the Meeting – June 12, 2026
Page 3

38-3508. Personal supervision by a physician, defined.
Personal supervision by a physician means the physical attendance of a physician in the room during the
performance of a surgical procedure.
Source: Laws 2016, LB721, § 8.

38-3511. Licensed surgical first assistant; activities authorized.
A licensed surgical first assistant may engage in the practice of surgical assisting, including, but not limited to, the
following:
(1) Assisting in the intraoperative care of a surgical patient;
(2) Positioning the patient;
(3) Preparing and draping the patient for the surgical procedure;
(4) Providing visualization of the operative site;
(5) Assisting with hemostasis;
(6) Assisting with closure of body planes, including the following:
(a) Inserting running or interrupted subcutaneous sutures with absorbable or nonabsorbable material;
(b) Utilizing subcuticular closure technique with or without adhesive skin closure strips; and
(c) Closing skin with method indicated by surgeon, including, but not limited to, suture and staples;
(7) Applying appropriate wound dressings;
(8) Providing assistance in securing drainage systems to tissue;
(9) Preparing specimens, such as grafts; and
(10) Performing other tasks during a surgical procedure delegated by and under the personal supervision of a
physician appropriate to the level of competence of the surgical first assistant.
Source: Laws 2016, LB721, § 11.

B.  Ketamine use by a patient in therapy provided by a Licensed Mental Health Provider (LMH)

It is the opinion of the Board that the use of Ketamine needs to be supervised by appropriate medical providers.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

BOARD MEETING SCHEDULE

The next meeting is scheduled for August 14, 2026, in the Husker Conference Room at the Hampton Inn &
Suites.  To see a complete list of the projected schedule for the 2026 schedule, visit the DHHS website:
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx

Board recess for Hearing Room setup at 11:00 a.m.
Board reconvened to Open Session at 12:07 p.m.

HEARING – OPEN SESSION

Daniel Martin Wik, MD requested a Hearing before the Board of Medicine and Surgery regarding his application
for removal of the limitations on his license to practice medicine and surgery.

Ellie Rohr, Department Attorney and Hearing Administrator requested that the Board go into Closed Session at
1:56 p.m. for discussion of the evidence that was presented at the Hearing.

The Board returned to Open Session at 2:17 p.m.

Kuenning moved, seconded by Hedrick to affirm the prior denial of the removal of the limitation on Dr. Wik’s
license.  Basis of the decision is due to lack of sufficient evidence to support the removal of the restriction.
Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning and Massey.  Voting nay: None.  Absent:
Zeger.  Abstain: None.  Motion carried.

Board of Medicine and Surgery
Minutes of the Meeting – June 12, 2026
Page 4

ADJOURNMENT

There being no further business, Goodman, Vice-Chairperson adjourned the meeting at 2:18 p.m.

Respectfully submitted,

*signature available upon request*

Jeffrey Howorth, Secretary
Board of Medicine and Surgery

---

### 2026-05-08 — Nebraska Board of Medicine and Surgery — May 08, 2026

**[AGENDA] 2026-05-08_050826medagenda.pdf**

NOTICE OF MEETING OF THE
BOARD OF MEDICINE AND SURGERY
Date Posted April 29, 2026
REVISED MAY 4, 2026

       Hampton Inn & Suites
       Husker Conference Room
       7343 Husker Circle
       Lincoln, NE  68504-9816

Friday
May 8, 2026
9:00 am

This meeting will be held by WebEx conference and In-Person.  The public is welcome to attend any Open Session discussion
at the Hampton Inn & Suites.  A WebEx line has also been established for the public rather than visit the open meeting location.
If you wish to attend the meeting by WEBEX please let Jan Harris know by May 7, 2026 via email at janis.gadeken-
harris@nebraska.gov or you can join by using the below WebEx link:

https://sonvideo.webex.com/sonvideo/j.php?MTID=mddaa7e62bb070dcd90c714345eb8255a

or call in information is:  1-408-418-9388 using meeting number of:  2498 498 2428

Here is a link to the Open Meetings Act:

https://nebraskalegislature.gov/laws/display_html.php?begin_section=84-1407&end_section=84-1414

Here is a link to a copy of all the Open Session discussion items:

https://dhhs.ne.gov/licensure/Pages/Board-Meeting-Documents.aspx

For information, contact Jan Harris, Health Licensing Coordinator, at 402/471-2118, or Janis.Gadeken-Harris@nebraska.gov

1.  Roll Call

AGENDA

      Announcement:  There is a current copy of the Open Meetings Act posted near the door to the meeting room

2.  Adoption of Agenda

A.  Additions, Modification, Reordering and Adoption of Agenda
B.  Adoption of CONSENT Agenda(s)

(9A)  Physician and Osteopathic Physician Initial Application(s) (0) (CONSENT)
(9B)  Physician and Osteopathic Physician Reinstatement after Discipline Application(s) (0) (CONSENT)
(9C)  Physician and Osteopathic Physician Reinstatement Application(s) (0) (CONSENT)

     3.     Legislation Updates
     4.     Regulations Updates
     5.    Approval of Minutes of the Meeting - April 10, 2026
     6.    Public Comments

7.     Investigational Reports – CLOSED SESSION pursuant to Neb. Rev. Stat. 38-1,105 (The Board will go into closed
session for the purpose of review and discussion of investigative reports, licensure applications, and other
confidential information, and for the prevention of needless injury to the reputation of the individuals).

(Approx. time to go into Closed Session: 9:30 am)

Investigation Cases

A.
B.    Compliance Monitoring Reports
C.    Proposed Agreed Settlement

     8.

Application Review – CLOSED SESSION pursuant to Neb. Rev. Stat. 84-1410

     9.     Application Review – OPEN SESSION

(Approx. time to reconvene Open Session: 10:45 am)

     A.   Physician and Osteopathic Physician Initial Application(s) (0) (CONSENT)

                   B.   Physician and Osteopathic Physician Reinstatement after Discipline Application(s) (0) (CONSENT)
                   C.   Physician and Osteopathic Physician Reinstatement Application(s) (0) (CONSENT)
    10.  Email Ballot(s) since last meeting – (1)

    11.     Discussion(s):

     A.  Low-Level Laser Therapy also called Red Light Therapy
     B.  Therapeutic Botox injections for pediatric spasticity
     C.  NP’s and PA’s Treating Pain Management

                   D.   AOA (American Osteopathic Association) Letter of Concern Regarding Patient Safety Issues

    12.  FSMB (Federation of State Medical Boards) Annual Meeting 4/30/2026 – 5/2/2026 in Baltimore, MD

       Updates from Dr. Hedrick, Dr. Blake and Dr. Massey

    13.     Public Comments
    14.     Board of Medicine and Surgery 2026 Meeting Schedule – Next scheduled meeting June 12, 2026
    15.  Adjournment

***The Board will work through LUNCH***

All items known at time of distribution of this agenda are listed; a current agenda is available on the First Floor, State Office Building, 301
Centennial Mall South, Lincoln, Nebraska.

Notice: A tape recording of the meeting will be made for the purpose of preparing minutes of the meeting.  Said tape will not be transcribed but
will be available to the public until such time that the minutes of this meeting are approved by the Board.  In accordance with the records
retention schedule of the Licensure Unit as authorized by Nebraska Statute, the Division may dispose of the tapes ten (10) days after the
meeting; however, staff shall retain the tapes until the Board has approved the minutes.

Auxiliary aids or reasonable accommodations needed to participate in a meeting can be requested by calling (402) 471-2118.  Individuals who
are deaf or hard of hearing may call DHHS via the Nebraska Relay System at 711 or (800) 833-7352 TDD at least 2 weeks prior to the meeting.

---

**[MINUTES] 2026-05-08_050826medminutes.pdf**

NEBRASKA BOARD OF MEDICINE AND SURGERY

MEETING MINUTES
May 8, 2026

ROLL CALL

The meeting of the Board of Medicine and Surgery was called to order by Chairperson, Wesley Zeger, DO, at
9:03 a.m. on May 8, 2026, at the Hampton Inn & Suites, 7343 Husker Circle, Lincoln, Nebraska 68504.  The
meeting was conducted In-Person and by WebEx.  The following members answered the roll call:

Wesley Zeger, DO, Chairperson
Mark Goodman, MD, Vice-Chairperson via WebEx
Rachel Blake, MD
Jodanne Hedrick, DO via WebEx
Brian Keegan, MD via WebEx
Adam Kuenning, JD, LLM
John Massey, MD

Absent: Jeffrey Howorth, Secretary

A quorum was present, and the meeting convened.

Also present to participate in the meeting: Vonda Apking, Program Manager and Jan Gadeken-Harris, Health
Licensing Coordinator with the Licensure Unit; Mindy Lester, Assistant Attorney General; Randy Clark and Hayle
Alvarado, Investigators with the Investigation Unit; Tricia Allen, Program Manager with the Investigation Unit; Ellie
Rohr, DHHS Department Attorney and Jeanette Peterson, RN, BSN with Compliance Monitoring via WebEx.

Zeger announced that there is a copy of all the public documents being reviewed at this meeting available in the
meeting room pursuant to the Open Meetings Act.

In accordance with Neb. Rev. Stat. § 84-1411 of the Nebraska Open Meetings Act, copies of the agenda were e-
mailed to the Board members and other interested parties, posted on the DHHS web site at
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx and posted on the Bulletin Board at the entrance
to the Nebraska State Office Building April 29, 2026 and revised on May 4, 2026.

REVIEW OF AGENDA

Kuenning moved, seconded by Goodman, to approve adoption of the agenda with the Chair having the authority
to rearrange agenda items as needed.  Voting aye: Blake, Goodman, Hedrick, Keegan, Kuenning, Massey and
Zeger.  Voting nay: None.  Absent: Howorth.  Abstain: None.  Motion carried.

ADOPTION OF THE APPLICATION(S) CONSENT AGENDA

There were no applications for review on the Consent Agenda for this meeting.

LEGISLATION UPDATES

Amy Reynoldson, Executive Vice President and Eric Sutton, JD, Director of Health Policy via WebEx with the
NMA (Nebraska Medical Association) were present to discuss and provide updates to the Board for the 109th
Legislature.

Rural Health Care Transformation Program – the NMA is working with the DHHS on establishing funding for the
Recruitment Initiative and the Retention Initiative

Board of Medicine and Surgery
Minutes of the Meeting – May 8, 2026
Page 2

Amy also shared the following chart on the NMA’s recent Legislative impacts – notably LB527 & LB77 both from
2025:

Board of Medicine and Surgery
Minutes of the Meeting – May 8, 2026
Page 3

Board of Medicine and Surgery
Minutes of the Meeting – May 8, 2026
Page 4

REGULATIONS UPDATE

Currently there are no updates for the Board.

APPROVAL OF MINUTES OF THE MEETING

Kuenning moved, seconded by Massey to approve April 10, 2026, meeting minutes as written.  Voting aye: Blake,
Goodman, Hedrick, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: Howorth.  Abstain: None.
Motion carried.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

INVESTIGATIONAL REPORTS, DISCIPLINARY REPORTS, APPLICATION REVIEW – CLOSED SESSION

Kuenning moved, seconded by Blake, to go to closed session at 9:23 a.m. for the purpose of review and
discussion of investigative reports, disciplinary reports, licensure applications, and other confidential information,
and for the prevention of needless injury to the reputation of the individuals.  Voting aye: Blake, Goodman,
Hedrick, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: Howorth.  Abstain: None.  Motion
carried.

Board Break 10:32 a.m.
Board Returned 10:48 a.m.

The Board members returned to Open Session at 10:48 a.m.

APPLICATION REVIEW – OPEN SESSION

BOARD RECOMMENDATIONS ON APPLICATIONS FOR LICENSURE AND REGISTRATION

There were no applications for review for this meeting.

EMAIL BALLOTS SINCE LAST MEETING

An Email Ballot was sent to the Board Members on April 16, 2026, requesting approval of the draft for the
Nebraska Board of Medicine and Surgery Newsletter for May 2026.  The Email Ballot was approved

DISCUSSION(S)

A.  Low-Level Laser Therapy also called Red Light Therapy

It is the opinion of the Board that low-level laser therapy is a therapeutic intervention that goes deeper than the
dermis, therefore it represents the practice of medicine and surgery as defined by State Statutes.  The practice of
medicine and surgery requires the appropriate scope, education and training with informed consent as
appropriate.

B.  Therapeutic Botox Injections for Pediatric Spasticity

The Department does not currently have an approved course that it recommends.  The Board would recommend
researching for a course that offers continuing medical education credits with application specific.  The Board also
suggests that prior to any procedures that your employer and supervisors have been informed.

C.  Nurse Practitioners and Physician Assistants Treating Pain Management

It is the opinion of the Board that PA’s practice pain management within their scope of practice and training and
their supervising physician needs to have the appropriate scope of practice.

The Board cannot comment on NP’s; therefore, the Board of Nursing would need to be addressed for comment.

Board of Medicine and Surgery
Minutes of the Meeting – May 8, 2026
Page 5

D.  AOA (American Osteopathic Association) Letter of Concern Regarding Patient Safety Issues

The Board acknowledges receipt of the letter.

FSMB (FEDERATION OF STATE MEDICAL BOARDS) ANNUAL MEETING

The FSMB meeting was held April 30 – May 2, 2026, in Baltimore, MD.  Dr. Hedrick and Dr. Blake attended the
meeting representing the Nebraska Board.  Dr. Hedrick also represented the Board as their voting delegate.  Dr.
Blake said that it was an excellent conference with numerous informative sessions.  One of the sessions was
regarding AI (Artificial Intelligence) and its role and regulations for medicine and surgery.  The FSMB will continue
to share guidelines on AI as appropriate.

The 2027 FSMB Annual Meeting will be Oklahoma City, OK.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

BOARD MEETING SCHEDULE

The next meeting is scheduled for June 12, 2026, in the Husker Conference Room at the Hampton Inn & Suites.
To see a complete list of the projected schedule for the 2026 schedule, visit the DHHS website:
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx

ADJOURNMENT

There being no further business, Zeger, Chairperson adjourned the meeting at 10:55 a.m.

Respectfully submitted,

*signature available upon request*

Mark Goodman, MD, Vice-Chairperson
Board of Medicine and Surgery

---

### 2026-04-10 — Nebraska Board of Medicine and Surgery — April 10, 2026

**[AGENDA] 2026-04-10_041026medagenda.pdf**

NOTICE OF MEETING OF THE
BOARD OF MEDICINE AND SURGERY
Date Posted March 30, 2026

       Hampton Inn & Suites
       Husker Conference Room
       7343 Husker Circle
       Lincoln, NE  68504-9816

Friday
April 10, 2026
9:00 am

This meeting will be held by WebEx conference and In-Person.  The public is welcome to attend any Open Session discussion
at the Hampton Inn & Suites.  A WebEx line has also been established for the public rather than visit the open meeting location.
If you wish to attend the meeting by WEBEX please let Jan Harris know by April 9, 2026 via email at janis.gadeken-
harris@nebraska.gov or you can join by using the below WebEx link:

https://sonvideo.webex.com/sonvideo/j.php?MTID=m51973995fc255a4009ef667f808b52b9

or call in information is:  1-408-418-9388 using meeting number of:  2483 745 5514

Here is a link to the Open Meetings Act:

https://nebraskalegislature.gov/laws/display_html.php?begin_section=84-1407&end_section=84-1414

Here is a link to a copy of all the Open Session discussion items:

https://dhhs.ne.gov/licensure/Pages/Board-Meeting-Documents.aspx

For information, contact Jan Harris, Health Licensing Coordinator, at 402/471-2118, or Janis.Gadeken-Harris@nebraska.gov

1.  Roll Call

AGENDA

      Announcement:  There is a current copy of the Open Meetings Act posted near the door to the meeting room

2.  Adoption of Agenda

A.  Additions, Modification, Reordering and Adoption of Agenda
B.  Adoption of CONSENT Agenda(s)

(9A)  Physician and Osteopathic Physician Initial Application(s) (1) (CONSENT)
(9B)  Physician and Osteopathic Physician Reinstatement after Discipline Application(s) (1) (CONSENT)
(9C)  Temporary Visiting Faculty Permit Application(s) (1) (CONSENT)

     3.     Legislation Updates
     4.     Regulations Updates
     5.    Approval of Minutes of the Meeting:

     Board Meeting – March 13, 2026

     6.    Public Comments

7.     Investigational Reports – CLOSED SESSION pursuant to Neb. Rev. Stat. 38-1,105 (The Board will go into closed
session for the purpose of review and discussion of investigative reports, licensure applications, and other
confidential information, and for the prevention of needless injury to the reputation of the individuals).

(Approx. time to go into Closed Session: 9:30 am)

Investigation Cases

A.
B.    Compliance Monitoring Reports
C.    Proposed Agreed Settlement

     8.

Application Review – CLOSED SESSION pursuant to Neb. Rev. Stat. 84-1410

     9.     Application Review – OPEN SESSION

(Approx. time to reconvene Open Session: 10:45 am)

     A.   Physician and Osteopathic Physician Initial Application(s) (1) (CONSENT)

                   B.   Physician and Osteopathic Physician Reinstatement after Discipline Application(s) (1) (CONSENT)
                   C.   Temporary Visiting Faculty Permit Application(s) (1) (CONSENT)
    10.  Email Ballots since last meeting
    11.     Pharmaceutical Care Agreements – January & March 2026

    12.  Practice Question(s)

       A.   Is it within the scope of practice of a Surgical First Assistant to close the skin without a physician in the room?

    13.     Update from NCBAHM (National Certification Board for Acupuncture and Herbal Medicine – formerly known as
              NCCAOM (National Certification Commission for Acupuncture and Oriental Medicine)
    14.     Public Comments
    15.     Board of Medicine and Surgery 2026 Meeting Schedule – Next scheduled meeting May 8, 2026
    16.  Adjournment

***The Board will work through LUNCH***

All items known at time of distribution of this agenda are listed; a current agenda is available on the First Floor, State Office Building, 301
Centennial Mall South, Lincoln, Nebraska.

Notice: A tape recording of the meeting will be made for the purpose of preparing minutes of the meeting.  Said tape will not be transcribed but
will be available to the public until such time that the minutes of this meeting are approved by the Board.  In accordance with the records
retention schedule of the Licensure Unit as authorized by Nebraska Statute, the Division may dispose of the tapes ten (10) days after the
meeting; however, staff shall retain the tapes until the Board has approved the minutes.

Auxiliary aids or reasonable accommodations needed to participate in a meeting can be requested by calling (402) 471-2118.  Individuals who
are deaf or hard of hearing may call DHHS via the Nebraska Relay System at 711 or (800) 833-7352 TDD at least 2 weeks prior to the meeting.

---

**[MINUTES] 2026-04-10_041026medminutes.pdf**

NEBRASKA BOARD OF MEDICINE AND SURGERY

MEETING MINUTES
April 10, 2026

ROLL CALL

The meeting of the Board of Medicine and Surgery was called to order by Chairperson, Wesley Zeger, DO, at
9:00 a.m. on April 10, 2026, at the Hampton Inn & Suites, 7343 Husker Circle, Lincoln, Nebraska 68504.  The
meeting was conducted In-Person and by WebEx.  The following members answered the roll call:

Wesley Zeger, DO, Chairperson
Mark Goodman, MD, Vice-Chairperson
Jeffrey Howorth, Secretary
Rachel Blake, MD
Jodanne Hedrick, DO
Brian Keegan, MD
Adam Kuenning, JD, LLM
John Massey, MD

Absent: None

A quorum was present, and the meeting convened.

Also present to participate in the meeting: Vonda Apking, Program Manager and Jan Gadeken-Harris, Health
Licensing Coordinator with the Licensure Unit; Mindy Lester, Assistant Attorney General; Randy Clark, Mark
Meyerson, Andrea Cramer and Veronica Briggs, Investigators with the Investigation Unit; Ellie Rohr, DHHS
Department Attorney and Jessie Enfield, DHHS Licensure Support.

Zeger announced that there is a copy of all the public documents being reviewed at this meeting available in the
meeting room pursuant to the Open Meetings Act.

In accordance with Neb. Rev. Stat. § 84-1411 of the Nebraska Open Meetings Act, copies of the agenda were e-
mailed to the Board members and other interested parties, posted on the DHHS web site at
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx and posted on the Bulletin Board at the entrance
to the Nebraska State Office Building March 30, 2026.

REVIEW OF AGENDA

Kuenning moved, seconded by Blake, to approve adoption of the agenda with the Chair having the authority to
rearrange agenda items as needed.  Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey
and Zeger.  Voting nay: None.  Absent: None.  Abstain: None.  Motion carried.

ADOPTION OF THE APPLICATION(S) CONSENT AGENDA

Kuenning moved, seconded by Blake, to have the following applications removed from the consent agenda:

Ali, Wazir, MD – Initial Physician application
Evans, Joshua, MD – Reinstatement after Discipline application
Simchuk, Dariia, MD – Temporary Visiting Faculty Permit Initial application

Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.
Absent: None.  Abstain: None.  Motion carried.

Board of Medicine and Surgery
Minutes of the Meeting – April 10, 2026
Page 2

LEGISLATION UPDATES

Paul Henderson, JD, Vice President, Advocacy & Regulation, In-House Counsel and Eric Sutton, JD, Director of
Health Policy via WebEx with the NMA (Nebraska Medical Association) were present to discuss and provide
updates to the Board for the 109th Legislature.

LB1212 - Provide for licensure of internationally trained physicians under the Uniform Credentialing Act
Paul indicated that this Bill is expected to pass.
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63078&docnum=LB1212&leg=109LB955 –

LB955 - Provide for practice agreements between pharmacists and physician assistants
Paul indicated that this Bill is expected to pass.
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=62703&docnum=LB955&leg=109

LB958 - Provide for implementation of a home and community-based services waiver, retroactive coverage of
certain benefits, and reimbursement of doula services and change reporting requirements under the Medical
Assistance Act, change provisions relating to the Nebraska Prenatal Plus Program, and provide limits for crisis
assistance payments under the low-income home energy assistance program
This Bill has several Amendments that have been adopted and is expected to pass.
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63301&docnum=LB958&leg=109

LB912 - Adopt the Community Health Worker Training Endorsement Act, the Athletic Trainer Compact, and the
Respiratory Care Interstate Compact, change provisions relating to child care licensing and the practice of athletic
training, respiratory care, massage therapy, medical radiography, nurse practitioners, pharmacy, and
pharmacists, provide for liens for physical therapy services and automated pickup kiosks for certain prescription
medication, and eliminate provisions relating to physician liability for physician assistants
April 7, 2026, the Bill was placed on Final Reading.
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=62787&docnum=LB912&leg=109

LB929 - Provide for managed care organizations to pay the deductible, cost sharing, or similar charges on behalf
of Medicaid enrollees
April 8, 2026, the Bill was placed on Final Reading
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63088&docnum=LB929&leg=109

LB933 - Provide immunity for health care practitioners under the Nebraska Medical Cannabis Patient Protection
Act
Paul indicated that this Bill did not pass.
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63001&docnum=LB933&leg=109

REGULATIONS UPDATE

Currently there are no updates for the Board.

APPROVAL OF MINUTES OF THE MEETING

Goodman moved, seconded by Massey to approve March 13, 2026, meeting minutes as written.  Voting aye:
Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: None.
Abstain: None.  Motion carried.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

Board of Medicine and Surgery
Minutes of the Meeting – April 10, 2026
Page 3

INVESTIGATIONAL REPORTS, DISCIPLINARY REPORTS, APPLICATION REVIEW – CLOSED SESSION

Blake moved, seconded by Howorth, to go to closed session at 9:09 a.m. for the purpose of review and
discussion of investigative reports, disciplinary reports, licensure applications, and other confidential information,
and for the prevention of needless injury to the reputation of the individuals.  Voting aye: Blake, Goodman,
Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: None.  Abstain: None.
Motion carried.

Kuenning recused himself at 9:32 a.m.
Kuenning returned at 9:48 a.m.

The Board members returned to Open Session at 10:50 a.m.

APPLICATION REVIEW – OPEN SESSION

BOARD RECOMMENDATIONS ON APPLICATIONS FOR LICENSURE AND REGISTRATION

Physician Initial Application(s) (1)

ALI, WAZIR, MD – application for initial license to practice medicine and surgery.  Goodman moved, seconded by
Kuenning to recommend denial of the license to practice medicine and surgery.  The basis for the denial is
previous disciplinary action in another state.  Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning,
Massey and Zeger.  Voting nay: None.  Absent: None.  Abstain: None.  Motion carried.

Physician Reinstatement after Discipline Application(s) (1)

EVANS, JOSHUA T., MD – Goodman moved, seconded by Hedrick to recommend reinstatement of the license
subject to a three (3) year Probation, with the first year subject to a reentry license, and to include usual terms
and conditions.  Basis for the Probation is not having actively practiced medicine utilizing clinical skills for over two
years and prior disciplinary action.  Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey
and Zeger.  Voting nay: None.  Absent: None.  Abstain: None.  Motion carried.

Physician TVFP (Temporary Visiting Faculty Permit) Application(s) (1)

SIMCHUK, DARILIA, MD – application for a TVFP to practice medicine and surgery.  Blake moved, seconded by
Hedrick, to recommend approval of the license to practice medicine and surgery.  Voting aye: Blake, Goodman,
Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: None.  Abstain: None.
Motion carried.

EMAIL BALLOTS SINCE LAST MEETING

There were no Email Ballots to report.

PHARMACEUTICAL CARE AGREEMENTS

The Board recognizes the receipt of the Pharmaceutical Care Agreements from January and March 2026.

PRACTICE QUESTION(S)

A.  Is it within the scope of practice of a Surgical First Assistant to close the skin without a physician in the room?

It is the opinion of the Board that the physician must be in the operating room based on Statute under “Personal
Supervision”

UPDATE FROM NCBAHM (NATIONAL CERTIFICATION BOARD FOR ACUPUNCTURE AND HERBAL MEDICINE –
FORMERLY KNOWN AS NCCAOM (NATIONAL CERTIFICATION COMMISSION FOR ACUPUNCTURE AND ORIENTAL
MEDICINE)

Due to the name change the Regulations will need to be revised to reflect this update.

Board of Medicine and Surgery
Minutes of the Meeting – April 10, 2026
Page 4

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

BOARD MEETING SCHEDULE

The next meeting is scheduled for May 8, 2026, in the Husker Conference Room at the Hampton Inn & Suites.
To see a complete list of the projected schedule for the 2026 schedule, visit the DHHS website:
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx

ADJOURNMENT

There being no further business, Zeger, Chairperson adjourned the meeting at 10:56 a.m.

Respectfully submitted,

*signature available upon request*

Jeffrey Howorth, Secretary
Board of Medicine and Surgery

---

### 2026-03-13 — Nebraska Board of Medicine and Surgery — March 13, 2026

**[AGENDA] 2026-03-13_031326medagenda.pdf**

NOTICE OF MEETING OF THE
BOARD OF MEDICINE AND SURGERY
Date Posted March 2, 2026

       Hampton Inn & Suites
       Husker Conference Room
       7343 Husker Circle
       Lincoln, NE  68504-9816

Friday
March 13, 2026
9:00 am

This meeting will be held by WebEx conference and In-Person.  The public is welcome to attend any Open Session discussion
at the Hampton Inn & Suites.  A WebEx line has also been established for the public rather than visit the open meeting location.
If you wish to attend the meeting by WEBEX please let Vonda Apking know by March 12, 2026 via email at
vonda.apking@nebraska.gov or you can join by using the below WebEx link:

https://sonvideo.webex.com/sonvideo/j.php?MTID=m9899b5ccd3b038e6aa57aaf6c7a6e818

or call in information is:  1-408-418-9388 using meeting number of:  2492 891 4381

Here is a link to the Open Meetings Act:

https://nebraskalegislature.gov/laws/display_html.php?begin_section=84-1407&end_section=84-1414

Here is a link to a copy of all the Open Session discussion items:

https://dhhs.ne.gov/licensure/Pages/Board-Meeting-Documents.aspx

For information, contact Jan Harris, Health Licensing Coordinator, at 402/471-2118, or Janis.Gadeken-Harris@nebraska.gov

1.  Roll Call

AGENDA

      Announcement:  There is a current copy of the Open Meetings Act posted near the door to the meeting room

2.  Adoption of Agenda

A.  Additions, Modification, Reordering and Adoption of Agenda
B.  Adoption of CONSENT Agenda(s)

(10A)  Physician and Osteopathic Physician Initial Application(s) (CONSENT)
(10B)  Physician and Osteopathic Physician Reinstatement Application(s)(CONSENT)
(10C)  Temporary Visiting Faculty Permit Application(s) (CONSENT)

     3.     Legislation Updates
     4.     Regulations Updates
     5.    Approval of Minutes of the Meeting:

     Emergency Board Meeting – February 9, 2026
     Board Meeting – February 13, 2026

     6.    EBAS (Ethics Boundaries Assessment Services) Presentation by Bradley Guye – (15-20 minutes)
     7.    Public Comments

(Approx. time to go into Closed Session: 9:45 am)

8.     Investigational Reports – CLOSED SESSION pursuant to Neb. Rev. Stat. 38-1,105 (The Board will go into closed
session for the purpose of review and discussion of investigative reports, licensure applications, and other
confidential information, and for the prevention of needless injury to the reputation of the individuals).

Investigation Cases

A.
B.    Compliance Monitoring Reports
C.    Proposed Agreed Settlement

     9.

Application Review – CLOSED SESSION pursuant to Neb. Rev. Stat. 84-1410

    10.     Application Review – OPEN SESSION

(Approx. time to reconvene Open Session: 10:45 am)

     A.   Physician and Osteopathic Physician Initial Application(s) (CONSENT)
                   B.   Physician and Osteopathic Physician Reinstatement Application(s) (CONSENT)
                   C.   Temporary Visiting Faculty Permit Application(s) (CONSENT)
    11.  Email Ballots since last meeting
    12.     FSMB Annual Conference April 30-May 2, 2026 – Vote for Delegate to represent the Board at the Conference

 13.    Public Comments
 14.     Board of Medicine and Surgery 2026 Meeting Schedule – Next scheduled meeting April 10, 2026

***Board Break to allow for Hearing Room Setup

15.

Hearing before the Board of Medicine and Surgery – Daniel Martin Wik, MD – 12:00 Noon – OPEN SESSION CONT.

16.

17.

18.

Hearing Review – CLOSED SESSION

Hearing Review – OPEN SESSION

Adjournment

***The Board will work through LUNCH***

All items known at time of distribution of this agenda are listed; a current agenda is available on the First Floor, State Office Building, 301
Centennial Mall South, Lincoln, Nebraska.

Notice: A tape recording of the meeting will be made for the purpose of preparing minutes of the meeting.  Said tape will not be transcribed but
will be available to the public until such time that the minutes of this meeting are approved by the Board.  In accordance with the records
retention schedule of the Licensure Unit as authorized by Nebraska Statute, the Division may dispose of the tapes ten (10) days after the
meeting; however, staff shall retain the tapes until the Board has approved the minutes.

Auxiliary aids or reasonable accommodations needed to participate in a meeting can be requested by calling (402) 471-2118.  Individuals who
are deaf or hard of hearing may call DHHS via the Nebraska Relay System at 711 or (800) 833-7352 TDD at least 2 weeks prior to the meeting.

---

**[MINUTES] 2026-03-13_031326medminutes.pdf**

NEBRASKA BOARD OF MEDICINE AND SURGERY

MEETING MINUTES
March 13, 2026

ROLL CALL

The meeting of the Board of Medicine and Surgery was called to order by Vice-Chairperson, Mark Goodman, MD,
at 9:00 a.m. on March 13, 2026, at the Hampton Inn & Suites, 7343 Husker Circle, Lincoln, Nebraska 68504.  The
meeting was conducted In-Person and by WebEx.  The following members answered the roll call:

Mark Goodman, MD, Vice-Chairperson
Jeffrey Howorth, Secretary
Rachel Blake, MD
Jodanne Hedrick, DO
Brian Keegan, MD
Adam Kuenning, JD, LLM
John Massey, MD

Absent: Wesley Zeger, DO, Chairperson

A quorum was present, and the meeting convened.

Also present to participate in the meeting: Vonda Apking, Program Manager and Jan Gadeken-Harris, Health
Licensing Coordinator with the Licensure Unit; Mindy Lester, Assistant Attorney General; Randy Clark, Mark
Meyerson, Mendy Hahar-Clark and Hayle Alvarado, Investigators with the Investigation Unit; Tricia Allen,
Program Manager with the Investigation Unit; Ellie Rohr, DHHS Department Attorney and Jessie Enfield, DHHS
Licensure Support.

Goodman announced that there is a copy of all the public documents being reviewed at this meeting available in
the meeting room pursuant to the Open Meetings Act.

In accordance with Neb. Rev. Stat. § 84-1411 of the Nebraska Open Meetings Act, copies of the agenda were e-
mailed to the Board members and other interested parties, posted on the DHHS web site at
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx and posted on the Bulletin Board at the entrance
to the Nebraska State Office Building March 2, 2026.

REVIEW OF AGENDA

Blake moved, seconded by Hedrick, to approve adoption of the agenda with the Chair having the authority to
rearrange agenda items as needed.  Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning and
Massey.  Voting nay: None.  Absent: Zeger.  Abstain: None.  Motion carried.

Goodman, announced that there is one change of the Agenda with the Hearing scheduled as Items 15-17 being
postponed to a future Board meeting.

ADOPTION OF THE APPLICATION(S) CONSENT AGENDA

There are no applications for review for this meeting.

Board of Medicine and Surgery
Minutes of the Meeting – March 13, 2026
Page 2

LEGISLATION UPDATES

Amy Reynoldson, Executive Vice President and Paul Henderson, JD, Vice President, Advocacy & Regulation, In-
House Counsel and Eric Sutton, JD, Director of Health Policy with the NMA (Nebraska Medical Association) were
present to discuss and provide updates to the Board for the 109th Legislature.

LB1212 - Provide for licensure of internationally trained physicians under the Uniform Credentialing Act
Hearing was held on - February 11, 2026
AM2477 was filed – March 10, 2026
https://nebraskalegislature.gov/FloorDocs/109/PDF/AM/AM2477.pdf
AM2477 has a list of new duties for the Board of Medicine and Surgery under LB1212
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63078&docnum=LB1212&leg=109

LB933 - Provide immunity for health care practitioners under the Nebraska Medical Cannabis Patient Protection
Act
Hearing was held on February 19, 2026
Several Amendment have been filed
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63001&docnum=LB933&leg=109

There is a stall on the midwife Bill before the Legislature and there is consideration of a 407 Credentialing Review
for changes in scope of practice.

Athletic Trainers for operating room privileges is possibly going to a 407 Credentialing Review for changes in
scope of practice.

REGULATIONS UPDATE

Currently there are no updates for the Board.

APPROVAL OF MINUTES OF THE MEETING

Hedrick moved, seconded by Kuenning to approve February 9, 2026, Emergency Meeting minutes as written.
Voting aye: Goodman, Hedrick, Howorth and Kuenning.  Voting nay: None.  Absent: Zeger.  Abstain: Blake,
Keegan and Massey.  Motion carried.

Kuenning moved, seconded by Blake to approve February 13, 2026, minutes with the correction on page1 where
the word “Chairperson” needs to be deleted after Kuenning’s name.  Voting aye: Blake, Hedrick, Howorth,
Kuenning and Massey.  Voting nay: None.  Absent: Zeger.  Abstain: Goodman and Keegan.

EBAS (ETHICS BOUNDARIES ASSESSMENT SERVICES) PRESENTATION BY BRADLEY GUYE,
BUSINESS DEVELOPMENT MANAGER

EBAS is Trusted by:
150 Regulatory Boards
37 Industries
41 States
1,000+ Disciplinary Processes

Protecting Public Safety
ABOUT EBAS:
23% of Employees Witnessed or Involved in Unethical Behavior
Nearly 60% of misconduct observed in the workplace never reported
Repeat Offender Figures
Passive Learning Numbers
CE Answers “Did they attend?”
EBAS Answers “Did they understand?”
EBAS Testing Process:

Board of Medicine and Surgery
Minutes of the Meeting – March 13, 2026
Page 3

The Board – Orders the disciplinary action
The Licensee – does the Registration and goes through the Assessment
EBAS – will provide the Scoring of the Assessment and give the Results to the Board

EBAS Assessment Types:

•  Boundaries
•  Unprofessional Conduct
•  Professional Standards
•  Substance Abuse
•  Fraud

Cost:

•  No cost to the Board
•  No contractual requirement
•  $400 per assessment, paid by the licensee

EBAS Provides a thorough review of your Licensee’s Ethical and Moral Compass with a streamlined
administration

The Board and the Department want to Thank Mr. Guye for his presentation and answering all their questions and
will highly consider implementing EBAS into their future disciplinary processes.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

INVESTIGATIONAL REPORTS, DISCIPLINARY REPORTS, APPLICATION REVIEW – CLOSED SESSION

Howorth moved, seconded by Kuenning, to go to closed session at 9:44 a.m. for the purpose of review and
discussion of investigative reports, disciplinary reports, licensure applications, and other confidential information,
and for the prevention of needless injury to the reputation of the individuals.  Voting aye: Blake, Goodman,
Hedrick, Howorth, Keegan, Kuenning and Massey.  Voting nay: None.  Absent: Zeger.  Abstain: None.  Motion
carried.

Dr. Blake and Dr. Massey recused themselves at 10:17a.m.
Dr. Blake and Dr. Massey returned at 10:26 a.m.

The Board members returned to Open Session at 11:10 a.m.

APPLICATION REVIEW – OPEN SESSION

BOARD RECOMMENDATIONS ON APPLICATIONS FOR LICENSURE AND REGISTRATION

There were no applications for review by the Board for this meeting.

EMAIL BALLOTS SINCE LAST MEETING

On February 9, 2026, an Email Ballot was sent to the Board regarding the Letter drafted by Dr. Hedrick on behalf
of the Board of Medicine and Surgery to present to the Nebraska Legislature regarding the Board’s opposition to
LB 1212.  Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay:
None. Absent: None. Abstain: None.

Board of Medicine and Surgery
Minutes of the Meeting – March 13, 2026
Page 4

FSMB (FEDERATION OF STATE MEDICAL BOARDS) ANNUAL CONFERENCE – VOTE FOR DELEGATE TO
REPRESENT THE BOARD

Howorth moved, seconded by Kuenning to nominate Dr. Hedrick to act as the Voting Delegate to represent the
Nebraska Board of Medicine and Surgery at the FSMB conference in Baltimore, MD, April 30 – May 2, 2026.
Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning and Massey.  Voting nay: None. Absent:
Zeger.  Abstain: None.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

BOARD MEETING SCHEDULE

The next meeting is scheduled for April 10, 2026, in the Husker Conference Room at the Hampton Inn & Suites.
To see a complete list of the projected schedule for the 2026 schedule, visit the DHHS website:
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx

ADJOURNMENT

There being no further business, Goodman, Vice-Chairperson adjourned the meeting at 11:39 a.m.

Respectfully submitted,

*signature available upon request*

Jeffrey Howorth, Secretary
Board of Medicine and Surgery

---

### 2026-02-13 — Nebraska Board of Medicine and Surgery — February 13, 2026

**[AGENDA] 2026-02-13_021326medagenda.pdf**

NOTICE OF MEETING OF THE
BOARD OF MEDICINE AND SURGERY
Date Posted February 2, 2026

       Hampton Inn & Suites
       Husker Conference Room
       7343 Husker Circle
       Lincoln, NE  68504-9816

Friday
February 13, 2026
9:00 am

This meeting will be held by WebEx conference and In-Person.  The public is welcome to attend any Open Session discussion
at the Hampton Inn & Suites.  A WebEx line has also been established for the public rather than visit the open meeting location.
If you wish to attend the meeting by WEBEX please let Jan Gadeken-Harris know by January 8, 2026 via email at
janis.gadeken-harris@nebraska.gov or you can join by using the below WebEx link:

https://sonvideo.webex.com/sonvideo/j.php?MTID=m4be939b44a8292db3fa5eb949580b8f3

or call in information is:  1-408-418-9388 using meeting number of:  2485 430 5916

Here is a link to the Open Meetings Act:

https://nebraskalegislature.gov/laws/display_html.php?begin_section=84-1407&end_section=84-1414

Here is a link to a copy of all the Open Session discussion items:

https://dhhs.ne.gov/licensure/Pages/Board-Meeting-Documents.aspx

For information, contact Jan Harris, Health Licensing Coordinator, at 402/471-2118, or Janis.Gadeken-Harris@nebraska.gov

1.  Roll Call

AGENDA

      Announcement:  There is a current copy of the Open Meetings Act posted near the door to the meeting room

2.  Adoption of Agenda

A.  Additions, Modification, Reordering and Adoption of Agenda
B.  Adoption of CONSENT Agenda(s)

(9A)  Physician and Osteopathic Physician Initial Application(s) (CONSENT)
(9B)  Physician and Osteopathic Physician Reinstatement Application(s)(CONSENT)
(9C)  Temporary Visiting Faculty Permit Application(s) (CONSENT)

     3.     Legislation Updates
     4.     Regulations Updates
     5.    Approval of Minutes of the Meeting – January 9, 2026
     6.    Public Comments

7.     Investigational Reports – CLOSED SESSION pursuant to Neb. Rev. Stat. 38-1,105 (The Board will go into closed
session for the purpose of review and discussion of investigative reports, licensure applications, and other
confidential information, and for the prevention of needless injury to the reputation of the individuals).

(Approx. time to go into Closed Session: 9:30 am)

Investigation Cases

A.
B.    Compliance Monitoring Reports
C.    Proposed Agreed Settlement
D.    AG 4th Quarter Report
Application Review – CLOSED SESSION pursuant to Neb. Rev. Stat. 84-1410

     8.

     9.     Application Review – OPEN SESSION

(Approx. time to reconvene Open Session: 10:45 am)

A.   Physician and Osteopathic Physician Initial Application(s) (CONSENT)
              B.   Physician and Osteopathic Physician Reinstatement Application(s) (CONSENT)
              C.   Temporary Visiting Faculty Permit Application(s) (CONSENT)
    10.     Public Comments
    11.     Board of Medicine and Surgery 2026 Meeting Schedule – Next scheduled meeting March 13, 2026

***Board Break to allow for Hearing Room Setup

12.

Hearing before the Board of Medicine and Surgery – Daniel Martin Wik, MD – 12:00 Noon – OPEN SESSION CONT.

13.

14.

15.

Hearing Review – CLOSED SESSION

Hearing Review – OPEN SESSION

Adjournment

***The Board will work through LUNCH***

All items known at time of distribution of this agenda are listed; a current agenda is available on the First Floor, State Office Building, 301
Centennial Mall South, Lincoln, Nebraska.

Notice: A tape recording of the meeting will be made for the purpose of preparing minutes of the meeting.  Said tape will not be transcribed but
will be available to the public until such time that the minutes of this meeting are approved by the Board.  In accordance with the records
retention schedule of the Licensure Unit as authorized by Nebraska Statute, the Division may dispose of the tapes ten (10) days after the
meeting; however, staff shall retain the tapes until the Board has approved the minutes.

Auxiliary aids or reasonable accommodations needed to participate in a meeting can be requested by calling (402) 471-2118.  Individuals who
are deaf or hard of hearing may call DHHS via the Nebraska Relay System at 711 or (800) 833-7352 TDD at least 2 weeks prior to the meeting.

---

**[MINUTES] 2026-02-13_021326medminutes.pdf**

NEBRASKA BOARD OF MEDICINE AND SURGERY

MEETING MINUTES
February 13, 2026

ROLL CALL

The meeting of the Board of Medicine and Surgery was called to order by Chairperson, Wesley Zeger, DO, at
9:03 a.m. on February 13, 2026, at the Hampton Inn & Suites, 7343 Husker Circle, Lincoln, Nebraska 68504.  The
meeting was conducted In-Person and by WebEx.  The following members answered the roll call:

Wesley Zeger, DO, Chairperson
Jeffrey Howorth, Secretary
Rachel Blake, MD
Jodanne Hedrick, DO
Adam Kuenning, JD, LLM
John Massey, MD

Absent: Mark Goodman, MD, Vice-Chairperson

Brian Keegan, MD

A quorum was present, and the meeting convened.

Also present to participate in the meeting: Vonda Apking, Program Manager and Jan Gadeken-Harris, Health
Licensing Coordinator with the Licensure Unit; Mindy Lester, Assistant Attorney General; Randy Clark and Hayle
Alvarado, Investigators with the Investigation Unit; Tricia Allen, Program Manager with the Investigation Unit; Ellie
Rohr, DHHS Department Attorney and Jessie Enfield, DHHS Licensure Support.

Zeger announced that there is a copy of all the public documents being reviewed at this meeting available in the
meeting room pursuant to the Open Meetings Act.

In accordance with Neb. Rev. Stat. § 84-1411 of the Nebraska Open Meetings Act, copies of the agenda were e-
mailed to the Board members and other interested parties, posted on the DHHS web site at
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx and posted on the Bulletin Board at the entrance
to the Nebraska State Office Building February 2, 2026.

REVIEW OF AGENDA

Howorth moved, seconded by Hedrick, to approve adoption of the agenda with the Chair having the authority to
rearrange agenda items as needed.  Voting aye: Blake, Hedrick, Howorth, Kuenning, Massey and Zeger.  Voting
nay: None.  Absent: Goodman and Keegan.  Abstain: None.  Motion carried.

Zeger, announced that there is one change of the Agenda with the Hearing scheduled as Items 12-14 being
postponed to the next Board meeting on March 13, 2026.

ADOPTION OF THE APPLICATION(S) CONSENT AGENDA

Massey moved, seconded by Howorth to have the following applications removed from the consent agenda:

Benson, Robert, MD – Initial Physician application
Simchuk, Darilia, MD – TVFP application

Voting aye: Blake, Hedrick, Howorth, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: Goodman and
Keegan.  Abstain: None.  Motion carried.

Board of Medicine and Surgery
Minutes of the Meeting – February 13, 2026
Page 2

LEGISLATION UPDATES

Amy Reynoldson, Executive Vice President and Paul Henderson, Vice President, Advocacy & Regulation, In-
House Counsel with the NMA (Nebraska Medical Association) were present to discuss and provide updates to the
Board for the 109th Legislature.

LB1212 - Provide for licensure of internationally trained physicians under the Uniform Credentialing Act
Notice of Hearing - February 11, 2026
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63078&docnum=LB1212&leg=109

The Board previously discussed LB1212 at an Emergency meeting on February 9, 2026.  The Board opposes
LB1212 as currently written.  A Letter of Opposition was delivered by Hedrick via oral testimony to the Legislature
at the Hearing on February 11, 2013.

Below is the Board’s Letter of Opposition delivered by Hedrick:

Chairperson and members of the committee, thank you for the opportunity to speak today. My name is Dr.
Jodanne Hedrick, and I am here on behalf of the Nebraska Board of Medicine and Surgery.

We recognize and share the Legislature’s concern about access to care in rural Nebraska. Many of our
communities face significant physician shortages and long travel distances for care. Patients in these areas
deserve timely access to services and a stable healthcare workforce. We appreciate the intent of this bill to help
address those needs.

The Board’s first and foremost responsibility, however, is public safety. Our statutory mission is to ensure that all
physicians practicing in Nebraska meet consistent standards for safe, competent, and high-quality care. For that
reason, we must respectfully oppose Legislative Bill 1212 in its current form and recommend several important
revisions to ensure that any pathway forward maintains the highest standards for patient care.

First, the bill does not clearly require verification of board certification or equivalent specialty certification in the
physician’s home country. While many internationally trained physicians are exceptionally well trained, confirming
specialty certification or its equivalent is an important measure to ensure consistent standards of medical
expertise and clinical readiness. Including this requirement would strengthen public confidence and help ensure
that patients—particularly those in rural communities—receive care from highly trained professionals.

Second, the bill does not specifically state that the physician must have practiced medicine within the past 12
months. Recent, active clinical practice is an important indicator of current competence. Adding language
requiring recent practice would help ensure that physicians entering Nebraska’s workforce are clinically current
and prepared to deliver safe care from day one.

Third, we recommend revising the terminology used in the bill. The current language referring to a “limited” or
“restricted” license may create confusion, as those terms are presently associated in Nebraska with disciplinary
actions. We suggest instead the use of the term “provisional license to practice,” which more accurately reflects a
structured transition period and avoids unintended implications for both physicians and the public.

We want to be clear: the Board supports thoughtful pathways that welcome qualified internationally trained
physicians into Nebraska’s workforce. These physicians contribute greatly to healthcare across our country. But
rural communities deserve more than a temporary solution to shortages. They deserve competent, highly trained
professionals who are prepared to practice safely within the U.S. healthcare system. Expanding access and
maintaining high standards are not mutually exclusive goals. We can—and must—do both.

The Board stands ready to collaborate with the Legislature to strengthen this bill so that it both improves access
to care and preserves the safeguards that protect patients. Public safety must remain the foundation of any
licensure pathway.

Thank you for your time and for your commitment to the health of Nebraskans. I am happy to answer any
questions.  Jodanne W. Hedrick, DO member and representative of the Nebraska Board of Medicine and Surgery.

Board of Medicine and Surgery
Minutes of the Meeting – February 13, 2026
Page 3

LB933 - Provide immunity for health care practitioners under the Nebraska Medical Cannabis Patient Protection
Act
Notice of Hearing – February 19, 2026
To learn more regarding this Bill go to:  https://nebraskalegislature.gov/FloorDocs/109/PDF/Intro/LB933.pdf

LB1234 - Adopt the Freestanding Birth Center Act
Notice of Hearing – February 12, 2026
To learn more regarding this Bill go to:  https://nebraskalegislature.gov/FloorDocs/109/PDF/Intro/LB1234.pdf
The NMA, the DHHS Department and the Nursing Association do not support this Bill as written

REGULATIONS UPDATE

Currently there are no updates for the Board.

APPROVAL OF MINUTES OF THE MEETING

Blake moved, seconded by Kuenning to approve January 9, 2026, minutes as written.  Voting aye: Blake,
Hedrick, Howorth, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: Goodman and Keegan.  Abstain:
None.  Motion carried.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

INVESTIGATIONAL REPORTS, DISCIPLINARY REPORTS, APPLICATION REVIEW – CLOSED SESSION

Blake moved, seconded by Kuenning, to go to closed session at 9:35 a.m. for the purpose of review and
discussion of investigative reports, disciplinary reports, licensure applications, and other confidential information,
and for the prevention of needless injury to the reputation of the individuals.  Voting aye: Blake, Hedrick, Howorth,
Kuenning, Massey and Zeger.  Voting nay: None.  Absent: Goodman and Keegan.  Abstain: None.  Motion
carried.

The Board members returned to Open Session at 11:53 a.m.

APPLICATION REVIEW – OPEN SESSION

BOARD RECOMMENDATIONS ON APPLICATIONS FOR LICENSURE AND REGISTRATION

Physician Initial Application(s) (1)

BENSON, ROBERT WILLIAM, MD – application for initial license to practice medicine and surgery.  Hedrick
moved, seconded by Howorth, to recommend approval of the license to practice medicine and surgery.  Voting
aye: Blake, Hedrick, Howorth, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: Goodman and Keegan.
Abstain: None.  Motion carried.

Physician TVFP (Temporary Visiting Faculty Permit) Application(s) (1)

SIMCHUK, DARILIA, MD – application for a TVFP to practice medicine and surgery.  Hedrick moved, seconded
by Howorth, to recommend tabling the application for additional information.  Voting aye: Blake, Hedrick, Howorth,
Kuenning, Massey and Zeger.  Voting nay: None.  Absent: Goodman and Keegan.  Abstain: None.  Motion
carried.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

Board of Medicine and Surgery
Minutes of the Meeting – February 13, 2026
Page 4

BOARD MEETING SCHEDULE

The next meeting is scheduled for March 13, 2026, in the Husker Conference Room at the Hampton Inn & Suites.
To see a complete list of the projected schedule for the 2026 schedule, visit the DHHS website:
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx

ADJOURNMENT

There being no further business, Zeger, Chairperson adjourned the meeting at 11:56 a.m.

Respectfully submitted,

*signature available upon request*

Jeffrey Howorth, Secretary
Board of Medicine and Surgery

---

### 2026-02-09 — Nebraska Board of Medicine and Surgery — February 09, 2026

**[AGENDA] 2026-02-09_020926medagenda.pdf**

NOTICE OF EMERGENCY CONFERENCE CALL MEETING OF THE
BOARD OF MEDICINE AND SURGERY
Date Posted February 6, 2026

       State Office Building
       6A Conference Room
       301 Centennial Mall South
       Lincoln, NE  68508

Friday
February 9, 2026
12:30 pm

This meeting will be held by WebEx conference.  The public is welcome to attend any Open Session discussion via WebEx.  A
WebEx line has also been established for the public rather than visiting the open meeting location.  If you wish to attend the
meeting by WEBEX please let Vonda Apking know via email at vonda.apking@nebraska.gov or you can join by using the below
WebEx link:

https://sonvideo.webex.com/sonvideo/j.php?MTID=m2f8706af6229c12bd024e964c526f493

or call in information is:  1-408-418-9388 using meeting number of:  2483 179 4676

Here is a link to the Open Meetings Act:

https://nebraskalegislature.gov/laws/display_html.php?begin_section=84-1407&end_section=84-1414

Here is a link to a copy of all the Open Session discussion items:

https://dhhs.ne.gov/licensure/Pages/Board-Meeting-Documents.aspx

For information, contact Jan Harris, Health Licensing Coordinator, at 402/471-2118, or Janis.Gadeken-Harris@nebraska.gov

1.  Roll Call

AGENDA

      Announcement:  There is a current copy of the Open Meetings Act posted near the door to the meeting room

2.  Adoption of Agenda

     3.     Discussion on Legislative Bill - 1212
     4.     Adjournment

All items known at time of distribution of this agenda are listed; a current agenda is available on the First Floor, State Office Building, 301
Centennial Mall South, Lincoln, Nebraska.

Notice: A tape recording of the meeting will be made for the purpose of preparing minutes of the meeting.  Said tape will not be transcribed but
will be available to the public until such time that the minutes of this meeting are approved by the Board.  In accordance with the records
retention schedule of the Licensure Unit as authorized by Nebraska Statute, the Division may dispose of the tapes ten (10) days after the
meeting; however, staff shall retain the tapes until the Board has approved the minutes.

Auxiliary aids or reasonable accommodations needed to participate in a meeting can be requested by calling (402) 471-2118.  Individuals who
are deaf or hard of hearing may call DHHS via the Nebraska Relay System at 711 or (800) 833-7352 TDD at least 2 weeks prior to the meeting.

---

**[MINUTES] 2026-02-09_020926medminutes.pdf**

NEBRASKA BOARD OF MEDICINE AND SURGERY

EMERGENCY MEETING MINUTES
February 09, 2026

ROLL CALL

The meeting of the Board of Medicine and Surgery was called to order by Chairperson, Wesley Zeger, DO, at
12:31 p.m. on February 9, 2026, at the NE State Office Building, 301 Centennial Mall South, 6A Conference
Room, Lincoln, Nebraska 68508.  The meeting was conducted In-Person and by WebEx.  The following members
answered the roll call:

Wesley Zeger, DO, Chairperson, via WebEx
Mark Goodman, MD, Vice-Chairperson, via WebEx
Jeffrey Howorth, Secretary, via WebEx
Jodanne Hedrick, DO, via WebEx
Adam Kuenning, JD, LLM, via WebEx

Absent: Rachel Blake, MD
Brian Keegan, MD
John Massey, MD

A quorum was present, and the meeting convened.

Also present to participate in the meeting: Vonda Apking, Program Manager and Jan Gadeken-Harris, Health
Licensing Coordinator with the Licensure Unit; Milissa Johnson-Wiles, Assistant Attorney General, via WebEx;
and Ellie Rohr, DHHS Department Attorney, via WebEx.

Zeger announced that there is a copy of all the public documents being reviewed at this meeting available in the
meeting room pursuant to the Open Meetings Act.

In accordance with Neb. Rev. Stat. § 84-1411 of the Nebraska Open Meetings Act, copies of the agenda were e-
mailed to the Board members and other interested parties, posted on the DHHS web site at
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx and posted on the Bulletin Board at the entrance
to the Nebraska State Office Building February 6, 2026.

REVIEW OF AGENDA

Goodman moved, seconded by Hedrick, to approve adoption of the agenda with the Chair having the authority to
rearrange agenda items as needed.  Voting aye: Goodman, Hedrick, Howorth, Kuenning, and Zeger.  Voting nay:
None.  Absent: Blake, Keegan and Massey.  Abstain: None.  Motion carried.

DISCUSSION:

LB1212 - Provide for licensure of internationally trained physicians under the Uniform Credentialing Act
Notice of Hearing - February 11, 2026
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63078&docnum=LB1212&leg=109

Amy Reynoldson, Executive Vice President and Paul Henderson, Vice President, Advocacy & Regulation; In-
house Counsel with the NMA (Nebraska Medical Association) were present to discuss and provide updates to the
Board regarding LB1212 that is scheduled for Hearing February 11, 2026.

The Board discussed whether they wanted to give an opinion as to whether they are opposed, neutral or
supportive of LB1212 as currently written.

Hedrick moved and Howorth seconded that the Board would oppose LB1212 as currently written and to have
Hedrick draft a letter of opposition for the Board’s approval.  Voting aye: Goodman, Hedrick, Howorth, Kuenning,
and Zeger.  Voting nay: None.  Absent: Blake, Keegan and Massey.  Abstain: None.  Motion carried.

Board of Medicine and Surgery
Minutes of the Meeting – February 9, 2026
Page 2

Hedrick moved and Goodman seconded to have the Board’s approved Letter of Opposition be given as oral
testimony at the Legislative Hearing on February 11, 2026, by Hedrick. Voting aye: Goodman, Hedrick, Howorth,
Kuenning, and Zeger.  Voting nay: None.  Absent: Blake, Keegan and Massey.  Abstain: None.  Motion carried.

ADJOURNMENT

There being no further business, Zeger, Chairperson adjourned the meeting at 1:20 p.m.

Respectfully submitted,

*signature available upon request*

Jeffrey Howorth, Secretary
Board of Medicine and Surgery

---

### 2026-01-29 — Nebraska Board of Medicine and Surgery — January 29, 2026

*(No extracted text available)*

---

### 2026-01-09 — Nebraska Board of Medicine and Surgery — January 09, 2026

**[AGENDA] 2026-01-09_010926medagenda.pdf**

NOTICE OF MEETING OF THE
BOARD OF MEDICINE AND SURGERY
Date Posted December 23, 2025
REVISION POSTED January 6, 2026

       Hampton Inn & Suites
       Husker Conference Room
       7343 Husker Circle
       Lincoln, NE  68504-9816

Friday
January 9, 2026
9:00 am

This meeting will be held by WebEx conference and In-Person.  The public is welcome to attend any Open Session discussion
at the Hampton Inn & Suites.  A WebEx line has also been established for the public rather than visit the open meeting location.
If you wish to attend the meeting by WEBEX please let Jan Gadeken-Harris know by January 8, 2026 via email at
janis.gadeken-harris@nebraska.gov or you can join by using the below WebEx link:

https://sonvideo.webex.com/sonvideo/j.php?MTID=m1cd8a83baacc80c62aa780ec83a62a3a

or call in information is:  1-408-418-9388 using meeting number of:  2484 935 4019

Here is a link to the Open Meetings Act:

https://nebraskalegislature.gov/laws/display_html.php?begin_section=84-1407&end_section=84-1414

Here is a link to a copy of all the Open Session discussion items:

https://dhhs.ne.gov/licensure/Pages/Board-Meeting-Documents.aspx

For information, contact Jan Harris, Health Licensing Coordinator, at 402/471-2118, or Janis.Gadeken-Harris@nebraska.gov

1.  Roll Call

AGENDA

      Announcement:  There is a current copy of the Open Meetings Act posted near the door to the meeting room

2.  Adoption of Agenda

A.  Additions, Modification, Reordering and Adoption of Agenda
B.  Adoption of CONSENT Agenda(s)

(10A)  Physician and Osteopathic Physician Initial Application(s) (0) (CONSENT)
(10B) Physician and Osteopathic Physician Reinstatement Application(s) (0) (CONSENT)

     3.     2026 Legislation Updates
     4.     Regulations Updates
     5.    Approval of Minutes of the Meeting – December 12, 2025
     6.    EBAS (Ethics Boundaries Assessent Services) Presentation by Bradley Guye – (15-20 minutes)
     7.    Public Comments

(Approx. time to go into Closed Session: 9:45 am)

8.     Investigational Reports – CLOSED SESSION pursuant to Neb. Rev. Stat. 38-1,105 (The Board will go into closed
session for the purpose of review and discussion of investigative reports, licensure applications, and other
confidential information, and for the prevention of needless injury to the reputation of the individuals).

Investigation Cases

A.
B.    Compliance Monitoring Reports
C.    Proposed Agreed Settlement
Application Review – CLOSED SESSION pursuant to Neb. Rev. Stat. 84-1410

     9.

    10.     Application Review – OPEN SESSION

(Approx. time to reconvene Open Session: 10:45 am)

A.   Physician and Osteopathic Physician Initial Application(s) (0) (CONSENT)
              B.   Physician and Osteopathic Physician Reinstatement Application(s) (0) (CONSENT)
    11.  FYI – Drexel’s Physician Refresher/Re-entry Program – Virtual Information Session February 2, 2026
    12.     Designation of the Method by which This Body will Give Public Notice of Its Meetings
    13.     Election of Officers for 2026
    14.     Public Comments
    15.     Board of Medicine and Surgery 2026 Meeting Schedule – Next scheduled meeting February 13, 2026
    16.     Adjournment

***The Board will work through LUNCH***

All items known at time of distribution of this agenda are listed; a current agenda is available on the First Floor, State Office Building, 301
Centennial Mall South, Lincoln, Nebraska.

Notice: A tape recording of the meeting will be made for the purpose of preparing minutes of the meeting.  Said tape will not be transcribed but
will be available to the public until such time that the minutes of this meeting are approved by the Board.  In accordance with the records
retention schedule of the Licensure Unit as authorized by Nebraska Statute, the Division may dispose of the tapes ten (10) days after the
meeting; however, staff shall retain the tapes until the Board has approved the minutes.

Auxiliary aids or reasonable accommodations needed to participate in a meeting can be requested by calling (402) 471-2118.  Individuals who
are deaf or hard of hearing may call DHHS via the Nebraska Relay System at 711 or (800) 833-7352 TDD at least 2 weeks prior to the meeting.

---

**[MINUTES] 2026-01-09_010926medminutes.pdf**

NEBRASKA BOARD OF MEDICINE AND SURGERY

MEETING MINUTES
January 9, 2026

ROLL CALL

The meeting of the Board of Medicine and Surgery was called to order by Chairperson, Adam Kuenning, at 9:01
a.m. on January 9, 2026, at the Hampton Inn & Suites, 7343 Husker Circle, Lincoln, Nebraska 68504.  The
meeting was conducted In-Person and by WebEx.  The following members answered the roll call:

Adam Kuenning, JD, LLM, Chairperson
Wesley Zeger, DO, Vice-Chairperson
Mark Goodman, MD, Secretary via WebEx
Rachel Blake, MD
Jodanne Hedrick, DO
Jeffrey Howorth
Brian Keegan, MD via WebEx
John Massey, MD

Absent: None

A quorum was present, and the meeting convened.

Also present to participate in the meeting: Vonda Apking, Program Manager and Jan Gadeken-Harris, Health
Licensing Coordinator with the Licensure Unit; Mindy Lester, Assistant Attorney General; Mark Meyerson and
Randy Clark, Investigators with the Investigation Unit; Tricia Allen, Program Manager with the Investigation Unit;
Ellie Rohr, DHHS Department Attorney; Jeanette Peterson, DHHS Compliance Monitoring via WebEx and Jessie
Enfield, DHHS Licensure Support via WebEx.

Kuenning announced that there is a copy of all the public documents being reviewed at this meeting available in
the meeting room pursuant to the Open Meetings Act.

In accordance with Neb. Rev. Stat. § 84-1411 of the Nebraska Open Meetings Act, copies of the agenda were e-
mailed to the Board members and other interested parties, posted on the DHHS web site at
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx and posted on the Bulletin Board at the entrance
to the Nebraska State Office Building December 23, 2025 and revision posted January 6, 2026.

REVIEW OF AGENDA

Howorth moved, seconded by Hedrick, to approve adoption of the agenda with the Chair having the authority to
rearrange agenda items as needed.  Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey
and Zeger.  Voting nay: None.  Absent: None.  Abstain: None.  Motion carried.

ADOPTION OF THE APPLICATION(S) CONSENT AGENDA

There are no applications for review at this time.

LEGISLATION UPDATES

Paul Henderson, Vice President, Advocacy & Regulation, In-House Counsel with the NMA (Nebraska Medical
Association) was present to discuss and provide updates to the Board for the 109th Legislature.

193 Bills have been introduced within two days. Bills to watch:

LB1212 - Provide for licensure of internationally trained physicians under the Uniform Credentialing Act
Notice of Hearing - February 11, 2026
To learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=63078&docnum=LB1212&leg=109

Board of Medicine and Surgery
Minutes of the Meeting – January 9, 2026
Page 2

LB731 - Adopt the Gender Transition Malpractice Accountability Act, provide an exemption to the time limitation
to commence certain actions relating to professional negligence, require insurance coverage for certain
treatments and procedures arising as a result of a gender-altering procedure, and change provisions relating to
civil actions under the Let Them Grow Act
Notice of Hearing – January 29, 2026
To Learn more regarding this Bill go to:
https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=62603&docnum=LB731&leg=109

The PSCF (Patient Safety Cash Fund) fee legislation sunset as of January 1, 2026, and has not been extended.
https://nebraskalegislature.gov/laws/statutes.php?statute=71-8722

REGULATIONS UPDATE

Currently there are no updates for the Board.

APPROVAL OF MINUTES OF THE MEETING

Goodman moved, seconded by Hedrick to approve December 12, 2025, minutes as written.  Voting aye: Blake,
Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: None.  Abstain:
None.  Motion carried.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

INVESTIGATIONAL REPORTS, DISCIPLINARY REPORTS, APPLICATION REVIEW – CLOSED SESSION

Howorth moved, seconded by Hedrick, to go to closed session at 9:13 a.m. for the purpose of review and
discussion of investigative reports, disciplinary reports, licensure applications, and other confidential information,
and for the prevention of needless injury to the reputation of the individuals.  Voting aye: Blake, Goodman,
Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.  Absent: None.  Abstain: None.
Motion carried.

Dr. Goodman recused himself at 9:27 a.m.
Dr. Goodman returned at 9:43 a.m.

Board Break at 10:30 a.m.
Board Retuned at 10:48 a.m.

The Board members returned to Open Session at 10:48 a.m.

APPLICATION REVIEW – OPEN SESSION

BOARD RECOMMENDATIONS ON APPLICATIONS FOR LICENSURE AND REGISTRATION

There were no applications for review for this meeting.

FYI – DREXEL’S PHYSICIAN REFRESHER/RE-ENTRY PROGRAM

There is a virtual information session available February 2, 2026 – visit Drexel University College of Medicine for
more information.

Board of Medicine and Surgery
Minutes of the Meeting – January 9, 2026
Page 3

DESIGNATION OF THE METHOD BY WHICH THIS BODY WILL GIVE PUBLIC NOTICE OF ITS MEETINGS

Gadeken-Harris explained that the Board needs to inform the public each year the method by which the Board will
provide notice of their meetings.  In the past, the Board had chosen to post meeting agendas on the Bulletin
Board at the Nebraska State Office Building, to e-mail agendas to the interested parties list, and to post agendas
on the Department’s website.  Massey moved, seconded by Hedrick, to continue the same method that the
Department has been using to provide public notice of this Board’s meetings by posting meeting agendas at the
Nebraska State Office Building, by e-mailing agendas to the interested parties list, and by posting agendas on the
Department’s website.  Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.
Voting nay: None.  Absent: None.  Abstain: None.  Motion carried.

ELECTION OF OFFICERS

Goodman moved, seconded by Hedrick to elect new officers for 2026 as follows:
Chairperson: Wesley Zeger, DO
Vice-Chairperson: Mark Goodman, MD
Secretary: Jeff Howorth

Voting aye: Blake, Goodman, Hedrick, Howorth, Keegan, Kuenning, Massey and Zeger.  Voting nay: None.
Absent: None.  Abstain: None.  Motion carried.

PUBLIC COMMENTS

There were no public comments at this time of the meeting.

BOARD MEETING SCHEDULE

The next meeting is scheduled for February 13, 2026, in the Husker Conference Room at the Hampton Inn &
Suites.  To see a complete list of the projected schedule for the 2026 schedule, visit the DHHS website:
https://dhhs.ne.gov/licensure/Pages/Agendas-and-Minutes.aspx

ADJOURNMENT

There being no further business, Kuenning, Chairperson adjourned the meeting at 10:53 a.m.

Respectfully submitted,

*signature available upon request*

Mark Goodman, MD, Secretary
Board of Medicine and Surgery
