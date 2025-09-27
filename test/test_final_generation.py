"""
Final test - check if site generation still works
"""
import subprocess
import sys
from pathlib import Path

print("=" * 60)
print("FINAL GENERATION TEST")
print("=" * 60)

# Run main.py
result = subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\main.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)

if result.returncode == 0:
    print("[OK] main.py executed successfully")
    
    # Check generated files
    output_dir = Path(r'F:\AiKlientBank\Lir\output')
    if output_dir.exists():
        html_files = list(output_dir.glob('**/*.html'))
        css_files = list(output_dir.glob('**/*.css'))
        js_files = list(output_dir.glob('**/*.js'))
        
        print(f"\n[RESULTS]")
        print(f"  HTML files: {len(html_files)}")
        print(f"  CSS files:  {len(css_files)}")
        print(f"  JS files:   {len(js_files)}")
        print(f"  TOTAL:      {len(html_files) + len(css_files) + len(js_files)}")
        
        if len(html_files) >= 55:
            print("\n[SUCCESS] Site generation works perfectly!")
        else:
            print(f"\n[WARNING] Expected 55+ HTML files, got {len(html_files)}")
    else:
        print("[ERROR] Output directory not found")
else:
    print(f"[ERROR] main.py failed")
    print(result.stderr[:500])
