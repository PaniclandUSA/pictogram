# PICTOGRAM Canonical Glyph Table (v1.0)

All 28 canonical glyphs, as defined in `glyphs/registry.json`, including their
PUA codepoints, display equivalents, SVG sources, PSH-256 canonical hashes, and
semantic vectors.

---

## Legend

- **PUA** – Unicode Private Use Area codepoint for this glyph  
- **Disp.** – Human-friendly visual stand-in (not the canonical PUA)  
- **SVG File** – Canonical 512×512 SVG source  
- **PSH-256** – Orientation-invariant semantic-topological hash (hex)  
- **Sem. Vector** – Compressed description of the intended semantic field  

---

## Flow Glyphs

| #  | Name        | PUA     | Disp. | SVG File             | PSH-256 Canonical Hash                                                       | Semantic Vector |
|----|-------------|---------|-------|----------------------|-------------------------------------------------------------------------------|-----------------|
| 01 | CYCLIC      | U+E000  | ⟲    | `E000_CYCLIC.svg`    | `74052bd14dfd3b66b71ee19f346ddda985578eb21f6d6e1159a3da450137ed89`           | ⟨TEMPORAL:RECURSIVE \| PATTERN:PERIODIC \| MOMENTUM:SUSTAINED⟩ |
| 02 | ERUPTIVE    | U+E001  | ⤊    | `E001_ERUPTIVE.svg`  | `f283113825a066ce8f077a336704c44da097b1cc854d45968d13bdc1595245fb`           | ⟨TEMPORAL:ASCENT \| ENERGY:BREAKTHROUGH \| PRESSURE:ACCELERATING⟩ |
| 03 | STAGNANT    | U+E002  | ▭    | `E002_STAGNANT.svg`  | `7c282e9b8841d485c152cd630b17e512a423f8fb47b76b3b65fd001bf3da1959`           | ⟨TEMPORAL:STATIC \| MOMENTUM:ZERO \| INERTIA:MAXIMUM⟩ |
| 04 | TURBULENT   | U+E003  | ⤨    | `E003_TURBULENT.svg` | `864fd323d9bb726d32f107ffb0fe3fddfbad70696167e1f138eecc5b0426a1ed`           | ⟨TEMPORAL:IRREGULAR \| PATTERN:CHAOTIC \| COHERENCE:LOW⟩ |
| 05 | DISSIPATIVE | U+E004  | ⤋    | `E004_DISSIPATIVE.svg` | `cb28fbb130a794a65d6dec588c6a07fa37f6e382d4a02adc01110bea6f5144ab`         | ⟨TEMPORAL:DESCENT \| ENERGY:RELEASE \| PRESSURE:DECREASING⟩ |
| 17 | ASCENT      | U+E010  | ⟋    | `E016_ASCENT.svg`    | `7892f6d13804d99d4cd19b11059f259dfbff44128e741a4756c3213bb9b6888e`           | ⟨TRAJECTORY:UPWARD \| TEMPORAL:DIRECTIONAL \| CHANGE:POSITIVE⟩ |
| 20 | OSCILLATION | U+E013  | ∿∿   | `E019_OSCILLATION.svg` | `29aedf0a6915373ac468e7e92fd9f92732d1402cbc6f3d95c7aba6e915b642d7`         | ⟨TEMPORAL:BACK-AND-FORTH \| STABILITY:METASTABLE \| PERIODICITY:HIGH⟩ |

---

## Pressure Glyphs

