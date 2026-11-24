#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why it ate
the homework, in the dog's own voice. Python 3.13 stdlib only, no network.
"""

import os

# Draft 3 (final): same literal "show your working" setup, but the kicker
# is tighter — the stomach is the marker, and it awarded full marks. The
# dog is proud, not sorry, and the whole joke lands in one line.
ENTRY = (
    "It said 'show your working', so I showed it to my stomach — "
    "and it gave me full marks."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
