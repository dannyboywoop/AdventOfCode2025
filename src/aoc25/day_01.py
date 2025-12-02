from aoc_tools import AdventTimer

from aoc25.inputs import get_input_lines


class Dial:
    def __init__(self, initial_position: int = 50, size: int = 100) -> None:
        self._position: int = 50
        self._size: int = size
        self._times_on_zero: int = int(initial_position == 0)

    @property
    def position(self) -> int:
        return self._position

    @property
    def times_on_zero(self) -> int:
        return self._times_on_zero

    def rotate(self, rotation: str) -> None:
        if len(rotation) < 2:
            raise ValueError(f"Invalid rotation string: {rotation}")

        direction, clicks = rotation[0], int(rotation[1:])
        old_position = self._position

        # rotate dial
        match direction:
            case "L":
                self._position -= clicks
            case "R":
                self._position += clicks
            case _:
                raise ValueError(f"Invalid rotation string: {rotation}")
        div, self._position = divmod(self._position, self._size)

        # calculate times on zero
        self._times_on_zero += abs(div)
        if direction == "L":
            if self._position == 0:
                self._times_on_zero += 1
            elif old_position == 0:
                self._times_on_zero -= 1


def crack_password(lines: list[str]) -> tuple[int, int]:
    dial = Dial()
    count: int = 0
    for line in lines:
        dial.rotate(line)
        if dial.position == 0:
            count += 1
    return count, dial.times_on_zero


if __name__ == "__main__":
    timer = AdventTimer()

    lines = get_input_lines(day=1)
    print("Input parsed!")
    timer.checkpoint_hit()

    star_01, star_02 = crack_password(lines)
    print(f"Star_01: {star_01}")
    print(f"Star_02: {star_02}")
    timer.checkpoint_hit()

    timer.end_hit()
