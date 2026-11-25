#!/usr/bin/env python3
"""Write one deadline-miss excuse for the make.fun bounty.

Deterministic, standard library only: it always writes the same
single line to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default /output).
"""

import os

# The excuse: fresh angle (the calendar moved the deadline, not the
# dog ate it), sounds like something a cornered person would say, and
# the punch lands on the last three words — I believed it.
LINE = (
    "I missed the deadline because my calendar moved it to next week "
    "without telling me, and honestly I believed it."
)

MAX_CHARS = 200


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(LINE)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in LINE:
        raise ValueError("entry must be exactly one line")
    if LINE != LINE.strip() or not LINE.endswith("."):
        raise ValueError("entry must be one trimmed line ending in a period")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
