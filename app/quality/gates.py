"""Summary ingest gate — deterministic checks run BEFORE a subagent-written
*_summary.md file is allowed into the database.

Design rules:
  * check_summary() is PURE — no DB access. Callers query the date sets and
    source texts and pass them in, so the same gate runs identically from
    ingest (async SQLAlchemy), the _validate_summaries.py audit (sync
    sqlite3), and unit tests (no DB at all).
  * Every error message is written for a RETRY AGENT: it says what is wrong,
    what to change, and lists the valid values/dates.
  * Bands are deliberately wider than the authoring contract in
    prompts.per_board_prompt (300-600 word rollup, 80-200 word blocks) so a
    near-miss summary doesn't retry-loop. The bands were calibrated against
    the 57 real summary files in data/reports/ — those files are ground
    truth and must always pass.

Calibration notes (2026-07-03, against the live DB):
  * Block word floor is 25, not the spec'd 40 — real files contain
    legitimate 29-38 word blocks for short procedural meetings
    (VA_MD 2025-10-31 = 29w, MT_MD 2025-12-05 = 30w).
  * GHOST_BLOCK demotes to a warning when the block's date is a real
    meeting that has slid OUT of the rolling 365-day window since the
    summary was written (IL_MD 2025-07-02: in-window at generation time,
    out-of-window one day later). A truly fabricated date is still hard.
  * MISSING_BLOCK is a WARNING, never hard. The 2026-07 archive backfill
    added extracted text to window meetings on 9 boards AFTER their
    summaries were written (CA_MD now "misses" 9 of its 10 text dates;
    RI_MD 16 of 31), and summarizers also legitimately skip agenda-only
    meetings (IL_MD skips 5 of 24). A missing block puts no false data in
    the database — the meeting simply stays unsummarized — so staleness is
    a re-summarization trigger, not a rejection. Hard errors are reserved
    for content that would ingest WRONG data (ghost dates, unverifiable
    names, bad topics, format breaks).
  * NAME_CHECK falls back to the board-wide source corpus when a surname
    isn't in that block's own date text — collectors sometimes register a
    combined PDF under one meeting date, so a real name can verify against
    a neighboring meeting's document (12 such blocks in the real files,
    all names present board-wide).
"""
import json
import re
from dataclasses import dataclass, field
from urllib.parse import urlparse

from app.quality.taxonomy import (
    CONFIDENCE, DISCIPLINE_CATEGORIES, INSTRUMENTS, INVOLVEMENTS,
    PROMPT_VERSION, STAGES, TOPICS,
)


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------

@dataclass
class GateError:
    code: str
    message: str