| #  | Name               | PUA     | Disp. | SVG File                   | PSH-256 Canonical Hash                                                       | Semantic Vector |
|----|--------------------|---------|-------|----------------------------|-------------------------------------------------------------------------------|-----------------|
| 06 | LOW_PRESSURE       | U+E005  | ◯    | `E005_LOW_PRESSURE.svg`    | `385e7b765ba60a6c5a40aeb55f0db7f22e126fa8b05003deeb83225888f0f464`           | ⟨TENSION:MINIMAL \| SPACE:EXPANSIVE \| DENSITY:LOW \| VOLUME:INCREASING⟩ |
| 07 | RISING_PRESSURE    | U+E006  | ◓    | `E006_RISING_PRESSURE.svg` | `e4b55003373aa01971cd64e2f7a31d5b4c8207ae16ff2ceb3f366fd6c36ee45b`           | ⟨TENSION:INCREASING \| TRAJECTORY:UPWARD \| TRANSITION:ACTIVE \| MOMENTUM:BUILDING⟩ |
| 08 | HIGH_PRESSURE      | U+E007  | ●    | `E007_HIGH_PRESSURE.svg`   | `c64d12bd1f6fbf6b5a341c8be12a9046f97304e09ba35c9c3ddf9cafc737ff5b`           | ⟨TENSION:MAXIMUM \| DENSITY:MAXIMAL \| COMPRESSION:EXTREME \| STABILITY:PRECARIOUS⟩ |
| 09 | COLLAPSING_PRESSURE| U+E008  | ◉    | `E008_COLLAPSING_PRESSURE.svg` | `035b5c8e895df284f4592d13640a64960bddf96f54a64ad4706938cda5df1995`       | ⟨TENSION:RELEASING \| DIRECTION:INWARD \| MOMENTUM:IMPLOSIVE \| TRANSITION:CATASTROPHIC⟩ |

---

## Texture Glyphs

| #  | Name       | PUA     | Disp. | SVG File              | PSH-256 Canonical Hash                                                       | Semantic Vector |
|----|------------|---------|-------|-----------------------|-------------------------------------------------------------------------------|-----------------|
| 10 | CRYSTALLINE| U+E009  | ◇    | `E009_CRYSTALLINE.svg`| `e6c6a6ef50900279f95d22355d96bb2fbb1ae5e7b224f07be27dd89ee08d583c`           | ⟨TEXTURE:CRISP \| STRUCTURE:DISCRETE \| ORDER:HIGH⟩ |
| 11 | ORGANIC    | U+E00A  | ∿    | `E010_ORGANIC.svg`    | `547a3b1050afba89cb8cc69f624eff894815b0b8f531ea54d8e24ad22700d7fc`           | ⟨TEXTURE:SOFT \| STRUCTURE:CONTINUOUS \| ORDER:MEDIUM⟩ |
| 12 | MINIMAL    | U+E00B  | ·     | `E011_MINIMAL.svg`    | `ff18199accb6713b5075c9f3a7700c8ee53c820a9e0a9a5cbd9b8f4b8b09580e`           | ⟨TEXTURE:SPARSE \| DENSITY:MINIMAL \| ARTICULATION:POINTLIKE⟩ |
| 13 | DIFFUSE    | U+E00C  | ⁘    | `E012_DIFFUSE.svg`    | `bee2a0de394f779a0dbebd33f84ab9b5c80896cc618c4b3a1d2f41fb46d191d1`           | ⟨TEXTURE:GRAINED \| DENSITY:LOW \| DISTRIBUTION:SPARSE-MULTIPOINT⟩ |

---

## Structure Glyphs

