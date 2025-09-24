#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для правильного форматування театральних вправ
Замість простого тексту створює об'єкт з полем content
"""

import json
import re
from pathlib import Path

def format_theatrical_exercise(exercise_text):
    """
    Форматує театральну вправу в правильну структуру
    """
    
    # Розбиваємо текст на речення для створення питань
    # Шукаємо всі пропуски
    gaps = re.findall(r'___ \(([^)]+)\)', exercise_text)
    
    # Створюємо структуру вправи
    exercise = {
        "title": "🎭 Заповніть пропуски в театральній постановці",
        "type": "theatrical_gaps",
        "content": exercise_text,
        "gaps": gaps,
        "instruction": f"Заповніть {len(gaps)} пропусків у театральному тексті. Підказки в дужках допоможуть вам."
    }
    
    return exercise

def process_json_files(base_path='F:\\AiKlientBank\\Lir\\data'):
    """
    Обробляє всі JSON файли та форматує вправи
    """
    base_dir = Path(base_path)
    
    # Папки для обробки
    folders = ['b1', 'a2', 'thematic']
    
    total_processed = 0
    total_updated = 0
    
    for folder in folders:
        folder_path = base_dir / folder
        if not folder_path.exists():
            print(f"[!] Папка не існує: {folder_path}")
            continue
            
        print(f"\n[=] Обробка папки: {folder}")
        print("=" * 50)
        
        # Знаходимо всі JSON файли
        json_files = list(folder_path.glob('**/*.json'))
        
        for json_file in json_files:
            total_processed += 1
            print(f"\n[{total_processed}] Файл: {json_file.name}")
            
            try:
                # Читаємо JSON
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Перевіряємо, чи exercise є рядком (текстом)
                if 'exercise' in data and isinstance(data['exercise'], str):
                    # Форматуємо в правильну структуру
                    exercise_text = data['exercise']
                    data['exercise'] = format_theatrical_exercise(exercise_text)
                    
                    # Зберігаємо оновлений JSON
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    
                    print(f"  [OK] Вправу відформатовано!")
                    print(f"  Знайдено пропусків: {len(data['exercise']['gaps'])}")
                    total_updated += 1
                else:
                    print(f"  [=] Вправа вже має правильний формат або відсутня")
                    
            except Exception as e:
                print(f"  [ERROR] Помилка: {e}")
                import traceback
                traceback.print_exc()
    
    print("\n" + "=" * 50)
    print(f"[РЕЗУЛЬТАТ]")
    print(f"  Оброблено файлів: {total_processed}")
    print(f"  Відформатовано: {total_updated}")
    print(f"  Без змін: {total_processed - total_updated}")

def main():
    print("[START] Форматування театральних вправ у правильну структуру")
    print("=" * 50)
    
    process_json_files()
    
    print("\n[DONE] Скрипт завершено!")

if __name__ == '__main__':
    main()
