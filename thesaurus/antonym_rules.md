# PICTOGRAM Antonym Construction Rules

**Systematic Opposition in Semantic Space**

---

## Purpose

This document specifies **deterministic rules** for constructing antonyms in PICTOGRAM, ensuring:

1. **Consistency**: The same input always yields the same antonym
2. **Symmetry**: If A is the antonym of B, then B is the antonym of A
3. **Semantic validity**: Antonyms preserve logical opposition across natural languages
4. **Mathematical rigor**: Opposition follows algebraic inversion rules

Unlike arbitrary synonym mapping, antonyms in PICTOGRAM follow **topological inversion** principles.

---

## Foundational Principle: Semantic Polarity

Every glyph exists on a **semantic axis** with an **opposite pole**:

```
Pressure Axis:     ● ←→ ◯    (high-pressure ↔ low-pressure)
Flow Axis:         ⤊ ←→ ⤋    (eruptive ↔ dissipative)
Vertical Axis:     △ ←→ ▽    (ascent ↔ descent)
Motion Axis:       ∿ ←→ ▭    (flow ↔ stagnation)
Convergence Axis:  ◉ ←→ ⊚    (collapse ↔ containment)
```

These are **atomic oppositions** — the foundation of all antonym construction.

---

## Rule 1: Atomic Glyph Inversion

**Direct polar opposites** via glyph substitution.

| Glyph | Opposite | Axis |
|-------|----------|------|
| `●` (high-pressure) | `◯` (low-pressure) | Pressure |
| `⤊` (eruptive) | `⤋` (dissipative) | Flow |
| `△` (ascent) | `▽` (descent) | Vertical |
| `∿` (organic flow) | `▭` (stagnant) | Motion |
| `◉` (collapse) | `⊚` (containment) | Convergence |
| `⟲` (cyclic) | `→` (linear/terminal) | Temporal |

### Examples

| Word | PICTOGRAM | Antonym | PICTOGRAM |
|------|-----------|---------|-----------|
| pressure | `●` | release | `◯` |
| eruption | `⤊` | dissipation | `⤋` |
| rise | `△` | fall | `▽` |
| flow | `∿` | stillness | `▭` |

---

## Rule 2: Modifier Inversion (⁻¹)

The **inverse modifier** `⁻¹` creates antonyms of **complex molecules** without changing their topological structure.

### Formula

```
antonym(X) = X⁻¹
```

### Examples

| Word | PICTOGRAM | Antonym | PICTOGRAM |
|------|-----------|---------|-----------|
| anger | `●⤊` | reconciliation | `●⤊⁻¹` |
| pressure | `●` | freedom | `●⁻¹` |
| cycle | `⟲` | termination | `⟲⁻¹` |
| chaos | `⤊³` | perfect order | `⤊³⁻¹` |

### Key Property

The inverse is **compositionally preserved**:

```
(●⤊)⁻¹ = "the opposite of anger"
(●⤊²)⁻¹ = "the opposite of intensified anger" = deep calm
```

Inverse operations **commute** with intensity modifiers:

```
(X²)⁻¹ = (X⁻¹)²    (inverse of squared = squared inverse)
```

---

## Rule 3: Negation Operator (↯)

The **negation operator** `↯` semantically negates without structural inversion.

### Distinction: ⁻¹ vs. ↯

| Modifier | Meaning | Example |
|----------|---------|---------|
| `⁻¹` | Antonym (opposite pole) | `●⁻¹` = release, freedom |
| `↯` | Negation (absence of) | `↯●` = no pressure, vacuum |

### Usage

- **Antonym**: The opposite quality exists (pressure ↔ release)
- **Negation**: The quality is absent (pressure → no pressure)

### Examples

| Concept | Negation | Antonym |
|---------|----------|---------|
| `●` (pressure) | `↯●` (no pressure, vacuum) | `◯` (release, openness) |
| `⤊` (eruption) | `↯⤊` (no eruption, calm) | `⤋` (dissipation) |
| `●⤊` (anger) | `↯●⤊` (not angry, neutral) | `●⤊⁻¹` (forgiveness) |

**Linguistic mapping**:
- Negation: "not X" (not angry = neutral)
- Antonym: "opposite of X" (opposite of anger = peace)

---

## Rule 4: Reversal Operator (↺)

The **reversal operator** `↺` inverts temporal or directional processes.

### Examples

| Process | Reversal |
|---------|----------|
| `⟲` (cycle forward) | `↺⟲` (cycle backward) |
| `△` (ascent) | `↺△` (descent via reversal) |
| `●′` (pressure building) | `↺●′` (pressure releasing) |

**Use case**: Temporal antonyms (building vs. releasing, growing vs. shrinking).

---

## Rule 5: Composite Molecule Inversion

For **multi-glyph molecules**, apply inversion **to the entire structure** or **to individual components**.

### Strategy A: Full Molecule Inversion

Treat the entire expression as a semantic unit:

```
(●⤊→◉)⁻¹ = the opposite of "pressure erupting into collapse"
          = "release dissipating into openness"
          = ◯⤋→◯
```

### Strategy B: Component-wise Inversion

