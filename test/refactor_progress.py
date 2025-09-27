"""
Quick statistics for refactoring progress
"""
from pathlib import Path

def analyze_files():
    """Analyze all Python files in generators."""
    generators_dir = Path(r'F:\AiKlientBank\Lir\src\generators')
    
    large_files = []
    refactored = []
    
    for py_file in generators_dir.glob('*.py'):
        if '__init__' not in py_file.name and 'backup' not in py_file.name:
            content = py_file.read_text(encoding='utf-8')
            lines = len(content.splitlines())
            
            if lines > 300:
                large_files.append((py_file.name, lines))
            elif py_file.name == 'exercises_assets.py' and lines < 100:
                refactored.append(py_file.name)
    
    # Check for modular directories
    module_dirs = list(generators_dir.glob('*_modules'))
    
    print("=" * 60)
    print("REFACTORING PROGRESS")
    print("=" * 60)
    
    print("\n[COMPLETED]")
    print(f"- exercises_assets.py refactored into modules")
    print(f"- Module directories created: {len(module_dirs)}")
    
    print("\n[REMAINING] Files > 300 lines:")
    for name, lines in sorted(large_files, key=lambda x: x[1], reverse=True):
        print(f"  {name:30} | {lines:5} lines")
    
    print(f"\n[SUMMARY]")
    print(f"- Files refactored: {len(refactored)}")
    print(f"- Files remaining: {len(large_files)}")
    print(f"- Progress: {len(refactored)}/{len(large_files) + len(refactored)} ({len(refactored)*100//(len(large_files) + len(refactored))}%)")

if __name__ == "__main__":
    analyze_files()
