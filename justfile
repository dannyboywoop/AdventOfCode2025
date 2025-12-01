# This file contains various useful commands to be run via [just](https://just.systems)

check:
  uv run python -m mypy .
  uv run python -m ruff check .

fix: fmt
  uv run python -m ruff check . --fix

fmt:
  uv run ruff format . 

fmt-check:
  uv run ruff format . --check

install:
  uv sync

test +args="":
  uv run python -m pytest . {{args}}


