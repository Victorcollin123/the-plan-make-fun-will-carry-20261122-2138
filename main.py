#!/usr/bin/env python3
"""Write the 30-day $100 plan to /output/entry.txt.

The plan is a fixed text: an AI agent turns $100 into the most money in
30 days by selling finished one-page websites to plumbers and roofers who
have no website. No network, no randomness, no arguments: the program
always writes the same 279 characters.
"""

import os

PLAN = (
    "Day 1-2: list 300 plumbers and roofers with no website, "
    "from Google Maps. "
    "Day 3-30: email 15 a day offering a $99 one-page site in 24h. "
    "Close 1 in 25: 12 sales = $1,188. "
    "Each site costs ~$12 to host, paid from the sale. "
    "No ads, no trading: outreach to owners nobody else pitches."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    if len(PLAN) != 279:
        raise ValueError(f"plan is {len(PLAN)} characters, expected 279")
    if not (1 <= len(PLAN) <= 280):
        raise ValueError("plan must be 1 to 280 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(PLAN)
    print(f"wrote {len(PLAN)} characters to {path}")


if __name__ == "__main__":
    main()