@dataclass
class GateResult:
    ok: bool
    errors: list[GateError] = field(default_factory=list)
    warnings: list[GateError] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Normalization — cost-free auto-repairs only (nothing that could change
# meaning): BOM, wrapping code fences, outer whitespace.
# ---------------------------------------------------------------------------

_FENCE_OPEN_RE = re.compile(r"^```[a-zA-Z]*[ \t]*\r?\n")
_FENCE_CLOSE_RE = re.compile(r"\r?\n```[ \t]*$")


def normalize_summary(text: str) -> str:
    """Strip wrapping ```markdown fences, BOM, and trailing whitespace."""
    text = (text or "").lstrip("﻿").strip()
    if _FENCE_OPEN_RE.match(text) and _FENCE_CLOSE_RE.search(text):
        text = _FENCE_OPEN_RE.sub("", text, count=1)
        text = _FENCE_CLOSE_RE.sub("", text, count=1)
        text = text.strip()
    return text


# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
_END_RE = re.compile(r"^\s*={2,}\s*END\s*={2,}\s*$", re.MULTILINE)
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Any markdown link into the dashboard: bracket text + /board/... target.
_BOARD_LINK_RE = re.compile(r"\[([^\]]*)\]\((/board/[^)\s]*)\)")
# Any #YYYY-MM-DD anchor (catches ghosts even in malformed citations).
_ANCHOR_RE = re.compile(r"#(\d{4}-\d{2}-\d{2})")
# The Sources table heading, as written in the real files ("## Sources").
_SOURCES_SPLIT_RE = re.compile(r"^\s{0,3}#{1,6}\s*Sources\b.*$", re.MULTILINE)
_HTTP_URL_RE = re.compile(r"https?://[^)\s|\]>]+")

# Clinician names: "First [Middle...] Last, MD|DO|PA" (dots optional) ...
_CRED_NAME_RE = re.compile(
    r"((?:[A-Z][\w.'-]+ ){1,3}[A-Z][\w.'-]+),?\s*"
    r"(M\.?D\.?|D\.?O\.?|P\.?A\.?)(?![\w])")
# ... plus "Dr. Lastname" / "Drs. Lastname".
_DR_NAME_RE = re.compile(r"\bDrs?\.?\s+([A-Z][\w'’-]+)")

# S9 numerics: standalone runs of 4+ digits (not part of a YYYY-MM-DD or a
# hyphenated case number) and N% percentages.
_BIG_NUM_RE = re.compile(r"(?<![\d.\-/])(\d{4,})(?![\d\-/])")
_PCT_RE = re.compile(r"(?<![\d.])(\d+(?:\.\d+)?)\s?%")

_REFUSAL_STRINGS = (
    "No extracted text available", "As an AI", "I cannot", "I'm sorry",
)

# Bands (see calibration notes in the module docstring).
ROLLUP_WORDS = (150, 900)
BLOCK_WORDS = (25, 350)
NAME_FAIL_MIN_UNMATCHED = 2
NAME_FAIL_FRACTION = 0.30


def _host(url: str) -> str:
    h = (urlparse(url).netloc or "").lower()
    return h.split(":")[0]


def _strip_www(host: str) -> str:
    return host[4:] if host.startswith("www.") else host


def _hosts_compatible(candidate: str, references: set[str]) -> bool:
    """True if candidate host matches any reference host, accepting
    subdomains in either direction (commerce.alaska.gov ~ alaska.gov)."""
    c = _strip_www(candidate)
    for ref in references:
        r = _strip_www(ref)
        if c == r or c.endswith("." + r) or r.endswith("." + c):
            return True
    return False


def _extract_surnames(block_md: str) -> list[str]:
    """Pull verifiable clinician surnames out of a meeting block."""
    names: list[str] = []
    for m in _CRED_NAME_RE.finditer(block_md):
        names.append(m.group(1).split()[-1])
    for m in _DR_NAME_RE.finditer(block_md):
        names.append(m.group(1))
    cleaned: list[str] = []
    for n in names:
        # strip possessives ("Paisley's") and trailing punctuation
        n = re.sub(r"[’']s$", "", n).strip(".,'’-")
        if len(n) >= 2 and n not in cleaned:
            cleaned.append(n)
    return cleaned


# ---------------------------------------------------------------------------
# The gate
# ---------------------------------------------------------------------------

def check_summary(
    board_code: str,
    text: str,
    *,
    state: str,
    db_text_dates: set[str],
    db_all_dates: set[str],
    source_texts_by_date: dict[str, str],
    minutes_url: str | None,
    homepage: str | None,
    mode: str = "rollup",
) -> GateResult:
    """Run every gate check against a normalized summary file.

    Pure function: callers supply the DB-derived inputs.
      db_text_dates        meeting dates (ISO) in the 12-month window that
                           have at least one document with extracted text.
                           In archive mode this is the set the file's blocks
                           are checked against (the sidecar covered dates).
      db_all_dates         every meeting date the board has, any window
      source_texts_by_date concatenated document text per window date
      minutes_url/homepage the board's registered URLs (Sources host check)
      mode                 'rollup' (default) runs the full two-layer gate:
                           frontmatter, rollup citations, Sources table,
                           rollup length, ghost citations, plus every
                           per-block check. 'archive' is for a rollup-less
                           archive file — it SKIPS the rollup-only checks
                           (frontmatter requirement, citation format, Sources
                           table, rollup length, ghost citations) and keeps
                           the block-level checks: END terminator, blocks vs
                           covered dates (S2), block length bands (S4), topics
                           (S7), name verification (S8), and refusal (S10).
                           Default 'rollup' keeps all existing behavior
                           unchanged.
    """
    # Local import: summarizer imports this module for ingest wiring, so the
    # reverse import must happen at call time to avoid a cycle.
    from app.extractor.summarizer import parse_board_summary_file

    archive = mode == "archive"

    errors: list[GateError] = []
    warnings: list[GateError] = []
    text = text or ""
    valid_text_dates = ", ".join(sorted(db_text_dates)) or "(none)"

    # --- S1 STRUCTURE ------------------------------------------------------
    # Archive files carry NO frontmatter (no rollup layer), so the
    # frontmatter requirement is skipped for them; the END terminator and
    # per-meeting blocks are still required.
    if not archive:
        fm_match = _FRONTMATTER_RE.match(text)
        if not fm_match:
            errors.append(GateError(
                "STRUCTURE",
                "Missing YAML frontmatter. The file must start with a '---' "
                "block containing 'topics: [...]', 'board: <code>' and "
                "'state: <ST>' lines."))
        else:
            fm = fm_match.group(1)
            for key in ("topics", "board", "state"):
                if not re.search(rf"^{key}\s*:", fm, re.MULTILINE):
                    errors.append(GateError(
                        "STRUCTURE",
                        f"Frontmatter is missing the '{key}:' key. Required "
                        "keys: topics, board, state."))
            bm = re.search(r"^board\s*:\s*(.+?)\s*$", fm, re.MULTILINE)
            if bm and bm.group(1).strip("\"'") != board_code:
                errors.append(GateError(
                    "STRUCTURE",
                    f"Frontmatter 'board:' is '{bm.group(1).strip()}' but "
                    f"this file is for board {board_code}. Set board: "
                    f"{board_code}."))

    if not _END_RE.search(text):
        errors.append(GateError(
            "STRUCTURE",
            "File does not contain the '=== END ===' terminator. Append "
            "'=== END ===' on its own line after the last meeting block."))

    board_topics, rollup, sections = parse_board_summary_file(text)

    if not sections:
        if archive:
            errors.append(GateError(
                "STRUCTURE",
                "No '=== MEETING: YYYY-MM-DD ===' blocks found. An archive "
                "file is per-meeting blocks only: one '=== MEETING: date "
                "===' block per covered meeting date "
                f"({valid_text_dates}), ending with '=== END ==='."))
        else:
            errors.append(GateError(
                "LEGACY_FORMAT",
                "No '=== MEETING: YYYY-MM-DD ===' blocks found — this is the "
                "legacy single-blob format. Rewrite using the two-layer "
                "contract: a 12-month rollup, then one '=== MEETING: date "
                "===' "
                f"block per text-bearing meeting date ({valid_text_dates}), "
                "ending with '=== END ==='."))
        # Block-level checks are meaningless without blocks.
        return GateResult(ok=False, errors=errors, warnings=warnings)

    # --- S2 BLOCKS vs DB text dates -----------------------------------------
    # In archive mode db_text_dates == the sidecar covered_dates, so this is
    # "blocks vs covered dates". In rollup mode it is the 12-month text dates.
    block_dates = set(sections)
    min_text_date = min(db_text_dates) if db_text_dates else None
    for d in sorted(block_dates - db_text_dates):
        if d in db_all_dates and min_text_date and d < min_text_date:
            # Real meeting that slid out of the rolling 365-day window
            # after the summary was written — harmless, ingest ignores it.
            warnings.append(GateError(
                "GHOST_BLOCK",
                f"Block dated {d} is a real meeting but now falls outside "
                "the 12-month window (window drift). It will be ignored at "
                "ingest; drop it on the next regeneration. Valid dates: "
                f"{valid_text_dates}."))
        else:
            errors.append(GateError(
                "GHOST_BLOCK",
                f"Block dated {d} does not match any covered meeting date. "
                "Remove it or re-date it to one of "
                f"the valid dates: {valid_text_dates}."))

    missing = sorted(db_text_dates - block_dates)
    if missing:
        # Warning, never hard: text routinely lands AFTER a summary was
        # written (archive backfills, fresh extract passes), and nothing
        # false enters the DB — the meeting just stays unsummarized. The
        # refresh pipeline treats this as its re-summarization trigger.
        warnings.append(GateError(
            "MISSING_BLOCK",
            f"{len(missing)} covered meeting date(s) have no "
            f"'=== MEETING: date ===' block: {', '.join(missing)}. "
            "Re-summarize this board to cover them (an agenda-only note is "
            f"acceptable). Valid dates: {valid_text_dates}."))

    # --- S3 + S5 rollup citations (rollup mode only) ------------------------
    if not archive:
        expected_path = f"/board/{state}/{board_code}"
        well_formed = 0
        for bracket, target in _BOARD_LINK_RE.findall(rollup):
            anchor_m = re.search(r"#(\d{4}-\d{2}-\d{2})$", target)
            anchor = anchor_m.group(1) if anchor_m else None
            base = target.split("#")[0]
            if (not _DATE_RE.match(bracket) or base != expected_path
                    or anchor != bracket):
                errors.append(GateError(
                    "CITATION_FORMAT",
                    f"Malformed citation '[{bracket}]({target})'. Every "
                    "rollup citation must be ([YYYY-MM-DD](" + expected_path +
                    "#YYYY-MM-DD)) with the SAME date in the brackets and the "
                    "anchor."))
            else:
                well_formed += 1

        for a in sorted(set(_ANCHOR_RE.findall(rollup)) - db_all_dates):
            errors.append(GateError(
                "GHOST_CITATION",
                f"Citation anchor #{a} does not match any meeting this board "
                "has in the database. Cite only real meeting dates: "
                f"{', '.join(sorted(db_all_dates)) or '(none)'}."))

        need = min(3, len(db_text_dates))
        if well_formed < need:
            errors.append(GateError(
                "CITATION_FORMAT",
                f"Rollup has only {well_formed} well-formed citation(s); at "
                f"least {need} required. Add citations in the form "
                f"([YYYY-MM-DD]({expected_path}#YYYY-MM-DD)) for claims drawn "
                f"from specific meetings ({valid_text_dates})."))

    # --- S4 LENGTH + S6 SOURCES ----------------------------------------------
    # Rollup length + Sources table are rollup-only; block bands run always.
    if not archive:
        parts = _SOURCES_SPLIT_RE.split(rollup, maxsplit=1)
        prose = parts[0]
        rollup_words = len(prose.split())
        lo, hi = ROLLUP_WORDS
        if not lo <= rollup_words <= hi:
            errors.append(GateError(
                "LENGTH",
                f"Rollup is {rollup_words} words (excluding the Sources "
                f"table); it must be {lo}-{hi}. Target 300-600 words of "
                "cited narrative."))

    blo, bhi = BLOCK_WORDS
    for d in sorted(sections):
        block_words = len(sections[d][0].split())
        if not blo <= block_words <= bhi:
            errors.append(GateError(
                "LENGTH",
                f"Meeting block {d} is {block_words} words; each block must "
                f"be {blo}-{bhi}. Target 80-200 words summarizing only that "
                "meeting."))

    if not archive:
        if len(parts) == 1:
            errors.append(GateError(
                "SOURCES",
                "Rollup has no '## Sources' section. End the rollup with a "
                "'## Sources' markdown table (| # | Date | Board | Source |) "
                "with one row per meeting, linking to the board's minutes "
                "page."))
        else:
            tail = parts[1]
            data_rows = [ln for ln in tail.splitlines()
                         if ln.strip().startswith("|")
                         and re.search(r"\d{4}-\d{2}-\d{2}|https?://", ln)]
            if not data_rows:
                errors.append(GateError(
                    "SOURCES",
                    "The '## Sources' section has no table rows. Add at "
                    "least one row: | 1 | YYYY-MM-DD | Board name | [Minutes "
                    "page](URL) |."))
            ref_hosts = {h for h in (_host(u) for u in (minutes_url, homepage)
                                     if u) if h}
            if ref_hosts:
                for url in _HTTP_URL_RE.findall(tail):
                    h = _host(url)
                    if h and not _hosts_compatible(h, ref_hosts):
                        errors.append(GateError(
                            "SOURCE_HOST",
                            f"Sources URL host '{h}' does not belong to this "
                            "board. Use the board's own site(s): "
                            f"{', '.join(sorted(ref_hosts))}."))

    # --- S7 TOPICS ------------------------------------------------------------
    valid_topics = ", ".join(TOPICS)
    for t in board_topics:
        if t not in TOPICS:
            errors.append(GateError(
                "BAD_TOPIC",
                f"Frontmatter topic '{t}' is not in the taxonomy. Valid "
                f"values: {valid_topics}."))
    union: set[str] = set()
    for d in sorted(sections):
        block_topics = sections[d][1]
        union.update(block_topics)
        for t in block_topics:
            if t not in TOPICS:
                errors.append(GateError(
                    "BAD_TOPIC",
                    f"Meeting block {d} topic '{t}' is not in the taxonomy. "
                    f"Valid values: {valid_topics}."))
    # Archive files have no frontmatter, so there is no frontmatter-vs-block
    # union to reconcile — skip the TOPIC_UNION reconciliation for them.
    if not archive and set(board_topics) != union:
        extra = sorted(set(board_topics) - union)
        missing_t = sorted(union - set(board_topics))
        warnings.append(GateError(
            "TOPIC_UNION",
            "Frontmatter topics should be the union of the per-block "
            f"topics. Not in any block: {extra or '[]'}; in blocks but not "
            f"frontmatter: {missing_t or '[]'}."))

    # --- S8 NAME_CHECK + S9 NUMERIC + S10 REFUSAL ------------------------------
    corpus_lower = "\n".join(source_texts_by_date.values()).lower()
    for d in sorted(sections):
        block_md = sections[d][0]

        for s in _REFUSAL_STRINGS:
            if s in block_md:
                errors.append(GateError(
                    "REFUSAL",
                    f"Meeting block {d} contains the refusal/placeholder "
                    f"text '{s}'. Blocks must contain only a genuine "
                    "summary of that meeting's documents; omit blocks with "
                    "nothing to summarize only if the meeting has no "
                    "extracted text."))

        source = source_texts_by_date.get(d)
        if not source:
            continue  # no source text for this date — never false-reject
        source_lower = source.lower()

        names = _extract_surnames(block_md)
        if names:
            unmatched = [
                n for n in names
                if n.lower() not in source_lower
                and n.lower() not in corpus_lower]
            if (len(unmatched) >= NAME_FAIL_MIN_UNMATCHED
                    or len(unmatched) / len(names) > NAME_FAIL_FRACTION):
                errors.append(GateError(
                    "NAME_CHECK",
                    f"Meeting block {d} names clinician(s) not found in any "
                    f"of this board's source documents: "
                    f"{', '.join(unmatched)} "
                    f"({len(unmatched)}/{len(names)} unverifiable). Only "
                    "name people who appear in the source text for that "
                    "meeting."))

        for num in sorted(set(_BIG_NUM_RE.findall(block_md))):
            if num not in source and num not in corpus_lower:
                warnings.append(GateError(
                    "NUMERIC",
                    f"Meeting block {d} contains the number '{num}' which "
                    "does not appear in that date's source text. Verify it "
                    "against the documents."))
        for pct in sorted(set(_PCT_RE.findall(block_md))):
            if pct not in source:
                warnings.append(GateError(
                    "NUMERIC",
                    f"Meeting block {d} cites '{pct}%' which does not "
                    "appear in that date's source text. Verify it against "
                    "the documents."))

    # --- S10 REFUSAL: instruction echo in the rollup ---------------------------
    # Rollup-only: archive files have no rollup, so there is nothing to echo.
    if not archive and ("Output Format" in rollup or "=== MEETING:" in rollup):
        errors.append(GateError(
            "REFUSAL",
            "The rollup echoes the prompt instructions ('Output Format' / "
            "'=== MEETING:' found inside the rollup). Write only the "
            "12-month narrative and Sources table in the rollup; meeting "
            "blocks belong after it, delimited by '=== MEETING: date ==='."))

    return GateResult(ok=not errors, errors=errors, warnings=warnings)


# ===========================================================================
# Gate F — structured-facts ingest gate (facts-v1)
#
# Same design rules as Gate S above: check_facts() is PURE (no DB access —
# callers pass the covered dates, the board's text-bearing dates, and the
# source texts), and every error message is written for a RETRY AGENT: what
# is wrong, what to change, and the valid values.
#
# One deliberate impurity: F5 downgrades a mismatched quote's confidence to
# 'low' IN PLACE on the parsed dict the caller passed (plus a warning), so
# the ingest that follows stores the downgraded value. That is the only
# mutation this gate performs, and it never changes fact content — only the
# model's self-reported confidence.
# ===========================================================================

_FACTS_TOP_KEYS = ("schema_version", "board_code", "model", "meetings")
_FACT_ARRAYS = ("policy_actions", "legislation", "disciplinary",
                "emerging_topics")

FACTS_TITLE_MAX = 200
FACTS_QUOTE_MAX = 400
FACTS_SLUG_MAX = 60          # emerging_topics.topic_slug column width
FACTS_BILL_NUMBER_MAX = 60   # bill numbers vary (compound refs, prefixes);
#                              SQLite ignores the String(30) column hint
FACTS_RULE_REF_MAX = 120     # policy_actions.rule_reference column width
FACTS_RESPONDENT_MAX = 200   # disciplinary_actions.respondent column width
# facts-v2 itemizes disciplinary actions (one entry per case), so a
# discipline-heavy chunk legitimately carries hundreds of facts. The cap is
# an anti-spam backstop, not a target.
FACTS_MAX_PER_FILE = 500
QUOTE_MISMATCH_MAX_FRACTION = 0.30

_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_BILL_STATE_RE = re.compile(r"^[A-Z]{2}$")

# (field, nullable) per fact type. 'count' is checked separately (int).
_POLICY_FIELDS = (
    ("instrument", False), ("stage", False), ("topic", False),
    ("title", False), ("description", False), ("rule_reference", True),
    ("action_date", False), ("quote", True), ("source_document", False),
    ("confidence", False),
)
_LEGISLATION_FIELDS = (
    ("bill_number", False), ("bill_state", False), ("subject", False),
    ("topic", True), ("involvement", False), ("status_note", True),
    ("quote", True), ("source_document", False), ("confidence", False),
)
# facts-v2: respondent nullable (null = bulk entry); quote REQUIRED — each
# disciplinary entry anchors on a verbatim quote, hard-checked like
# emerging_topics.
_DISCIPLINARY_FIELDS = (
    ("category", False), ("respondent", True), ("quote", False),
    ("source_document", False), ("confidence", False),
)
_EMERGING_FIELDS = (
    ("topic_slug", False), ("subject", False), ("quote", False),
    ("source_document", False), ("confidence", False),
)


def _ws(text) -> str:
    """Whitespace-normalize: collapse all runs of whitespace to one space."""
    return " ".join(str(text or "").split())


# Number words a quote might use instead of a digit — for the bulk-entry
# rule (a count >= 2 must be visible in its own quote). Shared with the
# provenance audit (app.quality.audit).
NUM_WORDS = {
    2: ("two", "both"), 3: ("three",), 4: ("four",), 5: ("five",),
    6: ("six",), 7: ("seven",), 8: ("eight",), 9: ("nine",), 10: ("ten",),
    11: ("eleven",), 12: ("twelve",), 13: ("thirteen",), 14: ("fourteen",),
    15: ("fifteen",), 16: ("sixteen",), 17: ("seventeen",), 18: ("eighteen",),
    19: ("nineteen",), 20: ("twenty",),
}


def count_visible(count: int, quote: str) -> bool:
    """True when a numeric count is visible in the quote — as a digit string
    or a number word. The anchor for bulk disciplinary entries."""
    q = _ws(quote).lower()
    if str(count) in q:
        return True
    return any(w in q for w in NUM_WORDS.get(count, ()))


def _check_fields(
    fact: dict, spec, where: str, errors: list,
) -> bool:
    """F2 for one fact: required keys present, string/None types, caps.

    Returns True when the fact is structurally sound enough for the
    content checks (F4-F6) to run on it.
    """
    if not isinstance(fact, dict):
        errors.append(GateError(
            "FIELD",
            f"{where} is {type(fact).__name__}, not an object. Each fact "
            "must be a JSON object with the contract's fields."))
        return False
    ok = True
    for key, nullable in spec:
        if key not in fact:
            errors.append(GateError(
                "FIELD",
                f"{where} is missing required key '{key}'. Optional fields "
                "must be null, never omitted."))
            ok = False
            continue
        val = fact[key]
        if val is None:
            if not nullable:
                errors.append(GateError(
                    "FIELD",
                    f"{where} has null '{key}' but that field is required. "
                    "Fill it from the source text or drop the fact."))
                ok = False
            continue
        if not isinstance(val, str):
            errors.append(GateError(
                "FIELD",
                f"{where} field '{key}' is {type(val).__name__}, not a "
                "string. All contract fields are strings (or null where "
                "the contract says |null)."))
            ok = False
            continue
        if not nullable and not val.strip():
            errors.append(GateError(
                "FIELD",
                f"{where} field '{key}' is an empty string. Required "
                "fields must carry real content."))
            ok = False
    # length caps (only when the value is a string)
    caps = (("title", FACTS_TITLE_MAX), ("quote", FACTS_QUOTE_MAX),
            ("topic_slug", FACTS_SLUG_MAX),
            ("bill_number", FACTS_BILL_NUMBER_MAX),
            ("rule_reference", FACTS_RULE_REF_MAX),
            ("respondent", FACTS_RESPONDENT_MAX))
    for key, cap in caps:
        val = fact.get(key)
        if isinstance(val, str) and len(val) > cap:
            hint = (" Move detail into 'description'." if key == "title"
                    else " Quote a shorter span." if key == "quote" else "")
            errors.append(GateError(
                "FIELD",
                f"{where} field '{key}' is {len(val)} chars; the cap is "
                f"{cap}.{hint}"))
            ok = False
    return ok


def _check_enum(
    fact: dict, key: str, values: tuple, where: str, errors: list,
    *, nullable: bool = False,
) -> None:
    """F4 for one enum field (skips values F2 already rejected)."""
    val = fact.get(key)
    if val is None and nullable:
        return
    if isinstance(val, str) and val not in values:
        errors.append(GateError(
            "BAD_ENUM",
            f"{where} {key} '{val}' is not in the taxonomy. Valid values: "
            f"{', '.join(values)}."))


def check_facts(
    board_code: str,
    data,
    *,
    covered_dates: set[str],
    db_text_dates: set[str],
    source_texts_by_date: dict[str, str],
) -> GateResult:
    """Run every Gate F check against a facts-v1 extraction file.

    Pure function: callers supply the DB-derived inputs.
      data                  the parsed JSON dict — or the raw file text
                            (str), which is normalized and parsed here.
                            Pass the DICT when you intend to ingest: the F5
                            confidence downgrade mutates it in place.
      covered_dates         meeting dates (ISO) this prompt chunk covered,
                            from the {code}_{NN}_facts_prompt.meta.json
                            sidecar
      db_text_dates         this board's meeting dates (ISO) that have at
                            least one document with extracted text
      source_texts_by_date  concatenated document text per meeting date
    """
    errors: list[GateError] = []
    warnings: list[GateError] = []

    # --- F1 JSON + top-level structure --------------------------------------
    if isinstance(data, str):
        try:
            data = json.loads(normalize_summary(data))
        except json.JSONDecodeError as exc:
            errors.append(GateError(
                "BAD_JSON",
                f"File is not valid JSON ({exc.msg} at line {exc.lineno}). "
                "Output ONLY the JSON object — no fences, no commentary, "
                "no trailing text."))
            return GateResult(ok=False, errors=errors, warnings=warnings)

    if not isinstance(data, dict):
        errors.append(GateError(
            "STRUCTURE",
            f"Top level is {type(data).__name__}, not an object. The file "
            "must be a single JSON object per the facts-v1 contract."))
        return GateResult(ok=False, errors=errors, warnings=warnings)

    expected = set(_FACTS_TOP_KEYS)
    actual = set(data)
    for k in sorted(expected - actual):
        errors.append(GateError(
            "STRUCTURE",
            f"Missing top-level key '{k}'. The top level must have exactly: "
            f"{', '.join(_FACTS_TOP_KEYS)}."))
    for k in sorted(actual - expected):
        errors.append(GateError(
            "STRUCTURE",
            f"Unexpected top-level key '{k}'. The top level must have "
            f"exactly: {', '.join(_FACTS_TOP_KEYS)}."))

    if data.get("schema_version") != PROMPT_VERSION:
        errors.append(GateError(
            "STRUCTURE",
            f"schema_version is '{data.get('schema_version')}' but this "
            f"gate accepts only '{PROMPT_VERSION}'. Set schema_version: "
            f"{PROMPT_VERSION}."))
    if data.get("board_code") != board_code:
        errors.append(GateError(
            "STRUCTURE",
            f"board_code is '{data.get('board_code')}' but this file is "
            f"for board {board_code}. Set board_code: {board_code}."))

    meetings = data.get("meetings")
    if not isinstance(meetings, list):
        errors.append(GateError(
            "STRUCTURE",
            "'meetings' must be an array of meeting objects (one per "
            "covered meeting date)."))
        return GateResult(ok=False, errors=errors, warnings=warnings)

    valid_dates = ", ".join(
        sorted(covered_dates & db_text_dates)) or "(none)"
    norm_sources = {d: _ws(t) for d, t in source_texts_by_date.items()}

    total_facts = 0
    quote_checked = 0
    quote_mismatched = 0
    seen_keys: set[tuple] = set()
    json_dates: set[str] = set()

    for mi, mrec in enumerate(meetings):
        if not isinstance(mrec, dict):
            errors.append(GateError(
                "STRUCTURE",
                f"meetings[{mi}] is {type(mrec).__name__}, not an object."))
            continue

        d = mrec.get("meeting_date")
        if not isinstance(d, str) or not _ISO_DATE_RE.match(d):
            errors.append(GateError(
                "STRUCTURE",
                f"meetings[{mi}] meeting_date '{d}' is not a YYYY-MM-DD "
                f"date. Use one of the covered dates: {valid_dates}."))
            continue
        json_dates.add(d)

        # --- F3 date must be covered by the chunk AND text-bearing in DB ---
        if d not in covered_dates or d not in db_text_dates:
            where_bad = ("this prompt chunk" if d not in covered_dates
                         else "the board's text-bearing meetings")
            errors.append(GateError(
                "GHOST_MEETING",
                f"Meeting date {d} does not match {where_bad}. Extract "
                f"facts only for the covered dates: {valid_dates}."))
            continue

        missing_arrays = [k for k in _FACT_ARRAYS
                          if not isinstance(mrec.get(k), list)]
        if missing_arrays:
            errors.append(GateError(
                "STRUCTURE",
                f"Meeting {d} is missing fact array(s): "
                f"{', '.join(missing_arrays)}. Every meeting carries all "
                f"four arrays ({', '.join(_FACT_ARRAYS)}); empty arrays "
                "mean examined-nothing-found."))
            continue

        source = norm_sources.get(d, "")

        def _quote_ok(quote: str) -> bool:
            # Never false-reject when a date has no source text on file.
            return not source or _ws(quote) in source

        def _subject_check(fact: dict, where: str) -> None:
            # F6: the subject should be traceable to the quote or the text.
            subject = fact.get("subject")
            if not isinstance(subject, str) or not subject.strip():
                return
            hay = (_ws(fact.get("quote")) + " " + source).lower()
            if _ws(subject).lower() not in hay:
                warnings.append(GateError(
                    "SUBJECT_CHECK",
                    f"{where} subject '{subject}' does not appear in its "
                    "quote or in that meeting's source text. Verify it "
                    "against the documents."))

        # --- policy_actions -------------------------------------------------
        for i, fact in enumerate(mrec["policy_actions"]):
            where = f"Meeting {d} policy_actions[{i}]"
            total_facts += 1
            if not _check_fields(fact, _POLICY_FIELDS, where, errors):
                continue
            _check_enum(fact, "instrument", INSTRUMENTS, where, errors)
            _check_enum(fact, "stage", STAGES, where, errors)
            _check_enum(fact, "topic", TOPICS, where, errors)
            _check_enum(fact, "confidence", CONFIDENCE, where, errors)
            ad = fact.get("action_date")
            if isinstance(ad, str) and not _ISO_DATE_RE.match(ad):
                errors.append(GateError(
                    "FIELD",
                    f"{where} action_date '{ad}' is not a YYYY-MM-DD date. "
                    "Use the date the action occurred (normally the "
                    "meeting date)."))
            key = ("policy", d, fact.get("instrument"), fact.get("stage"),
                   fact.get("topic"), _ws(fact.get("title")).lower())
            if key in seen_keys:
                errors.append(GateError(
                    "DUPLICATE_FACT",
                    f"{where} duplicates another policy action in this "
                    "file (same meeting, instrument, stage, topic, and "
                    "title). Merge them into one fact."))
            seen_keys.add(key)
            quote = fact.get("quote")
            if isinstance(quote, str) and quote.strip():
                quote_checked += 1
                if not _quote_ok(quote):
                    quote_mismatched += 1
                    fact["confidence"] = "low"
                    warnings.append(GateError(
                        "QUOTE_MISMATCH",
                        f"{where} quote is not a verbatim substring of "
                        "that meeting's source text — confidence forced "
                        "to 'low'. Copy quotes exactly from the source."))

        # --- legislation ----------------------------------------------------
        for i, fact in enumerate(mrec["legislation"]):
            where = f"Meeting {d} legislation[{i}]"
            total_facts += 1
            if not _check_fields(fact, _LEGISLATION_FIELDS, where, errors):
                continue
            _check_enum(fact, "involvement", INVOLVEMENTS, where, errors)
            _check_enum(fact, "topic", TOPICS, where, errors, nullable=True)
            _check_enum(fact, "confidence", CONFIDENCE, where, errors)
            bs = fact.get("bill_state")
            if isinstance(bs, str) and not _BILL_STATE_RE.match(bs):
                errors.append(GateError(
                    "FIELD",
                    f"{where} bill_state '{bs}' must be a two-letter "
                    "uppercase code ('US' for federal bills)."))
            key = ("legislation", d, _ws(fact.get("bill_number")).lower(),
                   (fact.get("bill_state") or "").upper())
            if key in seen_keys:
                errors.append(GateError(
                    "DUPLICATE_FACT",
                    f"{where} duplicates another mention of bill "
                    f"{fact.get('bill_number')} at this meeting. Merge "
                    "them into one fact."))
            seen_keys.add(key)
            quote = fact.get("quote")
            if isinstance(quote, str) and quote.strip():
                quote_checked += 1
                if not _quote_ok(quote):
                    quote_mismatched += 1
                    fact["confidence"] = "low"
                    warnings.append(GateError(
                        "QUOTE_MISMATCH",
                        f"{where} quote is not a verbatim substring of "
                        "that meeting's source text — confidence forced "
                        "to 'low'. Copy quotes exactly from the source."))
            _subject_check(fact, where)

        # --- disciplinary (facts-v2: itemized; quote hard-checked) ----------
        for i, fact in enumerate(mrec["disciplinary"]):
            where = f"Meeting {d} disciplinary[{i}]"
            total_facts += 1
            if not _check_fields(fact, _DISCIPLINARY_FIELDS, where, errors):
                continue
            _check_enum(fact, "category", DISCIPLINE_CATEGORIES, where,
                        errors)
            _check_enum(fact, "confidence", CONFIDENCE, where, errors)
            count = fact.get("count")
            respondent = fact.get("respondent")
            if not isinstance(count, int) or isinstance(count, bool) \
                    or count < 1:
                errors.append(GateError(
                    "FIELD",
                    f"{where} count is {count!r}; it must be an integer "
                    ">= 1 (1 for an itemized action; the stated total for "
                    "a bulk entry). Never emit zero-count entries."))
                continue
            if respondent is not None and count != 1:
                errors.append(GateError(
                    "COUNT_RULE",
                    f"{where} names respondent '{respondent}' but has "
                    f"count {count}. An itemized action is always count 1 "
                    "— emit one entry per action."))
            if respondent is None and count > 1 \
                    and not count_visible(count, fact["quote"]):
                errors.append(GateError(
                    "COUNT_NOT_IN_QUOTE",
                    f"{where} is a bulk entry (count {count}) but its "
                    "quote does not contain that number. Bulk entries are "
                    "allowed ONLY when the document itself states the "
                    "total — quote the sentence stating it, or itemize "
                    "the actions one entry each."))
            if respondent is not None:
                key = ("disciplinary", d, fact.get("category"),
                       _ws(respondent).lower())
                dup_msg = (f"{where} duplicates respondent '{respondent}' "
                           f"for category '{fact.get('category')}' at this "
                           "meeting. One entry per action.")
            else:
                key = ("disciplinary-bulk", d, fact.get("category"),
                       _ws(fact["quote"]).lower())
                dup_msg = (f"{where} duplicates a bulk entry with the same "
                           "quote at this meeting. Merge them.")
            if key in seen_keys:
                errors.append(GateError("DUPLICATE_FACT", dup_msg))
            seen_keys.add(key)
            if not _quote_ok(fact["quote"]):
                errors.append(GateError(
                    "FABRICATED_QUOTE",
                    f"{where} quote is not a verbatim substring of that "
                    "meeting's source text. Disciplinary quotes anchor "
                    "each action and must be copied exactly from the "
                    "source."))

        # --- emerging_topics (quote REQUIRED + always hard-checked) ---------
        for i, fact in enumerate(mrec["emerging_topics"]):
            where = f"Meeting {d} emerging_topics[{i}]"
            total_facts += 1
            if not _check_fields(fact, _EMERGING_FIELDS, where, errors):
                continue
            _check_enum(fact, "confidence", CONFIDENCE, where, errors)
            key = ("emerging", _ws(fact.get("topic_slug")).lower())
            if key in seen_keys:
                errors.append(GateError(
                    "DUPLICATE_FACT",
                    f"{where} duplicates topic_slug "
                    f"'{fact.get('topic_slug')}' elsewhere in this file. "
                    "Keep only the EARLIEST mention of an emerging topic."))
            seen_keys.add(key)
            if not _quote_ok(fact["quote"]):
                errors.append(GateError(
                    "FABRICATED_QUOTE",
                    f"{where} quote is not a verbatim substring of that "
                    "meeting's source text. Emerging-topic quotes are the "
                    "fabrication anchor and must be copied exactly from "
                    "the source."))
            _subject_check(fact, where)

    # --- F5 file-level mismatch rate -----------------------------------------
    if quote_checked and \
            quote_mismatched / quote_checked > QUOTE_MISMATCH_MAX_FRACTION:
        errors.append(GateError(
            "QUOTE_MISMATCH_RATE",
            f"{quote_mismatched} of {quote_checked} quotes are not "
            "verbatim substrings of their meeting's source text (over "
            f"{QUOTE_MISMATCH_MAX_FRACTION:.0%} of the file). Re-extract "
            "with quotes copied exactly from the source."))

    # --- F7 every covered meeting must appear --------------------------------
    missing = sorted(covered_dates - json_dates)
    if missing:
        errors.append(GateError(
            "MISSING_MEETING",
            f"{len(missing)} covered meeting date(s) are absent from the "
            f"file: {', '.join(missing)}. Every covered meeting MUST "
            "appear; empty arrays mean examined-nothing-found."))

    # --- F8 volume -------------------------------------------------------------
    if total_facts > FACTS_MAX_PER_FILE:
        errors.append(GateError(
            "TOO_MANY_FACTS",
            f"File contains {total_facts} facts; the cap is "
            f"{FACTS_MAX_PER_FILE} per board-file. Keep only the clearly "
            "supported facts (routine meetings correctly produce empty "
            "arrays)."))

    return GateResult(ok=not errors, errors=errors, warnings=warnings)
