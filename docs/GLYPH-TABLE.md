# PICTOGRAM Canonical Glyph Table

This document lists all **28 canonical PICTOGRAM glyphs** in v1.0, grouped by semantic family.

Each glyph is defined by:

- A **Private Use Area (PUA)** codepoint (`U+E0xx`)
- A **human-readable name**
- A **semantic category**
- A **legacy Unicode display** (for approximate visual reference only)
- A **canonical SVG file** in `glyphs/canonical/`
- A short **semantic description**
- A **PSH-256 canonical hash** (to be published after final verification)

> **Note:** The “Legacy Symbol” column is *representational only*.  
> The **PUA codepoint + SVG topology** are the true canonical identifiers.

---

## Flow Family (5 glyphs)

| PUA     | Name       | Category | Legacy Symbol | SVG File                                     | Brief Description                                               | PSH-256 (Canonical) |
|---------|------------|----------|---------------|----------------------------------------------|------------------------------------------------------------------|----------------------|
| U+E000  | CYCLIC     | flow     | ⟲            | [`E000_CYCLIC.svg`](../glyphs/canonical/E000_CYCLIC.svg)         | Continuous circular flow with a deliberate gap and arrowhead, representing recursive temporal momentum. | TBD |
| U+E001  | ERUPTIVE   | flow     | ⤊            | [`E001_ERUPTIVE.svg`](../glyphs/canonical/E001_ERUPTIVE.svg)     | Vertical eruption channel with asymmetric flares, symbolizing upward release of built pressure. | TBD |
| U+E002  | STAGNANT   | flow     | ▭            | [`E002_STAGNANT.svg`](../glyphs/canonical/E002_STAGNANT.svg)     | Pure horizontal bar representing complete temporal stillness and zero momentum. | TBD |
| U+E003  | TURBULENT  | flow     | ⤨            | [`E003_TURBULENT.svg`](../glyphs/canonical/E003_TURBULENT.svg)   | Irregular zigzag expressing chaotic, low-coherence, non-periodic flow. | TBD |
| U+E004  | DISSIPATIVE| flow     | ⤋            | [`E004_DISSIPATIVE.svg`](../glyphs/canonical/E004_DISSIPATIVE.svg)| Downward, spreading flow indicating energy dispersal and fading momentum. | TBD |

---

## Pressure Family (4 glyphs)

| PUA     | Name               | Category | Legacy Symbol | SVG File                                            | Brief Description                                                                 | PSH-256 (Canonical) |
|---------|--------------------|----------|---------------|-----------------------------------------------------|----------------------------------------------------------------------------------|----------------------|
| U+E005  | LOW_PRESSURE       | pressure | ◯            | [`E005_LOW_PRESSURE.svg`](../glyphs/canonical/E005_LOW_PRESSURE.svg)         | Open circle representing expansive, low-density, low-tension state.             | TBD |
| U+E006  | RISING_PRESSURE    | pressure | ◓            | [`E006_RISING_PRESSURE.svg`](../glyphs/canonical/E006_RISING_PRESSURE.svg)   | Half-filled circle indicating transitional buildup of pressure and tension.     | TBD |
| U+E007  | HIGH_PRESSURE      | pressure | ●            | [`E007_HIGH_PRESSURE.svg`](../glyphs/canonical/E007_HIGH_PRESSURE.svg)       | Solid filled circle representing maximal compression and dense, trapped energy. | TBD |
| U+E008  | COLLAPSING_PRESSURE| pressure | ◉            | [`E008_COLLAPSING_PRESSURE.svg`](../glyphs/canonical/E008_COLLAPSING_PRESSURE.svg) | Concentric rings with core point, expressing implosive inward collapse.         | TBD |

---

## Texture Family (4 glyphs)

| PUA     | Name        | Category | Legacy Symbol | SVG File                                        | Brief Description                                                            | PSH-256 (Canonical) |
|---------|-------------|----------|---------------|-------------------------------------------------|-----------------------------------------------------------------------------|----------------------|
| U+E009  | ORGANIC     | texture  | ∿            | [`E009_ORGANIC.svg`](../glyphs/canonical/E009_ORGANIC.svg)       | Flowing, irregular stroke suggesting organic, evolving, non-mechanical texture. | TBD |
| U+E00A  | GRAINED     | texture  | ⁘            | [`E00A_GRAINED.svg`](../glyphs/canonical/E00A_GRAINED.svg)       | Clustered micro-marks indicating granular, particulate, or noisy surfaces.   | TBD |
| U+E00B  | CRYSTALLINE | texture  | ◇            | [`E00B_CRYSTALLINE.svg`](../glyphs/canonical/E00B_CRYSTALLINE.svg) | Geometric diamond motif representing rigid, faceted, crystalline structure.  | TBD |
| U+E00C  | PUNCTATE    | texture  | ·            | [`E00C_PUNCTATE.svg`](../glyphs/canonical/E00C_PUNCTATE.svg)      | Sparse, isolated points conveying extreme minimalism and pointillistic texture. | TBD |

---

## Structure Family (5 glyphs)

