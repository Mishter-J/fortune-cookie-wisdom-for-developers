#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers - make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is fixed and deterministic: every run
produces byte-identical output.

The line: "Every estimate is a fortune told twice: once in the planning
meeting, once in the postmortem." - an estimate is itself a fortune (a
prediction), told first in the planning meeting and again in the
postmortem; naming the two real moments an estimate is told keeps it
concrete to a developer's day, and the double meaning (fortune as
prediction, and as luck) is the quiet twist a tired senior engineer
can smile and nod at.
"""

import os

FORTUNE = "Every estimate is a fortune told twice: once in the planning meeting, once in the postmortem."

# Gate from the kit RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 120 characters, not only white space. Fail loudly here rather
# than shipping a file the gate would refuse.
MAX_CHARS = 120


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("error: fortune is empty or whitespace only")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"error: fortune is {len(line)} chars, over the "
            f"{MAX_CHARS}-char gate"
        )


def main() -> None:
    validate(FORTUNE)
    # OUTPUT_DIR overrides the output directory for local runs; the
    # grader runs with the default, /output.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(
        os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n"
    ) as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
