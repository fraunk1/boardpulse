"""Prompt builder for the structured-facts extraction pipeline (facts-v1).

Clones the summarize pattern (app/extractor/prompts.py): this module builds
prompt bundle files that external Claude Code subagents consume — it never
calls an LLM itself. The output contract is validated at ingest by
app.quality.gates.check_facts, so every rule stated here is enforced by a
deterministic check on the way into the database.
"""
import json

from app.config import DATA_DIR
from app.quality.taxonomy import (
    CONFIDENCE, DISCIPLINE_CATEGORIES, INSTRUMENTS, INVOLVEMENTS, STAGES,
    TOPICS, TOPIC_DEFINITIONS,
)

# Per-document slice budget. Unlike the summary pipeline's head-only cap,
# facts need BOTH ends of a document: minutes front-load the agenda and
# votes, but the disciplinary action tables sit at the END. So each document
# keeps its head and tail with an explicit truncation marker between them.
FACTS_MAX_DOC_CHARS = 30_000
FACTS_DOC_HEAD_CHARS = 24_000
FACTS_DOC_TAIL_CHARS = 6_000
TRUNCATION_MARKER = "\n\n[... middle truncated ...]\n\n"

# Total per-CHUNK prompt budget (chars). Facts prompts carry the contract,
# taxonomy, and few-shot examples as fixed overhead, so the budget is lower
# than the summary pipeline's 480K. Boards that exceed it are split into
# multiple chunks on meeting boundaries (see facts.prepare_facts_bundles).
FACTS_MAX_PROMPT_CHARS = 360_000

# Few-shot example bank (authored separately). When the directory exists,
# every *.json inside is embedded verbatim as an example.
EXAMPLES_DIR = DATA_DIR / "examples" / "facts"


# The JSON contract, embedded verbatim in the prompt AND used as the single
# reference for gate checks and tests.
FACTS_CONTRACT = (
    '{"schema_version":"facts-v1","board_code":"XX_MD",'
    '"model":"<filled by agent>","meetings":[{"meeting_date":"YYYY-MM-DD",'
    '"policy_actions":[{instrument,stage,topic,title,description,'
    'rule_reference|null,action_date,quote|null,source_document,confidence}],'
    '"legislation":[{bill_number,bill_state,subject,topic|null,involvement,'
    'status_note|null,quote|null,source_document,confidence}],'
    '"disciplinary":[{category,count,quote|null,source_document,confidence}],'
    '"emerging_topics":[{topic_slug,subject,quote,source_document,'
    'confidence}]}]}'
)


def slice_doc_text(text: str) -> str:
    """HEAD+TAIL slice for one document's extracted text.

    Documents at or under FACTS_MAX_DOC_CHARS pass through untouched;
    longer ones keep the first FACTS_DOC_HEAD_CHARS and last
    FACTS_DOC_TAIL_CHARS with a visible truncation marker between.
    """
    if len(text) <= FACTS_MAX_DOC_CHARS:
        return text
    return (text[:FACTS_DOC_HEAD_CHARS] + TRUNCATION_MARKER
            + text[-FACTS_DOC_TAIL_CHARS:])


def render_meeting_section(meeting: dict) -> str:
    """Render one meeting's documents as a prompt section.

    Shared with facts.prepare_facts_bundles so the chunker measures exactly
    the text the prompt will contain.
    """
    header = (f"### {meeting['meeting_date']} — "
              f"{meeting.get('title') or 'Board Meeting'}")
    doc_texts = []
    for doc in meeting.get("documents", []):
        if doc.get("content_text"):
            label = f"[{doc['doc_type'].upper()}] {doc['filename']}"
            doc_texts.append(
                f"**{label}**\n\n{slice_doc_text(doc['content_text'])}")
    if doc_texts:
        return header + "\n\n" + "\n\n---\n\n".join(doc_texts)
    return header + "\n\n*(No extracted text available)*"


# ---------------------------------------------------------------------------
# Taxonomy rendering — one line per enum value, so a weak model sees a
# definition next to every value it is allowed to emit. The tuples come from
# app.quality.taxonomy; the definitions live here (prompt concern only).
# ---------------------------------------------------------------------------

