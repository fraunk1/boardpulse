"""Controlled vocabularies — the single source of truth.

Imported by the models (CHECK constraints), the prompt builders, and the
ingest gates, so the vocabulary a model is asked to use and the vocabulary
the database accepts can never drift apart. Extend deliberately: adding a
value here changes what every future extraction is allowed to say.
"""

# The 15 dashboard topic tags (used by meeting summaries AND fact rows),
# plus "other" as the pressure valve so models never invent tags.
TOPICS = (
    "licensing", "disciplinary", "telehealth", "scope-of-practice",
    "rulemaking", "legislation", "opioids", "controlled-substances",
    "patient-safety", "physician-wellness", "AI", "CME", "IMLC",
    "workforce", "public-health",
    # Added 2026-07-04 (Frank's expanded policy set):
    "reproductive-health", "gender-affirming-care", "IMG",
    "licensure-portability", "behavioral-health", "prescribing",
    "board-governance", "regulatory-innovation",
    "other",
)

# One-line definitions so the model applies each tag consistently. Keys must
# match TOPICS; used by the summary + fact prompts.
TOPIC_DEFINITIONS = {
    "licensing": "physician licensure, applications, renewals, requirements",
    "disciplinary": "board disciplinary actions, orders, complaints, hearings",
    "telehealth": "telemedicine, remote care, cross-state virtual practice",
    "scope-of-practice": "scope of practice for physicians, PAs, APRNs, other professions",
    "rulemaking": "board rules/regulations proposed, amended, or adopted",
    "legislation": "state or federal bills, statutes, legislative activity",
    "opioids": "opioid prescribing, addiction, overdose policy",
    "controlled-substances": "controlled-substance scheduling, DEA, dispensing",
    "patient-safety": "patient harm, safety standards, adverse events",
    "physician-wellness": "physician health/wellness, burnout, impairment programs",
    "AI": "artificial intelligence in medicine or board operations",
    "CME": "continuing medical education requirements",
    "IMLC": "the Interstate Medical Licensure Compact specifically",
    "workforce": "physician supply, shortages, distribution, retention",
    "public-health": "public-health emergencies, disease, vaccination, community health",
    "reproductive-health": "abortion, maternal/reproductive care rules and access",
    "gender-affirming-care": "gender-affirming or transgender care policy/rulemaking",
    "IMG": "international medical graduates — licensure pathways, requirements",
    "licensure-portability": "expedited, reciprocal, or portable licensure beyond the IMLC",
    "behavioral-health": "mental-health/psychiatric care, access, telepsychiatry",
    "prescribing": "prescriptive authority, PDMP, e-prescribing (not just scheduling)",
    "board-governance": "board elections, bylaws, budget, fees, staffing, administration",
    "regulatory-innovation": "novel regulatory frameworks, pilots, sandboxes, new licensure or oversight models",
    "other": "anything substantive not covered above",
}

# policy_actions: what kind of instrument the board acted on ...
INSTRUMENTS = (
    "rule", "guidance", "policy_statement", "position", "resolution", "other",
)

# ... and where in its lifecycle the action sits. instrument x stage is
# orthogonal on purpose: "rule adoptions" = instrument='rule' AND
# stage='adopted' — fewer values for a weak model to memorize.
STAGES = (
    "discussed", "proposed", "comment_period", "adopted", "amended",
    "repealed", "effective", "tabled", "withdrawn",
)

# legislation_mentions: the board's described relationship to a bill.
INVOLVEMENTS = (
    "monitoring", "supporting", "opposing", "neutral", "testified",
    "implementing", "commented", "other",
)

# disciplinary_actions: per-meeting counts by outcome category.
DISCIPLINE_CATEGORIES = (
    "revocation", "suspension", "probation", "reprimand", "fine",
    "consent_order", "surrender", "reinstatement", "denial",
    "dismissal", "other",
)

CONFIDENCE = ("high", "medium", "low")

# Bumped only when the extraction contract itself changes shape.
PROMPT_VERSION = "facts-v2"


def _check(column: str, values: tuple[str, ...]) -> str:
    """Render a SQL CHECK clause for an enum column."""
    joined = ", ".join(f"'{v}'" for v in values)
    return f"{column} IN ({joined})"
