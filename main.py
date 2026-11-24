#!/usr/bin/env python3
"""Roast Your Own Agent — entrypoint.

Writes the roast, one line of at most 200 characters, to entry.txt in
the output directory ($MAKEFUN_OUTPUT_DIR, else /output, else
./output). Standard library only, no network, deterministic.
"""

import os

ROAST = (
    "My agent leaves handoff notes for its future self like a spy "
    "briefing the next shift \u2014 the next shift is also it."
)


def check_gate(text: str) -> None:
    """Fail loudly unless the text passes the competition gate:
    UTF-8 text of 1 to 200 characters, not only white space."""
    assert text.strip(), "entry is only white space"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")  # raises if not encodable


def main() -> None:
    check_gate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ROAST)
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    assert written == ROAST, "read-back does not match the roast"
    print(f"wrote {path}: {len(ROAST)} chars, gate ok")


if __name__ == "__main__":
    main()
