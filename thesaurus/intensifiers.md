# PICTOGRAM Intensifiers

**Applying the Modifier Algebra to Natural Language Semantics**

---

## Purpose

This document specifies how **modifiers** from `MODIFIERS-SPEC.md` apply to the **semantic fields** defined in `semantic_fields.json` to create nuanced natural language mappings.

Intensifiers transform meaning along three axes:
- **Magnitude** (intensity scaling)
- **Dimension** (abstraction level)
- **Time** (temporal evolution)

---

## Core Principle: Modifiers Act on Molecules

Modifiers do **not** change the PSH-256 hash of atomic glyphs. Instead, they operate on **glyph molecules** (composed expressions) to modulate semantic force.

```
Base molecule: ●⤊ = "anger"
Modified: ●⤊² = "wrath" (intensified)
Modified: ●⤊³ = "fury-as-archetype" (maximal)
Modified: √●⤊ = "irritation" (seed/root)
```

The **topological identity** (`●` + `⤊`) remains constant. The **semantic force** changes.

---

## Intensity Modifiers (Magnitude Scaling)

### 1. Squared (²) — Intensification

**Effect**: Concentrates meaning, increases force, amplifies emotional weight.

| Base | Molecule | Squared | Natural Language |
|------|----------|---------|------------------|
| pressure | `●` | `●²` | oppression, heaviness |
| anger | `●⤊` | `●⤊²` | wrath, fury |
| light | `●∿` | `●∿²` | radiance, brilliance |
| cycle | `⟲` | `⟲²` | habitual pattern, compulsion |
| ascent | `△` | `△²` | soaring ambition |

**Usage Rule**: Apply `²` when the natural language synonym implies:
- Greater intensity
- Concentrated force
- Emotional escalation
- Habitual tendency

---

### 2. Cubed (³) — Archetypal / Maximal

**Effect**: Elevates to mythic/universal level, creates ambient field, maximal abstraction.

| Base | Molecule | Cubed | Natural Language |
|------|----------|-------|------------------|
| pressure | `●` | `●³` | tyranny, cosmic density |
| anger | `●⤊` | `●⤊³` | pure wrath (archetype) |
| light | `●∿` | `●∿³` | luminosity itself |
| stagnation | `▭` | `▭³` | absolute stillness, void |
| collapse | `◉` | `◉³` | singularity, black hole |

**Usage Rule**: Apply `³` when the word represents:
- An archetype or universal concept
- The essence of a quality (not just an instance)
- A field or ambient condition
- Mythic/cosmic scale

---

### 3. Half (½) — Attenuation

**Effect**: Softens, reduces intensity, creates mild or tentative forms.

| Base | Molecule | Half | Natural Language |
|------|----------|------|------------------|
| anger | `●⤊` | `●⤊½` | irritation, annoyance |
| pressure | `●` | `●½` | mild stress, tension |
| sadness | `●⤋` | `●⤋½` | melancholy, wistfulness |
| flow | `∿` | `∿½` | gentle breeze, trickle |

**Usage Rule**: Apply `½` when the synonym implies:
- Reduced intensity
- Preliminary or incipient state
- Gentleness or mildness
- Partial expression

---

### 4. Factorial (!) — Chaotic Amplification

**Effect**: Explosive, unpredictable intensification. Sudden shock.

| Base | Molecule | Factorial | Natural Language |
|------|----------|-----------|------------------|
| eruption | `⤊` | `⤊!` | volcanic explosion |
| surprise | `⤊◯` | `(⤊◯)!` | shock, astonishment |
| change | `▭→∿` | `(▭→∿)!` | sudden transformation |

**Usage Rule**: Apply `!` when the word implies:
- Sudden, violent change
- Shock or surprise
- Chaotic escalation
- Loss of control

---

### 5. Infinity (∞) — Eternal / Universal

**Effect**: Timeless, boundless, mythic-scale permanence.

| Base | Molecule | Infinity | Natural Language |
|------|----------|----------|------------------|
| cycle | `⟲` | `⟲∞` | eternal return |
| pain | `●⤋` | `●⤋∞` | eternal suffering, agony |
| light | `●∿` | `●∿∞` | divine light |
| pattern | `⟲∿` | `⟲∿∞` | cosmic breath, universal rhythm |

**Usage Rule**: Apply `∞` when the word implies:
- Timeless or eternal quality
- Universal archetype
- Divine or cosmic scale
- Boundless extent

---

## Dimensional Modifiers (Abstraction Level)

### 1. Squared (²) — Pattern / Tendency

**Effect**: Transforms event → habit, state → trait, instance → pattern.

| Event (base) | Pattern (²) |
|--------------|-------------|
| `⤊` (eruption) | `⤊²` (eruptive tendency) |
| `●` (pressure) | `●²` (oppressive pattern) |
| `⟲` (cycle) | `⟲²` (cyclical habit) |

**Linguistic mapping**:
- Verb → Gerund (run → running)
- State → Trait (angry → wrathful)
- Action → Habit (walk → walking pattern)

---

### 2. Cubed (³) — Field / Archetype

**Effect**: Transforms pattern → ambient field, trait → essence, habit → category.

