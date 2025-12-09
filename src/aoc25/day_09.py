from collections.abc import Iterable
from itertools import combinations, pairwise

from aoc_tools import AdventTimer

from aoc25.common import Pair, Position2D
from aoc25.inputs import get_input_lines

type Positions = list[Position2D]


def parse_input(input_lines: list[str]) -> list[Position2D]:
    return [
        Position2D(int(x), int(y)) for x, y in (line.split(",") for line in input_lines)
    ]


def find_pairs(positions: list[Position2D]) -> Iterable[Pair[Position2D]]:
    yield from combinations(positions, 2)


def calculate_square_size(corners: Pair[Position2D]) -> int:
    return (abs(corners[1].x - corners[0].x) + 1) * (
        abs(corners[1].y - corners[0].y) + 1
    )


def star_1(positions: Iterable[Position2D]) -> int:
    biggest_square = 0
    for pair in find_pairs(positions):
        biggest_square = max(biggest_square, calculate_square_size(pair))

    return biggest_square


class Polygon:
    def __init__(self, positions: Iterable[Position2D]) -> None:
        self._corners = list(positions)
        self._edges: list[Pair[Position2D]] = [
            (first, second) for first, second in pairwise(self._corners)
        ] + [(self._corners[-1], self._corners[0])]
        self._vertical_edges: list[Pair[Position2D]] = [
            edge for edge in self._edges if self.is_vertical(edge)
        ]
        self._horizontal_edges: list[Pair[Position2D]] = [
            edge for edge in self._edges if not self.is_vertical(edge)
        ]

    @staticmethod
    def is_vertical(edge: Pair[Position2D]) -> bool:
        return edge[1].x == edge[0].x

    def is_edge_inside(self, edge: Pair[Position2D]) -> bool:
        del edge
        return True  # TODO


def star_2(positions: Iterable[Position2D]) -> int:
    """My Approach:

    Process the positions to get a list of lines that represent edges of the polygon.
    Create a function that takes a line from 1 red tile to another and checks if it is fully inside the polygon:
        * This will be based on intersection counts
        * The difficulty will be defining intersections along polygon edges/corners
    For every test square, check if all 4 of its sides are fully inside the polygon:
        * If so, calculate its size
        * If not, move on to next test square
    """
    polygon = Polygon(positions)
    biggest_square = 0
    for pair in find_pairs(positions):
        # TODO get edges and check them
        biggest_square = max(biggest_square, calculate_square_size(pair))

    return biggest_square


if __name__ == "__main__":
    timer = AdventTimer()

    input_lines = get_input_lines(day=9)
    positions = parse_input(input_lines)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(positions)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(positions)}")
    timer.checkpoint_hit()

    timer.end_hit()
