from typing import Final

import pytest

from aoc25.day_01 import crack_password

_EXAMPLE_INPUT: Final[str] = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


@pytest.fixture
def sample_data() -> list[str]:
    return _EXAMPLE_INPUT.strip().split()


def test_crack_password(sample_data: list[str]) -> None:
    expected_star_1 = 3
    expected_star_2 = 6
    star_1, star_2 = crack_password(sample_data)

    assert star_1 == expected_star_1
    assert star_2 == expected_star_2
