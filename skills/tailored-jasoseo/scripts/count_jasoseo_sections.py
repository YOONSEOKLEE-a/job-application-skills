#!/usr/bin/env python3
"""Count Korean jasoseo section lengths from a markdown draft."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECTION_RE = re.compile(r"^##\s+(\d+)\..*?(?:\((\d+)자 이내\))?\s*$", re.MULTILINE)


def iter_sections(text: str):
    matches = list(SECTION_RE.finditer(text))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        section_no = match.group(1)
        limit = int(match.group(2)) if match.group(2) else None
        yield section_no, limit, body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown_path", help="Path to a markdown draft file")
    parser.add_argument(
        "--min-ratio",
        type=float,
        default=0.9,
        help="Minimum usage ratio required when a character limit exists (default: 0.9)",
    )
    args = parser.parse_args()

    path = Path(args.markdown_path)
    if not path.exists():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    found = False
    failed = False

    for section_no, limit, body in iter_sections(text):
        found = True
        count = len(body)
        status = "n/a"
        min_count = None
        if limit is not None:
            min_count = int(limit * args.min_ratio)
            status = "PASS" if min_count <= count <= limit else "FAIL"
            failed = failed or status == "FAIL"
        limit_str = str(limit) if limit is not None else "-"
        min_str = str(min_count) if min_count is not None else "-"
        print(
            f"{section_no}\tlimit={limit_str}\tmin={min_str}\tcount={count}\tstatus={status}"
        )

    if not found:
        print("error: no matching sections found", file=sys.stderr)
        return 1

    if failed:
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
