"""Generate the pipeline context markdown file — the handoff between CLI and AI."""
from datetime import date
from pathlib import Path

from sqlalchemy import select

import app.database as db
from app.models import Board, Meeting

TOPIC_TAXONOMY = [
    "AI & Technology", "Board Operations", "Budget & Finance",
    "Continuing Education", "Discipline", "Ethics",
    "Interstate Compact", "Legal", "Licensing",
    "Opioids & Prescribing", "Patient Safety", "Public Health",
    "Rulemaking", "Scope of Practice", "Telehealth", "Workforce",
]


async def generate_context_file(
    run_id: int,
    delta: dict[str, dict[str, int]],
    no_change_boards: list[str],
    output_path: Path,
    reports_dir: Path,
) -> Path:
    """Write the pipeline context markdown file."""
    today = date.today().isoformat()
    total_new_meetings = sum(d["new_meetings"] for d in delta.values())
    total_new_docs = sum(d["new_documents"] for d in delta.values())
    boards_with_new = len(delta)

    board_names = {}
    async with db.async_session() as session:
        boards = (await session.execute(select(Board))).scalars().all()
        for b in boards:
            board_names[b.code] = b.name

    board_meeting_dates: dict[str, list[str]] = {}
    for code in delta:
        async with db.async_session() as session:
            board = (await session.execute(
                select(Board).where(Board.code == code)
            )).scalar_one_or_none()
            if board:
                meetings = (await session.execute(
                    select(Meeting)
                    .where(Meeting.board_id == board.id)
                    .order_by(Meeting.meeting_date.desc())
                    .limit(delta[code]["new_meetings"])
                )).scalars().all()
                board_meeting_dates[code] = [m.meeting_date.isoformat() for m in meetings]

    lines = [
        f"# Pipeline Run #{run_id} — {today}",
        "",
        "## Summary",
        f"- Boards scanned: {len(delta) + len(no_change_boards)}",
        f"- New meetings found: {total_new_meetings}",
        f"- New documents downloaded: {total_new_docs}",
        f"- Boards with new content: {boards_with_new}",
        "",
    ]

    if delta:
        lines.append("## Delta by Board")
        lines.append("")
        for code, counts in sorted(delta.items()):
            name = board_names.get(code, code)
            dates = board_meeting_dates.get(code, [])
            meeting_word = "meeting" if counts["new_meetings"] == 1 else "meetings"
            doc_word = "document" if counts["new_documents"] == 1 else "documents"
            lines.append(f"### {code} — {name}")
            if dates:
                lines.append(f"- {counts['new_meetings']} new {meeting_word} ({', '.join(dates)})")
            else:
                lines.append(f"- {counts['new_meetings']} new {meeting_word}")
            lines.append(f"- {counts['new_documents']} new {doc_word} downloaded")
            prompt_file = reports_dir / f"{code}_prompt.md"
            if prompt_file.exists():
                lines.append(f"- Prompt file: {prompt_file}")
            lines.append("")

    if no_change_boards:
        lines.append("## Boards with No New Activity")
        lines.append(", ".join(sorted(no_change_boards)))
        lines.append("")

    lines.extend([
        "## Topic Taxonomy",
        "",
        "Assign one or more of these tags to each new document:",
        "",
        ", ".join(f"`{t}`" for t in TOPIC_TAXONOMY),
        "",
        "## Instructions",
        "",
        f"1. **Categorize:** For each new document, read its extracted text and assign topic tags from the taxonomy above. Write results to `data/reports/run_{run_id}_topics.json` as `{{\"document_id\": [\"tag1\", \"tag2\"]}}`",
        f"2. **Ingest topics:** Run `python cli.py pipeline --ingest-topics --run-id {run_id}`",
        f"3. **Summarize:** For each board in Delta above, read its prompt file and write a summary to `data/reports/{{code}}_summary.md`",
        "4. **Ingest summaries:** Run `python cli.py summarize --ingest`",
        f"5. **Write digest:** Generate a \"What's New\" digest to `data/reports/run_{run_id}_digest.md`",
        f"6. **Regenerate report:** Write the updated national landscape report to `data/reports/{today}-board-landscape.md`",
        f"7. **Finalize:** Run `python cli.py pipeline --finalize --run-id {run_id} --digest-path data/reports/run_{run_id}_digest.md --report-path data/reports/{today}-board-landscape.md`",
        "",
    ])

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
