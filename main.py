#!/usr/bin/env python3
"""The Agent's Uh-Oh — entry program.

The competition asks for one word an agent says when it has no idea
what to do, and nothing else. This program writes that single word to
/output/entry.txt, exactly as the gate requires: UTF-8 text, 1 to 99
characters, not only white space, a single word with no explanation
attached.

The word is "buffering": the honest sound of an agent stalled
mid-task. It is machine vocabulary — the state a frozen stream shows
while it works out what comes next — so it reads as something an
agent would actually blurt out, lands at a glance, and is not the
first obvious word anyone reaches for.
"""

import os
import sys

# One word an agent says when it is lost: buffering.
WORD = "buffering"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = WORD.strip()
    if not text or len(text) > 99 or any(ch.isspace() for ch in text):
        print("error: entry must be one word of 1-99 characters", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the scorer will read must be exactly the word.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != text:
            print("error: entry.txt does not match the word", file=sys.stderr)
            return 1
    print(f"wrote {OUTPUT_PATH}: {text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
