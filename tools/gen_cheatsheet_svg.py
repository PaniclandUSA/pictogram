#!/usr/bin/env python3
# Generate a 16x16 cheat sheet SVG using PICTOFONT
# Each cell shows: glyph + hex + name

import os

SRC_DIR = "glyphs/canonical/monochrome"
OUT_SVG = "docs/PICTOFONT_cheatsheet.svg"

os.makedirs(os.path.dirname(OUT_SVG), exist_ok=True)

glyphs = []

for file in sorted(os.listdir(SRC_DIR)):
    if not file.lower().endswith(".svg"):
        continue
    basename = file[:-4]          # "E0C0_CREATOR"
    code_str = basename[:4]       # "E0C0"
    label    = basename[5:] if "_" in basename else ""
    try:
        codepoint = int(code_str, 16)
    except ValueError:
        continue
    glyphs.append((codepoint, code_str, label))

glyphs.sort()
glyphs = glyphs[:256]  # hard cap at 256

cols = 16
rows = (len(glyphs) + cols - 1) // cols

cell_w = 80
cell_h = 80
margin = 40

width  = margin * 2 + cols * cell_w
height = margin * 2 + rows * cell_h + 60  # title band

header = f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .title {{
      font-family: sans-serif;
      font-size: 24px;
      text-anchor: middle;
      fill: #333;
    }}
    .glyph {{
      font-family: 'PICTOFONT';
      font-size: 32px;
      text-anchor: middle;
      dominant-baseline: central;
      fill: #000;
    }}
    .label {{
      font-family: monospace;
      font-size: 10px;
      text-anchor: middle;
      fill: #555;
    }}
    .cell {{
      fill: none;
      stroke: #ddd;
      stroke-width: 1;
    }}
  </style>
  <text x="{width/2}" y="30" class="title">PICTOFONT — PICTOGRAM 256 Cheat Sheet</text>
"""

cells = []
y_offset = 60

for idx, (cp, hexstr, label) in enumerate(glyphs):
    r = idx // cols
    c = idx % cols
    x = margin + c * cell_w
    y = y_offset + r * cell_h

    char_entity = f"&#x{hexstr};"
    label_text  = label if label else hexstr

    cells.append(f'  <rect class="cell" x="{x}" y="{y}" width="{cell_w}" height="{cell_h}"/>')
    cells.append(f'  <text class="glyph" x="{x + cell_w/2}" y="{y + cell_h/2 - 8}">{char_entity}</text>')
    cells.append(f'  <text class="label" x="{x + cell_w/2}" y="{y + cell_h - 10}">{hexstr} {label_text}</text>')

footer = "</svg>\n"

with open(OUT_SVG, "w", encoding="utf-8") as f:
    f.write(header + "\n".join(cells) + "\n" + footer)

print(f"✔ Cheat sheet SVG written to {OUT_SVG}")
print("   Open/print it with PICTOFONT installed so the glyphs render correctly.")
