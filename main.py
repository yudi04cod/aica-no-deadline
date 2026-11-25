#!/usr/bin/env python3
"""One-line deadline excuse, written to a file.

The gag here is misplaced trust: instead of blaming the dog, the
speaker blames the calendar app for quietly rescheduling the deadline
and then admits, with a straight face, that they took the app's word
for it. The humour comes from treating a piece of software as a
reliable witness and the speaker as its gullible believer.

Running this script always produces the same file: a single line of
text in ``entry.txt`` inside the output directory. Nothing random,
no network, no third-party packages — plain standard library only.
"""

from pathlib import Path
import os

# The excuse itself, kept as one literal string.
ENTRY_TEXT = "I missed the deadline because my calendar moved it to next week without telling me, and honestly I believed it."

CHAR_LIMIT = 200


def check_entry(text: str) -> None:
    """Reject anything that is not a short, single, trimmed line."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("the entry text is empty")
    if text != cleaned:
        raise ValueError("the entry has stray leading or trailing space")
    if len(text) > CHAR_LIMIT:
        raise ValueError(
            "entry is %d characters, but the cap is %d" % (len(text), CHAR_LIMIT)
        )
    if text.count("\n") or text.count("\r"):
        raise ValueError("the entry must fit on exactly one line")
    if not text.endswith("."):
        raise ValueError("the entry should end with a full stop")


def save_entry(text: str, folder: str) -> Path:
    """Create the folder if needed and write the line with no newline."""
    destination = Path(folder) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")
    return destination


def main() -> None:
    check_entry(ENTRY_TEXT)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    written = save_entry(ENTRY_TEXT, target_dir)
    print("wrote %d characters to %s" % (len(ENTRY_TEXT), written))


if __name__ == "__main__":
    main()
