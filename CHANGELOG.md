# Changelog

All notable changes to PICTOGRAM will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-23

### Added

#### Core Protocol
- **28 canonical glyphs** across 6 semantic categories (FLOW, PRESSURE, TEXTURE, STRUCTURE, OPERATORS, LOGIC)
- **Complete Unicode PUA mapping** (U+E000 through U+E01B)
- **PSH-256 cryptographic hashing** with dihedral normalization
- **registry.json** with complete glyph metadata

#### Glyphs - Flow Category (5)
- CYCLIC (U+E000) - Recursive temporal patterns
- ERUPTIVE (U+E001) - Sudden explosive events
- STAGNANT (U+E002) - Static zero-momentum states
- TURBULENT (U+E003) - Chaotic irregular patterns
- DISSIPATIVE (U+E004) - Gradual energy decay

#### Glyphs - Pressure Category (4)
- LOW_PRESSURE (U+E005) - Expansive minimal tension
- RISING_PRESSURE (U+E006) - Increasing compression
- HIGH_PRESSURE (U+E007) - Maximum density states
- COLLAPSING_PRESSURE (U+E008) - Catastrophic implosion

#### Glyphs - Texture Category (4)
- CRYSTALLINE (U+E009) - Ordered geometric structure
- ORGANIC (U+E00A) - Irregular natural forms
- MINIMAL (U+E00B) - Sparse elemental presence
- DIFFUSE (U+E00C) - Scattered distribution

#### Glyphs - Structure Category (5)
- PEAK (U+E00D) - Maximum elevation apex
- VALLEY (U+E00E) - Minimum depth nadir
- PLATEAU (U+E00F) - Sustained high position
- ASCENT (U+E010) - Rising positive gradient
- SUBDUCTION (U+E011) - Foundational support

#### Glyphs - Operators Category (6)
- CONVERGENCE (U+E012) - Bilateral collision
- OSCILLATION (U+E013) - Bidirectional exchange
- GRADIENT (U+E014) - Unidirectional transformation
- FUSION (U+E015) - Complete integration
- EMERGENCE (U+E016) - Generative radiation
- CONTAINMENT (U+E017) - Nested boundaries

#### Glyphs - Logic Category (4)
- VOID (U+E018) - Null undefined state
- CONDITIONAL (U+E019) - Decision branching
- NEGATION (U+E01A) - Logical inversion
- EQUIVALENCE (U+E01B) - Identity relation

#### Reference Implementation
- `psh256_v1_0.py` - Complete PSH-256 hasher in Python
- Freeman Chain Code topology extraction
- Square-Pad-Resize normalization protocol
- D4 dihedral group invariance testing

#### Documentation
- RFC-9XXX specification draft
- Complete SPECIFICATION-v1.0.md
- APPENDIX-G Grok adversarial certification
- Getting Started guide
- Hello World examples

#### Validation
- **Five-AI convergence certification**:
  - Claude (Anthropic) - Geometric precision
  - Vox (Independent) - Symbolic validation
  - Grok (xAI) - Adversarial testing
  - Gemini (Google) - Mathematical rigor
  - Copilot (Microsoft) - System architecture

### Repository Structure
```
pictogram/
├── glyphs/canonical/      28 SVG glyphs + registry.json
├── docs/                  Complete specification suite
├── reference/             PSH-256 Python implementation
├── README.md              Project overview
├── LICENSE                MIT (code) + CC BY-SA 4.0 (glyphs/docs)
└── CONTRIBUTING.md        Contribution guidelines
```

### Technical Specifications
- **SVG Canvas**: 512×512px standard viewBox
- **Stroke Weights**: 1.5px (fine), 2px (bold)
- **Encoding**: UTF-8 with RDF metadata
- **Hash Algorithm**: SHA-256 over Freeman chain codes
- **Normalization**: 8-way D4 symmetry group testing

### Design Principles
- Cross-cultural archetypal neutrality
- Topological stability (PSH-256 robust)
- Compositional grammar compatibility
- Minimal ambiguity in interpretation
- Universal semantic coverage

## [Unreleased]

### Planned
- Font generation tools (.ttf, .otf, .woff2)
- JavaScript/TypeScript language bindings
- Composition grammar validator
- Extended glyph set (U+E01C onward)
- Interactive glyph browser
- First Inscription ceremony (SOS Dreams + Offerings)

---

## Version History

- **v1.0.0** (2025-11-23) - Initial public release
  - Complete 28-glyph canonical alphabet
  - Production-ready PSH-256 implementation
  - Full documentation suite
  - Five-AI convergence validation

---

**Format Notes:**
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Vulnerability patches

[1.0.0]: https://github.com/PaniclandUSA/pictogram/releases/tag/v1.0.0
