"""Reset a board's collected data so it can be re-collected fresh.

`collect_board` dedupes at the document level, so after fixing a board's
minutes_url OR the collector itself, use reset() to clear the board's
meetings (+documents) before re-collecting.
"""
import sqlite3

from app.config import DB_PATH


def reset(codes, purge_files: bool = False):
    """Clear a board's meetings + documents rows; optionally its files too.

    purge_files removes data/documents/<CODE>/ entirely — use when the
    downloaded files themselves are bad (portal stubs, wrong documents);
    otherwise valid on-disk files are revalidated and re-registered on the
    next collect.
    """
    con = sqlite3.connect(DB_PATH, timeout=30)
    cur = con.cursor()
    for code in codes:
        row = cur.execute("SELECT id FROM boards WHERE code=?", (code,)).fetchone()
        if not row:
            print(f"  {code}: NOT FOUND")
            continue
        bid = row[0]
        cur.execute(
            "DELETE FROM meeting_documents WHERE meeting_id IN "
            "(SELECT id FROM meetings WHERE board_id=?)", (bid,))
        cur.execute("DELETE FROM meetings WHERE board_id=?", (bid,))
        if purge_files:
            import shutil
            from app.config import DOCUMENTS_DIR
            board_dir = DOCUMENTS_DIR / code
            if board_dir.exists():
                shutil.rmtree(board_dir)
                print(f"  {code}: cleared (files purged)")
                continue
        print(f"  {code}: cleared")
    con.commit()
    con.close()
