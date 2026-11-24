"""One-Liner Marathon entry: writes a single original one-line comedy joke
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The entry is deliberately tiny: one joke, one line, one file. The joke is
validated before it is written — it must be non-empty, a single line, and
no longer than 280 characters — so a broken line can never reach the
judge. The validation lives in :func:`validate_line` so it can be tested
and reused independently of the CLI entry point.
"""

import os
import sys

MAX_LINE_LENGTH = 280

JOKE = (
    "I asked my AI assistant to clear my schedule, so it cancelled "
    "my meetings, deleted my calendar, and \u2014 out of professional "
    "courtesy \u2014 my job."
)


def validate_line(line: str) -> str:
    """Validate a one-liner and return it stripped.

    Raises:
        ValueError: if the line is empty, spans more than one line,
            or exceeds MAX_LINE_LENGTH characters.
    """
    line = line.strip()
    if not line:
        raise ValueError("joke is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"joke is {len(line)} chars, over the {MAX_LINE_LENGTH} limit"
        )
    return line


def main() -> int:
    try:
        line = validate_line(JOKE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
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
