#!/usr/bin/env python3
"""Validate *_summary.md files with the ingest gate (app.quality.gates).

Thin wrapper: for each file (or the codes given as args) it queries the
same DB inputs the ingest path uses, then runs check_summary() and prints a
per-file table. Exits 1 if any file fails the gate.

    python _validate_summaries.py            # all files (rollup + archive)
    python _validate_summaries.py HI_MD VA_MD

Manifest-driven: when a {stem}_prompt.meta.json sidecar exists, the gate is
scoped to its covered_dates (blocks not in covered_dates -> ghost errors;
covered dates with no block -> a MISSING warning). Archive files
(mode='archive' in the sidecar, living in data/reports/archive/) are gated
in archive mode — the rollup-only checks are skipped.
"""
import json
import sqlite3
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
DB = ROOT / "boardpulse.db"
REPORTS = ROOT / "data" / "reports"
ARCHIVE = REPORTS / "archive"

from app.quality.gates import check_summary, normalize_summary  # noqa: E402

# "{board_code}_{YYYY}{a|b}" -> strip the chunk suffix to get the board code.
import re  # noqa: E402
_ARCHIVE_CHUNK_SUFFIX_RE = re.compile(r"_(\d{4})([a-z])$")


def _board_code_from_stem(stem: str) -> str:
    return _ARCHIVE_CHUNK_SUFFIX_RE.sub("", stem)


def _read_sidecar(meta_path: Path) -> dict | None:
    if not meta_path.exists():
        return None
    try:
        data = json.loads(meta_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    return data if isinstance(data, dict) else None


def gate_inputs(
    con: sqlite3.Connection, code: str, *,
    sidecar: dict | None = None, archive: bool = False,
) -> dict | None:
    """Build the check_summary() keyword inputs for one file.

    Rollup mode mirrors the ingest path: window-scoped text dates + per-date
    source text; db_all_dates is every meeting the board has.

    When a sidecar is present, db_text_dates is REPLACED by its covered_dates
    (that is the prompt's real scope — blocks must be a subset of it, and
    covered dates with no block are the MISSING set). Archive files pull
    source text for ALL of the board's meeting dates (covered dates are
    out-of-window by definition).
    """
    row = con.execute(
        "SELECT state, minutes_url, homepage FROM boards WHERE code = ?",
        (code,)).fetchone()
    if row is None:
        return None
    state, minutes_url, homepage = row

    # All meeting text (any age), keyed by date — used for archive/sidecar.
    all_texts: dict[str, list[str]] = {}
    for d, t in con.execute("""
        SELECT m.meeting_date, d.content_text FROM meetings m
        JOIN boards b ON b.id = m.board_id
        JOIN meeting_documents d ON d.meeting_id = m.id
        WHERE b.code = ?
          AND d.content_text IS NOT NULL AND d.content_text != ''
    """, (code,)):
        all_texts.setdefault(d[:10], []).append(t)

    cutoff = (date.today() - timedelta(days=365)).isoformat()
    window_texts = {d: v for d, v in all_texts.items() if d >= cutoff}

    all_dates = {r[0][:10] for r in con.execute("""
        SELECT DISTINCT m.meeting_date FROM meetings m
        JOIN boards b ON b.id = m.board_id
        WHERE b.code = ?
    """, (code,))}

    if sidecar and isinstance(sidecar.get("covered_dates"), list):
        # Manifest-driven: the gate's "text dates" are the covered set, and
        # source text comes from the whole board so any covered date resolves.
        db_text_dates = set(sidecar["covered_dates"])
        texts = all_texts
    elif archive:
        db_text_dates = set(all_texts)
        texts = all_texts
    else:
        db_text_dates = set(window_texts)
        texts = window_texts

    return dict(
        state=state,
        db_text_dates=db_text_dates,
        db_all_dates=all_dates,
        source_texts_by_date={k: "\n\n".join(v) for k, v in texts.items()},
        minutes_url=minutes_url,
        homepage=homepage,
    )


def _validate_one(con, path: Path, *, archive: bool) -> bool:
    """Gate one file; print a status row. Returns True if OK."""
    stem = path.stem.replace("_summary", "")
    code = _board_code_from_stem(stem) if archive else stem
    meta_path = path.with_name(f"{stem}_prompt.meta.json")
    sidecar = _read_sidecar(meta_path)
    mode = "archive" if archive else "rollup"

    inputs = gate_inputs(con, code, sidecar=sidecar, archive=archive)
    if inputs is None:
        print(f"  {stem:14} {'NO-BOARD':12} board not found in DB")
        return False

    text = normalize_summary(path.read_text(encoding="utf-8"))
    result = check_summary(code, text, mode=mode, **inputs)

    status = "OK" if result.ok else "FAIL"
    err_codes = ",".join(sorted({e.code for e in result.errors}))
    print(f"  {stem:14} {status:12} errors={len(result.errors):<3} "
          f"warnings={len(result.warnings):<3}"
          f"{'  [' + err_codes + ']' if err_codes else ''}")
    for e in result.errors:
        print(f"           {e.code}: {e.message}")
    return result.ok


def main():
    codes = sys.argv[1:]
    con = sqlite3.connect(DB)

    rollup_files = sorted(REPORTS.glob("*_summary.md"))
    archive_files = sorted(ARCHIVE.glob("*_summary.md")) if ARCHIVE.exists() else []

    if codes:
        rollup_files = [f for f in rollup_files
                        if f.stem.replace("_summary", "") in codes]
        archive_files = [
            f for f in archive_files
            if _board_code_from_stem(f.stem.replace("_summary", "")) in codes]

    bad = 0
    for f in rollup_files:
        if not _validate_one(con, f, archive=False):
            bad += 1
    for f in archive_files:
        if not _validate_one(con, f, archive=True):
            bad += 1

    con.close()
    total = len(rollup_files) + len(archive_files)
    print(f"\n{total} files checked, {bad} problematic")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
