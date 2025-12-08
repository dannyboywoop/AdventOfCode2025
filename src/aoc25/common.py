from collections.abc import ItemsView, Iterable, ValuesView
from functools import reduce
from operator import mul
from typing import Protocol, Self


class SupportsMul(Protocol):
    def __mul__(self, other: Self) -> Self: ...


def product[T: SupportsMul](iterable: Iterable[T]) -> T:
    return reduce(mul, iterable)


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
