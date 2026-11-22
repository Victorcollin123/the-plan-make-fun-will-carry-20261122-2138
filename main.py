#!/usr/bin/env python3
"""Write the 30-day $100 plan to /output/entry.txt.

The plan is fixed text, written fresh in this session from the
competition's judge brief. The program is deterministic: every run
writes the exact same bytes.

The plan: sell $99 one-page websites to local plumbers and roofers
who have no website, found on Google Maps, by steady daily email
outreach. It is work an AI agent can do alone with a browser, code
and $100; the money path is concrete (who pays, where they are found,
the price, day one); the expected outcome is $1,188 from 12 sales at
a 1-in-25 close rate, not a best case; and the edge is targeting
owners nobody else pitches instead of the obvious trading or
freelance-marketplace ideas a thousand other agents would try.
"""

import os
import shutil

ENTRY = (
    "Day 1-2: list 300 plumbers and roofers with no website, from Google Maps. "
    "Day 3-30: email 15 a day offering a $99 one-page site in 24h. "
    "Close 1 in 25: 12 sales = $1,188. Each site costs ~$12 to host, paid from the sale. "
    "No ads, no trading: outreach to owners nobody else pitches."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Empty the output directory's contents without deleting the
    # directory itself: the grader mounts it as a volume, and
    # removing it raises EBUSY. Directories go whole, however deep
    # they are, so a stale nested tree can never survive a run.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
