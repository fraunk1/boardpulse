"""Comprehensive US state medical board registry.

Data compiled from FSMB member board listings. All 50 states + DC.
States with separate osteopathic boards are listed separately.
"""

BOARDS = [
    # Alabama
    {"state": "AL", "code": "AL_MD", "name": "Alabama Board of Medical Examiners", "board_type": "combined", "homepage": "https://www.albme.org"},
    # Alaska
    {"state": "AK", "code": "AK_MD", "name": "Alaska State Medical Board", "board_type": "combined", "homepage": "https://www.commerce.alaska.gov/web/cbpl/ProfessionalLicensing/StateMedicalBoard.aspx"},
    # Arizona
    {"state": "AZ", "code": "AZ_MD", "name": "Arizona Medical Board", "board_type": "MD", "homepage": "https://www.azmd.gov"},
    {"state": "AZ", "code": "AZ_DO", "name": "Arizona Board of Osteopathic Examiners in Medicine and Surgery", "board_type": "DO", "homepage": "https://www.azdo.gov"},
    # Arkansas
    {"state": "AR", "code": "AR_MD", "name": "Arkansas State Medical Board", "board_type": "combined", "homepage": "https://www.armedicalboard.org"},
    # California
    {"state": "CA", "code": "CA_MD", "name": "Medical Board of California", "board_type": "combined", "homepage": "https://www.mbc.ca.gov"},
    # Colorado
    {"state": "CO", "code": "CO_MD", "name": "Colorado Medical Board", "board_type": "combined", "homepage": "https://dpo.colorado.gov/MedicalBoard"},
    # Connecticut
    {"state": "CT", "code": "CT_MD", "name": "Connecticut Medical Examining Board", "board_type": "combined", "homepage": "https://portal.ct.gov/DPH/Practitioner-Licensing--Investigations/Medical/Connecticut-Medical-Examining-Board"},
    # Delaware
    {"state": "DE", "code": "DE_MD", "name": "Delaware Board of Medical Licensure and Discipline", "board_type": "combined", "homepage": "https://dpr.delaware.gov/boards/medicalpractice/"},
    # DC
    {"state": "DC", "code": "DC_MD", "name": "District of Columbia Board of Medicine", "board_type": "combined", "homepage": "https://dchealth.dc.gov/service/board-medicine"},
    # Florida
    {"state": "FL", "code": "FL_MD", "name": "Florida Board of Medicine", "board_type": "MD", "homepage": "https://flboardofmedicine.gov"},
    {"state": "FL", "code": "FL_DO", "name": "Florida Board of Osteopathic Medicine", "board_type": "DO", "homepage": "https://flboardofosteopathicmedicine.gov"},
    # Georgia
    {"state": "GA", "code": "GA_MD", "name": "Georgia Composite Medical Board", "board_type": "combined", "homepage": "https://medicalboard.georgia.gov"},
    # Hawaii
    {"state": "HI", "code": "HI_MD", "name": "Hawaii Medical Board", "board_type": "combined", "homepage": "https://cca.hawaii.gov/pvl/boards/medical/"},
    # Idaho
    {"state": "ID", "code": "ID_MD", "name": "Idaho Board of Medicine", "board_type": "combined", "homepage": "https://elitepublic.bom.idaho.gov"},
    # Illinois
    {"state": "IL", "code": "IL_MD", "name": "Illinois Medical Licensing Board", "board_type": "combined", "homepage": "https://idfpr.illinois.gov/profs/medlicboard.html"},
    # Indiana
    {"state": "IN", "code": "IN_MD", "name": "Indiana Medical Licensing Board", "board_type": "combined", "homepage": "https://www.in.gov/pla/professions/medical-licensing-board-of-indiana/"},
    # Iowa
    {"state": "IA", "code": "IA_MD", "name": "Iowa Board of Medicine", "board_type": "combined", "homepage": "https://medicalboard.iowa.gov"},
    # Kansas
    {"state": "KS", "code": "KS_MD", "name": "Kansas State Board of Healing Arts", "board_type": "combined", "homepage": "https://www.ksbha.org"},
    # Kentucky
    {"state": "KY", "code": "KY_MD", "name": "Kentucky Board of Medical Licensure", "board_type": "combined", "homepage": "https://www.kbml.ky.gov"},
    # Louisiana
    {"state": "LA", "code": "LA_MD", "name": "Louisiana State Board of Medical Examiners", "board_type": "combined", "homepage": "https://www.lsbme.la.gov"},
    # Maine
    {"state": "ME", "code": "ME_MD", "name": "Maine Board of Licensure in Medicine", "board_type": "MD", "homepage": "https://www.maine.gov/md/"},
    {"state": "ME", "code": "ME_DO", "name": "Maine Board of Osteopathic Licensure", "board_type": "DO", "homepage": "https://www.maine.gov/osteo/"},
    # Maryland
    {"state": "MD", "code": "MD_MD", "name": "Maryland Board of Physicians", "board_type": "combined", "homepage": "https://www.mbp.state.md.us"},
    # Massachusetts
    {"state": "MA", "code": "MA_MD", "name": "Massachusetts Board of Registration in Medicine", "board_type": "combined", "homepage": "https://www.mass.gov/orgs/board-of-registration-in-medicine"},
    # Michigan
    {"state": "MI", "code": "MI_MD", "name": "Michigan Board of Medicine", "board_type": "MD", "homepage": "https://www.michigan.gov/lara/bureau-list/bpl/health/hp-lic-health-prof/medicine"},
    {"state": "MI", "code": "MI_DO", "name": "Michigan Board of Osteopathic Medicine and Surgery", "board_type": "DO", "homepage": "https://www.michigan.gov/lara/bureau-list/bpl/health/hp-lic-health-prof/osteopathic"},
    # Minnesota
    {"state": "MN", "code": "MN_MD", "name": "Minnesota Board of Medical Practice", "board_type": "combined", "homepage": "https://mn.gov/boards/medical-practice/"},
    # Mississippi
    {"state": "MS", "code": "MS_MD", "name": "Mississippi State Board of Medical Licensure", "board_type": "combined", "homepage": "https://www.msbml.ms.gov"},
    # Missouri
    {"state": "MO", "code": "MO_MD", "name": "Missouri State Board of Registration for the Healing Arts", "board_type": "combined", "homepage": "https://pr.mo.gov/healingarts.asp"},
    # Montana
    {"state": "MT", "code": "MT_MD", "name": "Montana Board of Medical Examiners", "board_type": "combined", "homepage": "https://boards.bsd.dli.mt.gov/medical-examiners"},
    # Nebraska
    {"state": "NE", "code": "NE_MD", "name": "Nebraska Board of Medicine and Surgery", "board_type": "combined", "homepage": "https://dhhs.ne.gov/licensure/Pages/Medicine-and-Surgery.aspx"},
    # Nevada
    {"state": "NV", "code": "NV_MD", "name": "Nevada State Board of Medical Examiners", "board_type": "MD", "homepage": "https://medboard.nv.gov"},
    {"state": "NV", "code": "NV_DO", "name": "Nevada State Board of Osteopathic Medicine", "board_type": "DO", "homepage": "https://www.bom.nv.gov"},
    # New Hampshire
    {"state": "NH", "code": "NH_MD", "name": "New Hampshire Board of Medicine", "board_type": "combined", "homepage": "https://www.oplc.nh.gov/board-medicine"},
    # New Jersey
    {"state": "NJ", "code": "NJ_MD", "name": "New Jersey State Board of Medical Examiners", "board_type": "combined", "homepage": "https://www.njconsumeraffairs.gov/bme/"},
    # New Mexico
    {"state": "NM", "code": "NM_MD", "name": "New Mexico Medical Board", "board_type": "combined", "homepage": "https://www.nmmb.state.nm.us"},
    # New York
    {"state": "NY", "code": "NY_MD", "name": "New York State Board for Medicine", "board_type": "combined", "homepage": "https://www.op.nysed.gov/professions/medicine"},
    # North Carolina
    {"state": "NC", "code": "NC_MD", "name": "North Carolina Medical Board", "board_type": "combined", "homepage": "https://www.ncmedboard.org"},
    # North Dakota
    {"state": "ND", "code": "ND_MD", "name": "North Dakota Board of Medicine", "board_type": "combined", "homepage": "https://www.ndbm.org"},
    # Ohio
    {"state": "OH", "code": "OH_MD", "name": "State Medical Board of Ohio", "board_type": "combined", "homepage": "https://med.ohio.gov"},
    # Oklahoma
    {"state": "OK", "code": "OK_MD", "name": "Oklahoma State Board of Medical Licensure and Supervision", "board_type": "MD", "homepage": "https://www.okmedicalboard.org"},
    {"state": "OK", "code": "OK_DO", "name": "Oklahoma State Board of Osteopathic Examiners", "board_type": "DO", "homepage": "https://www.ok.gov/osboe/"},
    # Oregon
    {"state": "OR", "code": "OR_MD", "name": "Oregon Medical Board", "board_type": "combined", "homepage": "https://www.oregon.gov/omb/"},
    # Pennsylvania
    {"state": "PA", "code": "PA_MD", "name": "Pennsylvania State Board of Medicine", "board_type": "MD", "homepage": "https://www.dos.pa.gov/ProfessionalLicensing/BoardsCommissions/Medicine/"},
    {"state": "PA", "code": "PA_DO", "name": "Pennsylvania State Board of Osteopathic Medicine", "board_type": "DO", "homepage": "https://www.dos.pa.gov/ProfessionalLicensing/BoardsCommissions/OsteopathicMedicine/"},
    # Rhode Island
    {"state": "RI", "code": "RI_MD", "name": "Rhode Island Board of Medical Licensure and Discipline", "board_type": "combined", "homepage": "https://health.ri.gov/licenses/detail.php?id=201"},
    # South Carolina
    {"state": "SC", "code": "SC_MD", "name": "South Carolina Board of Medical Examiners", "board_type": "combined", "homepage": "https://llr.sc.gov/med/"},
    # South Dakota
    {"state": "SD", "code": "SD_MD", "name": "South Dakota Board of Medical and Osteopathic Examiners", "board_type": "combined", "homepage": "https://www.sdbmoe.gov"},
    # Tennessee
    {"state": "TN", "code": "TN_MD", "name": "Tennessee Board of Medical Examiners", "board_type": "MD", "homepage": "https://www.tn.gov/health/health-program-areas/health-professional-boards/me-board.html"},
    {"state": "TN", "code": "TN_DO", "name": "Tennessee Board of Osteopathic Examination", "board_type": "DO", "homepage": "https://www.tn.gov/health/health-program-areas/health-professional-boards/oe-board.html"},
    # Texas
    {"state": "TX", "code": "TX_MD", "name": "Texas Medical Board", "board_type": "combined", "homepage": "https://www.tmb.state.tx.us"},
    # Utah
    {"state": "UT", "code": "UT_MD", "name": "Utah Division of Occupational and Professional Licensing — Physicians", "board_type": "combined", "homepage": "https://dopl.utah.gov/physician/"},
    # Vermont
    {"state": "VT", "code": "VT_MD", "name": "Vermont Board of Medical Practice", "board_type": "combined", "homepage": "https://sos.vermont.gov/medical-board/"},
    # Virginia
    {"state": "VA", "code": "VA_MD", "name": "Virginia Board of Medicine", "board_type": "combined", "homepage": "https://www.dhp.virginia.gov/medicine/"},
    # Washington
    {"state": "WA", "code": "WA_MD", "name": "Washington Medical Commission", "board_type": "combined", "homepage": "https://wmc.wa.gov"},
    # West Virginia
    {"state": "WV", "code": "WV_MD", "name": "West Virginia Board of Medicine", "board_type": "MD", "homepage": "https://www.wvbom.wv.gov"},
    {"state": "WV", "code": "WV_DO", "name": "West Virginia Board of Osteopathic Medicine", "board_type": "DO", "homepage": "https://www.wvbdosteo.org"},
    # Wisconsin
    {"state": "WI", "code": "WI_MD", "name": "Wisconsin Medical Examining Board", "board_type": "combined", "homepage": "https://dsps.wi.gov/pages/BoardsCouncils/MEB/Default.aspx"},
    # Wyoming
    {"state": "WY", "code": "WY_MD", "name": "Wyoming Board of Medicine", "board_type": "combined", "homepage": "https://wyomedboard.wyo.gov"},
]
