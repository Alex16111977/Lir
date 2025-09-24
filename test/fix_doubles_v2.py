#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
УЛУЧШЕННЫЙ ФИКСЕР упражнений v2
Исправляет ВСЕ типы дубликатов, включая разноязычные
"""

import json
import re
from pathlib import Path

def fix_all_doubles(text):
    """
    Исправляет ВСЕ типы дубликатов:
    - ___ (hint) (hint)
    - ___ (hint) (другое_слово)
    - Звездочки и прочее
    """
    # 1. Любые дубликаты после пропусков (не только одинаковые)
    # Паттерн: ___ (что-то) (еще_что-то)
    text = re.sub(r'(___ \([^)]+\))\s*\([^)]+\)', r'\1', text)
    
    # 2. Звездочки с подчеркиваниями
    text = re.sub(r'\*{3,}[_\s]*', '___', text)
    
    # 3. Паттерн с артиклями и звездочками
    text = re.sub(r'(DER|DIE|DAS)\s+\*{3,}[_\s]*\(([^)]+)\)', r'\1 ___ (\2)', text)
    
    return text

def fix_json_file(json_path):
    """Исправляет один JSON файл"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        exercise = data.get('exercise')
        if not exercise or not isinstance(exercise, dict):
            return False
        
        original_text = exercise.get('text', '')
        if not original_text:
            return False
        
        # Применяем исправления
        fixed_text = fix_all_doubles(original_text)
        
        if fixed_text != original_text:
            exercise['text'] = fixed_text
            
            # Сохраняем
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    return False

# Исправляем конкретный файл
file_path = Path(r'F:\AiKlientBank\Lir\data\b1\15_Смерть_Корделии_и_Лира_B1.json')
if fix_json_file(file_path):
    print("[OK] Файл исправлен!")
    
    # Проверяем результат
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    text = data['exercise']['text']
    
    # Показываем фрагменты с пропусками
    import re
    gaps = re.findall(r'((?:DER|DIE|DAS)?\s*___ \([^)]+\))', text)
    
    print("\nПропуски после исправления:")
    for gap in gaps:
        print(f"  {gap}")
else:
    print("[!] Файл не требует исправления или ошибка")
