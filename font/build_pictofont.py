#!/usr/bin/env python3
# PICTOFONT Forge — Golden Master 1.0
# Builds OTF/TTF from glyphs/canonical/monochrome (256 glyphs, E000–E0FF)

import fontforge
import os
import glob

SVG_DIR = "glyphs/canonical/monochrome"
OUT_DIR = "font/out"

os.makedirs(OUT_DIR, exist_ok=True)

f = fontforge.font()
f.encoding   = "UnicodeFull"
f.fontname   = "PICTOFONT"
f.familyname = "Pictogram Canonical"
f.fullname   = "Pictogram Canonical Regular"
f.weight     = "Regular"

# 1000 UPM (standard); tweak ascent/descent for vertical balance
f.em      = 1000
f.ascent  = 850
f.descent = 150

svg_files = sorted(glob.glob(os.path.join(SVG_DIR, "E*.svg")))
if not svg_files:
    raise SystemExit(f"No SVGs found in {SVG_DIR}. Are the 256 monochrome glyphs there?")

for svg in svg_files:
    basename = os.path.basename(svg)   # e.g. "E0C0_CREATOR.svg"
    code_str = basename[:4]            # "E0C0"
    try:
        codepoint = int(code_str, 16)
    except ValueError:
        print(f"[SKIP] {basename} (invalid hex prefix)")
        continue

    print(f"[FONT] {basename} → U+{code_str}")

    g = f.createChar(codepoint, basename[:-4])  # glyph name = E0C0_CREATOR
    g.importOutlines(svg)

    # Side bearings — adjust as needed once you visually proof spacing
    g.left_side_bearing  = 60
    g.right_side_bearing = 60

    g.correctDirection()
    g.simplify(0.1)
    g.round()

out_otf = os.path.join(OUT_DIR, "PICTOFONT-Regular.otf")
out_ttf = os.path.join(OUT_DIR, "PICTOFONT-Regular.ttf")

f.generate(out_otf)
f.generate(out_ttf)

print("\n✔ PICTOFONT-Regular.otf")
print("✔ PICTOFONT-Regular.ttf")
print(f"  written to: {OUT_DIR}/")
print("Install the OTF to activate U+E000–E0FF as PICTOGRAM 256.")
