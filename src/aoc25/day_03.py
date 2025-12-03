from collections.abc import Sequence

from aoc_tools import AdventTimer

from aoc25.inputs import get_input_lines


def get_max_and_index[T](sequence: Sequence[T]) -> tuple[T, int]:
    """
    Get the maximum value from an sequence and its index.
    The index returned is for the FIRST instance of the max value in the sequence.

    Type `T` must define `__gt__`.
    """
    max_val = sequence[0]
    index = 0
    for i, val in enumerate(sequence):
        if val > max_val:  # type: ignore[operator]
            max_val = val
            index = i

    return max_val, index


def get_max_joltage(bank: str, battery_count: int = 2) -> int:
    if len(bank) < battery_count:
        raise ValueError("Not enough batteries in bank!")

    digits: list[str] = []
    previous_battery_idx: int = -1
    for digit_idx in range(battery_count):
        # digit must be after the previous digit, but not all the way to the end of the bank
        # (must leave space for remaining batteries)
        max_index = (
            digit_idx + 1 - battery_count if digit_idx < battery_count - 1 else None
        )
        new_digit, new_index = get_max_and_index(
            bank[previous_battery_idx + 1 : max_index]
        )
        digits.append(new_digit)
        previous_battery_idx += new_index + 1

    return int("".join(digits))


def star_1(battery_banks: list[str]) -> int:
    return sum(get_max_joltage(bank) for bank in battery_banks)


def star_2(battery_banks: list[str]) -> int:
    return sum(get_max_joltage(bank, battery_count=12) for bank in battery_banks)


if __name__ == "__main__":
    timer = AdventTimer()

    battery_banks = get_input_lines(day=3)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(battery_banks)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(battery_banks)}")
    timer.checkpoint_hit()

    timer.end_hit()
