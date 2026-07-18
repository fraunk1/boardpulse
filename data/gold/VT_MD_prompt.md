You are an expert analyst summarizing state medical board meeting minutes.

## Task

Summarize the meeting minutes for **Vermont Board of Medical Practice** (VT) covering the meetings listed below.

## Instructions

1. Read all the meeting text provided below carefully.
2. Produce ONE file with TWO layers: first a 12-month BOARD ROLLUP, then one
   PER-MEETING section for every meeting that has extracted text.
3. **In the rollup, every factual claim MUST cite the specific meeting date** using the format `([YYYY-MM-DD](/board/VT/VT_MD#YYYY-MM-DD))`. This creates a clickable link.
4. Write in a professional, neutral tone suitable for a regulatory affairs audience.
5. Use ONLY information contained in this file. Never invent facts, dates, votes, or names. Every name+date pairing you write must appear together in the source text for that exact date.

## Available Meeting Dates (for citations and section headers)

- `[2026-06-15]` — Vermont Board of Medical Practice — June 15, 2026
- `[2026-06-03]` — Vermont Board of Medical Practice — June 03, 2026
- `[2026-05-20]` — Vermont Board of Medical Practice — May 20, 2026
- `[2026-04-15]` — Vermont Board of Medical Practice — April 15, 2026
- `[2026-03-18]` — Vermont Board of Medical Practice — March 18, 2026
- `[2026-03-06]` — Vermont Board of Medical Practice — March 06, 2026
- `[2026-02-18]` — Vermont Board of Medical Practice — February 18, 2026
- `[2026-02-04]` — Vermont Board of Medical Practice — February 04, 2026
- `[2026-01-21]` — Vermont Board of Medical Practice — January 21, 2026
- `[2025-12-10]` — Vermont Board of Medical Practice — December 10, 2025
- `[2025-12-03]` — Vermont Board of Medical Practice — December 03, 2025
- `[2025-11-19]` — Vermont Board of Medical Practice — November 19, 2025
- `[2025-11-05]` — Vermont Board of Medical Practice — November 05, 2025
- `[2025-10-15]` — Vermont Board of Medical Practice — October 15, 2025
- `[2025-09-17]` — Vermont Board of Medical Practice — September 17, 2025
- `[2025-09-03]` — Vermont Board of Medical Practice — September 03, 2025
- `[2025-08-20]` — Vermont Board of Medical Practice — August 20, 2025
- `[2025-08-06]` — Vermont Board of Medical Practice — August 06, 2025
- `[2025-07-16]` — Vermont Board of Medical Practice — July 16, 2025
- `[2025-07-09]` — Vermont Board of Medical Practice — July 09, 2025

## Output Format

Produce EXACTLY this structure (the `=== MEETING: ... ===` delimiters are parsed by machine — reproduce them exactly):

