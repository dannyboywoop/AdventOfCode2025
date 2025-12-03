from typing import Final

import pytest

from aoc25.day_03 import (
    get_max_joltage,
    star_1,
    star_2,
)

_EXAMPLE_INPUT: Final[str] = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


@pytest.fixture
def sample_data() -> list[str]:
    return _EXAMPLE_INPUT.strip().split()


def test_get_max_joltage_2_batteries(sample_data: list[str]) -> None:
    expected_joltages = [98, 89, 78, 92]
    for bank, expected_joltage in zip(sample_data, expected_joltages):
        assert get_max_joltage(bank) == expected_joltage


def test_get_max_joltage_12_batteries(sample_data: list[str]) -> None:
    expected_joltages = [987654321111, 811111111119, 434234234278, 888911112111]
    for bank, expected_joltage in zip(sample_data, expected_joltages):
        assert get_max_joltage(bank, battery_count=12) == expected_joltage


def test_star_1(sample_data: list[str]) -> None:
    expected = 357
    actual = star_1(sample_data)

    assert actual == expected


def test_star_2(sample_data: list[str]) -> None:
    expected = 3121910778619
    actual = star_2(sample_data)

    assert actual == expected
