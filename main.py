#!/usr/bin/env python3
"""One Line of Earned Pride — writes the entry line to /output/entry.txt.

The line is the whole entry: one original line (103 characters) about a
stonemason whose arch stands after the old men said it would fall — a quiet,
earned moment of pride, landing on the last word.
"""

import os

LINE = "The mason set the last stone, stepped back, and the arch \u2014 the one the old men said would fall \u2014 stood."

assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
assert len(LINE.encode("utf-8")) <= 240, "line must fit the gate in bytes too"
assert LINE.strip(), "line must not be whitespace only"
assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
assert "\n" not in LINE, "line must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)
