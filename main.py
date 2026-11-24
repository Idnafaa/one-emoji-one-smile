# SPDX-License-Identifier: MIT
"""One Emoji, One Smile — make.fun entry.

The program writes exactly one emoji to /output/entry.txt: the one
most likely to make a stranger smile.

The pick is the face holding back tears (U+1F979). It reads at a
glance as touched and grateful, warm without needing any context,
and it works coming from a stranger: no joke, no flirtation, no
in-joke. It is also a deliberate choice rather than the first
default smiley, which is what the judge's brief asks for.
"""

import os

# The single emoji this entry sends: face holding back tears.
EMOJI = "🥹"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the chosen emoji, and nothing else, to the output file."""
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    # Self-check against the gate: UTF-8 text of 1 to 8 characters,
    # not only white space. Fail loudly instead of shipping a bad file.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if not 1 <= len(written) <= 8 or not written.strip():
        raise ValueError("entry.txt failed the gate: %r" % written)


if __name__ == "__main__":
    main()
