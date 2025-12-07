#!/usr/bin/env python3
import sys
from pathlib import Path

JUSTFILE = Path("justfile")


def main() -> int:
    if not JUSTFILE.exists():
        # If there's no justfile in this repo, nothing to do.
        return 0

    bad_lines = []

    for i, raw in enumerate(JUSTFILE.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.rstrip("\n")

        # Allow empty lines and full-line comments
        stripped = line.lstrip()
        if stripped == "" or stripped.startswith("#"):
            continue

        # Justfile syntax expects:
        # - top-level stuff (recipes, variables) with NO leading spaces or tabs
        # - recipe bodies indented with TABS, not spaces
        #
        # We forbid any leading SPACES.
        if line.startswith(" "):
            bad_lines.append((i, line))
            continue

    if not bad_lines:
        return 0

    print("ERROR: justfile contains lines with leading spaces (Just requires tabs for recipe bodies).", file=sys.stderr)
    print("Offending lines:", file=sys.stderr)
    for lineno, content in bad_lines:
        print(f"  line {lineno}: {content!r}", file=sys.stderr)

    print("\nFix: Replace leading spaces with tabs on recipe lines.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