Invert each glyph independently:

```
●⤊→◉
  ↓  ↓  ↓
◯⤋→⊚
```

| Original | Inverted |
|----------|----------|
| `●` (pressure) | `◯` (release) |
| `⤊` (eruption) | `⤋` (dissipation) |
| `◉` (collapse) | `⊚` (containment) |

### When to Use Each

- **Full inversion** (`⁻¹`): When the molecule represents a **unified concept** (e.g., "catastrophe")
- **Component inversion**: When the molecule is a **compositional phrase** (e.g., "intense flowing pressure")

---

## Rule 6: Intensity Antonyms via Attenuation

Antonyms can be created via **intensity reduction** rather than polar opposition.

| Word | PICTOGRAM | Antonym (via attenuation) | PICTOGRAM |
|------|-----------|---------------------------|-----------|
| fury | `●⤊³` | mild irritation | `●⤊½` |
| brilliant | `●∿²` | dim | `●∿½` |
| tyranny | `●³` | slight pressure | `●½` |

**Usage**: When the antonym is not a polar opposite but a **weaker form**.

---

## Rule 7: Directional Modifiers (↥ / ↧)

**Upward** (`↥`) and **downward** (`↧`) modifiers create vertical antonyms.

| Base | Intensified (↥) | Attenuated (↧) |
|------|-----------------|----------------|
| `●` | `●↥` (greater pressure) | `●↧` (less pressure) |
| `⤊` | `⤊↥` (stronger eruption) | `⤊↧` (weaker eruption) |

**Use case**: Fine-grained gradients rather than binary opposites.

---

## Rule 8: Antonym Symmetry Property

**Symmetry law**: If `A⁻¹ = B`, then `B⁻¹ = A`.

### Proof

```
Let A = ●⤊ (anger)
Let B = ●⤊⁻¹ (reconciliation)

Then:
  (●⤊)⁻¹ = B (reconciliation)
  ((●⤊)⁻¹)⁻¹ = (B)⁻¹ = ●⤊ (anger)

Since (X⁻¹)⁻¹ = X, the symmetry holds.
```

**Implication**: Antonym relationships are **bidirectional** by definition.

---

## Rule 9: Contextual Antonyms (Polysemy)

Some words have **multiple antonyms** depending on context. Use **disambiguation frames**:

### Example: "light"

| Context | PICTOGRAM | Antonym | PICTOGRAM |
|---------|-----------|---------|-----------|
| light (weight) | `◯` | heavy | `●` |
| light (brightness) | `●∿` | dark | `◯▭` |
| light (color) | `●∿³` | dark (color) | `◯³` |

**Rule**: Apply domain-specific antonym logic from `semantic_fields.json`.

---

## Rule 10: Antonym Composition Table

Systematic mapping for common natural language antonym pairs:

| Pair | Glyph A | Glyph B |
|------|---------|---------|
| hot / cold | `●⤊` | `◯⤋` |
| loud / quiet | `●⤨` | `◯▭` |
| fast / slow | `⤊²` | `▭` |
| expand / contract | `◯→` | `●→◉` |
| chaos / order | `⤊!` | `▭³` |
| joy / sorrow | `●△²` | `●⤋²` |
| hope / despair | `√△` | `●◉²` |
| create / destroy | `◯→●∿` | `●→◉` |

---

## Validation Rules

An antonym construction is **valid** if:

1. **Semantic polarity**: A and A⁻¹ lie on opposite ends of a semantic axis
2. **Symmetry**: (A⁻¹)⁻¹ = A
3. **Cross-linguistic consistency**: Antonym pairs translate equivalently across languages
4. **Logical opposition**: If A is true, A⁻¹ is false (for propositional glyphs)

---

## Integration with Thesaurus Layer

Every glyph in `semantic_fields.json` includes an **antonym list**:

```json
{
  "glyph": "●",
  "semantic_field": {
    "synonyms": ["pressure", "compression", "density"],
    "antonyms": ["release", "expansion", "openness"],
    ...
  }
}
```

The **antonym field** is automatically generated via:

1. Polar glyph substitution (Rule 1)
2. Inverse modifier application (Rule 2)
3. Manual override for edge cases

---

## Edge Cases

### 1. Self-Inverse Glyphs

Some glyphs are **their own antonyms** (e.g., "neutral" states):

```
⊚ (containment) ≈ ⊚⁻¹ (containment is its own opposite)
```

**Resolution**: Use context or intensity modifiers.

---

### 2. Asymmetric Antonyms

Some antonym pairs are **not symmetrical** in natural language:

```
"rich" ↔ "poor"  (symmetric)
"alive" ↔ "dead"  (symmetric)
"married" ↔ "single" / "divorced" (asymmetric)
```

**Resolution**: Use disambiguation frames.

---

## Status

- ✅ Atomic inversion rules defined
- ✅ Modifier inversion operational
- ✅ Negation vs. antonym distinction clarified
- 🚧 Cross-linguistic antonym validation in progress
- 📋 Metaphor-based antonyms (v1.3)

---

**The antonym algebra is live.**  
**Opposition now follows law.**