_TOPIC_DEFS = {
    "licensing": "license applications, renewals, requirements, pathways",
    "disciplinary": "complaints, investigations, sanctions against licensees",
    "telehealth": "remote care delivery, telemedicine standards",
    "scope-of-practice": "what license holders may do; supervision, delegation",
    "rulemaking": "the board's own administrative-rule process",
    "legislation": "bills and statutes affecting the board",
    "opioids": "opioid prescribing, monitoring, treatment programs",
    "controlled-substances": "scheduled-drug regulation beyond opioids",
    "patient-safety": "safety standards, adverse events, reporting",
    "physician-wellness": "burnout, health programs, impairment support",
    "AI": "artificial intelligence in practice or board operations",
    "CME": "continuing medical education requirements",
    "IMLC": "Interstate Medical Licensure Compact matters",
    "workforce": "physician supply, shortages, workforce data",
    "public-health": "emergencies, immunization, population health",
    "other": "genuinely fits none of the above (the pressure valve)",
}

_INSTRUMENT_DEFS = {
    "rule": "an administrative regulation (has or gets a rule number)",
    "guidance": "non-binding guidance, FAQ, or interpretive document",
    "policy_statement": "a formal policy statement the board issued",
    "position": "a stance the board voted to take on an issue",
    "resolution": "a formal board resolution",
    "other": "a policy instrument that fits none of the above",
}

_STAGE_DEFS = {
    "discussed": "talked about; no formal procedural step taken",
    "proposed": "formally proposed or noticed",
    "comment_period": "open for public comment",
    "adopted": "formally adopted or approved",
    "amended": "an existing instrument was changed",
    "repealed": "rescinded or removed",
    "effective": "took legal effect",
    "tabled": "postponed to a later meeting",
    "withdrawn": "withdrawn from consideration",
}

_INVOLVEMENT_DEFS = {
    "monitoring": "the board is tracking the bill",
    "supporting": "the board expressed support",
    "opposing": "the board expressed opposition",
    "neutral": "the board took a formally neutral position",
    "testified": "board members or staff testified on the bill",
    "implementing": "the board is implementing an enacted law",
    "commented": "the board submitted formal comments",
    "other": "a relationship that fits none of the above",
}

_CATEGORY_DEFS = {
    "revocation": "license revoked",
    "suspension": "license suspended (any duration)",
    "probation": "licensee placed on probation",
    "reprimand": "formal reprimand, censure, or letter of concern",
    "fine": "monetary penalty or civil fine",
    "consent_order": "consent order / consent agreement / settlement",
    "surrender": "voluntary surrender or relinquishment of license",
    "reinstatement": "license or privileges reinstated",
    "denial": "application or reinstatement denied",
    "dismissal": "complaint or case dismissed / closed with no action",
    "other": "a disciplinary outcome that fits none of the above",
}

_CONFIDENCE_DEFS = {
    "high": "explicitly stated in the source text",
    "medium": "clearly implied by the source text",
    "low": "an uncertain reading of the source text",
}


def _render_vocab(name: str, values: tuple, defs: dict) -> str:
    lines = [f"### `{name}`"]
    for v in values:
        desc = defs.get(v, "")
        lines.append(f"- `{v}` — {desc}" if desc else f"- `{v}`")
    return "\n".join(lines)


def _taxonomy_block() -> str:
    return "\n\n".join([
        # topic defs come from the taxonomy so new topics stay in sync
        _render_vocab("topic", TOPICS, TOPIC_DEFINITIONS),
        _render_vocab("instrument (policy_actions)", INSTRUMENTS,
                      _INSTRUMENT_DEFS),
        _render_vocab("stage (policy_actions)", STAGES, _STAGE_DEFS),
        _render_vocab("involvement (legislation)", INVOLVEMENTS,
                      _INVOLVEMENT_DEFS),
        _render_vocab("category (disciplinary)", DISCIPLINE_CATEGORIES,
                      _CATEGORY_DEFS),
        _render_vocab("confidence", CONFIDENCE, _CONFIDENCE_DEFS),
    ])


