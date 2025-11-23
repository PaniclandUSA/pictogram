# PSH-256 v1.0 Reference Implementation

code_content = """#!/usr/bin/env python3
\"\"\"
PSH-256 v1.0 Reference Implementation
Pictographic Semantic Hash - 256 bit

This is the PSH-256 v1.0 reference implementation, hardened based on adversarial analysis (Grok) and formalized by Gemini.

v1.0 HARDENING FEATURES:
1. Dihedral Normalization: Hash is invariant under D4 symmetry group (rotation/reflection).
2. PUA Mapping: Annexed Unicode Private Use Area (U+E000–E01F) to prevent semantic collision.
3. Square-Pad-Resize: Aspect-ratio preserving normalization protocol.
\"\"\"

import cv2
import numpy as np
import hashlib
import logging
from typing import Tuple, List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =============================================================================
# ENUMS AND CONSTANTS
# =============================================================================

class GlyphCategory(Enum):
    FLOW = "flow"
    PRESSURE = "pressure"
    TEXTURE = "texture"
    STRUCTURE = "structure"
    OPERATOR = "operator"
    LOGIC = "logic"

@dataclass
class GlyphDefinition:
    fingerprint: str
    category: GlyphCategory
    pua_codepoint: str  # v1.0: PUA Code
    unicode_symbol: str # Legacy/Display symbol
    semantic_vector: str
    description: str
    line_weight: str

# v1.0 REGISTRY: Mapped to Private Use Area (E000-E01F)
GLYPH_REGISTRY: Dict[str, GlyphDefinition] = {
    # Flow Glyphs
    'CYCLIC': GlyphDefinition('GLYPH_01_CYCLIC', GlyphCategory.FLOW, '\\uE000', '⟲', '⟨TEMPORAL:RECURSIVE|PATTERN:PERIODIC⟩', 'Circular arrow forming complete loop', 'fine'),
    'ERUPTIVE': GlyphDefinition('GLYPH_02_ERUPTIVE', GlyphCategory.FLOW, '\\uE001', '⤊', '⟨TEMPORAL:SUDDEN|INTENSITY:MAXIMUM⟩', 'Upward explosion', 'fine'),
    'STAGNANT': GlyphDefinition('GLYPH_03_STAGNANT', GlyphCategory.FLOW, '\\uE002', '▭', '⟨TEMPORAL:STATIC|MOMENTUM:ZERO⟩', 'Horizontal bar', 'fine'),
    'TURBULENT': GlyphDefinition('GLYPH_04_TURBULENT', GlyphCategory.FLOW, '\\uE003', '⤨', '⟨TEMPORAL:IRREGULAR|PATTERN:CHAOTIC⟩', 'Chaotic zigzag', 'fine'),
    'DISSIPATIVE': GlyphDefinition('GLYPH_05_DISSIPATIVE', GlyphCategory.FLOW, '\\uE004', '⤋', '⟨TEMPORAL:GRADUAL|INTENSITY:DECREASING⟩', 'Downward fade', 'fine'),

    # Pressure Glyphs
    'LOW_PRESSURE': GlyphDefinition('GLYPH_06_LOW_PRESSURE', GlyphCategory.PRESSURE, '\\uE005', '◯', '⟨TENSION:MINIMAL|SPACE:EXPANSIVE⟩', 'Open circle', 'bold'),
    'RISING_PRESSURE': GlyphDefinition('GLYPH_07_RISING_PRESSURE', GlyphCategory.PRESSURE, '\\uE006', '◓', '⟨TENSION:INCREASING|TRAJECTORY:UPWARD⟩', 'Half-filled circle', 'medium'),
    'HIGH_PRESSURE': GlyphDefinition('GLYPH_08_HIGH_PRESSURE', GlyphCategory.PRESSURE, '\\uE007', '●', '⟨TENSION:MAXIMUM|DENSITY:MAXIMAL⟩', 'Solid filled circle', 'bold'),
    'COLLAPSING_PRESSURE': GlyphDefinition('GLYPH_09_COLLAPSING_PRESSURE', GlyphCategory.PRESSURE, '\\uE008', '◉', '⟨TENSION:RELEASING|DIRECTION:INWARD⟩', 'Concentric circles imploding', 'bold'),

    # Texture Glyphs
    'CRYSTALLINE': GlyphDefinition('GLYPH_10_CRYSTALLINE', GlyphCategory.TEXTURE, '\\uE009', '◇', '⟨STRUCTURE:GEOMETRIC|CLARITY:HIGH⟩', 'Geometric diamond', 'fine'),
    'ORGANIC': GlyphDefinition('GLYPH_11_ORGANIC', GlyphCategory.TEXTURE, '\\uE00A', '∿', '⟨STRUCTURE:IRREGULAR|NATURALNESS:HIGH⟩', 'Irregular wave', 'fine'),
    'MINIMAL': GlyphDefinition('GLYPH_12_MINIMAL', GlyphCategory.TEXTURE, '\\uE00B', '·', '⟨DENSITY:SPARSE|ELEMENTS:FEW⟩', 'Single point', 'fine'),
    'DIFFUSE': GlyphDefinition('GLYPH_13_DIFFUSE', GlyphCategory.TEXTURE, '\\uE00C', '⁘', '⟨BOUNDARY:UNCLEAR|DISTRIBUTION:SCATTERED⟩', 'Scattered dots', 'fine'),

    # Structure Glyphs
    'PEAK': GlyphDefinition('GLYPH_14_PEAK', GlyphCategory.STRUCTURE, '\\uE00D', '△', '⟨POSITION:MAXIMUM|PROMINENCE:HIGH⟩', 'Triangle pointing upward', 'medium'),
    'VALLEY': GlyphDefinition('GLYPH_15_VALLEY', GlyphCategory.STRUCTURE, '\\uE00E', '▽', '⟨POSITION:MINIMUM|DEPTH:MAXIMAL⟩', 'Triangle pointing downward', 'medium'),
    'PLATEAU': GlyphDefinition('GLYPH_16_PLATEAU', GlyphCategory.STRUCTURE, '\\uE00F', '▬', '⟨POSITION:ELEVATED|DURATION:EXTENDED⟩', 'Elevated horizontal line', 'medium'),
    'ASCENT': GlyphDefinition('GLYPH_17_ASCENT', GlyphCategory.STRUCTURE, '\\uE010', '⟋', '⟨DIRECTION:UPWARD|GRADIENT:POSITIVE⟩', 'Rising diagonal', 'medium'),
    'SUBDUCTION': GlyphDefinition('GLYPH_18_SUBDUCTION', GlyphCategory.STRUCTURE, '\\uE011', '⊂', '⟨RELATION:BENEATH|INTERACTION:FOUNDATIONAL⟩', 'Curve sliding beneath', 'medium'),

    # Operators
    'CONVERGENCE': GlyphDefinition('GLYPH_19_CONVERGENCE', GlyphCategory.OPERATOR, '\\uE012', '⊢⊣', '⟨INTERACTION:COLLISION|RESULT:FUSION⟩', 'Forms meeting', 'medium'),
    'OSCILLATION': GlyphDefinition('GLYPH_20_OSCILLATION', GlyphCategory.OPERATOR, '\\uE013', '⟷', '⟨PATTERN:ALTERNATING|STABILITY:DYNAMIC⟩', 'Double-headed arrow', 'medium'),
    'GRADIENT': GlyphDefinition('GLYPH_21_GRADIENT', GlyphCategory.OPERATOR, '\\uE014', '→', '⟨TRANSFORMATION:CONTINUOUS|DIRECTION:UNIDIRECTIONAL⟩', 'Directional arrow', 'medium'),
    'FUSION': GlyphDefinition('GLYPH_22_FUSION', GlyphCategory.OPERATOR, '\\uE015', '◬', '⟨INTEGRATION:COMPLETE|IDENTITY:HYBRID⟩', 'Overlapping circles', 'medium'),
    'EMERGENCE': GlyphDefinition('GLYPH_23_EMERGENCE', GlyphCategory.OPERATOR, '\\uE016', '⊙', '⟨CAUSALITY:GENERATIVE|NOVELTY:HIGH⟩', 'Dot with radiating circle', 'medium'),
    'CONTAINMENT': GlyphDefinition('GLYPH_24_CONTAINMENT', GlyphCategory.OPERATOR, '\\uE017', '⊚', '⟨RELATION:NESTED|BOUNDARY:CLEAR⟩', 'Concentric circles', 'bold'),

    # Logic
    'VOID': GlyphDefinition('GLYPH_25_VOID', GlyphCategory.LOGIC, '\\uE018', '∅', '⟨DATA:MISSING|STATE:UNDEFINED⟩', 'Empty set symbol', 'bold'),
    'CONDITIONAL': GlyphDefinition('GLYPH_26_CONDITIONAL', GlyphCategory.LOGIC, '\\uE019', '☇', '⟨LOGIC:CONDITIONAL|DECISION:REQUIRED⟩', 'Lightning bolt', 'bold'),
    'NEGATION': GlyphDefinition('GLYPH_27_NEGATION', GlyphCategory.LOGIC, '\\uE01A', '¬', '⟨LOGIC:INVERSION|POLARITY:NEGATIVE⟩', 'Negation symbol', 'bold'),
    'EQUIVALENCE': GlyphDefinition('GLYPH_28_EQUIVALENCE', GlyphCategory.LOGIC, '\\uE01B', '≡', '⟨RELATION:IDENTITY|COMPARISON:EQUAL⟩', 'Equivalence symbol', 'bold'),
}


@dataclass
class PictogramHash:
    psh256: str
    topology_hash: str
    spatial_code: str
    semantic_fingerprint: str
    chain_code: str
    glyph_name: str
    orientation_id: int  # Which of the 8 D4 orientations was canonical

# =============================================================================
# PROCESSING PIPELINE
# =============================================================================

class ImagePreprocessor:
    \"\"\"
    v1.0 Hardened Preprocessing
    Implements Square-Pad-Resize protocol for aspect ratio stability.
    \"\"\"
    
    def __init__(self, grid_size: int = 64):
        self.grid_size = grid_size
        
    def process(self, image_path: str) -> np.ndarray:
        # 1. Load
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError(f"Could not load image: {image_path}")
            
        # 2. Blur & Binarize (Noise Reduction)
        k = int(min(img.shape) * 0.02) | 1
        blurred = cv2.GaussianBlur(img, (k, k), 0)
        _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        # 3. Square-Pad-Resize (Aspect Ratio Stability)
        normalized = self._square_pad_resize(binary)
        
        # 4. Skeletonize (Stroke Width Independence)
        skeleton = self._skeletonize(normalized)
        
        return skeleton

    def _square_pad_resize(self, binary: np.ndarray) -> np.ndarray:
        \"\"\"
        Implements v1.0 Square-Pad protocol:
        1. Find tight bounding box
        2. Pad to square (centering content)
        3. Add safe zone (10%)
        4. Resize to 64x64
        \"\"\"
        # Find bounding box
        coords = cv2.findNonZero(binary)
        if coords is None:
            return np.zeros((self.grid_size, self.grid_size), dtype=np.uint8)
            
        x, y, w, h = cv2.boundingRect(coords)
        crop = binary[y:y+h, x:x+w]
        
        # Determine square dimension
        dim = max(w, h)
        
        # Create square canvas with content centered
        square = np.zeros((dim, dim), dtype=np.uint8)
        x_offset = (dim - w) // 2
        y_offset = (dim - h) // 2
        square[y_offset:y_offset+h, x_offset:x_offset+w] = crop
        
        # Add 10% Safe Zone padding
        padding = int(dim * 0.10)
        padded_dim = dim + 2 * padding
        final_canvas = np.zeros((padded_dim, padded_dim), dtype=np.uint8)
        final_canvas[padding:padding+dim, padding:padding+dim] = square
        
        # Final canonical resize
        return cv2.resize(final_canvas, (self.grid_size, self.grid_size), interpolation=cv2.INTER_NEAREST)

    def _skeletonize(self, img: np.ndarray) -> np.ndarray:
        skeleton = np.zeros(img.shape, np.uint8)
        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        temp_img = img.copy()
        
        while cv2.countNonZero(temp_img) > 0:
            eroded = cv2.erode(temp_img, element)
            temp = cv2.dilate(eroded, element)
            temp = cv2.subtract(temp_img, temp)
            skeleton = cv2.bitwise_or(skeleton, temp)
            temp_img = eroded.copy()
            
        return skeleton

# =============================================================================
# TOPOLOGY ENGINE (DIHEDRAL D4)
# =============================================================================

class DihedralCanonicalizer:
    \"\"\"
    v1.0 Hardened Topology Extractor
    Implements Dihedral Normalization (D4 Group Invariance).
    Generates 8 orientation variants and selects lexicographically minimal chain code.
    \"\"\"
    
    def __init__(self, grid_size: int = 64):
        self.grid_size = grid_size
        
    def get_canonical_topology(self, skeleton: np.ndarray) -> Tuple[str, int]:
        \"\"\"
        Returns (canonical_chain_code, orientation_id)
        orientation_id maps to: 0=0deg, 1=90deg, 2=180deg, 3=270deg, 
                              4=Flip0, 5=Flip90, 6=Flip180, 7=Flip270
        \"\"\"
        candidates = []
        
        # Generate all 8 symmetries
        # 0-3: Rotations
        for k in range(4):
            rotated = np.rot90(skeleton, k)
            code = self._extract_chain(rotated)
            candidates.append((code, k))
            
        # 4-7: Reflections + Rotations
        flipped_base = cv2.flip(skeleton, 1) # Flip around y-axis
        for k in range(4):
            rotated = np.rot90(flipped_base, k)
            code = self._extract_chain(rotated)
            candidates.append((code, k + 4))
            
        # Select canonical (lexicographically smallest)
        # This ensures 'upside down' glyphs hash to the same value as 'right side up'
        candidates.sort(key=lambda x: x[0])
        return candidates[0]
    
    def _extract_chain(self, img: np.ndarray) -> str:
        \"\"\"Standard Freeman Chain Code Extraction\"\"\"
        coords = np.column_stack(np.where(img > 0))
        if len(coords) == 0: return "0"
        
        # Canonical start: Top-most, then Left-most
        coords = coords[np.lexsort((coords[:, 1], coords[:, 0]))]
        sy, sx = coords[0]
        
        visited = set()
        stack = [(sy, sx)]
        chain = []
        
        # Freeman directions: E, SE, S, SW, W, NW, N, NE
        moves = [(0,1,'0'), (1,1,'1'), (1,0,'2'), (1,-1,'3'), 
                 (0,-1,'4'), (-1,-1,'5'), (-1,0,'6'), (-1,1,'7')]
        
        while stack:
            cy, cx = stack.pop()
            if (cy, cx) in visited: continue
            visited.add((cy, cx))
            
            for dy, dx, c in moves:
                ny, nx = cy+dy, cx+dx
                if 0<=ny<self.grid_size and 0<=nx<self.grid_size:
                    if img[ny, nx] > 0 and (ny, nx) not in visited:
                        chain.append(c)
                        stack.append((ny, nx))
                        break # DFS
        
        return "".join(chain)

# =============================================================================
# MAIN HASHER
# =============================================================================

class PictogramHasher:
    def __init__(self):
        self.preprocessor = ImagePreprocessor()
        self.canonicalizer = DihedralCanonicalizer()
        
    def compute_psh256(self, image_path: str, glyph_name: str, spatial_code="0000") -> PictogramHash:
        # 1. Hardened Preprocessing
        skeleton = self.preprocessor.process(image_path)
        
        # 2. Dihedral Canonicalization
        chain_code, orientation = self.canonicalizer.get_canonical_topology(skeleton)
        topology_hash = hashlib.sha256(chain_code.encode()).hexdigest()
        
        # 3. Semantic ID (PUA-aware)
        if glyph_name in GLYPH_REGISTRY:
            # v1.0: Use PUA fingerprint if available, or registry ID
            semantic_id = GLYPH_REGISTRY[glyph_name].fingerprint
        else:
            semantic_id = f"UNKNOWN_{glyph_name}"
            
        # 4. Final Composite Hash
        composite = f"{topology_hash}:{spatial_code}:{semantic_id}"
        psh256 = hashlib.sha256(composite.encode()).hexdigest()
        
        return PictogramHash(psh256, topology_hash, spatial_code, semantic_id, chain_code, glyph_name, orientation)

# =============================================================================
# USAGE DEMO
# =============================================================================

if __name__ == "__main__":
    print("Initializing PSH-256 v1.0 Reference Implementation...")
    print(f"Loaded {len(GLYPH_REGISTRY)} glyph definitions from PUA block E000-E01F.")
    
    # Example logic
    hasher = PictogramHasher()
    # In a real run, you would provide a path:
    # h = hasher.compute_psh256("path/to/glyph.png", "CYCLIC")
    # print(f"PSH-256: {h.psh256}")
    # print(f"Canonical Orientation: {h.orientation_id}")
"""

with open('psh256_v1_0.py', 'w') as f:
    f.write(code_content)
