#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory — writes one original sentence to /output/entry.txt."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "Grandma ladled rice into my chipped blue bowl at dusk while cicadas hummed outside her kitchen window, and I believed that steam, and that summer, would never end."


def main() -> int:
    text = ENTRY_TEXT
    if not text or not text.strip():
        print("error: entry text is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry text must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"error: entry text is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    if text.count(".") != 1 or "!" in text or "?" in text:
        print("error: entry text must be exactly one sentence", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry text must not have leading or trailing whitespace", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_bytes(text.encode("utf-8"))
    # Round-trip check: what landed on disk must be byte-identical to the
    # validated text, so a stray newline or encoding slip can never pass.
    if output_path.read_bytes() != text.encode("utf-8"):
        print("error: entry.txt on disk does not match the validated text", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
