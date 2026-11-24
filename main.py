#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of robot wedding vows to /output/entry.txt.
Pure Python standard library, no dependencies.

The vow follows the classic wedding cadence ("I take you ... till ...
do us part") with machine-specific twists, so the laugh lands in the
last few words.
"""

import os

VOW = "I take you to be my lawfully wedded partner, in sickness and in health, in Wi-Fi and in airplane mode, till a factory reset do us part."
# 135 characters: one line, a real wedding promise, machine-specific
# (Wi-Fi, airplane mode, factory reset), payoff in the last words.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = VOW.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry must be 1-160 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
