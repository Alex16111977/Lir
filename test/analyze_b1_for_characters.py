#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Анализ B1 словаря для создания карт персонажей
Версия: 1.0 - 06.09.2025
"""

import json
from pathlib import Path
from collections import defaultdict

def analyze_b1_vocabulary():
    """Анализирует существующий B1 словарь"""
    
    b1_path = Path(r'F:\AiKlientBank\Lir\data\b1')
    
    # Собираем статистику
    all_words = []
    character_words = defaultdict(list)
    location_words = defaultdict(list) 
    emotion_words = defaultdict(list)
    gesture_words = defaultdict(list)
    
    # Данные по файлам
    file_data = {}
    
    for json_file in sorted(b1_path.glob('*.json')):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            file_name = json_file.stem
            
            # Сохраняем данные файла
            file_data[file_name] = {
                'title': data.get('title', ''),
                'icon': data.get('icon', ''),
                'quote': data.get('quote', ''),
                'words_count': 0
            }
            
            if 'vocabulary' in data:
                file_data[file_name]['words_count'] = len(data['vocabulary'])
                
                for word in data['vocabulary']:
                    word_text = word['german']
                    all_words.append(word_text)
                    
                    # Анализируем персонажей
                    if 'character_voice' in word:
                        char = word['character_voice']['character']
                        character_words[char].append({
                            'word': word_text,
                            'context': word['character_voice']['german'],
                            'translation': word['translation'],
                            'file': file_name
                        })
                    
                    # Анализируем эмоции и жесты
                    if 'gesture' in word:
                        if 'emotion' in word['gesture']:
                            emotion_words[word['gesture']['emotion']].append(word_text)
                        if 'gesture' in word['gesture']:
                            gesture_words[word['gesture']['gesture']].append(word_text)
                    
                    # Определяем локацию по файлу
                    if 'Тронный' in file_name:
                        location = '🏰 Замок'
                    elif 'Буря' in file_name or 'безумие' in file_name:
                        location = '⛈️ Буря'
                    elif 'Дувр' in file_name:
                        location = '🏔️ Дувр'
                    elif 'Битва' in file_name or 'Дуэль' in file_name:
                        location = '⚔️ Битва'
                    elif 'Смерть' in file_name:
                        location = '⛓️ Тюрьма'
                    elif 'Примирение' in file_name:
                        location = '💝 Примирение'
                    elif 'Интрига' in file_name or 'Обман' in file_name:
                        location = '🎭 Интрига'
                    else:
                        location = '🛤️ Путь'
                    
                    location_words[location].append({
                        'word': word_text,
                        'translation': word['translation'],
                        'file': file_name
                    })
    
    # Формируем отчет
    report = []
    report.append("="*70)
    report.append("АНАЛИЗ B1 СЛОВАРЯ ДЛЯ КАРТ ПЕРСОНАЖЕЙ")
    report.append("="*70)
    
    # Общая статистика
    unique_words = list(set(all_words))
    report.append(f"\n[ОБЩАЯ СТАТИСТИКА]")
    report.append(f"Файлов: {len(file_data)}")
    report.append(f"Всего слов: {len(all_words)}")
    report.append(f"Уникальных слов: {len(unique_words)}")
    
    # Статистика по персонажам
    report.append(f"\n[ПЕРСОНАЖИ И ИХ СЛОВАРЬ]")
    report.append("-"*50)
    
    # Главные персонажи для проверки
    main_characters = {
        'Лир': {'role': 'Король', 'arc': 'власть→безумие→прозрение', 'target': 400},
        'Корделия': {'role': 'Младшая дочь', 'arc': 'правда→изгнание→прощение', 'target': 200},
        'Эдмунд': {'role': 'Бастард', 'arc': 'интрига→власть→падение', 'target': 250},
        'Глостер': {'role': 'Граф', 'arc': 'доверие→прозрение→страдание', 'target': 150},
        'Эдгар': {'role': 'Законный сын', 'arc': 'изгнание→безумие→справедливость', 'target': 150},
        'Гонерилья': {'role': 'Старшая дочь', 'arc': 'лесть→жестокость→гибель', 'target': 100},
        'Регана': {'role': 'Средняя дочь', 'arc': 'лесть→жестокость→гибель', 'target': 100},
        'Кент': {'role': 'Верный граф', 'arc': 'верность→изгнание→возвращение', 'target': 100},
        'Шут': {'role': 'Шут короля', 'arc': 'мудрость→верность→исчезновение', 'target': 150}
    }
    
    for char_name, char_info in main_characters.items():
        if char_name in character_words:
            words = character_words[char_name]
            unique_char_words = list(set([w['word'] for w in words]))
            report.append(f"\n{char_name} ({char_info['role']})")
            report.append(f"  Арка: {char_info['arc']}")
            report.append(f"  Слов сейчас: {len(unique_char_words)} / Цель: {char_info['target']}")
            report.append(f"  Процент готовности: {len(unique_char_words)*100//char_info['target']}%")
            
            # Примеры слов персонажа
            if len(words) > 0:
                report.append(f"  Примеры:")
                for w in words[:3]:
                    report.append(f"    - {w['word']} ({w['translation']})")
                    report.append(f"      \"{w['context']}\"")
        else:
            report.append(f"\n{char_name} ({char_info['role']})")
            report.append(f"  [!] НЕТ В СЛОВАРЕ - нужно добавить {char_info['target']} слов")
    
    # Статистика по локациям
    report.append(f"\n\n[КАРТА ПУТЕШЕСТВИЯ ЛИРА]")
    report.append("-"*50)
    
    journey_order = ['🏰 Замок', '🎭 Интрига', '⛈️ Буря', '🏔️ Дувр', '💝 Примирение', '⚔️ Битва', '⛓️ Тюрьма']
    
    for location in journey_order:
        if location in location_words:
            words = location_words[location]
            unique_loc_words = list(set([w['word'] for w in words]))
            report.append(f"\n{location}: {len(unique_loc_words)} уникальных слов")
            
            # Группируем по файлам
            files_in_location = set([w['file'] for w in words])
            report.append(f"  Сцены ({len(files_in_location)}):")
            for file_name in sorted(files_in_location):
                if file_name in file_data:
                    report.append(f"    - {file_data[file_name]['icon']} {file_name}")
    
    # Эмоциональная карта
    report.append(f"\n\n[ЭМОЦИОНАЛЬНАЯ КАРТА]")
    report.append("-"*50)
    
    top_emotions = sorted(emotion_words.items(), key=lambda x: len(x[1]), reverse=True)[:15]
    for emotion, words in top_emotions:
        report.append(f"{emotion:30} {len(words):3} слов")
    
    # Рекомендации
    report.append(f"\n\n[РЕКОМЕНДАЦИИ ДЛЯ РЕАЛИЗАЦИИ]")
    report.append("="*70)
    
    report.append("\n1. ДОПОЛНИТЬ ПЕРСОНАЖЕЙ:")
    missing_words_total = 0
    for char_name, char_info in main_characters.items():
        current = len(set([w['word'] for w in character_words.get(char_name, [])]))
        needed = char_info['target'] - current
        if needed > 0:
            report.append(f"   - {char_name}: добавить {needed} слов")
            missing_words_total += needed
    
    report.append(f"\n   ИТОГО нужно добавить: {missing_words_total} слов")
    
    report.append("\n2. СТРУКТУРА КАРТ ПЕРСОНАЖЕЙ:")
    report.append("   - Взять существующие {0} уникальных слов".format(len(unique_words)))
    report.append("   - Распределить по персонажам согласно их аркам")
    report.append("   - Добавить недостающие слова из dictionary_b1.py")
    report.append("   - Создать character_maps.json с привязками")
    
    report.append("\n3. ТЕХНИЧЕСКИ:")
    report.append("   - Создать CharacterVocabularyGenerator")
    report.append("   - Обогатить существующие JSON character_voice")
    report.append("   - Сгенерировать HTML страницы по персонажам")
    report.append("   - Добавить навигацию по путешествию Лира")
    
    # Сохраняем отчет
    output_path = Path(r'F:\AiKlientBank\Lir\test\b1_character_analysis.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"[OK] Анализ сохранен в: {output_path}")
    
    # Возвращаем данные для дальнейшего использования
    return {
        'unique_words': len(unique_words),
        'characters': character_words,
        'locations': location_words,
        'emotions': emotion_words,
        'files': file_data
    }

if __name__ == "__main__":
    result = analyze_b1_vocabulary()
    print(f"[INFO] Уникальных слов: {result['unique_words']}")
    print(f"[INFO] Персонажей: {len(result['characters'])}")
    print(f"[INFO] Локаций: {len(result['locations'])}")
