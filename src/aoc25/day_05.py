from typing import NamedTuple, TypeAlias

from aoc_tools import AdventTimer

from aoc25.inputs import get_input_text


class Range(NamedTuple):
    """
    Helper class to hold ranges.
    Deliberately using a NamedTuple as tuples sort into lexicographic by default.
    """

    lower: int
    upper: int


Ranges: TypeAlias = list[Range]
Ingredients: TypeAlias = list[int]


def parse_ingredient_database(input_text: str) -> tuple[Ranges, Ingredients]:
    ranges_text, ingredients_text = input_text.split("\n\n")
    ranges = [
        Range(int(lower), int(upper))
        for lower, upper in (
            range_str.split("-") for range_str in ranges_text.strip().split()
        )
    ]
    ingredients = [int(line) for line in ingredients_text.strip().split()]
    return (ranges, ingredients)


def ingredient_is_fresh(
    sorted_fresh_ingredient_ranges: Ranges, ingredient: int
) -> bool:
    for ingredient_range in sorted_fresh_ingredient_ranges:
        if ingredient >= ingredient_range.lower:
            if ingredient <= ingredient_range.upper:
                return True
        else:
            # definitely not in the rest of the ranges, can stop looking
            break
    return False


def star_1(database: tuple[Ranges, Ingredients]) -> int:
    """
    Basic solution to first star.
    Time complexity is O(N*M) where N is the number of ingredients and M is the number of ranges.
    Could make it O(NlogM) by sorted (and merging) ranges up front (O(MlogM)) and then performing a binary search to check each ingredient (O(NlogM))

    I may come back and implement that if I can be bothered, but it is plenty fast with the shortcutting I've implemented already.
    """

    fresh_ingredient_count = 0
    ingredient_ranges, ingredients = database
    ingredient_ranges.sort()
    for ingredient in ingredients:
        fresh_ingredient_count += ingredient_is_fresh(ingredient_ranges, ingredient)

    return fresh_ingredient_count


def star_2(database: tuple[Ranges, Ingredients]) -> int:
    fresh_ingredient_count = 0
    ingredient_ranges, _ = database
    ingredient_ranges.sort()

    lower_pointer, upper_pointer = 0, -1
    for ingredient_range in ingredient_ranges:
        # does this range start AFTER the current range ends
        if ingredient_range.lower > upper_pointer:
            # gap found, record previous merged range and update to new range
            fresh_ingredient_count += upper_pointer - lower_pointer + 1
            lower_pointer, upper_pointer = ingredient_range
        # else does this range EXTEND the upper bound of the current range
        elif ingredient_range.upper > upper_pointer:
            upper_pointer = ingredient_range.upper

    # add final range
    fresh_ingredient_count += upper_pointer - lower_pointer + 1
    return fresh_ingredient_count


if __name__ == "__main__":
    timer = AdventTimer()

    input_text = get_input_text(day=5)
    database = parse_ingredient_database(input_text)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(database)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(database)}")
    timer.checkpoint_hit()

    timer.end_hit()
