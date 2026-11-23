#!/usr/bin/env python3
"""One Line, Best Line — entry program.

Writes the single entry line to /output/entry.txt (the harness artifact)
and prints it to stdout. The line is one line of text, well under the
240-character cap, on a free and entertaining theme.
"""

import os

LINE = (
    "My cat pays no rent, breaks my stuff, and sleeps 16 hours a day "
    "\u2014 I've never respected a business model more."
)


def get_line() -> str:
    """Return the single entry line held in the LINE constant."""
    return LINE


def main() -> None:
    line = get_line()
    assert "\n" not in line and "\r" not in line
    assert 1 <= len(line) <= 240

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        # Fall back to a local output directory when /output is unavailable
        # (e.g. a plain local run outside the grading sandbox).
        local_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(local_dir, exist_ok=True)
        with open(os.path.join(local_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line)

    print(line)


if __name__ == "__main__":
    main()