| #  | Name         | PUA     | Disp. | SVG File                | PSH-256 Canonical Hash                                                       | Semantic Vector |
|----|--------------|---------|-------|-------------------------|-------------------------------------------------------------------------------|-----------------|
| 14 | PEAK         | U+E00D  | △    | `E013_PEAK.svg`         | `3ef24402411c077d5a32d1a6fe6ff624b28cc7518fcd12a62aa1dd1e373de176`           | ⟨STRUCTURE:PEAK \| TOPOLOGY:MAXIMA \| STABILITY:MARGINAL⟩ |
| 15 | VALLEY       | U+E00E  | ▽    | `E014_VALLEY.svg`       | `b1e52fd9c2e76f36af9517356e5066ea8e366e070bb347a44ba770e07e9a87ff`           | ⟨STRUCTURE:MINIMA \| TOPOLOGY:LOW POINT \| STABILITY:RELATIVE⟩ |
| 16 | PLATEAU      | U+E00F  | ▬    | `E015_PLATEAU.svg`      | `58a04ab60ee5be8b9bb163a21a162eb2f1d657883344fd3375457b1c6c985603`           | ⟨STRUCTURE:EXTENDED_MAXIMA \| TEMPORAL:DURATION \| CHANGE:STALLED⟩ |
| 18 | SUBDUCTION   | U+E011  | ⊂    | `E017_SUBDUCTION.svg`   | `342e2245cf1c274e2e0209351710f545dbc36d069848713d7d7ff861e7f44679`           | ⟨RELATION:UNDERLAP \| TOPOLOGY:ENCROACHING \| PRESSURE:LOCALIZED⟩ |
| 19 | CONVERGENCE  | U+E012  | ◬    | `E018_CONVERGENCE.svg`  | `aa022e9ee2a6fe4ecd6cb2da886d96ccfbc3dfdf25f09e8f11bedd1abc83bc3c`           | ⟨RELATION:MERGING \| FLOW:INWARD \| ALIGNMENT:INCREASING⟩ |
| 21 | GRADIENT     | U+E014  | ⟍⟋  | `E020_GRADIENT.svg`     | `afa1752b8d123238695816be6487ce6cc2edff6f4e9dc2a98b6bdbffc371b7a9`           | ⟨CHANGE:STEADY \| TOPOLOGY:SLOPED \| DIRECTION:MONOTONIC⟩ |
| 22 | FUSION       | U+E015  | ◬◉  | `E021_FUSION.svg`       | `5370c5ccdc9e1b825b82e7531c7e29f02a9b764b30435a3f74d4270a5960599f`           | ⟨RELATION:UNION \| BOUNDARY:PARTIAL \| IDENTITY:INTERPENETRATING⟩ |
| 23 | EMERGENCE    | U+E016  | ⊙    | `E022_EMERGENCE.svg`    | `debc0e06b23f72bafcdba6ef28389297cb68ee73a4373797a4b76992e540ecc4`           | ⟨RELATION:OUTWARD \| PATTERN:UNFOLDING \| COHERENCE:RISING⟩ |
| 24 | CONTAINMENT  | U+E017  | ⊚    | `E023_CONTAINMENT.svg`  | `66611133f421fdf497fdaac09ad87f13072ed530bd599eeff76d3c5ce757447d`           | ⟨BOUNDARY:ENCLOSING \| TENSION:HELD \| CONTENT:INTERNALIZED⟩ |

---

## Logic Glyphs

| #  | Name         | PUA     | Disp. | SVG File             | PSH-256 Canonical Hash                                                       | Semantic Vector |
|----|--------------|---------|-------|----------------------|-------------------------------------------------------------------------------|-----------------|
| 25 | VOID         | U+E018  | ∅    | `E024_VOID.svg`      | `3ee91958cc40ee86d69ef88bc75adbd62b0dd5b8515aa3ebabdd85687cb55c65`           | ⟨PRESENCE:NONE \| CONTENT:ABSENT \| POTENTIAL:LATENT⟩ |
| 26 | CONDITIONAL  | U+E019  | ☇    | `E025_CONDITIONAL.svg` | `b363e86556f47a5c1dc7fbbd27b966e263e97d25a47dc42493ef64a8365e77b2`         | ⟨LOGIC:IF-THEN \| STATE:BRANCHING \| DEPENDENCE:EXPLICIT⟩ |
| 27 | NEGATION     | U+E01A  | ¬    | `E026_NEGATION.svg`  | `39932a4dda5d67b78e9bc4e097d43fe7af037cf420cda97f31da15011db3d7b7`           | ⟨LOGIC:NOT \| STATE:INVERSION \| POLE:OPPOSITE⟩ |
| 28 | EQUIVALENCE  | U+E01B  | ≡    | `E027_EQUIVALENCE.svg` | `09693c55e510bf5b06ef6a230b06e43713ba858f2f0a5219f8db730aac7c33ad`         | ⟨LOGIC:IF-AND-ONLY-IF \| RELATION:BIDIRECTIONAL \| SYMMETRY:HIGH⟩ |

---

**Status:** All 28 glyphs are **HARDENED** under PSH-256 v1.0 (dihedral-invariant) and
form the complete canonical PICTOGRAM alphabet for v1.0.
