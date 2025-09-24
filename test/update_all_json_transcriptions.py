#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для обновления всех транскрипций в JSON файлах
на основе словаря full_stress_dictionary_v2.py
"""

import os
import json
from pathlib import Path
import sys

def main():
    os.chdir(r'F:\AiKlientBank\Lir')
    
    print("[START] Обновление транскрипций в JSON файлах")
    print("=" * 60)
    
    # Загружаю словарь транскрипций
    try:
        with open('test/full_stress_dictionary_v2.py', 'r', encoding='utf-8') as f:
            exec_globals = {}
            exec(f.read(), exec_globals)
            FULL_STRESS_DICTIONARY = exec_globals['FULL_STRESS_DICTIONARY']
        
        print(f"[OK] Загружен словарь: {len(FULL_STRESS_DICTIONARY)} транскрипций")
    except Exception as e:
        print(f"[ERROR] Не могу загрузить словарь: {e}")
        return
    
    # Собираю все JSON файлы
    data_path = Path('data')
    json_files = []
    
    for subdir in data_path.iterdir():
        if subdir.is_dir():
            json_files.extend(subdir.glob('*.json'))
    
    print(f"[INFO] Найдено JSON файлов: {len(json_files)}")
    
    # Счетчики
    updated_files = 0
    updated_words = 0
    not_in_dict = set()
    examples = []
    
    # Обновляю каждый файл
    for json_file in json_files:
        try:
            # Читаю JSON
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            file_updated = False
            file_updates = []
            
            # Обновляю транскрипции
            if 'vocabulary' in data:
                for word_item in data['vocabulary']:
                    # Ищу немецкое слово
                    german_word = word_item.get('german') or word_item.get('word')
                    
                    if german_word:
                        if german_word in FULL_STRESS_DICTIONARY:
                            new_trans = FULL_STRESS_DICTIONARY[german_word]
                            old_trans = word_item.get('transcription', '')
                            
                            if old_trans != new_trans:
                                word_item['transcription'] = new_trans
                                file_updated = True
                                updated_words += 1
                                file_updates.append({
                                    'word': german_word,
                                    'old': old_trans,
                                    'new': new_trans
                                })
                        else:
                            # Слова нет в словаре
                            if word_item.get('transcription'):
                                not_in_dict.add(german_word)
            
            # Сохраняю если были изменения
            if file_updated:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                updated_files += 1
                
                # Сохраняю примеры для вывода
                if len(examples) < 5 and file_updates:
                    examples.append({
                        'file': json_file.name,
                        'updates': file_updates[:2]  # Первые 2 обновления
                    })
                    
        except Exception as e:
            print(f"[ERROR] {json_file.name}: {e}")
    
    # Вывод результатов
    print(f"\n[RESULTS] Результаты обновления:")
    print(f"  Обновлено файлов: {updated_files}/{len(json_files)}")
    print(f"  Обновлено слов: {updated_words}")
    print(f"  Слов со старой транскрипцией (не в словаре): {len(not_in_dict)}")
    
    if examples:
        print(f"\n[EXAMPLES] Примеры обновлений:")
        for ex in examples:
            print(f"\n  Файл: {ex['file']}")
            for upd in ex['updates']:
                print(f"    {upd['word']}:")
                print(f"      Было: {upd['old']}")
                print(f"      Стало: {upd['new']}")
    
    if not_in_dict and len(not_in_dict) <= 20:
        print(f"\n[NOT IN DICT] Слова без новой транскрипции:")
        for word in sorted(list(not_in_dict))[:10]:
            print(f"  - {word}")
    
    # Проверяю конкретный файл
    test_file = Path('data/b1/09_Ослепление_Глостера_B1.json')
    if test_file.exists():
        with open(test_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"\n[VERIFY] Проверка файла {test_file.name}:")
        check_words = ['die Augen', 'blind', 'binden', 'der Verräter']
        found_any = False
        
        for word_item in data['vocabulary']:
            german = word_item.get('german', word_item.get('word'))
            if german in check_words:
                trans = word_item.get('transcription', 'НЕТ')
                print(f"  {german}: {trans}")
                found_any = True
        
        if not found_any:
            print("  (проверочные слова не найдены в этом файле)")
    
    print(f"\n[SUCCESS] Обновление завершено!")
    print(f"[NEXT] Теперь можно запускать генерацию: python main.py")

if __name__ == "__main__":
    main()
