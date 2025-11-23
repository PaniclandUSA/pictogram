# Contributing to PICTOGRAM  
### Guidelines for Collaboration

Thank you for contributing to the PICTOGRAM protocol.  
This document provides instructions for submitting improvements, code, tests, or new glyph ideas.

---

## 1. Code of Conduct

All contributors MUST uphold:

- Respect  
- Technical accuracy  
- Cultural neutrality  
- Openness to review  
- No proprietary claims over glyph designs  

---

## 2. Repository Layout

/docs → Specification, RFC, appendices
/reference → PSH-256 and utilities
/glyphs → Canonical SVGs and metadata
/tests → Stability and regression tests
/examples → Sample PICTOGRAM sequences


---

## 3. Reporting Issues

Please open an issue for:

- hash mismatches  
- canonicalization errors  
- SVG inconsistencies  
- proposed glyph revisions  
- pipeline bugs  

---

## 4. Submitting Pull Requests

### Requirements:

- PRs MUST pass existing stability tests  
- New code MUST follow existing structure  
- Glyph changes MUST update:
  - `/glyphs/canonical/*.svg`
  - `/glyphs/registry.json`
  - `/docs/registry.md`

### Glyph Proposals:

- MUST avoid Unicode similarity  
- MUST remain topologically stable under skeletonization  
- MUST be analysable at 64×64 resolution  

---

## 5. Adding Tests

All new code MUST include:

- unit tests  
- dihedral invariance tests  
- pixel dropout/noise resilience tests  

Use:
tests/stability-results/
tests/test-images/


for storage.

---

## 6. Licensing

All contributions are accepted under:

- MIT License (code)  
- CC BY-SA 4.0 (glyphs & docs)  

---

# END OF CONTRIBUTING GUIDE

