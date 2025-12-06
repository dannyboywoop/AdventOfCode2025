from aoc_tools import AdventTimer
from operator import add, mul

from aoc25.inputs import get_input_lines


def parse_problems(input_lines: list[str]) -> tuple[list[tuple], list[str]]:
    problems: list[tuple] = list(
        zip(*([int(val) for val in line.split()] for line in input_lines[:-1]))
    )
    symbols: list[str] = [val for val in input_lines[-1].split()]
    return problems, symbols


def star_1(input_lines: list[str]) -> int:
    grid = list(zip(*([int(val) for val in line.split()] for line in input_lines[:-1])))
    symbols = [val for val in input_lines[-1].split()]
    total = 0
    for i, numbers in enumerate(grid):
        if symbols[i] == "+":
            operation = add
            col_result = 0
        elif symbols[i] == "*":
            operation = mul
            col_result = 1
        else:
            raise ValueError(f"Invalid operator: {symbols[i]}")

        for number in numbers:
            col_result = operation(col_result, number)

        total += col_result

    return total


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
