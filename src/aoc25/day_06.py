from collections.abc import Iterable
from itertools import zip_longest
from operator import add, mul

from aoc_tools import AdventTimer

from aoc25.inputs import get_input_lines


class Problem:
    def __init__(self, numbers: Iterable[int], operator: str) -> None:
        self._numbers = numbers
        if operator == "+":
            self._operation = add
            self._identity = 0
        elif operator == "*":
            self._operation = mul
            self._identity = 1
        else:
            raise ValueError(f"Invalid operator: {operator}")

    def solve_method_1(self) -> int:
        result = self._identity
        for number in self._numbers:
            result = self._operation(result, number)

        return result

    def solve_method_2(self) -> int:
        result = self._identity

        # NOTE: This doesn't work as I didn't realise the alignment varies from question to question
        # I assumed they were all left alligned (as the first example was)
        actual_numbers_strs = zip_longest(
            *(str(num) for num in self._numbers), fillvalue=str(self._identity)
        )
        actual_numbers = [int("".join(digits)) for digits in actual_numbers_strs]

        for number in actual_numbers:
            result = self._operation(result, number)
        return result


def parse_problems(input_lines: list[str]) -> list[Problem]:
    problem_inputs: list[Iterable[int]] = list(
        zip(
            *([int(val) for val in line.split()] for line in input_lines[:-1]),
            strict=True,
        )
    )
    operators: list[str] = input_lines[-1].split()
    return [
        Problem(numbers, operator)
        for numbers, operator in zip(problem_inputs, operators, strict=True)
    ]


def star_1(problems: list[Problem]) -> int:
    return sum(problem.solve_method_1() for problem in problems)


def star_2(problems: list[Problem]) -> int:
    return sum(problem.solve_method_2() for problem in problems)


if __name__ == "__main__":
    timer = AdventTimer()

    input_lines = get_input_lines(day=6)
    problems = parse_problems(input_lines)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(problems)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(problems)}")
    timer.checkpoint_hit()

    timer.end_hit()
