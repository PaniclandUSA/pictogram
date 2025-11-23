# 📘 **STYLE-GUIDE.md**

```markdown
# PICTOGRAM Style Guide  
### Canonical Glyph Design Principles (v1.0)

This document defines the **visual design rules** for all official PICTOGRAM glyphs.

These rules ensure:

- Human recognizability  
- Machine interpretability  
- Canonical SVG consistency  
- Cross-cultural neutrality  

---

## 1. Canvas

- **512 × 512 px**  
- Full glyph centered  
- 10% breathing margin  
- Stroke aligned to pixel grid whenever possible

---

## 2. Stroke Weight

Three allowed weights:

- **Fine:**   24 px  
- **Medium:** 36 px  
- **Bold:**   48 px  

Guidelines:

- Flow glyphs → medium  
- Pressure glyphs → bold  
- Texture glyphs → fine  
- Structure glyphs → medium  
- Operators → bold  

These weights are symbolic and will be reflected in SVG output.

---

## 3. Line Style

- Round line caps  
- Round line joins  
- Consistent curvature  
- No decorative flares  
- No serif-like terminations  

PICTOGRAM glyphs must be **geometric**, not calligraphic.

---

## 4. Geometry

All glyphs MUST:

- Be constructed from lines, arcs, and simple curves  
- Avoid ambiguity with common Unicode shapes  
- Take forms that remain recognizable after skeletonization  
- Maintain structural clarity at 64 × 64 resolution  

---

## 5. Symmetry

Where applicable:

- Flow glyphs should emphasize directionality  
- Pressure glyphs should emphasize containment  
- Texture glyphs should emphasize multiplicity or granularity  
- Structure glyphs should emphasize hierarchy  
- Operators should emphasize relational behavior  

---

## 6. Color

Color is **non-canonical**.  
Glyph identity is determined by:

- topology  
- stroke relationships  
- PUA codepoint  
- PSH-256 hash  

Color may be used in UI contexts but must not define meaning.

---

## 7. Naming & File Structure

Each canonical glyph lives in:

/glyphs/canonical/<NAME>.svg

And must also appear in:

/glyphs/registry.json
/docs/registry.md

---

# END OF STYLE GUIDE
