#!/usr/bin/env python3
"""Write the 30-day plan to /output/entry.txt.

The plan sells $99 one-page websites to local plumbers and roofers
with no website, found on Google Maps, by steady daily email
outreach: 12 sales at a 1-in-25 close rate, $1,188 in 30 days.
Deterministic: the same text on every run, no network.
"""

import os
import shutil

PLAN = "Day 1-2: list 300 plumbers and roofers with no website, from Google Maps. Day 3-30: email 15 a day offering a $99 one-page site in 24h. Close 1 in 25: 12 sales = $1,188. Each site costs ~$12 to host, paid from the sale. No ads, no trading: outreach to owners nobody else pitches."

# The gate needs 1 to 280 characters, counted as Unicode code points.
assert 1 <= len(PLAN) <= 280, len(PLAN)


def empty_output_dir(path):
    """Remove the contents of path without deleting path itself.

    The grader mounts /output as a volume, so deleting the directory
    itself would fail; clearing only its contents works there and
    also keeps any stale file from a previous run out of the entry.
    """
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    empty_output_dir(out_dir)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