| PUA     | Name       | Category | Legacy Symbol | SVG File                                     | Brief Description                                                                  | PSH-256 (Canonical) |
|---------|------------|----------|---------------|----------------------------------------------|-----------------------------------------------------------------------------------|----------------------|
| U+E00D  | PEAK       | structure| △            | [`E00D_PEAK.svg`](../glyphs/canonical/E00D_PEAK.svg)         | Ascending triangular form representing a singular high point or climax.          | TBD |
| U+E00E  | VALLEY     | structure| ▽            | [`E00E_VALLEY.svg`](../glyphs/canonical/E00E_VALLEY.svg)     | Inverted peak representing depression, trough, or low structural point.          | TBD |
| U+E00F  | PLATEAU    | structure| ▬            | [`E00F_PLATEAU.svg`](../glyphs/canonical/E00F_PLATEAU.svg)   | Extended horizontal band representing sustained elevation or maintained state.   | TBD |
| U+E010  | GRADIENT   | structure| ⟋            | [`E010_GRADIENT.svg`](../glyphs/canonical/E010_GRADIENT.svg) | Diagonal slope indicating continuous increase or decrease over time/space.       | TBD |
| U+E011  | SUBDUCTION | structure| ⊂            | [`E011_SUBDUCTION.svg`](../glyphs/canonical/E011_SUBDUCTION.svg) | One form beneath another, representing overlay, subsumption, or layered depth. | TBD |

---

## Operator Family (6 glyphs)

| PUA     | Name                | Category | Legacy Symbol | SVG File                                           | Brief Description                                                                    | PSH-256 (Canonical) |
|---------|---------------------|----------|---------------|----------------------------------------------------|-------------------------------------------------------------------------------------|----------------------|
| U+E012  | CONVERGENT_BOUNDARY | operator | ⊢⊣           | [`E012_CONVERGENT_BOUNDARY.svg`](../glyphs/canonical/E012_CONVERGENT_BOUNDARY.svg) | Two opposing faces meeting, representing compressive convergence or collision line. | TBD |
| U+E013  | OSCILLATION         | operator | ⟷            | [`E013_OSCILLATION.svg`](../glyphs/canonical/E013_OSCILLATION.svg)                 | Bidirectional relation indicating back-and-forth cycling between two states.       | TBD |
| U+E014  | DIRECTIONAL_FLOW    | operator | →            | [`E014_DIRECTIONAL_FLOW.svg`](../glyphs/canonical/E014_DIRECTIONAL_FLOW.svg)       | Arrow indicating directed movement, mapping, or causal transition.                 | TBD |
| U+E015  | FUSION              | operator | ◬            | [`E015_FUSION.svg`](../glyphs/canonical/E015_FUSION.svg)                           | Overlapping forms representing integration, merging, or synthesis of elements.     | TBD |
| U+E016  | CONTAINMENT         | operator | ⊚            | [`E016_CONTAINMENT.svg`](../glyphs/canonical/E016_CONTAINMENT.svg)                 | Enclosed ring structure indicating one state held within the bounds of another.   | TBD |
| U+E017  | EMERGENCE           | operator | ⊙            | [`E017_EMERGENCE.svg`](../glyphs/canonical/E017_EMERGENCE.svg)                     | Central point within a field, representing something arising from a surrounding medium. | TBD |

---

## Logic Family (4 glyphs)

| PUA     | Name         | Category | Legacy Symbol | SVG File                                      | Brief Description                                                                  | PSH-256 (Canonical) |
|---------|--------------|----------|---------------|-----------------------------------------------|-----------------------------------------------------------------------------------|----------------------|
| U+E018  | VOID         | logic    | ∅            | [`E018_VOID.svg`](../glyphs/canonical/E018_VOID.svg)         | Empty set / null-state marker denoting absence, annihilation, or evacuated context. | TBD |
| U+E019  | CONDITIONAL  | logic    | ☇            | [`E019_CONDITIONAL.svg`](../glyphs/canonical/E019_CONDITIONAL.svg) | Conditional strike representing contingent outcomes or “if-then” dynamics.      | TBD |
| U+E01A  | NEGATION     | logic    | ¬            | [`E01A_NEGATION.svg`](../glyphs/canonical/E01A_NEGATION.svg) | Logical not-operator indicating inversion or denial of a given state.             | TBD |
| U+E01B  | EQUIVALENCE  | logic    | ≡            | [`E01B_EQUIVALENCE.svg`](../glyphs/canonical/E01B_EQUIVALENCE.svg) | Triple-bar sign representing semantic or structural equivalence between states.  | TBD |

---

## Hash Publication Notes

Once all canonical SVGs are finalized and verified with the **PSH-256 v1.0 dihedral-normalized engine**, the **canonical hashes** for each glyph will be published here and in:

- `docs/SPECIFICATION-v1.0.md`
- `docs/APPENDIX-G-Grok-Certification.md`
- `reference/psh256_v1_0.py` docstrings (as test vectors)

Until then, the `TBD` entries serve as placeholders.

---

PICTOGRAM v1.0 — **The SHA-256 of Qualia.**
