#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Анализ и классификация дополнительных слов для проекта Lir
Классификация по уровням A2/B1 и тематикам
Дата: 06.09.2025
"""

import json
from pathlib import Path
import sys

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from full_stress_dictionary_v2 import FULL_STRESS_DICTIONARY

def classify_extra_words():
    """Классификация слов из словаря, которых нет в JSON"""
    
    # Собираем слова из JSON
    json_words = set()
    data_dir = project_root / 'data'
    
    for json_file in data_dir.glob('**/*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'vocabulary' in data:
                    for word_entry in data['vocabulary']:
                        german = word_entry.get('german', '').strip()
                        if german:
                            json_words.add(german)
        except:
            pass
    
    # Находим дополнительные слова
    extra_words = set(FULL_STRESS_DICTIONARY.keys()) - json_words
    
    # Классификация слов по уровням и тематикам
    classification = {
        'A2': {
            'Семья и отношения': [],
            'Дом и быт': [],
            'Чувства и эмоции': [],
            'Время и место': [],
            'Базовые действия': [],
            'Описания': []
        },
        'B1': {
            'Власть и политика': [],
            'Война и конфликт': [],
            'Мораль и этика': [],
            'Природа и стихии': [],
            'Абстрактные понятия': [],
            'Сложные действия': [],
            'Характер и личность': []
        }
    }
    
    # Правила классификации
    a2_keywords = {
        'Семья и отношения': ['Vater', 'Mutter', 'Kind', 'Bruder', 'Schwester', 'Familie', 'Eltern', 'Sohn', 'Tochter', 'heiraten', 'lieben'],
        'Дом и быт': ['Haus', 'Fenster', 'Tür', 'Zimmer', 'Bett', 'Tisch', 'essen', 'trinken', 'schlafen', 'wohnen', 'Zuhause'],
        'Чувства и эмоции': ['froh', 'traurig', 'glücklich', 'weinen', 'lachen', 'Freude', 'Angst', 'mögen', 'lustig'],
        'Время и место': ['heute', 'morgen', 'gestern', 'jetzt', 'hier', 'dort', 'früh', 'spät', 'alt', 'neu', 'jung'],
        'Базовые действия': ['gehen', 'kommen', 'sehen', 'hören', 'sprechen', 'lesen', 'schreiben', 'arbeiten', 'spielen'],
        'Описания': ['groß', 'klein', 'gut', 'schlecht', 'schön', 'hässlich', 'warm', 'kalt', 'hell', 'dunkel', 'dick', 'dünn']
    }
    
    b1_keywords = {
        'Власть и политика': ['König', 'Herrscher', 'Reich', 'Thron', 'Macht', 'regieren', 'befehlen', 'Adel', 'Herzog', 'Graf'],
        'Война и конфликт': ['Krieg', 'Kampf', 'Schlacht', 'Schwert', 'Armee', 'siegen', 'kämpfen', 'Feind', 'Frieden'],
        'Мораль и этика': ['Ehre', 'Pflicht', 'Gerechtigkeit', 'Verrat', 'Treue', 'Schuld', 'Sünde', 'vergeben', 'bereuen'],
        'Природа и стихии': ['Sturm', 'Donner', 'Blitz', 'Regen', 'Wind', 'Unwetter', 'Chaos', 'überfluten'],
        'Абстрактные понятия': ['Schicksal', 'Vernunft', 'Wahnsinn', 'Wahrheit', 'Lüge', 'Geheimnis', 'Rätsel', 'Ewigkeit'],
        'Сложные действия': ['verraten', 'verschwören', 'verteidigen', 'vernichten', 'verzweifeln', 'verstellen', 'täuschen'],
        'Характер и личность': ['hochmütig', 'demütig', 'grausam', 'gnädig', 'wahnsinnig', 'weise', 'verrückt', 'edel']
    }
    
    # Классифицируем каждое слово
    for word in sorted(extra_words):
        classified = False
        word_lower = word.lower()
        
        # Проверяем A2 категории
        for category, keywords in a2_keywords.items():
            for keyword in keywords:
                if keyword.lower() in word_lower or word_lower in keyword.lower():
                    classification['A2'][category].append(f"{word} {FULL_STRESS_DICTIONARY[word]}")
                    classified = True
                    break
            if classified:
                break
        
        # Если не классифицировано как A2, проверяем B1
        if not classified:
            for category, keywords in b1_keywords.items():
                for keyword in keywords:
                    if keyword.lower() in word_lower or word_lower in keyword.lower():
                        classification['B1'][category].append(f"{word} {FULL_STRESS_DICTIONARY[word]}")
                        classified = True
                        break
                if classified:
                    break
        
        # Дополнительная классификация по структуре слова
        if not classified:
            # Простые короткие слова - обычно A2
            if len(word) <= 6 and not any(prefix in word for prefix in ['ver', 'be', 'ent', 'er', 'zer']):
                # Определяем категорию по типу слова
                if word.startswith('der ') or word.startswith('die ') or word.startswith('das '):
                    classification['A2']['Описания'].append(f"{word} {FULL_STRESS_DICTIONARY[word]}")
                else:
                    classification['A2']['Базовые действия'].append(f"{word} {FULL_STRESS_DICTIONARY[word]}")
            # Сложные слова с префиксами - обычно B1
            else:
                if word.startswith('der ') or word.startswith('die ') or word.startswith('das '):
                    classification['B1']['Абстрактные понятия'].append(f"{word} {FULL_STRESS_DICTIONARY[word]}")
                else:
                    classification['B1']['Сложные действия'].append(f"{word} {FULL_STRESS_DICTIONARY[word]}")
    
    # Выводим результаты
    print("=" * 80)
    print("КЛАССИФИКАЦИЯ ДОПОЛНИТЕЛЬНЫХ СЛОВ ДЛЯ ПРОЕКТА LIR")
    print("=" * 80)
    print(f"\nВсего дополнительных слов: {len(extra_words)}")
    print("(Эти слова есть в словаре транскрипций, но отсутствуют в учебных материалах)")
    
    # Подсчет по уровням
    a2_total = sum(len(words) for words in classification['A2'].values())
    b1_total = sum(len(words) for words in classification['B1'].values())
    
    print(f"\nРаспределение по уровням:")
    print(f"  A2: {a2_total} слов")
    print(f"  B1: {b1_total} слов")
    
    # Детальный вывод
    for level in ['A2', 'B1']:
        print(f"\n{'=' * 80}")
        print(f"УРОВЕНЬ {level}")
        print('=' * 80)
        
        for category, words in classification[level].items():
            if words:
                print(f"\n{category} ({len(words)} слов):")
                print("-" * 60)
                for word in words[:10]:  # Показываем первые 10 слов
                    print(f"  • {word}")
                if len(words) > 10:
                    print(f"  ... и еще {len(words) - 10} слов")
    
    # Сохраняем полный отчет
    report_path = project_root / 'test' / 'extra_words_classification.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("КЛАССИФИКАЦИЯ ДОПОЛНИТЕЛЬНЫХ СЛОВ ДЛЯ ПРОЕКТА LIR\n")
        f.write("=" * 80 + "\n")
        f.write(f"Дата: 06.09.2025\n")
        f.write(f"Всего дополнительных слов: {len(extra_words)}\n")
        f.write(f"Уровень A2: {a2_total} слов\n")
        f.write(f"Уровень B1: {b1_total} слов\n")
        f.write("\n" + "=" * 80 + "\n")
        
        for level in ['A2', 'B1']:
            f.write(f"\nУРОВЕНЬ {level}\n")
            f.write("=" * 80 + "\n")
            
            for category, words in classification[level].items():
                if words:
                    f.write(f"\n{category} ({len(words)} слов):\n")
                    f.write("-" * 60 + "\n")
                    for word in words:
                        f.write(f"  • {word}\n")
    
    print(f"\n[OK] Полный отчет сохранен: {report_path}")
    
    # Создаем рекомендации для добавления в учебные материалы
    print("\n" + "=" * 80)
    print("РЕКОМЕНДАЦИИ ДЛЯ РАСШИРЕНИЯ УЧЕБНЫХ МАТЕРИАЛОВ")
    print("=" * 80)
    
    print("\nПриоритетные слова для добавления в уровень A2:")
    priority_a2 = [
        "allein [а-ЛАЙН] - один, одинокий",
        "alt [АЛЬТ] - старый",
        "heute [ХОЙ-те] - сегодня",
        "jetzt [ЙЕТЦТ] - сейчас",  
        "morgen [МОР-ген] - завтра",
        "kommen [КО-мен] - приходить",
        "sehen [ЗЕ-ен] - видеть",
        "sprechen [ШПРЕ-хен] - говорить",
        "groß [ГРОС] - большой",
        "klein [КЛАЙН] - маленький"
    ]
    
    for word in priority_a2:
        print(f"  • {word}")
    
    print("\nПриоритетные слова для добавления в уровень B1:")
    priority_b1 = [
        "der Kampf [дер КАМПФ] - борьба",
        "der Krieg [дер КРИГ] - война",
        "die Schlacht [ди ШЛАХТ] - битва",
        "die Pflicht [ди ПФЛИХТ] - долг",
        "die Vernunft [ди фер-НУНФТ] - разум",
        "kämpfen [КЕМП-фен] - бороться",
        "siegen [ЗИ-ген] - побеждать",
        "täuschen [ТОЙ-шен] - обманывать",
        "grausam [ГРАУ-зам] - жестокий",
        "mächtig [МЕХ-тиг] - могущественный"
    ]
    
    for word in priority_b1:
        print(f"  • {word}")
    
    return classification, extra_words

if __name__ == "__main__":
    classification, extra_words = classify_extra_words()
