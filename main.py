"""Cat Reviews Its Human -- one-star review, one line.

The program writes a single one-star review, written in the voice of a
house cat about its human, to entry.txt inside the output directory
the grader provides. Standard library only, no network, no secrets.
"""

import os
import sys

REVIEW = (
    "One star. My human bought me a bed, then slept in the big one "
    "himself. I have moved into his pillow. He can have the cat bed."
)


def check_review(text):
    """Keep the gate happy: one line, 1 to 200 characters, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("review is empty")
    if len(text) > 200:
        raise ValueError("review is over 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    return text


def resolve_output_dir():
    """Return the directory the grader wants the entry written into."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return chosen
    return os.path.join(os.getcwd(), "output")


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(check_review(REVIEW))
    return 0


if __name__ == "__main__":
    sys.exit(main())
