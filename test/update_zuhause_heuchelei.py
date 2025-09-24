#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Оновлення двох нових виправлень транскрипцій в JSON файлах
"""

import os
import json
from pathlib import Path

def main():
    os.chdir(r'F:\AiKlientBank\Lir')
    
    print("[UPDATE] Оновлення транскрипцій das Zuhause та die Heuchelei")
    print("=" * 60)
    
    # Нові виправлення
    UPDATES = {
        'das Zuhause': '[дас цу-ХАУ-зе]',  # було ЦУ-хау-зе → цу-ХАУ-зе
        'die Heuchelei': '[ди хой-хе-ЛАЙ]'  # було ХОЙ-хе-лай → хой-хе-ЛАЙ
    }
    
    print("\n[CHANGES] Нові транскрипції:")
    for word, trans in UPDATES.items():
        print(f"  {word}: {trans}")
    
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
                
                if german in UPDATES:
                    old_trans = item.get('transcription', '')
                    new_trans = UPDATES[german]
                    
                    if old_trans != new_trans:
                        item['transcription'] = new_trans
                        file_updated = True
                        updated_words += 1
                        
                        updates_log.append({
                            'file': json_file.name,
                            'word': german,
                            'old': old_trans,
                            'new': new_trans
                        })
        
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
        print(f"\n[LOG] Детальний лог оновлень:")
        for upd in updates_log:
            print(f"\n  Файл: {upd['file']}")
            print(f"  Слово: {upd['word']}")
            print(f"    Було: {upd['old']}")
            print(f"    Стало: {upd['new']}")
    
    # Перевірка оновлення
    print(f"\n[VERIFY] Перевірка оновлення:")
    verify_count = 0
    
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'vocabulary' in data:
            for item in data['vocabulary']:
                german = item.get('german', item.get('word'))
                
                if german in UPDATES:
                    trans = item.get('transcription', '')
                    expected = UPDATES[german]
                    status = "[OK]" if trans == expected else "[ERROR]"
                    print(f"  {status} {json_file.name}: {german} = {trans}")
                    verify_count += 1
    
    if verify_count == 0:
        print("  Слова das Zuhause та die Heuchelei не знайдені в JSON файлах")
    
    print(f"\n[SUCCESS] Оновлення завершено!")

if __name__ == "__main__":
    main()
