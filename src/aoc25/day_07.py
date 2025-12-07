import re
from functools import cache
from typing import Final

from aoc_tools import AdventTimer

from aoc25.inputs import get_input_lines

_SPLITTER_PATTERN: Final[re.Pattern] = re.compile(r"\^")


def parse_input(input_lines: list[str]) -> tuple[int, tuple[set[int], ...]]:
    start_position: int = input_lines[0].find("S")
    splitter_positions: tuple[set[int], ...] = tuple(
        {match.start() for match in _SPLITTER_PATTERN.finditer(line)}
        for line in input_lines[2::2]  # only care about every-other line
    )

    return start_position, splitter_positions


def star_1(puzzle_input: tuple[int, tuple[set[int], ...]]) -> int:
    start_position, splitter_layers = puzzle_input
    beam_positions: set[int] = set([start_position])
    split_count = 0

    for splitter_positions in splitter_layers:
        # get new splits
        splits = splitter_positions & beam_positions
        split_count += len(splits)

        # create new beams
        new_beams = set()
        for split in splits:
            new_beams.update([split - 1, split + 1])
        beam_positions = (beam_positions | new_beams) - splits

    return split_count


def star_2(puzzle_input: tuple[int, tuple[set[int], ...]]) -> int:
    start_position, splitter_layers = puzzle_input

    @cache
    def get_number_of_paths(beam_pos: int, remaining_splitter_layers: int) -> int:
        if remaining_splitter_layers == 0:
            return 1

        # if beam split in next layer
        if beam_pos in splitter_layers[-remaining_splitter_layers]:
            return get_number_of_paths(
                beam_pos - 1, remaining_splitter_layers - 1
            ) + get_number_of_paths(beam_pos + 1, remaining_splitter_layers - 1)

        return get_number_of_paths(beam_pos, remaining_splitter_layers - 1)

    return get_number_of_paths(start_position, len(splitter_layers))


if __name__ == "__main__":
    timer = AdventTimer()

    input_lines = get_input_lines(day=7)
    puzzle_input = parse_input(input_lines)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(puzzle_input)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(puzzle_input)}")
    timer.checkpoint_hit()

    timer.end_hit()
