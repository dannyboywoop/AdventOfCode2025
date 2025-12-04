from typing import Final

import pytest

from aoc25.day_04 import Index, parse_grid, star_1, star_2

_EXAMPLE_INPUT: Final[str] = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


@pytest.fixture
def sample_data() -> set[Index]:
    return parse_grid(_EXAMPLE_INPUT.strip().split())


def test_star_1(sample_data: set[Index]) -> None:
    expected = 13
    actual = star_1(sample_data)

    assert actual == expected


def test_star_2(sample_data: set[Index]) -> None:
    expected = 43
    actual = star_2(sample_data)

    assert actual == expected
