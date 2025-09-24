#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Оновлення останніх виправлень транскрипцій від викладача
"""

import os
import json
from pathlib import Path

def main():
    os.chdir(r'F:\AiKlientBank\Lir')
    
    print("[UPDATE] Оновлення останніх виправлень транскрипцій")
    print("=" * 60)
    
    # Завантажую повний словник
    with open('test/full_stress_dictionary_v2.py', 'r', encoding='utf-8') as f:
        exec_globals = {}
        exec(f.read(), exec_globals)
        DICT = exec_globals['FULL_STRESS_DICTIONARY']
    
    # Виправлені слова
    FIXED_WORDS = {
        'die Undankbarkeit': '[ди ун-ДАНК-бар-кайт]',  # було УН- → ун-ДАНК-
        'der Wächter': '[дер ВЕХ-тер]',                # було ВЕХТ-ер → ВЕХ-тер
        'die Schwester': '[ди ШВЕС-тер]',              # було ШВЕСТ-ер → ШВЕС-тер
        'demütig': '[ДЕ-мю-тиг]',                      # було де-МЮ-тиг → ДЕ-мю-тиг
        'demütigen': '[ДЕ-мю-ти-ген]',                 # було де-МЮ-ти-ген → ДЕ-мю-ти-ген
        'naiv': '[на-ИФ]',                             # було НАЙФ → на-ИФ
        'das Rätsel': '[дас РЕТ-цель]'                 # було РЕТ-зель → РЕТ-цель
    }
    
    print("\n[CHANGES] Виправлені транскрипції:")
    for word, trans in FIXED_WORDS.items():
        dict_trans = DICT.get(word, 'НЕ В СЛОВНИКУ')
        print(f"  {word}:")
        print(f"    Нова: {trans}")
        print(f"    Словник: {dict_trans}")
        print(f"    Збігається: {'ТАК' if trans == dict_trans else 'НІ'}")
    
    # Збираю всі JSON файли
    data_path = Path('data')
    json_files = []
    
    for subdir in data_path.iterdir():
        if subdir.is_dir():
            json_files.extend(subdir.glob('*.json'))
    
    print(f"\n[INFO] Знайдено JSON файлів: {len(json_files)}")
    
    # Оновлюю файли
    updated_files = 0
    updated_words = 0
    updates_log = []
    
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        file_updated = False
        
        if 'vocabulary' in data:
            for item in data['vocabulary']:
                german = item.get('german', item.get('word'))
                
                if german in DICT:
                    old_trans = item.get('transcription', '')
                    new_trans = DICT[german]
                    
                    # Оновлюю якщо відрізняється
                    if old_trans != new_trans:
                        # Логую тільки виправлені слова
                        if german in FIXED_WORDS:
                            updates_log.append({
                                'file': json_file.name,
                                'word': german,
                                'old': old_trans,
                                'new': new_trans
                            })
                        
                        item['transcription'] = new_trans
                        file_updated = True
                        updated_words += 1
        
        # Зберігаю файл якщо були зміни
        if file_updated:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            updated_files += 1
    
    # Виводжу результати
    print(f"\n[RESULTS] Результати оновлення:")
    print(f"  Оновлено файлів: {updated_files}")
    print(f"  Оновлено слів: {updated_words}")
    
    if updates_log:
        print(f"\n[LOG] Оновлення виправлених слів:")
        for upd in updates_log:
            print(f"\n  Файл: {upd['file']}")
            print(f"  Слово: {upd['word']}")
            print(f"    Було: {upd['old']}")
            print(f"    Стало: {upd['new']}")
    
    # Фінальна перевірка
    print(f"\n[VERIFY] Перевірка оновлення:")
    found_any = False
    
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'vocabulary' in data:
            for item in data['vocabulary']:
                german = item.get('german', item.get('word'))
                
                if german in FIXED_WORDS:
                    trans = item.get('transcription', '')
                    expected = FIXED_WORDS[german]
                    status = "[OK]" if trans == expected else "[ERROR]"
                    print(f"  {status} {json_file.name}: {german} = {trans}")
                    found_any = True
    
    if not found_any:
        print("  (виправлені слова не знайдені в JSON файлах)")
    
    print(f"\n[SUCCESS] Оновлення завершено!")

if __name__ == "__main__":
    main()
