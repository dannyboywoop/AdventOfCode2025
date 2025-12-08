from typing import Final

import pytest

from aoc25.day_08 import find_sorted_pairs, parse_input, star_1, star_2

_EXAMPLE_INPUT: Final[str] = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


@pytest.fixture
def sample_data():
    return parse_input(_EXAMPLE_INPUT.strip().splitlines())


def test_star_1(sample_data) -> None:
    expected = 40
    actual = star_1(find_sorted_pairs(sample_data), len(sample_data), num_pairs=10)

    assert actual == expected


def test_star_2(sample_data) -> None:
    expected = 25272
    actual = star_2(find_sorted_pairs(sample_data), len(sample_data))

    assert actual == expected
