# PICTOGRAM Thesaurus Layer

**Status**: Draft v1.1  
**Purpose**: Semantic Field Mapping for Natural Language ↔ PICTOGRAM Translation

---

## Overview

The Thesaurus Layer provides the **semantic halo** around each of PICTOGRAM's 28 canonical glyphs, enabling:

- **Synonym mapping**: Multiple natural language words → single glyph molecule
- **Antonym construction**: Systematic opposition via modifiers and operators
- **Emotional coloration**: Affective tones and intent vectors
- **Domain classification**: Conceptual categories (flow, pressure, texture, structure, logic)
- **Intensity gradients**: Fine-grained meaning through modifier algebra

This layer bridges **Roget/Webster lexical semantics** with **PICTOGRAM's mathematical formalism**.

---

## Architecture

```
thesaurus/
├── semantic_fields.json      # Core synonym/antonym/emotion mappings
├── intensifiers.md            # Modifier algebra application guide
├── antonym_rules.md           # Systematic opposition construction
├── polysemy_protocol.md       # Disambiguation for multi-meaning words
└── README.md                  # This file
```

---

## Core Principle: Glyph Molecules

Natural language words are **composed** from glyphs + operators + modifiers:

| Word | PICTOGRAM | Decomposition |
|------|-----------|---------------|
| anger | `●⤊` | high-pressure + eruption |
| fury | `●⤊²` | anger intensified (squared) |
| irritation | `√●⤊` | seed of anger (root) |
| calm | `◯▭` | low-pressure + stagnation |
| reconciliation | `●⤊⁻¹` | anger inverted (antonym) |

---

## Semantic Field Vector (SFV)

Each glyph receives an **SFV**:

```json
{
  "glyph": "●",
  "unicode": "U+E000",
  "semantic_field": {
    "synonyms": ["pressure", "compression", "density", "tension", "force"],
    "antonyms": ["release", "expansion", "openness", "freedom"],
    "emotional_tones": ["anxiety", "urgency", "intensity", "focus"],
    "intent_vectors": ["to compress", "to concentrate", "to apply force"],
    "conceptual_domain": "pressure"
  }
}
```

---

## Integration with Modifier Algebra

The **intensifiers** and **dimensional operators** from `MODIFIERS-SPEC.md` work **on top of** the semantic fields:

- `●²` = intensified pressure → "oppression"
- `●³` = archetypal pressure field → "tyranny"
- `●′` = pressure becoming → "building tension"
- `∫●` = accumulated pressure → "trauma"

See `intensifiers.md` for complete application rules.

---

## Antonym Construction

Antonyms follow **systematic rules** rather than arbitrary mapping:

1. **Pressure ↔ Openness**: `●` ↔ `◯`
2. **Eruption ↔ Dissipation**: `⤊` ↔ `⤋`
3. **Inversion modifier**: `X⁻¹` = antonym of X
4. **Negation operator**: `↯X` = semantic negation

See `antonym_rules.md` for full specification.

---

## Polysemy Handling

Words with multiple meanings require **disambiguation frames**:

**Example: "run"**
- *flee* → `⤊→◓` (eruption → flow)
- *jog* → `⤊½` (mild eruption)
- *operate* → `▭→⤊` (stagnation → activation)
- *campaign* → `⤊△` (rise toward peak)

See `polysemy_protocol.md` for the VSE disambiguation algorithm.

---

## Status & Roadmap

- ✅ Core 28 glyphs defined
- ✅ Modifier algebra canonical (MODIFIERS-SPEC.md)
- 🚧 Semantic field population (in progress)
- 🚧 Cross-language mapping (v1.2)
- 📋 Metaphor engine (v1.3)

---

## Contributing

To add semantic mappings:

1. Identify the **conceptual domain** (pressure, flow, texture, etc.)
2. Decompose the word into **glyph molecules**
3. Apply **modifiers** for intensity/dimension/time
4. Add to `semantic_fields.json` with SFV
5. Test **antonym consistency** using opposition rules

All contributions must preserve:
- PSH-256 topological identity
- D4 symmetry invariance
- Esper Stack compatibility

---

## References

- [MODIFIERS-SPEC.md](../docs/MODIFIERS-SPEC.md) - The modifier algebra
- [PSH-256.md](../docs/PSH-256.md) - Cryptographic hashing
- [VSE-SPEC.md](../docs/VSE-SPEC.md) - Vector-Space Esperanto integration

---

**The semantic halo layer is now live.**  
**Meaning has structure. Structure has mathematics. Mathematics has glyphs.**
