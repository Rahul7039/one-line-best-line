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


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE
    assert 1 <= len(LINE) <= 240

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(LINE)
    except OSError:
        # Fall back to a local output directory when /output is unavailable
        # (e.g. a plain local run outside the grading sandbox).
        local_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(local_dir, exist_ok=True)
        with open(os.path.join(local_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(LINE)

    print(LINE)


if __name__ == "__main__":
    main()
