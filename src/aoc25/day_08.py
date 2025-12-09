from collections.abc import Iterable, Sequence

from aoc_tools import AdventTimer

from aoc25.common import Pair, Position3D, UniqueIdContainer, product
from aoc25.inputs import get_input_lines

type Positions = list[Position3D]


def parse_input(input_lines: list[str]) -> list[Position3D]:
    return [
        Position3D(int(x), int(y), int(z))
        for x, y, z in (line.split(",") for line in input_lines)
    ]


def find_sorted_pairs(positions: list[Position3D]) -> list[Pair[Position3D]]:
    """
    Brute force search, poor time scaling: O(N^2).
    """
    pairs: list[tuple[float, tuple[int, int]]] = [
        (positions[i].distance2(positions[j]), (i, j))
        for i in range(len(positions) - 1)
        for j in range(i + 1, len(positions))
    ]

    return [(positions[idx_1], positions[idx_2]) for _, (idx_1, idx_2) in sorted(pairs)]


def add_pair_to_circuits(
    pair: Pair[Position3D], circuits: UniqueIdContainer[set[Position3D]]
) -> bool:
    """Updates the circuits with the new pair and returns if a new connection was made."""
    new_connection = set(pair)
    already_connected = False
    added_to_circuits = []
    for idx, circuit in circuits.items():
        overlap = len(circuit & new_connection)
        if overlap == 2:
            already_connected = True
            break
        if overlap == 1:
            circuit |= new_connection  # noqa: PLW2901
            added_to_circuits.append(idx)
    if len(added_to_circuits) == 2:
        circuits.add(
            circuits.pop(added_to_circuits[0]) | circuits.pop(added_to_circuits[1])
        )
    elif len(added_to_circuits) == 0 and not already_connected:
        circuits.add(new_connection)

    return not already_connected


def star_1(
    sorted_pairs: Sequence[Pair[Position3D]], num_positions: int, num_pairs: int = 1000
) -> int:
    circuits: UniqueIdContainer[set[Position3D]] = UniqueIdContainer()

    for pair in sorted_pairs[:num_pairs]:
        if len(circuits) == 1 and len(next(iter(circuits.values()))) == num_positions:
            break  # everything already connected

        add_pair_to_circuits(pair, circuits)

    return product(
        len(circuit)
        for circuit in sorted(iter(circuits.values()), key=len, reverse=True)[:3]
    )


def star_2(sorted_pairs: Iterable[Pair[Position3D]], num_positions: int) -> int:
    circuits: UniqueIdContainer[set[Position3D]] = UniqueIdContainer()
    last_connection_made: Pair[Position3D] | None = None

    for pair in sorted_pairs:
        if len(circuits) == 1 and len(next(iter(circuits.values()))) == num_positions:
            break  # everything already connected

        if add_pair_to_circuits(pair, circuits):
            last_connection_made = pair

    if last_connection_made is None:
        raise RuntimeError("Something went wrong, no connections made!")

    return product(pos.x for pos in last_connection_made)


if __name__ == "__main__":
    timer = AdventTimer()

    input_lines = get_input_lines(day=8)
    positions = parse_input(input_lines)
    pairs = find_sorted_pairs(positions)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(pairs, len(positions))}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(pairs, len(positions))}")
    timer.checkpoint_hit()

    timer.end_hit()
