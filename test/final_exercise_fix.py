#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ФИНАЛЬНЫЙ ФИКСЕР - исправляет ВСЕ проблемы с упражнениями
"""

import json
import re
from pathlib import Path

def fix_all_problems(text):
    """
    Исправляет ВСЕ проблемы одним махом:
    1. Любые дубликаты после пропусков
    2. Звездочки
    3. Лишние пробелы
    """
    # 1. Убираем любые дубликаты в скобках после пропусков
    # Паттерн: ___ (что-то) (еще_что-то) -> ___ (что-то)
    text = re.sub(r'(___ \([^)]+\))\s*\([^)]+\)', r'\1', text)
    
    # 2. Заменяем звездочки на подчеркивания
    text = re.sub(r'\*{3,}[_\s]*', '___', text)
    
    # 3. Исправляем паттерны с артиклями и звездочками
    text = re.sub(r'(DER|DIE|DAS)\s+\*{3,}[_\s]*\(([^)]+)\)', r'\1 ___ (\2)', text)
    
    # 4. Убираем двойные пробелы
    text = re.sub(r'\s+', ' ', text)
    
    return text

def process_all_files():
    """Обрабатывает все JSON файлы"""
    base_dir = Path(r'F:\AiKlientBank\Lir\data')
    
    fixed_files = []
    total_files = 0
    
    for folder in ['a2', 'b1', 'thematic']:
        folder_path = base_dir / folder
        if not folder_path.exists():
            continue
        
        json_files = list(folder_path.glob('*.json'))
        
        for json_file in json_files:
            total_files += 1
            
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                exercise = data.get('exercise')
                if not exercise or not isinstance(exercise, dict):
                    continue
                
                original_text = exercise.get('text', '')
                if not original_text:
                    continue
                
                # Применяем все исправления
                fixed_text = fix_all_problems(original_text)
                
                if fixed_text != original_text:
                    exercise['text'] = fixed_text
                    
                    # Сохраняем
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    
                    fixed_files.append({
                        'folder': folder,
                        'file': json_file.name
                    })
            
            except Exception as e:
                print(f"[ERROR] {json_file.name}: {e}")
    
    return fixed_files, total_files

# Запускаем исправление
print("[FINAL FIX] Исправление ВСЕХ проблем с упражнениями")
print("=" * 70)

fixed, total = process_all_files()

if fixed:
    print(f"\n[OK] Исправлено файлов: {len(fixed)}/{total}")
    
    # Группируем по папкам
    by_folder = {}
    for item in fixed:
        folder = item['folder']
        if folder not in by_folder:
            by_folder[folder] = []
        by_folder[folder].append(item['file'])
    
    for folder, files in by_folder.items():
        print(f"\n[{folder.upper()}] Исправлено {len(files)} файлов:")
        for f in files[:3]:  # Показываем первые 3
            print(f"  - {f}")
        if len(files) > 3:
            print(f"  ... и еще {len(files) - 3}")
else:
    print("\n[!] Все упражнения уже исправлены!")

print("\n" + "=" * 70)
print("[DONE] Все проблемы устранены! Можно генерировать сайт.")
