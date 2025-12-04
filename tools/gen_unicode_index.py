#!/usr/bin/env python3
# Generate a Unicode index from glyph filenames in glyphs/canonical/monochrome/

import os

SRC_DIR = "glyphs/canonical/monochrome"
OUT_MD  = "docs/UNICODE_INDEX.md"

os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)

rows = []

for file in sorted(os.listdir(SRC_DIR)):
    if not file.lower().endswith(".svg"):
        continue

    basename = file[:-4]        # "E0C0_CREATOR"
    code_str = basename[:4]     # "E0C0"
    label    = basename[5:] if "_" in basename else ""

    try:
        codepoint = int(code_str, 16)
    except ValueError:
        continue

    rows.append((codepoint, code_str, label))

rows.sort()

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("# PICTOFONT Unicode Index (E000–E0FF)\n\n")
    f.write("| Codepoint | Hex  | Name           |\n")
    f.write("|-----------|------|----------------|\n")
    for cp, hexstr, label in rows:
        name = label if label else "(unnamed)"
        f.write(f"| U+{hexstr} | `{hexstr}` | `{name}` |\n")

print(f"✔ Unicode index written to {OUT_MD}")
