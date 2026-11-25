#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one original sentence (<= 280 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
from pathlib import Path

ENTRY = (
    "Every August evening my grandmother scraped the crisp burnt rice "
    "from the bottom of her pot into my bowl with a chipped wooden spoon, "
    "cicadas humming beyond the kitchen window, and I still listen for "
    "that scrape whenever rice steams."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} characters"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
