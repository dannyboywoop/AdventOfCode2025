from typing import Final

import pytest

from aoc25.day_05 import (
    Ranges,
    Ingredients,
    parse_ingredient_database,
    star_1,
    star_2,
    get_sorted_nonoverlapping_ranges,
)

_EXAMPLE_INPUT: Final[str] = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


@pytest.fixture
def sample_data() -> tuple[Ranges, Ingredients]:
    return parse_ingredient_database(_EXAMPLE_INPUT)


def test_star_1(sample_data: tuple[Ranges, Ingredients]) -> None:
    ranges, ingredients = sample_data
    expected = 3
    actual = star_1(get_sorted_nonoverlapping_ranges(ranges), ingredients)

    assert actual == expected


def test_star_2(sample_data: tuple[Ranges, Ingredients]) -> None:
    ranges, _ = sample_data
    expected = 14
    actual = star_2(get_sorted_nonoverlapping_ranges(ranges))

    assert actual == expected
