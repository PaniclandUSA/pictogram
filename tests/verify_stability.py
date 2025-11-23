import sys
import os
import cv2
import numpy as np
import logging

# Ensure we can import the local psh256 module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from psh256 import PictogramHasher

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("PSH-Test")

def generate_synthetic_glyph(style="canonical"):
    """
    Generates a 512x512 image of a 'Cyclic' glyph (Circle) 
    with various adversarial defects based on style.
    """
    img = np.zeros((512, 512), dtype=np.uint8)
    
    if style == "canonical":
        # Perfect center, standard thickness
        cv2.circle(img, (256, 256), 100, 255, 5)
        
    elif style == "hand_drawn_jitter":
        # Simulating shaky hand by drawing multiple offset ellipses
        cv2.ellipse(img, (256, 256), (100, 95), 0, 0, 360, 255, 4)
        cv2.ellipse(img, (258, 254), (102, 98), 5, 0, 360, 255, 4)
        
    elif style == "offset":
        # Drawn in top-left corner (should be fixed by Centroid Alignment)
        cv2.circle(img, (150, 150), 100, 255, 5)
        
    elif style == "bold_marker":
        # Very thick line (should be fixed by Skeletonization)
        cv2.circle(img, (256, 256), 100, 255, 25)
        
    elif style == "fine_pen":
        # Very thin line
        cv2.circle(img, (256, 256), 100, 255, 1)

    return img

def run_stability_test():
    hasher = PictogramHasher()
    
    print("="*60)
    print("PSH-256 ADVERSARIAL STABILITY TEST")
    print("Target: Prove Topology Hash Invariance under Distortion")
    print("="*60)

    # 1. Generate Canonical Baseline
    canonical_img = generate_synthetic_glyph("canonical")
    cv2.imwrite("test_canonical.png", canonical_img)
    
    canonical_hash = hasher.compute_psh256("test_canonical.png", "CYCLIC")
    target_topology = canonical_hash.topology_hash
    
    print(f"[BASELINE] Canonical Glyph generated.")
    print(f"Target Topology Hash: {target_topology}")
    print("-" * 60)

    # 2. Run Adversarial Cases
    test_cases = ["hand_drawn_jitter", "offset", "bold_marker", "fine_pen"]
    passed = 0
    
    for case in test_cases:
        # Generate and Save
        filename = f"test_{case}.png"
        img = generate_synthetic_glyph(case)
        cv2.imwrite(filename, img)
        
        # Compute Hash
        result = hasher.compute_psh256(filename, "CYCLIC")
        
        # Verify
        if result.topology_hash == target_topology:
            status = "✅ PASS"
            passed += 1
        else:
            status = "❌ FAIL"
            
        print(f"[{case.ljust(18)}] {status} | Hash: {result.topology_hash}")
        
        # Cleanup
        os.remove(filename)
    
    os.remove("test_canonical.png")
    
    print("-" * 60)
    if passed == len(test_cases):
        print("🏆 CERTIFICATION SUCCESS: PSH-256 is Topologically Stable.")
    else:
        print("⚠️  CERTIFICATION FAILED: Normalization pipeline needs tuning.")

if __name__ == "__main__":
    run_stability_test()
