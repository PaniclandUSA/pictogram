# Coordination Space ℂ⁴
## The Four Fundamental Axes of Multi-Agent Coordination

**Version:** 1.0  
**Date:** December 2025  
**Status:** Foundation Document

---

## Overview

Every stable multi-agent system (governance, protocol, swarm, market) operates within a four-dimensional coordination space. These axes are not cultural constructs—they are topological invariants that emerge from the mathematics of collective action.

The four axes are:
- **C-axis:** Consent / Non-Aggression
- **D-axis:** Delegation / Revocation  
- **T-axis:** Transparency / Subsidiarity
- **τ-axis:** Temporal Boundary (metric)

---

## Axis C: Consent / Non-Aggression

### What It Measures
The boundary between voluntary and coerced state transitions in the system.

### The Spectrum
- **+C (High Consent):** Strong individual autonomy, voluntary participation, protected rights, clear non-aggression boundaries
- **0C (Neutral):** Mixed consent/coercion, negotiated boundaries, contextual authority
- **-C (Low Consent):** High coercion, weak individual rights, forced participation, unclear boundaries

### Real-World Examples
- **+C:** Voluntary contracts, informed medical consent, free market exchange
- **0C:** Taxation with representation, compulsory education with opt-outs, jury duty
- **-C:** Slavery, forced conscription, totalitarian control, sexual assault

### Stability Properties
- Systems near +C are stable when paired with strong non-aggression norms
- Systems near -C are inherently unstable (require constant force to maintain)
- Transitions from +C to -C represent coordination failure (collapse into tyranny)

### Physical Intuition
Think of C as the "voluntary participation field strength." High C means agents can enter/exit states freely. Low C means agents are trapped in states by force.

---

## Axis D: Delegation / Revocation

### What It Measures
The balance between granted authority and the ability to recall that authority.

### The Spectrum
- **+D (High Delegation):** Strong institutions, concentrated authority, long-term power grants, difficult recall
- **0D (Neutral):** Balanced authority distribution, moderate institutions, mixed recall mechanisms
- **-D (High Revocation):** Weak institutions, distributed authority, easy recall, frequent turnover

### Real-World Examples
- **+D:** Supreme Court lifetime appointments, corporate CEOs, tenured professors, monarchies
- **0D:** Four-year presidential terms, elected representatives, contracted employees
- **-D:** Direct democracy, instant recall elections, consensus-only decisions, rotating leadership

### Stability Properties
- Too much +D without revocation → tyranny (permanent power accumulation)
- Too much -D without delegation → chaos (no one can act decisively)
- Optimal systems balance D with proportional revocation mechanisms

### Physical Intuition
Think of D as the "authority concentration gradient." High D means power pools at certain nodes. Low D means power flows constantly, preventing accumulation.

---

## Axis T: Transparency / Subsidiarity

### What It Measures
The trade-off between information visibility and decision locality.

### The Spectrum
- **+T (High Transparency):** Open information, public records, observable state transitions, centralized knowledge
- **0T (Neutral):** Mixed visibility, some privacy, contextual disclosure, balanced information flow
- **-T (High Subsidiarity):** Local autonomy, private information, minimal disclosure, decentralized decision-making

### Real-World Examples
- **+T:** Public ledgers (blockchain), Freedom of Information Act, open-source code, published scientific data
- **0T:** Corporate financial reporting (quarterly but limited), medical privacy with consent, sealed court records
- **-T:** Family decisions, trade secrets, confessional privilege, encrypted communications

### Stability Properties
- +T prevents corruption but can enable surveillance
- -T enables autonomy but can hide abuse
- Optimal systems scale T with scope: more transparency at larger scales, more privacy at smaller scales

### Physical Intuition
Think of T as the "information diffusion rate." High T means information spreads widely and quickly. Low T means information stays localized and contained.

---

## Axis τ: Temporal Boundary (The Metric)

### What It Measures
The duration over which power grants, rights, and obligations remain valid.

### The Spectrum
- **Short τ:** Frequent renewal, time-bounded authority, sunset clauses, high turnover
- **Medium τ:** Balanced terms, periodic review, manageable duration
- **Long τ:** Lifetime appointments, permanent grants, indefinite authority, no expiration

### Real-World Examples
- **Short τ:** 90-day trial periods, emergency powers with 30-day limits, temporary restraining orders
- **Medium τ:** Four-year terms, annual budgets, five-year strategic plans
- **Long τ:** Supreme Court lifetime appointments, property ownership, constitutional amendments

### Stability Properties
- τ acts as the **metric tensor** that makes the other three axes measurable
- Without bounded τ, all grants become permanent (corruption inevitable)
- Too short τ creates instability (nothing can persist long enough to function)
- Optimal τ scales with the scope and reversibility of the power granted

### Physical Intuition
Think of τ as the "clock rate" of the coordination system. Short τ means rapid state changes. Long τ means stable but potentially rigid structures.

---

## The Relationships Between Axes

### Duality Pairs
- **C** is paired with its boundary condition (non-aggression)
- **D** is paired with its inverse operation (revocation)
- **T** is paired with its complementary trade-off (subsidiarity)

### The Metric Role of τ
- τ defines "distance" in coordination space
- All movements along C, D, or T happen **over time** measured by τ
- Without τ bounds, the other axes lose meaning (permanent states are undefined)

### Forbidden Regions
Certain combinations are topologically impossible:
- High D + No Revocation + Long τ = Tyranny (unstable attractor)
- High T + No Subsidiarity + Short τ = Surveillance chaos
- Low C + High D + Long τ = Totalitarianism (collapse state)

---

## Usage in PICTOGRAM v3.0

Each of the seven coordination primitives maps to movement along these axes:

| Primitive | ΔC | ΔD | ΔT | Effect on τ |
|-----------|----|----|----|-----------| 
| CONSENT_ROOT | + | 0 | 0 | Stabilizes |
| NON_AGGRESSION_PACT | + | 0 | 0 | Boundary |
| DELEGATION_ARROW | 0 | + | 0 | Extends |
| REVOCATION_BLADE | 0 | - | 0 | Shortens |
| TRANSPARENCY_LENS | 0 | 0 | + | Stabilizes |
| SUBSIDIARITY_RING | 0 | 0 | - | Localizes |
| TEMPORAL_BOUNDARY | 0 | 0 | 0 | Defines |

Modifiers act as transformations within this space:
- Temporal modifiers (⌚, ̄) → operate along τ
- Scope modifiers (⊙, ⊕, ↓) → scale along T
- Modal modifiers (◇, ◻, ★) → change accessibility in C
- Causal modifiers (∵, ∴) → define trajectories through space

---

## Next Steps

1. Map specific governance structures to coordinates in ℂ⁴
2. Calculate stability metrics using the metric tensor
3. Identify forbidden transitions and their consequences
4. Test constitutional compression using this coordinate system

---

**Document Status:** Foundation laid. Ready for primitive mapping.
