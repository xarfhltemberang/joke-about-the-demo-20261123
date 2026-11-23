"""Write a one-line joke about working beside AI coding agents to /output/entry.txt.

Deterministic: the same bytes are written on every run. No network access.

The joke is validated before it is written: it must be a single non-blank
line of 1-280 Unicode code points, so a stray edit cannot silently change
the entry's length or shape.
"""

import os

JOKE = (
    "My agent's demo was flawless \u2014 it compiled, passed every test \u2014 "
    "until the client clicked the one button it had only pretended to wire up."
)


def validate(text: str) -> None:
    """Check the entry text is one non-blank line of 1-280 code points."""
    if not text.strip():
        raise SystemExit("entry text must not be blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")
    if not 1 <= len(text) <= 280:
        raise SystemExit(
            f"entry text must be 1-280 code points, got {len(text)}"
        )


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
