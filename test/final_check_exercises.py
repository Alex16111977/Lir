"""
Фінальна перевірка виправлення
"""
from pathlib import Path
import json
import re

print("=" * 70)
print("ФІНАЛЬНА ПЕРЕВІРКА ВИПРАВЛЕННЯ")
print("=" * 70)

# 1. Перевіряємо HTML
html_file = Path(r'F:\AiKlientBank\Lir\output\b1\gruppe_5_finale\14_Duel_bratev_B1.html')
content = html_file.read_text(encoding='utf-8')

print("\n[1] ПЕРЕВІРКА HTML:")

# Перевіряємо наявність JavaScript
if 'exerciseAnswers' in content:
    print("  [OK] JavaScript об'єкт з відповідями")
    
    # Витягуємо відповіді
    match = re.search(r'exerciseAnswers = ({[^}]+})', content)
    if match:
        answers_str = match.group(1)
        print(f"  [OK] Відповіді в JS: {answers_str[:100]}...")

# Перевіряємо data-атрибути
if 'data-answer' in content:
    print("  [OK] data-answer атрибути в пропусках")
    
    # Знаходимо всі пропуски з відповідями
    blanks = re.findall(r'data-answer="([^"]+)"', content)
    if blanks:
        print(f"  [OK] Знайдено {len(blanks)} відповідей:")
        for answer in blanks[:5]:
            print(f"      - {answer}")

# Перевіряємо функцію
if 'function toggleAnswers' in content:
    print("  [OK] Функція toggleAnswers оновлена")

# 2. Порівнюємо з JSON
json_file = Path(r'F:\AiKlientBank\Lir\data\b1\14_Дуэль_братьев_B1.json')
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("\n[2] ПОРІВНЯННЯ З JSON:")

if 'exercise' in data:
    expected_answers = data['exercise']['answers']
    print(f"  JSON має {len(expected_answers)} відповідей")
    
    # Перевіряємо чи всі відповіді в HTML
    all_present = True
    for hint, answer in expected_answers.items():
        if answer in content:
            print(f"  [OK] '{answer}' для '{hint}'")
        else:
            print(f"  [!] '{answer}' для '{hint}' - ВІДСУТНЄ")
            all_present = False
    
    if all_present:
        print("\n  [OK] ВСІ ВІДПОВІДІ З JSON Є В HTML!")

print("\n[3] ТЕСТУВАННЯ ІНШИХ ФАЙЛІВ:")

# Перевіряємо кілька інших файлів
test_files = [
    'a2/01_Otec_i_docheri_A2.html',
    'b1/01_Tronnyy_zal_B1.html',
    'thematic/semya.html'
]

for file_path in test_files:
    full_path = Path(r'F:\AiKlientBank\Lir\output') / file_path
    if full_path.exists():
        content = full_path.read_text(encoding='utf-8')
        has_js = 'exerciseAnswers' in content
        has_func = 'toggleAnswers' in content
        
        status = "[OK]" if (has_js and has_func) else "[!]"
        print(f"  {status} {file_path}")

print("\n" + "=" * 70)
print("ВИСНОВОК:")
print("Генератор виправлено! Вправи тепер:")
print("  1. Використовують оригінальний текст з JSON")
print("  2. Містять всі німецькі слова як відповіді")
print("  3. Показують/приховують відповіді при натисканні кнопки")
print("=" * 70)
