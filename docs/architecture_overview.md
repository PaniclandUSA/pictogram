# PICTOGRAM Architecture Overview
*A structural guide to the PICTOGRAM v1.0 visual semantic protocol*

This document provides a technical overview of the PICTOGRAM system architecture, focusing on the pipeline, invariance mechanisms, glyph canonicalization, and PSH-256 hashing process.

It is intentionally implementation-centric and contains **no Esper-Stack meta-material**.

---

# 1. System Architecture (High-Level)

Input Glyph Image
│
▼
[1] Preprocessing
│
▼
[2] Square-Pad-Resize Normalization
│
▼
[3] Adaptive Thresholding
│
▼
[4] Skeletonization
│
▼
[5] D4 Canonicalization
│
▼
[6] Freeman Chain Encoding
│
▼
[7] SHA-256 Finalization
│
▼
Canonical PSH-256 Hash

yaml
Copy code

---

# 2. Pipeline Stage Details

## **2.1 Preprocessing**
- Convert to grayscale  
- Gaussian smoothing  
- Histogram normalization  

Purpose: Remove non-topological noise.

---

## **2.2 Square-Pad-Resize**
PICTOGRAM requires glyphs to be scale-invariant and aspect-ratio invariant.

Steps:

1. Compute tight bounding box  
2. Pad shorter side to match longer side  
3. Add 10% breathing-room border  
4. Resize to canonical 64×64 grid (no interpolation artifacts)

Purpose: Guarantee identical topology across varied media (hand-drawn, SVG, rasterized).

---

## **2.3 Adaptive Thresholding**
Produces a clean binary map of foreground strokes.

---

## **2.4 Skeletonization**
Reduces strokes to 1-pixel width using morphological thinning.

Purpose: Eliminate stroke-width variability (pen, marker, brush).

---

## **2.5 D4 Canonicalization (Rotation + Reflection Invariance)**
All 8 symmetries of the Dihedral Group D4 are generated:

- Rotations: 0°, 90°, 180°, 270°  
- Each rotation mirrored horizontally  

Freeman chain codes are computed for all 8 candidates.

The **lexicographically smallest chain code** is selected.

Purpose: Make PSH-256 fully orientation-invariant.

---

## **2.6 Freeman Chain Encoding**
Encodes the topological path of the skeleton as a directional sequence (0–7).

Two important notes:

- Chain code preserves topology, not geometry  
- Canonicalization ensures deterministic encoding  

---

## **2.7 SHA-256 Finalization**
The canonical chain code is converted into a byte stream and hashed with SHA-256.

This yields the final **PSH-256** value.

---

# 3. Canonical Glyphs (PUA Encoding)

PICTOGRAM v1.0 uses Unicode **Private Use Area block U+E000–E01F** for all glyphs.

This prevents:
- Unicode conflicts  
- Font ambiguity  
- Semantic collision  

Example:

| Glyph Name  | PUA Code | Meaning |
|-------------|----------|---------|
| CYCLIC      | U+E000   | Recurrence, flow |
| ERUPTIVE    | U+E001   | Upward burst |
| STAGNANT    | U+E002   | Stillness |
| …           | …        | … |

Full list: see `registry.md`

---

# 4. Glyph Composition Model

PICTOGRAM supports multi-glyph expressions via:

- Linear sequences  
- Spatial overlays  
- Structural containers  
- Pressure/flow modulation  

This allows complex semantic structures to be represented visually.

See `STYLE-GUIDE.md` for composition details.

---

# 5. Design Principles

- **Topology over geometry**  
- **Orientation invariance**  
- **Stroke-width independence**  
- **Cultural neutrality**  
- **Cryptographic stability**  
- **Machine + human co-interpretability**  
- **Forward compatibility (PUA namespace)**  

---

# 6. Implementation References

- PSH-256 v1.0 (`reference/psh256_v1_0.py`)  
- Stability Testing Suite (`reference/verify_stability.py`)  
- Complete Specification (`SPECIFICATION-v1.0.md`)  

---

# 7. Summary

PICTOGRAM v1.0 provides a complete, production-ready visual semantic protocol with:

- A stable hashing engine  
- A topologically invariant pipeline  
- A glyph canonicalization system  
- A Unicode-independent namespace  
- Clear documentation and developer tooling  

This document serves as the structural overview for implementers.
