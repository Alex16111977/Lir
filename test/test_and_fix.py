"""
Test and Fix Project
Тестування та виправлення проекту Lir
"""

import sys
from pathlib import Path

# Додаємо шлях до проекту
project_dir = Path(r'F:\AiKlientBank\Lir')
sys.path.insert(0, str(project_dir))

def fix_imports():
    """Виправити імпорти в json_generator.py"""
    json_gen_file = project_dir / 'src' / 'generators' / 'json_generator.py'
    
    if json_gen_file.exists():
        content = json_gen_file.read_text(encoding='utf-8')
        
        # Виправляємо імпорти
        old_imports = [
            "from src.generators.exercises_assets import ExercisesAssetsGenerator",
            "from src.generators.exercises_generator import ExercisesGenerator"
        ]
        
        new_imports = [
            "from .exercises_assets import ExercisesAssetsGenerator",
            "from .exercises_generator import ExercisesGenerator"
        ]
        
        for old, new in zip(old_imports, new_imports):
            if old in content:
                content = content.replace(old, new)
                print(f"[FIX] Замінено: {old[:40]}...")
        
        # Зберігаємо виправлений файл
        json_gen_file.write_text(content, encoding='utf-8')
        print("[OK] Імпорти виправлено")
        return True
    else:
        print("[ERROR] json_generator.py не знайдено")
        return False

def test_project():
    """Тестування проекту"""
    import subprocess
    
    result = subprocess.run(
        [sys.executable, str(project_dir / 'main.py')],
        capture_output=True,
        text=True,
        cwd=str(project_dir)
    )
    
    if result.returncode == 0:
        print("[OK] Проект працює!")
        print(result.stdout[:500])
        
        # Перевірка кількості файлів
        output_dir = project_dir / 'output'
        if output_dir.exists():
            html_files = list(output_dir.glob('**/*.html'))
            print(f"[RESULT] Згенеровано {len(html_files)} HTML файлів")
            
            if len(html_files) >= 55:
                print("[SUCCESS] Генерація успішна!")
                return True
    else:
        print(f"[ERROR] Помилка запуску: {result.stderr[:500]}")
        
    return False

def analyze_structure():
    """Аналіз структури проекту"""
    print("\n[ANALYZE] Аналіз великих файлів:")
    print("-" * 60)
    
    generators_dir = project_dir / 'src' / 'generators'
    large_files = []
    
    for py_file in generators_dir.glob('*.py'):
        if py_file.name != '__init__.py':
            try:
                content = py_file.read_text(encoding='utf-8')
                lines = len(content.splitlines())
                
                if lines > 300:
                    large_files.append((py_file.name, lines))
                    print(f"  {py_file.name:30} - {lines:5} рядків")
            except Exception as e:
                print(f"  {py_file.name:30} - ERROR: {e}")
    
    print(f"\n[TOTAL] {len(large_files)} файлів > 300 рядків")
    return large_files

if __name__ == "__main__":
    print("=" * 60)
    print("TEST AND FIX LIR PROJECT")
    print("=" * 60)
    
    # Виправляємо імпорти
    if fix_imports():
        # Тестуємо проект
        if test_project():
            # Аналізуємо структуру
            analyze_structure()
            print("\n[READY] Проект готовий до рефакторингу!")
        else:
            print("\n[ACTION] Потрібне додаткове налагодження")
    else:
        print("\n[ERROR] Не вдалось виправити імпорти")
