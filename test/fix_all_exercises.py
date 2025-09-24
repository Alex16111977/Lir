#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
УНИВЕРСАЛЬНЫЙ ФИКСЕР упражнений
Исправляет все проблемы:
1. Дубликаты подсказок: ___ (hint) (hint) -> ___ (hint)
2. Звездочки: DER *****_______ -> DER ___
3. Несоответствие answers
"""

import json
import re
from pathlib import Path

class ExerciseFixer:
    def __init__(self):
        self.fixed_count = 0
        self.problems_fixed = {
            'doubles': 0,
            'stars': 0,
            'mismatched': 0
        }
    
    def fix_double_hints(self, text):
        """
        Исправляет дубликаты подсказок
        ___ (подсказка) (подсказка) -> ___ (подсказка)
        """
        # Паттерн: ___ (hint) (same_hint)
        pattern = r'___ \(([^)]+)\) \(\1\)'
        fixed_text = re.sub(pattern, r'___ (\1)', text)
        
        # Подсчет исправлений
        if fixed_text != text:
            self.problems_fixed['doubles'] += 1
        
        return fixed_text
    
    def fix_stars_pattern(self, text):
        """
        Исправляет звездочки на подчеркивания
        DER *****_______ (hint) -> DER ___ (hint)
        DAS *****_______ -> DAS ___
        """
        # Паттерн 1: артикль + звездочки + подчеркивания + подсказка
        pattern1 = r'(DER|DIE|DAS)\s+\*{3,}[_\s]*\(([^)]+)\)(?:\s*\([^)]+\))?'
        text = re.sub(pattern1, r'\1 ___ (\2)', text)
        
        # Паттерн 2: просто звездочки с подчеркиваниями
        pattern2 = r'\*{3,}[_\s]+\(([^)]+)\)(?:\s*\([^)]+\))?'
        text = re.sub(pattern2, r'___ (\1)', text)
        
        # Паттерн 3: звездочки внутри слов (для случаев типа DER *****_______ )
        pattern3 = r'\*{3,}[_\s]*'
        text = re.sub(pattern3, '___', text)
        
        return text
    
    def fix_exercise(self, json_file):
        """
        Исправляет все проблемы в упражнении
        """
        try:
            # Читаем JSON
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            exercise = data.get('exercise')
            if not exercise or not isinstance(exercise, dict):
                return False
            
            original_text = exercise.get('text', '')
            if not original_text:
                return False
            
            # Применяем все исправления
            fixed_text = original_text
            
            # 1. Сначала исправляем звездочки
            fixed_text = self.fix_stars_pattern(fixed_text)
            
            # 2. Затем исправляем дубликаты
            fixed_text = self.fix_double_hints(fixed_text)
            
            # 3. Обновляем answers если нужно
            answers = exercise.get('answers', {})
            gaps = re.findall(r'___ \(([^)]+)\)', fixed_text)
            
            # Создаем новые answers на основе vocabulary
            vocabulary = data.get('vocabulary', [])
            new_answers = {}
            
            for gap in gaps:
                # Сначала проверяем существующие answers
                if gap in answers:
                    new_answers[gap] = answers[gap]
                else:
                    # Ищем в vocabulary
                    found = False
                    for word_item in vocabulary:
                        if word_item.get('translation') == gap:
                            german = word_item.get('german', '')
                            # Удаляем артикли
                            for article in ['der ', 'die ', 'das ', 'Der ', 'Die ', 'Das ']:
                                german = german.replace(article, '')
                            new_answers[gap] = german
                            found = True
                            self.problems_fixed['mismatched'] += 1
                            break
                    
                    if not found:
                        # Если не нашли, оставляем пустым
                        print(f"    [!] Не найден ответ для: {gap}")
                        new_answers[gap] = "???"
            
            # Проверяем были ли изменения
            if fixed_text != original_text or new_answers != answers:
                exercise['text'] = fixed_text
                exercise['answers'] = new_answers
                
                # Сохраняем исправленный JSON
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                self.fixed_count += 1
                return True
            
        except Exception as e:
            print(f"    [ERROR] {e}")
            return False
        
        return False

def main():
    print("[FIX] Универсальное исправление упражнений")
    print("=" * 80)
    
    fixer = ExerciseFixer()
    base_dir = Path(r'F:\AiKlientBank\Lir\data')
    
    for folder in ['a2', 'b1', 'thematic']:
        folder_path = base_dir / folder
        if not folder_path.exists():
            continue
        
        print(f"\n[{folder.upper()}] Обработка папки...")
        
        json_files = list(folder_path.glob('*.json'))
        folder_fixed = 0
        
        for json_file in json_files:
            if fixer.fix_exercise(json_file):
                print(f"  [FIXED] {json_file.name}")
                folder_fixed += 1
            else:
                # Проверяем есть ли вообще упражнение
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if data.get('exercise'):
                        print(f"  [OK] {json_file.name}")
                except:
                    pass
        
        if folder_fixed > 0:
            print(f"  Исправлено файлов: {folder_fixed}")
    
    # Итоговая статистика
    print("\n" + "=" * 80)
    print("[РЕЗУЛЬТАТ]")
    print(f"Всего исправлено файлов: {fixer.fixed_count}")
    print(f"Исправлено дубликатов: {fixer.problems_fixed['doubles']}")
    print(f"Исправлено звездочек: {fixer.problems_fixed['stars']}")
    print(f"Добавлено недостающих ответов: {fixer.problems_fixed['mismatched']}")
    
    if fixer.fixed_count > 0:
        print("\n[OK] Все проблемы исправлены!")
        print("[!] Теперь можно перегенерировать сайт")
    else:
        print("\n[!] Проблем не найдено или уже исправлены")

if __name__ == '__main__':
    main()
