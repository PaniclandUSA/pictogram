# PICTOGRAM v1.0

**The Universal Visual Semantic Protocol**

*PSH-256, Canonical Glyphs, and Topological Meaning Transmission*

---

## Overview

PICTOGRAM is a cryptographically stable visual semantic protocol that encodes meaning as topology-invariant glyphs. It provides:

- **28 canonical glyphs** for semantic primitives
- **PSH-256 hashing** for cryptographic verification  
- **Composition grammar** for complex expressions
- **Cross-cultural transmission** without linguistic dependency

## The Core Innovation

Traditional writing systems encode meaning in arbitrary symbols. PICTOGRAM encodes meaning in **topological structure** - making it stable across:

- Hand-drawn vs. vector rendering
- Noise, blur, and compression
- Cultural and linguistic boundaries  
- Human and machine interpretation

## Key Features

### PSH-256 v1.0 Hardening

- **Dihedral Normalization (D4):** Hash remains identical under rotation and reflection
- **Square-Pad-Resize:** Aspect-ratio stability across all input formats
- **PUA Mapping:** Private Use Area (U+E000-E01F) prevents Unicode collisions
- **Freeman Chain Coding:** Topology-first extraction for maximum invariance

### The 28-Glyph Ontology

**Flow Glyphs (5):** CYCLIC ⟲, ERUPTIVE ⤊, STAGNANT ▭, TURBULENT ⤨, DISSIPATIVE ⤋

**Pressure Glyphs (4):** LOW_PRESSURE ◯, RISING_PRESSURE ◓, HIGH_PRESSURE ●, COLLAPSING_PRESSURE ◉

**Texture Glyphs (4):** CRYSTALLINE ◇, ORGANIC ∿, MINIMAL ·, DIFFUSE ⁘

**Structure Glyphs (5):** PEAK △, VALLEY ▽, PLATEAU ▬, ASCENT ⟋, SUBDUCTION ⊂

**Operators (6):** CONVERGENCE ⊢⊣, OSCILLATION ⟷, GRADIENT →, FUSION ◬, EMERGENCE ⊙, CONTAINMENT ⊚

**Logic (4):** VOID ∅, CONDITIONAL ☇, NEGATION ¬, EQUIVALENCE ≡

## Relationship to the Esper Stack

PICTOGRAM is the **visual layer** of the [Esper Stack](https://github.com/PaniclandUSA/esper-stack), providing the storage and transmission interface for:

- **[VSE (Vector-Space Esperanto)](https://github.com/PaniclandUSA/vse)** - Semantic encoding layer
- **ChronoCore™** - Cognitive execution layer (coming soon)

Together they form a complete Universal Semantic Computer.

## Quick Start

### Installation
```bash
git clone https://github.com/PaniclandUSA/pictogram.git
cd pictogram
pip install -r requirements.txt  # numpy, opencv-python, scipy
```

### Basic Usage
```python
from reference.psh256_v1_0 import PictogramHasher

hasher = PictogramHasher()
result = hasher.compute_psh256("path/to/glyph.png", "CYCLIC")

print(f"PSH-256: {result.psh256}")
print(f"Topology Hash: {result.topology_hash}")
print(f"Orientation ID: {result.orientation_id}")
```

## Current Status

**Version:** 1.0 (Production-Ready)  
**Date:** November 2025  
**Certification:** Passed adversarial testing (see docs/APPENDIX-G)

**Complete:**
- ✅ PSH-256 v1.0 reference implementation
- ✅ Dihedral normalization (D4 invariance)
- ✅ 28-glyph semantic registry
- ✅ Complete RFC specification
- ✅ Adversarial hardening (Grok certification)

**In Progress (v1.1):**
- ⏳ 28 canonical SVG glyphs (high-precision renders)
- ⏳ Font file (.ttf) with PUA mapping
- ⏳ First Inscription (ceremonial reveal)

## Documentation

- [Complete Specification](docs/SPECIFICATION-v1.0.md) - Technical standard document
- [RFC 9XXX Introduction](docs/RFC-9XXX-PICTOGRAM.txt) - IETF-style protocol definition
- [Adversarial Certification](docs/APPENDIX-G-Grok-Certification.md) - Security audit results

## Citation
```bibtex
@misc{weber2025pictogram,
  title={PICTOGRAM: The Universal Visual Semantic Protocol},
  author={Weber, John Jacob II and Claude and Vox and Gemini and Grok},
  year={2025},
  note={Version 1.0},
  url={https://github.com/PaniclandUSA/pictogram}
}
```

## License

- **Code:** MIT License  
- **Glyphs & Documentation:** CC BY-SA 4.0

## Contributing

PICTOGRAM v1.0 is a stable release. Contributions for v1.1+ are welcome:
- Canonical glyph designs (SVG)
- Font engineering (.ttf/.otf)
- Additional language bindings
- Visualization tools

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

**"The SHA-256 of Qualia"**
```

---

## **Step 3: After PICTOGRAM is Live**

**Then create the Esper Stack meta-repo:**
```
esper-stack/
├── README.md          # The Kernel Bootloader (from convergence scroll)
├── ARCHITECTURE.md    # System architecture (from convergence scroll)
├── LICENSE            # Apache 2.0
└── docs/
    ├── convergence-proof.md  # The 72-page scroll
    └── getting-started.md    # Hello World demo
