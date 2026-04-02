"""CLI smoke tests — verify dispatch functions don't crash."""
import pytest
from datetime import date
from types import SimpleNamespace

from app import database as db
from app.models import Board, Meeting, MeetingDocument


async def _seed_classifiable_data(seed_board):
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        d = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="test.pdf", file_path="/tmp/test.pdf",
            content_text="The board discussed disciplinary actions and license suspensions.",
        )
        session.add(d)
        await session.commit()


async def test_cli_status(seed_board, capsys):
    await seed_board()
    from cli import show_status
    await show_status()
    captured = capsys.readouterr()
    assert "TX_MD" in captured.out


async def test_cli_classify(seed_board, capsys):
    await _seed_classifiable_data(seed_board)
    from cli import handle_classify
    args = SimpleNamespace(pages=False, force=False, min_matches=2)
    await handle_classify(args)
    captured = capsys.readouterr()
    assert "Classifying" in captured.out or "classified" in captured.out.lower()


async def test_cli_classify_force(seed_board, capsys):
    await _seed_classifiable_data(seed_board)
    from cli import handle_classify
    args = SimpleNamespace(pages=False, force=True, min_matches=1)
    await handle_classify(args)
    # No exception = pass


async def test_cli_pipeline_status(capsys):
    from cli import show_pipeline_status
    await show_pipeline_status()
    # Should handle empty run list without error


async def test_cli_pipeline_rebuild_fts(seed_board, capsys):
    await seed_board()
    from cli import handle_pipeline
    args = SimpleNamespace(
        status=False, rebuild_fts=True, ingest_topics=False,
        finalize=False, boards=None, skip_report=False,
        run_id=None, digest_path=None, report_path=None,
    )
    await handle_pipeline(args)
    captured = capsys.readouterr()
    assert "Done" in captured.out or "rebuilt" in captured.out.lower()


async def test_cli_argparse_help():
    import sys
    from cli import main
    sys.argv = ["cli.py", "--help"]
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0
