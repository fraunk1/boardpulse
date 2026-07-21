"""Re-date month-placeholder meetings from their minutes text.

Some boards list only a month for the current year -- Maryland's 2026 page
says "January 2026 Panel A", with no day. `parse_date` falls back to its
month-only format and yields day=1, so every such link groups under one
placeholder meeting dated the 1st. Where a board meets twice a month (Maryland
runs a Panel A and a Panel B roughly two weeks apart) both sessions merge into
a single meeting on a date the board never met.

The listing cannot be fixed at collect time -- the day simply is not published
there. The minutes PDFs do carry it ("The Board met Wednesday, June 10, 2026"),
so this runs AFTER extraction and moves each minutes document onto its true
meeting, creating that meeting when needed and splitting merged sessions apart
as a side effect.

Two guards keep this from inventing new errors:

* **Minutes only.** Agendas do not state their own date -- they recite the
  PRIOR meeting's minutes for approval, so dating an agenda by its text moves
  it a month backwards. Agendas stay on the placeholder and are re-attached
  when their own minutes appear.
* **Month/year must match the placeholder.** A date extracted from the text is
  only trusted when it falls in the placeholder's own month and year. This
  rejects stray references to other meetings and survives typos in the source:
  Maryland's Feb 2026 Panel B minutes read "met Wednesday, February 25, 2025"
  while the header and four other references say 2026.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import date, datetime

from sqlalchemy import select, text

import app.database as db
from app.models import Board, Meeting, MeetingDocument

logger = logging.getLogger(__name__)

# Fact tables keyed by meeting_id. They have no ORM cascade from Meeting, so a
# dissolved placeholder must clear them explicitly.
_FACT_TABLES = ("policy_actions", "legislation_mentions",
                "emerging_topics", "disciplinary_actions")

# "The Board met Wednesday, June 10, 2026" / "met on June 10, 2026"
_MET_ON = re.compile(
    r"\bmet\s+(?:on\s+)?(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday"
    r"|Sunday)?,?\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})")
# A bare date on its own line near the top -- the minutes' header block.
_HEADER_DATE = re.compile(r"^\s*([A-Z][a-z]+\s+\d{1,2},\s+\d{4})\s*$", re.M)

# How much of the document to inspect. The meeting date always appears in the
# opening block; scanning further only picks up references to other meetings.
_HEAD_CHARS = 1500


@dataclass
class ReattributeResult:
    """What a run changed. Counts are documents unless stated otherwise."""
    scanned: int = 0
    moved: int = 0
    meetings_created: int = 0
    placeholders_removed: int = 0
    skipped_no_date: int = 0
    skipped_month_mismatch: int = 0
    details: list[str] = field(default_factory=list)

    def summary(self) -> str:
        return (f"scanned={self.scanned} moved={self.moved} "
                f"created={self.meetings_created} "
                f"placeholders_removed={self.placeholders_removed} "
                f"no_date={self.skipped_no_date} "
                f"month_mismatch={self.skipped_month_mismatch}")


def is_redate_candidate(meeting_date: date) -> bool:
    """True when a meeting sits on day 1 and is worth checking against its text.

    Deliberately does NOT consult the title. Placeholder titles are generated
    FROM the placeholder date ("Maryland Board of Physicians — June 01, 2026"),
    so the title reads as an explicit 1st and cannot serve as evidence either
    way -- it is circular.

    Boards really do meet on the 1st, and that is safe here: such a meeting's
    minutes say so, `extract_meeting_date` returns the same date, and the caller
    skips it. The document text is the evidence, not the date's shape.
    """
    return meeting_date.day == 1


def extract_meeting_date(text: str, expect: date) -> date | None:
    """Pull the true meeting date out of minutes *text*.

    *expect* is the placeholder's month/year. A candidate is accepted only when
    it falls in that same month and year, which rejects references to other
    meetings and source typos in the year.
    """
    if not text:
        return None
    head = text[:_HEAD_CHARS]
    candidates: list[str] = []
    m = _MET_ON.search(head)
    if m:
        candidates.append(m.group(1))
    candidates.extend(_HEADER_DATE.findall(head))

    for raw in candidates:
        try:
            got = datetime.strptime(raw.strip(), "%B %d, %Y").date()
        except ValueError:
            continue
        if got.year == expect.year and got.month == expect.month:
            return got
    return None


async def reattribute_placeholder_meetings(
    board_code: str | None = None,
    dry_run: bool = False,
) -> ReattributeResult:
    """Move minutes off month-placeholder meetings onto their true dates.

    Pass *board_code* to limit the scan to one board; ``None`` scans every
    board. With *dry_run* the database is left untouched and the result still
    reports what would change.
    """
    result = ReattributeResult()

    async with db.async_session() as session:
        q = select(Meeting, Board).join(Board, Meeting.board_id == Board.id)
        if board_code:
            q = q.where(Board.code == board_code.upper())
        rows = (await session.execute(q)).all()

        placeholders = [
            (m, b) for m, b in rows if is_redate_candidate(m.meeting_date)
        ]
        if not placeholders:
            return result

        for meeting, board in placeholders:
            moved_here = 0
            docs = (await session.execute(
                select(MeetingDocument).where(
                    MeetingDocument.meeting_id == meeting.id)
            )).scalars().all()

            for doc in docs:
                # Agendas recite the PRIOR meeting's date -- never trust them.
                if (doc.doc_type or "").lower() != "minutes":
                    continue
                result.scanned += 1
                if not doc.content_text:
                    result.skipped_no_date += 1
                    continue

                real = extract_meeting_date(doc.content_text,
                                            meeting.meeting_date)
                if real is None:
                    # Distinguish "no date at all" from "found the wrong month".
                    if _MET_ON.search(doc.content_text[:_HEAD_CHARS]) or \
                            _HEADER_DATE.search(doc.content_text[:_HEAD_CHARS]):
                        result.skipped_month_mismatch += 1
                    else:
                        result.skipped_no_date += 1
                    continue
                if real == meeting.meeting_date:
                    continue

                result.details.append(
                    f"{board.code}: {doc.filename} "
                    f"{meeting.meeting_date} -> {real}")
                if dry_run:
                    result.moved += 1
                    continue

                target = (await session.execute(
                    select(Meeting).where(
                        Meeting.board_id == board.id,
                        Meeting.meeting_date == real,
                    )
                )).scalar_one_or_none()

                if target is None:
                    target = Meeting(
                        board_id=board.id,
                        meeting_date=real,
                        title=f"{board.name} — {real.strftime('%B %d, %Y')}",
                        meeting_type=meeting.meeting_type,
                        source_url=meeting.source_url,
                        scraped_at=meeting.scraped_at,
                    )
                    session.add(target)
                    await session.flush()
                    result.meetings_created += 1

                doc.meeting_id = target.id
                result.moved += 1
                moved_here += 1

            if dry_run:
                continue

            # Only dissolve a placeholder THIS RUN emptied. A day-1 meeting
            # that already had no documents is not our business: boards
            # legitimately publish scheduled meetings whose minutes have not
            # appeared yet (future-dated rows), and deleting those would
            # silently drop known upcoming meetings from the dashboard.
            if not moved_here:
                continue

            # A placeholder that has given up all its documents described a
            # meeting that never happened -- drop it, and with it any summary
            # written from the merged content.
            await session.flush()
            remaining = (await session.execute(
                select(MeetingDocument).where(
                    MeetingDocument.meeting_id == meeting.id)
            )).scalars().all()
            if not remaining:
                # Facts reference meeting_id by FK with no ORM cascade, and
                # SQLite does not enforce foreign keys by default -- deleting
                # the meeting alone would silently orphan them. They were
                # extracted from documents that have since moved to their real
                # meetings, and a fact's quote cannot be traced back to which
                # one, so they are dropped for re-extraction rather than
                # re-pointed.
                for table in _FACT_TABLES:
                    await session.execute(
                        text(f"DELETE FROM {table} WHERE meeting_id = :mid"),
                        {"mid": meeting.id})
                await session.delete(meeting)
                result.placeholders_removed += 1

        if not dry_run:
            await session.commit()

    logger.info("reattribute: %s", result.summary())
    return result
