from aoc_tools import AdventTimer
from operator import add, mul

from aoc25.inputs import get_input_lines


def star_1(input_lines: list[str]) -> int:
    grid = [[int(val) for val in line.split()] for line in input_lines[:-1]]
    symbols = [val for val in input_lines[-1].split()]
    num_rows = len(grid)
    num_cols = len(grid[0])
    total = 0
    for col in range(num_cols):
        if symbols[col] == "+":
            operation = add
            col_result = 0
        elif symbols[col] == "*":
            operation = mul
            col_result = 1
        else:
            raise ValueError(f"Invalid operator: {symbols[col]}")

        for row in range(num_rows):
            col_result = operation(col_result, grid[row][col])

        total += col_result

    return total


def star_2(input_lines: list[str]) -> int:
    grid = [[int(val) for val in line.split()] for line in input_lines[:-1]]
    symbols = [val for val in input_lines[-1].split()]
    num_rows = len(grid)
    num_cols = len(grid[0])
    total = 0
    for col in range(num_cols):
        if symbols[col] == "+":
            operation = add
            col_result = 0
        elif symbols[col] == "*":
            operation = mul
            col_result = 1
        else:
            raise ValueError(f"Invalid operator: {symbols[col]}")

        # TODO calculate column result

        total += col_result

    return total


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
