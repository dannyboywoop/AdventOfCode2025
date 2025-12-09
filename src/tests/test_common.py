from aoc25.common import Position2D, Position3D


def test_position_distance2() -> None:
    assert Position2D(1, 2).distance2(Position2D(3, 4)) == 8
    assert Position3D(1, 2, 3).distance2(Position3D(4, 5, 6)) == 27


def test_position_add() -> None:
    assert Position2D(1, 2) + Position2D(3, 4) == Position2D(4, 6)
    assert Position3D(1, 2, 3) + Position3D(4, 5, 6) == Position3D(5, 7, 9)


def test_position_sub() -> None:
    assert Position2D(4, 6) - Position2D(3, 4) == Position2D(1, 2)
    assert Position3D(5, 7, 9) - Position3D(4, 5, 6) == Position3D(1, 2, 3)
