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
    "workforce", "public-health", "other",
)

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
PROMPT_VERSION = "facts-v1"


def _check(column: str, values: tuple[str, ...]) -> str:
    """Render a SQL CHECK clause for an enum column."""
    joined = ", ".join(f"'{v}'" for v in values)
    return f"{column} IN ({joined})"
