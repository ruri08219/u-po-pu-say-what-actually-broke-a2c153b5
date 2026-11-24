"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy (at most 200 characters)
to /output/entry.txt. Standard library only.
"""

import os

MAX_CHARS = 200

ENTRY = (
    "This page crashed because the app tried to load 40,000 rows into a "
    "dropdown. It worked in testing \u2014 testing had 12 rows. "
    "Refresh and pretend you didn't see this."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be whitespace-only")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what we wrote: the gate checks the file, not the constant.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch in /output/entry.txt")


if __name__ == "__main__":
    main()