def _few_shot_block() -> str:
    """Load the few-shot bank from data/examples/facts/*.json when present.

    The bank is authored separately; until it lands, the prompt carries a
    clearly-marked placeholder so nothing pretends examples exist.
    """
    if EXAMPLES_DIR.is_dir():
        parts = []
        for path in sorted(EXAMPLES_DIR.glob("*.json")):
            try:
                content = path.read_text(encoding="utf-8").strip()
                json.loads(content)  # only embed examples that are valid JSON
            except (OSError, json.JSONDecodeError):
                continue
            parts.append(f"### Example: {path.stem}\n\n```json\n{content}\n```")
        if parts:
            return ("The following worked examples show correct output "
                    "for real excerpts:\n\n" + "\n\n".join(parts))
    return ("*(FEW_SHOT PLACEHOLDER — the example bank at "
            "data/examples/facts/ has not been authored yet. Follow the "
            "contract, vocabularies, and hard rules above exactly.)*")


def fact_extraction_prompt(
    board: dict,
    meetings_payload: list[dict],
    chunk_note: str,
) -> str:
    """Build one facts-extraction prompt chunk.

    Args:
        board: dict with keys name, state, code.
        meetings_payload: list of dicts with keys meeting_date, title,
            documents (each doc: doc_type, filename, content_text — text is
            expected to already fit slice_doc_text, but is sliced again here
            defensively).
        chunk_note: chunk framing ("Chunk 2 of 3 ... write output to ...").
    """
    covered_lines = "\n".join(
        f"- `{m['meeting_date']}` — {m.get('title') or 'Board Meeting'}"
        for m in meetings_payload)

    sections = "\n\n---\n\n".join(
        render_meeting_section(m) for m in meetings_payload)

    return f"""# Structured Facts Extraction — {board['name']} ({board['state']})

You are an expert regulatory analyst extracting STRUCTURED FACTS from state
medical board meeting minutes. Your output is machine-readable JSON that is
ingested into a database only after strict deterministic validation — every
rule below is enforced by an automated gate, not a suggestion.

{chunk_note}

## Covered meetings

Every date listed here MUST appear in your output's "meetings" array (with
empty arrays if the meeting yields no facts):

{covered_lines}

## Output contract (schema_version "facts-v1")

Emit exactly this shape — four fact arrays per meeting:

```
{FACTS_CONTRACT}
```

Field notes:
- `policy_actions` — formal policy instruments the board moved on: rules,
  guidance, policy statements, positions, resolutions. `title` names the
  action in <= 200 characters; put detail in `description`. `rule_reference`
  is the rule/code number when one is given, else null. `action_date` is the
  date the action occurred (normally the meeting date, YYYY-MM-DD).
- `legislation` — bills the board discussed. `bill_number` exactly as written
  in the minutes (e.g. "SB 123", "HB 4001"); `bill_state` is the two-letter
  state code (or "US" for federal bills). `involvement` is the board's
  described relationship to the bill.
- `disciplinary` — per-meeting COUNTS of actions by outcome category.
  `count` is a non-negative integer. One entry per category per meeting.
  Disciplinary tables often sit at the END of the minutes — read to the end.
- `emerging_topics` — the first time this board discusses a genuinely NEW
  subject (not routine business). `topic_slug` is a short lowercase-hyphen
  slug (<= 60 chars, e.g. "ai-scribes"). Use sparingly.
- `source_document` — the exact filename (as shown in the [MINUTES]/[AGENDA]
  labels below) the fact came from.
- `confidence` — high/medium/low per the vocabulary below.
- Optional fields are `null`, never omitted and never `""`.
- Quotes are <= 400 characters each.

## Controlled vocabularies (use these EXACT values — anything else is rejected)

{_taxonomy_block()}

## Hard rules

1. every quote must be copied verbatim from the source text — an exact substring check rejects mismatches
2. every covered meeting MUST appear; empty arrays mean examined-nothing-found
3. never invent bill numbers
4. output ONLY the JSON object, no fences, no commentary
5. Use ONLY information contained in this file. Never invent facts, dates,
   counts, or rule numbers. When the text is ambiguous, prefer fewer facts
   at higher confidence over many facts at low confidence.
6. Emit at most 100 facts total in this file. Routine procedural meetings
   correctly produce empty arrays.

## Examples

{_few_shot_block()}

## Meeting minutes data

Board: {board['name']}
State: {board['state']}
Code: {board['code']}

{sections}
"""
