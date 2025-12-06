from aoc_tools import AdventTimer

from aoc25.inputs import get_input_lines


def star_1(input_lines: list[str]) -> int:
    return 0  # TODO


def star_2(input_lines: list[str]) -> int:
    return 0  # TODO


if __name__ == "__main__":
    timer = AdventTimer()

    input_lines = get_input_lines(day=6)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(input_lines)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(input_lines)}")
    timer.checkpoint_hit()

    timer.end_hit()
