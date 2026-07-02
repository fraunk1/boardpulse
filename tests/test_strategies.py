"""Tests for the per-board strategy layer — pins the no-regression contract."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.scraper.strategies import (  # noqa: E402
    DEFAULT,
    STRATEGIES,
    BoardStrategy,
    chromium_only_codes,
    get_strategy,
)
from app.scraper.seed_data import BOARDS  # noqa: E402

SEED_CODES = {b["code"] for b in BOARDS}


def test_default_strategy_is_inert():
    """The 34 working boards have no entry — their behavior must be stock.

    This is the regression contract for Wave 3: every field of the default
    strategy must be the inert value. If a field is added to BoardStrategy,
    add its inert default here.
    """
    s = get_strategy("ZZ_NOT_A_BOARD")
    assert s is DEFAULT
    assert s.headed is False
    assert s.browser is None
    assert s.depth == 0
    assert s.include_patterns == ()
    assert s.filter_text is None
    assert s.url_probes == ()
    assert s.paginate == 0


def test_strategy_is_frozen():
    import dataclasses
    import pytest
    with pytest.raises(dataclasses.FrozenInstanceError):
        DEFAULT.depth = 1  # type: ignore[misc]


def test_all_strategy_codes_are_valid_board_codes():
    unknown = set(STRATEGIES) - SEED_CODES
    assert not unknown, f"STRATEGIES has codes not in seed data: {unknown}"


def test_headed_and_chromium_boards_in_chromium_only():
    expected = {
        code for code, s in STRATEGIES.items()
        if s.headed or s.browser == "chromium"
    }
    assert chromium_only_codes() == expected


def test_get_strategy_returns_entries():
    probe = BoardStrategy(depth=1)
    STRATEGIES["ZZ_TEST"] = probe
    try:
        assert get_strategy("ZZ_TEST") is probe
    finally:
        del STRATEGIES["ZZ_TEST"]
