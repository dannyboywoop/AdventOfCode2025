from functools import cache
from itertools import product
from typing import Final, NamedTuple

from aoc_tools import AdventTimer

from aoc25.inputs import get_input_lines


class Offset(NamedTuple):
    row_delta: int
    col_delta: int


_ADJACENT_OFFSETS: Final[list[Offset]] = [
    Offset(i, j) for i, j in product((-1, 0, 1), (-1, 0, 1)) if i != 0 or j != 0
]


class Index(NamedTuple):
    row: int
    col: int

    @cache
    def get_adjacent_indices(self) -> list["Index"]:
        return [
            Index(self.row + offset.row_delta, self.col + offset.col_delta)
            for offset in _ADJACENT_OFFSETS
        ]


def parse_grid(grid_lines: list[str]) -> set[Index]:
    return {
        Index(i, j)
        for i, row in enumerate(grid_lines)
        for j, char in enumerate(row)
        if char == "@"
    }


def get_adjacent_rolls(roll_indices: set[Index], roll_index: Index) -> set[Index]:
    return {
        adjacent_index
        for adjacent_index in roll_index.get_adjacent_indices()
        if adjacent_index in roll_indices
    }


def star_1(roll_indices: set[Index]) -> int:
    accessible_roll_count: int = 0
    for index in roll_indices:
        neighbours_with_rolls = get_adjacent_rolls(roll_indices, index)
        accessible_roll_count += len(neighbours_with_rolls) < 4
    return accessible_roll_count


def star_2(roll_indices: set[Index]) -> int:
    # start with all roll indices
    remaining_rolls = roll_indices.copy()
    potentially_removable_rolls: set[Index] = remaining_rolls.copy()
    original_roll_count = len(remaining_rolls)

    # loop until there are no rolls that can be removed
    while potentially_removable_rolls:
        affected_rolls: set[Index] = set()

        # check each potentially removable roll
        for roll_to_check in potentially_removable_rolls:
            neighbours_with_rolls = get_adjacent_rolls(remaining_rolls, roll_to_check)

            if len(neighbours_with_rolls) < 4:
                remaining_rolls.remove(roll_to_check)
                affected_rolls |= neighbours_with_rolls

        # rolls adjacent to removed rolls may now be removable
        potentially_removable_rolls = affected_rolls & remaining_rolls

    return original_roll_count - len(remaining_rolls)


if __name__ == "__main__":
    timer = AdventTimer()

    grid_lines = get_input_lines(day=4)
    roll_indices = parse_grid(grid_lines)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(roll_indices)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(roll_indices)}")
    timer.checkpoint_hit()

    timer.end_hit()
