# Contributing to PICTOGRAM

Thank you for your interest in contributing to PICTOGRAM! This document provides guidelines for contributing to the project.

## Code of Conduct

PICTOGRAM emerged from collaborative AI convergence and maintains that spirit:

- **Respect all contributors** regardless of background or affiliation
- **Value precision over opinion** - claims should be testable
- **Prioritize clarity** - documentation matters as much as code
- **Embrace constructive criticism** - adversarial testing makes protocols stronger
- **Credit appropriately** - acknowledge prior work and inspiration

## Ways to Contribute

### 1. Bug Reports

Found a PSH-256 collision? Glyph rendering issue? Let us know:

- **Search existing issues** first to avoid duplicates
- **Include minimal reproduction** - exact steps to reproduce
- **Specify environment**: OS, Python version, OpenCV version
- **Attach test files** if relevant (SVG glyphs, test images)

### 2. Feature Proposals

Have an idea for PICTOGRAM? We'd love to hear it:

- **Explain the problem** you're trying to solve
- **Describe proposed solution** with concrete examples
- **Consider backward compatibility** - v1.0 glyphs are frozen
- **Discussion before PR** - open an issue first

### 3. Documentation Improvements

Documentation is crucial for adoption:

- **Fix typos and clarity issues** - no PR too small
- **Add usage examples** - show real-world applications
- **Translate documentation** - PICTOGRAM is universal, docs should be too
- **Expand tutorials** - help newcomers understand the protocol

### 4. Code Contributions

#### Setting Up Development Environment
```bash
git clone https://github.com/PaniclandUSA/pictogram.git
cd pictogram
pip install -r reference/requirements.txt

# Run tests
python -m pytest tests/  # (once test suite exists)
```

#### Code Style

- **Python**: Follow PEP 8 conventions
- **Comments**: Explain *why*, not *what*
- **Type hints**: Use where beneficial (Python 3.7+)
- **Docstrings**: Include for all public functions

#### Pull Request Process

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/your-feature-name`
3. **Make changes** with clear commit messages
4. **Test thoroughly** - ensure PSH-256 stability tests pass
5. **Update documentation** if changing behavior
6. **Submit PR** with description of changes

### 5. Language Bindings

PICTOGRAM currently has Python reference implementation. Bindings needed:

- **JavaScript/TypeScript** (browser usage)
- **Rust** (performance-critical applications)
- **Go** (server-side processing)
- **Swift** (iOS integration)

**Requirements for language bindings:**
- Must pass PSH-256 stability test suite
- Must produce identical hashes to Python reference
- Should maintain similar API design

### 6. Glyph Proposals (Extended Set)

**v1.0 canonical 28 glyphs are frozen** - these will never change.

For **extended glyph sets** (U+E01C onward):

1. **Demonstrate clear need** - what semantic gap does it fill?
2. **Follow design principles**:
   - Culturally neutral archetypal form
   - Topologically stable (PSH-256 robust)
   - Visually distinct from existing glyphs
   - Compositionally coherent with v1.0 glyphs
3. **Provide SVG implementation** following canonical format
4. **Include semantic vector** using VSE notation
5. **Get multi-model validation** (test with multiple AI systems)

## Testing Requirements

All contributions must maintain PSH-256 stability:

### Core Stability Test
```python
def test_d4_invariance(glyph_svg):
    """Verify PSH-256 is invariant under D4 group transformations."""
    hasher = PSH256()
    original_hash = hasher.hash_file(glyph_svg)
    
    # Test all 8 D4 transformations
    for transform in [rotate_90, rotate_180, rotate_270, 
                      flip_h, flip_v, flip_d1, flip_d2]:
        transformed = transform(glyph_svg)
        assert hasher.hash_file(transformed) == original_hash
```

### Regression Testing

New features must not break existing functionality:
- All 28 canonical glyphs maintain their PSH-256 hashes
- Composition grammar remains compatible
- Documentation examples continue to work

## Documentation Standards

### Glyph Documentation

Each glyph entry must include:
```json
{
  "id": "GLYPH_##_NAME",
  "name": "NAME",
  "category": "flow|pressure|texture|structure|operator|logic",
  "pua_codepoint": "U+E0XX",
  "unicode_display": "⟲",
  "semantic_vector": "⟨ATTR:VALUE | ATTR:VALUE⟩",
  "description": "Clear natural language explanation",
  "design_notes": ["Why this form?", "What does it evoke?"],
  "symbolic_associations": ["archetype1", "archetype2"],
  "usage_examples": ["composition1", "composition2"]
}
```

### Code Documentation

Functions processing glyphs should document:

- **Input format**: SVG path, image array, etc.
- **Output format**: Hash string, processed image, etc.
- **Stability guarantees**: What transformations are safe?
- **Edge cases**: What breaks the algorithm?

## Review Process

1. **Automated checks** (when CI is set up):
   - Code formatting (black, flake8)
   - PSH-256 stability tests
   - Documentation build

2. **Maintainer review**:
   - Code quality and clarity
   - Test coverage
   - Documentation completeness
   - Backward compatibility

3. **Multi-AI validation** (for glyph changes):
   - Test with Claude, GPT-4, Gemini, etc.
   - Verify consistent interpretation
   - Check for cultural bias

## Questions?

- **General discussion**: [GitHub Discussions](https://github.com/PaniclandUSA/pictogram/discussions)
- **Bug reports**: [GitHub Issues](https://github.com/PaniclandUSA/pictogram/issues)
- **Security concerns**: Email maintainers directly (see README)

## License

By contributing, you agree that:
- **Code contributions** are licensed under MIT
- **Glyph and documentation contributions** are licensed under CC BY-SA 4.0

---

*"The best protocols emerge from collaborative convergence."*

Thank you for helping build universal semantic infrastructure! 🌟
