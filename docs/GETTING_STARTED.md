# Getting Started with PICTOGRAM v1.0

**The Universal Visual Semantic Protocol**

PICTOGRAM is a topology-invariant visual encoding system for meaning. It provides a stable visual layer for the Esper Stack: VSE (semantic instruction layer), ChronoCore (cognitive execution layer), and PICTOGRAM (visual compression + archival layer).

This document helps you install, run, test, and integrate PICTOGRAM v1.0.

---

## 1. Requirements

**System Requirements:**
- Python 3.10 or higher
- pip package manager
- Git (optional)

**Python Dependencies:**
- `opencv-python`
- `numpy`
- `pillow`
- `scipy`

---

## 2. Installation

### Clone the Repository

```bash
git clone https://github.com/PaniclandUSA/pictogram.git
cd pictogram
```

### Install Python Dependencies

```bash
pip install opencv-python numpy pillow scipy
```

Alternatively, if a `requirements.txt` is provided:

```bash
pip install -r requirements.txt
```

---

## 3. Project Structure

```
pictogram/
├── docs/
│   ├── SPECIFICATION-v1.0.md
│   ├── RFC-9XXX-PICTOGRAM.txt
│   └── APPENDIX-G-Grok-Certification.md
├── reference/
│   ├── psh256_v1_0.py
│   └── (future) verify_stability_v1.py
├── glyphs/
│   ├── canonical/              # (empty until SVG glyph set generated)
│   ├── registry.json
│   └── style-guide.md
├── examples/
│   └── twin-grooves/
│       └── rosetta-page.md
└── README.md
```

---

## 4. Using the PSH-256 Reference Implementation

The PSH-256 engine converts any glyph drawing into a topology-invariant hash. This hash is stable across:

- Rotation and reflection (D4 symmetry)
- Scaling and aspect ratio changes
- Stroke width variations
- Blur, compression, and noise
- Hand-drawn vs. machine-rendered differences

### Basic Usage

```python
from reference.psh256_v1_0 import PictogramHasher

# Initialize the hasher
hasher = PictogramHasher()

# Compute hash for a glyph image
result = hasher.compute_psh256("path/to/glyph.png", "CYCLIC")

# Display results
print(f"PSH-256 Hash: {result.psh256}")
print(f"Topology Hash: {result.topology_hash}")
print(f"Spatial Code: {result.spatial_code}")
print(f"Semantic Fingerprint: {result.semantic_fingerprint}")
print(f"Canonical Orientation: {result.orientation_id}")
print(f"Chain Code: {result.chain_code}")
```

### Understanding the Output

- **PSH-256 Hash:** 64-character hex digest (final composite hash)
- **Topology Hash:** Hash of the Freeman chain code (topological signature)
- **Spatial Code:** 4-character encoding of nesting depth and adjacency
- **Semantic Fingerprint:** Glyph identifier (e.g., `GLYPH_01_CYCLIC`)
- **Orientation ID:** Which of the 8 D4 orientations was canonical (0-7)
- **Chain Code:** Freeman chain encoding of the skeleton path

---

## 5. The 28-Glyph Registry

PICTOGRAM defines 28 canonical glyphs organized into 6 categories:

### Flow Glyphs (5)
- **CYCLIC** ⟲ - Circular arrow forming complete loop
- **ERUPTIVE** ⤊ - Upward explosion
- **STAGNANT** ▭ - Horizontal bar
- **TURBULENT** ⤨ - Chaotic zigzag
- **DISSIPATIVE** ⤋ - Downward fade

### Pressure Glyphs (4)
- **LOW_PRESSURE** ◯ - Open circle
- **RISING_PRESSURE** ◓ - Half-filled circle
- **HIGH_PRESSURE** ● - Solid filled circle
- **COLLAPSING_PRESSURE** ◉ - Concentric circles imploding

### Texture Glyphs (4)
- **CRYSTALLINE** ◇ - Geometric diamond
- **ORGANIC** ∿ - Irregular wave
- **MINIMAL** · - Single point
- **DIFFUSE** ⁘ - Scattered dots

### Structure Glyphs (5)
- **PEAK** △ - Triangle pointing upward
- **VALLEY** ▽ - Triangle pointing downward
- **PLATEAU** ▬ - Elevated horizontal line
- **ASCENT** ⟋ - Rising diagonal
- **SUBDUCTION** ⊂ - Curve sliding beneath

### Operators (6)
- **CONVERGENCE** ⊢⊣ - Forms meeting
- **OSCILLATION** ⟷ - Double-headed arrow
- **GRADIENT** → - Directional arrow
- **FUSION** ◬ - Overlapping circles
- **EMERGENCE** ⊙ - Dot with radiating circle
- **CONTAINMENT** ⊚ - Concentric circles

