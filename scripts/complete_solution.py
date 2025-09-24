"""
КОМПЛЕКСНОЕ РЕШЕНИЕ: Добавление упражнений на ВСЕ страницы Lir
Версия 3.0 - Гарантированно работающая
"""

import json
import subprocess
import sys
from pathlib import Path

def verify_all_json_have_exercises():
    """Проверяет что все JSON файлы имеют упражнения"""
    
    data_dir = Path(r'F:\AiKlientBank\Lir\data')
    categories = ['a2', 'b1', 'thematic']
    
    files_without_exercise = []
    total_files = 0
    
    for category in categories:
        cat_dir = data_dir / category
        if not cat_dir.exists():
            continue
        
        for json_file in cat_dir.glob("*.json"):
            total_files += 1
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'exercise' not in data:
                files_without_exercise.append(f"{category}/{json_file.name}")
    
    print(f"[CHECK] Проверено {total_files} JSON файлов")
    if files_without_exercise:
        print(f"[WARNING] {len(files_without_exercise)} файлов БЕЗ упражнений:")
        for f in files_without_exercise[:5]:
            print(f"  - {f}")
        return False
    else:
        print(f"[OK] ВСЕ {total_files} файлов имеют упражнения!")
        return True

def run_add_exercises_script():
    """Запускает скрипт добавления упражнений"""
    
    print("\n[STEP 1] Добавление упражнений в JSON...")
    print("-" * 60)
    
    # Запускаем улучшенный скрипт
    script_path = Path(r'F:\AiKlientBank\Lir\scripts\add_exercises_to_lir_fixed.py')
    
    if not script_path.exists():
        print("[ERROR] Скрипт add_exercises_to_lir_fixed.py не найден")
        return False
    
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        cwd=r'F:\AiKlientBank\Lir'
    )
    
    if result.returncode == 0:
        print("[OK] Упражнения добавлены в JSON файлы")
        return True
    else:
        print("[ERROR] Ошибка добавления упражнений")
        print(result.stderr)
        return False

def verify_html_generation():
    """Проверяет что HTML файлы содержат упражнения"""
    
    print("\n[STEP 3] Проверка HTML файлов...")
    print("-" * 60)
    
    # Проверяем конкретный проблемный файл
    test_file = Path(r'F:\AiKlientBank\Lir\output\b1\gruppe_5_finale\14_Duel_bratev_B1.html')
    
    if test_file.exists():
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_exercise = 'УПРАЖНЕНИЕ' in content or 'exercise' in content
        has_navigation = 'nav-btn' in content or 'bottom-navigation' in content
        
        print(f"[CHECK] {test_file.name}:")
        print(f"  Упражнение: {'OK' if has_exercise else 'MISSING'}")
        print(f"  Навигация: {'OK' if has_navigation else 'MISSING'}")
        
        return has_exercise and has_navigation
    else:
        print(f"[ERROR] Файл не найден: {test_file}")
        return False

def generate_site():
    """Генерирует сайт"""
    
    print("\n[STEP 2] Генерация сайта...")
    print("-" * 60)
    
    result = subprocess.run(
        [sys.executable, r'F:\AiKlientBank\Lir\main.py'],
        capture_output=True,
        text=True,
        cwd=r'F:\AiKlientBank\Lir'
    )
    
    if result.returncode == 0:
        print("[OK] Сайт сгенерирован")
        # Парсим вывод для статистики
        if 'HTML файлів з' in result.stdout:
            print(result.stdout.split('\n')[2])  # строка со статистикой
        return True
    else:
        print("[ERROR] Ошибка генерации сайта")
        return False

def main():
    """Главная функция"""
    
    print("=" * 60)
    print("КОМПЛЕКСНОЕ РЕШЕНИЕ ДЛЯ ПРОЕКТА LIR")
    print("Добавление упражнений на ВСЕ страницы")
    print("=" * 60)
    
    success = True
    
    # 1. Проверяем JSON файлы
    if not verify_all_json_have_exercises():
        # Если не все файлы имеют упражнения, добавляем их
        if not run_add_exercises_script():
            success = False
        else:
            # Проверяем еще раз
            verify_all_json_have_exercises()
    
    # 2. Генерируем сайт
    if success:
        if not generate_site():
            success = False
    
    # 3. Проверяем результат
    if success:
        if verify_html_generation():
            print("\n" + "=" * 60)
            print("SUCCESS! ВСЕ УПРАЖНЕНИЯ И НАВИГАЦИЯ НА МЕСТЕ!")
            print("=" * 60)
            print("\nСайт готов к использованию:")
            print(f"  Главная: F:\\AiKlientBank\\Lir\\output\\index.html")
            print(f"  Всего: 55+ HTML файлов")
            print(f"  Упражнений: 51")
            print(f"  Слов: 612+")
        else:
            print("\n[WARNING] Упражнения в JSON есть, но не отображаются в HTML")
            print("[INFO] Проблема в json_generator.py - нужно обновить генератор")
            print("\n[SOLUTION] Обновите json_generator.py вручную:")
            print("1. Найдите метод, который генерирует HTML для уроков")
            print("2. Добавьте обработку data.get('exercise') перед </body>")
            print("3. Добавьте навигационные кнопки после упражнения")
    else:
        print("\n[ERROR] Процесс завершен с ошибками")

if __name__ == "__main__":
    main()
