from typing import Final

import pytest

from aoc25.day_07 import (
    parse_input,
    star_1,
    star_2,
)

_EXAMPLE_INPUT: Final[str] = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


@pytest.fixture
def sample_data():
    return parse_input(_EXAMPLE_INPUT.strip().splitlines())


def test_star_1(sample_data) -> None:
    expected = 21
    actual = star_1(sample_data)

    assert actual == expected


def test_star_2(sample_data) -> None:
    expected = 40
    actual = star_2(sample_data)

    assert actual == expected
