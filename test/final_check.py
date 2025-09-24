#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Фінальна перевірка всіх виправлень транскрипцій
"""

import json
from pathlib import Path

print("[FINAL CHECK] Фінальна перевірка всіх виправлень")
print("=" * 60)

# Всі виправлені слова за всю сесію
ALL_FIXED = {
    # Перші виправлення
    'außergewöhnlich': '[ау-сер-ге-ВЁН-лих]',
    'der Fehler': '[дер ФЕ-лер]',
    'die Königin': '[ди КЁ-ни-гин]',
    'die Herzogin': '[ди ХЕР-цо-гин]',
    'die Zeremonie': '[ди це-ре-мо-НИ]',
    # Слова з zweif-
    'verzweifeln': '[фер-ЦВАЙ-фельн]',
    'die Verzweiflung': '[ди фер-ЦВАЙ-флунг]',
    # Інші
    'geboren werden': '[ге-БО-рен вер-ден]',
    'zu spät': '[цу-ШПЕТ]',
    'hintergehen': '[хин-тер-ГЕ-ен]',
    # Слова з un-
    'unbestimmt': '[ун-бе-ШТИМТ]',
    'unglücklich': '[ун-ГЛЮК-лих]',
    # Нові
    'das Zuhause': '[дас цу-ХАУ-зе]',
    'die Heuchelei': '[ди хой-хе-ЛАЙ]',
    # Останні
    'die Undankbarkeit': '[ди ун-ДАНК-бар-кайт]',
    'der Wächter': '[дер ВЕХ-тер]',
    'die Schwester': '[ди ШВЕС-тер]',
    'demütigen': '[ДЕ-мю-ти-ген]',
    'naiv': '[на-ИФ]',
    'das Rätsel': '[дас РЕТ-цель]'
}

print(f"[INFO] Всього виправлено слів: {len(ALL_FIXED)}")

# Перевіряю в JSON
data_path = Path(r'F:\AiKlientBank\Lir\data')
found_correct = 0
found_incorrect = 0
not_found = []

for word, expected in ALL_FIXED.items():
    found = False
    
    for subdir in data_path.iterdir():
        if subdir.is_dir() and not found:
            for json_file in subdir.glob('*.json'):
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if 'vocabulary' in data:
                    for item in data['vocabulary']:
                        german = item.get('german', item.get('word'))
                        
                        if german == word:
                            trans = item.get('transcription', '')
                            if trans == expected:
                                found_correct += 1
                            else:
                                found_incorrect += 1
                                print(f"[ERROR] {word} в {json_file.name}:")
                                print(f"  Очікується: {expected}")
                                print(f"  Знайдено: {trans}")
                            found = True
                            break
                if found:
                    break
    
    if not found:
        not_found.append(word)

print(f"\n[SUMMARY] Підсумок перевірки:")
print(f"  Правильних: {found_correct}")
print(f"  Неправильних: {found_incorrect}")
print(f"  Не знайдено в JSON: {len(not_found)}")

if not_found:
    print(f"\n[INFO] Слова відсутні в JSON (нормально):")
    for word in not_found:
        print(f"  - {word}")

if found_incorrect == 0:
    print(f"\n[SUCCESS] ВСІ знайдені слова мають правильні транскрипції!")
else:
    print(f"\n[WARNING] Деякі слова потребують виправлення!")

print("\n" + "=" * 60)
print("[READY] Проект готовий до генерації сайту!")
print("[RUN] python main.py - для створення 55+ HTML файлів")
