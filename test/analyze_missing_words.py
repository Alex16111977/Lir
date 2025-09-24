#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Анализ слов из JSON файлов и поиск отсутствующих в словаре
Дата: 06.09.2025
"""

import json
import os
from pathlib import Path
import sys

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Загружаем словарь транскрипций
from full_stress_dictionary_v2 import FULL_STRESS_DICTIONARY

def analyze_vocabulary():
    """Анализ всех слов из JSON файлов"""
    
    # Собираем все слова из JSON файлов
    all_words_from_json = {}
    data_dir = project_root / 'data'
    
    # Категории для группировки
    categories = {
        'a2': [],
        'b1': [],
        'thematic': []
    }
    
    # Обходим все JSON файлы
    for json_file in data_dir.glob('**/*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Определяем категорию по пути
                category = 'thematic'
                if 'a2' in str(json_file).lower():
                    category = 'a2'
                elif 'b1' in str(json_file).lower():
                    category = 'b1'
                
                if 'vocabulary' in data:
                    for word_entry in data['vocabulary']:
                        german = word_entry.get('german', '').strip()
                        russian = word_entry.get('russian', '').strip()
                        pos = word_entry.get('pos', '').strip()
                        
                        if german:
                            # Сохраняем информацию о слове
                            word_info = {
                                'german': german,
                                'russian': russian,
                                'pos': pos,
                                'file': json_file.name,
                                'category': category
                            }
                            
                            if german not in all_words_from_json:
                                all_words_from_json[german] = []
                            all_words_from_json[german].append(word_info)
                            
        except Exception as e:
            print(f'[ERROR] {json_file}: {e}')
    
    # Статистика
    print("=" * 70)
    print("АНАЛИЗ СЛОВАРЯ ПРОЕКТА LIR")
    print("=" * 70)
    
    print(f"\n[СТАТИСТИКА]")
    print(f"  Уникальных слов в JSON: {len(all_words_from_json)}")
    print(f"  Слов в словаре транскрипций: {len(FULL_STRESS_DICTIONARY)}")
    
    # Находим слова, которых нет в словаре
    missing_words = set(all_words_from_json.keys()) - set(FULL_STRESS_DICTIONARY.keys())
    
    print(f"  Отсутствует в словаре: {len(missing_words)}")
    
    # Группируем отсутствующие слова по категориям и частям речи
    missing_by_category = {
        'a2': {'существительные': [], 'глаголы': [], 'прилагательные': [], 'другое': []},
        'b1': {'существительные': [], 'глаголы': [], 'прилагательные': [], 'другое': []},
        'thematic': {'существительные': [], 'глаголы': [], 'прилагательные': [], 'другое': []}
    }
    
    for word in missing_words:
        word_infos = all_words_from_json[word]
        for info in word_infos:
            category = info['category']
            pos = info['pos']
            
            # Определяем часть речи
            if 'существительное' in pos.lower():
                pos_category = 'существительные'
            elif 'глагол' in pos.lower():
                pos_category = 'глаголы'
            elif 'прилагательное' in pos.lower():
                pos_category = 'прилагательные'
            else:
                pos_category = 'другое'
            
            # Добавляем в соответствующую категорию
            entry = f"{word} - {info['russian']}"
            if entry not in missing_by_category[category][pos_category]:
                missing_by_category[category][pos_category].append(entry)
    
    # Выводим отсутствующие слова по категориям
    print("\n" + "=" * 70)
    print("СЛОВА, ОТСУТСТВУЮЩИЕ В СЛОВАРЕ ТРАНСКРИПЦИЙ")
    print("=" * 70)
    
    for category in ['a2', 'b1', 'thematic']:
        category_data = missing_by_category[category]
        total_in_category = sum(len(words) for words in category_data.values())
        
        if total_in_category > 0:
            print(f"\n[{category.upper()}] УРОВЕНЬ - {total_in_category} слов")
            print("-" * 50)
            
            for pos_type, words in category_data.items():
                if words:
                    print(f"\n  {pos_type.capitalize()} ({len(words)} слов):")
                    for word in sorted(words):
                        print(f"    - {word}")
    
    # Дополнительный анализ - слова в словаре, но не в JSON
    extra_words = set(FULL_STRESS_DICTIONARY.keys()) - set(all_words_from_json.keys())
    
    if extra_words:
        print("\n" + "=" * 70)
        print("СЛОВА В СЛОВАРЕ, НО ОТСУТСТВУЮЩИЕ В JSON")
        print(f"Всего: {len(extra_words)} слов")
        print("=" * 70)
        
        # Показываем первые 20 слов
        print("\nПримеры (первые 20):")
        for word in sorted(extra_words)[:20]:
            print(f"  - {word}: {FULL_STRESS_DICTIONARY[word]}")
    
    # Сохраняем отчет
    report_path = project_root / 'test' / 'vocabulary_gap_analysis.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("АНАЛИЗ ПРОБЕЛОВ В СЛОВАРЕ ТРАНСКРИПЦИЙ\n")
        f.write("=" * 70 + "\n")
        f.write(f"Дата: 06.09.2025\n")
        f.write(f"Уникальных слов в JSON: {len(all_words_from_json)}\n")
        f.write(f"Слов в словаре: {len(FULL_STRESS_DICTIONARY)}\n")
        f.write(f"Отсутствует: {len(missing_words)}\n")
        f.write("\n" + "=" * 70 + "\n")
        
        for category in ['a2', 'b1', 'thematic']:
            category_data = missing_by_category[category]
            total_in_category = sum(len(words) for words in category_data.values())
            
            if total_in_category > 0:
                f.write(f"\n[{category.upper()}] - {total_in_category} слов\n")
                f.write("-" * 50 + "\n")
                
                for pos_type, words in category_data.items():
                    if words:
                        f.write(f"\n{pos_type.capitalize()} ({len(words)}):\n")
                        for word in sorted(words):
                            f.write(f"  - {word}\n")
    
    print(f"\n[OK] Отчет сохранен: {report_path}")
    
    return missing_words, all_words_from_json

if __name__ == "__main__":
    missing_words, all_words = analyze_vocabulary()
