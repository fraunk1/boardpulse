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
import re
from dataclasses import dataclass, field
from urllib.parse import urlparse

from app.quality.taxonomy import TOPICS


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
) -> GateResult:
    """Run every gate check against a normalized summary file.

    Pure function: callers supply the DB-derived inputs.
      db_text_dates        meeting dates (ISO) in the 12-month window that
                           have at least one document with extracted text
      db_all_dates         every meeting date the board has, any window
      source_texts_by_date concatenated document text per window date
      minutes_url/homepage the board's registered URLs (Sources host check)
    """
    # Local import: summarizer imports this module for ingest wiring, so the
    # reverse import must happen at call time to avoid a cycle.
    from app.extractor.summarizer import parse_board_summary_file

    errors: list[GateError] = []
    warnings: list[GateError] = []
    text = text or ""
    valid_text_dates = ", ".join(sorted(db_text_dates)) or "(none)"

    # --- S1 STRUCTURE ------------------------------------------------------
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
                f"Frontmatter 'board:' is '{bm.group(1).strip()}' but this "
                f"file is for board {board_code}. Set board: {board_code}."))

    if not _END_RE.search(text):
        errors.append(GateError(
            "STRUCTURE",
            "File does not contain the '=== END ===' terminator. Append "
            "'=== END ===' on its own line after the last meeting block."))

    board_topics, rollup, sections = parse_board_summary_file(text)

    if not sections:
        errors.append(GateError(
            "LEGACY_FORMAT",
            "No '=== MEETING: YYYY-MM-DD ===' blocks found — this is the "
            "legacy single-blob format. Rewrite using the two-layer "
            "contract: a 12-month rollup, then one '=== MEETING: date ===' "
            f"block per text-bearing meeting date ({valid_text_dates}), "
            "ending with '=== END ==='."))
        # Block-level checks are meaningless without blocks.
        return GateResult(ok=False, errors=errors, warnings=warnings)

    # --- S2 BLOCKS vs DB text dates -----------------------------------------
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
                f"Block dated {d} does not match any text-bearing meeting "
                "in the last 12 months. Remove it or re-date it to one of "
                f"the valid dates: {valid_text_dates}."))

    missing = sorted(db_text_dates - block_dates)
    if missing:
        # Warning, never hard: text routinely lands AFTER a summary was
        # written (archive backfills, fresh extract passes), and nothing
        # false enters the DB — the meeting just stays unsummarized. The
        # refresh pipeline treats this as its re-summarization trigger.
        warnings.append(GateError(
            "MISSING_BLOCK",
            f"{len(missing)} text-bearing meeting date(s) have no "
            f"'=== MEETING: date ===' block: {', '.join(missing)}. "
            "Re-summarize this board to cover them (an agenda-only note is "
            f"acceptable). Valid dates: {valid_text_dates}."))

    # --- S3 + S5 rollup citations -------------------------------------------
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
                f"Malformed citation '[{bracket}]({target})'. Every rollup "
                "citation must be ([YYYY-MM-DD](" + expected_path +
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
    parts = _SOURCES_SPLIT_RE.split(rollup, maxsplit=1)
    prose = parts[0]
    rollup_words = len(prose.split())
    lo, hi = ROLLUP_WORDS
    if not lo <= rollup_words <= hi:
        errors.append(GateError(
            "LENGTH",
            f"Rollup is {rollup_words} words (excluding the Sources table); "
            f"it must be {lo}-{hi}. Target 300-600 words of cited "
            "narrative."))

    blo, bhi = BLOCK_WORDS
    for d in sorted(sections):
        block_words = len(sections[d][0].split())
        if not blo <= block_words <= bhi:
            errors.append(GateError(
                "LENGTH",
                f"Meeting block {d} is {block_words} words; each block must "
                f"be {blo}-{bhi}. Target 80-200 words summarizing only that "
                "meeting."))

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
                "The '## Sources' section has no table rows. Add at least "
                "one row: | 1 | YYYY-MM-DD | Board name | [Minutes "
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
    if set(board_topics) != union:
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
    if "Output Format" in rollup or "=== MEETING:" in rollup:
        errors.append(GateError(
            "REFUSAL",
            "The rollup echoes the prompt instructions ('Output Format' / "
            "'=== MEETING:' found inside the rollup). Write only the "
            "12-month narrative and Sources table in the rollup; meeting "
            "blocks belong after it, delimited by '=== MEETING: date ==='."))

    return GateResult(ok=not errors, errors=errors, warnings=warnings)
