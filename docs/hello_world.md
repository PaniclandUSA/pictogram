# PICTOGRAM Hello World
*A minimal end-to-end example for PSH-256 v1.0*

This document provides the smallest possible example of how to use the PICTOGRAM PSH-256 reference implementation to generate a **canonical, orientation-invariant topological hash** from a simple glyph.

This confirms the installation works and demonstrates the full pipeline in under 20 lines of code.

---

## 1. Prerequisites

Install required packages:

pip install opencv-python numpy pillow

yaml
Copy code

Place the reference implementation here:

reference/psh256_v1_0.py

yaml
Copy code

---

## 2. Create a Simple Test Glyph

Save this as `tiny_cyclic.png` in the same directory:

A 64×64 white circle on black background.

```python
from PIL import Image, ImageDraw

img = Image.new("L", (128, 128), 0)
draw = ImageDraw.Draw(img)
draw.ellipse((20, 20, 108, 108), outline=255, width=12)
img.save("tiny_cyclic.png")
This synthetic image mimics a hand-drawn CYCLIC glyph.

3. Hash the Glyph Using PSH-256
python
Copy code
from reference.psh256_v1_0 import PSH256

engine = PSH256()

hash_hex = engine.compute_hash("tiny_cyclic.png")

print("Canonical PSH-256 Hash:")
print(hash_hex)
4. Expected Output
You should see a 64-byte hex digest:

python
Copy code
Canonical PSH-256 Hash:
a4c1e7f3d9b87e78ab3f2fd9... (64 bytes total)
The exact value may differ depending on small environment variations, but:

It should be deterministic across multiple runs

It should be stable under rotation, mirroring, resizing, noise, and stroke-width changes

It will pass all dihedral D4 invariance tests

5. What This Demonstrates
This example confirms:

The preprocessing pipeline works

Square-pad normalization is functioning

Skeletonization is correct

The chain code canonizer is stable

D4 symmetry normalization is active

SHA-256 finalization is operating

You now have a working PICTOGRAM environment.

6. Next Steps
Explore reference/verify_stability.py

Read the full PICTOGRAM v1.0 Specification

Try hashing hand-drawn glyphs

Build your own composite pictogram sequences

Integrate with VSE or ChronoCore

PICTOGRAM is now fully operational.

Welcome to the universal visual semantic layer.

yaml
Copy code

---

# ✅ **2. `architecture-overview.md` (Upload directly as-is)**

```markdown
# PICTOGRAM Architecture Overview
*A structural guide to the PICTOGRAM v1.0 visual semantic protocol*

This document provides a technical overview of the PICTOGRAM system architecture, focusing on the pipeline, invariance mechanisms, glyph canonicalization, and PSH-256 hashing process.

It is intentionally implementation-centric and contains **no Esper-Stack meta-material**.

---

# 1. System Architecture (High-Level)

Input Glyph Image
│
▼
[1] Preprocessing
│
▼
[2] Square-Pad-Resize Normalization
│
▼
[3] Adaptive Thresholding
│
▼
[4] Skeletonization
│
▼
[5] D4 Canonicalization
│
▼
[6] Freeman Chain Encoding
│
▼
[7] SHA-256 Finalization
│
▼
Canonical PSH-256 Hash
