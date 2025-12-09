from typing import Final

import pytest

from aoc25.day_09 import (
    parse_input,
    star_1,
    star_2,
)

_EXAMPLE_INPUT: Final[str] = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


@pytest.fixture
def sample_data():
    return parse_input(_EXAMPLE_INPUT.strip().splitlines())


def test_star_1(sample_data) -> None:
    expected = 50
    actual = star_1(sample_data)

    assert actual == expected


def test_star_2(sample_data) -> None:
    expected = 24  # TODO
    actual = star_2(sample_data)

    assert actual == expected
