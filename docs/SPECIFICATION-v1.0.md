# PICTOGRAM Specification v1.0  
### Universal Visual Semantic Protocol  
### Release Candidate — November 23, 2025

---

## 1. Purpose

The PICTOGRAM v1.0 Specification defines a universal visual semantic protocol for encoding meaning into topologically stable glyphs. This system enables:

- Human readability  
- Machine verifiability  
- Cultural neutrality  
- Cross-model semantic alignment  
- Long-term archival durability  

Its companion protocol, **VSE (Vector-Space Esperanto)**, defines semantic structure.  
PICTOGRAM defines the **visual identity of meaning**.

Together, they form the **Universal Meaning Interface**.

---

## 2. Motivation

Most writing systems depend on historical convention.  
PICTOGRAM depends on **topological invariants**.

This specification addresses several limitations of current symbolic encodings:

- Glyphs collapse under rotation  
- Symbols depend on font rendering  
- Semantic drift across cultures  
- Fragility under noise and compression  
- Lack of transparency in AI reasoning  

PICTOGRAM v1.0 solves these through:

- **Dihedral symmetry normalization**  
- **PUA codepoint allocation**  
- **Square-Pad-Resize geometric stabilization**  
- **Freeman-chain topology identity**  
- **PSH-256 cryptographic hashing**  

---

## 3. Core Design Principles

1. **Topology Over Rendering**  
   Meaning derives from structural geometry, not stylistic appearance.

2. **D4 Invariance (Dihedral Normalization)**  
   A glyph retains identity under all 8 symmetries of the square.

3. **Semantic Sovereignty (PUA Block)**  
   Glyphs map to U+E000–U+E01F, eliminating Unicode collision.

4. **Deterministic Canonicalization**  
   All renderings normalize to identical topology before hashing.

5. **Human–Machine Symmetry**  
   Symbols readable to humans correspond exactly to machine-verified identities.

---

## 4. The Glyph Canon (v1.0)

PICTOGRAM v1.0 defines:

- **28 canonical glyphs**
- grouped into:
  - Flow  
  - Pressure  
  - Texture  
  - Structure  
  - Operators  

Each glyph includes:

- Semantic definition  
- Canonical SVG geometry  
- PUA codepoint  
- PSH-256 reference hash  
- Composition constraints  

Refer to `registry.json` for authoritative mapping.

---

## 5. Canonicalization Pipeline

### 5.1 Square-Pad-Resize Protocol

All glyph renderings MUST undergo:

1. Bounding box extraction  
2. Square padding (centered)  
3. 10% safe-zone border  
4. Resize to 64×64 grid  

### 5.2 Skeletonization

Images MUST reduce to 1-pixel strokes via morphological thinning.

### 5.3 Dihedral Normalization

All 8 symmetries MUST be generated:

- 0°  
- 90°  
- 180°  
- 270°  
- and each mirrored  

The lexicographically smallest chain code is the **canonical topology**.

### 5.4 PSH-256 Hash

The canonical topology MUST be hashed using SHA-256 to produce the final identity.

---

## 6. Normative References

- RFC 2119 (MUST / SHOULD / MAY)  
- Freeman Chain Code  
- Unicode Private Use Area (U+E000–F8FF)  
- SHA-256 (RFC 6234)  
- ChronoCore Cognitive Encoding  

---

## 7. Licensing

- Code: MIT License  
- Glyph Canon & Documentation: CC BY-SA 4.0  
- Specification: Public, open, and royalty-free  

---

## 8. Standardization Statement

This document defines PICTOGRAM v1.0 as the canonical standard for visual semantic encoding. All future versions MUST preserve:

- D4 invariance  
- PUA codepoint allocations  
- canonical glyph topology  

---

## 9. Implementation Status

This spec is accompanied by:

- `psh256_v1_0.py` — reference implementation  
- `verify_stability.py` — stability test suite  
- `registry.json` — glyph metadata  
- `canonical/` — SVG glyph directory  

---

# END OF SPECIFICATION
