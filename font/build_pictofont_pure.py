#!/usr/bin/env python3
# PICTOFONT Pure — only U+E000–U+E0FF, no Latin, no extras

import fontforge
import os
import glob

SVG_DIR = "glyphs/canonical/monochrome"
OUT_DIR = "font/out"

os.makedirs(OUT_DIR, exist_ok=True)

# Create a fresh font
f = fontforge.font()
f.encoding   = "UnicodeFull"
f.fontname   = "PICTOFONT_Pure"
f.familyname = "Pictogram Canonical Pure"
f.fullname   = "Pictogram Canonical Pure"
f.weight     = "Regular"

# Units/em & vertical metrics
f.em      = 1000
f.ascent  = 850
f.descent = 150

# Import ONLY the PUA glyphs from monochrome SVGs
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

    print(f"[PUA] {basename} → U+{code_str}")

    g = f.createChar(codepoint, basename[:-4])  # glyph name = E0C0_CREATOR
    g.importOutlines(svg)
    g.left_side_bearing  = 60
    g.right_side_bearing = 60
    g.correctDirection()
    g.simplify(0.1)
    g.round()

# Remove any glyphs outside U+E000–U+E0FF (keep .notdef)
for g in list(f.glyphs()):
    if g.unicode == -1:
        continue  # keep .notdef
    if not (0xE000 <= g.unicode <= 0xE0FF):
        f.removeGlyph(g)

out_otf = os.path.join(OUT_DIR, "PICTOFONT-Pure.otf")
out_ttf = os.path.join(OUT_DIR, "PICTOFONT-Pure.ttf")

f.generate(out_otf)
f.generate(out_ttf)

print("\n✔ PICTOFONT-Pure.otf")
print("✔ PICTOFONT-Pure.ttf")
print(f"  written to: {OUT_DIR}/")
print("This version contains ONLY U+E000–U+E0FF PICTOGRAM glyphs.")
