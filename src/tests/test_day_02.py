from typing import Final

import pytest

from aoc25.day_02 import (
    Range,
    get_invalid_ids,
    get_numbers_with_repetitions,
    parse_input,
    star_1,
    star_2,
)

_EXAMPLE_INPUT: Final[str] = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""


@pytest.fixture
def sample_data() -> list[Range]:
    return parse_input(_EXAMPLE_INPUT)


def test_get_numbers_with_repetitions_2_repetitions(sample_data: list[Range]) -> None:
    """Test get_numbers_with_repetitions with repetitions set to 2."""
    expected_outputs: list[list[int]] = [
        [11, 22],
        [99],
        [1010],
        [1188511885],
        [222222],
        [],
        [446446],
        [38593859],
        [],
        [],
        [],
    ]

    for num_range, expected_ids in zip(sample_data, expected_outputs, strict=True):
        assert list(sorted(get_numbers_with_repetitions(num_range, 2))) == expected_ids


def test_get_numbers_with_repetitions_3_repetitions() -> None:
    """Test get_numbers_with_repetitions with repetitions set to 3."""
    expected = [565656]
    actual = list(get_numbers_with_repetitions(Range(565653, 565659), repetitions=3))

    assert actual == expected


def test_get_all_invalid_numbers(sample_data: list[Range]) -> None:
    expected_outputs: list[list[int]] = [
        [11, 22],
        [99, 111],
        [999, 1010],
        [1188511885],
        [222222],
        [],
        [446446],
        [38593859],
        [565656],
        [824824824],
        [2121212121],
    ]
    for num_range, expected_ids in zip(sample_data, expected_outputs, strict=True):
        assert list(sorted(get_invalid_ids(num_range))) == expected_ids


def test_star_1(sample_data: list[Range]) -> None:
    expected = 1227775554
    actual = star_1(sample_data)

    assert actual == expected


def test_star_2(sample_data: list[Range]) -> None:
    expected = 4174379265
    actual = star_2(sample_data)

    assert actual == expected
