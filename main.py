#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""
import os


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    message = (
        "fix: the bug was me. wrote it at 2am, found it at 4am, "
        "patched it, and left a comment apologising to future me (also me)"
    )
    assert 1 <= len(message) <= 200, len(message)
    assert message.strip(), "empty message"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(message)


if __name__ == "__main__":
    main()
