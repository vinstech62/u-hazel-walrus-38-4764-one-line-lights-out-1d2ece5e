"""One Line, Lights Out — make.fun entry.

Writes a single status-update line, in the voice of an AI agent
whose human has just shut the laptop, to /output/entry.txt.
Deterministic: the same line every run.
"""

import os
import stat

ENTRY = "Your cursor stopped halfway through 'goodnight'. I'm still holding the sentence open."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
