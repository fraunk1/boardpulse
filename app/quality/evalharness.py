"""Gold-standard eval harness for board summaries.

The Fable-era summaries in data/reports/ are the gold corpus. This module
freezes a representative set of (prompt, summary) pairs into data/gold/,
then scores candidate summaries (written by a challenger model into
data/eval/{run_id}/) against that frozen gold set with deterministic,
file-based metrics. An optional LLM-judge pass (judge_prompt.md ->
judge_verdict.json) is merged into the scorecard when present.

Entry points (CLI wiring lives in cli.py, owned by the orchestrator):

    prepare(boards)             freeze gold set + manifest, print dispatch block
    score(run_id, model_label)  deterministic scorecard -> scorecard.json
    judge(run_id)               emit judge_prompt.md for a qualitative pass

Everything here is synchronous and file-based on purpose: the harness must
produce identical output for identical inputs, with no DB or network
dependency. The quality gate (app.quality.gates.check_summary) is imported
lazily and defensively — if the module is missing or its signature is
unrecognized, every other metric still runs and the gate is reported as
"gate module not available".
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from app.config import DATA_DIR, REPORTS_DIR

GOLD_DIR = DATA_DIR / "gold"
EVAL_DIR = DATA_DIR / "eval"

# The 8 archetype boards frozen as the default gold set:
#   HI_MD (narrative minutes, name-dense)   NE_MD (mid-size)
#   VT_MD (very large bundle)               CA_DO (large, few meetings)
#   TX_MD (press-release style)             AZ_MD (big / truncation)
#   WY_MD (thin, agenda-only)               MI_DO (small DO board)
DEFAULT_BOARDS = [
    "HI_MD", "NE_MD", "VT_MD", "CA_DO", "TX_MD", "AZ_MD", "WY_MD", "MI_DO",
]

MANIFEST_NAME = "manifest.json"

# --- score thresholds (gold-number recall + length bands are reported,
#     not thresholded) ---
THRESHOLDS = {
    "block_coverage": 1.0,
    "citation_validity": 1.0,
    "topic_jaccard": 0.5,
    "name_verification": 0.95,
    "gold_name_recall": 0.6,
}

ROLLUP_BAND = (300, 600)   # words, per the authoring contract
MEETING_BAND = (80, 200)   # words

# ---------------------------------------------------------------------------
# regexes
# ---------------------------------------------------------------------------

# Reference-table line: - `[2026-03-30]` — Wyoming Board of Medicine — ...
_REF_DATE_RE = re.compile(r"^- `\[(\d{4}-\d{2}-\d{2})\]`", re.MULTILINE)

# Per-meeting source header: ### 2026-03-30 — Wyoming Board of Medicine — ...
_SECTION_HEADER_RE = re.compile(r"^### (\d{4}-\d{2}-\d{2})\b.*$", re.MULTILINE)

_NO_TEXT_MARKER = "(No extracted text available)"

_STATE_RE = re.compile(r"^State:\s*([A-Z]{2})\s*$", re.MULTILINE)
_CODE_RE = re.compile(r"^Code:\s*([A-Z]{2}_[A-Z]{2})\s*$", re.MULTILINE)

# The URL the model is told to use in its Sources table
_SOURCES_URL_RE = re.compile(r"^Sources-table URL:\s*(\S+)", re.MULTILINE)

# Clinician name, e.g. "Aman K. Patel, D.O." (spec'd regex — do not "improve")
_NAME_RE = re.compile(
    r"((?:[A-Z][\w.'-]+ ){1,3}[A-Z][\w.'-]+),?\s*(M\.?D\.?|D\.?O\.?|P\.?A\.?)"
)

# Numbers with >= 3 digits, allowing comma grouping ("49,000" -> "49000")
_NUM_RE = re.compile(r"\d{1,3}(?:,\d{3})+|\d{3,}")

# A citation attempt: any markdown link whose label is an ISO date
_CITE_RE = re.compile(r"\[(\d{4}-\d{2}-\d{2})\]\(([^)]*)\)")

# Any markdown link (stripped before word counts)
_MD_LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")


# ---------------------------------------------------------------------------
# parsing helpers
# ---------------------------------------------------------------------------

def parse_prompt_file(text: str) -> dict:
    """Parse a per-board prompt bundle.

    Returns dict with:
        state, code           from the "State:" / "Code:" lines
        reference_dates       all dates in the "Available Meeting Dates" table
        sections              {date: source text} for meetings WITH text
        textless_dates        dates whose section carries the no-text marker
        sources_table_url     the URL the summary is told to cite (or None)
    """
    state_m = _STATE_RE.search(text)
    code_m = _CODE_RE.search(text)
    state = state_m.group(1) if state_m else ""
    code = code_m.group(1) if code_m else ""

    # Reference table lives between "## Available Meeting Dates" and next "## "
    reference_dates: list[str] = []
    ref_start = text.find("## Available Meeting Dates")
    if ref_start != -1:
        nxt = text.find("\n## ", ref_start + 1)
        ref_block = text[ref_start: nxt if nxt != -1 else len(text)]
        reference_dates = _REF_DATE_RE.findall(ref_block)

    # Per-meeting sections live under "## Meeting Minutes Data"
    sections: dict[str, str] = {}
    textless: list[str] = []
    data_start = text.find("## Meeting Minutes Data")
    body = text[data_start:] if data_start != -1 else text
    matches = list(_SECTION_HEADER_RE.finditer(body))
    for i, m in enumerate(matches):
        date_str = m.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        section = body[m.end():end].strip()
        if _NO_TEXT_MARKER in section:
            textless.append(date_str)
            continue
        if date_str in sections:  # duplicate header: concatenate
            sections[date_str] += "\n\n" + section
        else:
            sections[date_str] = section

    url_m = _SOURCES_URL_RE.search(text)
    return {
        "state": state,
        "code": code,
        "reference_dates": sorted(set(reference_dates)),
        "sections": sections,
        "textless_dates": sorted(set(textless)),
        "sources_table_url": url_m.group(1) if url_m else None,
    }


def extract_names(text: str) -> list[tuple[str, str]]:
    """(full_name, surname) pairs found by the clinician-name regex, deduped
    in first-seen order."""
    seen: dict[str, str] = {}
    for m in _NAME_RE.finditer(text):
        full = m.group(1).strip()
        surname = full.split()[-1].strip(".,'’")
        if full not in seen:
            seen[full] = surname
    return list(seen.items())


def _surname_in(surname: str, text: str) -> bool:
    if not surname:
        return False
    return re.search(rf"\b{re.escape(surname)}\b", text, re.IGNORECASE) is not None


def extract_numbers(text: str) -> set[str]:
    """Normalized (comma-stripped) digit strings with >= 3 digits."""
    out = set()
    for m in _NUM_RE.finditer(text):
        out.add(m.group(0).replace(",", ""))
    return out


def _strip_links_and_count(text: str) -> int:
    """Word count with markdown links and bare punctuation removed."""
    cleaned = _MD_LINK_RE.sub(" ", text)
    cleaned = re.sub(r"[()\[\];,]", " ", cleaned)
    return len([w for w in cleaned.split() if re.search(r"[A-Za-z0-9]", w)])


def rollup_word_count(rollup: str) -> int:
    """Narrative word count of a rollup: headings, Period/Meetings lines and
    the Sources table are excluded, citation links stripped."""
    lines = []
    for line in rollup.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            continue
        if s.startswith("**Period:") or s.startswith("**Meetings analyzed:"):
            continue
        lines.append(s)
    return _strip_links_and_count(" ".join(lines))


def jaccard(a, b) -> float:
    sa = {str(t).strip().lower() for t in a if str(t).strip()}
    sb = {str(t).strip().lower() for t in b if str(t).strip()}
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb)


def _parse_summary(text: str):
    """Thin wrapper around the production parser (lazy import keeps this
    module importable even if summarizer's dependencies are unavailable)."""
    from app.extractor.summarizer import parse_board_summary_file
    return parse_board_summary_file(text)


# ---------------------------------------------------------------------------
# 1. prepare — freeze the gold set
# ---------------------------------------------------------------------------

def prepare(
    boards: list[str] | None = None,
    *,
    reports_dir: Path | None = None,
    gold_dir: Path | None = None,
) -> dict:
    """Freeze the gold set: copy (prompt, summary) pairs into data/gold/ and
    write manifest.json with everything score() needs. Returns the manifest.
    """
    reports_dir = Path(reports_dir or REPORTS_DIR)
    gold_dir = Path(gold_dir or GOLD_DIR)
    gold_dir.mkdir(parents=True, exist_ok=True)

    requested = list(boards) if boards else list(DEFAULT_BOARDS)

    def has_pair(code: str) -> bool:
        return (reports_dir / f"{code}_prompt.md").exists() and \
               (reports_dir / f"{code}_summary.md").exists()

    # available pool for substitutions (deterministic: sorted)
    pool = sorted(
        p.name[: -len("_prompt.md")]
        for p in reports_dir.glob("*_prompt.md")
        if has_pair(p.name[: -len("_prompt.md")])
    )

    chosen: list[str] = []
    substitutions: dict[str, str] = {}
    for code in requested:
        if has_pair(code):
            chosen.append(code)
            continue
        sub = next((c for c in pool if c not in chosen and c not in requested), None)
        if sub:
            substitutions[code] = sub
            chosen.append(sub)
            print(f"NOTE: {code} missing prompt or summary on disk — substituting {sub}")
        else:
            print(f"NOTE: {code} missing prompt or summary on disk — no substitute available, skipping")

    manifest: dict = {
        "schema_version": 1,
        "boards": {},
        "requested_boards": requested,
        "substitutions": substitutions,
    }

    for code in chosen:
        prompt_text = (reports_dir / f"{code}_prompt.md").read_text(encoding="utf-8")
        summary_text = (reports_dir / f"{code}_summary.md").read_text(encoding="utf-8")

        # copy verbatim into the gold dir
        (gold_dir / f"{code}_prompt.md").write_text(prompt_text, encoding="utf-8")
        (gold_dir / f"{code}_summary.md").write_text(summary_text, encoding="utf-8")

        pinfo = parse_prompt_file(prompt_text)
        _topics, rollup, meetings = _parse_summary(summary_text)

        text_dates = sorted(pinfo["sections"].keys())
        gold_dates = sorted(meetings.keys())

        gold_topics_by_date: dict[str, list[str]] = {}
        gold_names_by_date: dict[str, list[str]] = {}
        gold_numbers_by_date: dict[str, list[str]] = {}
        for d in gold_dates:
            block_text, block_topics = meetings[d]
            gold_topics_by_date[d] = sorted({str(t).strip() for t in block_topics if str(t).strip()})
            source = pinfo["sections"].get(d, "")
            # verified gold names: regex over the gold block, surname must
            # appear in the prompt's source text for that date
            verified = [
                full for full, surname in extract_names(block_text)
                if source and _surname_in(surname, source)
            ]
            gold_names_by_date[d] = sorted(set(verified))
            # gold numbers: >=3-digit numbers in the gold block that also
            # appear in that date's source text
            gold_numbers_by_date[d] = sorted(
                extract_numbers(block_text) & extract_numbers(source)
            )

        entry = {
            "state": pinfo["state"],
            "code": pinfo["code"] or code,
            "prompt_file": f"{code}_prompt.md",
            "summary_file": f"{code}_summary.md",
            "all_prompt_dates": pinfo["reference_dates"],
            "text_meeting_dates": text_dates,
            "textless_dates": pinfo["textless_dates"],
            "gold_block_dates": gold_dates,
            "gold_missing_text_dates": sorted(set(text_dates) - set(gold_dates)),
            "gold_topics_by_date": gold_topics_by_date,
            "gold_names_by_date": gold_names_by_date,
            "gold_numbers_by_date": gold_numbers_by_date,
            "rollup_word_count": rollup_word_count(rollup),
            "notes": (
                [f"substituted for {k}" for k, v in substitutions.items() if v == code]
            ),
        }
        manifest["boards"][code] = entry

    manifest_path = gold_dir / MANIFEST_NAME
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    # ---- report ----
    print(f"\nGold set frozen: {len(chosen)} boards -> {gold_dir}")
    print(f"Manifest: {manifest_path}\n")
    print(f"{'board':8} {'state':5} {'text mtgs':>9} {'gold blocks':>11} "
          f"{'names':>5} {'nums':>5} {'rollup words':>12}")
    for code in chosen:
        e = manifest["boards"][code]
        n_names = sum(len(v) for v in e["gold_names_by_date"].values())
        n_nums = sum(len(v) for v in e["gold_numbers_by_date"].values())
        print(f"{code:8} {e['state']:5} {len(e['text_meeting_dates']):>9} "
              f"{len(e['gold_block_dates']):>11} {n_names:>5} {n_nums:>5} "
              f"{e['rollup_word_count']:>12}")
        if e["gold_missing_text_dates"]:
            print(f"         NOTE: gold summary lacks blocks for text dates: "
                  f"{', '.join(e['gold_missing_text_dates'])}")

    print("\n--- DISPATCH INSTRUCTIONS " + "-" * 40)
    print("Pick a run_id (e.g. opus48-preflight). For EACH board below, "
          "dispatch one agent with this task:\n")
    for code in chosen:
        print(f"  {code}: read data/gold/{code}_prompt.md fully, follow its "
              f"'Output Format' contract exactly,\n"
              f"          write the finished summary to "
              f"data/eval/{{run_id}}/{code}_summary.md")
    print("\nThen run: score(run_id, model_label) and optionally judge(run_id).")
    print("-" * 66)

    return manifest


# ---------------------------------------------------------------------------
# gate (lazy, defensive)
# ---------------------------------------------------------------------------

def _run_gate(candidate_text: str, *, board_code: str, state: str,
              source_texts_by_date: dict[str, str],
              all_dates: list[str] | None = None,
              minutes_url: str | None = None) -> dict:
    """Call app.quality.gates.check_summary defensively.

    The kwargs are built by matching check_summary's own signature against a
    pool of everything the frozen gold files can supply (the gate module is
    owned by another workstream, so its exact signature is not assumed).

    Returns {"available": bool, "passed": bool|None, "detail": str}.
    passed=None means the gate could not be evaluated (missing module or
    unrecognized signature/result) — score() then excludes the gate from the
    verdict and flags it.
    """
    try:
        import app.quality.gates as gates
        check_summary = gates.check_summary
    except Exception as exc:  # ImportError or anything raised at import time
        return {"available": False, "passed": None,
                "detail": f"gate module not available: {exc}"}

    import inspect

    text = candidate_text
    normalize = getattr(gates, "normalize_summary", None)
    if callable(normalize):
        text = normalize(candidate_text)

    text_dates = set(source_texts_by_date)
    value_pool = {
        "summary_text": text, "summary": text,
        "text": text, "candidate": text,
        "board_code": board_code, "code": board_code, "board": board_code,
        "state": state,
        "source_texts_by_date": source_texts_by_date,
        "source_texts": source_texts_by_date,
        "sources_by_date": source_texts_by_date,
        "db_text_dates": text_dates,
        "text_meeting_dates": text_dates,
        "db_all_dates": set(all_dates) | text_dates if all_dates else text_dates,
        "all_dates": set(all_dates) if all_dates else text_dates,
        "expected_dates": sorted(text_dates),
        "meeting_dates": sorted(text_dates),
        "minutes_url": minutes_url,
        "homepage": None,
    }
    try:
        sig = inspect.signature(check_summary)
        kwargs = {}
        for i, (pname, p) in enumerate(sig.parameters.items()):
            if p.kind in (inspect.Parameter.VAR_POSITIONAL,
                          inspect.Parameter.VAR_KEYWORD):
                continue
            if pname in value_pool:
                kwargs[pname] = value_pool[pname]
            elif i == 0 and p.default is inspect.Parameter.empty:
                kwargs[pname] = text  # first required arg: the summary text
        result = check_summary(**kwargs)
    except Exception as exc:
        return {"available": True, "passed": None,
                "detail": f"gate call failed: {exc}"}

    passed, detail = _normalize_gate_result(result)
    return {"available": True, "passed": passed, "detail": detail}


def _issue_str(issue) -> str:
    code = getattr(issue, "code", None)
    message = getattr(issue, "message", None)
    if code or message:
        return f"{code}: {message}" if code else str(message)
    return str(issue)


def _join_issues(issues) -> str:
    strs = [_issue_str(i) for i in issues]
    if len(strs) > 5:
        strs = strs[:5] + [f"... (+{len(strs) - 5} more)"]
    return "; ".join(strs)


def _normalize_gate_result(result) -> tuple[bool | None, str]:
    if isinstance(result, bool):
        return result, ""
    if isinstance(result, tuple) and result and isinstance(result[0], bool):
        rest = "; ".join(str(x) for x in result[1:]) if len(result) > 1 else ""
        return result[0], rest
    if isinstance(result, dict):
        for key in ("passed", "pass", "ok", "success"):
            if key in result and isinstance(result[key], bool):
                issues = result.get("issues") or result.get("errors") or []
                return result[key], _join_issues(issues)
    for attr in ("passed", "ok", "success"):
        val = getattr(result, attr, None)
        if isinstance(val, bool):
            issues = getattr(result, "issues", None) or getattr(result, "errors", None) or []
            return val, _join_issues(issues)
    return None, f"unrecognized gate result type: {type(result).__name__}"


# ---------------------------------------------------------------------------
# 2. score — deterministic scorecard
# ---------------------------------------------------------------------------

def _score_board(entry: dict, candidate_text: str,
                 source_sections: dict[str, str]) -> dict:
    """All deterministic metrics for one board. Pure: no I/O."""
    state, code = entry["state"], entry["code"]
    _cand_topics, cand_rollup, cand_meetings = _parse_summary(candidate_text)

    text_dates = entry["text_meeting_dates"]
    cand_dates = sorted(cand_meetings.keys())
    known_dates = set(entry["all_prompt_dates"]) | set(text_dates)

    # -- block coverage: candidate blocks covering the prompt's text dates
    covered = [d for d in text_dates if d in cand_meetings]
    block_coverage = len(covered) / len(text_dates) if text_dates else 1.0

    # -- citation validity over the candidate rollup
    cites = _CITE_RE.findall(cand_rollup)
    valid = sum(
        1 for d, url in cites
        if url == f"/board/{state}/{code}#{d}" and d in known_dates
    )
    if cites:
        citation_validity = valid / len(cites)
        citation_note = f"{valid}/{len(cites)} valid"
    else:
        citation_validity = 0.0
        citation_note = "no citations found in rollup"

    # -- topic overlap: mean Jaccard on dates both gold and candidate cover
    shared = [d for d in entry["gold_block_dates"] if d in cand_meetings]
    if shared:
        topic_jaccard = sum(
            jaccard(entry["gold_topics_by_date"].get(d, []), cand_meetings[d][1])
            for d in shared
        ) / len(shared)
    else:
        topic_jaccard = 0.0

    # -- name verification: names the CANDIDATE asserts must exist in the
    #    source text for that date
    total_names = verified_names = 0
    unverified: list[str] = []
    for d, (block_text, _topics) in cand_meetings.items():
        source = source_sections.get(d, "")
        for full, surname in extract_names(block_text):
            total_names += 1
            if source and _surname_in(surname, source):
                verified_names += 1
            else:
                unverified.append(f"{d}: {full}")
    name_verification = verified_names / total_names if total_names else 1.0

    # -- gold-name recall: verified gold names the candidate reproduces
    gold_total = gold_found = 0
    missed_names: list[str] = []
    for d, names in entry["gold_names_by_date"].items():
        cand_block = cand_meetings.get(d, ("", []))[0]
        for full in names:
            gold_total += 1
            surname = full.split()[-1].strip(".,'’")
            if cand_block and _surname_in(surname, cand_block):
                gold_found += 1
            else:
                missed_names.append(f"{d}: {full}")
    gold_name_recall = gold_found / gold_total if gold_total else 1.0

    # -- gold-number recall (reported, not thresholded)
    num_total = num_found = 0
    for d, nums in entry["gold_numbers_by_date"].items():
        cand_nums = extract_numbers(cand_meetings.get(d, ("", []))[0])
        for n in nums:
            num_total += 1
            if n in cand_nums:
                num_found += 1
    gold_number_recall = num_found / num_total if num_total else 1.0

    # -- length bands (reported, not thresholded)
    r_words = rollup_word_count(cand_rollup)
    rollup_in_band = ROLLUP_BAND[0] <= r_words <= ROLLUP_BAND[1]
    m_counts = {d: _strip_links_and_count(t) for d, (t, _) in cand_meetings.items()}
    in_band = sum(1 for w in m_counts.values() if MEETING_BAND[0] <= w <= MEETING_BAND[1])
    meeting_in_band_rate = in_band / len(m_counts) if m_counts else 1.0

    metrics = {
        "block_coverage": round(block_coverage, 4),
        "citation_validity": round(citation_validity, 4),
        "topic_jaccard": round(topic_jaccard, 4),
        "name_verification": round(name_verification, 4),
        "gold_name_recall": round(gold_name_recall, 4),
        "gold_number_recall": round(gold_number_recall, 4),
        "rollup_words": r_words,
        "rollup_in_band": rollup_in_band,
        "meeting_in_band_rate": round(meeting_in_band_rate, 4),
    }
    detail = {
        "candidate_block_dates": cand_dates,
        "missing_text_dates": sorted(set(text_dates) - set(cand_meetings)),
        "extra_block_dates": sorted(set(cand_dates) - set(text_dates)),
        "citation_note": citation_note,
        "unverified_names": unverified,
        "missed_gold_names": missed_names,
        "gold_names_total": gold_total,
        "gold_numbers_total": num_total,
        "candidate_names_total": total_names,
    }

    failures = [
        name for name, floor in THRESHOLDS.items()
        if metrics[name] < floor
    ]
    return {"metrics": metrics, "detail": detail, "threshold_failures": failures}


def score(
    run_id: str,
    model_label: str | None = None,
    *,
    gold_dir: Path | None = None,
    eval_dir: Path | None = None,
) -> dict:
    """Score data/eval/{run_id}/ candidates against the frozen gold set.

    Writes data/eval/{run_id}/scorecard.json and prints a compact table with
    a PASS/FAIL verdict. Returns the scorecard dict.
    """
    gold_dir = Path(gold_dir or GOLD_DIR)
    eval_dir = Path(eval_dir or EVAL_DIR)
    run_dir = eval_dir / run_id

    manifest_path = gold_dir / MANIFEST_NAME
    if not manifest_path.exists():
        raise FileNotFoundError(
            f"No gold manifest at {manifest_path} — run prepare() first."
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    boards: dict[str, dict] = {}
    absent: list[str] = []
    gate_available = True

    for code, entry in sorted(manifest["boards"].items()):
        cand_path = run_dir / f"{code}_summary.md"
        if not cand_path.exists():
            absent.append(code)
            boards[code] = {"present": False}
            continue

        candidate_text = cand_path.read_text(encoding="utf-8")
        prompt_text = (gold_dir / entry["prompt_file"]).read_text(encoding="utf-8")
        pinfo = parse_prompt_file(prompt_text)
        source_sections = pinfo["sections"]

        result = _score_board(entry, candidate_text, source_sections)
        gate = _run_gate(
            candidate_text,
            board_code=entry["code"],
            state=entry["state"],
            source_texts_by_date=source_sections,
            all_dates=entry["all_prompt_dates"],
            minutes_url=pinfo.get("sources_table_url"),
        )
        if gate["passed"] is None:
            gate_available = gate_available and False
        result["gate"] = gate
        result["present"] = True

        gate_fails = gate["passed"] is False
        result["pass"] = not result["threshold_failures"] and not gate_fails
        boards[code] = result

    present = [c for c, r in boards.items() if r.get("present")]

    def _mean(metric: str) -> float | None:
        vals = [boards[c]["metrics"][metric] for c in present
                if isinstance(boards[c]["metrics"].get(metric), (int, float))]
        return round(sum(vals) / len(vals), 4) if vals else None

    aggregate = {
        m: _mean(m)
        for m in ("block_coverage", "citation_validity", "topic_jaccard",
                  "name_verification", "gold_name_recall", "gold_number_recall",
                  "meeting_in_band_rate")
    }
    aggregate["boards_scored"] = len(present)
    aggregate["boards_absent"] = len(absent)

    overall_pass = (
        bool(present)
        and not absent
        and all(boards[c]["pass"] for c in present)
    )

    scorecard: dict = {
        "run_id": run_id,
        "model_label": model_label,
        "gate_evaluated": gate_available and bool(present),
        "boards": boards,
        "absent_boards": absent,
        "aggregate": aggregate,
        "pass": overall_pass,
    }

    # merge the LLM-judge verdict when present
    verdict_path = run_dir / "judge_verdict.json"
    if verdict_path.exists():
        try:
            verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
            scorecard["judge"] = verdict
            if str(verdict.get("overall", "")).lower() == "fail":
                scorecard["pass"] = False
                scorecard["judge_blocked_pass"] = True
        except json.JSONDecodeError as exc:
            scorecard["judge"] = {"error": f"judge_verdict.json unparseable: {exc}"}

    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "scorecard.json").write_text(
        json.dumps(scorecard, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    _print_scorecard(scorecard)
    return scorecard


def _print_scorecard(sc: dict) -> None:
    label = f" model={sc['model_label']}" if sc.get("model_label") else ""
    print(f"\nEval scorecard — run {sc['run_id']}{label}")
    hdr = (f"{'board':8} {'gate':>6} {'cover':>6} {'cite':>6} {'topic':>6} "
           f"{'names':>6} {'g-name':>6} {'g-num':>6} {'band':>6} {'verdict':>8}")
    print(hdr)
    print("-" * len(hdr))
    for code, r in sorted(sc["boards"].items()):
        if not r.get("present"):
            print(f"{code:8} {'-':>6} {'ABSENT — blocks overall PASS':>40}")
            continue
        m = r["metrics"]
        g = r["gate"]
        gate_str = ("n/a" if g["passed"] is None
                    else ("PASS" if g["passed"] else "FAIL"))
        print(f"{code:8} {gate_str:>6} {m['block_coverage']:>6.2f} "
              f"{m['citation_validity']:>6.2f} {m['topic_jaccard']:>6.2f} "
              f"{m['name_verification']:>6.2f} {m['gold_name_recall']:>6.2f} "
              f"{m['gold_number_recall']:>6.2f} {m['meeting_in_band_rate']:>6.2f} "
              f"{'PASS' if r['pass'] else 'FAIL':>8}")
        for fail in r["threshold_failures"]:
            print(f"         !! {fail} below threshold "
                  f"({m[fail]} < {THRESHOLDS[fail]})")
        if g["passed"] is None:
            print(f"         !! gate not evaluated: {g['detail']}")
    if sc["absent_boards"]:
        print(f"\nAbsent candidates: {', '.join(sc['absent_boards'])}")
    if not sc.get("gate_evaluated"):
        print("\nWARNING: quality gate not evaluated (gate module not "
              "available) — verdict covers all other metrics only.")
    if sc.get("judge_blocked_pass"):
        print("\nJudge verdict: FAIL — overrides deterministic PASS.")
    elif "judge" in sc:
        print(f"\nJudge verdict merged: {sc['judge'].get('overall', 'n/a')}")
    print(f"\nVERDICT: {'PASS' if sc['pass'] else 'FAIL'}")


# ---------------------------------------------------------------------------
# 3. judge — emit a qualitative comparison prompt
# ---------------------------------------------------------------------------

def _sample_dates(dates: list[str], k: int = 3) -> list[str]:
    """Deterministic sample: first, middle, last of the sorted list."""
    dates = sorted(dates)
    if len(dates) <= k:
        return dates
    idx = sorted({0, len(dates) // 2, len(dates) - 1})
    return [dates[i] for i in idx]


def judge(
    run_id: str,
    *,
    gold_dir: Path | None = None,
    eval_dir: Path | None = None,
) -> Path:
    """Write data/eval/{run_id}/judge_prompt.md pairing gold vs candidate
    blocks (up to 3 sampled meetings per board). A judge agent reads it and
    writes judge_verdict.json next to it; score() merges that verdict.
    """
    gold_dir = Path(gold_dir or GOLD_DIR)
    eval_dir = Path(eval_dir or EVAL_DIR)
    run_dir = eval_dir / run_id

    manifest = json.loads((gold_dir / MANIFEST_NAME).read_text(encoding="utf-8"))

    lines = [
        "# Gold vs candidate — judge instructions",
        "",
        "You are comparing per-meeting summaries of the SAME source minutes:",
        "GOLD (trusted reference) vs CANDIDATE (challenger model output).",
        "For each pair below, list:",
        "- **contradictions**: candidate states something the gold (or plain",
        "  reading of the gold) contradicts — wrong names, outcomes, votes,",
        "  dates, or numbers.",
        "- **omissions**: substantive gold facts (actions, names, decisions)",
        "  missing from the candidate.",
        "Style differences are fine; only substance counts.",
        "",
        f"When done, write your verdict to `data/eval/{run_id}/judge_verdict.json`:",
        "",
        "```json",
        "{",
        '  "boards": {',
        '    "XX_MD": {"verdict": "pass|fail", "contradictions": ["..."], "omissions": ["..."]}',
        "  },",
        '  "overall": "pass|fail"',
        "}",
        "```",
        "",
        'Fail a board only for material contradictions or omissions that would',
        "mislead a regulatory-affairs reader.",
        "",
    ]

    n_pairs = 0
    for code, entry in sorted(manifest["boards"].items()):
        cand_path = run_dir / f"{code}_summary.md"
        if not cand_path.exists():
            lines += [f"## {code}", "", "_Candidate file absent — mark this board fail._", ""]
            continue
        _t, _r, gold_meetings = _parse_summary(
            (gold_dir / entry["summary_file"]).read_text(encoding="utf-8"))
        _t2, _r2, cand_meetings = _parse_summary(
            cand_path.read_text(encoding="utf-8"))

        shared = [d for d in gold_meetings if d in cand_meetings]
        sampled = _sample_dates(shared)
        lines += [f"## {code}", ""]
        if not sampled:
            lines += ["_No overlapping meeting blocks to compare._", ""]
            continue
        for d in sampled:
            n_pairs += 1
            lines += [
                f"### {code} — {d}",
                "",
                "**GOLD:**",
                "", gold_meetings[d][0], "",
                "**CANDIDATE:**",
                "", cand_meetings[d][0], "",
            ]

    run_dir.mkdir(parents=True, exist_ok=True)
    out = run_dir / "judge_prompt.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Judge prompt written: {out} ({n_pairs} gold/candidate pairs)")
    print(f"Judge agent should write verdict to: {run_dir / 'judge_verdict.json'}")
    return out
