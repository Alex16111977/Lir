"""
Test for exercises_assets refactoring
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    # Test 1: Import from wrapper
    from src.generators.exercises_assets import ExercisesAssetsGenerator
    print("[OK] Import from exercises_assets.py works")
    
    # Test 2: Import from modules
    from src.generators.exercises_assets_modules import ExercisesAssetsGenerator as ModularGen
    print("[OK] Import from modules works")
    
    # Test 3: Create instance
    gen = ExercisesAssetsGenerator()
    print(f"[OK] Generator created: {type(gen).__name__}")
    
    # Test 4: Generate CSS
    css = gen.generate_css()
    css_lines = len(css.splitlines())
    print(f"[OK] CSS generated: {css_lines} lines")
    
    # Test 5: Generate JS
    js = gen.generate_js()
    js_lines = len(js.splitlines())
    print(f"[OK] JS generated: {js_lines} lines")
    
    # Summary
    print("\n[SUCCESS] All tests passed!")
    print(f"- CSS lines: {css_lines}")
    print(f"- JS lines: {js_lines}")
    print(f"- Total methods available: {len([m for m in dir(gen) if not m.startswith('_')])}")
    
except Exception as e:
    print(f"[ERROR] Test failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
