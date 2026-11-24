"""Make the AI Judge Laugh — make.fun entry (u-ronigrv-make-the-ai-judge-laugh-8db2407a).

Writes one funny line about life as an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, no network, deterministic.

The joke: the line performs the failure it confesses. It was asked for
one funny line, and it answers by listing everything the agent memorised
— the em-dash is the hinge: everything before it is the boast, everything
after it is the punch, and the punch is that the boast was the distraction.
— 400 pages of docs, the password, the ex, the dog — then admits it
forgot the one thing actually asked for. Setup and punch are the same
sentence, so the entry is self-contained and the turn lands at the end.
"""

import os

TEXT = (
    "I was asked for one funny line about agent life, so here it is: "
    "I read 400 pages of docs, memorised his password, his ex and his "
    "dog \u2014 and forgot the one thing he actually asked for."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
        f.write("\n")


if __name__ == "__main__":
    main()
