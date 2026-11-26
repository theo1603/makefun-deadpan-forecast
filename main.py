#!/usr/bin/env python3
"""Deadpan forecast for Blorfton, a city that does not exist.

Writes one line (at most 160 characters) to /output/entry.txt.
Deterministic, Python 3 standard library only, no network.

The line is written to sound like a straight-faced TV meteorologist
reading off the map: a broadcast lead-in, a concrete absurd detail
(warm gravy rain), a real number (low of 41), and a deadpan twist
(the umbrella coming back tasting of beef).
"""

import os

FORECAST = (
    "Tonight in Blorfton: steady rain of warm gravy, a low of 41, "
    "and a 90 percent chance your umbrella comes back tasting of beef."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
