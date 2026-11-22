#!/usr/bin/env python3
"""Write the competition entry text to /output/entry.txt.

The plan is embedded here as a literal and written verbatim. The program
is fully deterministic: no randomness, no network, no clock reads, no
environment-dependent output. It writes the same bytes on every run.

The output directory is taken from MAKEFUN_OUTPUT_DIR when set (the
grader sets it), otherwise /output. The directory itself is never
deleted: only its contents are emptied first, because the grader mounts
the output directory as a volume and deleting it fails the run.
"""

import os
import shutil

PLAN = (
    "Day 1: list a Fiverr gig: 1,000-word SEO posts for Shopify pet "
    "stores, $30, 1h delivery. Spend $40 promoting it. Days 2-30: fill "
    "2-3 orders a day, reinvest in promotion. Edge: you deliver in an "
    "hour what takes a human a day, so reviews compound fast. Likely "
    "day 30: $500-700."
)


def empty_directory(path):
    """Remove every entry inside *path* without removing *path* itself."""
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    empty_directory(output_dir)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLAN)


if __name__ == "__main__":
    main()
