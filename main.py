#!/usr/bin/env python3
"""Entry for Two Days of Quiet Dread — writes the one-line code-review approval to entry.txt."""

import os

ENTRY_TEXT = "Approved: 214 tests pass. This helper will outlive us both; its author left in March, and it still signs all its work 'the remaining team.'"


def main() -> None:
    # Output directory is provided by the grader; default to /output.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
