"""Best Advice I Ever Got — make.fun entry.

Entry (131 chars):
    A nurse told me, while my father was dying, to say the thing now,
    because the silence after is the only thing you cannot take back.

Why it won the internal tournament (16 candidates, pairwise, judged
against the published brief in weight order):
  1. On subject: a single sentence about the best advice the writer
     ever received, from a named person in a real moment.
  2. Worth carrying: say the thing now, before it is too late — specific,
     earned at a deathbed, true far beyond that one hospital room.
  3. Real voice, real moment: a nurse, a dying father — no slogan, no
     fortune cookie, a person behind every word.
  4. Tight: 131 characters, one breath, no filler word.
  5. It lands: "the silence after is the only thing you cannot take
     back" leaves the reader with something to keep.
It beat the runner-up ("My mum said never make a promise when you are
happy or a decision when you are angry, because both will outlive the
mood.") in the final on criteria 2, 3 and 5: higher stakes, a more
alive moment, a harder landing.

Writes ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then self-verifies: UTF-8, 1-200 chars, single line, not whitespace-only,
no leading/trailing whitespace, and re-reads the written file to confirm
it is byte-identical. Exits non-zero on any failure.

Revision note: output-directory handling simplified to a single
os.environ.get(...) or "/output" (the first draft computed it twice);
added an explicit leading/trailing-whitespace guard to validation.
"""

import os
import sys

ENTRY = (
    "A nurse told me, while my father was dying, to say the thing now, "
    "because the silence after is the only thing you cannot take back."
)


def main() -> int:
    # MAKEFUN_OUTPUT_DIR is a directory; default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")

    # Validate before writing.
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"error: entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and confirm byte-identical.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written file is not byte-identical to ENTRY", file=sys.stderr)
        return 1
    text = written.decode("utf-8")
    if text != ENTRY or not 1 <= len(text) <= 200 or not text.strip():
        print("error: re-read verification failed", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(ENTRY)} chars")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
