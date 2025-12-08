from collections.abc import Iterator
from dataclasses import dataclass

from aoc_tools import AdventTimer

from aoc25.inputs import get_input_text


@dataclass
class Range:
    lower: int
    upper: int


def parse_input(input_text: str) -> list[Range]:
    pair_strings: list[str] = input_text.split(",")
    ranges: list[Range] = []
    for pair_str in pair_strings:
        lower, upper = pair_str.split("-")
        ranges.append(Range(lower=int(lower), upper=int(upper)))

    return ranges


def get_numbers_with_repetitions(
    num_range: Range, repetitions: int = 2
) -> Iterator[int]:
    lower_str = str(num_range.lower)
    digits = len(lower_str)
    repetition_size, remainder = divmod(digits, repetitions)
    if remainder:  # number of digits not divisible by repetitions
        left_part = "1" + "0" * repetition_size
    else:
        left_part = lower_str[:repetition_size]

    while True:
        test_value = int(left_part * repetitions)

        if test_value <= num_range.upper:
            if test_value >= num_range.lower:
                yield test_value
            left_part = str(int(left_part) + 1)
        else:
            break


def get_invalid_ids(num_range: Range) -> Iterator[int]:
    yield from {
        invalid_id
        for reps in range(2, len(str(num_range.upper)) + 1)
        for invalid_id in get_numbers_with_repetitions(num_range, repetitions=reps)
    }


def star_1(ranges: list[Range]) -> int:
    return sum(
        invalid_id
        for num_range in ranges
        for invalid_id in get_numbers_with_repetitions(num_range, repetitions=2)
    )


def star_2(ranges: list[Range]) -> int:
    return sum(
        invalid_id for num_range in ranges for invalid_id in get_invalid_ids(num_range)
    )


if __name__ == "__main__":
    timer = AdventTimer()

    text = get_input_text(day=2)
    ranges = parse_input(text)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(ranges)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(ranges)}")
    timer.checkpoint_hit()

    timer.end_hit()
