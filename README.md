# [AdventOfCode 2025](https://adventofcode.com/2025)
AdventOfCode is a yearly event for which a new, two-part, coding challenge is released each day of December until the 25th.

I have struggled to find the time to do the previous two years, and with a busy december ahead I don't expect to get much more time this year.
That being said I am going to make an effort to make time to do the problems in python at least.

If I find myself with the time available, or perhaps in the new year, I will also attempt to produce solutions in Rust.
As always, I will try to make my python solutions readable, maintainable and efficient, but I will not be spending excessive time on them.
I am (completely) new to rust, so any solutions I implement in Rust are likely to be "odd" as I try to expose myself to as much of the language as possible.
I will not be using AI of any kind, as it's not really in the spirit of the event.

Here is the current status of my solutions:

| Day | Star | Solved in Python | Solved in Rust |
| --- | ---- | ---------------- | ------------- |
| 01 | 01 | No | No |

Some python solutions will import modules from my aoc_tools package, you will need to install this using:
```pip install aoc-tools-dannyboywoop```

(Or you can install the dependencies with [`uv`](https://docs.astral.sh/uv/)).

## Setup

* Install [`uv`](https://docs.astral.sh/uv/)
* Install [`just`](https://just.systems/man/en/) with `cargo install just`
* Run `just install` to install various package dependencies
* Run `just check` to run linters
* Run `just test` to run tests
* Run `just fmt` to format code