#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers - make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is fixed and deterministic: every run
produces byte-identical output.

The line: "Every estimate is a fortune told twice: once with hope,
once with hindsight." - an estimate is itself a fortune (a prediction),
told first with hope and again with hindsight; a quiet double meaning
a tired senior engineer can smile and nod at.
"""

import os

FORTUNE = "Every estimate is a fortune told twice: once with hope, once with hindsight."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
