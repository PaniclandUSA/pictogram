**Version:** 1.0
**Date:** 2025-12-09
**Status:** Formal Definition

---

## 1. The Manifold

We define **Coordination Space** ($\mathcal{M}$) as a 4-dimensional Lorentzian manifold with coordinates $x^\mu = (\tau, C, D, T)$.

* $x^0 = \tau$ (Temporal Boundary / Time)
* $x^1 = C$ (Consent)
* $x^2 = D$ (Delegation)
* $x^3 = T$ (Transparency)

## 2. The Metric Interval

The invariant interval $ds^2$ defines the "legitimacy" of a trajectory through coordination space.

$$ds^2 = -c_{coord}^2 d\tau^2 + dC^2 + dD^2 + dT^2$$

Where:
* $c_{coord}$ is the **Speed of Coordination**: The maximum rate at which information and consent can propagate through the agent network.
* $d\tau$ is the change in temporal duration.
* $dC, dD, dT$ are changes in the topological state variables.

## 3. Causal Structure (The Light Cone)

The sign of $ds^2$ determines the nature of the coordination event:

### A. Timelike Interval ($ds^2 < 0$)
**Status:** **LEGITIMATE**
The change in time ($d\tau$) is sufficient to account for the changes in state ($dC, dD, dT$). The system is causally connected. Consent and transparency have "caught up" to the action.

### B. Lightlike Interval ($ds^2 = 0$)
**Status:** **CRITICAL LIMIT**
The system is operating at exactly the speed of coordination. This is the **Event Horizon** of governance. Maximum efficiency before breaking legitimacy.

### C. Spacelike Interval ($ds^2 > 0$)
**Status:** **FORBIDDEN (TYRANNY/CHAOS)**
The state changes ($dC, dD, dT$) are strictly larger than the time allowed ($c_{coord} d\tau$). The action effectively happens "faster than light."
* *Example:* A law passed and enforced instantly without public reading ($dT$ change without sufficient $d\tau$).
* *Example:* A revocation of rights without due process ($dC$ change without sufficient $d\tau$).

## 4. The Stability Condition

For a governance structure to be stable, the integral of its trajectory $\gamma$ must be real and negative:

$$S[\gamma] = \int_{\tau_1}^{\tau_2} \sqrt{-ds^2} > 0$$

If the term under the square root becomes positive (spacelike), the action is imaginary/undefined in the legitimate manifold.
