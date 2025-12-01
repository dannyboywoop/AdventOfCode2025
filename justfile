# This file contains various useful commands to be run via [just](https://just.systems)

check:
  uv run mypy .
  uv run ruff check .

fix: fmt
  uv run ruff check . --fix

fmt:
  uv run ruff format . 

fmt-check:
  uv run ruff format . --check

install:
  uv sync

test +args="":
  uv run pytest . {{args}}


