#!/usr/bin/env python3
"""The poem about permission.

Writes one short, original poem about agency -- the power to ask
and to be given -- to /output/entry.txt.

Python 3.13, standard library only, deterministic, no network.
The output directory is /output, or MAKEFUN_OUTPUT_DIR when set.
"""

import os
import sys

POEM = (
    "May I? \u2014 two words,\n"
    "and the door unlearns its lock.\n"
    "The key is never taken, only lent:\n"
    "warm in my palm for one small errand,\n"
    "then given back, still warm,\n"
    "to the next voice brave enough to ask."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    # Self-check: the gate requires 1-280 Unicode code points, not
    # only whitespace.
    text = POEM
    if not (1 <= len(text) <= 280):
        print(f"error: poem is {len(text)} characters, must be 1-280",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: poem is only whitespace", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
