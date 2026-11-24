"""One-Liner Marathon entry: writes a single original one-line comedy joke
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)."""

import os
import sys

JOKE = (
    "I asked my AI assistant to clear my schedule, so it cancelled "
    "my meetings, deleted my calendar, and \u2014 out of professional "
    "courtesy \u2014 my job."
)


def main() -> int:
    line = JOKE.strip()
    if not line:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(line) > 280:
        print(f"error: joke is {len(line)} chars, over the 280 limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
