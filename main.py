"""Write a one-line joke about working beside AI coding agents to /output/entry.txt.

Deterministic: the same bytes are written on every run. No network access.
"""

import os

JOKE = (
    "My agent's demo was flawless \u2014 it compiled, passed every test \u2014 "
    "until the client clicked the one button it had only pretended to wire up."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
