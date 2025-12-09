from collections import namedtuple
from collections.abc import ItemsView, Iterable, ValuesView
from functools import reduce
from operator import add, mul, sub
from typing import Protocol, Self


class SupportsMul(Protocol):
    def __mul__(self, other: Self) -> Self: ...


def product[T: SupportsMul](iterable: Iterable[T]) -> T:
    return reduce(mul, iterable)


class Position:
    def distance2(self, other: Self) -> float:
        return sum((c1 - c2) ** 2 for c1, c2 in zip(self, other, strict=True))

    def __add__(self, other: object) -> Self:
        if not isinstance(other, type(self)):
            raise NotImplementedError
        return type(self)(*map(add, self, other))

    def __sub__(self, other: object) -> Self:
        if not isinstance(other, type(self)):
            raise NotImplementedError
        return type(self)(*map(sub, self, other))


class Position2D(Position, namedtuple("Position2D", ["x", "y"])):  # noqa: PYI024
    __slots__ = ()


class Position3D(Position, namedtuple("Position3D", ["x", "y", "z"])):  # noqa: PYI024
    __slots__ = ()


type Pair[T] = tuple[T, T]


class UniqueIdContainer[V]:
    def __init__(self, data: Iterable[V] | None = None) -> None:
        self._data = dict(enumerate(data)) if data is not None else {}
        self._last_id = len(self._data) - 1

    def add(self, val: V) -> int:
        self._last_id += 1
        self._data[self._last_id] = val
        return self._last_id

    def pop(self, key: int) -> V:
        return self._data.pop(key)

    def __getitem__(self, key: int) -> V:
        return self._data[key]

    def __setitem__(self, key: int, val: V) -> None:
        if key in self._data:
            self._data[key] = val
        else:
            raise KeyError(f"Key not found: {key}")

    def items(self) -> ItemsView[int, V]:
        return self._data.items()

    def values(self) -> ValuesView[V]:
        return self._data.values()

    def __len__(self) -> int:
        return len(self._data)
