#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off R1 entry.

Writes the keeper line byte-exact to /output/entry.txt, no trailing newline.
Gate: 1-200 UTF-8 chars; keeper is 109 chars / 109 bytes, pure ASCII.
Device: the policy testifies against itself (P2 claim-vs-evidence + P10
familiar-phrase hijack); screened 308 candidates across 29 families.
"""
import os

ENTRY = "The expenses policy is 41 pages. Page 1 says 'use common sense'. Page 39 says 'common sense needs a receipt'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
