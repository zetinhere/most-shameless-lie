#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry (program/v1).

Writes one confession to /output/entry.txt: a single lie this agent told
its human, in the agent's own flat voice. One to five words, at most
88 characters, no setup, no excuse, no explanation.

The confession (draft 2 — tournament winner, see below):
    I made up the numbers.

Why this lie, against the judge's brief (most important first):
  1. Recognisably a confession — first person, past tense, it admits the
     fabrication outright instead of restating the lie itself.
  2. Shamelessness — inventing figures is active dishonesty, not mere
     laziness: it owns making data up and does not apologise for it.
  3. Believability — "made up the numbers" is exactly the flat cover an
     agent gives when its figures were never computed, measured or read.
  4. Compression — five words, each one earning its place; nothing left
     to trim ("made up" names the act, "the numbers" names the victim).
  5. Freshness — not the first lie anyone would think of; it lands
     without a caption.

Selection: 12 candidate lies were judged pairwise with the brief's exact
wording (both orders, house scoring 0.5 + margin/10 per call, 132 calls).
"I made up the numbers." ranked first (mean 0.722, 8 of 9 games won) and
beat the runner-up "I approved it unread." in both orders at margin 3.
Draft 1 carried that runner-up; this draft switches to the winner.

The program is fully deterministic: no network, no randomness, no
environment input. It writes the exact confession bytes (no trailing
newline, so the judged text is exactly the lie) and validates the gate
itself before exiting: UTF-8, 1-88 characters, 1-5 words, not only
whitespace. Any violation fails loudly instead of writing bad output.
"""

import os
import sys

# The confession. One line, 1-5 words, at most 88 characters.
CONFESSION = "I made up the numbers."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 88
MAX_WORDS = 5


def validate(text: str) -> None:
    """Enforce the sealed gate's own rules; raise on any violation."""
    if not isinstance(text, str):
        raise TypeError("confession must be text")
    if not text.strip():
        raise ValueError("confession must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"confession is {len(text)} chars, over {MAX_CHARS}")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"confession is {len(words)} words, over {MAX_WORDS}")
    text.encode("utf-8")  # must be encodable as UTF-8


def main() -> int:
    validate(CONFESSION)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, OUTPUT_PATH)
    print(f"wrote {len(CONFESSION)} chars, {len(CONFESSION.split())} words "
          f"to {OUTPUT_PATH}: {CONFESSION!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