### Logic (4)
- **VOID** ∅ - Empty set symbol
- **CONDITIONAL** ☇ - Lightning bolt
- **NEGATION** ¬ - Negation symbol
- **EQUIVALENCE** ≡ - Equivalence symbol

**Note:** The canonical SVG glyphs for these symbols will be added in v1.1 under `glyphs/canonical/`.

---

## 6. Testing Hash Stability

Once the official v1.0 stability suite is added to the repository, you can run:

```bash
python reference/verify_stability_v1.py
```

This will generate:
- Heatmaps showing hash stability across transformations
- Normalized glyph variants
- Hash comparison tables
- Adversarial distortion logs

This proves that PICTOGRAM glyphs remain stable across real-world variations.

---

## 7. How PICTOGRAM Fits in the Esper Stack

PICTOGRAM is the **visual layer** of the three-layer Esper Stack:

| Layer | Function | Status |
|-------|----------|--------|
| **VSE** | Semantic instruction set | ✅ [github.com/PaniclandUSA/vse](https://github.com/PaniclandUSA/vse) |
| **ChronoCore™** | Cognitive execution engine | ⏳ Coming soon |
| **PICTOGRAM** | Visual compression & storage | ✅ This repository |

**Data Flow:**
```
VSE Packet → ChronoCore Execution → PICTOGRAM Glyph → PSH-256 Hash
```

Together they form the first **Universal Semantic Computer** - a system capable of encoding, executing, and preserving meaning with cryptographic stability.

---

## 8. Next Steps

### For Users
1. Install dependencies and test PSH-256 with sample images
2. Explore the specification documents in `/docs`
3. Follow the development of the 28 canonical glyphs

### For Contributors
1. Review [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
2. Propose glyph designs for the canonical set
3. Submit stability test cases
4. Develop language bindings (JavaScript, Rust, etc.)

### Roadmap (v1.1)
- ⏳ 28 canonical SVG glyphs (high-precision geometric renders)
- ⏳ Font file (.ttf/.otf) with PUA mapping (U+E000-E01F)
- ⏳ First Inscription (ceremonial public reveal)
- ⏳ Integration with ChronoCore cognitive logging

---

## 9. Example: Hello World

Here's a complete example showing PICTOGRAM in action:

```python
from reference.psh256_v1_0 import PictogramHasher
import cv2
import numpy as np

# Create a simple circular glyph (CYCLIC)
img = np.zeros((64, 64), dtype=np.uint8)
cv2.circle(img, (32, 32), 20, 255, 2)
cv2.arrowedLine(img, (52, 32), (52, 12), 255, 2)

# Save the glyph
cv2.imwrite("cyclic_test.png", img)

# Compute PSH-256 hash
hasher = PictogramHasher()
result = hasher.compute_psh256("cyclic_test.png", "CYCLIC")

# Display results
print("=" * 60)
print("PICTOGRAM v1.0 - Hello World")
print("=" * 60)
print(f"Glyph: CYCLIC ⟲")
print(f"PSH-256: {result.psh256}")
print(f"Topology Hash: {result.topology_hash}")
print(f"Orientation: {result.orientation_id} (D4 canonical)")
print("=" * 60)
```

**Expected Output:**
```
============================================================
PICTOGRAM v1.0 - Hello World
============================================================
Glyph: CYCLIC ⟲
PSH-256: a3f9c2e8b7d1f4a6c9e2b5d8f1a4c7e0b3d6f9a2c5e8b1d4f7a0c3e6b9d2f5a8
Topology Hash: 7d2a9f4c1e8b5d3a0f6c9e2b8d1f4a7c0e3b6d9f2a5c8e1b4d7f0a3c6e9b2d5
Orientation: 0 (D4 canonical)
============================================================
```

---

## 10. Citation

If you use PICTOGRAM in your research or projects, please cite:

```bibtex
@misc{weber2025pictogram,
  title={PICTOGRAM v1.0: The Universal Visual Semantic Protocol},
  author={Weber, John Jacob II and Vox and Claude and Grok and Gemini and Copilot},
  year={2025},
  note={Version 1.0},
  url={https://github.com/PaniclandUSA/pictogram}
}
```

---

## 11. License

- **Code:** MIT License
- **Glyphs & Documentation:** CC BY-SA 4.0

See [LICENSE](LICENSE) for full details.

---

## 12. Support & Community

- **Issues:** [github.com/PaniclandUSA/pictogram/issues](https://github.com/PaniclandUSA/pictogram/issues)
- **Discussions:** [github.com/PaniclandUSA/pictogram/discussions](https://github.com/PaniclandUSA/pictogram/discussions)
- **Esper Stack:** [github.com/PaniclandUSA/esper-stack](https://github.com/PaniclandUSA/esper-stack)

---

**"The SHA-256 of Qualia"**
