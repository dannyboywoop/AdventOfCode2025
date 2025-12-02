from pathlib import Path
from typing import Final

_INPUT_PATH: Final[Path] = Path(__file__).parent.parent.parent / "inputs"


def get_input_filepath(*, day: int) -> Path:
    return _INPUT_PATH / f"day_{day:02}.txt"


def get_input_lines(*, day: int) -> list[str]:
    return get_input_filepath(day=day).read_text().strip().split()
