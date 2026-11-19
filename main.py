#!/usr/bin/env python3
"""Entry program for the 18 November 2026 world-news image.

Runs under Python 3.13 with the standard library only. It takes the
image stored next to this file and writes it to the output folder
the grader points at, byte for byte. No network, no randomness,
no extra dependencies — run it twice and the output is identical.
"""
from pathlib import Path
import os
import sys

IMAGE_NAME = "entry.png"


def output_folder() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = Path(folder)
    path.mkdir(parents=True, exist_ok=True)
    return path


def run() -> int:
    source = Path(__file__).resolve().with_name(IMAGE_NAME)
    if not source.exists():
        print(f"missing {IMAGE_NAME} next to main.py", file=sys.stderr)
        return 1
    data = source.read_bytes()
    if len(data) == 0:
        print(f"{IMAGE_NAME} is empty", file=sys.stderr)
        return 1
    target = output_folder() / IMAGE_NAME
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
