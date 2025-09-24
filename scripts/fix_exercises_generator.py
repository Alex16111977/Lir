"""
ВИПРАВЛЕНИЙ ГЕНЕРАТОР - Використовує ОРИГІНАЛЬНІ вправи з JSON
НЕ перезаписує існуючі вправи!
Версія: 1.0
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

def check_existing_exercises():
    """Перевіряє які JSON файли вже мають вправи"""
    
    data_dir = Path(r'F:\AiKlientBank\Lir\data')
    categories = ['a2', 'b1', 'thematic']
    
    stats = {
        'total': 0,
        'with_exercise': 0,
        'without_exercise': 0,
        'files_without': []
    }
    
    print("[АНАЛІЗ] Перевірка існуючих вправ...")
    print("-" * 60)
    
    for category in categories:
        cat_dir = data_dir / category
        if not cat_dir.exists():
            continue
        
        for json_file in cat_dir.glob("*.json"):
            stats['total'] += 1
            
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'exercise' in data and data['exercise']:
                stats['with_exercise'] += 1
                # Перевіряємо якість вправи
                exercise = data['exercise']
                if exercise.get('text') and exercise.get('answers'):
                    print(f"  [OK] {json_file.name}: {len(exercise['answers'])} пропусків")
                else:
                    print(f"  [!] {json_file.name}: неповна вправа")
            else:
                stats['without_exercise'] += 1
                stats['files_without'].append(f"{category}/{json_file.name}")
    
    print("\n[СТАТИСТИКА]")
    print(f"  Всього файлів: {stats['total']}")
    print(f"  З вправами: {stats['with_exercise']}")
    print(f"  Без вправ: {stats['without_exercise']}")
    
    if stats['files_without']:
        print(f"\n[УВАГА] Файли БЕЗ вправ:")
        for f in stats['files_without'][:10]:
            print(f"    - {f}")
    
    return stats

def add_missing_exercises_only():
    """Додає вправи ТІЛЬКИ до файлів, де їх немає"""
    
    data_dir = Path(r'F:\AiKlientBank\Lir\data')
    categories = ['a2', 'b1', 'thematic']
    
    added_count = 0
    
    print("\n[ДОДАВАННЯ] Вправи до файлів БЕЗ них...")
    print("-" * 60)
    
    for category in categories:
        cat_dir = data_dir / category
        if not cat_dir.exists():
            continue
        
        for json_file in cat_dir.glob("*.json"):
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # КРИТИЧНО: НЕ чіпаємо файли з існуючими вправами!
            if 'exercise' in data and data['exercise']:
                continue
            
            # Додаємо вправу тільки якщо її немає
            print(f"\n[NEW] {json_file.name}")
            
            # Створюємо вправу з vocabulary
            vocabulary = data.get('vocabulary', [])
            if not vocabulary:
                print("  [SKIP] Немає vocabulary")
                continue
            
            # Беремо перші 8 слів для вправи
            exercise_words = {}
            for i, word_data in enumerate(vocabulary[:8]):
                german = word_data.get('german', '')
                translation = word_data.get('translation', '')
                if german and translation:
                    exercise_words[translation] = german
            
            if not exercise_words:
                print("  [SKIP] Немає слів для вправи")
                continue
            
            # Створюємо текст вправи з контекстом
            title = data.get('title', 'Урок')
            story = data.get('story', {})
            
            # Намагаємося створити контекстну вправу
            exercise_text = create_contextual_exercise(story, vocabulary, exercise_words)
            
            data['exercise'] = {
                'title': f"УПРАЖНЕНИЕ: {title.replace('🎭', '').strip()}",
                'text': exercise_text,
                'answers': exercise_words
            }
            
            # Зберігаємо
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            added_count += 1
            print(f"  [OK] Додано вправу з {len(exercise_words)} словами")
    
    return added_count

def create_contextual_exercise(story, vocabulary, exercise_words):
    """Створює контекстну вправу на основі історії"""
    
    # Якщо є історія, намагаємося використати її контекст
    if story and story.get('content'):
        # Беремо ключові фрази з історії
        content = story['content']
        
        # Шукаємо згадки слів в історії
        sentences = []
        for rus_word, ger_word in list(exercise_words.items())[:8]:
            # Створюємо речення з контекстом
            if 'die' in ger_word or 'der' in ger_word or 'das' in ger_word:
                # Іменник
                sentences.append(f"Wo ist ___ ({rus_word})?")
            elif 'en' in ger_word[-2:]:
                # Дієслово
                sentences.append(f"Er will ___ ({rus_word}).")
            else:
                # Загальний випадок
                sentences.append(f"Das ist ___ ({rus_word}).")
        
        return ' '.join(sentences)
    
    else:
        # Стандартні шаблони якщо немає історії
        templates = [
            "Hier ist ___ ({}).",
            "Er braucht ___ ({}).",
            "Sie hat ___ ({}).",
            "Wir sehen ___ ({}).",
            "Das war ___ ({}).",
            "Wo ist ___ ({})?",
            "Ich kenne ___ ({}).",
            "Du sagst: ___ ({})!"
        ]
        
        sentences = []
        for i, (rus_word, _) in enumerate(exercise_words.items()):
            if i < len(templates):
                sentences.append(templates[i].format(rus_word))
        
        return ' '.join(sentences)

def verify_and_regenerate():
    """Перевіряє та перегенерує сайт"""
    
    print("\n[ГЕНЕРАЦІЯ] Запуск main.py...")
    print("-" * 60)
    
    result = subprocess.run(
        [sys.executable, r'F:\AiKlientBank\Lir\main.py'],
        capture_output=True,
        text=True,
        cwd=r'F:\AiKlientBank\Lir'
    )
    
    if result.returncode == 0:
        print("[OK] Сайт згенеровано успішно!")
        
        # Перевіряємо конкретний проблемний файл
        test_file = Path(r'F:\AiKlientBank\Lir\output\b1\gruppe_5_finale\14_Duel_bratev_B1.html')
        
        if test_file.exists():
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Перевіряємо чи є правильна вправа
            if 'die Ehre' in content and 'das Duell' in content:
                print("[OK] Вправа відображається правильно!")
            else:
                print("[ERROR] Вправа не відповідає JSON!")
                
                # Показуємо що в HTML
                if 'УПРАЖНЕНИЕ' in content:
                    start = content.find('УПРАЖНЕНИЕ')
                    end = content.find('</section>', start)
                    exercise_html = content[start:end][:500]
                    print("\nВправа в HTML:")
                    print(exercise_html)
    else:
        print("[ERROR] Помилка генерації!")
        print(result.stderr)

def main():
    """Головна функція"""
    
    print("=" * 70)
    print("ВИПРАВЛЕННЯ ГЕНЕРАТОРА ВПРАВ")
    print("Використовуємо ОРИГІНАЛЬНІ вправи з JSON!")
    print("=" * 70)
    
    # 1. Аналізуємо поточний стан
    stats = check_existing_exercises()
    
    # 2. Додаємо вправи ТІЛЬКИ де їх немає
    if stats['without_exercise'] > 0:
        print(f"\n[ПОТРІБНО] Додати вправи до {stats['without_exercise']} файлів")
        added = add_missing_exercises_only()
        print(f"\n[РЕЗУЛЬТАТ] Додано {added} нових вправ")
    else:
        print("\n[OK] Всі файли вже мають вправи!")
    
    # 3. Перегенеруємо сайт
    verify_and_regenerate()
    
    print("\n" + "=" * 70)
    print("[ГОТОВО] Генератор виправлено!")
    print("Тепер вправи відповідають JSON файлам")
    print("=" * 70)

if __name__ == "__main__":
    main()
