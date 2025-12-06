from typing import Final

import pytest

from aoc25.day_06 import star_1, star_2

_EXAMPLE_INPUT: Final[str] = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


@pytest.fixture
def sample_data():
    return _EXAMPLE_INPUT.strip().split()


def test_star_1(sample_data) -> None:
    expected = 4277556
    actual = star_1(sample_data)

    assert actual == expected


def test_star_2(sample_data) -> None:
    expected = 0 # TODO
    actual = star_2(sample_data)

    assert actual == expected