```markdown
---
topics: ["tag1", "tag2"]
board: VT_MD
state: VT
---

# Vermont Board of Medical Practice — 12-Month Board Summary

**Period:** [earliest date] to [latest date]
**Meetings analyzed:** [count]

[BOARD ROLLUP: 300-600 words synthesizing the year across meetings — key
topics, notable actions, recurring themes. This is the ONLY place for
cross-meeting narrative, and every claim carries a date citation link.
End the rollup with the Sources table:]

## Sources
| # | Date | Board | Source |
|---|------|-------|--------|
| 1 | YYYY-MM-DD | Vermont Board of Medical Practice | [Minutes page](VT_MD_MINUTES_URL) |

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

Sources-table URL: https://www.healthvermont.gov/emergency/emergency-medical-services/policies-documents-forms-and-meeting-minutes

## Meeting Minutes Data

Board: Vermont Board of Medical Practice
State: VT
Code: VT_MD

### 2026-06-15 — Vermont Board of Medical Practice — June 15, 2026

**[MINUTES] 2026-06-15_eprip-ems-course-allegations.pdf**

POLICY: ALLEGATIONS MADE AGAINST AN EMS EDUCATION COURSE OR STUDENT

Policy Statement:

This policy gives guidance on the processes that are followed when an allegation is brought
to any EMS Office staff related to a Vermont approved, initial EMS education course.

Relevant EMS Rule:
EMS Rule 9.0: Conducting Initial EMS Training Courses
EMS Rule 10.0: EMS Instructor Licenses
EMS Rule 14.0: Standards and Procedures for Issuing, Restricting and Revoking Service and
Personnel Licenses:
EMS Rule 14.1.7: For Instructors

Procedure:

Below are the steps that will be taken when the EMS Office is notified of an allegation
against any student, Instructor Coordinator (IC), or other personnel involved in an Initial
EMS course.
1.  Complaint process and Reporting:

a.  The Course Medical director will be notified of any allegations brought to the

EMS office related to an EMS course they oversee.

b.  Any concerns regarding student or IC performance- whether knowledge based,
skills based, or professional behavior- should be documented and sent to the
EMS Programs Administrator who will forward it to the appropriate individuals
on a case-by-case basis.

c.  An individual with concerns related to an EMS course may report their concerns
to the EMS Office; however, they are encouraged to relay the concerns to the
course IC in accordance with that program’s policy.

2.  Investigation Procedures:

a.  If it is deemed by EMS Office staff that a full investigation is necessary for the

allegation, the EMS Programs Administrator will lead the process going forward.

3.  Disciplinary Actions:

a.  The Department may condition, suspend, or revoke a personnel or instructor

license or certification in accordance with EMS Rule 14.0

4.  Protection of Rights:

a.  If a license or certification is conditioned, suspended, or revoked after

investigation of an allegation, the individual should refer to EMS Policy- EMS
Hearings and Appeals found on the VT EMS website.

Rationale:
Initial EMS Education courses have a significant impact on the EMS system. It is imperative that
all allegations related to an EMS course- whether it be staff or student related- are reviewed
appropriately.

Effective Date:  August 2024

POLICY: ALLEGATIONS MADE AGAINST AN EMS EDUCATION COURSE OR STUDENT

---

**[MINUTES] 2026-06-15_VTEMS%20Protocols%202023%20-%20Hyperlinked.pdf**

20132013
2013

Vermont Department of Health
Office of Public Health Preparedness and Emergency Medical Services
Vermont Statewide EMS Protocols – 2023 (replaces 2020 version)
Legend Definition
E Emergency Medical Technician (EMT)
A Advanced Emergency Medical Technician (AEMT)
P Paramedic
X Extended Care Protocol
CAUTION – Red Flag topic
Contact Medical Direction
Blue underline – text formatted as a hyperlink
These protocols are a “living document” developed and drafted by the Protocol Workgroup of
Vermont Emergency Medical Services.
These 2023 Vermont Statewide EMS Protocols were reviewed, edited, and approved of by all of
Vermont's District Medical Advisors and other stakeholders. Any deviation from these protocols
must be approved in writing by the Vermont EMS Office.
Please Note: For visual clarity, trademark and registered symbols have not been included with
drug, product, or equipment names.
Questions and comments should be directed to:
Vermont Department of Health
Division of Emergency Preparedness, Response
& Injury Prevention
Post Office Box 70
Burlington, VT 05402
(802) 863-7310
(800) 244-0911 (in VT)
vtems@vermont.gov
This document may not be amended or altered; however, it may be reproduced and distributed.
DISCLAIMER: Although the authors of this document have made great efforts to ensure that all
the information is accurate, there may be errors. The authors cannot be held responsible for any
such errors. For the latest corrections to these protocols, see the Vermont EMS website at:
http://www.vermontems.org
20132013
2013

Vermont Statewide EMS Protocols 2023 – Table of Contents
| Page | (Alphabetical order by section) |       |
| ---- | ------------------------------- | ----- |
| vi   | Preface                         |       |
SECTION 1 – General Patient Care
| 1.0 | Routine Patient Care (VEFR) |     |
| --- | --------------------------- | --- |
| 1.1 | Routine Patient Care (EMR)  |     |
| 1.2 | Routine Patient Care        |     |
| 1.3 | Extended Care Guidelines    |     |
SECTION 2 – Medical Protocols
| 2.0  | Abdominal Pain (Non Traumatic) – Adult & Pediatric |     |
| ---- | -------------------------------------------------- | --- |
| 2.1  | Adrenal Insufficiency – Adult/Pediatric            |     |
| 2.2A | Allergic Reaction/Anaphylaxis – Adult              |     |
| 2.2P | Allergic Reaction/Anaphylaxis – Pediatric          |     |
| 2.3A | Altered Mental Status – Adult                      |     |
| 2.3P | Altered Mental Status – Pediatric                  |     |
| 2.4A | Asthma/COPD/RAD – Adult                            |     |
| 2.4P | Asthma/Bronchiolitis/RAD/Croup – Pediatric         |     |
2.5 Behavioral Emergencies Including Suicide Attempts & Threats – Adult/Pediatric
| 2.6P  | Brief Resolved Unexplained Event (BRUE) – Pediatric      |     |
| ----- | -------------------------------------------------------- | --- |
| 2.7   | Diabetic Emergencies (Hyperglycemia) – Adult & Pediatric |     |
| 2.8A  | Diabetic Emergencies (Hypoglycemia) – Adult              |     |
| 2.8P  | Diabetic Emergencies (Hypoglycemia) – Pediatric          |     |
| 2.9   | Epistaxis / Nosebleed                                    |     |
| 2.10  | Exertional Heat Stroke                                   |     |
| 2.11  | Hyperkalemia & Renal Failure                             |     |
| 2.12  | Hyperthermia (Environmental) – Adult & Pediatric         |     |
| 2.13  | Hypothermia (Environmental) – Adult & Pediatric          |     |
| 2.14  | Nausea/Vomiting – Adult & Pediatric                      |     |
| 2.15A | Nerve Agent/Organophosphate Poisoning – Adult            |     |
| 2.15P | Nerve Agent/Organophosphate Poisoning – Pediatric        |     |
| 2.16  | Newborn Care                                             |     |
| 2.17  | Newborn Resuscitation                                    |     |
| 2.18  | Normal Labor and Delivery                                |     |
| 2.19  | Obstetrical Emergencies                                  |     |
| 2.20A | Pain Management – Adult                                  |     |
| 2.20P | Pain Management – Pediatric                              |     |
| 2.21A | Poisoning/Substance Abuse/Overdose – Adult               |     |
| 2.21P | Poisoning/Substance Abuse/Overdose – Pediatric           |     |
| 2.22A | Seizures – Adult                                         |     |
| 2.22P | Seizures – Pediatric                                     |     |
| 2.23A | Sepsis – Adult                                           |     |
| 2.23P | Sepsis – Pediatric                                       |     |
| 2.24A | Shock – Adult                                            |     |
| 2.24P | Shock – Pediatric                                        |     |
| 2.25  | Smoke Inhalation/Carbon Monoxide Poisoning               |     |
| 2.26A | Stroke – Adult                                           |     |
| 2.27  | Syncope – Adult & Pediatric                              |     |
20132013
2013

Vermont Statewide EMS Protocols 2022 – Table of Contents
| Page | (Alphabetical order by section) |       |
| ---- | ------------------------------- | ----- |

SECTION 3 – Cardiac Protocols
| 3.0A | Acute Coronary Syndrome – Adult                    |     |
| ---- | -------------------------------------------------- | --- |
| 3.1A | Bradycardia – Adult                                |     |
| 3.1P | Bradycardia – Pediatric                            |     |
| 3.2A | Cardiac Arrest – Adult                             |     |
| 3.2P | Cardiac Arrest – Pediatric                         |     |
| 3.3A | Congestive Heart Failure (Pulmonary Edema) – Adult |     |
| 3.4A | Post Resuscitative Care – Adult                    |     |
| 3.4P | Post Resuscitative Care – Pediatric                |     |
| 3.5A | Tachycardia – Adult                                |     |
| 3.5P | Tachycardia – Pediatric                            |     |
| 3.6  | Team Focused CPR – Adult & Pediatric               |     |
SECTION 4 – Trauma Protocols
| 4.0  | Burns/Electrocution/Lightning – Adult & Pediatric   |     |
| ---- | --------------------------------------------------- | --- |
| 4.1  | Crush/Suspension Injury – Adult & Pediatric         |     |
| 4.2  | Drowning/Submersion Injuries – Adult & Pediatric    |     |
| 4.3  | Eye & Dental Injuries – Adult & Pediatric           |     |
| 4.4  | Hemorrhage Control – Adult & Pediatric              |     |
| 4.5  | Musculoskeletal Injuries – Adult & Pediatric        |     |
| 4.6  | Spinal Trauma and Assessment                        |     |
| 4.7  | Strangulation                                       |     |
| 4.8  | Thoracic and Abdominal Injuries – Adult & Pediatric |     |
| 4.9  | Trauma Triage and Transport Decision                |     |
| 4.10 | Traumatic Brain Injury – Adult & Pediatric          |     |
| 4.11 | Traumatic Cardiac Arrest                            |     |
| 4.12 | Traumatic Emergencies                               |     |
SECTION 5 – Airway Protocols & Procedures
| 5.0  | Airway Management Procedure                      |     |
| ---- | ------------------------------------------------ | --- |
| 5.1A | Airway Management – Adult                        |     |
| 5.1P | Airway Management – Pediatric                    |     |
| 5.2  | Automated Transport Ventilator                   |     |
| 5.3A | Bilevel Positive Airway Pressure (BiPAP) – Adult |     |
5.4 Continuous Positive Airway Pressure (CPAP) – Adult & Pediatric
| 5.5A | Endotracheal Tube Introducer (“Bougie”) – Adult |     |
| ---- | ----------------------------------------------- | --- |
| 5.6  | Foreign-Body Obstruction                        |     |
| 5.7  | Nasotracheal Intubation                         |     |
| 5.8  | Orotracheal Intubation                          |     |
| 5.9  | Percutaneous Cricothyrotomy                     |     |
| 5.10 | Suctioning of Inserted Airway                   |     |
| 5.11 | Supraglottic Airway – Adult & Pediatric         |     |
| 5.12 | Surgical Cricothyrotomy                         |     |
| 5.13 | Tracheostomy Care – Adult & Pediatric           |     |
| 5.14 | High Flow Nasal Canula                          |     |
SECTION 6 – Medical Procedures
| 6.0 | ECG Acquisition, Transmission and Interpretation         |     |
| --- | -------------------------------------------------------- | --- |
| 6.1 | High Consequence Pathogen – Maintenance & Considerations |     |
| 6.2 | Intraosseous Access                                      |     |
| 6.3 | Needle Decompression Thoracostomy (NDT)                  |     |
| 6.4 | Restraints                                               |     |

20132013
2013

Vermont Statewide EMS Protocols 2023 – Table of Contents
Page (Alphabetical order by section)
SECTION 6 – Medical Procedures (continued from previous page)
6.5 Taser (Conducted Electrical Weapon) Probe Removal and Assessment
6.6 Tourniquet & Hemostatic Agent – Adult & Pediatric
6.7 Vascular Access Via Pre-Existing Central Catheter
6.8 Waveform Capnography
SECTION 7 – Prerequisite Protocols
7.0 Interfacility Transfer
7.1 Interfacility Transport of Patients with IV Heparin by Paramedics
7.2 Rapid Sequence Intubation (RSI)
SECTION 8 – Medical Policies
8.0 Air Medical Transport
8.1 Baby Safe Haven
8.2 Bariatric Triage, Care & Transport
8.3 Communications
8.4 Communications Failure
8.5 Consent for Treatment of a Minor
8.6 Crime Scene/Preservation of Evidence
8.7 Do Not Resuscitate (DNR) & Clinician Orders (COLST) and DNR/COLST Form
8.8 Hospice
8.9 Implantable Ventricular Assist Device (VAD)
8.10 Lift Assist
8.11 Naloxone Leave Behind Overdose Rescue Program
8.12 Non-EMS Personnel at the Emergency Scene
8.13 Pediatric Transportation
8.14 Police Custody
8.15 Refusal of Care and Patient Non-Transport Form
8.16 Rehabilitation – Scene and Training Guidelines for EMS
8.17 Resuscitation Initiation and Termination
8.18 Safe Response and Transportation Guidelines
8.19 Victims of Violence
SECTION 9 – Hazmat & MCI
9.0 Hazardous Materials Exposure
9.1 Mass/Multiple Casualty Triage
9.2 Radiation Injuries – Adult & Pediatric
Appendices
A.1 Cardiac & CPAP Algorithms
A.2 Adult Drip Rate Charts
A.3 High Consequence Pathogens (COVID-19, Ebola, Measles)
A.4 Vermont Adult Medication Reference
A.5 Pediatric Color Coded Appendix
A.6 Scope of Practice
A.7 VT Interfacility Transfer Scope of Practice
20132013
2013

Preface
We welcome you to the 2023 Statewide Vermont EMS protocols. These protocols represent the
work of many people across the state and the continued evolution of prehospital medicine in
Vermont. In this process, these protocols have been reviewed by and specific feedback has been
received and incorporated from:
Members of the Protocol Workgroup
All 13 physicians who serve as District Medical Advisors
Department of Mental Health
Department of Children and Families
Vermont State Police
Office of the Chief Medical Examiner
Howard Center
Disability Rights Vermont
Vermont Ethics Network
Vermont Stroke Task Force
Vermont American Heart Association
Northern New England Poison Control
Over 80 other EMS providers, agencies, and districts
The Vermont Department of Health Division of Emergency Preparedness, Response and Injury
Prevention has attempted to ensure that all information in these protocols is accurate and in
accordance with the best medical evidence available and relevant professional guidelines as
commonly practiced at the time of publication. Use of these protocols is intended for Vermont
licensed EMS organizations and their affiliated licensed personnel functioning under Medical
Direction. EMS District Medical Advisors may restrict but not expand the scope of practice at each
level as outlined in these protocols. On occasion, drug shortages may require substitutions as
communicated by the State EMS Medical Director. Vermont EMS personnel, instructors, and
organizations are free to reproduce this document in whole or in part for educa

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_eprip-2025-EMS-Protocols_0.pdf**

20132013
2013

Vermont Department of Health
Office of Public Health Preparedness and Emergency Medical Services
Vermont Statewide EMS Protocols – 2025 (replaces 2023 version)
Legend Definition
VEFR Vermont Emergency First Responder (VEFR)
Emergency Medical Responder (EMR)
EMR
E Emergency Medical Technician (EMT)
A Advanced Emergency Medical Technician (AEMT)
P Paramedic
X Extended Care Protocol
CAUTION – Red Flag topic
Contact Medical Direction
Blue underline – text formatted as a hyperlink
These protocols are a living document developed and drafted by the EMS Protocol Technical
Advisory Group, which is comprised of EMS professionals and stakeholders of the Vermont
Emergency Medical Services system.
These 2025 Vermont Statewide EMS Protocols were reviewed, edited, and approved of by all of
Vermont's District Medical Advisors and other stakeholders. Any deviation from these protocols
must be approved in writing by the Vermont EMS Office.
Please note, for visual clarity, trademark and registered symbols have not been included with
drug, product, or equipment names.
Questions and comments should be directed to:
Office of Emergency Medical Services
Vermont Department of Health
280 State Drive
Waterbury, VT 05671-8330
(802) 863-7310
(800) 244-0911 (in VT)
vvtteemmss@@vveerrmmoonntt..ggoovv
This document may not be amended or altered; however, it may be reproduced and distributed.
DISCLAIMER: Although the authors of this document have made great efforts to ensure that all
the information is accurate, there may be errors. The authors cannot be held responsible for any
such errors. For the latest corrections to these protocols, see the Vermont EMS website at:
hhttttpp::////wwwwww..vveerrmmoonntteemmss..oorrgg
20132013
2013

Vermont Statewide EMS Protocols 2025 – Table of Contents
Page (Alphabetical order by section)
vi Preface
SECTION 1 – General Patient Care
1.0 Routine Patient Care (VEFR)
1.1 Routine Patient Care (EMR)
1.2 Routine Patient Care
1.3 Extended Care Guidelines
SECTION 2 – Medical Protocols
2.0 Abdominal Pain (Non Traumatic) – Adult & Pediatric
2.1 Adrenal Insufficiency – Adult/Pediatric
2.2A Allergic Reaction/Anaphylaxis – Adult
2.2P Allergic Reaction/Anaphylaxis – Pediatric
2.3A Altered Mental Status – Adult
2.3P Altered Mental Status – Pediatric
2.4A Asthma/COPD/RAD – Adult
2.4P Asthma/Bronchiolitis/RAD/Croup – Pediatric
2.5 Behavioral Emergencies Including Suicide Attempts & Threats – Adult/Pediatric
2.6P Brief Resolved Unexplained Event (BRUE) – Pediatric
2.7 Diabetic Emergencies (Hyperglycemia) – Adult & Pediatric
2.8A Diabetic Emergencies (Hypoglycemia) – Adult
2.8P Diabetic Emergencies (Hypoglycemia) – Pediatric
2.9 Epistaxis / Nosebleed
2.10 Exertional Heat Stroke
2.11 Hyperkalemia & Renal Failure
2.12 Hyperthermia (Environmental) – Adult & Pediatric
2.13 Hypothermia (Environmental) – Adult & Pediatric
2.14 Nausea/Vomiting – Adult & Pediatric
2.15A Nerve Agent/Organophosphate Poisoning – Adult
2.15P Nerve Agent/Organophosphate Poisoning – Pediatric
2.16 Newborn Care
2.17 Newborn Resuscitation
2.18 Normal Labor and Delivery
2.19 Obstetrical Emergencies
2.20A Pain Management – Adult
2.20P Pain Management – Pediatric
2.21A Poisoning/Substance Abuse/Overdose – Adult
2.21P Poisoning/Substance Abuse/Overdose – Pediatric
2.22A Seizures – Adult
2.22P Seizures – Pediatric
2.23A Sepsis – Adult
2.23P Sepsis – Pediatric
2.24A Shock – Adult
2.24P Shock – Pediatric
2.25 Smoke Inhalation/Carbon Monoxide Poisoning
2.26A Stroke – Adult
2.27 Syncope – Adult & Pediatric
20132013
2013

Vermont Statewide EMS Protocols 2025 – Table of Contents
Page (Alphabetical order by section)
SECTION 3 – Cardiac Protocols
3.0A Acute Coronary Syndrome – Adult
3.1A Bradycardia – Adult
3.1P Bradycardia – Pediatric
3.2A Cardiac Arrest – Adult
3.2P Cardiac Arrest – Pediatric
3.3A Congestive Heart Failure (Pulmonary Edema) – Adult
3.4A Post Resuscitative Care – Adult
3.4P Post Resuscitative Care – Pediatric
3.5A Tachycardia – Adult
3.5P Tachycardia – Pediatric
3.6 Team Focused CPR – Adult & Pediatric
SECTION 4 – Trauma Protocols
4.0 Burns/Electrocution/Lightning – Adult & Pediatric
4.1 Crush/Suspension Injury – Adult & Pediatric
4.2 Drowning/Submersion Injuries – Adult & Pediatric
4.3 Eye & Dental Injuries – Adult & Pediatric
4.4 Hemorrhage Control – Adult & Pediatric
4.5 Musculoskeletal Injuries – Adult & Pediatric
4.6 Spinal Trauma and Assessment
4.7 Strangulation
4.8 Thoracic and Abdominal Injuries – Adult & Pediatric
4.9 Trauma Triage and Transport Decision
4.10 Traumatic Brain Injury – Adult & Pediatric
4.11 Traumatic Cardiac Arrest
4.12 Traumatic Emergencies
SECTION 5 – Airway Protocols & Procedures
5.0 Airway Management Procedure
5.1A Airway Management – Adult
5.1P Airway Management – Pediatric
5.2 Automated Transport Ventilator
5.3A Bilevel Positive Airway Pressure (BiPAP) – Adult
5.4 Continuous Positive Airway Pressure (CPAP) – Adult & Pediatric
5.5A Endotracheal Tube Introducer (“Bougie”) – Adult
5.6 Foreign-Body Obstruction
5.7 High Flow Nasal Canula
5.8 Nasotracheal Intubation
5.9 Orotracheal Intubation
5.10 Percutaneous Cricothyrotomy
5.11 Suctioning of Inserted Airway
5.12 Supraglottic Airway – Adult & Pediatric
5.13 Surgical Cricothyrotomy
5.14 Tracheostomy Care – Adult & Pediatric
SECTION 6 – Medical Procedures
6.0 Children With Special Health Needs (CSHN)
6.1 Double Sequential Defibrillation
6.2 ECG Acquisition, Transmission and Interpretation
6.3 High Consequence Pathogen – Maintenance & Considerations
6.4 Intraosseous Access
6.5 Needle Decompression Thoracostomy (NDT)
20132013
6.6 Restraints
2013

Vermont Statewide EMS Protocols 2025 – Table of Contents
Page (Alphabetical order by section)
SECTION 6 – Medical Procedures (continued from previous page)
6.7 Taser (Conducted Electrical Weapon) Probe Removal and Assessment
6.8 Vascular Access Via Pre-Existing Central Catheter
6.9 Waveform Capnography
SECTION 7 – Prerequisite Protocols
7.0 Interfacility Transfer
7.1 Interfacility Transport of Patients with IV Heparin by Paramedics
7.2 Point of Care Ultrasound (POCUS)
7.3 Rapid Sequence Intubation (RSI)
SECTION 8 – Medical Policies
8.0 Air Medical Transport
8.1 Baby Safe Haven
8.2 Bariatric Triage, Care & Transport
8.3 Communications
8.4 Communications Failure
8.5 Consent for Treatment of a Minor
8.6 Crime Scene/Preservation of Evidence
8.7 Do Not Resuscitate (DNR) & Clinician Orders (COLST) and DNR/COLST Form
8.8 Hospice
8.9 Implantable Ventricular Assist Device (VAD)
8.10 Lift Assist
8.11 Naloxone Leave Behind Overdose Rescue Program
8.12 Non-EMS Personnel at the Emergency Scene
8.13 Pediatric Transportation
8.14 Police Custody
8.15 Refusal of Care and Patient Non-Transport Form
8.16 Rehabilitation – Scene and Training Guidelines for EMS
8.17 Resuscitation Initiation and Termination
8.18 Safe Response and Transportation Guidelines
8.19 Victims of Violence
SECTION 9 – Hazmat & MCI
9.0 Hazardous Materials Exposure
9.1 Mass/Multiple Casualty Triage
9.2 Radiation Injuries – Adult & Pediatric
Appendices
A.1 Cardiac & CPAP Algorithms
A.2 Adult Drip Rate Charts
A.3 High Consequence Pathogens (COVID-19, Ebola, Measles)
A.4 Vermont Adult Medication Reference
A.5 Pediatric Color Coded Appendix
A.6 Scope of Practice
A.7 VT Interfacility Transfer Scope of Practice
A.8 BEFAST
20132013
2013

Preface
We welcome you to the 2025 Statewide Vermont EMS Protocols. These protocols represent the
work of many people across the state and the continued evolution of prehospital medicine in
Vermont. In this process, these protocols have been reviewed by and specific feedback has been
received and incorporated from:
Members of the EMS Protocol Technical Advisory Group
All 13 physicians who serve as District Medical Advisors
Department of Mental Health
Department of Children and Families
Vermont State Police
Office of the Chief Medical Examiner
Howard Center
Disability Rights Vermont
Vermont Ethics Network
Vermont Stroke Task Force
Vermont American Heart Association
Northern New England Poison Control
Over 80 other EMS providers, agencies, and districts
The Vermont Department of Health Division of Emergency Preparedness, Response and Injury
Prevention, has attempted to ensure that all information in these protocols is accurate and in
accordance with the best medical evidence available and relevant professional guidelines as
commonly practiced at the time of publication. Use of these protocols is intended for Vermont
licensed EMS organizations and their affiliated licensed personnel functioning under Medical
Direction. EMS District Medical Advisors may restrict but not expand the scope of practice at each
level as outlined in these protocols. On occasion, drug shortages may require substitutions as
communicated by the State EMS Medical Director. Vermont EMS personnel, instructors, and
organizations are free to reproduce this document in whole or in part for educational, QA/QI, field
guidance, or similar purposes.
We continually scan for errors of all types (medication dosing, spelling, grammar, or punctuation),
clarify wording that may be confusing, incorporate feedback from EMS providers, and monitor
medical literature to keep abreast of current EMS practice. Please contact the EMS office with any
suggestions for future revisions or corrections at: vtems@vermont.gov
All licensed providers functioning within the Vermont EMS system are required to be familiar with
the contents of this document pertinent to their level of training and licensure. Updates to these
protocols prior to the next full revision will be posted on the Vermont EMS website and sent via
email to all agency heads, district chairs, and district medical advisors. Agency heads are
responsible for assuring that any updates are provided to their affiliated personnel and any
required training and credentialing occurs. Any updates will also be sent to all licensed EMS
providers that have provided Vermont EMS with a valid email address and are on the Vermont
EMS listserv. Contact the office to add your email address to this listserv if you do not already
receive periodic updates.
When using an electronic version of this document, you will find hyperlinks to each referenced
protocol.
(Continued)
Vermont EMS has taken extreme caution to ensure all information is accurate and in accordance with professional standards
in effect at the time of publication. These protocols, policies, or procedures MAY NOT BE altered or modified. 2025 2013

Preface
IMPORTANT CLARIFICATIONS AND EXPLANATIONS
Protocol Implementation
These protocols are written for the National EMS Scope of Practice Model levels: EMR, EMT,
AEMT, Paramedic, and for the Vermont Emergency First Responder (VEFR) certification. When an
entire agency has completed training on these protocols, they may begin to use these new
protocols. Appendix A.6 contains the scope of practice matrix.
VEFR Scope of Practice
For the Vermont Emergency First Responder (VEFR) certification, the scope of practice is based
upon the American Heart Association HeartSaver First Aid, CPR & AED course. The primary focus
of the Vermont Emergency First Responder is to initiate immediate lifesaving care to critical
patients. This individual possesses the basic knowledge and skills necessary to provide lifesaving
interventions while awaiting additional EMS response and to assist higher level personnel at the
scene and during transport. Vermont Emergency First Responders function as part of a
comprehensive EMS response, under medical oversight. Vermont Emergency First Responders
perform basic interventions with minimal equipment.
The skills and interventions of the VEFR scope of practice are described in the VEFR Routine
Patient Care section of this document.
EMR Scope of Practice
The skills and interventions of the EMR scope of practice are described in the EMR Routine Patient
Care section of this document.
Protocol Labeling
Protocols that are labeled #.A or #.P indicate the adult and pediatric versions of that protocol when
appropr

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_eprip-2025-EMS-resource-kit.pdf**

Protocol Education
Resource Kit

| RESOURCE KIT |     |     |     |     |
| ------------ | --- | --- | --- | --- |

Protocol Education Modules – Resource Kit

Table of Contents
Content  Page Number
| Overview of Education Module            |     |     | 4   |     |
| --------------------------------------- | --- | --- | --- | --- |
| Quick Reference Chart                   |     |     | 7   |     |
| Protocol Introduction 2025 VTEMS (All)  |     |     | 14  |     |
| 2025 VTEMS EMT Medical                  |     |     | 15  |     |
| 2025 VTEMS EMT Cardiac                  |     |     | 16  |     |
| 2025 VTEMS EMT Trauma                   |     |     | 17  |     |
| 2025 VTEMS EMT Airway                   |     |     | 18  |     |
| 2025 VTEMS EMT CPAP                     |     |     | 19  |     |
| 2025 VTEMS EMT/AEMT Behavioral 1        |     |     | 20  |     |
2025 VTEMS 2.5 Behavioral Emergencies/C-SSRS Screener Training (All) -   21
| 2025 VTEMS Naloxone Leave Behind (All)      |     |     | 22               |     |
| ------------------------------------------- | --- | --- | ---------------- | --- |
| 2025 VTEMS EMT Procedures & Policies        |     |     | 23               |     |
| 2025 VTEMS EMT Prerequisite Protocols       |     |     | 24               |     |
| 2025 VTEMS AEMT Medical                     |     |     | 25               |     |
| 2025 VTEMS AEMT Cardiac                     |     |     | 26               |     |
| 2025 VTEMS AEMT Trauma                      |     |     | 27               |     |
| 2025 VTEMS AEMT Airway                      |     |     | 28               |     |
| 2025 VTEMS AEMT Procedures & Policies       |     |     | 29               |     |
| 2025 VTEMS AEMT Prerequisite Protocols      |     |     | 30               |     |
| 2025 VTEMS Paramedic Medical                |     |     | 31               |     |
| 2025 VTEMS Paramedic Cardiac                |     |     | 32               |     |
| 2025 VTEMS Paramedic Trauma                 |     |     | 33               |     |
| 2025 VTEMS Paramedic Airway                 |     |     | 34               |     |
| 2025 VTEMS Paramedic Behavioral 1           |     |     | 35               |     |
| 2025 VTEMS Paramedic Procedures & Policies  |     |     | 36               |     |
| 2                                           |     |     | ver. 01/01/2025  |     |

| RESOURCE KIT |     |     |     |     |
| ------------ | --- | --- | --- | --- |

| 2025 VTEMS Paramedic Prerequisite Protocols  |     |     | 37  |     |
| -------------------------------------------- | --- | --- | --- | --- |
2025 VTEMS CHSN - Children with Special Healthcare Needs (All)  38
| 2025 VTEMS Stroke                      |     |     | 39  |     |
| -------------------------------------- | --- | --- | --- | --- |
| Resuscitation Academy Adult (All)      |     |     | 40  |     |
| Resuscitation Academy Pediatric (All)  |     |     | 41  |     |
| Class Roster for Record Keeping        |     |     | 42  |     |
| EMR Tracking Document                  |     |     | 43  |     |
| EMT Tracking Document                  |     |     | 44  |     |
| AEMT Tracking Document                 |     |     | 45  |     |
| Paramedic Tracking Document            |     |     | 46  |     |
| Acknowledgements                       |     |     | 47  |     |
Appendix I.  Psychomotor training tool kit for the VT EMS 2025 Protocol  48
Continuous Positive Airway Pressure (CPAP) for EMTs

** The information contained in this resource kit serves as guidance from VT EMS about protocol
education/training.  It is not intended to take the place of comprehensive initial or continuing education,
including transition courses, and is designed to be used in conjunction with other educational resources such as
VT EMS developed presentations, knowledgeable instructors, etc.

| 3   |     |     | ver. 01/01/2025  |     |
| --- | --- | --- | ---------------- | --- |

RESOURCE KIT
Overview of the Education Module -
Resource Kit for the Vermont Statewide EMS Protocols
This document has been created as a guide for both EMS practitioners and EMS Services to complete the
education modules for the 2025 Vermont Statewide EMS Protocol Updates. This training is required for every
level of licensure. This training is also required content for all initial EMR, EMT, AEMT, and Paramedic
courses.
If an EMS Service does not carry the equipment necessary for a protocol, then that protocol cannot be used, and
the training does not need to be completed. When an EMS Service purchases the necessary equipment, it will
be expected that the training will then be completed. If an EMS practitioner works at multiple services, they
should complete all required training on all available equipment.
If a district or EMS Service has already completed training on a skill listed due to a waiver granted under the
previous set of EMS protocols, clinicians and/or services must be able to provide documentation to VT EMS
that verifies the curricula and attendance of members. This includes previous completion of a Resuscitation
Academy for Adult HP-CPR and Surgical Cricothyrotomy for Paramedics.
This Resource Kit has been developed to provide both EMS clinicians and EMS Services with multiple options
for completing the education.
Presentation Methods
There are several possible formats in which topics may be presented and learned:
• Individual learning:
o Vector: All presentations are on Vector and can be accessed by logging in. The course title and
course number (if applicable) are listed. Presentations on Vector may be viewed individually or
as a group. Some of the presentations have quizzes. While quizzes do not have to be completed
to receive credit remember that self-assessment is a useful tool for review and practice.
o Some topics require an additional practical skills component that must be completed at the
EMS Service level (see below).
4 ver. 01/01/2025

RESOURCE KIT
• EMS Service-level Trainings (at the department, agency, squad, etc.): To benefit from group
learning opportunities, the protocol material can be delivered in a classroom setting by several methods,
making use of qualified instructors including Training Officers, VT EMS I/Cs, hospital staff, senior
EMS crew members, DMA, Physician, etc.
o Vector: As stated above, the presentations on Vector can be done as a group. (Example:
Training Officer connects a projector to a computer at the station, logs into Vector and runs the
course live for the group.)
Required Participants:
Who is required to complete this education? The options are for EMR, EMT, AEMT, and/or Paramedic. Both
the Quick Reference Chart beginning on page 7 and each individual topic list will include which license level is
required to take each course.
Practical Skills:
Is there a practical requirement for the topic? If yes, this section will provide guidance for how to perform that
training at the EMS Service level. The practical component must be instructed by a higher-level licensure. For
example: an AEMT can instruct a practical for EMTs, or a Paramedic/RN/RT/MD can instruct a practical for
AEMT. Paramedic training should be facilitated by the Paramedic’s training officer and/or physician medical
director.
All EMS personnel are encouraged to complete training for Adult and Pediatric High-Performance CPR
(HP-CPR) annually. Paramedics are encouraged to complete training in the use of surgical airway annually.
Documentation:
Documentation of completion of both the presentation and practical components should be completed in Vector.
Enhanced permissions for Training Officers allow for group training to be entered and tracked in the Vector
accounts of all participants. In addition, each clinician should keep track of their own protocol education. At
the end of this document is a tracking template that can be utilized but does not replace Vector. Both the
5 ver. 01/01/2025

RESOURCE KIT
clinician and service should track all protocol training hours as they do for all other continuing education
requirements. Verify training using the Vector Certification System.
Implementation:
The final protocols were released February 6, 2025. Once posted, EMS Services and districts are authorized to
begin training their personnel. Before an agency may begin to use the new protocols, ALL of the agency’s
EMS clinicians must be trained on the new protocols. Once an agency has trained all their EMS clinicians, they
MAY begin to use the new protocols as of 00:01 hours on February 10, 2025. ALL agencies MUST begin to
use the new protocols as of 00:01 hours on May 1, 2025.
Any questions or concerns should be directed to vtems@vermont.gov
6 ver. 01/01/2025

| RESOURCE KIT |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |

Quick Reference Chart
Presentation Availability/Practical
| Topic/Skill  |     |     | EMR  EMT  | AEMT  | Paramedic  |
| ------------ | --- | --- | --------- | ----- | ---------- |
Component
Vector: 2025 VTEMS Protocol Introduction

| 2025 VTEMS     | EMS Service Level Training:  Use of the  |     |       |     |     |
| -------------- | ---------------------------------------- | --- | ----- | --- | --- |
| Protocol       | 2025 VTEMS Protocol Introduction         |     | X  X  | X   | X   |
| Introduction   | presentation required – 8:35             |     |       |     |     |

Practical: No
Vector:  2025 VTEMS EMT Medical

| 2025 VTEMS   | EMS Service Level Training: Use of the  |     |      |     |     |
| ------------ | --------------------------------------- | --- | ---- | --- | --- |
| EMT          | 2025 VTEMS EMT Medical presentation     |     |   X  |     |     |
| Medical      | required – 13:34                        |     |      |     |     |

Practical: No
Vector:  2025 VTEMS EMT Cardiac
| 2025 VTEMS  |                                         |     |      |     |     |
| ----------- | --------------------------------------- | --- | ---- | --- | --- |
| EMT         | EMS Service Level Training: Use of the  |     |      |     |     |
| Cardiac     | 2025 VTEMS EMT Cardiac presentation     |     |   X  |     |     |
   required – 21:44
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Practical: No
Vector:  2025 VTEMS EMT Trauma
| 2025 VTEMS  |                                         |     |      |     |     |
| ----------- | --------------------------------------- | --- | ---- | --- | --- |
| EMT         | EMS Service Level Training: Use of the  |     |      |     |     |
|             |                                         |     |   X  |     |     |
| Trauma      | 2025 VTEMS EMT Trauma presentation      |     |      |     |     |
  required – 7:04
Practical: No
| 7   |     |     |     | ver. 01/01/2025  |     |
| --- | --- | --- | --- | ---------------- | --- |

| RESOURCE KIT |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |

Vector:  2025 VTEMS EMT Airway

2025 VTEMS
EMS Service Level Training: Use of the
| EMT  |     |     |   X  |     |     |
| ---- | --- | --- | ---- | --- | --- |
2025 VTEMS EMT Airway presentation
Airway
required – 6:55
Practical: No
Vector: 2025 VTEMS EMT CPAP

2025 VTEMS
EMS Service Level Training: Use of the
| EMT   |     |     |   X  |     |     |
| ----- | --- | --- | ---- | --- | --- |
2025 VTEMS EMT CPAP presentation
CPAP
required – 12.5
Practical: YES – CPAP – Adult Only
Vector: 2025 VTEMS Behavioral 1 (EMR,
EMT, AEMT)
2025 VTEMS

Behavioral 1
|     | EMS Service Level Training: Use of the  |     | X  X  | X   |     |
| --- | --------------------------------------- | --- | ----- | --- | --- |
(EMR, EMT,
2025 VTEMS EMR, EMT, AEMT
AEMT)
Behavioral 1 presentation required – 10:11
Practical: No
Vector: 2025 VTEMS EMR, EMT, AEMT,
| 2025 VTEMS    | Paramedic Behavioral Emergencies/C-SSRS   |     |       |     |     |
| ------------- | ----------------------------------------- | --- | ----- | --- | --- |
| Behavioral    |            

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_eprip-2025-Protocol-Summary-Changes-20250917.pdf**

Vermont Statewide
Emergency Medical Services Protocols
2025
Summary of Changes

Protocol

Area/Level

Change

Comments

Preface
Section 1: General Patient Care

Legend

VEFR Routine Patient Care

VEFR

VEFR

Added - Medical Direction: EMS medical direction
refers to the guidance and oversight provided by a
licensed physician to Emergency Medical Services
(EMS) personnel in the delivery of prehospital care.
This direction is crucial to ensure that EMS
practitioners deliver appropriate and effective
treatment to patients in the field. Medical direction
is typically outlined in a protocol book, which serves
as a comprehensive reference guide for EMS
practitioners.

Online medical direction involves real-time
communication between EMS personnel and a
designated medical director using
telecommunication technologies. This allows for
immediate consultation and guidance on patient
care decisions, especially in situations where time is
critical.

Offline medical direction, on the other hand,
involves predetermined protocols and standing
orders provided by the medical director. These
protocols are established based on best practices
and evidence-based medicine, allowing EMS
providers to initiate certain treatments without
direct real-time communication with a physician.

In cases where an EMS agency is transporting a
patient across district lines, it is important to note
that medical direction may shift to the medical
director at the receiving hospital once the transport
destination is chosen that is not the local facility. This
ensures continuity of care and allows the receiving
hospital's medical director to provide guidance and
oversight during the transport and upon arrival.
Local DMA restrictions will remain in place for the
transporting ambulance.

The protocol book serves as a valuable tool for EMS
personnel, containing a detailed set of guidelines,
procedures, and protocols approved by the medical
director. It provides a standardized approach to
patient care, ensuring consistency and adherence to
established medical practices. Both online and
offline medical direction contribute to the overall
quality and safety of prehospital care provided by
EMS agencies.
Added Vermont Emergency First Responder (VEFR)
and Emergency Medical Responder (EMR) to Legend
Added two bullets under Other Skills Section:
*VEFR may not complete a VT EMS Refusal Form.
*VEFR may not cancel an ambulance unless no
patient is present or found

New Medical Direction section in
preface

New color VEFR is Tan
New color EMR is Gray
Clarifies that VEFRs cannot do a patient
refusal or cancel an ambulance (unless
there is no patient)

2025 SUMMARY OF PROTOCOL CHANGES

EMR Routine Patient Care

EMR

EMR may cancel an ambulance only when no patient
is present or found.

Same clarification as for VEFR on
canceling an ambulance

Routine Patient Care
Extended Care Guidelines

All
All

Protocol

Area/Level

Change

Comments

Section 2: Medical Protocols

Abdominal Pain (Adult & Pediatric)

Adrenal Insufficiency

Allergic Reaction/Anaphylaxis- Adult
Allergic Reaction/Anaphylaxis - Pedi

EMT - All

Altered Mental Status - Adult
Altered Mental Status - Pedi
Asthma/COPD/RAD – Adult

AEMT
Paramedic

EMT

Paramedic

Asthma/Bronchiolitis/RAD/Croup - Pedi

AEMT

Behavioral Emergencies

All

Brief Resolved Unexplained Event (BRUE)
Diabetic Emergencies (Hyperglycemia)
Adult & Pediatric
Diabetic Hypoglycemia - Adult
Diabetic Hypoglycemia - Pediatric
Epistaxis/Nosebleed Adult & Pediatric

Exertional Heat Stroke

All

For anaphylaxis, administer: (anterolateral thigh
preferred administration site)
o Epinephrine Autoinjector:
? Patients < 25 kg: Pediatric epinephrine autoinjector
0.15 mg IM
 ? Patients > 25 kg: Adult epinephrine autoinjector
0.3 mg IM,
OR
o Epinephrine (1 mg/mL):
? Patient < 25 kg: Administer 0.15 mg (0.15 mL) IM
? Patient > 25kg: Administer 0.3 mg (0.3 mL) IM
? Contact Medical Direction for additional dosing
Removed weight based dosing of epinephrine

For patients who do not respond to treatments, or
for impending respiratory failure, continue
nebulizers and consider CPAP up to a maximum of 10
– 15 cm H2O pressure support.
Clarified magnesium 2 g in 50 mL of D5W or NaCl,
not 50-100 mL
For patients who do not respond to treatments, or
for impending respiratory failure, consider:
(anterolateral thigh preferred administration site)
o Epinephrine Autoinjector:
? Patients < 25 kg: Pediatric epinephrine autoinjector
0.15 mg IM
? Patients > 25 kg: Adult epinephrine autoinjector 0.3
mg IM,
OR
o Epinephrine (1 mg/mL):
 ? Patient < 25 kg: Administer 0.15 mg (0.15 mL) IM
 ? Patient > 25kg: Administer 0.3 mg (0.3 mL) IM
Major Updates to Protocol – Please Review Entirety
Temporary vs Protective Custody

Pediatric anaphylaxis epinephrine
dosing has been simplified. All
practitioner levels may use the EMT
dosing so as to avoid having to calulate
weight-based dosing which is error
prone

See EMT dosing schedule above
Removed PO diphenhydramine, not
good for anaphylaxis, IV/IM/IO remain

CPAP moved from AEMT to EMT level –
Adults Only

Changed epinephrine to simplified fixed
doses

Reformatted and new information,
RASS, C-SSRS, Changed the phone
number to 988.  Cleaned up graphics.
Added resources for first responders.

If Tmax is at or above 40 C (104F), initiate immediate
rapid cooling to a temperature less than 40C even it
means a delay in transport

This line was changed to read “even if it
means a delay in transport” instead of
the old version which said “within 30

2025 SUMMARY OF PROTOCOL CHANGES

Hyperkalemia and Renal Failure

Hyperthermia (Environmental) A&P
Hypothermia (Environmental ) A&P
Nausea/Vomiting Adult & Pediatric
Nerve Agents/Organophosphate Adult
Nerve Agents/Organophosphate Pedi
Newborn Resuscitation

Normal Labor and Delivery

Obstetrical Emergencies

Pain Management Adult

Pain Management Pediatric
Poisoning - Adult

Poisoning – Pediatric
Seizures - Adult

minutes of collapse”.  The change was
made to clarify that if you have access
to a cold water immersion, it is more
important to cool the patient
immediately on scene, even if it means
a delay in transport.  If no cold-water
immersion is available, continue the
other cooling techniques & transport
Clarified that if whole-body cold water
emersion is not available, other cooling
means are better than nothing and
should be utilized.  Added the “if not
feasible” part of the sentence
Clarified sodium bicarbonate dose as
mEq/Kg vs 50 mEq for all patients, with
a max of 50mEq which will be the most
common dose

Clarified use of a CUFFED endotracheal
tube

Moved oxytocin to AEMT Level.

Moved oxytocin to AEMT Level.

Added consider benzo for seizure not
responding to magnesium in eclampsia
– Caution respiratory depression.
Added ibuprofen po for EMT in pain mgt
section.
Added Red Flag for Ibuprofen

Removed need to call medical direction
for ketorolac, check with your DMA for
any local restrictions

Added pearl to improve care of
overdose patients in the post-overdose
phase

All

5.c. If whole-body cold water immersion is not
feasible, utilize ice packs, fans, cold water dousing or
shower.  Rotating ice water towels covering as much
of the body surface area as possible should be
considered a minimum cooling modality enroute.”
1 mEq/Kg sodium bicarbonate (maximum dose 50
mEq) IV/IO over 5 minutes

Paramedic

AEMT

AEMT

Paramedic
Paramedic

EMT

EMT

Paramedic

If bag valve mask ventilation is inadequate or chest
compressions are indicated, intubate the infant using
a cuffed 3.0 mm to 4.0 mm endotracheal tube.
 After completion of fetal delivery(s), consider
oxytocin 10 Units IM .
After completion of fetal delivery(s), consider
oxytocin 10 Units IM .
Clarified TXA is mixed in 50-100 mL 0.9% NaCl
Consider benzodiazepine for seizures not responding
to magnesium (See Seizures – 2.22A).

In not contraindicated, consider :
Ibuprofen 600 mg PO, no repeat.
Contraindication of ibuprofen: Hypersensitivity to
ibuprofen; cerebrovascular bleeding or other
bleeding disorders, active gastric bleeding;
administration of a medication containing ibuprofen
within last 6 hours.
For mild or moderate pain, consider ketorolac 15 mg
IV or 30 mg IM (no repeat).

To reduce post overdose agitation:
* Fix hypoxia first through rescue breathing
* Utilize only enough naloxone to restore
ventilations, titrate to effect when possible
* Allow 3 to 5 minutes between naloxone doses
* Provide therapeutic environment (reduce number of
people/uniforms in room upon awakening)

EMT
Paramedic

Obtain and transmit 12-lead ECG, if available.
Clarified seizure medication orders based on if
vascular access (IV or IO) is present or absent.

Pearls

If no vascular access is present, the preferred initial
dose of benzodiazepine is midazolam IM/intranasal.
After initial dose, establish an IV in case additional
medication doses are needed. If an IV is already
established, administer benzodiazepine IV.

Added ECG to EMT section in seizure
If vascular access is absent, use
Midazolam IM (preferred) or IN.  If
vascular access is present IV
medications are preferred over IM/IN.
Updated pearl to reflect above guidance
on presence or absence of vascular
access and seizure medications

Seizure - Pediatric

2025 SUMMARY OF PROTOCOL CHANGES

Sepsis – Adult
Sepsis - Pediatric
Shock - Adult
Shock - Pediatirc

Smoke Inhalation

Stroke - Adult

Syncope – Adult & Pediatric
Section 3: Cardiac Protocols

Acute Coronary Syndrome

Bradycardia Adult
Bradycardia Pediatric
Cardiac Arrest - Adult

Paramedic

EMT

All

All

All

Norepinephrine infusion 0.1 – 2 mcg/kg/min titrated
to effect (max dose 30 mcg/min), OR, Epinephrine
0.1 – 1 mcg/kg/min titrated to effect (max dose 10
mcg/min)
Consider CPAP for respiratory distress (Continuous
Positive Airway Pressure (CPAP) – 5.4). Adults Only.

Stroke Alert should be called within 10 minutes of
recognition.
Posterior Circulation Stroke (PCS): Unlike anterior
strokes, PCS often evades detection with standard
stroke screens like CPSS and FAST-ED. Key signs
include sudden visual disturbances, loss of balance
or coordination, dizziness, or nausea and vomiting.

Balance: Perform bilateral finger-to-nose and heel-
to-shin tests to assess sudden loss of balance,
coordination issues, or trouble walking.

Eyes: Assess trouble seeing out of one or both eyes
or sudden double vision by evaluating 4 quadrants of
the visual field, having the patient locate your index
finger in each quadrant. For patients with concerning
PCS symptoms and negative stroke screens, contact
Medical Direction to consider a stroke alert.
If your local stroke plan utilizes BEFAST, See BEFAST
Appendix A.8

ALL

Pulse Check/Analysis

All

EMT

AEMT

If hypothermic arrest (Hypothermia (Environmental)
Adult & Pediatric – 2.13).
Establish IV/IO access (IV preferred when possible;
use IO if IV access cannot be established promptly.

Paramedic

Changing pad placement from anterior-apex to
anterior-posterior, or vice versa.

Paramedic

If second manual defibrillator is available consider
Double Sequential Defibrillation Procedure 6.1

Added max dose for norepinephrine
and max dose for epinephrine in
pediatric patients

CPAP moved from AEMT to EMT level
for ADULTS ONLY
JoinTriage App may be used to calculate
a score, JOIN app is no longer available
for destination determination
Added to protocol and New Red Flag

Updated the pearls on Posterior
Circulation Stroke to include more
detailed instructions on assessing
Balance and Eyes.  The stroke screening
exam may include all of the following:
B – Balance
E – Eyes
F – Facial Droop
A – Arm Drift
S – Speech
T – Time last known well.
Local stroke plans may opt to include
BE-FAST vs FAST for stroke screening

Added a hyperlink to the BEFAST
protocol for those Districts/Agencies
that under their local stroke plan will be
using BEFAST vs. FAST for initial Stroke
assessment.

Review of oxygen and ASA
administration

Added “Pulse Check” along with
Analysis on the infographic to reinforce
that

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_DEPRIP%20Policy%20-%20Psychomotor%20Exam%20Accommodations%20Requests.220525.pdf**

POLICY: PSYCHOMOTOR EXAMINATION ACCOMMODATION REQUESTS

Policy Statement:
The Vermont Department of Health complies with the Americans with Disabilities Act (ADA) of 1990 by administering
EMS testing in a manner that does not discriminate against a qualified applicant while at the same time ensuring that its
tests assess the essential skills necessary to provide quality pre-hospital care. EMS candidates have the right to request
reasonable accommodations, but accommodations will not be granted if they would compromise or fundamentally alter
the testing of skills that are required to function safely and efficiently in the profession. A description of an EMT’s
functional job responsibilities is provided in the EMS Student Manual.

Authority and References:

•  EMS Rule 12.4: A person who fails the cognitive exam or any station of the psychomotor exam at any level may

be retested in accordance with the requirements of the National Registry of EMTs (NREMT)

•  Americans with Disabilities Act of 1990
•  National Registry of EMTs ADA Accommodations Policy
•  Vermont Office of Professional Regulation Disability Accommodations Policy

Procedure:
Requests for accommodations on the psychomotor examination must be submitted in writing to the Department of Health
using the Questionnaire for Applicants Requesting Examination Accommodations, which is based on documentation
provided by the NREMT. The Questionnaire requires submission of clear, credible, written documentation from a suitable
provider sufficient to demonstrate:

1)  That the candidate has a disability
2)  The nature, severity, and duration of that disability
3)  That the requested accommodation(s) would lessen the impact of the candidate’s disability on demonstrating

essential eligibility requirements to obtain an EMS license

A “suitable provider” means a licensed health care professional who has examined the candidate and becomes oriented to
their condition and is qualified by training, education, experience, and scope of professional practice to offer an opinion
on the nature, severity, and duration of any disability found, as well as the necessity and utility of the requested
accommodation(s).

The completed Questionnaire and accompanying documentation must be received by the Department at least thirty (30)
days prior to the candidate’s desired practical exam date. The candidate must not schedule the exam until the
accommodations review is complete. The Department will consider whether the requested accommodation(s) are
reasonable and allow an examiner to adequately measure the skills required to function safely and efficiently in the
profession.

Requests for accommodations on the National Registry of EMTs cognitive exams are determined exclusively by the
NREMT and must be directed to that organization.

Rationale:
It is a primary mission of the Vermont Department of Health’s EMS Office to ensure the safe, effective delivery of pre-
hospital emergency medical care. It is therefore essential that an EMS licensure candidate is evaluated in a manner that
closely resembles the work they will perform as a practitioner of emergency care, and that any testing accommodations
granted can be realistically achieved in the field.

Effective Date:  May 24, 2022

POLICY: PSYCHOMOTOR EXAMINATION ACCOMMODATION REQUESTS | May 2022

---

**[MINUTES] 2026-06-15_DEPRIP.Exam%20Accommodations%20Questionnaire.220525.pdf**

QUESTIONNAIRE FOR APPLICANTS REQUESTING EXAMINATION ACCOMMODATIONS

Requests for accommodations on a Vermont Emergency Medical Responder or Emergency Medical
Technician psychomotor examination must include clear, credible, written documentation from a suitable
provider, sufficient to demonstrate:

a.
b.
c.

that you have a disability
the nature, severity, and duration of that disability
that the accommodation(s) you request would lessen the impact of your disability on your
ability to demonstrate essential eligibility requirements to obtain an EMR or EMT license

A “suitable provider” means a licensed health care professional who has examined you and become
oriented to your condition and is qualified by training, education, experience, and scope of professional
practice to offer an opinion on the nature, severity, and duration of any disability found, as well as the
necessity and utility of the requested accommodation(s).

Please attach this documentation to this application.

Name: _______________________________________________________________________________

Street Address: ________________________________________________________________________

City, State, Zip: _______________________________________________________________________

Email Address: ________________________________________________________________________

Please describe your disability:

What accommodation(s) are your requesting?

Vermont Department of Health – EMS Office, Revised May 2022

QUESTIONNAIRE FOR APPLICANTS REQUESTING EXAMINATION ACCOMMODATIONS

Please describe prior classroom or test accommodations you have received, including during
elementary school, secondary school, college and/or EMS training:

Certification/Authorization:
I certify that the above information is true and accurate.

Signature: ________________________________________________ Date: _______________________

Authorization for Release of Information
If clarifications of further information regarding the documentation provided is needed, I authorize the
Vermont Department of Health to contact the professional(s) who diagnosed the disability and those
entities who have provided me test accommodations. I authorize such professional(s) and entities to
communicate with the Department in this regard to provide the Department with such clarification and/or
further information.

Signature: ________________________________________________ Date: _______________________

Next Steps:

Please submit this questionnaire and supporting documentation to:

Vermont Department of Health EMS Office
ATTN: Accommodations
PO Box 70
Burlington, Vermont 05402
vtems@vermont.gov

We will send you a letter indicating the results of the accommodations review with detailed instructions.
Please do not schedule your next exam until you receive this letter. If you do, you will not receive your
accommodations and will need to reschedule.  If you have questions, please contact us at
vtems@vermont.gov.

Vermont Department of Health – EMS Office, Revised May 2022

---

**[MINUTES] 2026-06-15_EPRIP-Hearings-And-Appeals-Policy.pdf**

EMS POLICY – EMS HEARINGS AND APPEALS

Policy Statement:
When the Department denies, conditions, suspends, or revokes an EMS license or
certification, the applicant shall be afforded an opportunity to appeal the decision first to
the Commissioner of Health or designee, then to the Superior Court, and ultimately to the
Vermont Supreme Court.

Authority:
VSA 18, Chapter 17, §128 and §814
EMS Rule Section 14.4, effective February 2022

Procedural Rights:
License Denial or Conditions
When the Department denies licensure or certification, denies the renewal of an EMS
license or certification, or conditions an EMS license or certification, the applicant shall
be afforded an opportunity for a hearing with the Commissioner or designee pursuant to
the provisions of 3V.S.A. § 814.

The Department will provide applicants, certified VEFRs or licensees with notice of
license denial or conditions by mail which explains the facts or conduct that warrants the
license action and their right to a hearing with the Commissioner.

The licenses of persons seeking renewal will not expire until their application has been
finally determined by the Department so long as their renewal application was timely
made.

Suspension and Revocation
The Department may suspend or revoke the EMS license or certification of any person
upon due notice and opportunity for hearing with the Commissioner or designee for
violation of any provision of this rule or applicable statutes pursuant to the provisions of
3 V.S.A. § 814. The Department will provide these people with notice by mail of the
facts or conduct that warrants suspension or revocation.

Summary Suspension
If the Department finds that public health, safety, or welfare imperatively requires
emergency action, and incorporates a finding to that effect in its order, summary
suspension of an EMS license or certification may be ordered pending a hearing for
revocation or other action. A hearing with the Commissioner or designee will be
promptly instituted and determined.

A person subjected to license denial, conditions, suspension, summary suspension, or
revocation who is not satisfied with the Commissioner’s decision will be afforded the
right to further appeal in accordance with the following Statement of Procedural Rights.

EMS POLICY – EMS HEARINGS AND APPEALS

STATEMENT OF PROCEDURAL RIGHTS

1.  Pursuant to 18 V.S.A. § 128(a), you have the right to appeal this decision to the

Civil Division of Superior Court in the county where you reside or maintain a
business.

2.  Appeals are governed by Vermont Rule of Civil Procedure 74.

3.  Pursuant to V.R.C.P. 74(b), in order to appeal a decision, you must send a Notice

of Appeal to the designated officer of the Vermont Department of Health
within thirty (30) days of the decision:

Sarah Gregorek
Office of the Commissioner of Health
280 State Drive
Waterbury, Vermont 05671-8300

4.  Your Notice of Appeal must: specify who is taking the appeal, identify the

decision being appealed, and name the court where you are taking the appeal.

5.  Upon receipt of the Notice of Appeal, the Department of Health will provide you
with a list of all interested parties and instructions to serve all interested
parties, and the Civil Division of the Superior Court, with the Notice.

6.  Pursuant to V.R.C.P. 74(c), an appeal to Superior Court does not stay

enforcement of the Department of Health’s decision. You are obligated to
follow the decision unless you request, and the Court grants, a motion to stay
the Department’s decision pending the appeal.

7.  The Superior Court will consider the matter de novo (anew) and all persons and

parties in interest, as determined by court rule, may appear and be heard. You
have the right to bring an attorney and witnesses.

Effective Date:
January 31, 2024

---

**[MINUTES] 2026-06-15_Policy%20-%20Abuse%20Registry%20Substantiated%20Reports.pdf**

POLICY: SUBSTANTIATED ABUSE REGISTRY REPORTS

Policy Statement:
Each EMS agency is required to have a process for screening the backgrounds of their members,
employees and other sponsored personnel in the Vermont Adult Abuse Registry and Vermont
Child Protection Registry. The EMS Rule gives EMS agencies discretion to determine when and
how often to screen their affiliates; to ensure all EMS practitioners are timely screened, the
Vermont Department of Health performs these background checks when a person applies for an
EMS license or enrolls in an EMS course.

Authority:
The Department licenses EMS agencies pursuant to 18 V.S.A. § 904(b); EMS Rule 4.4.2.5 and
5.4.3.4 require EMS agencies to perform crime and abuse registry background checks on their
personnel.  At the recommendation of the Vermont Auditor of Accounts, the EMS office
performs these checks with the support of the Department for Aging and Independent Living
(DAIL) and the Department for Children and Families (DCF).

The Department may act on a personnel license for unprofessional behavior; specifically, actions
that are dangerous or injurious, or potentially so, to the public, EMS personnel, or any other
persons. EMS Rule 14.1.5.6 addresses the exercise of undue influence or taking improper
advantage of a patient. EMS Rule 14.1.5.12 addresses acting in an abusive and/or threatening
manner.

Procedure:
The Department performs background checks in the Vermont Adult Abuse Registry and the
Vermont Child Protection Registry each time a person applies for an EMS license or enrolls in
an EMS course. The Department cannot access the abuse registries without the applicant’s
permission. The applicant is free to withhold permission, but the Department will not issue the
license until these background checks are complete.

If the background check reveals a substantiated report of abuse, the applicant is not eligible for
an EMS license. A substantiation means that DAIL or DCF investigated a report of abuse or
neglect and determined there was accurate and reliable information that would lead a reasonable
person to believe that a child or adult was abused or neglected.

If the applicant believes the report is inaccurate, they can ask the [DAIL/DCF] Commissioner’s
Registry Review Unit (802-241-2321) for a review to appeal or expunge the substantiation. If the
appeal is successful, the applicant can reapply for an EMS license.

Rationale:
Protecting the public, particularly members of vulnerable populations, is the top priority of the
Department’s EMS office; routinely checking all current and potential EMS practitioners in the
abuse registries is critical to carrying out that mission.

Approved: August 15, 2020

POLICY: SUBSTANTIATED ABUSE REGISTRY REPORTS | March 2019

---

**[MINUTES] 2026-06-15_Policy%20-%20False%20Answers%20to%20Self-Disclosed%20Security%20Questions%20on%20a%20License%20Application.220930.pdf**

POLICY: FALSE ANSWERS TO SELF-DISCLOSED SECURITY QUESTIONS ON A LICENSE APPLICATION

Policy Statement:
When an applicant for EMS licensure provides a false answer to any part of the Self-Disclosed
Security Questionnaire on a license application, their EMS license (or eligibility for initial
licensure) is suspended for a minimum of thirty (30) days.

Authority:
EMS Rule 14.1.1
EMS Rule 14.1.6.11

Procedure:
On an EMS license application, current and prospective EMS practitioners must truthfully
answer six questions pertaining to illegal drug use; criminal charges and convictions; actions
taken on professional licenses held; and compliance with obligations to pay child support and
taxes. These questions are worded in a clear and concise manner, and a reasonable person could
not misconstrue them. When the applicant provides a false answer, the Department will suspend
the person’s license – or in the case of a new applicant, render the person ineligible for licensure
– for a minimum of thirty (30) days.

If the person is not satisfied with the Department’s decision, they have the right to appeal the
decision in accordance with EMS Rule.

Rationale:
It is a primary mission of the Department to protect the public and safeguard the public’s trust.
When an EMS practitioner provides false information related to past harmful or worrisome
behavior, they erode the public’s trust and diminish the system’s ability to deliver safe, effective
emergency medical care.

Effective Date:
September 30, 2022

POLICY: FALSE ANSWERS TO SELF-DISCLOSED SECURITY QUESTIONS ON A LICENSE APPLICATION

---

**[MINUTES] 2026-06-15_Policy%20-%20Impaired%20or%20Negligent%20Vehicle%20Operation.220726.pdf**

POLICY & PROCEDURE: CARELESS OR NEGLIGENT OPERATION OR DRIVING UNDER THE INFLUENCE –
FIRST OFFENSE

Procedure Summary:
A licensed Vermont EMS practitioner who is arrested for careless or negligent operation of a
motor vehicle or driving under the influence of alcohol or other substance may not operate an
ambulance for the duration of the court case and subsequent Vermont Department of Health
EMS Office (the Department) investigation.

A person with a single criminal conviction for careless or negligent operation of a motor vehicle
or driving under the influence of alcohol or other substance shall, at a minimum, be prohibited
from operating an ambulance for eighteen (18) months after the date of the arrest.

Additional criminal convictions, or a failure to report an arrest or conviction in accordance with
EMS Rule 8.4 may result in further restrictions or license actions.

Authority:
EMS Rule 8.4
EMS Rule 14.1.4
EMS Rule 14.4

Procedure:
When an EMS practitioner is arrested for careless or negligent operation of a motor vehicle or
driving under the influence of alcohol or other substance, the practitioner must report the arrest
and provide the Department with a copy of the arresting officer’s affidavit within seven (7) days
of the arrest. Unless another action is warranted, the Department will immediately condition the
practitioner’s license as bulleted below for the duration of the court case and subsequent
Department investigation.

•  The person agrees to voluntarily surrender their EMS license if charged with and/or

found to have probable cause for any other criminal offense.

•  The person cannot operate an ambulance vehicle for a period of eighteen (18) months

from the date of the arrest

When an applicant for EMS licensure has pending charges of careless or negligent operation of a
motor vehicle or driving under the influence of alcohol or other substance, the Department will,
at a minimum, condition the applicant’s license as stated above.

When an applicant for EMS licensure has a criminal conviction for careless or negligent
operation of a motor vehicle or driving under the influence of alcohol or other substance, the
Department will examine documentation of the arrest and court proceedings and consider the
timing and circumstances of the incident leading to the arrest.

If the Department’s investigation confirms that 1) the person has a single careless or negligent or
impaired driver conviction, 2) the conviction occurred more than eighteen months prior, 3) the

POLICY & PROCEDURE: CARELESS OR NEGLIGENT OPERATION OR DRIVING UNDER THE INFLUENCE – FIRST
OFFENSE

POLICY & PROCEDURE: CARELESS OR NEGLIGENT OPERATION OR DRIVING UNDER THE INFLUENCE –
FIRST OFFENSE

person has a current driver’s license, and 4) the causal incident resulted in no property damage,
injury or death, the person is eligible for a full, unconditioned EMS license.

Upon verification that the person has only a single conviction, that the incident did not result in
property damage, injury or death, and that it occurred less than eighteen months prior, the
Department will, at a minimum, issue a license with the above bulleted conditions.

If the person is not satisfied with the Department’s decision, they have the right to appeal the
decision in accordance with EMS Rule 14.4.

Policy Rationale:
An EMS practitioner’s arrest or criminal conviction for impaired, careless or negligent motor
vehicle operation represents an elevated risk to public safety and the public’s trust of the EMS
profession.

Effective Date:
January 4, 2022, revised July 25, 2022

POLICY & PROCEDURE: CARELESS OR NEGLIGENT OPERATION OR DRIVING UNDER THE INFLUENCE – FIRST
OFFENSE

---

**[MINUTES] 2026-06-15_eprip-policy-pending-criminal-charges_250425%20.pdf**

EMS POLICY – CRIMINAL CASE PENDING

Pending Criminal Charges Policy

Policy Statement:
A licensed or certified EMS clinician or applicant for licensure or certification who is
arrested or charged with a crime shall report the incident and send the arresting officer’s
citation to the Department of Health EMS Office (the Department) within seven (7) days
of the arrest. They shall provide a case status update every ninety (90) days thereafter
until a judicial determination on the case is made and the matter is concluded. Regardless
of the outcome of the case, the EMS clinician must provide all court records available to
them within thirty (30) days of the case’s conclusion.

If the person fails to report an arrest or charge within seven (7) days, a condition will be
placed on their EMS license or certification whereby, if the person fails to report a new
charge or arrest that occurs during the remainder of the current or subsequent EMS
license period, the person shall voluntarily surrender their EMS license or certification.

Failure to comply with any of the requirements may result in immediate suspension of the
person’s EMS license or certification.

Authority:
EMS Rule Section 8.4
EMS Rule 14.1.4
EMS Rule 14.1.5
EMS Rule Section 14.4

Procedure:
When a Vermont-licensed or certified person is arrested or charged with a crime, they
must notify the Department and send the arresting officer’s citation within seven (7) days
of the arrest.

Similarly, if a person is a defendant in a criminal proceeding when they apply for a
licensure, renewal, certification, or enroll in an EMS course leading to state EMS
certification or licensure, they must disclose this status by truthfully answering the crime
history questions on the application.

If the Department determines that the nature of the alleged offense has a direct bearing on
the person’s fitness to serve as EMS personnel, the Department may place conditions on
the person’s license or certification. If the actions described in the police report
demonstrate that the person presents an imminent threat to public safety, the Department
may summarily suspend the person’s EMS license or certification pursuant to EMS Rule
14.

The EMS clinician must provide court case status updates to the Department every ninety
(90) days until the case is concluded.

EMS POLICY – CRIMINAL CASE PENDING

Within thirty (30) days of the disposition of the case, the EMS clinician must provide all
court records related to the case to the Department. These include, but are not limited to,
the court docket or summary of charges and disposition.

Failure to do so may result in, at a minimum, suspension of the person’s EMS license or
certification until the Department receives the required information and is satisfied that
the submission is complete.  Such failures will be a factor in the Department's
investigation and deliberations regarding continued eligibility for certification or
licensure.

If the person fails to report the arrest, fails to truthfully disclose the arrest or criminal
conviction, or fails to supply a copy of the arresting officer’s citation as mandated by this
and any other relevant Department policies, their license or certification, or eligibility for
licensure or certification, may be summarily suspended until the police report is received
by the Department.

In the case of driving offenses see Impaired or Negligent Vehicle Operation Policy.

In the case of false answers on license applications, see False Answers to Self-Disclosed
Security Questions on a License Application Policy.

In the case of substantiated abuse registry reports, see Substantiated Abuse Registry
Reports Policy.

Persons subject to conditions, suspension, or revocation will be afforded the opportunity
for a hearing in accordance with EMS Rule 14.

Rationale:
The public affords EMS personnel a high level of trust, so the Department must respond
swiftly if it receives credible information that an EMS practitioner has engaged in
behavior that puts the public at risk.  While all persons are considered innocent of a crime
until found guilty by a court of law, the Department must consider the potential harm to
the public, particularly vulnerable populations, and respond in a manner and urgency
commensurate to the hazard posed by the alleged crime.

Effective Date:
September 27, 2022
Updated: April 25, 2025

---

**[MINUTES] 2026-06-15_pre-Policy-RN-PA-Advanced-Placement-April-2026.pdf**

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY ADVANCED PLACEMENT

Policy Statement:
This policy allows registered nurses, physician assistants, hospital corpsmen/medics in the
United States Armed Services and veterans who served in these roles to obtain a National
Registry certification and a Vermont EMS license without first taking a full EMS course.

Authority:
V.S.A. 18, Chapter 17 §906 (10) (E)
EMS Rule Section 9.3, effective February 2022

Procedure:
A person covered by this policy must be affiliated with a Vermont-licensed EMS agency that is
licensed at the person’s desired license level. The person may apply for Vermont licensure at the
EMR, EMT and AEMT levels upon completion of National Registry of EMTs testing by
meeting the following requirements:

1)  Submission of an RN/PA/Military Challenge application in the LIGHTS system
2)  Advanced placement evaluation by a National Registry of EMTs Program Director
(VT-licensed EMS Instructor/Coordinator) selected by the Vermont State Training
Administrator. Immediate availability of a NREMT Program Director is not
guaranteed. The NREMT Program Director must verify that the applicant has
received training on the gap material between the Registered Nurse, Physician
Assistant, hospital corpsman or medic curriculum and the learning objectives for the
desired EMS license level, and that the applicant’s skills at the desired level have
been verified in accordance with Vermont Department of Health standards.

3)  Verification by the person’s primary agency’s training officer, head of service, and
District Medical Advisor that the person has the skills, knowledge, and affective
competency to function at the desired license level.

4)  Application for a National Registry certification on the NREMT website

(www.nremt.org), identifying the Instructor/Coordinator as your NREMT Program
Director

5)  Course completion verification by the NREMT Program Director on your NREMT

application

6)  At the AEMT level, hold a national EMT certification or state EMT license
7)  Successful completion of the NREMT cognitive examination

A person covered by this policy may apply for Vermont licensure at the Paramedic level
without a full Paramedic course by meeting the requirements above, except that course
completion verification must be done by the Program Director of a Paramedic program
accredited by the Commission on Accreditation of Allied Health Education Programs
(CAAHEP).

Due to changes under consideration at the NREMT for 68 Whiskey military medics, a pathway
for military medics may not exist at this time. Once the NREMT procedures have been finalized,

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY ADVANCED PLACEMENT

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY ADVANCED PLACEMENT

further action by the Vermont Legislature may be required to continue advanced placement for
military medics.

The application and testing process is as follows:

1)  Department approval of an RN/PA/Military Challenge application in the LIGHTS system
2)  Creation of an online National Registry of EMTs account at www.nremt.org and an

application for the desired national certification level

a.  Request that the Department pay the cognitive exam fee by submitting a

“NREMT Cognitive Exam Fee Payment Request” application. NOTE: A person
must be affiliated with a Vermont-licensed EMS agency to qualify for exam fee
payment

b.  Select as your instructor the NREMT Program Director who verified your gap

training

3)  The NREMT Program Director verifies course completion through their online NREMT

account.

4)  Upon successful completion of the NREMT exams and receiving a NREMT certification,

apply for a Vermont EMS license via the Vermont LIGHTS portal.

Rationale:
This policy recognizes that registered nurses, physician assistants, hospital corpsmen and
military medics possess clinical training that approximates and, in some cases, exceeds that of
licensed emergency medical clinicians. After an EMS instructor/coordinator has identified and
addressed any gaps between the prior education and applicable EMS curriculum, the applicant’s
primary EMS agency has attested that the applicant has the requisite skills, knowledge, and
affective competency, and the applicant passes the National Registry cognitive exam, they
should be allowed to obtain a National certification and a Vermont license.

Effective Date:
January 19, 2019, revised March 25, 2021, October 30, 2024, September 18, 2025, and April 13,
2026

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY ADVANCED PLACEMENT

---

**[MINUTES] 2026-06-15_Policy%20-%20RN%20PA%20Challenge.210325.pdf**

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY CHALLENGE

Policy Statement:
This policy allows registered nurses, physician assistants, hospital corpsmen/medics in the
United States Armed Services and veterans who served in these roles to obtain a National
Registry certification and a Vermont EMS license without first taking a full EMS course.

Authority:
V.S.A. 18, Chapter 17 §906 (10) (E)
EMS Rule Section 9.3, effective February 2022

Procedure:
Persons covered by this policy who are affiliated with a Vermont-licensed EMS agency may
apply for Vermont licensure at the EMR, EMT and AEMT levels upon completion of National
Registry of EMTs testing without prior EMS education by meeting the following requirements:

1)  Verification by a National Registry of EMTs Program Director (VT-licensed EMS
Instructor/Coordinator) that the applicant has received training on the gap material
between the Registered Nurse, Physician Assistant, hospital corpsman or medic
curriculum and the learning objectives for the desired EMS license level, and that the
applicant’s skills at the desired level have been verified in accordance with Vermont
Department of Health standards.

2)  Application for a National Registry certification on the NREMT website

(www.nremt.org), identifying the Instructor/Coordinator as your NREMT Program
Director

3)  Course completion verification by the NREMT Program Director on your NREMT

application

4)  At the AEMT level, hold a national EMT certification or state EMT license
5)  Successful completion of the NREMT cognitive examinations

Persons covered by this policy may apply for Vermont licensure at the Paramedic level without
prior EMS education by meeting the requirements above, except that course completion
verification must be done by the Program Director of a Paramedic program accredited by the
Commission on Accreditation of Allied Health Education Programs (CAAHEP).

The application and testing process is as follows:

1)  Create an online National Registry of EMTs account at www.nremt.org and initiate an

application for the desired license level

a.  Request that the Department pay the cognitive exam fee by submitting a

“NREMT Cognitive Exam Fee Payment Request” application. NOTE: A person
must be affiliated with a Vermont-licensed EMS agency to qualify for exam fee
payment

b.  Select as your instructor the NREMT Program Director who verified your gap

training

2)  The NREMT Program Director verifies course completion through their online NREMT

account.

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY CHALLENGE

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY CHALLENGE

3)  Upon successful completion of the NREMT exams and receiving a NREMT certification,

apply for a Vermont EMS license via the Vermont LIGHTS portal.

Rationale:
This policy recognizes that registered nurses, physician assistants, hospital corpsmen and
military medics possess clinical training that approximates and, in some cases, exceeds that of
licensed emergency medical practitioners. After an EMS instructor/coordinator has identified
and addressed any gaps between the prior education and the applicable EMS curriculum and the
applicant passes the National Registry psychomotor and cognitive exams, they should be allowed
to obtain a National certification and a Vermont license.

Effective Date:
January 19, 2019, revised March 25, 2021, and October 30, 2024

POLICY: REGISTERED NURSE/PHYSICIAN ASSISTANT/MILITARY CHALLENGE

---

**[NOTICE] 2026-06-15_EPRIP_InstructionsForPublicNotice2013Aug26.pdf**

Instructions for Posting a Public Notice

Before your application can be reviewed by the local EMS District Board, a public notice
stating your licensure intentions must be printed in the local newspaper of general
circulation for the intended service area.  The applicant should contact the EMS District
Board as early as possible to schedule a meeting after the deadline for public comments.

The public comment period should be set at least 14 days from the date the notice is
published.

The Department of Health will forward all comments to the applicant and the local District
Board.  The District Board with then review the application, any comments received, and
forward a recommendation regarding licensure to the Department.

Please contact the EMS Office at vtems@vermont.gov if you have questions on the public
notice process. The format template is shown below.

PUBLIC NOTICE

The (insert EMS agency name) has identified the need for a(n) (First Responder Agency or
Ambulance Agency) to operate in (list cities/towns of operation) and is applying for
licensure by the Vermont Department of Health. This agency proposes to begin operations
on (insert date) within the geographic boundaries of (list boundaries here). In accordance
with 24 V.S.A. Emergency Medical Services Statute, public comments are invited to be
received by the Department by (insert date 14 days after notice publication).

Address comments to:

Vermont Department of Health
Office of Emergency Medical Services
280 State Drive
Waterbury, Vermont 05671-8330

---

**[MINUTES] 2026-06-15_AEMT%20test%20instructions.pdf**

Testing and Licensure Information for Advanced Level Instructors
The testing and state licensing procedures for Advanced-EMT and Paramedic are different
from the process for becoming an EMR or EMT. At the lower levels, the registration and
management of the psychomotor examinations are handled by the state EMS office. At the
higher levels, the exams are managed by the NREMT with only minimal involvement by
the state office.

Please be sure that your students and their agency leadership understand that  the course
and the preceptor-supervised clinical internship end when the student takes the NR-AEMT
or NRP cognitive exam. Once the course ends, students may no longer perform Advanced
level skills until they obtain their Vermont AEMT or Paramedic license. Likewise, your
students  may  not  take  the  cognitive  exam  until  all  course  requirements  have  been
completed, including paying the course fee in full and finishing their clinical observation
time.

As  of  February  2017,  advanced  level  students  may  qualify  for  the  practical  exam  upon
completion of the course’s didactic and lab requirements (and before finishing their clinical
requirements) through NREMT’s Early Eligibility Verification process. See the Program
Director section of the NREMT website for more information on this option.

The  following  is  important  information  to  help  your  students  register  for  an  Advanced
Level exam and obtain a state license:

1)  Psychomotor  exam  sites  are  held  every  month  in  different  parts  of  the  state.
However,  if  you  would  like  to  hold  an  independent  test  site,  you  must  submit  a
Request  for  Independent  Exam  Site  form  (found  in  the  Documents  section  at
www.vermontems.org)  no  later  than  TWO  MONTHS  prior  to  the  desired  exam
date.  We will arrange with the NREMT for approval and provide a NREMT on-
site proctor. In addition to having sufficient equipment and qualified evaluators, you
must have an emergency physician on site or available by telephone for the duration
of the exam site. For detailed information about the psychomotor skill stations, go
to the NREMT website at www.nremt.org.

2)  Your  students  must  create  a  NR-AEMT  or  NRP  Application  online  before

beginning the testing process.

3)  Unlike for EMR and EMT exam sites, your students do not need to submit an exam
application prior to the psychomotor exam date. It is your responsibility to register
your  students  for  the  psychomotor  exam  by  submitting  a  list  of  their  names  and
Practical Authorization to Test (PATT) numbers to the EMS Office at least TWO
WEEKS prior to the exam date. The PATT number is provided after the student has
completed  their  online  NR-AEMT  application.  Students  whose  names  are
submitted less than two weeks before the exam date may not be admitted to the test
site.

4)  Each student will be assigned just one PATT number. If they need to retest a failed
skill station, they must wait until NREMT scores their exam and reactivates their
PATT number.

5)  The  Vermont  Department  of  Health  will  pay  for  all  attempts  on  the  NREMT
computer-based  cognitive  exam  for  candidates  who  hold  an  affiliation  with  a
Vermont EMS agency licensed at the Advanced level. When your students register
for the test, instruct them to select “Direct Bill to Home State” as the Application
Payment method.

6)  You will need to be approved by the NREMT as an AEMT or Paramedic Program

Director before your students can register for the cognitive exam.

7)  When your students receive their NR-AEMT or NRP certification card, they must
apply  for  state  licensure  by  submitting  a  Vermont  AEMT  or  Paramedic  license
application  and  a    copy  of  their  NREMT  certification  card  to  the  EMS  Office.
Possession  of  a  NR-AEMT  or  NRP  card  alone  is  not  sufficient  to  practice  in
Vermont.

If you have any questions about the Advanced Level testing and licensing process, please
don’t hesitate to contact the EMS Office at 800-244-0911 or 802-863-7310.

---

**[MINUTES] 2026-06-15_NASEMSO-AEMT-SMC-1.2%20Revised%206.14.24.pdf**

Advanced Emergency
Medical Technician
Student Minimum Competency
Model Guideline
Adopted:
Revised:

AEMT Student Minimum Competency Model Guideline
THIS PAGE INTENTIONALLY LEFT BLANK
© 2023 NASEMSO. All Rights Reserved 1

AEMT Student Minimum Competency Model Guideline
Department of Health Agency of Human Services
Division of Emergency Preparedness,
Response & Injury Prevention [phone] 802-863-7310
Emergency Medical Services & Injury Prevention [fax] 802-863-7577
108 Cherry Street – PO Box 70 [toll free] 800-244-0911
Burlington, VT 05402-0070 [email ] vtems@vermont.gov
http://www.vermontems.org
November 12, 2023
EMS Education Program Directors,
The Department of Health is adopting the Advanced Emergency Medical Technician (AEMT)
Student Minimum Competency Model Guideline, developed by the National Association of State EMS
Officials (NASEMSO), as the minimum standard for the verification of AEMT student minimum
competencies, with a limited number of exceptions. Exceptions to the original document are limited to:
• Table 1, Ages- Students must have a minimum of twenty (20) live patient exposures in the
prehospital emergency care setting.
• Table 2, Pathology/Complaints (Conditions)- The minimum of each specific age and
pathology may be met through simulation once the minimum of the twenty (20) patient
exposures in the pre-hospital emergency care setting has been met. Simulation vs live patient
exposures are based upon pathology or complaint. Simulation is permissible in specific
situations based on competency determination by the Program Director and course Medical
Advisor.
• Table 3, Minimum Skills Competency-Documents the minimum number of successful
psychomotor skills assessed during the laboratory, clinical, or pre-hospital field experience.
• Table 4, Pre-Hospital Emergency Field Experience- Documents the formative and
summative assessment requirements during the pre-hospital emergency field experience
intended to build student proficiency and confidence as an Advanced Emergency Medical
Technician (AEMT) in the field.
More than a year ago, the National Registry of Emergency Medical Technicians (NREMT)
announced that psychomotor testing for Advanced Emergency Medical Technician (AEMT)
certification would be coming to an end. A new AEMT Certification Examination would be replacing
the current cognitive exam. This exam measures cognitive and psychomotor entry-level competency of
the candidate in a single examination. In the absence of a psychomotor exam, the verification and
documentation of AEMT student motor skills will occur during the AEMT course.
This guideline is intended to maximize efficiency, consistency of instructional quality, and
student competence. Staff from the Office of Emergency Medical Services have worked collaboratively
with EMS educators, the EMS Education Council, and the EMS Advisory Committee, to inform and
refine this guideline. The guideline is schedule for review and updating in 2025.
Sincerely,
Bambi L. Dame
Bambi Dame, NRP
State EMS Chief
© 2023 NASEMSO. All Rights Reserved 2

AEMT Student Minimum Competency Model Guideline
Table of Contents
Disclaimer ................................................................................................................................. 4
Preface ...................................................................................................................................... 5
Acknowledgments .................................................................................................................... 7
Introduction .............................................................................................................................. 8
Principles of Design .................................................................................................................. 9
Ages ........................................................................................................................................ 11
Pathology/Complaint (Conditions) .......................................................................................... 12
Skills ........................................................................................................................................ 15
Field Experience/Capstone Field Internship ........................................................................... 19
EMT Skills ................................................................................................................................ 19
COVER PHOTOGRAPH BY JAY HEIKE ON UNSPLASH.
© 2023 NASEMSO. All Rights Reserved 3

AEMT Student Minimum Competency Model Guideline
Disclaimer
The National Association of State Emergency Medical Services Officials (NASEMSO) is the
association of the state EMS offices within all 50 states, the five territories, and the District
of Columbia.
NASEMSO affirms the authority and sovereignty of the states regarding the establishment of
law and administrative rules governing the regulation and practice of emergency medical
services (EMS). This includes requirements related to initial EMS education that in part
prepares individuals for state licensure.
As the 501(c)3 association formed by these state offices, NASEMSO collaborates with other
Federal and national EMS stakeholders and subject matter experts to develop guidance
documents to aid state EMS offices in interpreting and implementing new practices and
policies within the states. These documents should not be interpreted as directives nor as
superseding the authority properly delegated to a state EMS office. Rather, these guidance
documents are provided for the use of the state EMS regulating authorities and may be
modified or adopted in part or whole as those authorities deem appropriate.
EMS agencies, personnel, and educational institutions seeking clarification on EMS issues
should contact their state’s regulatory body, a list of which may be found at:
https://nasemso.org/about/state-agencies/.
NASEMSO reserves the right to amend, revise, or retract this document based on expert
and/or member consensus.
This document is available in Microsoft Word to state EMS officials for adaptation into a
state-specific document.
Suggested Citation:
National Association of State EMS Officials. Advanced Emergency Medical
Technician Student Minimum Competency Model Guideline. 2023.
© 2023 NASEMSO. All Rights Reserved 4

AEMT Student Minimum Competency Model Guideline
Preface
This document is a model guidance document that provides recommendations to state, the
District of Columbia, Puerto Rico, and territory (hereinafter “states”) Emergency Medical
Services (EMS) offices and Advanced Emergency Medical Technician (AEMT) Program
Directors for verification of student minimum competencies (SMC). It is important to note
that state EMS offices are responsible for the approval and standards for initial AEMT
programs. As such, the state EMS office is the approving organization, and state EMS office
requirements supersede any recommendations in this document. Please consult your state
EMS office for specific requirements in your jurisdiction.
To the extent possible, this document was created to provide recommendations for the
verification of AEMT student minimum competencies in a manner that is consistent with the
Paramedic Student Minimum Competencies as established by the Commission on
Accreditation of Allied Health Education Programs (CAAHEP). EMS programmatic
accreditation is overseen by its Committee on Accreditation of Educational Programs for the
EMS Professions (CoAEMSP).
This approach was selected to align the tracking of student minimum competencies so that
skills and competency tracking can use similar software tools and recognizing that many
AEMT training programs are integrated with paramedic educational programs. Consistent
templates and data for SMC tracking may also assist advanced placement opportunities for
AEMTs to continue preparation for paramedic certification to reduce redundancy in skills
verification.
Additionally, this document was designed to build upon and harmonize with the 2019
National EMS Scope of Practice Model that was produced by the National Association of
State EMS Officials (NASEMSO), with support from the U.S. Department of Transportation,
National Highway Traffic Safety Administration, Office of EMS, and with additional
supplemental funding from the Health Resources and Services Administration’s Emergency
Medical Services for Children Program.
This model guideline endeavors to maximize efficiency, consistency of instructional quality,
and student competence. Further, it supports a system of EMS personnel licensure that is
consistent with other healthcare occupations and is a guide for states when developing
legislation, rules, and regulations related to AEMT student minimum competencies. The
Scope of Practice Model has been used as a model by states to increase regulatory
uniformity in the profession.
Beginning July 1, 2024, the National Registry will require verification by the AEMT Program
Director that student minimum competency has been verified in compliance with state EMS
office requirements and in a manner consistent with this document. The National Registry
© 2023 NASEMSO. All Rights Reserved 5

AEMT Student Minimum Competency Model Guideline
anticipates updating this document on a regular cycle to ensure consistency with upcoming
EMS Scope of Practice revisions, ALS Practice Analysis, and Paramedic SMC documents.
This model guideline is intended to describe a recommended minimum standard that is
accessible for AEMT educational programs, while acknowledging variation between state
EMS office requirements. Recognizing existing variation between states, absolute
compliance with these recommendations is not anticipated during the initial
implementation. The National Registry recommends that the state EMS office reviews
existing requirements and considers the appropriate ways to address variations in ways that
meet local implementation challenges with the goal of substantial consistency with these
recommendations.
State EMS offices and AEMT programs should not interpret this document as a ceiling for
experiences, but as a recommended consistent minimum standard.
It may be helpful to refer to the implementation guidance for the CoAEMSP Paramedic
Student Minimum Competency document for comparison and background information. It is
important to note that state EMS offices are responsible for the approval and standards for
initial AEMT programs. The National Registry does not require submission of information to
the National Registry. Please refer to your state EMS office for specific requirements,
including any reporting requirements. Paramedic Student Minimum Competency Resource
documents include:
• CoAEMSP Student Minimum Competency Recommendations Frequently Asked
Questions (FAQ)
• CoAEMSP and NREMT Simulation Guidelines and Recommendations
© 2023 NASEMSO. All Rights Reserved 6

AEMT Student Minimum Competency Model Guideline
Acknowledgments
The National Association of State Emergency Medical Services Officials would like to
acknowledge and thank the experts who contributed their time and effort to the project.
Extensive dialogue, as well as the sharing of knowledge and experience, brought about
compromise, convergence, and consensus of ideas. The contributing members are listed
below.
COMMITTEE ON ACCREDITATION OF NATIONAL ASSOCIATION OF EMS EDUCATORS
EDUCATIONAL PROGRAMS FOR THE EMS Gary Bonewald, MEd, LP (Texas)
PROFESSIONS Ron Lawler, BUS, NRP (North Dakota)
Mike Miller, EdD, RN, NRP (Nebraska)
NATIONAL ASSOCIATION OF STATE EMS NATIONAL REGISTRY OF EMTS
OFFICIALS Alan Arguello, MBA, PMP, NRP (Ohio)
Deb Akers, NRP (Virginia) Bill Lehman, BA (Oregon)
Dawn Felt, MPA, NRP (Washington) Gail Fitzpatrick (North Carolina)
Ryan Greenberg, MBA, NRP (New York) Paul Rosenberger, EdD, NRP (Texas)
Wendy Snodgrass, NRP (Nebraska) Mark Terry, MPA, NRP (Retired) (Ohio)
Brian Webb, NRP (Alas

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_Policy%20-%20Course%20Medical%20Director%20Qualifications.230412.pdf**

EMS POLICY – COURSE MEDICAL DIRECTOR

Policy Statement:
All emergency medical services courses leading to a National Registry of EMTs
(NREMT) certification, or a Vermont EMS license or certification, must have oversight
by a course medical director who is a licensed physician with sufficient emergency
medicine experience to verify the medical accuracy of the emergency medical services
course and assess the knowledge, skills, and affective competency of emergency medical
services students.

Authority:
EMS Rule 9.1.2:
Physician medical oversight must be obtained for each course for the purpose of ensuring
medical accuracy of the course content.

Procedure:
The course instructor must select an emergency medical physician to provide oversight of
the course. The course medical director is the course’s ultimate medical authority. They
are responsible for ensuring the accuracy and quality of the course content, and for
verifying the knowledge, skills, and affective competency of each student before the
student is approved for NREMT certification or Vermont EMS licensure or certification.

The course medical director serves as the instructor’s liaison with the broader medical
community in two important ways.  One is by bringing in specialists where appropriate to
provide deeper medical knowledge or context to the course content. The other is to assist
the course instructor with establishing clinical affiliations with medical facilities for
courses that require a clinical internship.

Rationale:
Emergency medical services is a specialized field with many considerations not found in
other areas of health care. Emergency medicine involves urgently assessing and treating
ailments in potentially unpredictable conditions. The nature of pre-hospital emergency
medicine requires its practitioners to think quickly, independently, and critically to
diagnose and treat patients with minimal supervision. Therefore, an EMS practitioner’s
training must be directed by a clinician with a strong understanding of the unique aspects
of field-based emergency medical treatment.

Effective Date:
April 12, 2023

---

**[MINUTES] 2026-06-15_DEPRIP.%20Heart%20Safe%20Application%202020.pdf**

HEART
SAFE
F O U N D A T I O N
HeartSafe Community
Application Packet
This application is provided by:
Vermont EMS
For more information, see
Please email a completed application
www.heartsafefoundation.org packet and all attachments in electronic
format to: vtems@vermont.gov or mail to:
HeartSafe Foundation © 2017
VT EMS
PO Box 70
Burlington, VT 05402-0070

THE HEARTSAFE FOUNDATION APPLICATION: PREFACE
Sudden cardiac arrest (SCA) is a leading cause of death in the United States and world. More than
350,000 people annually in the US will suffer out-of-hospital cardiac arrest (OHCA) and most victims
die unless HeartSafe program initiatives are implemented and followed. Once a proper HeartSafe
program is established, survival rates sky rocket and many lives are saved that previously would have
been lost. SCA affects any age, any gender and any race. Unlike many other medical conditions,
survival from SCA depends on immediate intervention by bystanders or designated first responders
on scene; immediately performing at least hands only Cardiopulmonary Resuscitation (CPR) on the
affected person and using an Automated External Defibrillator (AED) as soon as possible.
The HeartSafe Foundation has been established to help further the cause of setting up proper
HeartSafe programs that improve SCA survival rates and prevent SCA-related deaths. HeartSafe
programs support the “cardiac chain of survival” reinforced by the American Heart Association and
encourage communities to work toward early recognition and response for any SCA-related event.
The Foundation is nationally focused but has global and unlimited reach. The HeartSafe Foundation
program designation applications exist for communities, zones, schools or campuses, workplaces
and / or hospitals. The HeartSafe Foundation evaluation & review system uses established best
practice standards and provides a common ground for rating or scoring HeartSafe programs, globally.
The goal of The HeartSafe Foundation is to allow for flexibility in the HeartSafe program to meet the
local needs of the applicant, region or area; yet ensure core focus on important categories known to
improve SCA survival rates.
This application will help facilitate and document collaboration with community partners and
organizations that will impact and improve SCA survival rates. This application serves to
promote your Heartsafe program achievements, development, progression, and best
practices while showcasing your HeartSafe designation certification and rating.

HeartSafe Designation & Rating System
A HeartSafe program’s rating and designation will be calculated using the following focused assessment criteria and five
program categories.
Each of the focus areas below earn 1 heart per category, based upon information provided. Any HeartSafe program can
earn up to 5 hearts. The number of accumulated hearts will determine the level of rating the program achieves. HeartSafe
designations can change over time and be upgraded upon request with an application resubmission at any time, if they
are assigned lower than a 5 heart rating. The rating will be reviewed as needed (if an upgrade is desired), or at least every
3 years once a five heart designation rating is achieved.
CATEGORY ONE: Training Focus
Cardiopulmonary Resuscitation (CPR) & Automated External Defibrillator (AED) Education. Regularly
occurring training sessions for CPR and automated external defibrillator (AED) use are being conducted in the
community. This training improves early recognition of heart attack or sudden cardiac arrest signs & symptoms
and allows for more immediate calling of 9-1-1 or the designated emergency number and reinforces early CPR
and quick use of any nearby automated external defibrillation (AED).
CATEGORY TWO: Public and Private AED Placement Focus
Public Access Defibrillator (PAD) Placements. AEDs are placed in public and private locations that are key areas
for improving community AED response times, and with public safety and designated first responders (usually
law enforcement officials) to improve access to early defibrillation while waiting for EMS or 9-1-1 advanced
care to arrive. Written Emergency Action Plans (EAPs) and community-wide AED protocols are established,
implemented into training, and communicated and reviewed on a regular basis.
CATEGORY THREE: Advanced Cardiovascular Life Support (ACLS) Focus
Advanced Care or EMS Care Involvement. Advanced care is engaged (including dispatch 9-1-1 centers)
in improving survival rates and a lead organization is designated that will oversee the HeartSafe initiatives.
Advanced care personnel are arriving early on scene to assist and use any advanced care or specialty ACLS
equipment (including 12 lead ECG or manual defibrillators and other monitoring or compression assist devices)
due to being dispatched to sudden cardiac arrest and heart attack events quickly. Advanced care is also engaged
in preventing SCA, and improving plus evaluating cardiovascular health in the community. This includes ready
access to screenings and counseling for risk reduction or referral to quality physician for followup care.
CATEGORY FOUR: Technology Focus
Updated Technology Involvement. Technology is used to monitor and ensure continual upkeep the health and
well being of the Public Access Defibrillator (PAD) or pertinent AED program. Information produced by the
technology tools or in the technology solutions enables appropriate levels of transparency of program data
and sharing of information with all PAD program administrators or other stakeholders and use by the PAD
participants, as appropriate. Cardiac Arrest Registry to Enhance Survival (CARES) or similar registry database
systems are engaged locally, that allow use by all entities and enforce the tracking of data for any AED use and
CPR event, enabling continuous quality improvement.
CATEGORY FIVE: Mobile Technology & Social Media Focus
Mobile & Phone Technology Notifications. Technology is engaged by designated dispatch systems (including
Public Safety Answering Points or PSAPs for zones or communities applying) and appropriate alerting parties
that use computers and mobile devices and/or smart phones/iPhones® social media, messaging, or other
pushed/call notifications to improve communication regarding an emergency in progress and improve response
times for CPR and AED use.

PART
ONE
HeartSafe Community Application

Part One: HeartSafe Community Application
Note: HeartSafe Programs will not have points or rankings taken away by missing fields. Each program is expected to be
different to meet the needs of the local community. Provide as much detail as possible that is relevant to your pending,
current, or soon to be updated HeartSafe Program to ensure an accurate rating will be assigned.
Please provide: Additional details at the end of the packet on pages 20 and 21 for any sections needing more detail or
attach another sheet with pertinent information.
SECTION A: HeartSafe Program Name / Address
HeartSafe Program Name:
PART HeartSafe Main Contact Name:
Address:
ONE
| City:  |      | State: |        | Zip: |
| ------ | ---- | ------ | ------ | ---- |
| Phone: | Fax: |        | Email: |      |
HeartSafe Community Application
| Community Population: |     | Geographic Region |     |     |
| --------------------- | --- | ----------------- | --- | --- |
SECTION B: Elected Officials Involved
| Name: |     | Job title: |     |     |
| ----- | --- | ---------- | --- | --- |
Address:
| City:                  |      | State:     |        | Zip: |
| ---------------------- | ---- | ---------- | ------ | ---- |
| Phone:                 | Fax: |            | Email: |      |
| Medical Director Name: |      | License #: |        |      |
If additional, please attach another sheet with pertinent information noted above.
SECTION C: EMS Agency Contact 1
?  Intermediate              ?  ALS              ?  BLS              ?  Transport ________ # Vehicles              ?  AED Equipped
| Organization/Agency: |     | Contact: |     |     |
| -------------------- | --- | -------- | --- | --- |
Address:
| City:                  |      | State:     |        | Zip: |
| ---------------------- | ---- | ---------- | ------ | ---- |
| Phone:                 | Fax: |            | Email: |      |
| Medical Director Name: |      | License #: |        |      |
SECTION D: EMS Agency Contact 2
?  Intermediate              ?  ALS              ?  BLS              ?  Transport ________ # Vehicles              ?  AED Equipped
©2017 HeartSafe Foundation – Page 5

| Organization/Agency: |     | Contact: |     |     |
| -------------------- | --- | -------- | --- | --- |
Address:
| City:                  |      | State: |            | Zip: |
| ---------------------- | ---- | ------ | ---------- | ---- |
| Phone:                 | Fax: |        | Email:     |      |
| Medical Director Name: |      |        | License #: |      |
If additional, please attach another sheet with pertinent information noted above.
SECTION E: Advanced Life Support (ALS) Agency
?  Transport ________ # Vehicles          ?  12 lead equipped?
| Organization/Agency: |     | Contact: |     |     |
| -------------------- | --- | -------- | --- | --- |
Address:
| City:                  |      | State:     |        | Zip: |
| ---------------------- | ---- | ---------- | ------ | ---- |
| Phone:                 | Fax: |            | Email: |      |
| Medical Director Name: |      | License #: |        |      |
If additional, please attach another sheet with pertinent information noted above.
SECTION F: Critical Care Hospital Or Cardiac Specialty Center
| Organization/Agency: |     | Contact: |     |     |
| -------------------- | --- | -------- | --- | --- |
Address:
| City:                  |      | State:     |        | Zip: |
| ---------------------- | ---- | ---------- | ------ | ---- |
| Phone:                 | Fax: |            | Email: |      |
| Medical Director Name: |      | License #: |        |      |
If additional, please attach another sheet with pertinent information noted above.
SECTION G: Dispatch / PSAP Agency
Check if applicable:
?  Primary Dispatch           ?  EMD           ?  e-911           ?  Other_________________________           # dispatchers__________
| Organization/Agency: |     | Contact: |     |     |
| -------------------- | --- | -------- | --- | --- |
Address:
| City:                  |      | State:     |        | Zip: |
| ---------------------- | ---- | ---------- | ------ | ---- |
| Phone:                 | Fax: |            | Email: |      |
| Medical Director Name: |      | License #: |        |      |
 Page 6  – ©2017 HeartSafe Foundation

If additional, please attach another sheet with pertinent information noted above.
|     | SECTION H: Police or Law Enforcement  |     |     | ?  Check if designated |
| --- | ------------------------------------- | --- | --- | ---------------------- |
  first responder
Contact 1
?  Transport ________ # Vehicles              ?  AED Equipped              ?  Other_________________________
| Organization/Agency: |     | Contact: |     |     |
| -------------------- | --- | -------- | --- | --- |
Address:
| City:                  |      | State:     |        | Zip: |
| ---------------------- | ---- | ---------- | ------ | ---- |
| Phone:                 | Fax: |            | Email: |      |
| Medical Director Name: |      | License #: |        |      |
?  Check if designated
SECTION I: Police or Law Enforcement
|     |     | Contact 2 |     |   first responder |
| --- | --- | --------- | --- | ----------------- |
?  Transport ________ # Vehicles              ?  AED Equipped              ?  Other_________________________
| Organization/Agency: |     | Contact: |     |     |
| -------------------- | --- | -------- | --- | --- |
Address:
| City:                  |      | State:     |        | Zip: |
| ---------------------- | ---- | ---------- | ------ | ---- |
| Phone:                 | Fax: |   

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_eprip-EMSAC-Final-Report-2025.pdf**

Vermont Emergency Medical Services System Assessment
December 15, 2025
Emergency Medical Services Advisory Committee Report

Executive Summary
Vermont’s EMS system is rooted in service, community values, and an unwavering commitment
to ensuring that every person—regardless of geography—has access to reliable, equitable, and
high-quality emergency medical care. Today, Vermont stands at a pivotal moment. With
strategic investment, collaboration, and a shared vision, there is an opportunity to build a more
coordinated and sustainable EMS system—one that strengthens the workforce, supports
providers, and enhances patient care statewide. By embracing innovation and planning for long-
term resiliency, Vermont can shape an EMS system that not only meets today's needs but also
elevates the future of emergency medical care for generations to come.
The Vermont EMS assessment—compiled from statewide data collection, cost reports, and
system surveys—reveals a complex and uneven landscape. Call volumes are rising, workforce
shortages are worsening, and financial deficits are deepening. The total annual system cost is
approximately $98 million, but insurance reimbursement covers only $53 million, leaving local
taxes and volunteers to bridge a widening gap.
The recent passage of Act 157 of 2024, which formally designates EMS as an essential service,
is an important policy milestone. However, without aligned funding, governance reform, and
workforce investment, Vermont's EMS system cannot reliably continue to deliver equitable,
high-quality emergency care to all residents.
Emergency Medical Services
Emergency Medical Services is an integrated system of emergent and non-emergent practice of
medicine in the out-of-hospital environment. This includes personnel and resources designed to
assess, treat, and determine the appropriate disposition of patients with injury and illness and
those in need of specialized care and safe transportation. EMS is a vital component of the
healthcare, public health, and public safety systems.
Overall System Performance
Vermont's Emergency Medical Services face significant challenges that compromise
effectiveness and sustainability. Access to EMS varies widely across the state, with inconsistent
service delivery, response times, and reliability from town to town. The system struggles with
increasing call volumes that strain capacity, while emergency and non-emergency interfacility
transportation remains unreliable in parts of the State.
Inadequate funding creates critical gaps in essential functions, including training, education, data
collection, and medical direction. Additionally, the current infrastructure does not support
Mobile Integrated Health (MIH) initiatives, limiting opportunities for more comprehensive
community healthcare delivery.
2 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

Vermont's EMS system retains several core strengths despite growing pressures. The State
benefits from a deeply committed workforce, many of whom volunteer their time to ensure
neighbors receive emergency care. This community-based model reflects Vermont's values of
service and mutual aid. The enactment of Act 157 of 2024 officially recognizes EMS as essential
and signals a bipartisan commitment to systemic reform.
Key Findings
Service levels, response times, staffing models and reliability vary significantly by town.
Emergency and non-emergency interfacility transportation resources are not consistently
reliable in parts of the State.
EMS agencies operate with different revenue mixes, leading to notable funding gaps between
agencies.
Inadequate funding creates gaps in training, education, data collection, and medical direction
needed for system quality.
Until regulatory and funding models align with MIH delivery and costs, the current system
cannot support MIH implementation.
Governance and System Structure
The Vermont EMS system operates under a multi-tiered governance framework. The Office of
Emergency Medical Services, housed within the Department of Health, serves as the state
regulatory body providing oversight that includes licensing of services and personnel, conducting
investigations, collecting system-wide data, developing training programs, and establishing
clinical protocols. This centralized function supports and oversees 13 regional districts, which
provide varying levels of local system oversight.
However, Vermont's 13-district system is not functioning consistently or sustainably. Districts
operate without enforcement authority and face role ambiguity, resource constraints, and
insufficient funding. This lack of adequate funding and support has resulted in insufficient
physician medical oversight and assessment across the system. Many areas of Vermont rely on
volunteer physicians to provide medical oversight, creating gaps in clinical guidance and quality
assurance.
To evaluate the operational and financial characteristics of Vermont's EMS system, the
committee analyzed four service delivery models. These models include regional EMS services,
career fire department-based EMS, municipal services, and local service providers. The analysis
examined each model's structure, funding sources, response capabilities, and staffing models.
3 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

1. Regional EMS Services
Regional EMS services require the least local tax support and provide the majority of
interfacility transport (IFT) work statewide. Response times to critical incidents are longer
than fire-based systems but better than stand-alone municipal systems. These services use
mixed staffing models, including full-time, part-time, and volunteer staff, with 79% providing
paramedic services.
2. Career Fire Department-Based EMS
Career fire department-based EMS is the most expensive model, but it provides the shortest
response times. These services offer very little IFT support, use 100% paid staff, and 100%
provide paramedic service. Fire-based ambulance services have higher costs per call and per
capita due to their additional fire suppression responsibilities.
3. Municipal Services
Municipal services are slightly more dependent on local tax support than regional services,
though less than fire-based models. Response times are higher than those of regional
providers. Several services support IFT needs, but most do not. These services rely more on
part-time and volunteer labor than regional providers, with 91% providing paramedic services.
4. Local Service Providers
Local service providers are comparable to municipal services in cost, response time, and IFT
work, but have slightly lower paramedic availability.
Key Findings
Insufficient funding and support leave the system with inadequate physician medical oversight
and assessment. Physician medical advisors (usually insufficiently compensated) provide
medical oversight in many areas of Vermont.
Fragmented data across multiple systems creates data quality issues for the advisory
committee, the Office of EMS, and leaders.
The manual data collection process used for this report is not viable moving forward.
Districts lack enforcement authority, role clarity, and sufficient funding.
The State EMS Office is understaffed and under resourced.
Data Sources and Limitations
The Vermont EMS Assessment faced significant data challenges that impacted the
comprehensiveness and precision of the analysis. The assessment relied on a complex patchwork
of information sources, including self-reporting surveys, Vermont EMS data systems, and
publicly available information, because no unified system exists for collecting and storing EMS
data. While the team made efforts to verify data with service leaders, they had to estimate some
4 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

information due to unavailable records. Additionally, reporting periods varied widely across
services. Ground ambulance data covered the period from 2023 to 2025 and could be based on
fiscal or calendar years, or a mix.
Furthermore, the analysis excluded first-response services from cost analyses due to insufficient
data and a lack of verification. Cost calculations for services operating mixed business lines—
such as fire departments providing both fire suppression and EMS—used a proportional
allocation formula in which total organizational expenses were divided by the ratio of ground
ambulance volume to total service volume.
Staffing projections were standardized under the assumption of one crew for every 1,200 calls,
with each crew requiring nine full-time equivalents (FTE), 18 part-time personnel, or a
combination thereof; however, this approach may overlook efficiencies based on actual service
staffing or workload rather than theoretical estimates.
Key Findings
Inconsistent data entry, inadequate collection tools, and manual processes fragment data,
hindering accurate system monitoring and reliability measurement. Prioritizing data collection
and analysis is essential.
The manual data collection process required for this report is not viable for ongoing EMS
system needs.
Underfunding of Vermont's EMS records system results in insufficient and inconsistent data
collection.
Insufficient financial resources and staffing limits the State's ability to gather accurate,
actionable EMS data for planning and oversight.
Without an integrated, statewide computer-aided dispatch system, the State cannot prioritize
time-sensitive 9-1-1 calls, monitor the system in real time, or effectively evaluate response
data.
There is little data on training, education, and support.
Interfacility transport (IFT) data from hospitals is unavailable to this committee
Statewide EMS Data
In 2024, Vermont's EMS system responded to approximately 100,000 911 calls, reflecting a 6%
increase from the previous year. Of the 100,000 calls, 29,500 did not result in transport.
Additionally, Interfacility transfers totaled 28,000, an 8% increase over the previous year.
• 911 Emergency Calls: ~100,000 (?6%)
Non-Transport Calls: 29,500
• Interfacility Transfers: 28,000 (?8%)
• Licensed Ambulance Services: 65 in-state, nine out-of-state
5 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

• Total System Cost: $98 million
Financial Assessment
Overall, the financial model is challenging and increasingly unsustainable. Nearly half of EMS
agencies operate at a deficit, as reimbursement rates do not cover the actual costs of readiness.
The total cost of Vermont-based ambulances is approximately $98 million, funded by various
sources:
• Insurance reimbursement: ~$53 million (54% cost recovery rate)
• Local tax support: ~$43 million
• Volunteer labor (valued): $9.7 million
• Annual fundraising: ~$1.2 million
• Provider taxes: ~$1.4 million
Ambulance services pay provider taxes to the state, which then uses this revenue to leverage
additional federal Medicaid funds. The system also relies on volunteer labor; however, declining
volunteer availability and increasing requirements make this model increasingly unsustainable.
Service Type Average Cost Per Capita Cost Average % of Staff
per Call Avg. Reimbursement Compensated
per Transport
Fire-Based $1,168 $189 $476 100%
Municipal $801 $57 $561 43%
Regional $670 $31 $598 57%
Local $729 $53 $691 44%
Key Findings
Inadequate ambulance reimbursement from Medicare and Medicaid forces towns to cover
costs through property taxes, creating funding disparities across communities.
Medicare does not reimburse for patients who are treated yet not transported, creating a
financial burden on services.
Act 157 of 2024 requires Medicaid reimbursement for certain non-transport calls but Medicare
does not reimburse non-transport calls.
A reimbursement system needs to be created to support Mobile Integrated Health (MIH)
services.
Vermont lacks mandatory, systematic state-level financial reporting for EMS agencies.
Volunteer availability is decreasing statewide.
Delivery costs vary sign

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_eprip-data-collection-2025.pdf**

Emergency Medical Services
System Data Collection and
Assessment Study
Final Report Published and Released MAY 2025
Report Completed and Issued May 2025 to
The Vermont Emergency Medical Services Advisory Committee

This is the Final Report by
The Cambridge Consulting Group
This report supersedes all previous drafts. Published on May 29, 2025
Vincent D. Robbins Engagement Manager, Workforce Assessment, Data Analysis
Brian LaCroix Assistant Engagement Manager, Stakeholder Engagement, Site Visits
Mic Gunderson Performance & Quality Management
A.J. Heightman Stakeholder Engagement
Drew Dawson System Design
Ray Barishansky Operations, Statewide Scan
Robert Holman Interfacility Transportation
Steven Kroll EMS Operations
Amy Mauro Financial Sustainability
John Todaro Education Process Assessment
Jeff Behm Emergency Communications Centers
David Shotwell Legal & Regulatory Review
Contact:
202-505-2256 | CambridgeCG.net VRobbins@CambridgeCG.net
PO Box 798, Wayne Vincent D. Robbins
Pennsylvania, 19087 Engagement Manager

VERMONT EMS Study FINAL REPORT Page 3 of 351
Table Of Contents
Glossary Of Abbreviations 4
Executive Brief 5
Major Findings 6
Detailed Report 7
The Geography and Demographics of Vermont 7
Vermont’s Transportation System 8
Vermont’s Health Care System 9
Vermont’s EMS System; An Overview 11
Vermont’s EMS System Overview Findings 14
Structure and Responsibilities 16
Structure and Responsibility Findings 22
EMS Delivery 23
EMS Delivery Findings 52
Financial Landscape 55
Financial Landscape Findings 60
Interfacility Transfers 62
Interfacility Transfers Findings 67
EMS Education System 69
EMS Education Findings 76
Performance and Quality in High Consequence Cases 78
Performance and Quality Improvement Findings 80
Clinical Data Dictionary 81
Clinical Data Dictionary Findings 87
Sources
Acknowledgments
Cambridge Consulting Group Issued May 26, 2025

VERMONT EMS Study FINAL REPORT Page 4 of 351
Glossary Of Abbreviations
AED Automated External Defibrillator MDT Mobile Data Computer
AEMT Advanced Emergency Medical Technician MPD Medical Priority Dispatch
AVL Automated Vehicle Location MPDS Medical Priority Dispatch System
BLS Bureau of Labor Statistics NEMSIS National EMS Information System
BTC Basic Telecommunicator NENA National Emergency Number Association
BTV Burlington International Airport NFIRS National Fire Incident Reporting System
CAD Computer Aided Dispatch NFPA National Fire Protection Association
CAH Critical Access Hospitals NH New Hampshire
CPR Cardiopulmonary Resuscitation NHTSA National Highway Traffic Safety Administration
CTY County NREMT National Registry of EMTs
ECC Emergency Communications Center NY New York
EMD Emergency Medical Dispatcher PD Police Department
EMR Emergency Medical Responder PDAP Public Dispatch Answering Point
EMS Emergency Medical Services PSAP Public Safety Answering Point
EMSAC Emergency Medical Services Advisory Council SIC Senior Instructor Coordinator
EMSD Emergency Medical Services Division SIREN Statewide Incident Reporting Network
of the Vermont Department of Health
SO Sheriffs Office
EMT Emergency Medical Technician
SSM System Status Management
ePCR Electronic patient care report
TO Training Officer
GMCB Green Mountain Care Board
VEFR Vermont Emergency First Responder Vermont
GPS Global Positioning Systems
VITL Health Information Exchange Vermont State
IC Instructor Coordinator
VSP Police
IFT Inter-facility medical transportation
This report references the Vermont EMS Academy in several
MA Massachusetts places. It should be noted this is a private, non-governmental
organization associated with Rescue, Inc.
Cambridge Consulting Group Issued May 26, 2025

VERMONT EMS Study FINAL REPORT Page 5 of 351
Executive Brief
The Vermont Emergency Medical Services Advisory Committee retained Cambridge Consulting Group to
conduct a comprehensive data collection and analysis of the state’s Emergency Medical Services (EMS)
system. The goal of this study was to provide a clear understanding of how the system is structured,
governed, and operated, and to identify areas of inconsistency, inefficiency or dysfunction. The study
deliverables specifically excluded the provision of any recommendations for changes to the system by
Cambridge Consulting Group. Therefore, this report focuses solely on findings with the exception of
recommendations requested for a data dictionary related to performance and quality indicators.
This assessment examines the legislative framework, operational landscape, and organizational
structure that defines Vermont’s EMS system. It includes a detailed review of EMS agencies, Emergency
Communications Centers (ECCs) and dispatch processes, Public Safety Answering Points (PSAPs),
licensing and certification procedures, EMS education, provider agency fiscal conditions and financial
sustainability, performance and quality improvement mechanisms, and the broader health and
transportation infrastructure that supports emergency response and patient transport.
Findings of the report highlight both strengths and challenges within the system. Vermont has a strong
community-based EMS culture, dedicated personnel, and a high density of responders. However,
challenges are present and related to overall structure, regional coordination, operational efficiency,
dispatch consistency, data collection and interoperability, and long-term workforce and financial
sustainability.
The report outlines several areas where targeted changes may improve system performance, equity of
access, quality of care, and system sustainability. These include improving statewide coordination of
services, modernizing communications processes, supporting and streamlining regionalization efforts, and
aligning EMS capabilities with broader healthcare transformation initiatives.
The firm reviewed hundreds of documents, four years of detailed dispatch and operational data, held
numerous key individual interviews, facilitated three site visits with agency leaders, analyzed dozens of
agency financial records, attended multiple EMS District meetings, and disseminated a dozen distinct and
targeted surveys to several stakeholder groups resulting in a substantial response rate.
Previous draft versions of this report were submitted for review of factual accuracy to the EMSD and
EMSAC prior to finalization and publication. Based on their feedback, especially concerning discrepancies
between perceived and actual data content in SIREN, the firm adjusted its findings from initial drafts to
include serious flaws and inconsistencies subsequently identified regarding data entry, collection,
uploading, and warehousing.
Cambridge Consulting Group’s analysis is intended to support informed decision-making and to serve as
a foundation for policy and operational reforms that strengthen the EMS system and better meet the
evolving needs of Vermonters.
The firm wishes to thank the EMSAC and the State of Vermont for choosing Cambridge Consulting Group
to conduct this important study.
Cambridge Consulting Group Issued May 26, 2025

6
VERMONT EMS Study FINAL REPORT Page 6 of 351
Major Findings
Cambridge Consulting Group‘s comprehensive review and analysis of the Vermont EMS system concludes
with the following major findings.
Vermont’s Health Care & EMS System
Vermont ranks among the healthiest states but faces an aging population, EMS workforce shortages, and
healthcare costs spent largely on hospital care. EMS lacks coverage standards, relies too heavily on a
diminishing group of volunteers, and is strained by rising 911 calls and inadequate, eroding financial
support.
EMS Structure and Governance
EMS oversight is decentralized across too many districts with unclear enforcement power and roles. The
EMSD is understaffed and underfunded, limiting its ability to successfully complete its mission.
Data Warehouse Flaws & Missing Information
The SIREN data warehouse was found to be missing as much as 15% of an agency's activity, with mis-
categorization or inconsistent classification of call types and patient dispositions, incomplete reporting
by services, and multiple names for some agencies. This renders reporting from SIREN incomplete,
complicated, and error prone.
EMS Operations and Performance
Vermont’s EMS system has too many small agencies, uneven call distribution and long response times in
some areas. Dispatch is fragmented, technology is underused, the system lacks real-time system status
monitoring, and does not have alternative EMS care delivery models.
EMS Financial Status
EMS agencies are significantly underfunded especially compared to fire and police. It is estimated that
nearly half operate at an annual deficit relying on eroding reserves. Financial reporting is inconsistent, as
many agencies lack administrative capacity and fiscal transparency due to lack of funding.
Interfacility Transport
IFT service availability is limited, expensive, inefficiently coordinated, and contributes to hospital delays and
staffing strain. Key data for managing IFTs is missing.
EMS Training Capacity
The state EMS training system is understaffed and underfunded, providing limited oversight, using outdated
certification standards, operates with inconsistent training costs, and no formal educator support.
Performance and Quality Improvement
The system lacks sufficient physician medical oversight and assessment due to a lack of funding and
support. In addition, missing data on early care response times limits quality assessment. EMS leaders
support performance tracking, but they are concerned it may lead to an overburdened workforce.
Cambridge Consulting Group Issued May 26, 2025

7
VERMONT EMS Study FINAL REPORT Page 7 of 351
Detailed Report
The Geography and Demographics of Vermont
Vermont is a state in the New England region of the northeastern United States.
It is bordered on the east by New Hampshire, on the south by Massachusetts, Vermont
on the west by New York and on the north by the Canadian province of Quebec.
The 45th largest state in area in the United States, it covers 9,616 square miles
(24,906 km²).
The Green Mountains run north-south through the state’s center, splitting it
into two distinct eastern and western regions. Mount Mansfield, at 4,395 feet
(1,340 meters) above sea level, is the state’s highest
point. Vermont’s landscape is home to many lakes
Population Density and rivers. The sixth largest freshwater body in the
United States, Lake Champlain, contributes much of
its western border.
Vermont is a diverse state. In Burlington, home
to the University of Vermont, an eclectic younger
population benefits from the social, educational,
and cultural amenities that are also a significant
draw for retirees. Burlington has had a recent wave of refugees who are
adding to the diversity of the state. According to the 2020 Census, there were
643,077 people living in Vermont, making it the 2nd least populated state
in the US, after Wyoming, with a population density of 67.9 per square mile
(26.2/km²). Vermont has the second highest median age in the nation at 42.8
years, trailing only Maine. Rural areas have seen their populations dwindle,
while cities like Burlington and surrounding Chittenden County have grown.
Vermont is a racially homogeneous state [see chart below] and its
population growth has been relatively modest compared to other states. The state had a population
growth of 2.8% from 2010-2020, which was lower than the national average of 7.4% during the same
period.
Vermont’s Racial Demographic
Vermont is known for its independence and
high voter turnout in national elections. This
evident community pride and enthusiasm have
been significant contributors to the growth and
volunteer staffing of Vermont’s EMS system,
however, they can also work against progress
when regional collaboration is needed to create
a more efficient system.
Cambridge Consulting Group Issued May 26, 2025

8
VERMONT EMS Study FINAL REPORT Page 8 of 351
Vermont’s Transportation System
A state’s roadway system is

*[document truncated for length]*

---

**[MINUTES] 2026-06-15_eprip-regional-coordination-study.pdf**

Report to
The Vermont Legislature

Vermont Regional Emergency Medical Services Coordination
Study 2024 Report to the Legislature

In Accordance with Act 78 (2023) Sec. E.312.1

Submitted to:

House Committee on Health Care

Submitted by:

Mark A. Levine, MD
Commissioner, Vermont Department of Health

Prepared by:

Bambi L. Dame
Emergency Medical Services Chief, Vermont Department of Health

William. M. Moran
Director, Vermont Department of Health

Report Date:

January 15, 2024

 Department of Health

108 Cherry Street, PO Box 70
Burlington, VT  05402
802.863.7280
healthvermont.gov

Vermont Department of Health

Contents
Introduction ..................................................................................................................................... 3

Background ..................................................................................................................................... 4

Study Findings – Cost of Service and Existing Funding Models ................................................... 5

Recommendations ........................................................................................................................... 7

Study Findings– Coordination Across Agencies ............................................................................ 9

Recommendations ......................................................................................................................... 10

Study Findings - EMS District Structure and Authority ............................................................... 10

Recommendation .......................................................................................................................... 11

Study Findings - EMS Personnel Mental Health and Wellness ................................................... 12

Recommendation .......................................................................................................................... 12

Regional Emergency Medical Services Coordination Study

2

Vermont Regional Emergency Medical Services Coordination Study
2024 Report to the Legislature

Vermont Department of Health

Executive Summary

In Vermont, emergency medical services (EMS) are delivered by a diverse group of
organizations.  These include municipal EMS, municipal fire-based, private not-for-profit,
private for-profit, and hospital-based services.   The diversity across the delivery of emergency
medical services results in a system where costs per transport can vary widely, and no single
financing model will meet each organization’s needs.

There is also significant variability among Vermont EMS services’ financial situations, with
some faring well and others facing acute challenges to their long-term viability. Crucially, while
parts of the Vermont EMS system are under great stress, the system is not in crisis. Indeed, there
are a number of targeted investments and improvements that should be considered that can move
services towards financial sustainability, and ultimately optimize the EMS system within the
existing framework. Doing so is likely to be more efficient and effective than a complete system
redesign – a complex undertaking that presents its own distinct challenges – and provides EMS
services with the agency to identify and implement the solutions that allow them to best serve
their community. As discussed below, there are investments that can be made now that will
enhance the system, improve service sustainability, and help some services identify that
significant additional reform or consolidation may be their best path forward.

Accordingly, the following recommendations offer opportunities to meaningfully improve the
EMS system in the near term while considerations about larger system reforms can continue to
be investigated. These recommendations are described in detail later in this report.

Cost of Service and Funding Model Recommendations

•  Establish and enforce EMS service performance requirements.
•

Incentivize regional coordination in those areas of the state at risk of losing access to
high-quality pre-hospital care.

•  Provide EMS services with technical assistance.
•  Enhance and expand the use of EMS data to support evidence-based operational and

clinical decision making.

•  Support EMS workforce development and sustainability by offering EMS initial and

continuing education at no cost to current and future EMS personnel.
Improve workforce recruitment and retention through incentives.

•

Coordination Across Agencies Recommendations

•  Modernize the emergency communications system.
•  Create an EMS Task Force to support response coordination among services.

EMS District and Authority Recommendations

•  Continue to work with EMS stakeholders to refine a vision and mission for EMS Districts

that reflects core values and focuses on current and future needs.

Regional Emergency Medical Services Coordination Study

3

Vermont Department of Health

EMS Mental Health and Wellness Recommendations

•  Support EMS workforce retention by ensuring EMS clinicians have access to mental

health and wellness resources and support.

Introduction

Act 78 (2023), Sec E.312.1 requires the Department of Health to conduct a regional coordination
study to identify issues and provide recommendations for legislative consideration to sustain and
improve the provision of EMS for Vermonters, focused on the following areas:

(1) issues related to costs of service and existing funding models;
(2) issues related to coordination across agencies; and
(3) issues related to EMS District structure and authority, including consideration of

recommendations on the number and configuration of EMS Districts and their powers,
duties, and authority.

The Department of Health contracted Emergency Management Matters, LLC to design and
implement the study processes, facilitate engagement with internal and external stakeholders,
and provide subject matter expertise to develop this report.

Through a comprehensive engagement process, including focus groups, one-on-one interviews,
surveys, email communications, website forms, and open meetings held virtually and in-person
across the state, over 673 stakeholders participated.  A Regional EMS Study Committee was
formed with representatives from across all stakeholder groups.  Through participation from the
Study committee members, emergency medical service professionals, citizens, hospital staff,
physicians, government leaders, and key stakeholder groups, consensus was found in some focus
areas and created additional questions in others.

Background

The Vermont EMS system is diverse, with various service types, models, and business
structures.  Vermont’s 256 municipalities are served by 78 ambulance services, one air medical
service, and 89 first-response non-transporting services. In 2022, the statewide EMS system
responded to 121,472 public requests for emergency medical care.  EMS professionals provide
an essential service by delivering basic and advanced emergency medical care and specialized
ambulance transportation to all residents and visitors of the state in need.  Furthermore, EMS
directly supports patients, hospitals, and other health care entities by providing medical care and
transportation for the sick and injured, moving between facilities, commonly referred to as
interfacility transfers. During 2022, EMS performed 17,103 interfacility transfers.

Throughout an eight-week engagement process, the following findings and recommendations
were developed.

Regional Emergency Medical Services Coordination Study

4

Vermont Department of Health

Study Findings – Cost of Service and Existing Funding Models

The diversity across the delivery of emergency medical services results in a system where costs
per transport can vary widely, and no single financing model will meet each organization’s
needs. For example, law enforcement and the fire service are primarily financed by public tax
dollars and are eligible for a greater number of federal grant opportunities, generally resulting in
better financial stability and predictability for communities when compared to services that are
unable to rely on public financing.

Vermont is ranked 49th in the country by population and 45th by area. With 79 licensed
ambulance services serving the state, there is one ambulance service for every 8,290 Vermonters.
67% of ambulance services respond to 1,500 calls or fewer annually. Low ambulance utilization
rates increase the cost per call, requiring greater amounts of government funding to sustain EMS
services.

Historically, the EMS system has been financed through a fee-for-service model for ambulance
transportation.  This means that if the patient is not transported by ambulance to an emergency
department, insurance would not reimburse an EMS service for the cost of deploying personnel
and equipment and delivering medical care at the scene.  As the cost of personnel, equipment,
and supplies has increased, the reimbursement rates paid by private insurance and government
programs (Medicare & Medicaid) have not kept pace.  Additional revenue in the form of local
government subsidies, subscriptions, private donations, and fundraising has been necessary to
pay for the cost of readiness, and to make up the difference not covered by insurance.
Insufficient reimbursement rates compounded by the inadequacy of the fee-for-service model for
ambulance transportation results in continued financial loss for some EMS services.

Many EMS service representatives report insufficient funding year after year.  Without sustained
and reliable funding, EMS services go without adequate staffing and modern equipment.  This
leaves EMS services unprepared and ill-equipped to respond to traumatic injuries and medical
emergencies, mass casualty incidents, and medical surge events.

In 2023, representatives from the American Ambulance Association, the Vermont Ambulance
Association, and others successfully secured a two-year extension of the Medicare add-on
payments (2% urban, 3% rural, and 22.6% super rural) from Congress.  Add-on payments
temporarily augment the Medicare Ambulance Fee Schedule and increase payments to
ambulance providers.  During the same year, Vermont Senators Peter Welch and Bernie Sanders
introduced the Emergency Medical Services Reimbursement for On-Scene Care and Support Act,
which, if enacted, would provide Medicare reimbursement for emergency medical services
provided on the scene, and does not necessitate the transport of a patient to a hospital emergency
department.  Vermont Representative Becca Balint introduced companion legislation in the
House of Representatives.

During the 2023 Vermont Legislative session, the Medicaid reimbursement rate for ambulance
transportation was increased to 100% of the Medicare reimbursement rate.  Additionally, a new
regulation in effect on July 1, 2023, will allow Medicaid reimbursement to an EMS service for
emergency medical care provided to a Medicaid beneficiary even if it does not result in transport

Regional Emergency Medical Services Coordination Study

5

Vermont Department of Health

to a hospital emergency department (Medicaid HCAR Rule 4.102). While these are important
improvements to the payment model for EMS services, the sufficiency of these current rates to
cover the cost of care and transport are still being assessed.  Since January of 2022, the Centers
for Medicare and Medicaid Services (CMS) has been actively collecting cost, revenue,
utilization, and other information from providers of ground ambulance services.  This
information collected will ultimately be provided to the Medicare Payment Advisory
Commission (MedPAC), which is required to report to Congress on the adequacy of Medicare
payment rates for ambulance services.

An appropriately staffed and equipped EMS service will have a higher cost of readiness as
compared to an understaffed and ill-equipped EMS service.  The cost of 

*[document truncated for length]*

---

### 2026-06-03 — Vermont Board of Medical Practice — June 03, 2026

**[MINUTES] 2026-06-03_pre-ems-advisory-council-minutes-20260603.pdf**

| Meeting Minutes  |     |     |     |   Jun 3, 2026 |     |
| ---------------- | --- | --- | --- | ------------- | --- |
Vermont Emergency Medical Services
Advisory Committee
Meeting Minutes
T
Date: June 3, 2026
Location: Waterbury State Office Complex, Waterbury, Vermont & Microsoft Teams
Meeting Called to Order: 2:00 PM
F
Roll Call
| Representative  | Attendance  | Representative  | Attendance  |     |     |
| --------------- | ----------- | --------------- | ----------- | --- | --- |
A
| District 1  | Present  | District 2  | Absent   |     |     |
| ----------- | -------- | ----------- | -------- | --- | --- |
| District 3  | Present  | District 4  | Present  |     |     |
| District 5  | Absent   | District 6  | Present  |     |     |
R
| District 7   | Present  | District 8   | Present  |     |     |
| ------------ | -------- | ------------ | -------- | --- | --- |
| District 9   | Absent   | District 10  | Present  |     |     |
| District 11  | Absent   | District 12  | Present  |     |     |
D
| District 13  | Present  | VAA   | Present  |     |     |
| ------------ | -------- | ----- | -------- | --- | --- |
| IREMS        | Present  | PFFV  | Present  |     |     |
| VCFC         | Absent   | VSFA  | Present  |     |     |
| VAHHS        | Absent   | VLCT  | Absent   |     |     |
| VDH          | Present  |       |          |     |     |

Editor's Note
Significant technical difficulties affected this meeting. Internet service at the Waterbury State
Office Complex was unavailable at the start of the meeting, requiring the use of cellular hotspot
connectivity, alternate audio equipment, and mobile devices to facilitate participation by
in-person and remote attendees. These issues impacted recording quality, transcription
accuracy, and remote participation during the early portion of the meeting. Connectivity and
| Vermont EMS Advisory Committee  |     |     |     |     |   1  |
| ------------------------------- | --- | --- | --- | --- | ---- |

Meeting Minutes Jun 3, 2026
audio quality improved later in the meeting following restoration of network services by State
officials. Portions of the meeting transcript are incomplete or difficult to reconstruct due to these
technical limitations.
Workgroup Updates
Education & Workforce Development (EWD)
T
Bill Camarda provided an update on recent Education & Workforce Development workgroup
discussions. Topics included degree requirements for EMS clinicians, development of potential
paramedic practitioner pathways, educational entry pathways into the profession,
apprenticeship models, relationships with collegeFs and universities, associate degree
requirements, and considerations regarding out-of-state providers and future workforce
development. The workgroup anticipated bringing additional consent items forward for future
EMSAC consideration.
A
Healthcare Integration (HIN)
The Healthcare Integration Workgroup reported ongoing discussions regarding interfacility
transport (IFT) categorization, prioritization methodologies, patient movement timelines, and
healthcare system impacts. Members also discussed the relationship between EMS and
R
designated mental health agencies and added a roadmap item focused on EMS and mental
health system integration. No consent items were advanced for EMSAC consideration at this
meeting.
Medical Direction (MED)
D
The Medical Direction Workgroup reported progress on foundational definitions related to
medical control and medical direction. Members indicated that future meetings would focus on
refining definitions and developing consent items intended to establish common terminology and
understanding across the EMS system.
Operations (OPS)
Discussion centered on statewide EMS resource tracking, ambulance inventories, specialty
resources, strike team concepts, statewide situational awareness, and exploration of geographic
information system (GIS) mapping solutions to support operational planning. Additional
discussion occurred regarding statewide CAD systems, resource allocation, and opportunities to
improve statewide operational visibility and coordination.
Finance (FIN)
The Finance Workgroup reported ongoing efforts related to reimbursement for non-transport
EMS services, identification of EMS funding gaps, development of financial recommendations
Vermont EMS Advisory Committee 2

Meeting Minutes Jun 3, 2026
for legislative consideration, and strategies to encourage regional collaboration among EMS
agencies. Discussion also included potential approaches to coalition development and financial
support mechanisms for agencies pursuing collaborative operational models.
Consent Item Review
CI-FIN-001 – Reimbursement for Treatment Without Transport
T
The Committee reviewed Finance Consent Item FIN-001 regarding reimbursement pathways for
EMS agencies providing medically necessary evaluation, treatment, and related EMS services
when patient transport does not occur.
F
Motion: David Danforth moved approval of CI-FIN-001.
Second: Bill Camarda.
During discussion, members expressed concern regarding language referencing reimbursement
at the Medicare BLS non-emergenAcy base rate. Several members noted that similar language
had previously resulted in reimbursement limitations that may not accurately reflect emergency
EMS responses and the intent of the recommendation. Discussion focused on whether the
reimbursement benchmark should instead reflect emergency service reimbursement rates.
The Chair remindedR members that EMSAC had previously established a process prohibiting
material modification of consent items during full committee meetings. As the proposed change
would materially alter the recommendation, members agreed that the item should be returned to
the originating workgroup for further consideration.
David Danforth withdrew the motion. Bill Camarda withdrew the second.
D
Result: CI-FIN-001 was returned to the Finance Workgroup for revision and future
consideration. No vote was taken.
EMSAC 2026 Planning Process & Chair Report
The Committee discussed development of the EMSAC 2026 final report and five-year planning
document. Members reviewed a proposed report structure including executive summaries,
workgroup summaries, implementation timelines, financial analyses, legislative
recommendations, governance recommendations, supporting documentation, and appendices.
Discussion included strategies for organizing recommendations into phased implementation
timelines and development of a framework for final review and approval of the completed report.
Committee leadership reported that a technical writer would be engaged to assist with report
development and formatting as the project moves into the implementation planning phase. The
Committee expressed their support for the planning initiative including engagement with the
technical writer.
Vermont EMS Advisory Committee 3

Meeting Minutes Jun 3, 2026
EMS Compact Discussion
The Committee held an initial discussion regarding potential participation in the EMS Compact.
Members discussed national registry requirements, provider impacts, background check
requirements, interstate licensure considerations, regulatory oversight implications, and
potential operational impacts to Vermont EMS agencies. Members agreed that additional
research and subject matter expertise would be required before developing formal
T
recommendations and that the topic should be referred to the Governance Workgroup for further
evaluation.
Vermont Department of Health Update
F
Representatives from the Vermont Department of Health provided a brief update regarding
Mobile Integrated Health initiatives and ongoing efforts related to Rural Health Transformation
Program activities. Members were advised that consultant support was being sought to assist
with program development and implementation efforts.
A
Upcoming Meetings
Committee leadership reviewed upcoming workgroup and EMSAC meeting schedules and
discussed plans forR future workgroup meetings throughout June. Topics included continued
development of consent items, data needs identification, implementation planning, and
preparation of recommendations for inclusion in the final EMSAC report.
Adjournment
D
Motion: Pat Malone moved to adjourn.
Second: David Danforth.
Result: Motion passed unanimously.
The meeting adjourned at 3:48 PM.
Vermont EMS Advisory Committee 4

---

### 2026-05-20 — Vermont Board of Medical Practice — May 20, 2026

**[MINUTES] 2026-05-20_pre-ems-advisory-council-minutes-20260520.pdf**

| Meeting Minutes  |     |     |     |   May 20, 2026 |     |
| ---------------- | --- | --- | --- | -------------- | --- |
Vermont Emergency Medical Services
Advisory Committee
Meeting Minutes
T
Date: May 20, 2026
Location: Bennington Rescue Squad, Bennington, VT & Microsoft Teams
Meeting Called to Order: 1:00 PM by Drew Hazelton
F

Roll Call
| Representative  | Attendance  | Representative  | Attendance  |     |     |
| --------------- | ----------- | --------------- | ----------- | --- | --- |
A
| District 1    | Present  | District 2   | Absent   |     |     |
| ------------- | -------- | ------------ | -------- | --- | --- |
| District 3    | Present  | District 4   | Absent   |     |     |
| District 5    | RAbsent  | District 6   | Absent   |     |     |
| District 7    | Present  | District 8   | Present  |     |     |
| District 9    | Absent   | District 10  | Present  |     |     |
| DisDtrict 11  | Present  | District 12  | Present  |     |     |
| District 13   | Present  | VAA          | Present  |     |     |
| IREMS         | Present  | PFFV         | Absent   |     |     |
| VCFC          | Present  | VSFA         | Present  |     |     |
| VAHHS         | Absent   | VLCT         | Absent   |     |     |
| VDH           | Present  |              |          |     |     |

Editor's Note
Portions of the meeting transcript available to the committee were incomplete, corrupted, or
otherwise unreadable at the time these minutes were prepared. Attendance records, motions,
vote records, and meeting outcomes have been verified through available documentation and
manual vote counts taken during the meeting. Discussion summaries are reconstructed from the
| Vermont EMS Advisory Committee  |     |     |     |     |   1  |
| ------------------------------- | --- | --- | --- | --- | ---- |

Meeting Minutes May 20, 2026
portions of the transcript available and may not fully reflect all deliberations that occurred during
the meeting.
CI-EWD-006 – Field & Clinical Experience
Bill Camarda made the motion to approve CI-EWD-006, seconded by Pat Malone.
The Committee considered a recommendation establishing fieTld and clinical experience
requirements within Vermont EMS education programs. The proposal affirmed that initial EMS
education programs should include appropriate field and/or clinical experiences to support
competency development through patient assessment, patient care, operational exposure,
interdisciplinary interaction, clinical decision-making, and practical skill application. Future
F
requirements would be developed through the Vermont Board of EMS (VBEMS) and Vermont
Division of EMS (VDEMS).
Motion passed unanimously.
A
CI-EWD-007 – Curriculum & Resources
Bill Camarda made the motion to approve CI-EWD-007, seconded by Pat Malone.
The Committee revRiewed a recommendation supporting innovative and future-focused EMS
education pathways and curriculum development. The proposal encouraged the use of
accredited educational programs, modern educational technologies, competency-based
education, simulation, blended learning environments, and electronic learning management
systems to support advancement of EMS education within Vermont.
D
Motion passed unanimously.
CI-EWD-008 – VEFR Alignment
Pat Malone made the motion to approve CI-EWD-008, seconded by Bill Camarda.
The Committee considered a recommendation calling for redevelopment of the Vermont
Emergency First Responder (VEFR) curriculum to better align the certification with its intended
operational purpose. The proposal emphasized ambulance operations, foundational patient care
support, operational readiness, workforce development, and creation of an entry pathway into
the EMS profession.
Motion passed unanimously.
CI-EWD-009 – EMS Workforce Evaluation & Planning
Pat Malone made the motion to approve CI-EWD-009, seconded by Bill Camarda.
Vermont EMS Advisory Committee 2

| Meeting Minutes  |     |     |     |   May 20, 2026 |     |
| ---------------- | --- | --- | --- | -------------- | --- |
The Committee reviewed a recommendation assigning responsibility for ongoing workforce
evaluation and planning to the Education & Workforce Development Subcommittee. The
proposal called for continued assessment of workforce composition, recruitment, retention,
educational capacity, workforce sustainability, and future workforce needs in support of
statewide EMS planning efforts.
Motion passed unanimously.
T
CI-HIN-002 – IFT Endorsement
Will Elwell made the motion to approve CI-HIN-002, seconded by Bill Camarda.
F
The Committee considered a recommendation establishing an endorsement requirement for
EMS agencies conducting interfacility transports. The proposal outlined a future framework
under which interfacility transfers would be conducted by licensed EMS agencies holding an
interfacility transport endorsement and identified future development of endorsement standards
| and implementation processes.  |     | A   |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- |
Roll Call Vote
| Representative  | Vote  |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
R
| District 1  | Y       |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- |
| District 2  | Absent  |     |     |     |     |
| District 3  | N       |     |     |     |     |
D
| District 4                      | Absent  |     |     |     |      |
| ------------------------------- | ------- | --- | --- | --- | ---- |
| District 5                      | Absent  |     |     |     |      |
| District 6                      | Absent  |     |     |     |      |
| District 7                      | Y       |     |     |     |      |
| District 8                      | Y       |     |     |     |      |
| District 9                      | Absent  |     |     |     |      |
| District 10                     | N       |     |     |     |      |
| District 11                     | Absent  |     |     |     |      |
| District 12                     | Y       |     |     |     |      |
| District 13                     | Y       |     |     |     |      |
| Vermont EMS Advisory Committee  |         |     |     |     |   3  |

| Meeting Minutes  |         |     |     |   May 20, 2026 |     |
| ---------------- | ------- | --- | --- | -------------- | --- |
| VAA              | Y       |     |     |                |     |
| IREMS            | Y       |     |     |                |     |
| PFFV             | Absent  |     |     |                |     |
| VCFC             | Y       |     |     |                |     |
| VSFA             | Y       |     | T   |                |     |
| VAHHS            | Absent  |     |     |                |     |
| VLCT             | Absent  |     |     |                |     |
F
| VDH  | Abstain  |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- |
Motion passed.
A
CI-HIN-004 – IFT Agreements
Will Elwell made the motion to approve CI-HIN-004, seconded by Bill Camarda.
The Committee revRiewed a recommendation establishing the requirement that healthcare
facilities, systems, and regions routinely utilizing interfacility transport services enter into formal
agreements with EMS agencies, EMS systems, or EMS consortiums. The proposal was
intended to support coordinated patient care, transportation planning, and system readiness
throughout Vermont's healthcare system.
D
Roll Call Vote
| Representative                  | Vote    |     |     |     |      |
| ------------------------------- | ------- | --- | --- | --- | ---- |
| District 1                      | Y       |     |     |     |      |
| District 2                      | Absent  |     |     |     |      |
| District 3                      | Y       |     |     |     |      |
| District 4                      | Absent  |     |     |     |      |
| District 5                      | Absent  |     |     |     |      |
| District 6                      | Absent  |     |     |     |      |
| District 7                      | Y       |     |     |     |      |
| District 8                      | Y       |     |     |     |      |
| Vermont EMS Advisory Committee  |         |     |     |     |   4  |

| Meeting Minutes  |         |     |     |   May 20, 2026 |     |
| ---------------- | ------- | --- | --- | -------------- | --- |
| District 9       | Absent  |     |     |                |     |
| District 10      | Y       |     |     |                |     |
| District 11      | Absent  |     |     |                |     |
| District 12      | Y       |     |     |                |     |
| District 13      | Y       |     | T   |                |     |
| VAA              | Y       |     |     |                |     |
| IREMS            | Y       |     |     |                |     |
F
| PFFV   | Absent  |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- |
| VCFC   | Y       |     |     |     |     |
| VSFA   | Y       | A   |     |     |     |
| VAHHS  | Absent  |     |     |     |     |
| VLCT   | Absent  |     |     |     |     |
R
| VDH  | Abstain  |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- |
Motion passed.
CI-OPS-001 – EMS Resource Tracking
D
Will Elwell made the motion to approve CI-OPS-001, seconded by the District 8 Representative.
The Committee reviewed a recommendation directing development of a centralized statewide
EMS resource tracking program intended to support operational readiness, disaster
preparedness, statewide planning, and identification of EMS capability gaps. The proposal
included tracking of ambulances, specialty resources, state-owned caches, and other EMS
assets.
Motion passed unanimously.
CI-OPS-002 – Service Interruption
Aaron Collette made the motion to approve CI-OPS-002, seconded by Will Elwell.
The Committee considered a recommendation establishing a framework for temporary
state-directed EMS resource deployment during significant service interruptions, agency
| Vermont EMS Advisory Committee  |     |     |     |     |   5  |
| ------------------------------- | --- | --- | --- | --- | ---- |

Meeting Minutes May 20, 2026
failures, or operational disruptions. The proposal focused on continuity of care, regional
preparedness, and operational resilience.
Motion passed unanimously.
CI-OPS-003 – Statewide Operational Objective
Aaron Collette made the motion to approve CI-OPS-003, secoTnded by Will Elwell.
The Committee reviewed a recommendation establishing the statewide operational objective
that timely and effective EMS care should be available to every resident and visitor in Vermont.
The objective was presented as a guiding principle for future planning, operational
F
decision-making, and system development.
Motion passed unanimously.
CI-OPS-004 – Statewide Operational Plan
A
Aaron Collette made the motion to approve CI-OPS-004, seconded by Will Elwell.
The Committee considered a recommendation directing development and maintenance of a
formal statewide EMRS operational plan. The proposal identified planning elements including
mass casualty incident response, surge capacity planning, interstate response integration, EMS
resource tracking, healthcare disaster preparedness coordination, and public health emergency
response planning.
Motion passed unanimously.
D
CI-OPS-005 – Definitions 1
Aaron Collette made the motion to approve CI-OPS-005, seconded by Will Elwell.
The Committee reviewed a recommendation establishing standardized operational definitions
related to EMS mutual aid and EMS response relationships. The proposal defined mutual aid
provided in support of a primary agency, in lieu of a primary agency, and when acting as a
primary agency, with the goal of supporting statewide consistency in operations, planning,
reporting, and future NERIS alignment.
Motion passed unanimously.
Financial Report
Chair Drew Hazelton presented a financial report to the Committee.
Pat Malone made the motion to accept the financial report, seconded by R

*[document truncated for length]*

---

### 2026-04-15 — Vermont Board of Medical Practice — April 15, 2026

**[MINUTES] 2026-04-15_pre-ESMAC-minutes-4.15.pdf**

Vermont Emergency Medical Services
Education Council & Advisory Committee

Meeting Minutes

Education Council
Date: April 15, 2026
Location: Waterbury State Office Complex, Waterbury (VT), & Microsoft Teams
Meeting Called to Order: 1:02 PM by Drew Hazelton

Rollcall

|              | Representative    |     | Attendance  |                | Representative   |     | Attendance   |
| ------------ | ----------------- | --- | ----------- | -------------- | ---------------- | --- | ------------ |
| District 1   |                   |     |             |   District 2   |                  |     |              |
|              | Kathy Jochim      |     | Present     |                | Adam Heuslein    |     | Present      |
|              |                   |     |             |                | Samantha Atwood  |     |              |
| District 3   |                   |     |             |   District 4   |                  |     |              |
|              | Leslie Lindquist  |     | Present     |                | Scott Brinkman   |     |              |
|              | Becky Alemy       |     |             |                | Corey Boisvert   |     |              |
| District 5   |                   |     |             |   District 6   |                  |     |              |
|              | Michael Wright    |     | Present     |                | Joe Aldsworth    |     |              |
|              |                   |     |             |                | David Danforth   |     | Present      |
| District 7   |                   |     |             |   District 8   |                  |     |              |
|              | Charlene Phelps   |     |             |                | Matt Parrish     |     | Present      |
|              | Kate Rothwell     |     | Present     |                | Charles Piso     |     | Present      |
| District 9   |                   |     |             |   District 10  |                  |     |              |
|              | Rod Kenyon        |     | Present     |                | Michael Tarbell  |     | Present      |
|              |                   |     |             |                | Jim Finger       |     |              |
| District 11  |                   |     |             |   District 12  |                  |     |              |
|              | Ben Whalen        |     | Present     |                | Bill Camarda     |     | Present      |
|              |                   |     |             |                | Bobby Maynard    |     |              |
| District 13  |                   |     |             |   VAA          |                  |     |              |
|              | Eric Wilson       |     | Present     |                | Drew Hazelton    |     | Present      |
|              |                   |     |             |                |                  |     |              |
| IREMS        |                   |     |             |   PFFV         |                  |     |              |
|              | Pat Malone        |     |             |                | Marc Hachey      |     | Present Y Y  |
|              | Chris LaMonda     |     | Present     |                | Billy Fritz      |     | Present      |
| VCFC         |                   |     |             |   VSFA         |                  |     |              |
|              | Aaron Collette    |     | Present     |                | Richard Bowman   |     | Present      |
|              | Michael Randzio   |     |             |                | Will Elwell      |     | Present      |
| VAHHS        |                   |     |             |   VLCT         |                  |     |              |
|              | Liz Couto         |     |             |                | Lee Krohn        |     | Present      |
|              |                   |     |             |                |                  |     |              |
| VDH          |                   |     |             |                |                  |     |              |
|              | Will Moran        |     | Present     |                |                  |     |              |
|              | Chelsea Dubie     |     | Present     |                |                  |     |              |

1
April 15, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
Non-members in attendance: Courtney Newman, Ray Walker, Dan Wolfson, Dan Berkman,
Tyler Boucher, Dan Wolfson, Matthew Weisman, Kevin Argentieri, Asher Clark, Ben Whalen,
Bill Adams, Robert Grant, Aly Sanchez
Meeting Minutes Review & Approval
The minutes from the March 18th, 2026, meeting were previously distributed to the committee:
• Motion to approve the March 18th, 2026, meeting minutes David Danforth and seconded
by Matt Parrish
• No further discussion
• Motion carried unanimously
Opening Remarks
The meeting was called to order by the committee chair who outlined expectations for the
meeting. Members were reminded that significant work had already been completed within
assigned workgroups and that the purpose of this meeting was to review, discuss briefly, and vote
on proposed consent items—not to revisit or have extensive discussions already conducted in the
workgroups. Emphasis was placed on maintaining efficiency, respecting the time invested by
workgroups, and continuing to build toward a comprehensive system plan. If committee
members demonstrate an unwillingness to trust the product of the workgroup, members would be
required to attend eight-hour meetings scheduled by the chair. It was reiterated that all proposals
presented represent “minimum viable products” intended to evolve over time through future
refinement.
Overview of Process and Documentation
The facilitator reviewed the structure and handling of consent items, noting that:
• Draft documents are stored in a shared repository and categorized as “consent item
drafts.”
• Approved items will be moved to a finalized folder in PDF format to prevent further
edits.
• Items requiring revision will be returned to their respective workgroups.
• A roadmap will track progress and revisions across all consent items.
• Voting on items will formally close discussion unless revisions are requested.
Challenges related to aligning language across multiple workgroups were acknowledged, and
members were asked for flexibility as inconsistencies are identified and corrected.
Consent Item: Governance #1 – Vermont Board of EMS (VBEMS)
Motion: To approve Governance Consent Item #1 (Revision A) made by David Danforth and
seconded by Charles Piso
Summary of Proposal
The committee reviewed a proposal recommending the establishment of the Vermont Board of
EMS (VBEMS) as the future governing body to replace EMSAC. The proposed structure
includes:
2
April 15, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
• 21 voting members:
o 13 geographically representative members (based on existing districts)
o 8 stakeholder representatives (aligned with current statutory groups)
• Standing subcommittees:
o Governance
o Operations
o Healthcare Integration
o Education & Workforce Development
o Clinical Practice
o Finance
• Executive Committee composed of leadership and subcommittee chairs
• A self-perpetuating membership model, where the board nominates and approves future
members
• Participation of non-voting subject matter experts as needed
The board is intended to work in coordination with the state EMS office and support long-term
system planning, including a five-year strategic plan and legislative reporting.
Discussion Highlights
• Nomination Process: Members raised concerns about clarity regarding how stakeholder
representatives would be selected. It was emphasized that nominations should originate
from stakeholder organizations rather than the board itself. Agreement was reached to
clarify this language in future revisions.
• Stakeholder Representation: Questions were raised about the inclusion and balance of
stakeholder groups. It was noted that the current list reflects statutory requirements and
may be revisited in future iterations.
• Timing of Materials: Multiple members expressed concern about receiving documents
shortly before the meeting, limiting their ability to consult with their respective
constituencies.
• Transparency and Access: Requests were made to provide access to workgroup notes or
summaries to better understand how recommendations were developed.
• Process Concerns: Broader discussion emerged, consensus on a need for a more defined
process for reviewing and approving workgroup outputs.
Leadership emphasized the importance of maintaining momentum and trusting the workgroups
to bring forward well-developed recommendations.
A roll call vote was conducted.
Result: Motion passed
Representative Vote Representative Vote
District 1 District 2
Kathy Jochim Y Adam Heuslein Y
Samantha Atwood
District 3 District 4
3
April 15, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee

| Leslie Lindquist  |                 |     | Y         |                | Scott Brinkman   |     |     |
| ----------------- | --------------- | --- | --------- | -------------- | ---------------- | --- | --- |
|                   | Becky Alemy     |     |           |                | Corey Boisvert   |     |     |
| District 5        |                 |     |           |   District 6   |                  |     |     |
| Michael Wright    |                 |     | Y         |                | Joe Aldsworth    |     |     |
|                   |                 |     |           |                | David Danforth   |     | Y   |
| District 7        |                 |     |           |   District 8   |                  |     |     |
| Charlene Phelps   |                 |     |           |                | Matt Parrish     |     | Y   |
|                   | Kate Rothwell   |     | Y         |                | Charles Piso     |     |     |
| District 9        |                 |     |           |   District 10  |                  |     |     |
|                   | Rod Kenyon      |     | Y         |                | Michael Tarbell  |     | Y   |
|                   |                 |     |           |                | Jim Finger       |     |     |
| District 11       |                 |     |           |   District 12  |                  |     |     |
|                   | Ben Whalen      |     | Y         |                | Bill Camarda     |     | Y   |
|                   |                 |     |           |                | Bobby Maynard    |     |     |
| District 13       |                 |     |           |   VAA          |                  |     |     |
|                   | Eric Wilson     |     | Y         |                | Drew Hazelton    |     | Y   |
|                   |                 |     |           |                |                  |     |     |
| IREMS             |                 |     |           |   PFFV         |                  |     |     |
|                   | Pat Malone      |     |           |                | Marc Hachey      |     | Y   |
|                   | Chris LaMonda   |     | Y         |                | Billy Fritz      |     |     |
| VCFC              |                 |     |           |   VSFA         |                  |     |     |
|                   | Aaron Collette  |     | Y         |                | Richard Bowman   |     | Y   |
| Michael Randzio   |                 |     |           |                | Will Elwell      |     |     |
| VAHHS             |                 |     |           |   VLCT         |                  |     |     |
|                   | Liz Couto       |     |           |                | Lee Krohn        |     | Y   |
|                   |                 |     |           |                |                  |     |     |
| VDH               |                 |     |           |                |                  |     |     |
|             

*[document truncated for length]*

---

**[MINUTES] 2026-04-15_eprip-emsac-roster-2026.pdf**

EMS Advisory Committee Roster & Contact Information (2026)

District 1

District 2

District 3

District 4

District 5

District 6

District 7

District 8

District 9

District 10

District 11

District 12

District 13

Kathy Jochim

director@fairfaxrescue.org

Adam Heuslein
Samantha Atwood

adam@gloverambulance.org
smyroxy@gmail.com

Leslie Lindquist
Becky Alemy

Scott Brinkman
Cory Boisvert

Leslie.lindquist@uvmhealth.org
balemy@colchestervt.gov

sbrinkman@stowevt.gov
cboisvert@morristownvt.gov

No appointed representative

Joe Aldsworth
David Danforth

Joseph.Aldsworth@vermont.gov
ddanforth@barretown.org

Charlene Phelps
Kate Rothwell

luvtwins@gmavt.net
krothwell@middleburyems.com

Matt Parrish
Charles Piso

Alan Beebe

Michael Tarbell
Jim Finger

No appointed representative

director@wrva.org
charlespiso@live.com

abeebe1967@aol.com

deputychief@rasvt.com
ea@rasvt.com

Bill Camarda
Bobby Maynard

bcamarda@brsvt.org
bobby@dvrescue.com

Eric Wilson

ewilson@rescueinc.org

VAA

IREMS

PFFV

 Committee Chair Drew Hazelton

dhazelton@rescueinc.org

Pat Malone
Chris LaMonda

patrick.malone@med.uvm.edu
christopher.lamonda@med.uvm.edu

Marc Hachey

hacheymarc@gmail.com

EMSAC (2025)

VCFC

VSFA

VAHHS

VLCT

VDH

Billy Fritz

wfritz@brattleboro.gov

Aaron Collette
Michael Randzio

Richard Bowman
Will Elwell

Liz Couto

Lee Krohn

acollette@willistonfire.com
Michael.Randzio@chestervt.gov

fftech10@gmail.com
welwell0911@gmail.com

ecouto@chsi.org

leekrohn1@gmail.com

Will Moran
Chelsea Dubie

william.moran@vermont.gov
chelsea.dubie@vermont.gov

EMSAC (2025)

---

### 2026-03-18 — Vermont Board of Medical Practice — March 18, 2026

**[MINUTES] 2026-03-18_pre-ems-advisory-committee-minutes-3.18.26%20minutes.pdf**

Vermont Emergency Medical Services
Education Council & Advisory Committee

EMS Advisory Committee
Date: March 18, 2026
Location: Waterbury State Office Complex, Waterbury (VT), & Microsoft Teams
Meeting Called to Order: 1:03 PM by Drew Hazelton

Rollcall

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     |             |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     | Corey Boisvert   |                |     | Present     |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  | Jim Finger     |     | Present     |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     | Present     |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     |  Present    |     |                  | Marc Hachey    |     |             |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     |             |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     | Richard Bowman   |                |     | Present     |
|              | Michael Randzio   |     | Present     |     |                  | Will Elwell    |     | Present     |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              | Liz Couto         |     | Present     |     |                  | Lee Krohn      |     |             |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

Others in attendance: Dan Wolfson, Courtney Newman, Donna Jacob, Ray Walker, Connor
Dunn, Chelsea Dubie, Aly Sanchez
1
March 18, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
Meeting Minutes Review & Approval
The minutes from March 6th, 2026, meeting were previously distributed to the committee:
• Aaron Collette noted his attendance was not recorded on the attendance sheet; his
attendance was recorded. Adam Heuslein’s was also marked as present at the meeting.
Following clarification, the motion proceeded.
• Motion to approve the February 4th meeting minutes by Bill Camarda and seconded by
David Danforth
• No further discussion
• Motion carried unanimously
Governance Workgroup Update
The Committee received a report from the Governance Work Group, which outlined ongoing
efforts to design a comprehensive, statewide EMS governance framework. The proposal under
consideration would transition Vermont’s EMS system from a district-based structure to a
unified statewide model. This framework includes elevating the EMS Office within the Vermont
Department of Health to a division-level entity to enhance administrative capacity and oversight.
Additionally, the Work Group is evaluating the establishment of a statewide EMS Board
responsible for policy development, standards setting, and strategic direction, while the EMS
Office would retain responsibility for regulatory enforcement and operational management.
The Committee engaged in substantive discussion regarding the proposed governance model,
including considerations of representation, regional coordination, and stakeholder engagement.
Members emphasized the importance of maintaining equitable geographic representation and
ensuring that regional collaboration—particularly for mutual aid coordination and emergency
response planning—remains effective under a centralized system. While some concerns were
expressed regarding the elimination of district structures, there was consensus that regional
coordination mechanisms can be preserved within a statewide framework. The Work Group was
directed to continue refining the proposal with ongoing stakeholder input.
Further discussion addressed the delineation of responsibilities between the proposed EMS
Board and the EMS Office. The Committee generally supported a co-equal but distinct structure
in which the Board establishes policy and standards, and the EMS Office enforces compliance
and oversees system operations. Consideration was given to potential overlaps in authority,
funding implications, and administrative efficiency. The Committee found no significant
opposition to the conceptual model and encouraged continued development and clarification.
Education Workgroup Report Out
The Education Work Group provided an update on initiatives related to EMS education and
training. The Work Group reaffirmed its support for maintaining the National Registry of
Emergency Medical Technicians as the foundational standard for certification while identifying
gaps in advanced training, including critical care and mobile integrated health roles. The
potential implementation of accreditation requirements for EMS education programs was
discussed, with recognition of both the benefits of standardized quality and the potential financial
and operational challenges for smaller or volunteer-based organizations.
2
March 18, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
The Committee also considered issues related to instructor credentialing, including the
possibility of shifting responsibility for instructor qualification from the state to individual
training programs. Members expressed concern regarding the potential impact on recruitment,
retention, and program accessibility if accreditation and credentialing requirements become
overly burdensome. It was noted that any such changes would be implemented over an extended
timeline to allow for appropriate transition and adaptation.
Healthcare Integration Workgroup Report Out
The Healthcare Integration Work Group reported on its ongoing efforts to improve coordination
across the EMS and healthcare systems, with particular focus on interfacility transfers (IFTs).
The Work Group is developing a tiered classification system to define response expectations,
staffing requirements, and reimbursement structures. Challenges associated with mental health
patient transport and reimbursement limitations were discussed, and the need for improved
coordination and accountability was emphasized. The Work Group also highlighted the
importance of enhanced data integration across EMS agencies, hospitals, and emergency
communication systems.
Statewide Trauma System
The Committee engaged in an in-depth discussion regarding the absence of a formal statewide
trauma system. Members underscored the importance of establishing a trauma registry to support
data-driven performance improvement, patient outcome tracking, and system-wide coordination.
The potential use of existing data platforms was identified as a practical and cost-effective
approach. The development of a trauma system was recognized as a priority aligned with
legislative direction and broader system improvement goals.
Additional discussion addressed the utilization of data systems such as cardiac arrest registries to
support clinical performance improvement. While the value of these systems was widely
acknowledged, concerns were raised regarding the sustainability of funding, as current efforts
rely heavily on grant support. The Committee emphasized the need to identify stable, long-term
funding mechanisms to ensure continuity and effectiveness.
Working Group Scheduling
The Committee reviewed ongoing and upcoming work group activities. The Governance,
Education, and Healthcare Integration Work Groups will continue to meet regularly, while
additional groups—including Operations, Finance, and Medical Direction—are expected to
commence work as the governance framework is further defined. The importance of developing
standardized terminology and definitions across all work groups was noted to ensure consistency
and alignment in planning efforts.
In closing, the Committee confirmed its meeting schedule and discussed the potential for
adjustments based on workload and progress. Members were encouraged to remain actively
engaged in work group activities and collaborative efforts.
3
March 18, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
Committee Schedule
• April 1st – Waterbury State Office Complex, Ash Conference Room, Waterbury, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• April 15th - Morriston Ambulance Service, Morristown, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• May 6th – Waterbury Ambulance Service, Waterbury, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• May 20th – Bennington Rescue Squad, Bennington, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• June 3rd – Waterbury State Office Complex, Waterbury, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• June 17th – Newport Ambulance Service, Newport VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• July 1st – Waterbury State Office Complex, Waterbury, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• July 15th – Fairfax Rescue, Fairfax, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
Adjournment
Motion to adjourn unanimously approved.
Meeting adjourned at 3:10 PM
4
March 18, 2026

---

### 2026-03-06 — Vermont Board of Medical Practice — March 06, 2026

**[MINUTES] 2026-03-06_pre-ems-advisory-committee-minutes-3.6.36.pdf**

Vermont Emergency Medical Services
Education Council & Advisory Committee

EMS Education Council Committee
Date: March 06, 2026
Location: Vermont EMS Conference, Burlington (VT), & Microsoft Teams
Meeting Called to Order: 1:03 PM by Pat Malone

Rollcall

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     | Present     |     | Scott Brinkman   |                |     | Present     |
|              | Becky Alemy       |     |             |     | Corey Boisvert   |                |     |             |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     |             |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     |             |
|              |                   |     |             |     |                  | Jim Finger     |     | Present     |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     |             |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     |  Present    |     |                  | Marc Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     | Present     |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     | Richard Bowman   |                |     |             |
|              | Michael Randzio   |     |             |     |                  | Will Elwell    |     |             |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              | Liz Couto         |     |             |     |                  | Lee Krohn      |     |             |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     |             |     |                  |                |     |             |

Non-members in attendance: Ray Walker, Connor Dunn, Jeff Johanson, Mike Roberge,
Zachary Bryan
1
March 6, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
General Comments
The Chair opened the meeting by noting the unusually high attendance and expressing
appreciation to all participants. It was also noted that the meeting was being held as a public
meeting on the campus of the University of Vermont. The Chair further acknowledged that the
agenda was limited, with the primary focus being an update on the Education and Workforce
Development Work Group of the EMS Advisory Committee, which had recently met in
Waterbury. It was also confirmed that a key contributor was unable to attend due to teaching
obligations.
Meeting Schedule
The Chair reported that there were no formal reports to present at this meeting. The primary item
of business then shifted to the structure and scheduling of future meetings. It was proposed that
the Education Council temporarily suspend its regular meetings until the completion of the
Education Work Group’s assigned tasks. The anticipated completion timeline for the work group
was identified as approximately June 2026. Accordingly, it was stated that no Education Council
meetings would be held prior to the monthly Advisory Committee meetings until further notice.
Additionally, it was noted that work groups would meet regularly, anticipated to occur every
other Wednesday, to advance their assignments.
Education Workgroup Update
The Chair then provided a detailed update on the initial discussions and direction of the
Education Work Group. A central topic of discussion was whether Vermont should remain a
National Registry state for EMS licensure. Based on the work group’s deliberations, there was a
clear consensus in favor of maintaining National Registry status. The rationale cited included the
reliability, validity, and regular updating of National Registry examinations, as well as the
significant resource burden that would be required for the State of Vermont to independently
develop and maintain an equivalent licensure testing system. Historical context was also
provided, referencing Vermont’s prior participation in regional testing through the New England
Council for EMS before transitioning to the National Registry.
The work group also began defining the scope of its responsibilities, identifying three primary
focus areas: education, training, and credentialing, while recognizing that licensure remains
primarily a regulatory function outside the direct purview of the group. Initial efforts were made
to distinguish between education and training. Education was generally defined as the
foundational instruction associated with initial certification programs, including EMT, Advanced
EMT, and paramedic education. Training, by contrast, was characterized as ongoing skill
development, competency maintenance, and implementation of updated protocols. The group
acknowledged that further work is needed to establish formal, standardized definitions, including
a clear definition of credentialing.
Discussion then turned to the current structure of EMS education delivery in Vermont. It was
noted that education is provided through a diverse array of models, including individual
instructors, independent training agencies, licensed EMS organizations, and institutions of higher
education. Data from a recent statewide assessment indicated that a relatively small number of
senior instructors are responsible for delivering a significant proportion of certification courses,
2
March 6, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
often in affiliation with established organizations. Conversely, a substantial number of licensed
instructor coordinators were not actively teaching certification courses during the reviewed
period.
Based on these findings, the work group expressed preliminary consensus around moving toward
an organization-based education model, rather than one centered on individual instructors. Under
this model, educational programs would be delivered by approved or licensed organizations, with
the goal of improving consistency, student support, administrative capacity, and overall program
quality. The potential benefits of this approach include enhanced infrastructure, better resource
allocation, and improved educational outcomes for students.
The topic of accreditation was also discussed. Participants explored the potential role of third-
party accrediting bodies, as well as the possibility of developing state-level accreditation or
approval standards for EMS education programs. While no final determination was made,
several considerations were identified, including the cost, administrative burden, and current
limitations of existing accrediting organizations, which primarily focus on paramedic-level
programs. The possibility of developing regional or state-based accreditation frameworks was
also raised as a potential future direction.
Additional discussion addressed the structure of instructional roles within EMS education.
Specifically, the group considered whether the traditional “instructor coordinator” role remains
necessary under a more organization-based model. It was suggested that instructional
responsibilities and program coordination functions could be separated, with organizations
assuming responsibility for coordination while licensed instructors focus on content delivery.
This model could also allow for the inclusion of subject matter experts from outside EMS,
provided appropriate oversight is maintained.
The Council further discussed long-standing considerations regarding the potential establishment
of a statewide EMS academy. Comparisons were made to existing law enforcement and fire
service training academies, and it was noted that while such a model may offer benefits, the scale
and volume of EMS education in Vermont present unique challenges that would need to be
carefully evaluated.
In closing discussion, members were encouraged to continue contributing ideas and feedback as
the work group process progresses. It was reiterated that this was an initial, exploratory
discussion and that substantial additional work remains.
Meeting adjourned at 1:58
3
March 6, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee

EMS Advisory Committee
Date: March 06, 2026
Location: Vermont EMS Conference, Burlington (VT), & Microsoft Teams
Meeting Called to Order: 2:00 PM by Drew Hazelton

Rollcall

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     | Present     |     | Scott Brinkman   |                |     | Present     |
|              | Becky Alemy       |     |             |     | Corey Boisvert   |                |     |             |
| District 5   |                   |     |             |     | District 6       |                

*[document truncated for length]*

---

### 2026-02-18 — Vermont Board of Medical Practice — February 18, 2026

**[MINUTES] 2026-02-18_pre-ems-advisory-committee-minutes-2.18.26.pdf**

Vermont Emergency Medical Services
Education Council & Advisory Committee

EMS Advisory Committee
Date: February 18, 2026
Location: Middlebury Regional EMS, Middlebury (VT), & Microsoft Teams
Meeting Called to Order: 1:03 PM by Drew Hazelton

Rollcall

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     |             |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     | Present     |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     | Corey Boisvert   |                |     | Present     |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     | Present     |     |                  | Matt Parrish   |     |             |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  | Jim Finger     |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     | Present     |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     | Present     |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     |  Present    |     |                  | Marc Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     | Present     |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     | Richard Bowman   |                |     | Present     |
|              | Michael Randzio   |     | Present     |     |                  | Will Elwell    |     | Present     |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              | Liz Couto         |     | Present     |     |                  | Lee Krohn      |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

Non-members in attendance: Dan Wolfson, Courtney Newman, Donna Jacob, Ray Walker,
Connor Dunn, Chelsea Dubie
1
February 18, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
Meeting Minutes Review & Approval
The minutes from February 4th, 2026, meeting were previously distributed to the committee:
• A motion was made and seconded to approve the minutes of the previous meeting;
however a procedural question was raised regarding eligibility to make the motion based
on attendance at the prior meeting. Following clarification, the motion proceeded.
• Motion to approve the February 4th meeting minutes by Charles Piso and seconded by
Will Elwell
• No discussion
• Motion carried unanimously
Working Group Survey
The Chair provided an update on the formation of work groups. Members were informed that a
survey had been distributed to identify interests and preferences, with responses still being
collected. Work groups will be limited to seven members each to balance workload and
participation. Both primary members and alternates may serve on work groups unless otherwise
determined.
It was clarified that work groups will be composed of committee members, though non-
committee subject matter experts may be consulted at the discretion of each group. Members
were encouraged to complete the survey by the end of the day to allow assignments to be
finalized and distributed promptly.
Working Group Scheduling
The Chair reported that staff recommend maintaining a consistent Wednesday meeting schedule
for work groups, either alternating with or adjacent to full committee meetings. This consistency
is intended to support project management, coordination with anticipated technical support staff,
and timely completion of deliverables. While recognizing that some work may require additional
meetings, consistency was emphasized as a guiding principle.
EMS System Governance – Background and Discussion
The Committee began substantive discussion on EMS system governance, identified as the initial
priority work group topic due to its foundational impact on all other components of the statewide
EMS plan.
Staff reported on background research into statewide EMS plans, noting that 19 states currently
maintain such plans. Plans from Maine and California were highlighted as strong reference
models. The Committee’s approach will focus on developing a standardized plan template,
which will then be populated through committee and work group deliberations.
Overview of Current Governance Structure
A historical overview of Vermont’s EMS governance structure was presented. The presentation
reviewed the original intent of EMS governance nationally and in Vermont as a partnership
between state government and regional districts. Districts were described as quasi-governmental
entities with statutory authority to administer EMS functions regionally, while the state EMS
office serves as the primary regulatory authority.
2
February 18, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
It was noted that although districts possess statutory authority to collect funds, employ staff, and
conduct business, this authority has rarely been exercised, resulting in uneven capacity and
effectiveness statewide. Areas of clarity, such as district authority over district medical advisors,
were contrasted with areas of ambiguity, including service licensing, enforcement, and
accountability.
Review of Prior Governance Work
Members reviewed governance work conducted during the previous year, including facilitated
exercises identifying which EMS functions should occur at local, regional, or state levels. It was
acknowledged that prior efforts stalled due to the complexity and sensitivity of governance
issues, as well as competing assessment timelines.
Members of the prior governance subgroup summarized their work, which included development
of a detailed draft governance model emphasizing equity, regional balance, and shared authority
between regional entities and the state EMS Office. The model proposed consolidating districts
into a smaller number of regions to improve administrative capacity, representation, and
consistency, while preserving appropriate escalation pathways for licensure and enforcement.
The Committee discussed unresolved governance challenges, including:
• Lack of minimum EMS system standards in statute
• Absence of clear performance metrics for response reliability and service availability
• Limited enforcement tools available to the state EMS Office
• Risks associated with suspending or revoking licenses without contingency service plans
• Challenges faced by small, rural, and volunteer-based services
• Need for improved transparency and early notification when services are unavailable
Members emphasized the need to balance public safety, equity, feasibility, and sustainability in
any future governance model.
Medical Direction
The Committee identified hospital-based medical direction as a relative strength of the current
system. Members expressed general agreement that governance reforms should preserve and
strengthen clinical medical oversight, while considering separation of administrative and
operational governance from clinical medical direction.
The Committee agreed that EMS system governance will remain the cornerstone issue for the
statewide EMS plan. Work group assignments will be finalized following survey completion, and
governance discussions will continue within the work group framework, informed by full
committee input and stakeholder engagement.
3
February 18, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
Committee Schedule
• March 6th – Vermont EMS Conference, University of Vermont, Dudley H. Davis Center,
Burlington, VT
o Virtual Option (Yes)
o 1:30 to 2 PM Education Council
o 2 to 4 PM Advisory Committee
• March 18th – Waterbury State Office Complex, Ash Conference Room, Waterbury, VT
o Virtual Option (Yes)
o 1:00 to 3:00 PM
• April 1st – Waterbury State Office Complex, Waterbury, VT
o Virtual Option (Yes)
o Time TBD
• April 15th - Morriston Ambulance Service, Morristown, VT
o Virtual Option (Yes)
o Time TBD
• May 6th – Waterbury State Office Complex, Waterbury, VT
o Virtual Option (Yes)
o Time TBD
• May 20th – Bennington Rescue Squad, Bennington, VT
o Virtual Option (Yes)
o Time TBD
• June 3rd – Waterbury State Office Complex, Waterbury, VT
o Virtual Option (Yes)
o Time TBD
• June 17th – Newport Ambulance Service, Newport VT
o Virtual Option (Yes)
o Time TBD
• July 1st – Waterbury State Office Complex, Waterbury, VT
o Virtual Option (Yes)
o Time TBD
• July 15th – Fairfax Rescue, Fairfax, VT
o Virtual Option (Yes)
o Time TBD
Adjournment
Motion to adjourn unanimously approved.
Meeting adjourned at 3:10 PM
4
February 18, 2026

---

### 2026-02-04 — Vermont Board of Medical Practice — February 04, 2026

**[MINUTES] 2026-02-04_pre-ems-advisory-committee-minutes-2.4.26.pdf**

Vermont Emergency Medical Services
Education Council & Advisory Committee

Meeting Minutes

Education Council
Date: February 4, 2026
Location: Waterbury Ambulance Service, Waterbury (VT), & Microsoft Teams
Meeting Called to Order: 12:30 PM by Pat Malone

Rollcall

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     |             |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     |             |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     | Corey Boisvert   |                |     | Present     |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  | Jim Finger     |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     |             |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     |  Present    |     |                  | Marc Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     | Present     |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     | Richard Bowman   |                |     | Present     |
|              | Michael Randzio   |     | Present     |     |                  | Will Elwell    |     | Present     |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              | Liz Couto         |     | Present     |     |                  | Lee Krohn      |     |             |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

1
February 4, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
Non-members in attendance: Courtney Newman, Donna Jacob, Ray Walker, Dan Wolfson,
Liam Knight
Education Council Structure
The Committee first convened as the Education Council to discuss its structure and membership.
The Chair clarified that, procedurally, only members of the EMS Advisory Committee may serve
as official members of the Education Council.
The Chair introduced the question of whether the Education Council should be formally
established as a named subgroup or workgroup of the Advisory Committee, composed of a
defined group of members, or whether it should remain open to all members on an ongoing basis.
Multiple members expressed support for establishing a formal subgroup consisting of individuals
with experience and interest in EMS education. Discussion emphasized the value of having a
core group with educational expertise to ensure focused, consistent work, particularly given the
anticipated workload in the coming year.
Members noted that the Education Council has previously functioned effectively as a vetting and
advisory body for education-related initiatives, including curriculum and competency
recommendations. It was emphasized that the Council should serve as a resource to the EMS
Training Administrator, providing informed input and endorsements prior to forwarding
recommendations to the full Advisory Committee.
Additional discussion highlighted the importance of including members with diverse
perspectives, such as instructors, administrators, and operational leaders, including those with
experience in budgeting and service management. The potential future appointment of a Chair
and Vice Chair for the Education Council was identified as a topic for later consideration.
Consensus:
While no formal action was taken, the members present expressed consensus support for
recommending that the Advisory Committee formally establish an Education Council subgroup
with defined membership, while continuing to allow broader participation as appropriate.
Education Council Next Steps
The Chair outlined proposed next steps, including:
• Reporting the consensus recommendation to the full Advisory Committee.
• Soliciting interest from Advisory Committee members and alternates to serve on the
Education Council.
• Considering inclusion of senior instructors and other experienced stakeholders.
• Identifying an appropriate number of members (approximately six to eight).
• Aligning Education Council meetings with the regular monthly Advisory Committee
meeting schedule, with adjustments as needed.
2
February 4, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee
• The Education Council will meet on the third Wednesday of the month, and for 30
minutes prior to the EMS Advisory Committee meeting. One exception being the council
will meet on March 6th, at the EMS Conference.
Adjournment
• Motion to adjourn unanimously approved.
• Meeting adjourned at 1:30 PM
3
February 4, 2026

Vermont Emergency Medical Services
Education Council & Advisory Committee

EMS Advisory Committee
Date: February 4, 2026
Location: Waterbury Ambulance Service, Waterbury (VT), & Microsoft Teams
Meeting Called to Order: 1:30 PM by Drew Hazelton

Rollcall

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     |             |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     | Corey Boisvert   |                |     | Present     |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  | Jim Finger     |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     |             |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     |  Present    |     |                  | Marc Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     | Present     |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     | Richard Bowman   |                |     | Present     |
|              | Michael Randzio   |     | Present     |     |                  | Will Elwell    |     | Present     |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              | Liz Couto         |     | Present     |     |                  | Lee Krohn      |     |             |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

Non-members in attendance: Courtney Newman, Donna Jacob, Olivia Coe, Ray Walker,
Connor Dunn
4
February 

*[document truncated for length]*

---

### 2026-01-21 — Vermont Board of Medical Practice — January 21, 2026

**[MINUTES] 2026-01-21_eprip-EMS-advisory-minutes-1.21.26.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: January 21, 2026
Location: Barre Town Municipal Building, Board Room, Barre (VT), & Microsoft Teams
Meeting Called to Order: 1:00 PM by Drew Hazelton

Rollcall – Committee Members

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     | Present     |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     | Corey Boisvert   |                |     | Present     |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     |             |
|              |                   |     |             |     |                  | Jim Finger     |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     | Present     |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     | Present y   |     |                  | Marc Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     | Present     |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     |                  |                |     |             |
|              | Michael Randzio   |     | Present     |     |                  |                |     |             |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
| Liz Couto    |                   |     | Present     |     |                  | Lee Krohn      |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

Non-members in attendance: Courtney Newman, Donna Jacob, Olivia Coe
1
December 10, 2025

Vermont Emergency Medical Services
Advisory Committee
Introduction
Liz Kudo, the representative for the Vermont Association of Hospitals and Health Systems,
introduced herself.
Health Department Remarks and Committee Expectations
Will Moran, state EMS Chief, expressed appreciation for the committee’s work of the last year
and emphasized:
• Continued effort to strengthen relationships between VDH and the Committee
• Recognition of historical tensions and progress since earlier administrations
• Commitment to providing staff support and resources to the committee
A formal request was made that Committee members:
• Extend the same level of respect to all Health Department staff as fellow committee
members.
• Engage Health Department staff with curiosity and professionalism, even during
disagreement.
• Direct difficult or heated concerns to Will Moran, rather than staff members.
Meeting Minutes Review & Approval
The minutes from December 10th, 2025, meeting were previously distributed to the committee.
• Motion to approve the December 10th meeting minutes by David Danforth and seconded
by Charles Piso.
• A committee member inquired if the minutes had been previously districted; the minutes
were distributed the day after the last meeting.
• Motion carried with one abstention.
EMS Education Council Meeting Logistics
The committee reviewed the role and structure of the Education Council. The Education Council
is a formal sub-group of the EMS Advisory Committee. All Advisory Committee members are
members of the Education Council, though participation is optional. Open Meeting Law
requirements apply; meetings must be warned and minutes maintained. Legal guidance will be
sought so to ensure compliance with the law.
Members interested in formally participating should notify Council Chair Pat Malone.
Membership of the council will be formalized at the February meeting. Non-committee
members (e.g. senior instructors, instructor coordinators) are encouraged to attend and participate
in discussions.
The EMS Education Council will meet for 30 minutes monthly; the council meeting will precede
the EMS Advisory Committee meeting.
2
December 10, 2025

Vermont Emergency Medical Services
Advisory Committee
Legislative Report
The report was submitted to the state legislature on time. Pat Malone testified before House
Government Operations and Military Affairs and spoke to several findings. The committee was
interested, asked questions, and expressed their interest in having a representative of the EMSAC
back to continue the discussion.
A request from a member of the EMSAC to the EMSAC chair that future testimony more
thoughtfully distinguishes between personal expertise and opinion, and consensus developed by
the committee. A specific concern raised about statements related to paramedic deployment and
rural municipal agencies. The Committee clarified use of the “paramedic paradox” concept and
agreed to exercise caution in framing future discussions.
Data Quality and Interpretation
The committee engaged in extensive discussion regarding data quality and interpretation.
Limitations in data do exist (availability, consistency, and accuracy). Data was aggregated from
multiple years and sources; data provided to the committee from CCG was de-identified. The
committee chair emphasized the report was intended for a system-level analysis, not agency or
municipal comparisons. Committee members should consistently reinforce report limitations
when discussing findings.
Policymakers may rely too heavily on executive summaries; improving data infrastructure is a
core future objective. Committee members should consistently reinforce report limitations when
discussing findings.
• Motion to authorize the EMSAC committee chair to ask the legislature to amend the
DEVA Ambulance Provider Tax Form to include additional reporting elements by David
Danforth, and seconded by Matt Parish.
• No further discussion and the motion carried.
Financial Report and Consultant Contract Status
Following the end of Cambridge Consultant Group contact, Rescue Inc. spent $43,025.01 on
behalf of the EMSAC. The subrecipient grant to Rescue Inc., the fiscal sponsor for the EMSAC,
has been executed, and will be invoicing the Health Department for those expenses.
The original appropriation by the legislature was $370,000.00. Approxmittly $150K was spent
on the work completed by the Cambridge Consulting Group. Following the processing of the
latest invoice by the Department, approximately, $176, 975 will remain to support the EMSAC
in this project.
• Motion to contract again with MedOps to continue their work with the EMS Advisory
Committee by Pat Malone, and seconded by David Danforth.
• An amendment to the motion was made to place a spending cap of $100,000 on the
contract. The amendment was excepted.
3
December 10, 2025

Vermont Emergency Medical Services
Advisory Committee
• Discussion focused on the ongoing need for technical writing, project coordination and
analysis support. Members expressed a desire to continue working with the prior
consultants. If necessary, other contractor(s) can be obtained to accomplish the project.
• The motion carried.
Committee Leadership
The committee chair initiated a conversation on committee leadership, and who will be the
committee chair for the year. Drew Hazelton expressed his interest in continuing in the role,
however, would support the notion of electing a vice-chair.
• Motion to nominate Drew Hazelton as the EMS Advisory Committee chair for calendar
year 2026 by David Danforth and seconded by Will Moran.
• No discussion: the motion carried unanimously.
• Motion to appoint Pat Malone as the vice chair of the EMS Advisory Committee for
calendar year 2026 by David Danforth, and second Lee Krone.
• Pat Malone disclosed that his contract with the university expires mid-year; if his contract
is not extended it is unclear if he will continue working with the committee.
• The motion carried unanimously.
Future Work and Legislative Mandates
The committee reviewed the statutory requirements for the next phase of the project. This
includes the design of a statewide EMS system and developing a budget review framework.
Additionally, the committee is responsible for developing a five-year statewide plan to improve
the coordinated delivery of EMS statewide. This includes specific goals, a time frame for
achieving specific goals, cost data and alternative funding sources for achieving the stated goals,
and performance standards for evaluating the stated goals.
Recommendations for the design of a statewide EMS system, an EMS budget review framework,
and the five-year plan are all due to the legislature by December 15, 2026. To ensure all
members of the committee have the necessary time to review the draft recommendations with
their constituents prior to voting, the committee has set a draft report deadline of October 15,
2026.
The committee acknowledged the challenges that lie ahead. Developing consensus on
definitions, what a “statewide EMS plan” should include, or what is or is not included within a
statewide EMS system, will all require thorough discussion. Disagreement is anticipated in the
areas of governance and system design. Looking at the statewide EMS plans for other states can
and will inform the committee’s work. The participation of stakeholders in the process is
anticipated.
EMS Special Fund
The EMS Special Fund receives an annual appropriation of $450,000. Funds can b

*[document truncated for length]*

---

### 2025-12-10 — Vermont Board of Medical Practice — December 10, 2025

**[MINUTES] 2025-12-10_eprip-EMSAC-Final-Report-2025.pdf**

Vermont Emergency Medical Services System Assessment
December 15, 2025
Emergency Medical Services Advisory Committee Report

Executive Summary
Vermont’s EMS system is rooted in service, community values, and an unwavering commitment
to ensuring that every person—regardless of geography—has access to reliable, equitable, and
high-quality emergency medical care. Today, Vermont stands at a pivotal moment. With
strategic investment, collaboration, and a shared vision, there is an opportunity to build a more
coordinated and sustainable EMS system—one that strengthens the workforce, supports
providers, and enhances patient care statewide. By embracing innovation and planning for long-
term resiliency, Vermont can shape an EMS system that not only meets today's needs but also
elevates the future of emergency medical care for generations to come.
The Vermont EMS assessment—compiled from statewide data collection, cost reports, and
system surveys—reveals a complex and uneven landscape. Call volumes are rising, workforce
shortages are worsening, and financial deficits are deepening. The total annual system cost is
approximately $98 million, but insurance reimbursement covers only $53 million, leaving local
taxes and volunteers to bridge a widening gap.
The recent passage of Act 157 of 2024, which formally designates EMS as an essential service,
is an important policy milestone. However, without aligned funding, governance reform, and
workforce investment, Vermont's EMS system cannot reliably continue to deliver equitable,
high-quality emergency care to all residents.
Emergency Medical Services
Emergency Medical Services is an integrated system of emergent and non-emergent practice of
medicine in the out-of-hospital environment. This includes personnel and resources designed to
assess, treat, and determine the appropriate disposition of patients with injury and illness and
those in need of specialized care and safe transportation. EMS is a vital component of the
healthcare, public health, and public safety systems.
Overall System Performance
Vermont's Emergency Medical Services face significant challenges that compromise
effectiveness and sustainability. Access to EMS varies widely across the state, with inconsistent
service delivery, response times, and reliability from town to town. The system struggles with
increasing call volumes that strain capacity, while emergency and non-emergency interfacility
transportation remains unreliable in parts of the State.
Inadequate funding creates critical gaps in essential functions, including training, education, data
collection, and medical direction. Additionally, the current infrastructure does not support
Mobile Integrated Health (MIH) initiatives, limiting opportunities for more comprehensive
community healthcare delivery.
2 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

Vermont's EMS system retains several core strengths despite growing pressures. The State
benefits from a deeply committed workforce, many of whom volunteer their time to ensure
neighbors receive emergency care. This community-based model reflects Vermont's values of
service and mutual aid. The enactment of Act 157 of 2024 officially recognizes EMS as essential
and signals a bipartisan commitment to systemic reform.
Key Findings
Service levels, response times, staffing models and reliability vary significantly by town.
Emergency and non-emergency interfacility transportation resources are not consistently
reliable in parts of the State.
EMS agencies operate with different revenue mixes, leading to notable funding gaps between
agencies.
Inadequate funding creates gaps in training, education, data collection, and medical direction
needed for system quality.
Until regulatory and funding models align with MIH delivery and costs, the current system
cannot support MIH implementation.
Governance and System Structure
The Vermont EMS system operates under a multi-tiered governance framework. The Office of
Emergency Medical Services, housed within the Department of Health, serves as the state
regulatory body providing oversight that includes licensing of services and personnel, conducting
investigations, collecting system-wide data, developing training programs, and establishing
clinical protocols. This centralized function supports and oversees 13 regional districts, which
provide varying levels of local system oversight.
However, Vermont's 13-district system is not functioning consistently or sustainably. Districts
operate without enforcement authority and face role ambiguity, resource constraints, and
insufficient funding. This lack of adequate funding and support has resulted in insufficient
physician medical oversight and assessment across the system. Many areas of Vermont rely on
volunteer physicians to provide medical oversight, creating gaps in clinical guidance and quality
assurance.
To evaluate the operational and financial characteristics of Vermont's EMS system, the
committee analyzed four service delivery models. These models include regional EMS services,
career fire department-based EMS, municipal services, and local service providers. The analysis
examined each model's structure, funding sources, response capabilities, and staffing models.
3 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

1. Regional EMS Services
Regional EMS services require the least local tax support and provide the majority of
interfacility transport (IFT) work statewide. Response times to critical incidents are longer
than fire-based systems but better than stand-alone municipal systems. These services use
mixed staffing models, including full-time, part-time, and volunteer staff, with 79% providing
paramedic services.
2. Career Fire Department-Based EMS
Career fire department-based EMS is the most expensive model, but it provides the shortest
response times. These services offer very little IFT support, use 100% paid staff, and 100%
provide paramedic service. Fire-based ambulance services have higher costs per call and per
capita due to their additional fire suppression responsibilities.
3. Municipal Services
Municipal services are slightly more dependent on local tax support than regional services,
though less than fire-based models. Response times are higher than those of regional
providers. Several services support IFT needs, but most do not. These services rely more on
part-time and volunteer labor than regional providers, with 91% providing paramedic services.
4. Local Service Providers
Local service providers are comparable to municipal services in cost, response time, and IFT
work, but have slightly lower paramedic availability.
Key Findings
Insufficient funding and support leave the system with inadequate physician medical oversight
and assessment. Physician medical advisors (usually insufficiently compensated) provide
medical oversight in many areas of Vermont.
Fragmented data across multiple systems creates data quality issues for the advisory
committee, the Office of EMS, and leaders.
The manual data collection process used for this report is not viable moving forward.
Districts lack enforcement authority, role clarity, and sufficient funding.
The State EMS Office is understaffed and under resourced.
Data Sources and Limitations
The Vermont EMS Assessment faced significant data challenges that impacted the
comprehensiveness and precision of the analysis. The assessment relied on a complex patchwork
of information sources, including self-reporting surveys, Vermont EMS data systems, and
publicly available information, because no unified system exists for collecting and storing EMS
data. While the team made efforts to verify data with service leaders, they had to estimate some
4 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

information due to unavailable records. Additionally, reporting periods varied widely across
services. Ground ambulance data covered the period from 2023 to 2025 and could be based on
fiscal or calendar years, or a mix.
Furthermore, the analysis excluded first-response services from cost analyses due to insufficient
data and a lack of verification. Cost calculations for services operating mixed business lines—
such as fire departments providing both fire suppression and EMS—used a proportional
allocation formula in which total organizational expenses were divided by the ratio of ground
ambulance volume to total service volume.
Staffing projections were standardized under the assumption of one crew for every 1,200 calls,
with each crew requiring nine full-time equivalents (FTE), 18 part-time personnel, or a
combination thereof; however, this approach may overlook efficiencies based on actual service
staffing or workload rather than theoretical estimates.
Key Findings
Inconsistent data entry, inadequate collection tools, and manual processes fragment data,
hindering accurate system monitoring and reliability measurement. Prioritizing data collection
and analysis is essential.
The manual data collection process required for this report is not viable for ongoing EMS
system needs.
Underfunding of Vermont's EMS records system results in insufficient and inconsistent data
collection.
Insufficient financial resources and staffing limits the State's ability to gather accurate,
actionable EMS data for planning and oversight.
Without an integrated, statewide computer-aided dispatch system, the State cannot prioritize
time-sensitive 9-1-1 calls, monitor the system in real time, or effectively evaluate response
data.
There is little data on training, education, and support.
Interfacility transport (IFT) data from hospitals is unavailable to this committee
Statewide EMS Data
In 2024, Vermont's EMS system responded to approximately 100,000 911 calls, reflecting a 6%
increase from the previous year. Of the 100,000 calls, 29,500 did not result in transport.
Additionally, Interfacility transfers totaled 28,000, an 8% increase over the previous year.
• 911 Emergency Calls: ~100,000 (?6%)
Non-Transport Calls: 29,500
• Interfacility Transfers: 28,000 (?8%)
• Licensed Ambulance Services: 65 in-state, nine out-of-state
5 Vermont EMS Advisory Committee - EMS System Assessment December 15, 2025

• Total System Cost: $98 million
Financial Assessment
Overall, the financial model is challenging and increasingly unsustainable. Nearly half of EMS
agencies operate at a deficit, as reimbursement rates do not cover the actual costs of readiness.
The total cost of Vermont-based ambulances is approximately $98 million, funded by various
sources:
• Insurance reimbursement: ~$53 million (54% cost recovery rate)
• Local tax support: ~$43 million
• Volunteer labor (valued): $9.7 million
• Annual fundraising: ~$1.2 million
• Provider taxes: ~$1.4 million
Ambulance services pay provider taxes to the state, which then uses this revenue to leverage
additional federal Medicaid funds. The system also relies on volunteer labor; however, declining
volunteer availability and increasing requirements make this model increasingly unsustainable.
Service Type Average Cost Per Capita Cost Average % of Staff
per Call Avg. Reimbursement Compensated
per Transport
Fire-Based $1,168 $189 $476 100%
Municipal $801 $57 $561 43%
Regional $670 $31 $598 57%
Local $729 $53 $691 44%
Key Findings
Inadequate ambulance reimbursement from Medicare and Medicaid forces towns to cover
costs through property taxes, creating funding disparities across communities.
Medicare does not reimburse for patients who are treated yet not transported, creating a
financial burden on services.
Act 157 of 2024 requires Medicaid reimbursement for certain non-transport calls but Medicare
does not reimburse non-transport calls.
A reimbursement system needs to be created to support Mobile Integrated Health (MIH)
services.
Vermont lacks mandatory, systematic state-level financial reporting for EMS agencies.
Volunteer availability is decreasing statewide.
Delivery costs vary sign

*[document truncated for length]*

---

**[MINUTES] 2025-12-10_eprip-EMS-advisory-minutes-12.10.25_0.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: December 10, 2025
Location: Vermont EMS Academy, Newfane (VT), & Microsoft Teams
Meeting Called to Order: 1:03 PM by Drew Hazelton

Rollcall – Committee Members

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     |             |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     | Present     |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     |                  | Jeff Johansen  |     |             |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     |             |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     |             |
|              |                   |     |             |     |                  | Jim Finger     |     | Present     |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     | Present     |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     | Present     |     |                  | Marc Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     |             |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     |                  |                |     |             |
|              | Michael Randzio   |     | Present     |     |                  |                |     |             |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              |                   |     |             |     |                  | Lee Krohn      |     |             |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     |             |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

1
December 10, 2025

Vermont Emergency Medical Services
Advisory Committee
Non-members in attendance: Courtney Newman, Connor Dunn, Donna Jacob, Olivia Coe,
Julia Sugg, Corey Boisvert, Dan Wolfson
Meeting Minutes Review & Approval
The minutes from December 3rd, 2025, meeting were previously distributed to the committee.
• Motion to approve the December 3rd meeting minutes by Chelsea Dubie and seconded by
Adam Heuslein.
• Motion carried unanimously.
EMS Education Council Meeting Logistics
Discussion regarding the upcoming Education Council meeting on January 21st, 2026, and
whether meeting invites should be restricted to council members. The committee agreed that the
invite should go to the full committee, ensuring transparency and optional participation for non-
council members.
Legislative Report
Drew Hazelton reminded members that the primary purpose of today’s meeting was to:
• Review of the final legislative report draft
• Incorporate language regarding the Public Safety Telecommunications Report
• Finalize the document for submission by the statutory December 15 deadline
Drew Hazelton acknowledged Julia’s extensive work over the weekend to consolidate feedback,
reduce redundancies, preserve committee intent, and format the draft. Several members noted the
report’s length was condensed significantly while still capturing all major themes.
A motion to table adoption of report to legislature and revisit at a meeting that would be
scheduled at the end of the month due to the late distribution of the report was made by Chelsea
Dubie and seconded by Marc Hachey.
The rational for the motion:
• The final draft was sent to the Health Department for distribution to the committee late
the previous night (approximately 10 PM).
• The VDH policy and legal teams had no opportunity to review the report.
• EMS district representatives and represented groups also lacked the expected review
window.
• The committee risks submitting a report that does not reflect a polished consensus.
• There is no legislation being requested by the report, reducing urgency.
Several members strongly opposed the motion:
• The committee spent six hours in the previous meeting reviewing all sections line-by-
line, providing members of the committee to propose edits.
• The current draft includes all edits requested at the last meeting.
• Several other committees are already advancing EMS-related initiatives without
including the EMSAC.
2
December 10, 2025

Vermont Emergency Medical Services
Advisory Committee
• The report reflects the work of the committee (EMSAC), not the Health Department or
other stakeholder groups.
• Inaction by the committee risks the legislature or others setting EMS policy without
committee input; the committee has a statutory responsibility to deliver this work.
• Several members stated the Health Department has only one vote, it cannot slow the
committee’s overall process.
An amendment to the motion was proposed:
• Schedule a special meeting next week and vote on the report no later than December 15,
allowing the committee to meet the deadline.
• Concern raised that voting on the due date leaves no time to incorporate final edits.
The amendment was withdrawn; the original motion stood. The outcome of the committee vote
on the motion is:
• Votes: Yes - 4, No – 8, Abstain – 1
Name Vote
Adam Heuslein No
Leslie Lindquist Yes
David Danforth No
Kate Rothwell Abstain
Charles Piso No
Jim Finger No
Bill Camarda No
Eric Wilson No
Drew Hazelton No
Pat Malone No
Marc Hachey Yes
Aaron Collette Yes
Chelsea Dubie Yes
The committee recessed from 1:37 – 2:10 PM to allow committee members to review the report.
Upon reconvening, the committee resumed a detailed review and significant areas of discussion
included:
• Public Safety Telecommunication
o Language summarizing EMS implications of the Public Safety Communications
report.
o Recommendation to reference the report rather than re-summarizing.
o Recommendation to include legal citations.
3
December 10, 2025

Vermont Emergency Medical Services
Advisory Committee
• Glossary & Definitions
o The glossary added since the last meeting was written by Pat Malone using
national EMS definitions from NHTSA, Agenda for the Future, Maine EMS, and
others.
o Recommendation to include a citation for all glossary sources.
o Agreement ton the importance of consistent formatting (APA, title page,
headings).
o Agreement that final formatting should occur after content approval.
• System Structure & Service Delivery Clarifications
o Clarified Vermont has 90 first response agencies, and first responder coverage is
not statewide, and availability varies significantly.
o Clarification added for non-transported vs transported call totals to avoid
misinterpreting statewide EMS call volume.
• Air Ambulance Data
o Discussion whether “most air medical transports are out-of-state agencies” is
accurate.
o Leslie Lindquist explained:
? The Burlington based helicopter is staffed by Vermont clinicians but
licensed through Dartmouth-Hitchcock Medical Center.
? LifeNet of New York handles a significant share of flights.
? True proportions are unclear due to data limitations.
Concerns regarding the formatting of the report were raised. The Public Safety Communications
Report is noted as having a polished layout and it was recommended to match its style.
Vote on Final Draft of Committee Report
• Motion to accept and present the document as amended in this meeting to go forward to
the legislature by Adam Heuslein and seconded by Charles Pizzo.
• Amendment to the initial motion by Aaron: "the group agrees to the document content as
printed, baring any formatting, structural improvements or professional appearance edits
to enhance the readability. The substantive language of the document shall not be
amended after this vote."
• Votes: Yes – 11, No – 0, Abstain - 2
Name Vote
Adam Heuslein Yes
Leslie Lindquist *
David Danforth Yes
Kate Rothwell Yes
Charles Piso Yes
Jim Finger Yes
Bill Camarda Yes
Eric Wilson Yes
Drew Hazelton Yes
Pat Malone Yes
4
December 10, 2025

Vermont Emergency Medical Services
Advisory Committee
Marc Hachey Abstained
Aaron Collette Yes
Chelsea Dubie Abstained
Corey Boisvert Yes
* Absent at the time of voting.
Committee Schedule
• January 21 – Barre Town Municipal Building, Board Room, 149 Websterville Rd Barre,
VT 05641
o 1 to 3 PM
o Virtual - Microsoft Teams
• February 18 – Middlebury EMS, 55 Collins Dr, Middlebury, VT 05753
o 1 to 3 PM
o Virtual - Microsoft Teams
• March – The monthly meeting will be held at the EMS conference; the date and time will
be finalized and published.
Adjournment
Motion to adjourn unanimously approved.
Meeting adjourned at 3:15 PM
5
December 10, 2025

---

### 2025-12-03 — Vermont Board of Medical Practice — December 03, 2025

**[MINUTES] 2025-12-03_eprip-EMS-advisory-minutes-12.3.25.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: December 3, 2025
Location: Alumni Hall, Barre (VT), & Microsoft Teams
Meeting Called to Order: 10:16 PM by Drew Hazelton

Rollcall – Committee Members

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     | Present     |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     |             |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     | Present     |     |                  | Jeff Johansen  |     |             |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     | Present     |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     |             |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     | Present     |     |                  | Mark Hachey    |     | Present     |
|              | Chris LaMonda     |     | Present     |     |                  | Billy Fritz    |     |             |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     |                  |                |     |             |
|              | Michael Randzio   |     | Present     |     |                  |                |     |             |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              |                   |     |             |     |                  | Lee Krohn      |     |             |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

1
December 3, 2025

Vermont Emergency Medical Services
Advisory Committee
Non-members in attendance: Courtney Newman, Dan Wolfson, Connor Dunn, Donna Jacob,
Julia Sugg, Liam Knight, Elizabeth Couto, Chris Lamonda, Olivia Coe, Corey Boisvert, Liam
Knight, Maggie Burke, Michaela Brown
Meeting Minutes Review & Approval
The minutes from November 19th, 2025, meeting were previously distributed to the committee.
• Motion to approve the November 19th meeting minutes by Adam Hueslin, and seconded
by Michael Tarbell.
• The minutes were updated to reflect Billy Fritz’s attendance.
• Motion carried unanimously.
Office of EMS Update
EMS district chairs received notification last month of an update regarding the EMS Special
Fund. On an annual basis, districts will have a one-month period starting on January 1, 2026,
and ending on January 31, 2026, to apply for a sub-recipient grant. The grant performance
period will begin on July 1, 2026, and end on June 30, 2028.
EMS districts have several options to choose from to access state funding including applying for
a grant directly, utilizing a fiscal sponsor to apply on their behalf, or coordinating with state EMS
officials to direct resources to their region to meet their educational needs. Districts are asked to
bundle all application materials together and submit as a single package. A reminder will be
going out about the upcoming application window.
State EMS officials requested the Advisory Committee collaborate on developing a strategy to
spend down the remaining funding following the closing of the application window; this will be
a topic on the agenda for the January committee meeting.
Education Council Update
The council met for the first time in more than a year. Moving forward, the council will meet
before the monthly Advisory Committee meeting; the meeting will be scheduled for 30 minutes.
The next meeting will be on January 21, 2026.
Earlier today the council voted to endorse the Advanced EMT Student Minimum Competences
guidelines developed by State EMS Training Coordinator Courtney Newman.
Rural health Care Transformation Grant
The State submitted its application in early November for a 5-year federal healthcare
transformation program. EMS was nearly absent from the application—only mentioned once as
a “critical partner,” and not included as one of the participating stakeholders. This is inconsistent
with many other state applications across the country.
Patrick Malone suggests drafting a letter expressing concern; others suggest inviting the AHS
Secretary to a meeting instead. The committee chair asked members to review the grant
2
December 3, 2025

Vermont Emergency Medical Services
Advisory Committee
application (available on the AHS website) and be prepared to share their thoughts at the next
meeting.
Public Safety Telecommunications Task Force Report
A newly released 6-page report contains recommendations on dispatch modernization, which
includes:
• Statewide multidisciplinary CAD system
• Interoperability standards
• Creation of a new oversight board
• Discussion of long-term funding needs
No mention of priority medical dispatch (PMD); no explicit consolidation recommendations.
Key concerns raised are cost projections may be unrealistic, and EMS-hospital communications
system gaps not addressed.
Members were asked to review the report before next week's meeting; the committee may adopt
supportive or corrective language into EMSAC’s own legislative report.
Legislative Draft Report Review
The committee reviewed each section of the report, primarily focusing on key findings. Before
starting, the committee discussed and agreed the language must be accurate and evidence based;
avoid overly strong or unsupported claims; ensure clarity about system inconsistencies without
inadvertently prompting unrealistic state mandates.
The committee systematically worked through the report, with attendees both in person and
attending remotely contributing to the discussion. The report was updated in real-time.
All key findings were reviewed; however there was not sufficient time for the committee to
review the entire narrative. Committee members were encouraged to submit their remaining
comments to the technical writer no later than Friday, December 5. The committee will continue
the discussion on the report at the next meeting scheduled in just one week.
Committee Schedule
• December 10 – Vermont EMS Academy, 1096 VT-30, Newfane, VT 05345
o 1 to 3 PM
o Virtual - Microsoft Teams
Adjournment
Motion to adjourn unanimously approved.
Meeting adjourned at 3:15 PM
3
December 3, 2025

---

### 2025-11-19 — Vermont Board of Medical Practice — November 19, 2025

**[MINUTES] 2025-11-19_eprip-EMS-advisory-minutes-11.19.25_0.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: November 19, 2025
Location: Williston Fire Department, Williston (VT), & Microsoft Teams
Meeting Called to Order: 1:05 PM by Drew Hazelton

Rollcall – Committee Members

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     |             |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     | Present     |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     |                  | Jeff Johansen  |     |             |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     |             |
|              |                   |     |             |     | David Danforth   |                |     |             |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     | Present     |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     | Present     |     |                  | Mark Hachey    |     | Present     |
|              | Chris LaMonda     |     | Present     |     |                  | Billy Fritz    |     | Present     |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     |                  |                |     |             |
|              | Michael Randzio   |     | Present     |     |                  |                |     |             |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              |                   |     |             |     |                  | Lee Krohn      |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     |             |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

1
November 19, 2025

Vermont Emergency Medical Services
Advisory Committee
Non-members in attendance: Courtney Newman, Dan Wolfson, Connor Dunn, Ray Walker,
Donna Jacob, Julia Sugg, Gene Bifano, Mike Chiarella, Liam Knight, Kevin Argentieri, Marsha
McCombie, Ashley Fontaine, Elizabeth Couto
Meeting Minutes Review & Approval
The minutes from November 5th, 2025, meeting were previously distributed to the committee.
• Motion to approve the November 5th meeting minutes by Adam Hueslin, and seconded
by X.
• No discussion; motion carried with one abstention.
Financial Report
Drew Hazelton reported on expenses by the committee to date:
• $5,333.37 paid to the SAPPY Company for contract work.
• $97.00 spent on software.
Total expenditures to date: $32,172.78
Project Timeline and Deliverables Update
Drew reviewed expectations for the statewide EMS system assessment. Two meetings remain
before the statutory report is due in December. A rough draft of findings must be ready for the
December 3rd meeting. The final deliverable will be voted on at the following meeting before
submission to the Legislature. This phase is strictly an assessment; solutions fall under the
separate five-year plan to be developed next. Feedback submitted via QR code/forms has been
compiled by consultant Julia Sugg.
System Assessment Findings
Drew Hazelton led a structured review of submitted comments. Julia documented revisions for
incorporation into the draft.
Overall System Performance consensus findings:
• EMS coverage exists statewide, though service levels and reliability vary.
• Access is not equitable across Vermont; significant variation exists between counties and
between rural vs. urban settings.
• Interfacility transport (IFT) capacity is inconsistent and often unreliable; clearer language
will be drafted to reflect this.
• System demand is increasing, including call volume and patient complexity; phrasing
will be refined to reflect measurable data.
• Funding disparities exist across agencies, with EMS lacking the systematic support
provided to police and fire services.
• Agencies rely on patchwork revenue streams, leading to inconsistent financial stability.
• CAD limitations and lack of statewide dispatch integration significantly impair system
coordination and measurement.
2
November 19, 2025

Vermont Emergency Medical Services
Advisory Committee
Governance consensus findings:
• Medical direction and governance are not consistent statewide.
• The current district system, unchanged since the 1970s, no longer reflects operational
needs.
• Governance structures do not ensure equitable representation or system-wide
coordination.
• Mobile Integrated Health (MIH) lacks a functional governance framework.
Data consensus findings:
• Data collection is inconsistent, with significant variability in documentation quality.
• Lack of standardized data entry affects accuracy of clinical metrics and system analysis.
• Many agencies lack capacity or training for proper reporting; mandatory data education
was suggested for the five-year plan.
• Cost data is unavailable, limiting ability to evaluate financial needs.
• No statewide CAD integration limits dispatch data accuracy and response-time
assessment.
• Education data is similarly incomplete or difficult to obtain.
Finance consensus findings:
• The fee-for-service reimbursement model is outdated and inadequate.
• Medicaid reimbursement has not kept pace with cost of service.
• Non-transport calls and MIH services lack sustainable reimbursement pathways.
• Agencies vary widely in financial resources, often based on local tax bases rather than
service need.
• Administrative capacity varies dramatically; some small volunteer agencies responded
faster than fully staffed municipal departments.
Quality Measures consensus findings:
• State data shows Vermont falls below national benchmarks in numerous measures, but
documentation deficiencies make the true picture unclear.
• The committee agreed to avoid stating “all measures” due to data limitations.
• Wide disparities between districts are likely due to documentation, agency size, and
system design, not solely clinical performance.
• Response-time data from CAD is insufficient for drawing reliable conclusions.
System Reliability consensus findings:
• Only limited reliability data exists (mainly the Cambridge heat map).
• It is unclear how Cambridge produced some findings due to lack of statewide CAD or
mutual-aid tracking.
• Mutually dependent metro systems (e.g., Chittenden County) show high inter-agency
dependency by design, not system failure.
3
November 19, 2025

Vermont Emergency Medical Services
Advisory Committee
Public / Member Comments:
• Importance of differentiating rural vs. urban system challenges.
• Desire for equitable voice and representation, particularly from smaller districts.
• Need for clear legislative alignment across multiple committees (dispatch, healthcare,
EMS).
• Continued emphasis on establishing proper data governance, education, and
infrastructure.
Next steps:
• Julia will revise the document based on today’s guidance.
• Members encouraged to continue submitting recommendations via the active form; action
items will be retained for the five-year plan.
• Rough draft to be reviewed at the December 3rd meeting.
Committee Schedule
• December 3 – Alumni Hall, Washington Room, 20 Auditorium Hill, Barre, VT 05641
o 10 to 3 PM
o Virtual - Microsoft Teams
• December 10 – Vermont EMS Academy, 1096 VT-30, Newfane, VT 05345
o 1 to 3 PM
o Virtual - Microsoft Teams
Adjournment
Motion to adjourn unanimously approved.
Meeting adjourned at 3:40 PM
4
November 19, 2025

---

### 2025-11-05 — Vermont Board of Medical Practice — November 05, 2025

**[MINUTES] 2025-11-05_eprip-EMS-advisory-minutes-11.5.2025.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: November 5, 2025
Location: Waterbury State Office Complex, Waterbury (VT), & Microsoft Teams
Meeting Called to Order: 10:02 AM by Drew Hazelton

Rollcall – Committee Members

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     |             |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     | Present     |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     |             |     |                  | Jeff Johansen  |     | Present     |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     | Present     |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     |             |
|              |                   |     |             |     | Bobby Maynard    |                |     | Present     |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     | Present     |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     | Present     |     |                  | Mark Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     |             |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     |             |     |                  |                |     |             |
|              | Michael Randzio   |     | Present     |     |                  |                |     |             |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              |                   |     |             |     |                  | Lee Krohn      |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

1
November 5, 2025

Vermont Emergency Medical Services
Advisory Committee
Non-members in attendance: Courtney Newman, Dan Wolfson, Connor Dunn, Ray Walker,
Olivia Coe, Donna Jacob, Barb Neal, Julia Sugg
Update – Public Safety Communications Task Force
Barb Neal, executive director of E911, and co-chair of the task force, presented. The task force
was established under Act 78 (2023) to plan and implement a reliable, interoperable statewide
public safety communications system. Seven members are divided into working groups:
technology, policy/operations, governance, funding, facilities, regionalization, and cost-sharing.
Preliminary recommendations include statewide CAD (CAD-to-CAD) system integrated with
911 data; RFP to be developed for the statewide CAD system including: statistics/reporting tools,
CAD-RMS integration, recorder standards, fire station alerting, GIS integration, and a
cybersecurity framework. Additionally, Rapid SOS platform expansion (31 licenses available
for non-PSAP dispatch centers), a governance model and preference for an independent board
operating parallel to the 911 Board; includes state officials, municipal reps, and emergency
services associations. $11 million originally appropriated, $1 million spent, $570k currently
authorized. Preliminary cost for proposed new governance board ? $570 k per year.
EMSAC Committee Discussion Highlights:
• Task Force legislative report expected January 2026.
• Clarification that only two full-time state employees (Neal and Deputy Commissioner
Batsie) staff the task force.
• Questions on EMS data integration, interoperability with ImageTrend (EPCR), and
statewide resource visibility within CAD.
• Concern about financial impacts and need for state support for CAD licensing.
• Recommendation to include EMS (SIREN) integration with CAD systems in future
RFPs.
• Discussion on statewide electronic medical dispatch and transition from paper APCO
guidelines.
• Neal committed to relaying EMSAC feedback to the Task Force.
Committee confirmed intent to coordinate its December 2026 EMS system report with the Task
Force’s work to ensure alignment on CAD integration, data sharing, and governance
recommendations.
Meeting Minutes Review & Approval
The minutes from October 15, 2025, were previously distributed to the committee.
• Motion to approve the October 15th and meeting minutes by Marc Hachey, and seconded
by Joe Aldsworth.
• No discussion; motion carried unanimously.
2
November 5, 2025

Vermont Emergency Medical Services
Advisory Committee
Interfacility Transfer (IFT) Coordination & Blueprint for Health (AHS)
Continued discussions led by the Blueprint for Health team addressing hospital-to-hospital
transfers. Main issues are: limited bed availability, long transport times, inadequate
communication between hospitals and EMS, uncompensated non-medical necessity transfers.
Identified need for a statewide hospital bed-availability dashboard and stronger coordination to
keep patients closer to home. Blueprint meetings held at Gifford and NVRH; future sessions
planned for Brattleboro and Bennington. Plan to invite Blueprint team to present findings at a
December or January EMSAC meeting.
Draft EMS System Report
Follows legislative format with an executive summary, system overview, data findings, and
preliminary recommendations.
• Major sections include:
1. Definition and scope of EMS in Vermont
2. Governance and structure
3. Data sources and limitations
4. Statewide service metrics and financial assessment
5. Interfacility transfers
6. Dispatch and data infrastructure
7. Workforce and training challenges
8. Clinical benchmarks (hypoglycemia, stroke assessment, GCS documentation,
lights and sirens use)
9. System strengths, weaknesses, and future challenges
10. Recommendations (for legislative consideration) — in progress.
Members can submit input via an online form; submissions route directly to Julia for
incorporation. The draft will be distributed to all members, and everyone is encouraged to
review past minutes, consulting reports, and 2023 EMS study before submitting comments.
Deadline for feedback: November 19, 2025 (next meeting): the final draft vote planned for
December 2025 meeting.
Data Validation and Reporting Discussion
Concern about non-mandatory fields in SIREN (e.g., lights and sirens use) affecting data
accuracy. Discussion of making key fields mandatory and forming a data validation subgroup.
Chelsea Dubie (VDH) explained the balance between required fields and reporting burden;
changes require careful implementation. Connor Dunn noted technical complexities with state
and national validation standards. Consensus that better education and communication about
“why data matters” are essential before mandating new fields. Agreement on establishing an
EMS data technical advisory group (TAG).
3
November 5, 2025

Vermont Emergency Medical Services
Advisory Committee
Committee Schedule
• November 19 – Williston Fire Department, 645 Talcott Road, Williston, VT 05495
o 1 PM to 3 PM
• December 3 – Alumni Hall, Washington Room, 20 Auditorium Hill, Barre, VT 05641
o 10 to 3 PM
• December 10 – Details to follow
The next EMS Conference is scheduled for March 6-8th. Pat Malone has been in communication
with the event planner to host an EMSAC meeting on Friday March 7th. Additionally, there was
discussion and agreement to hold a panel discussion for conference attendees on the work of the
committee. Pat Malone will coordinate with the event planner; details to follow.
Adjournment
Motion to adjourn unanimously approved.
Meeting adjourned at 3:40 PM
4
November 5, 2025

---

### 2025-10-15 — Vermont Board of Medical Practice — October 15, 2025

**[MINUTES] 2025-10-15_eprip-EMS-advisory-minutes-presentation-10.15.25.pdf**

Governance
• The EMS office provides centralized oversight of the EMS system
• Licensing of Services
• Licensing of Personal
• Investigations
• Data collection
• Training
• Protocol Development
• 13 Districts through statute and rule provide varying levels of local system
oversite
• Organization and structure of these districts is inconsistent
• District medical advisor(s) provides local medical oversite by delegated
authority of the commissioner of health
• EMS Advisory Committee
• Created in statute to advise the commissioner and legislature on EMS
• Tasked to write and maintain a 5 yearplan for EMS

Vermont EMS Assessment
2025

Working Draft Information
*Not for Public Release
We have completed the data collection for ambulance services and to the
best of our ability validated that information prior to today’s presentation.
Over the next several weeks, each service will receive an individual email
with their information for one final opportunity to review and correct any
errors. It is unlikely that the aggregated information will be impacted if
minor corrections are needed.

Data Limitation Disclaimer
• Data is presented using a combination of data collected through self-
reporting surveys, ground ambulance data collection documents,
Vermont EMS data systems, and publicly available information.
Vermont does not have a system in place that collects and stores all
these data points.
• All data points have been verified directly with service leaders to the
best of our ability.
• A small percentage of data has been estimated in cases where detailed
information was not available.
• Each service reporting period is a 1-year period somewhere between
2023-2025 if the service was using the ground ambulance data
collection documents to share information.
• All other data requested was from 2024

Access to data, data assumptions and data
sources
Data used in this assessment was targeted toward calendar year
2024. Due to challenges with accessing a complete data set, many
different methods were used to collect the data. Service level data
may be based on a fiscal year, calendar year or in some cases
blended. Services that supplied their ground ambulance cost
report provided data for their assigned reporting year.

EMS System Data 2024
• Call numbers
• About 100,000 911 calls annually - 6% increase
• 28,000 interfacility transfers
(the definition varies from service to service) - 8% increase
• About 29,500 911 calls did not result in transport

EMS Service information
• Number of First Response Services
• 32 EMT
• 53 AEMT
• 5 paramedic
• Number of Vermont Licensed Ambulance services
• 65 Vermont based ambulance services
• 2 out of state with instate locations
• 7 out of state that are licensed in Vermont
• 15 AEMT
• 47 paramedic
• 14 CCP
• Out of state
• A number that are operating in Vermont without Vermont licenses. (we do not have data on their activity in VT)
• Air medical service data is not included
• Other Unique EMS service consideration
• 2 college based services
• 1 part time ski area service
• 1 transfer only service

System Finance
• Total system cost
• Approximately 98 million
• Total reimbursement from insurance payers
• Approximately 53 million
• Local tax
• Approximately 43 million
• Fundraising
• Approximately 1.2 million
• Volunteer labor contribution
• 9.7 million
• Provider Tax Paid
• Approximately 1.4 million

Suspected
Treatment Stroke
Administered Receiving
for Prehospital
Hypoglycemia Stroke
System Assessment
Performance
Documentation No use of Lights
of GCS, SBP, and Sirens
and Respiratory During
Rate Transport

Statewide

Statewide

| District 1 | District 4 | District 7 |
| ---------- | ---------- | ---------- |
| District 2 | District 5 | District 8 |
|            | District 6 | District 9 |
District 3

District 10
District 12
Northeast 32%
Vermont 35%
District 11 District 13

| District 1 | District 4 | District 7 |
| ---------- | ---------- | ---------- |
District 2
|            | District 5 | District 8 |
| ---------- | ---------- | ---------- |
| District 3 | District 6 | District 9 |

| District 10 | District 12 | Northeast         69% |
| ----------- | ----------- | --------------------- |
Vermont            64%
| District 11 | District 13 |     |
| ----------- | ----------- | --- |

District 1
District 4 District 7
District 5
District 2 District 8
District 9
District 3
District 6

District 10 District 12
Northeast 66%
Vermont 64%
District 13
District 11

| District 1 | District 4 | District 7 |
| ---------- | ---------- | ---------- |
District 2
District 5
District 8
| District 3 | District 6 | District 9 |
| ---------- | ---------- | ---------- |

District 10 District 12
Northeast 30%
Vermont 37%
District 13
District 11

Education and Work Force Development
• Number of providers
• location
• License level
• location
• Education Location
• access
• success

Workforce and Location

EMS Instructor Population 2023 - 2024
Who Is
Instructor/Coordinators
59
Teaching
Full-Time Educators
7
• Note: Number of
Senior Instructors
Instructor Coordinators 12
and Senior Instructors
(both full and part time
educators) from 2023-
2024
Part-Time Educators
5

VEFR & EMR Courses Per District 2023-2024
*EMR courses all occurred in 2023*
16
14
12
10
8
6
4
2
0
|      | D1  | D2  | D3  | D4  | D5  | D6  | D7  | D8  | D9  | D10 | D11 | D12 | D13 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EMR  | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 0   | 1   | 0   | 0   | 0   | 1   |
| 2024 | 0   | 2   | 3   | 1   | 3   | 3   | 3   | 5   | 0   | 4   | 3   | 5   | 7   |
| 2023 | 3   | 3   | 1   | 2   | 2   | 4   | 1   | 1   | 4   | 3   | 2   | 10  | 5   |

EMT Course Instruction
62 EMT Courses Total from 2023-2024
Instructor/Coor
dinator (23
Senior
Instructor
(39 Classes)
63%

AEMT Courses Per District 2023-2024
7
6
5
4
3
AEMT Course Instruction 2
18 Courses Total from 2023-2024
1
Instructor/Coordinat
or (4)
22%
0
D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13
2024 0 1 3 1 1 0 0 0 1 0 0 1 1
2023 1 1 3 0 0 0 0 0 1 0 0 0 3
Senior
Instructor (14)
78%

Progression of AEMT Students in 2023-2024
# of students enrolled 290
NREMT Cert 236
VT licensed 148
• *DISCLAIMER* - some students enrolled in EMT classes
prior to the 23-24 window completed only the NREMT & VT
License steps during the 23-24 period. Also, some EMT
students enrolled in 23-24 classes are still in the current
testing cycle.

Courses Offered By District 23-24
40
35
30
25
20
15
10
5
0
D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13
VEFR EMR EMT AEMT NRP

Transfer Activity
• 28k transfers statewide
• 19k transfers between hospitals
• 10k to nursing homes, rehab or other destinations
• 12k transfers being sent from Vermont hospitals to other hospitals
(DHMC is included)
• 25% leave Vermont
* Data from 2024 siren reporting provided to Cambridge Consulting

Transfer Data
71% of hospital to hospital transfers are
completed by 6 services
• Lamoille
• Rescue Inc
• Regional
• Barre Town
• Newport
• Amcare

Hospital to Hospital
•
83% BLS stable
•
14% potentially
unstable
• 1% unstable
• 2% critical care
• 72 separate receiving
hospitals
Trauma Center
Inbound Transfers
|     | Albany  | 479  |
| --- | ------- | ---- |
|     | DHMC    | 2582 |
|     | UVM     | 4521 |

When do hospital transfers happen?
11% 0000-0600
26% 0600-1200
44% 1200-1800
19% 1800-0000

Data calculation method
• Cost
• Staffing
• First response was not specifically included due to lack of data
• In some cases, data was received indirectly from services and IS
NOT verifiable.
• Partial towns were not assigned

• Formula to calculate expenses for services with mixed
business lines
• Total volume divided by ground ambulance volume
• Staffing formula
• 1 crew for every 1200 calls
• 9 FTE/crew or 18pt or a combination
Assumptions • Only using the fulltime staffing numbers provided
• Tax Contributions were calculated for governmental services
as the difference between net patient revenue and the
calculated EMS expense line
• For services that contract with a municipality, the contract
rate was used if not provided.
• Regional services serve 4 or more towns
• Partial towns were not assigned

The committee decided to look at the system
data in different ways
Size of the
• 0-500 calls
• 500-1200 calls
service
• 1200+ calls
• Municipal Fire based
Structure • Municipal
• Regional (5+ towns covered)
• Local (less than 4 towns covered)

0 to 500
emergency calls
• 5 services
• Covering 14 towns
• About 400 sq miles
• Population of 18K
• Average cost per call of
$793
• Average per capita $75

500-1200
emergency calls
• 17 services
• Covering 56 towns
• About 1900 sq miles
• Population of 110,000
people
• Average cost per call of
$641
• Average per capita $28

1200+
• 34 services
• Covering 156 towns
• About 5400 sq miles
• Population of 470,000
• Average cost per call of
$756
• Average per capita $55

Municipal Fire Based
EMS Ambulance
• Most reported their data by
providing their Medicare Ground
Ambulance Data Collection
documents.
• Town Budget information and US
census data was used in
calculations.
• Cost information is displayed
using simple percentage of call
volume calculation. The same
calculation was used for all
services that provide services in
addition to ground ambulance
service.

Fire Based
Ambulance Services
• 10 Licensed Services operating 31
ambulances
• 100% licensed at the Paramedic level
• Provide 911 service to 18 towns in
Vermont
• Covering 204 sq miles, about 2% of the
state
• Provide 911 service to 121,000
residents, 19% of Vermont's
population

Fire Based
Ambulance

Non-Emergency
Transports
• 2 Fire Departments provide IFT
services with each reporting that
20% of their call volume is IFT
• Fire based IFT provides 3% of the
states IFT services

Fire department
Expense/Revenue
• A combined $34.8 million operating budget
for EMS
• Local taxes provide $25.5 million to support
ambulance operations. Average per capita
cost of $189 with a range from $12 to $285
• Net patient receivables of $8.7 million or 14%
of the total state-wide reimbursement
• Average reimbursement per transport is $476
• Average cost per 911 call is $1168 with a
range from $735 to $1141
• 100% FT coverage

Municipal
Ambulance
Services
• 11 Licensed Services operating 27
ambulances
• 3 Critical Care
• 91% licensed at the Paramedic level
• Provide 911 service to 25 towns in
Vermont
• Covering 955 sq miles, about 11% of the
state
• Provide 911 service to 80k residents,
12% of Vermont's population

Municipal
Ambulance
• Respond to 14,000 911
EMS calls a year
• Transport 10,500 911
patients a year
• 24% of 911 calls do not
result in transport
• Average reported
response time to critical
incidents of 11 minutes

Non-Emergency
Transports
• 2 services provide IFT services
with one reporting that 37% of
their call volume is IFT
• Municipal services provide 11% of
the states IFT services

Municipal
Cost
• 10.9 million in annual cost
• 6.4 million in reimbursement
• Average Cost per call $801
• Cost range is from $6 - $163 Per
capita
• Average Per capita rate $57
• Average reimbursement per
transport is $476
• 2 provide subscription services
• 43% FT coverage

Regional Ambulance
Services
• 19 Licensed Services operating 77
ambulances
• 79% licensed at the Paramedic level
• 6 Critical Care Services
• Provide 911 service to146 towns in
Vermont
• Covering about 4800 sq miles, about
52% of the state
• Provide 911 service to 260,000
residents, 40% of Vermont's
population

Regional
• Respond to 43,500 911
EMS calls a year
• Transport 35,000 911
patients a year
• 20% of 911 calls do not
result in transport
• Average reported
response time to critical
incidents of 9.5 minutes

Non-Emergency
Transports
• 14 provide IFT services with each
reporting up to 37% of their call
volume is IFT
• Regional services provides 47% of
the states IFT services

Regional
Cost
• Total cost of 32 million
• Reimbursement of 22 million
• $665 average reimbursement per
call
• Cost range from $4

*[document truncated for length]*

---

**[MINUTES] 2025-10-15_eprip-EMS-advisory-minutes-10.15.25.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: October 15, 2025
Location: Regional Ambulance, Rutland (VT), & Microsoft Teams
Meeting Called to Order: 1:06 PM by Drew Hazelton

Rollcall – Committee Members

|              | Representative    |     | Attendance  |     | Representative   |                |     | Attendance  |
| ------------ | ----------------- | --- | ----------- | --- | ---------------- | -------------- | --- | ----------- |
| District 1   |                   |     |             |     | District 2       |                |     |             |
|              | Kathy Jochim      |     |             |     | Adam Heuslein    |                |     | Present     |
|              |                   |     |             |     | Samantha Atwood  |                |     |             |
| District 3   |                   |     |             |     | District 4       |                |     |             |
|              | Leslie Lindquist  |     |             |     | Scott Brinkman   |                |     |             |
|              | Becky Alemy       |     | Present     |     |                  | Jeff Johansen  |     | Present     |
| District 5   |                   |     |             |     | District 6       |                |     |             |
|              |                   |     |             |     |                  | Joe Aldsworth  |     | Present     |
|              |                   |     |             |     | David Danforth   |                |     | Present     |
| District 7   |                   |     |             |     | District 8       |                |     |             |
|              | Charlene Phelps   |     |             |     |                  | Matt Parrish   |     | Present     |
|              | Kate Rothwell     |     | Present     |     |                  | Charles Piso   |     | Present     |
| District 9   |                   |     |             |     | District 10      |                |     |             |
|              | Alan Beebe        |     |             |     | Michael Tarbell  |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| District 11  |                   |     |             |     | District 12      |                |     |             |
|              |                   |     |             |     |                  | Bill Camarda   |     | Present     |
|              |                   |     |             |     | Bobby Maynard    |                |     |             |
| District 13  |                   |     |             |     | VAA              |                |     |             |
|              | Eric Wilson       |     | Present     |     | Drew Hazelton    |                |     | Present     |
|              |                   |     |             |     |                  |                |     |             |
| IREMS        |                   |     |             |     | PFFV             |                |     |             |
|              | Pat Malone        |     | Present     |     |                  | Mark Hachey    |     | Present     |
|              | Chris LaMonda     |     |             |     |                  | Billy Fritz    |     | Present     |
| VCFC         |                   |     |             |     | VSFA             |                |     |             |
|              | Aaron Collette    |     | Present     |     |                  |                |     |             |
|              | Michael Randzio   |     | Present     |     |                  |                |     |             |
| VAHHS        |                   |     |             |     | VLCT             |                |     |             |
|              |                   |     |             |     |                  | Lee Krohn      |     |             |
|              |                   |     |             |     |                  |                |     |             |
| VDH          |                   |     |             |     |                  |                |     |             |
|              | Will Moran        |     | Present     |     |                  |                |     |             |
|              | Chelsea Dubie     |     | Present     |     |                  |                |     |             |

1
October 15, 2025

Vermont Emergency Medical Services
Advisory Committee
Non-members in attendance: Courtney Newman, Dan Wolfson, Connor Dunn, Ray Walker, Jay
Symonds, Maggie Burke, Zach Rounds, Jack Foster, Marsha McCombie, Avery Mosenthal,
Nicholas Hoff, Kara Wentzel, Leighton Laughlin, Joha Anderson-Foyner, Ava Kulikowski,
Victoria Lashbrook, Lucy Graber, Ella Sarama, Will Olshea, Max Romen-Blant, Gabe Sutton,
Jack Foster, Julia Sugg
Meeting Minutes Review & Approval
The minutes from August 20, 2025, and September 3, 2025, were previously distributed to the
committee.
• Motion to approve the August 20th and September 3 meeting minutes by Will Moran
• Seconded by Michael Tarbell
• No discussion; motion carried unanimously.
Advanced EMT Student Minimum Competencies
Courtney Newman presented an update on the AEMT Student Minimum Competencies (SMCs),
highlighting the shift away from psychomotor exams to competency-based evaluations. Vermont
adopted these standards in January 2024. Key proposed revisions include: updates to the skills
table, use of simulation for summative assessment, and a standardized statewide AEMT
portfolio.
Discussion: Members requested a summary of the proposed changes and recommended review
by the Education Subcommittee.
Action Items: Courtney to share revision summary; Education Subcommittee to review before
November 2025 meeting.
Interfacility Transfer (IFT) Coordination & Blueprint for Health (AHS)
David Danforth summarized findings from recent meetings with the Agency of Human Services.
Hospitals reported challenges moving patients within their networks, while EMS is often left out
of the communication process. Key proposals included improved hospital–EMS communication,
real-time dashboards, and potential CAD integration.
Concerns: Less than 50% of IFTs meet CMS medical necessity standards; hospitals typically
bear the cost. Members emphasized the need for coordination to prevent system strain.
Action Items: Continue representation at future AHS meetings (Danforth and Hazelton). Explore
integration of statewide data integration systems.
EMS Governance Subcommittee Report
Presented by David Danforth and Charles Piso. The subcommittee proposed a three-region EMS
governance model to improve equity, oversight, and consistency statewide.
Highlights: Three regions (Northwest, Northeast, Southern); Nine-member State EMS Board; 3-
member medical director board; standardized protocols; regional QA/QI and education
oversight; estimated annual cost $2.6M.
2
October 15, 2025

Vermont Emergency Medical Services
Advisory Committee
Discussion: Members requested more time for review and suggested alternative regional
alignment models. The proposal will be circulated for review, please provide feedback via QR
code and written comments. Refer to the proposal document for greater detail.
• Motion for the EMS Governance Subcommittee to submit a written report to the
members of the EMSAC with the opportunity to solicit feedback, and to revisit the
proposal at the December meeting by Pat Malone
• Second by Aaron Collette
• Friendly amendment – Would like to hear what other options exist regarding regional
alignment by Joe Aldsworth
• Friendly amendment accepted and the motion carried
Action Items: Subcommittee to distribute written report within a week; comments may be
submitted by the QR code; full discussion to occur at December 2025 meeting.
The statewide EMS system assessment is due to the legislature by December 15, 2025. The
Recommendations for a statewide EMS system report is due to the legislature by December 15,
2026.
Statewide EMS System Assessment and Data Report
Data was collected from multiple fiscal years (2023 and 2024) and obtained from SIREN,
municipal budgets, directly from agencies, and tax reports.
Highlights: Statewide data analysis presented: ~100,901 total calls, including 28,000 interfacility
transfers. Estimated annual system cost: $100M; reimbursement $53M; public funding $43M;
volunteer labor has an estimated value of $9.7M. Refer to the presentation slides for greater
detail.
At the request of the committee, EMS Data Manager Connor Dunn compiled two data sets, both
including the following four NEMSQA performance metrics. The first compared statewide data
to the national average, the second compared each EMS district to the national average.
3
October 15, 2025

Vermont Emergency Medical Services
Advisory Committee

|                    |                       | State        | National  |                        |
| ------------------ | --------------------- | ------------ | --------- | ---------------------- |
| Category           | Metric                |              |           | Notes                  |
|                    |                       | Performance  | Average   |                        |
| Hypoglycemia       | Proper documentation  |              |           | Consistent with        |
|                    |                       | 35%          | 35–38%    |                        |
| Treatment          | and treatment         |              |           | national mean          |
| Lights & Sirens    | Safety compliance     |              |           | Slightly below         |
|                    |                       | 37%          | 42%       |                        |
| Use                | during transport      |              |           | average                |
|                    | Proper FAST-ED        |              |           | Drop attributed to     |
| Stroke Assessment  |                       | 64%          | 70%       |                        |
|                    | documentation         |              |           | reporting tool change  |
| Trauma             | GCS, BP, RR           |              |           | Stable but room for    |
|                    |                       | 60–64%       | ~65%      |                        |
| Documentation      | recorded              |              |           | improvement            |

Performance metrics indicated consistency across service types but significant geographic
variability. Recommendations included making key data fields mandatory in SIREN and
expanding QA/QI processes.  Refer to the PowerPoint presentation for more details.

•  Motion to except the EMS service level data report as presented, including the
assumptions and methodology, by Pat Malone
•  Second by Michael Tarbell
•  No discussion, the motion carried without objection

Committee Schedule
•  November 5 – Waterbury State Office Complex, Department of Health, Waterbury
10 AM to 12 PM
o
•  November 19 – Williston Fire Department, 645 Talcott Road, Williston, VT 05495
o  1 PM to 3 PM
Adjournment
| Motion to adjourn unanimously approved.  |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- |
Meeting adjourned at 3:40 PM

4
October 15, 2025

---

### 2025-09-17 — Vermont Board of Medical Practice — September 17, 2025

**[MINUTES] 2025-09-17_eprip-EMS-advisory-minutes-9.17.25.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: September 17, 2025
Location: Waterbury State Office Complex, Waterbury (VT), & Microsoft Teams
Meeting Called to Order: 1:03 PM by Drew Hazelton

Rollcall – Committee Members

|             | Representative    |               | Attendance  |          |               | Representative   |                | Attendance  |          |
| ----------- | ----------------- | ------------- | ----------- | -------- | ------------- | ---------------- | -------------- | ----------- | -------- |
| District 1  |                   |               |             |          |   District 2  |                  |                |             |          |
|             |                   | Kathy Jochim  |             |          |               | Adam Heuslein    |                |             | Present  |
|             |                   |               |             |          |               | Samantha Atwood  |                |             |          |
| District 3  |                   |               |             |          |   District 4  |                  |                |             |          |
|             | Leslie Lindquist  |               |             | Present  |               | Scott Brinkman   |                |             |          |
|             |                   | Becky Alemy   |             |          |               |                  | Jeff Johansen  |             |          |
| District 5  |                   |               |             |          |   District 6  |                  |                |             |          |
|             |                   |               |             |          |               |                  | Joe Aldsworth  |             |          |
|             |                   |               |             |          |               | David Danforth   |                |             | Present  |
| District 7  |                   |               |             |          |   District 8  |                  |                |             |          |
Present
|              | Charlene Phelps  |                |     |     |                |                  | Matt Parrish  |     |          |
| ------------ | ---------------- | -------------- | --- | --- | -------------- | ---------------- | ------------- | --- | -------- |
|              |                  | Kate Rothwell  |     |     |                |                  | Charles Piso  |     | Present  |
| District 9   |                  |                |     |     |   District 10  |                  |               |     |          |
|              |                  | Alan Beebe     |     |     |                | Michael Tarbell  |               |     | Present  |
|              |                  |                |     |     |                |                  |               |     |          |
| District 11  |                  |                |     |     |   District 12  |                  |               |     |          |
|              |                  |                |     |     |                |                  | Bill Camarda  |     | Present  |
Present
|              |                  |                 |     |          |         | Bobby Maynard  |              |     |          |
| ------------ | ---------------- | --------------- | --- | -------- | ------- | -------------- | ------------ | --- | -------- |
| District 13  |                  |                 |     |          |   VAA   |                |              |     |          |
|              |                  | Eric Wilson     |     | Present  |         | Drew Hazelton  |              |     | Present  |
|              |                  |                 |     |          |         |                |              |     |          |
| IREMS        |                  |                 |     |          |   PFFV  |                |              |     |          |
|              |                  | Pat Malone      |     | Present  |         |                | Mark Hachey  |     |          |
|              |                  | Chris LaMonda   |     |          |         |                | Billy Fritz  |     | Present  |
| VCFC         |                  |                 |     |          |   VSFA  |                |              |     |          |
|              |                  | Aaron Collette  |     | Present  |         |                |              |     |          |
|              | Michael Randzio  |                 |     | Present  |         |                |              |     |          |
| VAHHS        |                  |                 |     |          |   VLCT  |                |              |     |          |
|              |                  |                 |     |          |         |                | Lee Krohn    |     |          |
|              |                  |                 |     |          |         |                |              |     |          |
| VDH          |                  |                 |     |          |         |                |              |     |          |
Present
|     |     | Will Moran     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Chelsea Dubie  |     |     |     |     |     |     |     |

Non-members in attendance: Courtney Newman, Dan Wolfson, Connor Dunn, Jim Finger, Jay
Symonds, Donna Jacob
Approval of the August 20 and September 3, 2025, Meeting Minutes
The minutes from August 20, 2025, and September 3, 2025, were previously distributed to the
committee.
• Motion to approve the August 20th and September 3 meeting minutes by Adam Heuslein
• Seconded by Aaron Collette
• No discussion; motion carried unanimously.
Approval of the Fiscal Sponsor Financial Report
• The EMSAC’s fiscal sponsor, Rescue Inc., presented an accounting of expenses incurred
by the committee to date (attached to this report).
• Motion to approve the financial report made, seconded, and approved unanimously.
UVM Interns
Four interns secured, each receiving 3 academic credits:
1. Jonas (UBM Rescue student; EMS major) – drafting continuing education requirements
using National Registry as baseline.
2. Jack (EMT, Geography minor) – creating GIS heat maps of EMS course locations,
analyzing travel time/distance to courses.
3. Gabe (EMS minor, Fairfax Rescue) – transforming raw statistics into visual
diagrams/graphs.
4. Carly (EMS minor) – analyzing instructor success rate data.
• Pat Malone noted interns were “motivated and already producing results.” Plan to invite
interns to present at the next meeting.
Governance & System Structure Discussion
Committee members were asked to reflect upon the conceptual EMS governance structure
presented at the last meeting. Members shared the following:
• Emphasized need for more education on governance models (e.g., DMA model). The
Career Fire Chiefs Association are not opposed but require further study before
supporting.
• Supported moving forward but raised concerns about regional equity (fear rural regions
could be neglected under a 3-region model). Suggested exploring UK-style funding
(charity-supported EMS).

• Echoed support; highlighted District 3’s barriers to federal funding. Stressed importance
of reducing administrative hurdles.
• Members highlighted the unsustainable reliance on volunteer district and committee
administrators. Currently, EMS organizations are subsidizing the Committee by allowing
staff to attend these meetings without compensation.
• Noted examples from other councils (e.g. Fire Service Training Council, Criminal Justice
Council, USAR), where part-time staff or stipend positions exist to support council work.
• Consensus the EMS council recommendations must include dedicated staff positions (e.g.
data analyst, council coordinators, state EMS Office liaison). The Committee has a
responsibility to include staffing resources in our report.
• Any recommendations must be backed by realistic funding requests.
• A Governance sub-group was formed and includes Leslie Lindquist, Charles Piso, David
Danforth, Drew Hazelton, Dan Wolfson, Mark Hachey and Will Moran.
Finance Data Presentation – By Drew Hazelton
The data set presented as an example for the committee is for the fire-based EMS cohort. The
fire-based cohort was the most complete data set; thanks was expressed for the fire service
leaders for submitting their data.
• Preliminary results for fire-based EMS group
o 11 licensed services, 31 ambulances
o ~28,000 EMS calls, 22,900 transports
o Total spent: $34.8 million; $25 million from tax dollars
o Average per capita cost is $191 (range $27 - $265)
o Patient receivables: $8.7 million (14% of total receivables across the EMS
system)
o Average reimbursement: $465 per transport
o Average cost per call: $1,100
• Data limitations
o Missing data for some agencies (Hanover Fire Dept., NH, and Brattleboro Fire
Dept.)
o Inconsistent reporting periods (some based on fiscal year, some on Medicaid Cost
Data Reporting period); while different periods of time, the years are adjacent to
one another
o Staffing data unreliable; reported as license level, not staffing patterns
• Next steps
o NEMSIS Epi team running performance measures analysis for 2024; results
expected in early October
o Data to be divided by delivery model (fire based, third service, municipal) and
annual call volume (<500, 500-1,200, >1,200 EMS calls/year)
o Every agency chief/director will be asked to review and validate their data before
final submission to the legislature.
• Note
o Consensus not to report out-of-service days by cohort to prevent political or labor
disputes. Alternatively, will report system wide total.

o Acknowledgement that EMS loses ~$700 per transport on average; highlights
financial instability of current model
Drafting the Assessment
The committee discussed the report and the need to agree upon recommendations. It was agreed
that any recommendation included in the report would require the approval of 75% of the
committee members present at a meeting. Dissenting opinions may be submitted in writing by
committee members and will be included in the report. The committee set a goal of settling on
clear and evidence-based conclusions.
Committee Schedule
• October 1 – Middlebury Regional EMS, Middlebury – 10 AM to 2 PM
• October 15 – Regional Ambulance Service, Rutland – 1 PM to 4 PM
• November 5 – Waterbury State Office Complex, Department of Health, Waterbury – 1
PM to 3 PM
Adjournment
Motion to adjourn unanimously approved.
Meeting adjourned at 2:40 PM

---

### 2025-09-03 — Vermont Board of Medical Practice — September 03, 2025

**[MINUTES] 2025-09-03_eprip-EMS-Governance-and%20-Organization-Presentation-%209.3.25.pdf**

EMS System Governance
and Organization
A conceptual plan under development by
the EMS Advisory Committee

Vermont Department of Health

1

Recommendations for a Statewide EMS System

Objective

A statewide EMS system that provides safe, effective, and accountable
systems of care and specialized transportation.

Goals

1. A patient centered EMS system
2. An integrated, multi-layered structure
3. Evolve and strengthen the public private partnership between the state

and local officials

Vermont Department of Health

2

Remove Boarders to Create a Statewide EMS System

Today
13
Independent
EMS Districts

Future
One statewide
EMS system

Vermont Department of Health

3

A Public Private Partnership

Department of
Health

Regional EMS
Officials

Statewide EMS
Council

Vermont Department of Health

4

Statewide EMS Council
The Statewide EMS Council Core Tenets

Collaboration

Communication

Coordination

Planning

Quality

Vermont Department of Health

5

Statewide Council with Regional Representation

The statewide EMS Council is
comprised of regional
representatives, EMS
leaders, state regulators,
EMS clinicians, physicians
and nurses, and the
community.

Regions are the primary sub-
unit of the council.

Regional makeup mirrors
that of EMS districts.

Northwest
Region

Northeast
Region

Southern
Region

Roles & Responsibilities

Department of Health

Statewide EMS Council

Inspections
Investigations

• Licensing
•
•
• Training & education
• Data collection and analysis
• Medical direction
• Specialty programs
• Quality assurance and quality

improvement

• Support & coordination
• Technical advisory groups
• Research

• Regional & statewide structure
• Communications
• MCI & medical surge
• Coordinated systems of care
• Human resources
• Workforce development
• Finance
• Physicians
• Quality improvement
• Public relations

Vermont Department of Health

7

Roles and Responsibilities - A New Vision

Department of Health

Statewide EMS Council

Inspections
Investigations

• Licensing
•
•
• Training & education
• Data collection and analysis
• Medical direction
• Specialty programs
• Quality assurance and quality

improvement

• Support & coordination
• Technical advisory groups
• Research

• Regional & statewide structure
• Communications
• MCI & medical surge
• Coordinated systems of care
• Human resources
• Workforce development
• Finance
• Physician oversight
• Quality improvement
• Public relations

Vermont Department of Health

8

Vermont EMS System

EMS Plan

Department of
Health

Statewide EMS Council

Region

Region

Region

Vermont Department of Health

9

Strength-Based Relationship

All Vermonters benefit from an EMS
systems that provides for enhanced
collaboration and communication,
strategic and operational
coordination, and expanded
opportunities and growth.

Vermont Department of Health

10

---

**[MINUTES] 2025-09-03_eprip-ems-advisory-committee-minutes-9.3.25.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: September 3, 2025
Location: White River Valley Ambulance, Bethal (VT), & Microsoft Teams
Meeting Called to Order: 10:00 AM by Drew Hazelton

Rollcall – Committee Members

|             | Representative    |               | Attendance  |          |               | Representative   |                | Attendance  |          |
| ----------- | ----------------- | ------------- | ----------- | -------- | ------------- | ---------------- | -------------- | ----------- | -------- |
| District 1  |                   |               |             |          |   District 2  |                  |                |             |          |
|             |                   | Kathy Jochim  |             |          |               | Adam Heuslein    |                |             | Present  |
|             |                   |               |             |          |               | Samantha Atwood  |                |             |          |
| District 3  |                   |               |             |          |   District 4  |                  |                |             |          |
|             | Leslie Lindquist  |               |             | Present  |               | Scott Brinkman   |                |             |          |
|             |                   | Becky Alemy   |             | Present  |               |                  | Jeff Johansen  |             |          |
| District 5  |                   |               |             |          |   District 6  |                  |                |             |          |
|             |                   |               |             |          |               |                  | Joe Aldsworth  |             | Present  |
|             |                   |               |             |          |               | David Danforth   |                |             | Present  |
| District 7  |                   |               |             |          |   District 8  |                  |                |             |          |
Present
|              | Charlene Phelps  |                 |     |          |                |                  | Matt Parrish  |     |          |
| ------------ | ---------------- | --------------- | --- | -------- | -------------- | ---------------- | ------------- | --- | -------- |
|              |                  | Kate Rothwell   |     | Present  |                |                  | Charles Piso  |     | Present  |
| District 9   |                  |                 |     |          |   District 10  |                  |               |     |          |
|              |                  | Alan Beebe      |     |          |                | Michael Tarbell  |               |     | Present  |
|              |                  |                 |     |          |                |                  |               |     |          |
| District 11  |                  |                 |     |          |   District 12  |                  |               |     |          |
|              |                  |                 |     |          |                |                  | Bill Camarda  |     | Present  |
|              |                  |                 |     |          |                | Bobby Maynard    |               |     |          |
| District 13  |                  |                 |     |          |   VAA          |                  |               |     |          |
|              |                  | Eric Wilson     |     | Present  |                | Drew Hazelton    |               |     | Present  |
|              |                  |                 |     |          |                |                  |               |     |          |
| IREMS        |                  |                 |     |          |   PFFV         |                  |               |     |          |
|              |                  | Pat Malone      |     | Present  |                |                  | Mark Hachey   |     | Present  |
|              |                  | Chris LaMonda   |     |          |                |                  | Billy Fritz   |     |          |
| VCFC         |                  |                 |     |          |   VSFA         |                  |               |     |          |
|              |                  | Aaron Collette  |     | Present  |                |                  |               |     |          |
|              | Michael Randzio  |                 |     | Present  |                |                  |               |     |          |
| VAHHS        |                  |                 |     |          |   VLCT         |                  |               |     |          |
|              |                  |                 |     |          |                |                  | Lee Krohn     |     | Present  |
|              |                  |                 |     |          |                |                  |               |     |          |
| VDH          |                  |                 |     |          |                |                  |               |     |          |
Present
|     |     | Will Moran     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Chelsea Dubie  |     |     |     |     |     |     |     |

Non-members in attendance: Courtney Newman, Ray Walker, Dan Wolfson, Donna Jacob,
Olivia Coe, Helen Reid, Dan Berkman
Governance & System Structure - Presentation by Drew Hazelton
Current State
• The concept presented today represents the past discussions and work done by the
committee on this topic.
• Vermont EMS currently operates as 13 independent districts, nearly all functioning as
“silos.”
o This has resulted in inconsistent district performance, lack of a statewide MCI
plan (a major vulnerability). Additionally, inequitable access to funding, training,
and education, and no cohesive statewide data strategy.
Conceptual Governance & Organization Model
• Objective – A statewide EMS system that provides safe, effective, and accountable
systems of care and specialized transportation.
• Goals include, 1. A patient centered EMS system; 2. An integrated, multi-layered
structure; 3. Evolve and strengthen the public-private partnership between the state and
local officials.
• Clear and defined roles and responsibilities for the state EMS office, and the statewide
EMS council. The role of the state EMS office remains relatively unchanged.
• Core tenets of the statewide EMS council include collaboration, communication,
coordination, planning, and quality.
• Replace EMS districts with a Statewide EMS Council.
• The role of the council, and the regions, is to provide structure and coordination in the
areas of communications, MCI and medical surge response, workforce development,
system finance, coordinated physician oversight, quality improvement, as well as public
and government relations.
• Regions are organizational sub-units of the council; together they are a single
organization.
• One option is to create 3 regions (Northwest, Northeast, and South), which come together
into the Statewide EMS Council. The number of regions is up for discussion.
• Responsibilities:
o Develop & maintain and implement the 5-year EMS system plan.
o Establish permanent committees (e.g. interfacility transport, mobile integrated
health, education, MCI planning).
o Coordinate data and system evaluation.
• State funding would flow to the Council first, then redistributed to regions/agencies,
ensuring equity and accountability.
• All Vermonters benefit from an EMS system that provides for enhanced collaboration
and communication, strategic and operational coordination, systems of care, and growth
opportunities.

Discussion
• Council size: too many voices could bog down decisions. One proposal suggested 9
members (3 per region).
• Could the council manage funds if structured like the Fire Service Training Council?
Further legal analysis needed.
• 13 independent and disconnected EMS districts are having an adverse impact on our
statewide system; consolidation is necessary.
• Act 157 explicitly tasked EMSAC with designing a statewide system, not maintaining a
fractured and siloed structure.
Consensus: Broad support for moving toward a statewide council with regional representation.
Details (legal structure, staffing, funding authority) to be developed.
Medical Direction
Issues Identified
• DMAs often limited to ~2 hours/month; not enough for oversight.
• Hospitals facing financial pressures, pulling back from EMS commitments.
• Unequal quality of medical oversight statewide.
Options Discussed
• Contractual Medical Resource Hospital model (like NH).
• Create regional DMAs (3–4 statewide).
• Hybrid: Regional oversight plus agency-level directors for larger services.
Concerns
• Risk of “DMA shopping” if agencies can switch hospitals for convenience.
• Vermont must ensure both regional consistency and service-level accountability.
Education & Workforce – Presentation Pat Malone
Exam Pass Rates
• EMT: Vermont (74.76%) vs. national (74.45%).
• AEMT: Vermont (~82%) vs. national (66%).
• Paramedic: Vermont (86.5%) vs. national (76%).
Comment: Members were encouraged by these strong comparative results but noted that the
absolute licensure rate from course entry to completion remains troubling.
Course Completion & Licensure

• Over a 2-year period:
o 66 EMT courses approved, with 959 students enrolled.
o 714 entered testing; only 307 became licensed (~32%).
• The number of students enrolled in EMS courses is low suggesting that EMT classes
could be more efficient with more students enrolled in fewer courses.
• AEMT completion stronger (62.7%), but with smaller class sizes.
• Some courses reported single-digit success rates, raising concerns about instructor
effectiveness, student preparedness, or course structure.
Instructor Performance Variability
• Some instructors achieved 100% pass rates, while others fell as low as 62%.
• Malone emphasized the need to investigate why certain instructors succeed and whether
resource levels, experience, or teaching approach play a role.
Class Sizes & Resources
• Small classes (9:1 ratio) correlated with better results but at high cost per student.
• Members questioned whether Vermont offers too many EMT classes for its size, diluting
resources and outcomes.
Funding & Commitment
• Several members questioned whether grant-funded “free” classes reduced student
commitment.
• Malone suggested a deeper dive into completion differences between self-funded vs.
state-funded classes.
Higher Education Partnerships
• Malone met with Community College of Vermont (CCV) and Vermont State University
(VSU) workforce leaders.
• Both are interested in collaboration but require instructors with Master’s degrees
(Bachelor’s possible with waiver).
• Opportunities:
o Use CCV’s widespread locations (95% of Vermont residents reside within 12
miles of a CCV facility).
o Develop certificate programs or co-branded workforce initiatives.
• Barrier: Many current EMS instructors lack required academic credentials to teach a
CCV course.
System Health & Mutal Aid
Out-of-Service Days
• Agencies’ reports ranged from 0 to 53 days/year fully out of service.

• Likely undercounted for volunteer agencies that do not maintain a schedule and therefore
do not know whether they are available until a call is dispatched.
Mutual Aid
• Some agencies report responding mutual aid to neighboring communities is as much as
20–25% of their total call volume.
Reliability Debate
• Some members suggested defining a minimum call volume threshold (~1,200 – 1,400
calls/year) for sustainability.
• Others argued rural towns cannot meet such thresholds, raising questions of equity.
Consensus: System reliability must be framed as a regional issue (not individual agency) in the
legislative report.
Financial & System Sustainabilit

*[document truncated for length]*

---

### 2025-08-20 — Vermont Board of Medical Practice — August 20, 2025

**[MINUTES] 2025-08-20_eprip-ems-advisory-committee-minutes-8.20.25.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: August 20, 2025
Location: Chester Fire Department, Chester (VT), & Microsoft Teams
Meeting Called to Order: 10:03 AM by Pat Malone

Rollcall – Committee Members

|             | Representative    |               | Attendance  |          |               | Representative   |                | Attendance  |          |
| ----------- | ----------------- | ------------- | ----------- | -------- | ------------- | ---------------- | -------------- | ----------- | -------- |
| District 1  |                   |               |             |          |   District 2  |                  |                |             |          |
|             |                   | Kathy Jochim  |             | Present  |               | Adam Heuslein    |                |             | Present  |
|             |                   |               |             |          |               | Samantha Atwood  |                |             |          |
| District 3  |                   |               |             |          |   District 4  |                  |                |             |          |
|             | Leslie Lindquist  |               |             | Present  |               | Scott Brinkman   |                |             |          |
|             |                   | Becky Alemy   |             |          |               |                  | Jeff Johansen  |             |          |
| District 5  |                   |               |             |          |   District 6  |                  |                |             |          |
|             |                   |               |             |          |               |                  | Joe Aldsworth  |             |          |
|             |                   |               |             |          |               | David Danforth   |                |             | Present  |
| District 7  |                   |               |             |          |   District 8  |                  |                |             |          |
Present
|              | Charlene Phelps  |                |     |          |                |                  | Matt Parrish  |     |          |
| ------------ | ---------------- | -------------- | --- | -------- | -------------- | ---------------- | ------------- | --- | -------- |
|              |                  | Kate Rothwell  |     | Present  |                |                  | Charles Piso  |     | Present  |
| District 9   |                  |                |     |          |   District 10  |                  |               |     |          |
|              |                  | Alan Beebe     |     |          |                | Michael Tarbell  |               |     | Present  |
|              |                  |                |     |          |                |                  |               |     |          |
| District 11  |                  |                |     |          |   District 12  |                  |               |     |          |
|              |                  |                |     |          |                |                  | Bill Camarda  |     |          |
Present
|              |                  |                 |     |          |         | Bobby Maynard  |              |     |          |
| ------------ | ---------------- | --------------- | --- | -------- | ------- | -------------- | ------------ | --- | -------- |
| District 13  |                  |                 |     |          |   VAA   |                |              |     |          |
|              |                  | Eric Wilson     |     |          |         | Drew Hazelton  |              |     |          |
|              |                  |                 |     |          |         |                |              |     |          |
| IREMS        |                  |                 |     |          |   PFFV  |                |              |     |          |
|              |                  | Pat Malone      |     | Present  |         |                | Mark Hachey  |     | Present  |
|              |                  | Chris LaMonda   |     | Present  |         |                |              |     |          |
| VCFC         |                  |                 |     |          |   VSFA  |                |              |     |          |
|              |                  | Aaron Collette  |     | Present  |         |                |              |     |          |
|              | Michael Randzio  |                 |     | Present  |         |                |              |     |          |
| VAHHS        |                  |                 |     |          |   VLCT  |                |              |     |          |
|              |                  |                 |     |          |         |                | Lee Krohn    |     | Present  |
|              |                  |                 |     |          |         |                |              |     |          |
| VDH          |                  |                 |     |          |         |                |              |     |          |
Present
|     |     | Will Moran     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Chelsea Dubie  |     |     |     |     |     |     |     |

Non-members in attendance: Mark Considine, Courtney Newman, Ray Walker, Inge Smith-Iuce,
Dan Wolfson
Approval of July Meeting Minutes
The August 6th meeting minutes were previously distributed to committee members.
• Motion to approve the minutes by Michael Tarbell
• Seconded by Adam Heuslein
• No discussion.
• Result: The minutes were approved unanimously with no amendments.
Update - State EMS Office
• No new updates since our last meeting.
Update - Pat Malone
Has identified one intern (a UVM Rescue member developing a major in EMS) and is pursuing a
second intern from the UVM Public Health graduate program. Interns will assist in compiling
and synthesizing data to support the legislative report and the five-year EMS plan.
Education data collected by Cambridge Consulting Group was included in prior surveys but
results were limited. Consultant efforts provided demographic information about instructors but
not detailed course or budget data. Recognition that data gaps remain significant; moving
forward, the committee must define what data should be systematically collected.
EMS Instructor System and Accountability – Presentation by Pat Malone
• 12 Senior Instructors currently licensed; seven are full-time educators.
o They delivered:
? 63% of EMT courses (2023–2024)
? 78% of AEMT courses
? Two of three Paramedic courses
• 56 Instructor Coordinators (ICs) licensed, but:
o 79% did not teach any EMT courses during 2023–2024.
o Only five ICs taught more than one EMT course.
o 44 ICs did not appear in EMT course records.
Concerns raised -
Unlike the Fire Academy, which requires instructors to teach regularly or lose status, EMS ICs
face no accountability for inactivity. Our education system, which is a legacy system, has
allowed for individuals to be credentialed without teaching, reducing instructional reliability.
Discussion emphasized the need for standards, evaluation, and performance tracking for
educators, including QA/QI mechanisms.

Course Distribution and Access
• 62 EMT courses delivered in Vermont (2023–2024).
• 11 of 13 districts hosted EMT courses; District 8 had none, though students joined
courses through neighboring districts or statewide partners.
• 18 AEMT courses were held in eight districts; three Paramedic courses were offered
statewide.
• Geographic access analysis:
o CCV reports 95% of Vermonters live within 12 miles of a CCV site, most of
which hosted EMS courses.
o Accessibility challenges are more about timing, frequency, and travel reluctance
than geographic gaps.
o Some courses had very low enrollment (fewer than 10 students), raising efficiency
concerns.
• Alternative models discussed:
o Regional career centers (e.g., Central Vermont Career Center) hosting district
courses.
o A rotational model similar to Firefighter I training, reducing duplication while
ensuring regional coverage.
Cost of EMS Education
• Committee agreed that true program costs are largely unknown.
• Barriers identified:
o Institutional accounting complexity.
o Independent contractor models with limited transparency.
o Inconsistent or incomplete reporting from ICs.
o Hidden costs: insurance, equipment replacement, facilities, utilities, instructor
continuing education.
• District 6 has collected course budgets and will share detailed reports (e.g., costs for
exams, facilities, instructional stipends).
• Comparisons:
o Firefighter I course costs ? $25,000 for 24 students.
o EMT course costs vary widely ($800–$3,000 per student depending on provider).
• Members stressed that without credible cost data, legislative funding requests are
undermined.
Recruitment Pathways and VFR Program
• Vermont Emergency First Responder (VEFR) program has exceeded expectations:
o Originally designed during COVID for ski patrol, wilderness, and non-traditional
providers.
o Now heavily adopted by volunteer fire departments as an entry point for EMS
participation.
• Benefits:
o Low time commitment (?16 hours of training).

o No National Registry exam requirement.
o Immediate community benefit by increasing responder presence.
o Has helped re-energize volunteer agencies.
• Debate:
o Some argued scope should expand (e.g., vitals, basic assessments).
o Others warned against overlapping EMR/EMT roles.
o Consensus: VFR should remain limited but tracked as a recruitment pipeline into
EMR/EMT training.
Key Takeaways
1. Senior Instructors carry most of the system’s instructional burden.
2. Instructor Coordinators are underutilized, highlighting accountability gaps.
3. Course distribution is geographically adequate, but inefficiencies exist due to duplication
and small class sizes.
4. The cost of EMS education remains undefined and must be clarified for legislative
credibility.
5. VFR has proven a valuable recruitment tool, especially for rural districts and volunteer
fire services.
Next Steps
• Meeting with CCV Workforce Education leadership scheduled to explore collaboration.
• Subcommittee to develop recommendations on workforce and education reform for
inclusion in the legislative report.
• Collection of district-level cost data to continue.
• Further discussion of continuing education, specialty courses, and recertification at a
future session.
Committee Schedule
• September 3 – White River Valley Ambulance – 10 AM to 2 PM
• September 17 – Waterbury State Office Complex – 1 PM to 3 PM
Adjournment
Meeting adjourned at 2:58 PM

---

### 2025-08-06 — Vermont Board of Medical Practice — August 06, 2025

**[MINUTES] 2025-08-06_eprip-Ambulance-Equipment-List-20250806.xlsx**

## Master List
| Unnamed: 0 | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 |
| --- | --- | --- | --- |
| NaN | Category | Item | Licensure Level |
| NaN | Vehicle Condition - Critical Items | NaN | NaN |
| NaN | Vehicle Condition - Critical Items | Current DMV Registration | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Current DMV Inspection | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Current Red Light Permit | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Current Insurance Coverage | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Ambulance starts and operates in Drive and Reverse | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Body and sheet metal in satisfactory condition | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Clean and Orderly - Patient Compartment and Cab | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Exterior Compartment Doors Functional | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Interior Cabinet Doors Functional | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Patient Compartment and Cab Entry Doors Functional | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Emergency Lights Operational - Front Light Bar | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Emergency Lights Operational - Rear Light Bar | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Emergency Lights Operational - Side/Rear Panels | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Siren / Horn Functional | Required at all levels |
| NaN | NaN | Backup Alarm Function | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Turn Signals Functional | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Headlights Functional | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Taillights Functional | Required at all levels |
| NaN | Vehicle Condition - Critical Items | Items Heavier than 5 Pounds Secured | Required at all levels |
| NaN | Critical Equipment and Supplies | NaN | NaN |
| NaN | Critical Equipment and Supplies | Access to Pediatric/Adult Patient Care Protocols | Required at all levels |
| NaN | Critical Equipment and Supplies | Automated External Defibrillator / Monitor | Required at all levels |
| NaN | Critical Equipment and Supplies | AED Cables | Required at all levels |
| NaN | Critical Equipment and Supplies | AED Pads - Adult and Pediatric | Required at all levels |
| NaN | Critical Equipment and Supplies | 12-Lead Capability | Required at all levels |
| NaN | Critical Equipment and Supplies | Oxygen Tank & Regulator - Fixed | Required at all levels |
| NaN | Critical Equipment and Supplies | Oxygen Tank & Regulator - Portable | Required at all levels |
| NaN | Critical Equipment and Supplies | Portable Oxygen Secured | Required at all levels |
| NaN | Critical Equipment and Supplies | Two-Way Communication Device | Required at all levels |
| NaN | Critical Equipment and Supplies | Fire Extinguisher (Current Inspection) | Required at all levels |
| NaN | Critical Equipment and Supplies | Sharps Container - Fixed | Required at all levels |
| NaN | Critical Equipment and Supplies | Wheeled Cot - Functional & Secured | Required at all levels |
| NaN | Critical Equipment and Supplies | Age/Weight Appropriate Pediatric Restraint Device | Required at all levels |
| NaN | Critical Equipment and Supplies | Transcutaneous Cardiac Pacemaker Capability | Required at the Paramedic Level |
| NaN | Emergency Lighting | NaN | NaN |
| NaN | Emergency Lighting | Corner Lights Functional | Required at all levels |
| NaN | Emergency Lighting | Scene Lights Functional | Required at all levels |
| NaN | Emergency Lighting | Grill Lights Functional | Required at all levels |
| NaN | Emergency Lighting | Headlight Wig-Wags Functional (if present) | Required at all levels |
| NaN | Bandages / Dressings | NaN | NaN |
| NaN | Bandages / Dressings | Sterile Burn Sheets | Required at all levels |
| NaN | Bandages / Dressings | Triangular Bandages | Required at all levels |
| NaN | Bandages / Dressings | Abdominal Pads | Required at all levels |
| NaN | Bandages / Dressings | 4x4 Gauze Sponges (or other sizes) | Required at all levels |
| NaN | Bandages / Dressings | Trauma Dressings | Required at all levels |
| NaN | Bandages / Dressings | Gauze Rolls (Various Sizes) | Required at all levels |
| NaN | Bandages / Dressings | Sterile Occlusive Dressings (3" x 8" or larger) | Required at all levels |
| NaN | Bandages / Dressings | Adhesive Tape - Hypoallergenic (Various Sizes) | Required at all levels |
| NaN | Bandages / Dressings | Arterial Tourniquet (Commercial) | Required at all levels |
| NaN | Bandages / Dressings | Hemostatic Dressings (e.g., Combat Gauze) | Required at all levels |
| NaN | Obstetrical | NaN | NaN |
| NaN | Obstetrical | Sealed Obstetrical Kit | Required at all levels |
| NaN | Obstetrical | Infant Suction Bulb | Required at all levels |
| NaN | Obstetrical | Infant Thermal Absorbent Blanket (Heat Reflective) | Required at all levels |
| NaN | Obstetrical | Infant Head Cover | Required at all levels |
| NaN | Infection Control | NaN | NaN |
| NaN | Infection Control | Eye Protection | Required at all levels |
| NaN | Infection Control | Shoe / Boot Covers | Required at all levels |
| NaN | Infection Control | Face Shield | Required at all levels |
| NaN | Infection Control | Gloves (Non-Sterile) | Required at all levels |
| NaN | Infection Control | Coveralls or Gowns (impermiable with head cover) | Required at all levels |
| NaN | Infection Control | Waterless Hand Cleaner (Commercial Antimicrobial) | Required at all levels |
| NaN | Infection Control | Disinfectant Solution for Cleaning Equipment | Required at all levels |
| NaN | Infection Control | Sharps Container (Portable) | Required at all levels |
| NaN | Infection Control | Trash Bags for Bio-Hazard Waste (Color-Coded / Emblem) | Required at all levels |
| NaN | Infection Control | N95 Respiratory Protection | Required at all levels |
| NaN | Ventilation / Airway | NaN | NaN |
| NaN | Ventilation / Airway | Rigid Suction Catheters | Required at all levels |
| NaN | Ventilation / Airway | Flexible Suction Catheter (at least one between 6F - 10F) | Required at all levels |
| NaN | Ventilation / Airway | Flexible Suction Catheter (at least one between 12F - 16F) | Required at all levels |
| NaN | Ventilation / Airway | Oxygen Mask (NRB or Valveless) - Adult, | Required at all levels |
| NaN | Ventilation / Airway | Oxygen Mask (NRB or Valveless) - Child | Required at all levels |
| NaN | Ventilation / Airway | Oxygen Mask (NRB or Valveless) - Infant | Required at all levels |
| NaN | Ventilation / Airway | Suction - Portable | Required at all levels |
| NaN | Ventilation / Airway | Suction - Fixed Unit | Required at all levels |
| NaN | Ventilation / Airway | Suction Tubing | Required at all levels |
| NaN | Ventilation / Airway | Nasal Cannulas - Adult | Required at all levels |
| NaN | Ventilation / Airway | Nasal Cannulas - Child | Required at all levels |
| NaN | Ventilation / Airway | Oxygen Supply Tubing | Required at all levels |
| NaN | Ventilation / Airway | Pulse Oximeter with Probes - Adult | Required at all levels |
| NaN | Ventilation / Airway | Pulse Oximeter with Probes - Pediatric | Required at all levels |
| NaN | Ventilation / Airway | Bag Valve Mask Device with O2 Reservoir - Adult | Required at all levels |
| NaN | Ventilation / Airway | Bag Valve Mask Device with O2 Reservoir - Child | Required at all levels |
| NaN | Ventilation / Airway | BVM Mask - Adult | Required at all levels |
| NaN | Ventilation / Airway | BVM Mask - Child | Required at all levels |
| NaN | Ventilation / Airway | BVM Mask - Infant | Required at all levels |
| NaN | Ventilation / Airway | BVM Mask - Neonate | Required at all levels |
| NaN | Ventilation / Airway | Oropharyngeal Airways - Sizes 0 - 5 | Required at all levels |
| NaN | Ventilation / Airway | Nasopharyngeal Airways - Sized 12F - 34F | Required at all levels |
| NaN | Ventilation / Airway | CPAP with Mask and Tubing | Required at the AEMT Level |
| NaN | Ventilation / Airway | Quantitative Waveform Capnography | Required at the AEMT Level |
| NaN | Ventilation / Airway | EtCO2 Monitoring Device | Required at the AEMT Level |
| NaN | Ventilation / Airway | Surpaglottic Airway Device: iGel 1-5 / King LTD 0-5 / LMA 1-6 / Other | Required at the AEMT Level |
| NaN | Ventilation / Airway | Laryngoscope Handles - Adult and Pediatric | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Extra Laryngoscope Bulbs and Batteries | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Laryngoscope Blades - Miller sizes 0-5 / MacIntosh sizes 1-4 | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Endotracheal Tubes (2 sets) - Cuffed or Uncuffed Sizes 2.5 - 5.0 | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Endotracheal Tubes (2 sets) - Cuffed Sizes 6.0 - 8.0 | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Stylettes for Endotracheal Tubes - Adult and Pediatric | Required at the Paramedic Level |
| NaN | NaN | Percutaneous Cricothyrotomy Kit (Commercial) | Not required if Surgical is present |
| NaN | Ventilation / Airway | Surgical Crycothyrotomy Kit (With Training) | Required at the Paramedic Level |
| NaN | Ventilation / Airway | BiPAP (Optional) | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Syringes - 10ml | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Magill (Rovenstein) Forceps - Adult and Pediatric | Required at the Paramedic Level |
| NaN | Ventilation / Airway | Gum Elastic Bougie | Required at the Paramedic Level |
| NaN | Medications | NaN | NaN |
| NaN | Medications | Aspirin | Required at all levels |
| NaN | Medications | Epi (1:1,000) Auto-Injector - Adult (or Ready/Check/Inject Kit) | Required at all levels |
| NaN | Medications | Epi (1:1,000) Auto-Injector - Pediatric (or Ready/Check/Inject Kit) | Required at all levels |
| NaN | Medications | Pure Vermont Maple Syrup (or Oral Glucose) | Required at all levels |
| NaN | Medications | Naloxone (Intranasal) | Required at all levels |
| NaN | Medications | Naloxone (IV/IM/IO/SQ) | Required at the AEMT Level |
| NaN | Medications | Nitroglycerin | Required at the AEMT Level |
| NaN | Medications | Ondansetron (ODT) | Required at the AEMT Level |
| NaN | Medications | Albuterol /DuoNeb | Required at the AEMT Level |
| NaN | Medications | D10 (or D50) | Required at the AEMT Level |
| NaN | Medications | Glucagon | Required at the AEMT Level |
| NaN | Medications | Epinephrine (1:1,000 & 1:10,000) | Required at the AEMT Level |
| NaN | Medications | Paramedic Medications, per Current State Protocols | Required at the Paramedic Level |
| NaN | Vascular Access | NaN | NaN |
| NaN | Vascular Access | IV Tourniquet - Latex Free | Required at the AEMT Level |
| NaN | Vascular Access | Isotonic Crystalloid Solutions (0.9% NaCl, etc.) - 4 liters (bags, not bottles) | Required at the AEMT Level |
| NaN | Vascular Access | Antiseptic Solution | Required at the AEMT Level |
| NaN | Vascular Access | IV Pole or Roof Hook | Required at the AEMT Level |
| NaN | Vascular Access | Intravenous Arm Board - Adult and Pediatric | Required at the AEMT Level |
| NaN | Vascular Access | Intravenous Catheters - Sizes 14G - 24G | Required at the AEMT Level |
| NaN | Vascular Access | Intraosseous Access Needles & Devices - Adult and Pediatric | Required at the AEMT Level |
| NaN | Vascular Access | Syringes - Various Sizes | Required at the AEMT Level |
| NaN | Vascular Access | Needles Suitable for IM Injection - Various Sizes | Required at the AEMT Level |
| NaN | Vascular Acce

*[document truncated for length]*

---

**[MINUTES] 2025-08-06_eprip-EMS-advisory-minutes-8.6.25.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: August 06, 2025
Location: Waterbury State Office Complex, Waterbury, & Microsoft Teams
Meeting Called to Order: 10:04 AM by Drew Hazelton

Rollcall – Committee Members

|              | Representative    | Present  |     |   Representative  |                  | Present  |     |
| ------------ | ----------------- | -------- | --- | ----------------- | ---------------- | -------- | --- |
| District 1   |                   |          |     |   District 2      |                  |          |     |
|              |                   |          |     |                   | Adam Heuslein    |          | X   |
|              |                   |          |     |                   | Samantha Atwood  |          |     |
| District 3   |                   |          |     |   District 4      |                  |          |     |
|              | Leslie Lindquist  |          |     |                   | Scott Brinkman   |          |     |
|              | Becky Alemy       |          |     |                   | Jeff Johansen    |          | X   |
| District 5   |                   |          |     |   District 6      |                  |          |     |
|              |                   |          |     |                   | Joe Aldsworth    |          | X   |
|              |                   |          |     |                   | David Danforth   |          |     |
| District 7   |                   |          |     |   District 8      |                  |          |     |
|              | Charlene Phelps   |          |     |                   | Matt Parrish     |          | X   |
|              | Kate Rothwell     |          | X   |                   | Charles Piso     |          | X   |
| District 9   |                   |          |     |   District 10     |                  |          |     |
|              | Alan Beebe        |          |     |                   | Michael Tarbell  |          | X   |
|              |                   |          |     |                   |                  |          |     |
| District 11  |                   |          |     |   District 12     |                  |          |     |
|              |                   |          |     |                   | Bill Camarda     |          | X   |
|              |                   |          |     |                   | Bobby Maynard    |          | X   |
| District 13  |                   |          |     |   VAA             |                  |          |     |
|              | Eric Wilson       |          | X   |                   | Drew Hazelton    |          | X   |
|              |                   |          |     |                   |                  |          |     |
| IREMS        |                   |          |     |   PFFV            |                  |          |     |
|              | Pat Malone        |          | X   |                   | Mark Hachey      |          | X   |
|              | Chris LaMonda     |          |     |                   |                  |          |     |
| VCFC         |                   |          |     |   VSFA            |                  |          |     |
|              | Aaron Collette    |          | X   |                   |                  |          |     |
|              | Michael Randzio   |          | X   |                   |                  |          |     |
| VAHHS        |                   |          |     |   VLCT            |                  |          |     |
|              |                   |          |     |                   | Lee Krohn        |          |     |
|              |                   |          |     |                   |                  |          |     |
| VDH          |                   |          |     |                   |                  |          |     |
|              | Will Moran        |          | X   |                   |                  |          |     |
|              | Chelsea Dubie     |          |     |                   |                  |          |     |

Non-members in attendance: Dan Wolfson, Connor Dunn, Courtney Newman, Ray Walker,
Donna Jacob
Approval of July Meeting Minutes
The July 9th and July 16 meeting minutes were previously distributed to committee members.
• Motion to approve the minutes by Michael Tarbell
• Seconded by Adam Heuslein
• No discussion.
• Result: 12 votes to accept the meeting minutes as presented, 1 abstained. Motion passed.
Adoption of EMS Definition
The committee needed a consensus definition of Emergency Medical Services (EMS) to frame
the forthcoming five-year EMS State Plan.
Draft Definition:
"Emergency Medical Services is an integrated system of emergent and non-emergent practice of
medicine in the out-of-hospital environment. This includes personnel and resources designed to
assess, treat, and determine the disposition of patients with injury and illness and those in need
of specialized care and safe transportation. EMS is a vital component of the healthcare, public
health, and public safety systems."
Key Discussion Points:
• Legal concern - The phrase "determine the disposition" raised ethical and legal
concerns—could be misinterpreted as EMS determining a patient's fate or overriding
consent.
• Friendly amendment - Add “appropriate” before “disposition” to clarify the role of EMS
as advisory rather than determinative.
Committee agreed that this language better aligns with patient rights and scope of
o
practice; the friendly amendment was accepted.
• Scope clarification - This definition is not statutory—it will be used in the advisory plan
and does not override existing legal language.
Revised Definition:
"Emergency Medical Services is an integrated system of emergent and non-emergent practice of
medicine in the out-of-hospital environment. This includes personnel and resources designed to
assess, treat, and determine the appropriate disposition of patients with injury and illness and
those in need of specialized care and safe transportation. EMS is a vital component of the
healthcare, public health, and public safety systems."
Motion – Adoption of EMS definition

• Motion to Accept the revised definition of EMS made by Pat Malone, and seconded by
Adam Heuslein
• Friendly amendment Accepted – Yes
• Result - Unanimously passed via roll call vote. Montion passed
Noted - Eric Wilson (District 13) and Joe Aldsworth (District 6) confirmed their votes post-hoc
due to technical audio issues.
This definition will be used in official committee reports and the upcoming EMS State Plan.
Performance Metrics Presentation and Planning
Presenter - EMS Data Manager Connor Dunn
Meet statutory obligations under the EMS planning legislation. Establish data-backed,
measurable indicators of EMS system performance. Create a framework for statewide QA/QI
(Quality Assurance/Improvement) and policy decisions.
Criteria for Selecting Metrics:
• Nationally recognized (e.g., NEMSQA, NEMSIS, CARES).
• Ability to extract from Vermont’s SIREN ePCR data.
• Must represent key clinical and operational areas (e.g., trauma, medical, pediatrics,
system readiness).
• Should ideally allow benchmarking against national norms.
Proposed Metrics:
1. Hypoglycemia 01 – % of symptomatic hypoglycemia patients who received treatment.
2. Pediatrics – Weight-based dosing and vital signs documented.
3. Trauma 08 – Documentation of GCS, SBP, and RR in trauma cases.
4. Chest Pain & STEMI – ECG, aspirin administration, etc.
5. Safety 02 – No use of lights/sirens during transport.
6. System Readiness – Response times >15 minutes (urban) or >30 minutes (rural).
7. Stroke 01 – % of suspected stroke patients who received prehospital stroke assessment.
Technical Details:
• Data Source: SIREN ePCR system (Vermont’s NEMSIS-compliant platform).
• Dependencies: Data documentation by EMS crews; some fields are optional or
inconsistently filled.
• Validation Needs: Manual queries; complex formulas; many records (30,000+).
• Limitations:
PSAP data not integrated ? no full response time visibility.
o
Incomplete documentation ? potential under-reporting.
o
Labor Intensive ? EMS Office lacks sufficient staff for data analysis.
o

Extended Committee Discussion on Metrics:
• Data Integrity: Emphasis on “garbage in, garbage out.” Poor documentation skews
results.
• BioSpatial Platform:
Long-term solution that would automate analysis and dashboards.
o
The EMS Office is making progress towards obtaining this software platform.
o
Would support agency-level data analysis.
o
• Short-Term Limitations:
Metrics must be selected that can be processed manually or with existing systems.
o
Manual report writing, querying, and QA needed for every metric.
o
Some metrics (e.g., Safety 02) are preferable because they are less prone to subjective error and
provide system-level insight. The System Readiness (response time) metric is valuable but
flawed—without PSAP time stamps, EMS clock starts late. Agency-specific metrics not feasible
due to data sensitivity, DUAs, and resource constraints.
Motion - Adoption of Performance Metrics
• Motion to adopt Hypoglycemia 01, Trauma 08, Safety 02, and Stroke 01 made by Bill
Camarda
• Seconded Adam Heuslein
• No additional discussion
• Result - Unanimously passed via roll call vote
These four metrics will be included in the EMS Plan and assessed using available data (via
NEMSIS or SIREN).
Motion - Authority to Pay for NEMSIS Data
Committee may need to request performance data from the national NEMSIS database to avoid
manual report generation. It is unclear if NEMSIS will charge a processing fee.
• Motion to allow the fiscal agent to pay a reasonable fee for data retrieval from NEMSIS
if needed, and to leave cost discretion to the committee chair made by Adam Heuslein
• Seconded by Michael Tarbell
• No additional discussion
• Result – Unanimously passed.
Service Inventory and Data Verification Update
Over the last month the percentage of ambulance services having reported their financial data has
increased from >20% to >70%. Committee members will be asked to contact those ambulance
services that have not responded to the contactor’s inquiry. The contractor will soon begin to
contact first response squads.

Interfacility Transport Data Analysis
The contractor is analyzing interfacility transport data for inclusion in the plan. It was
determined that greater than 2,000 out-of-state records (e.g., Washington D.C., Maryland) were
included in the dataset and have since been removed. Missing from the data set is the name of
the transporting agency, and the level of care provided. These fields were removed from the data
set delivered by Cambridge due to DUA restrictions.
Next Steps include additional data cleanup, integration of Vermont-specific identifiers, and
possible supplemental request to Cambridge or direct data export from Siren.
Key Challenges and Strategic Considerations
Issue Summary
Current EMS Office lacks a data analyst. Nearly all data analysis
Staff Capacity
handled by one person (Connor Dunn).
Documentation Many performance gaps may be due to poor or inconsistent
Quality documentation rather than actual performance deficiencies.
Lack of connection between EMS and 911 (PSAP) systems hampers full
System Integration
response time analysis.
Plan is due to the legislature in December, 2025. Time-sensitive work
Short Timeline
must be completed in the next 3 months.
Legal/Data Sharing DUAs and PHI restrictions limit outside help unless contracts or
Restrictions institutional support (e.g., UVM grad students) can be quickly arranged.
The committee continues to push for investments (e.g., BioSpatial, staff
Budget
positions) but legislative funding remains uncertain.
Committee Reports
The committee agrees that a contractor is needed to draft the legislative reports. Several options
were discuss, such as university students, or a technical expert from the National Association of
State EMS Officials. After futher disc

*[document truncated for length]*

---

### 2025-07-16 — Vermont Board of Medical Practice — July 16, 2025

**[MINUTES] 2025-07-16_ems-advisory-committee-july-16-minutes.pdf**

Vermont Emergency Medical Services
Advisory Committee

Meeting Minutes

Date: July 16, 2025
Location: Northeastern Vermont Regional Hospital & Microsoft Teams
Attendance: Drew Hazelton, Adam Heuslein, Pat Malone, Michael Wright, Courtney Newman,
Aaron Collette, Charles Piso, Will Moran, Dan Wolfson, Connor Dunn, Michael Tarbell, Brad
(no last name), Kate Rothwell, Joe Aldsworth, William Fritz, Charles Keir, Kathy Jochim,
Chelsea Dubie, Leslie Lindquist, Bill Camarda, Matthew Parrish, Donna Jacob

Meeting called to order: 1:07 PM

Call to Order and Agenda Modifications

Chair Drew Hazelton called the meeting to order and requested additions or deletions to the
agenda. One addition was made: a financial update from the fiscal agent. The update will be
included in the formal meeting minutes.

Financial Report

William Moran presented a summary of the Advisory Committee’s financial status:

•  Total Allocation (Act 157): $370,000
•  Funds Expended: $148,200
•  Remaining Balance: $221,800

In addition to these project-specific funds, the Advisory Committee receives an annual operating
allocation of $40,000, which may be rolled over for up to three years, totaling $120,000 in
potential support. The use of each funding stream must align with its intended purpose, either
operational support or project-specific deliverables.

Data Integrity and Minutes

The Committee acknowledged the absence of official minutes from the July 9th meeting due to
technical issues with the AI-based note-taking system. A summary is being reconstructed
manually using available data and partial recordings.

Primary Discussion: Performance Measures for EMS System Evaluation

Purpose

The Committee focused on identifying meaningful and actionable performance measures to
inform the development of Vermont’s EMS Five-Year Strategic Plan, as required by Act 157.

Drew Hazelton emphasized the importance of establishing performance metrics to define
baseline conditions, set improvement goals, and report outcomes to stakeholders, particularly the
legislature.

Clinical Measures

The Committee discussed the adoption of standardized clinical quality metrics, particularly those
defined by:

•  NEMSQA (National EMS Quality Alliance)
•  NEMSIS (National EMS Information System)

These standardized metrics are:

•  Based on nationally accepted definitions
•  Aligned with available data through ImageTrend/SIREN
•  Potentially compatible with Biospatial reporting dashboards

Example measures under consideration:

•  Timeliness and frequency of 12-lead EKG acquisition for ACS patients
•  Assessment and documentation standards for stroke, diabetes, and trauma cases

Committee members agreed that adoption of existing standards, rather than the creation of
custom metrics, would ensure greater validity, comparability, and resource efficiency.

Operational and System Reliability Measures

The Committee discussed ongoing challenges in measuring EMS system reliability, including:

Inconsistent 24/7/365 ambulance coverage across services

•
•  Lack of centralized or standardized dispatch time data
•  Difficulty capturing accurate mutual aid incidents and delays

Key Points Raised:

•  Many services do not have comprehensive dispatch CAD systems.
•  Existing systems often rely on manual time entries, which are prone to inconsistency.
•  Mutual aid responses are frequently underreported or misclassified in SIREN.

Potential Metrics Discussed:

•  Percentage of time services are unable to staff a primary ambulance
•  Number and frequency of mutual aid responses by town and agency
•  Proportion of agencies able to provide continuous 24/7 coverage

It was noted that while the ideal long-term solution would involve a statewide CAD system,
interim data collection efforts—such as structured interviews and targeted surveys—would be
essential.

CARES Registry and Dispatch Data

Dr. Daniel Wolfson reported on Vermont’s participation in the CARES (Cardiac Arrest Registry
to Enhance Survival) program, which includes:

•  Statewide cardiac arrest reporting
•  Outcome data such as AED use and neurologic survival
•  New collaboration with the 911 Board to provide time-to-dispatch data for cardiac arrests

This dataset offers an example of a reliable, reproducible, and outcome-focused performance
metric system already in place.

Data Access and Biospatial Integration

The Committee discussed recent progress in procuring Biospatial, a data visualization and
analytics platform that would:

Integrate with ImageTrend/SIREN

•
•  Allow real-time access to EMS performance dashboards
•  Support agency-level and statewide data comparisons

Although the contract is not finalized, the Office of EMS has received authorization to draft
contract language.

Next Steps: Formation of Technical Advisory Groups

To advance the development of performance measures, the Committee agreed to establish
subgroups, referred to as technical advisory groups (TAGs), to explore and recommend metrics
in the following domains:

•  Clinical performance
•  Operational/system reliability
•  Education and workforce development
•  Financial health and sustainability

The Office of EMS will work with its data team and Committee members to:

•  Review existing NEMSQA and CARES metrics
•  Assess feasibility based on currently available data
•  Recommend several initial measures for use in the EMS plan

Legislative Reporting and Accountability

Committee members stressed the importance of accountability and accurate system
representation in forthcoming reports to the legislature. Proposals included:

•  Tying reporting requirements to EMS licensing or provider tax submissions
•
•  Emphasizing transparency and support over punitive enforcement in early data collection

Issuing follow-up phone calls to collect critical operational data

phases

There was consensus that the Committee must report on not only services that have failed but
also those at risk, to guide future funding, legislative support, and system-wide improvements.

Meeting Conclusion and Action Items

Agreements:

•  Performance measures are essential and will be developed and presented at the next

meeting.
Initial focus will be on measures for which data currently exists or can be gathered.

•
•  Phone outreach to agencies has begun to verify system reliability information.
•  Legislative mandates regarding annual budget reviews and performance reporting will be

central to the Committee’s deliverables.

Next Meeting:

•  Members will receive a summary of candidate performance metrics and

recommendations from the data team.

•  Establish a technical advisory group to advance and agree upon performance metrics for

inclusion in the EMS plan will be reviewed.

Meeting adjourned at: 3 PM

---

### 2025-07-09 — Vermont Board of Medical Practice — July 09, 2025

**[MINUTES] 2025-07-09_eprip-advisory-council-july-9-minutes.pdf**

Vermont Emergency Medical Services
Advisory Committee
Meeting Minutes
Date: July 9, 2025
Location: Department of Health, Waterbury State Office Complex
Attendance: Drew Hazelton, Pat Malone, Aaron Collette, Charles Piso, Will Moran, Dan
Wolfson, Michael Tarbell, Jim Finger, Kate Rothwell, Chelsea Dubie, Leslie Lindquist, Bill
Camarda, Matthew Parrish, Donna Jacob, Bobby Maynard, Samantha Atwood
Meeting called to order: 10:00 AM
This meeting was facilitated by Katherine Sims.
Welcome and Framing the Day
Meeting participants each shared one thing they hoped the group leaves with today. Examples
include, “Progress and vision, engaged participants, clarity, vision for the future, progress,
towards 5-year plan, unity, tangible outcomes, increase energy, governance model.”
Draft Definition, Vision, and Principles
Key takeaways -
• Break up paragraphs in current state
• Get tone right, balance narrative and data
• In EMS definition, name “practice of medicine” intersection of public safety, public
health, healthcare, emergency management,
• Consider 500 characters or less with a longer explanation if needed
Latest version of the EMS definition:
Emergency Medical Services (EMS) is an integrated practice of medicine including personnel,
vehicles, equipment, protocols and dispatch that delivers emergency and non-emergency medical
care and transportation to individuals with illness, injury, or other health needs. EMS provides
rapid response to 911 calls, interfacility transfers, and time-sensitive care in the field, while also
supporting community health through mobile integrated healthcare, public health initiatives such
as vaccination and testing programs, and disaster response. EMS clinicians assess, treat, monitor,
and determine appropriate disposition for patients—including treatment in place, referral to
services, and transport to alternative destinations—making EMS a vital intersection of the
healthcare, public health, public safety, and emergency management systems.

Draft Six-Month Timeline
•
July 16 – EMSAC meeting revised definitions and system benchmarks.
•
August 6 – Finalize system benchmarks.
•
August 20 – EMS training presentation.
•
September – Finance
•  October – Line level data, and select a contractor to write the five-year plan.
•  Considerations include:
?  High level outreach about the process.
?  More district level engagement.
?  Road show to get public and stakeholder input.
?  Public comment on the draft plan.
Public messaging in two rounds.
•
Round 1
?  Why EMS matters.
?  Here is the data and current situation.
?  We have a timeline for our process.
?  We’re doing the work/we have a legislative mandate.
?  We want your input.
•  Round 2
?  We have a draft plan, and we want your comments.
Governance Roles
|                        | Local   | Regional  | State  |
| ---------------------- | ------- | --------- | ------ |
| EMS Task Force         |         |           | X      |
| MCI planning           |         |           | X      |
| Education - delivery   |         | X         |        |
| Education - Funding    |         |           | X      |
& oversight
| IFT                |     |     | X   |
| ------------------ | --- | --- | --- |
| Paramedic service  |     | X   |     |
coordination

| Service budget  |     |     | EMSAC  |
| --------------- | --- | --- | ------ |
review
| Ambulance  |     |     | X   |
| ---------- | --- | --- | --- |
inspection
| Service licensing   |     |     | X   |
| ------------------- | --- | --- | --- |
| Clinical standards  |     |     | X   |
| Statewide EMS       |     |     | X   |
protocols
| State Medical  |     |     | X   |
| -------------- | --- | --- | --- |
Director
| Service level MD:  | X   |     |     |
| ------------------ | --- | --- | --- |
-  Credentialing
-  Validate Edu
-  Review QA/QI
-  MIH
-  Be present
on the
ground at
service
| Dispatch           |            | X   | X   |
| ------------------ | ---------- | --- | --- |
| MIH - guidelines   |            |     | X   |
| MIH -              | X with MD  | X   |     |
implementation
| QA/QI - Standards  |     |     | X   |
| ------------------ | --- | --- | --- |
| QA-QI              | X   | X   |     |
implementation with
MD

| Global funding  |     |     | X   |
| --------------- | --- | --- | --- |
oversight and
response standards
| Personnel licensing   |     |     | X   |
| --------------------- | --- | --- | --- |
| Credentialing -       |     |     | X   |
Standards
| Credentialing -  | X with MD  |     |     |
| ---------------- | ---------- | --- | --- |
implementation
| Workforce  |     |     | X   |
| ---------- | --- | --- | --- |
recruitment and
development
| Data management   |     |     | X   |
| ----------------- | --- | --- | --- |
| Public relations  |     |     | X   |
| Mutual Aid (with  |     | X?  | X?  |
MCI?)

EMS Final Report Outline (draft)
•
Vermont’s EMS definition
•
Current status
•  Vision statement
•  Guiding principals
•  Governance roles
•  Finance
•  Line level data
•  System benchmarks
•  Education plan

Next Steps
• Continue to work with districts to validate service level data
• Create roadshow work group to create a “meeting in a box”
• Develop public messaging
• VDH send out letter to districts to formally appoint member to VEMSAC and alternate
with deadline of August meeting
• Flush out metrics for success for vision
• Continue to refine EMS definition
• Consider bringing on more capacity to help facilitate meetings and write report
• Statewide cardiac arrest reporting
• Outcome data such as AED use and neurologic survival
• New collaboration with the 911 Board to provide time-to-dispatch data for cardiac arrests
Final Reflections & Close
• “What’s one insight or priority you’re leaving with?”
? Concerns about the number of tasks that got moved to EMS office staff
? Work to do
? Amount of change from local to state for standardization
? Grateful for group (and wish there were more folks here)
? Complexity
? Determined
? Need to better understand other perspectives
? Challenges aren’t unique to Vermont/we aren’t alone
? Service level MD idea is interesting and at same time don't want to lose sight of
the value of regional coordination
Meeting adjourned at: 3:30 PM
