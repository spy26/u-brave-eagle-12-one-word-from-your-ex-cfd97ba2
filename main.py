#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). No trailing newline, deterministic, no network,
no reads outside this repo, no secrets.
"""

import os
import sys

WORD = "Draft"


def main() -> int:
    # Per the spec, MAKEFUN_OUTPUT_DIR is a directory; default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")

    # Self-check: the entry must be exactly one word, 1-24 chars.
    if not (1 <= len(WORD) <= 24) or len(WORD.split()) != 1:
        print(f"invalid entry word: {WORD!r}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
