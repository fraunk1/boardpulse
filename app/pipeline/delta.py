"""Delta calculation — snapshot board counts before/after collection."""
from sqlalchemy import select, func

import app.database as db
from app.models import Board, Meeting, MeetingDocument


async def snapshot_board_counts() -> dict[str, dict[str, int]]:
    """Return {board_code: {meetings: N, documents: N}} for all boards."""
    async with db.async_session() as session:
        boards = (await session.execute(select(Board))).scalars().all()

        result = {}
        for board in boards:
            meeting_count = (await session.execute(
                select(func.count(Meeting.id)).where(Meeting.board_id == board.id)
            )).scalar() or 0

            doc_count = (await session.execute(
                select(func.count(MeetingDocument.id))
                .where(MeetingDocument.meeting_id.in_(
                    select(Meeting.id).where(Meeting.board_id == board.id)
                ))
            )).scalar() or 0

            result[board.code] = {"meetings": meeting_count, "documents": doc_count}

    return result


def compute_delta(
    before: dict[str, dict[str, int]],
    after: dict[str, dict[str, int]],
) -> dict[str, dict[str, int]]:
    """Compute the difference between two snapshots.

    Returns {board_code: {new_meetings: N, new_documents: N}} for boards
    that gained meetings or documents. Boards with no change are omitted.
    """
    delta = {}
    for code, after_counts in after.items():
        before_counts = before.get(code, {"meetings": 0, "documents": 0})
        new_meetings = after_counts["meetings"] - before_counts["meetings"]
        new_documents = after_counts["documents"] - before_counts["documents"]
        if new_meetings > 0 or new_documents > 0:
            delta[code] = {"new_meetings": new_meetings, "new_documents": new_documents}
    return delta