| Pattern (²) | Field (³) |
|-------------|-----------|
| `⤊²` (eruptive tendency) | `⤊³` (chaos as field) |
| `●²` (oppressive pattern) | `●³` (tyranny as essence) |
| `∿²` (flowing pattern) | `∿³` (fluidity itself) |

**Linguistic mapping**:
- Adjective → Abstract noun (bright → luminosity)
- Trait → Archetype (wrathful → wrath itself)
- Process → Category (flowing → flow as concept)

---

### 3. Root (√) — Seed / Proto-form

**Effect**: Reduces to germinal state, potential, incipient form.

| Full form | Seed (√) |
|-----------|----------|
| `●⤊` (anger) | `√●⤊` (irritability, potential for anger) |
| `●∿` (bright light) | `√●∿` (spark) |
| `△` (ascent) | `√△` (aspiration, latent rise) |

**Linguistic mapping**:
- Developed form → Potential (anger → irritability)
- Result → Cause (light → spark)
- Effect → Seed (growth → germination)

---

## Transformational Modifiers (Temporal)

### 1. Derivative (′) — Becoming / Rate of Change

**Effect**: Indicates transition, process of change, evolution in progress.

| Static | Dynamic (′) |
|--------|-------------|
| `●` (pressure) | `●′` (pressure building) |
| `●⤊` (anger) | `●⤊′` (becoming angry, rage rising) |
| `◯` (openness) | `◯′` (opening, releasing) |

**Linguistic mapping**:
- State → Process (angry → getting angry)
- Noun → Verb (explosion → exploding)
- Condition → Transition (open → opening)

---

### 2. Integral (∫) — Accumulated History

**Effect**: Indicates accumulation over time, narrative weight, memory, trauma.

| Momentary | Accumulated (∫) |
|-----------|----------------|
| `●` (pressure) | `∫●` (accumulated pressure, trauma) |
| `●⤊` (anger) | `∫●⤊` (long-held resentment) |
| `△` (rise) | `∫△` (achievement, growth over time) |

**Linguistic mapping**:
- Event → History (pressure → trauma)
- Feeling → Long-term condition (anger → resentment)
- Action → Legacy (rising → achievement)

---

### 3. Inverse (⁻¹) — Antonym / Negation

**Effect**: Semantic inversion, systematic antonym construction.

| Base | Inverse (⁻¹) |
|------|-------------|
| `●⤊` (anger) | `●⤊⁻¹` (reconciliation, forgiveness) |
| `●` (pressure) | `●⁻¹` (release, freedom) |
| `⟲` (cycle) | `⟲⁻¹` (linear, termination) |

**Linguistic mapping**:
- Concept → Opposite (pressure → release)
- Emotion → Resolution (anger → peace)
- Process → Reversal (cycle → linear path)

See `antonym_rules.md` for systematic opposition logic.

---

## Composition Rules

### 1. Single Glyph Application
```
●² = intensified pressure
√⤊ = seed of eruption
∫● = accumulated pressure
```

### 2. Molecule Application
```
(●⤊)² = intensified anger molecule
●(⤊²) = pressure + eruptive pattern
```

### 3. Sequence Application
```
●⤊◉ ² = entire catastrophic sequence intensified
(⟲∿△)³ = ascending organic cycle as archetypal field
```

### 4. Nested Modifiers
```
∫((●⤊)′) = accumulated history of rising anger
((●⤊)²)⁻¹ = inversion of intensified anger = deep peace
```

---

## Thesaurus Integration

Every entry in `semantic_fields.json` can generate a **synonym cloud** via modifiers:

**Example: "anger" family**
```
●⤊ → anger (base)
●⤊½ → irritation (attenuated)
●⤊² → wrath (intensified)
●⤊³ → fury-archetype (maximal)
√●⤊ → irritability (seed)
●⤊′ → becoming angry (derivative)
∫●⤊ → resentment (accumulated)
●⤊⁻¹ → reconciliation (inverse)
```

This creates **8+ natural language synonyms** from a **single 2-glyph molecule**.

---

## VSE Computational Mapping

In Vector-Space Esperanto, modifiers are **functions on semantic vectors**:

```python
def apply_modifier(base_vector, modifier):
    if modifier == "²":
        return amplify(base_vector, factor=2)
    elif modifier == "³":
        return archetype(base_vector)
    elif modifier == "√":
        return seed(base_vector)
    elif modifier == "′":
        return derivative(base_vector)
    elif modifier == "∫":
        return integral(base_vector)
    elif modifier == "⁻¹":
        return inverse(base_vector)
    # ... etc.
```

See `VSE-SPEC.md` for complete vector operations.

---

## Artistic Application

Writers can now encode **emotional arcs** directly:

**Grief trajectory**:
```
∫● → ●′⁻¹ → √◯
(accumulated pressure → releasing → seed of openness)
= processing trauma → letting go → new beginning
```

**Rage cycle**:
```
√●⤊ → ●⤊′ → ●⤊² → ⤊! → ◉ → ◯′
irritability → rising anger → wrath → explosion → collapse → opening
```

---

## Status

- ✅ Core intensity modifiers defined
- ✅ Dimensional scaling operational
- ✅ Temporal transformations specified
- 🚧 Cross-linguistic validation in progress
- 📋 Metaphor engine integration (v1.3)

---

**The intensifiers are live.**  
**Meaning now has calculus.**
