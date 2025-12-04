#!/usr/bin/env python3
"""
PICTOGRAM Master Glyph Sheet Generator
Creates a visual grid of all 28 canonical glyphs with labels
"""

import os
from pathlib import Path
import cairosvg
from PIL import Image, ImageDraw, ImageFont
import io

# Configuration
GLYPH_DIR = Path("../glyphs/canonical")
OUTPUT_FILE = Path("../glyphs/GLYPH_SHEET.png")
GRID_COLS = 7
GRID_ROWS = 4
CELL_SIZE = 200
PADDING = 20
LABEL_HEIGHT = 40
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
GRID_COLOR = (220, 220, 220)

# Glyph order (by category)
GLYPH_ORDER = [
    # Flow (5)
    "E000_CYCLIC", "E001_ERUPTIVE", "E002_STAGNANT", "E003_TURBULENT", "E004_DISSIPATIVE",
    # Pressure (4)
    "E005_LOW_PRESSURE", "E006_RISING_PRESSURE", "E007_HIGH_PRESSURE", "E008_COLLAPSING_PRESSURE",
    # Texture (4)
    "E009_CRYSTALLINE", "E00A_ORGANIC", "E00B_MINIMAL", "E00C_DIFFUSE",
    # Structure (5)
    "E00D_PEAK", "E00E_VALLEY", "E00F_PLATEAU", "E010_ASCENT", "E011_SUBDUCTION",
    # Operators (6)
    "E012_CONVERGENCE", "E013_OSCILLATION", "E014_GRADIENT", "E015_FUSION", "E016_EMERGENCE", "E017_CONTAINMENT",
    # Logic (4)
    "E018_VOID", "E019_CONDITIONAL", "E01A_NEGATION", "E01B_EQUIVALENCE"
]

def svg_to_png(svg_path, size=150):
    """Convert SVG to PNG with transparent background"""
    png_data = cairosvg.svg2png(
        url=str(svg_path),
        output_width=size,
        output_height=size
    )
    return Image.open(io.BytesIO(png_data))

def create_glyph_sheet():
    """Generate master glyph sheet"""
    
    # Calculate canvas size
    canvas_width = GRID_COLS * CELL_SIZE
    canvas_height = GRID_ROWS * (CELL_SIZE + LABEL_HEIGHT) + 100  # Extra space for title
    
    # Create canvas
    canvas = Image.new('RGB', (canvas_width, canvas_height), BG_COLOR)
    draw = ImageDraw.Draw(canvas)
    
    # Try to load a nice font, fall back to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        code_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 11)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        code_font = ImageFont.load_default()
    
    # Draw title
    title = "PICTOGRAM v1.0 - Universal Visual Semantic Protocol"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (canvas_width - title_width) // 2
    draw.text((title_x, 30), title, fill=TEXT_COLOR, font=title_font)
    
    # Starting Y position after title
    start_y = 100
    
    # Draw glyphs
    for idx, glyph_name in enumerate(GLYPH_ORDER):
        row = idx // GRID_COLS
        col = idx % GRID_COLS
        
        # Calculate cell position
        cell_x = col * CELL_SIZE
        cell_y = start_y + row * (CELL_SIZE + LABEL_HEIGHT)
        
        # Draw cell border
        draw.rectangle(
            [cell_x, cell_y, cell_x + CELL_SIZE, cell_y + CELL_SIZE + LABEL_HEIGHT],
            outline=GRID_COLOR,
            width=1
        )
        
        # Load and draw glyph
        svg_path = GLYPH_DIR / f"{glyph_name}.svg"
        if svg_path.exists():
            try:
                glyph_img = svg_to_png(svg_path, size=CELL_SIZE - PADDING * 2)
                
                # Center glyph in cell
                glyph_x = cell_x + (CELL_SIZE - glyph_img.width) // 2
                glyph_y = cell_y + (CELL_SIZE - LABEL_HEIGHT - glyph_img.height) // 2
                
                # Paste with alpha channel
                if glyph_img.mode == 'RGBA':
                    canvas.paste(glyph_img, (glyph_x, glyph_y), glyph_img)
                else:
                    canvas.paste(glyph_img, (glyph_x, glyph_y))
            except Exception as e:
                print(f"Warning: Could not render {glyph_name}: {e}")
        
        # Draw label (name and code)
        name_display = glyph_name.split('_', 1)[1].replace('_', ' ')
        code_display = glyph_name.split('_')[0]
        
        # Center text in label area
        name_bbox = draw.textbbox((0, 0), name_display, font=label_font)
        name_width = name_bbox[2] - name_bbox[0]
        name_x = cell_x + (CELL_SIZE - name_width) // 2
        name_y = cell_y + CELL_SIZE - LABEL_HEIGHT + 5
        
        code_bbox = draw.textbbox((0, 0), f"U+{code_display}", font=code_font)
        code_width = code_bbox[2] - code_bbox[0]
        code_x = cell_x + (CELL_SIZE - code_width) // 2
        code_y = name_y + 18
        
        draw.text((name_x, name_y), name_display, fill=TEXT_COLOR, font=label_font)
        draw.text((code_x, code_y), f"U+{code_display}", fill=(100, 100, 100), font=code_font)
    
    # Add footer
    footer_y = canvas_height - 40
    footer_text = "28 Canonical Glyphs | PSH-256 Cryptographic Hashing | github.com/PaniclandUSA/pictogram"
    footer_bbox = draw.textbbox((0, 0), footer_text, font=code_font)
    footer_width = footer_bbox[2] - footer_bbox[0]
    footer_x = (canvas_width - footer_width) // 2
    draw.text((footer_x, footer_y), footer_text, fill=(120, 120, 120), font=code_font)
    
    # Save
    canvas.save(OUTPUT_FILE, 'PNG', optimize=True)
    print(f"✅ Master glyph sheet saved to: {OUTPUT_FILE}")
    print(f"   Dimensions: {canvas_width}x{canvas_height}px")
    print(f"   File size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    create_glyph_sheet()
