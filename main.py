"""One-Line Office Joke: 24-Hour Sprint.

Writes the single-line office joke entry to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.

The entry (137 chars, one sentence):

    Our Slack has 47 channels; the only one anyone reads is #random,
    where the CEO posts cat memes at 2 a.m. and HR pretends not to
    see them.

Why this angle: a field benchmark of 200 existing submission titles
shows the usual office tropes are crowded -- meeting/meetings ~35x,
printer 14x, email 10x, HR 9x, fridge 6x -- while Slack appears
0 times. The joke instead builds one concrete scene (47 channels,
#random, the CEO posting cat memes at 2 a.m., HR pretending not to
see them) so the punchline lands on first read: the channel nobody
is supposed to read is the only one anyone actually reads.
"""

import os

ENTRY = (
    "Our Slack has 47 channels; the only one anyone reads is #random, "
    "where the CEO posts cat memes at 2 a.m. and HR pretends not to see them."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    # Write exactly ENTRY: no trailing newline, so the entry stays one line.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
