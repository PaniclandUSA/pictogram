# Hello World — PICTOGRAM

PICTOGRAM is the **visual compression layer** of the Esper-Stack.

It renders a semantic-temporal payload into a **glyph surrogate** representing its compressed meaning.

---

# 1. Basic Example

```python
from pictogram import Compositor

crystal = {
    "stage": "chronocore",
    "timeline": ["t0: stabilize", "t1: emit"],
    "source": {
        "payload": {"intent": {"axis": "hello"}}
    }
}
```
glyph = Compositor().render(crystal)
print(glyph)

Expected output:

{'stage': 'pictogram', 'glyph': '[HELLO-Glyph]', ...}


---

2. Understanding PICTOGRAM

The true PICTOGRAM engine includes:

glyph families

modifier stacks

rule-of-three layering

PSH-256 extension rules

axis→glyph projection logic


The stub currently provides:

uppercase axis → placeholder glyph

consistent structure for real rendering engines

safe fallback behavior



---

3. Future Versions Will Add

SVG/Canvas export

16 modifier families

dynamic transforms

semantic+visual coexistence

visual convergence tests



---

4. Exercise

Try changing the axis:

intent_axis = "unify"

You’ll get:

'[UNIFY-Glyph]'
