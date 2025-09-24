#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для створення театральних вправ з пропусками
Замінює шаблонні речення на театральний текст з пропусками
"""

import json
import re
from pathlib import Path

def create_theatrical_exercise(story_content, vocabulary_words):
    """
    Створює вправу з театрального тексту, замінюючи виділені слова на пропуски
    """
    
    # Копіюємо театральний текст
    exercise_text = story_content
    
    # Словник для збереження замін
    replacements = []
    
    # Для кожного слова зі словника
    for i, word_item in enumerate(vocabulary_words):
        # Отримуємо німецьке слово та переклад
        word_de = word_item['german']
        word_translation = word_item['translation']
        
        # Видаляємо артиклі для пошуку
        word_clean = word_de
        for article in ['der ', 'die ', 'das ', 'Der ', 'Die ', 'Das ']:
            word_clean = word_clean.replace(article, '')
        
        # Створюємо різні варіанти слова для пошуку
        word_variants = [
            word_clean.upper(),
            word_clean.capitalize(),
            word_clean.lower(),
            word_de.upper(),
            word_de.capitalize(),
            word_de.lower()
        ]
        
        # Шукаємо слово в тексті
        replaced = False
        for variant in word_variants:
            # Шаблони для пошуку слова в тексті
            patterns = [
                f'\\*\\*{re.escape(variant)}\\*\\*',  # **СЛОВО**
                f'\\*\\*[A-Z]+\\s+{re.escape(variant)}\\*\\*',  # **DAS СЛОВО**
                f'\\*\\*{re.escape(variant)}\\s+\\([^)]+\\)\\*\\*',  # **СЛОВО (переклад)**
            ]
            
            for pattern in patterns:
                if re.search(pattern, exercise_text, re.IGNORECASE):
                    # Зберігаємо заміну
                    replacements.append((variant, word_translation))
                    # Замінюємо на пропуск з підказкою
                    exercise_text = re.sub(
                        pattern,
                        f'*___ ({word_translation})*',
                        exercise_text,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    replaced = True
                    print(f"  [+] Замінено: {variant} -> ___ ({word_translation})")
                    break
            
            if replaced:
                break
        
        # Якщо не знайшли у виділеному вигляді, шукаємо без зірочок
        if not replaced:
            for variant in word_variants:
                # Шукаємо слово як окреме слово (word boundary)
                pattern = f'\\b{re.escape(variant)}\\b'
                if re.search(pattern, exercise_text, re.IGNORECASE):
                    # Замінюємо перше входження
                    exercise_text = re.sub(
                        pattern,
                        f'___ ({word_translation})',
                        exercise_text,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    print(f"  [+] Замінено (без виділення): {variant} -> ___ ({word_translation})")
                    break
    
    return exercise_text

def process_json_files(base_path='F:\\AiKlientBank\\Lir\\data'):
    """
    Обробляє всі JSON файли та створює театральні вправи
    """
    base_dir = Path(base_path)
    
    # Папки для обробки - починаємо з B1
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
                
                # Перевіряємо структуру
                if 'story' not in data or 'vocabulary' not in data:
                    print(f"  [!] Пропускаємо - немає story або vocabulary")
                    continue
                
                if 'content' not in data['story']:
                    print(f"  [!] Пропускаємо - немає story.content")
                    continue
                
                # Отримуємо театральний текст та слова
                story_content = data['story']['content']
                vocabulary_words = data['vocabulary']
                
                if not vocabulary_words:
                    print(f"  [!] Пропускаємо - vocabulary порожній")
                    continue
                
                # Створюємо нову вправу з театрального тексту
                new_exercise = create_theatrical_exercise(story_content, vocabulary_words)
                
                # Оновлюємо exercise
                old_exercise = data.get('exercise', '')
                
                # Перевіряємо, чи потрібно оновлення
                if old_exercise != new_exercise:
                    data['exercise'] = new_exercise
                    
                    # Зберігаємо оновлений JSON
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    
                    print(f"  [OK] Вправу оновлено!")
                    total_updated += 1
                    
                    # Показуємо короткий приклад
                    print(f"  Початок вправи: {new_exercise[:150]}...")
                else:
                    print(f"  [=] Вправа вже правильна")
                    
            except Exception as e:
                print(f"  [ERROR] Помилка: {e}")
                import traceback
                traceback.print_exc()
    
    print("\n" + "=" * 50)
    print(f"[РЕЗУЛЬТАТ]")
    print(f"  Оброблено файлів: {total_processed}")
    print(f"  Оновлено: {total_updated}")
    print(f"  Без змін: {total_processed - total_updated}")

def main():
    print("[START] Виправлення вправ - створення театральних текстів з пропусками")
    print("=" * 50)
    
    process_json_files()
    
    print("\n[DONE] Скрипт завершено!")

if __name__ == '__main__':
    main()
