"""
Діагностика проблеми з вправами
"""
import json
from pathlib import Path

# Перевіряємо JSON
json_file = Path(r'F:\AiKlientBank\Lir\data\b1\14_Дуэль_братьев_B1.json')
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 70)
print("ДІАГНОСТИКА ПРОБЛЕМИ З ВПРАВАМИ")
print("=" * 70)

print("\n[1] JSON ФАЙЛ:")
if 'exercise' in data:
    exercise = data['exercise']
    print(f"  [OK] Має вправу")
    print(f"  Заголовок: {exercise.get('title', 'Немає')}")
    print(f"  Текст: {exercise.get('text', '')[:150]}...")
    print(f"  Відповіді: {list(exercise.get('answers', {}).keys())[:5]}")
else:
    print("  [ERROR] НЕ має вправи!")

# Перевіряємо HTML
html_file = Path(r'F:\AiKlientBank\Lir\output\b1\gruppe_5_finale\14_Duel_bratev_B1.html')

print("\n[2] HTML ФАЙЛ:")
if html_file.exists():
    content = html_file.read_text(encoding='utf-8')
    
    # Шукаємо маркери вправи
    exercise_found = False
    markers = {
        'УПРАЖНЕНИЕ': 'Заголовок вправи',
        'exercise-container': 'Контейнер вправи',
        'show-answer-btn': 'Кнопка відповідей',
        'Das ist ___': 'Текст вправи',
        'die Ehre': 'Слово з вправи'
    }
    
    for marker, description in markers.items():
        if marker in content:
            print(f"  [OK] Знайдено: {description}")
            exercise_found = True
        else:
            print(f"  [!] НЕ знайдено: {description}")
    
    if not exercise_found:
        print("\n  [ERROR] ВПРАВА НЕ ВІДОБРАЖАЄТЬСЯ В HTML!")
    
    # Рахуємо секції
    sections = content.count('<section')
    print(f"\n  Кількість секцій: {sections}")
    
    # Які секції є
    section_titles = ['Словарь сцены', 'Театральный момент', 'Диалоги персонажей', 'Шпаргалка', 'УПРАЖНЕНИЕ']
    for title in section_titles:
        if title in content:
            print(f"  [+] {title}")
        else:
            print(f"  [-] {title}")
else:
    print("  [ERROR] Файл не існує!")

print("\n[3] ВИСНОВОК:")
if exercise_found:
    print("  Вправа відображається в HTML")
else:
    print("  ПРОБЛЕМА: Генератор НЕ додає вправи в HTML!")
    print("  Потрібно виправити json_generator.py")
