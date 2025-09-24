#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
КРИТИЧНИЙ ФІКС: Виправлення формату exercise в JSON файлах
Генератор очікує: {text, answers}
Ми створили: {content, gaps}
"""

import json
import re
from pathlib import Path

def fix_exercise_format(json_file):
    """
    Виправляє формат exercise на правильний
    """
    try:
        # Читаємо JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        exercise = data.get('exercise')
        
        # Якщо exercise є об'єктом з неправильними полями
        if isinstance(exercise, dict):
            # Якщо є поле content - це наш новий формат
            if 'content' in exercise:
                # Перетворюємо content -> text
                text = exercise.get('content', '')
                
                # Створюємо answers з тексту
                answers = {}
                # Шукаємо всі пропуски в тексті
                gaps = re.findall(r'___ \(([^)]+)\)', text)
                
                # Для кожного пропуску беремо слово з vocabulary
                vocabulary = data.get('vocabulary', [])
                for i, gap in enumerate(gaps):
                    # gap - це підказка українською
                    # Шукаємо відповідне німецьке слово в vocabulary
                    for word_item in vocabulary:
                        if word_item.get('translation') == gap:
                            # Видаляємо артиклі для відповіді
                            german = word_item.get('german', '')
                            # Видаляємо артиклі
                            for article in ['der ', 'die ', 'das ', 'Der ', 'Die ', 'Das ']:
                                german = german.replace(article, '')
                            answers[gap] = german
                            break
                    
                    # Якщо не знайшли в vocabulary, шукаємо в тексті
                    if gap not in answers:
                        # Можливо слово вже є в правильному форматі
                        answers[gap] = gap  # Тимчасово
                
                # Створюємо новий формат exercise
                new_exercise = {
                    'title': exercise.get('title', 'Упражнение'),
                    'text': text,
                    'answers': answers
                }
                
                data['exercise'] = new_exercise
                
                # Зберігаємо виправлений JSON
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                return True, len(answers)
            
            # Якщо вже правильний формат
            elif 'text' in exercise and 'answers' in exercise:
                return False, 0  # Вже правильний формат
        
        # Якщо exercise - рядок (старий формат)
        elif isinstance(exercise, str):
            # Створюємо правильний формат
            text = exercise
            
            # Створюємо answers
            answers = {}
            gaps = re.findall(r'___ \(([^)]+)\)', text)
            
            vocabulary = data.get('vocabulary', [])
            for gap in gaps:
                for word_item in vocabulary:
                    if word_item.get('translation') == gap:
                        german = word_item.get('german', '')
                        for article in ['der ', 'die ', 'das ']:
                            german = german.replace(article, '')
                        answers[gap] = german
                        break
                
                if gap not in answers:
                    answers[gap] = gap
            
            data['exercise'] = {
                'title': 'Упражнение',
                'text': text,
                'answers': answers
            }
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True, len(answers)
    
    except Exception as e:
        print(f"[ERROR] {json_file.name}: {e}")
        return False, 0
    
    return False, 0

def main():
    print("[CRITICAL FIX] Виправлення формату exercise в JSON файлах")
    print("=" * 60)
    
    base_dir = Path(r'F:\AiKlientBank\Lir\data')
    
    total_fixed = 0
    total_files = 0
    
    for folder in ['b1', 'a2', 'thematic']:
        folder_path = base_dir / folder
        if not folder_path.exists():
            continue
        
        print(f"\n[{folder.upper()}] Обробка папки...")
        
        json_files = list(folder_path.glob('**/*.json'))
        
        for json_file in json_files:
            total_files += 1
            fixed, answers_count = fix_exercise_format(json_file)
            
            if fixed:
                print(f"  [FIXED] {json_file.name} - {answers_count} відповідей")
                total_fixed += 1
            else:
                print(f"  [OK] {json_file.name}")
    
    print("\n" + "=" * 60)
    print(f"[RESULT] Виправлено: {total_fixed}/{total_files} файлів")
    print("[DONE] Формат exercise виправлено!")

if __name__ == '__main__':
    main()
