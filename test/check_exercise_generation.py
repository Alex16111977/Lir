"""
Тест для перевірки генерації вправи з пропусками
"""
import json
import re
import sys
from pathlib import Path

# Додаємо шлях до проекту
sys.path.insert(0, str(Path(__file__).parent.parent))

# Завантажуємо JSON
json_path = Path(r'F:\AiKlientBank\Lir\data\b1\15_Смерть_Корделии_и_Лира_B1.json')
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("[1] CHECKING ORIGINAL JSON DATA")
print("-" * 50)

exercise = data.get('exercise', {})
text = exercise.get('text', '')
answers = exercise.get('answers', {})

print(f"Answers in JSON: {answers}")
print()

# Шукаємо проблемні місця
for hint, answer in answers.items():
    pattern = f"___ ({hint})"
    if pattern in text:
        print(f"[OK] Found pattern: {pattern}")
        # Знаходимо контекст
        idx = text.find(pattern)
        context = text[max(0, idx-30):idx+30]
        print(f"     Context: ...{context}...")
    else:
        print(f"[ERROR] Pattern not found: {pattern}")

print("\n[2] CHECKING FOR ASTERISKS")
print("-" * 50)

if '****' in text:
    print("[ERROR] Found asterisks in exercise text!")
    idx = text.find('****')
    fragment = text[max(0, idx-20):idx+50]
    print(f"Fragment: {repr(fragment)}")
else:
    print("[OK] No asterisks in exercise text")

print("\n[3] SIMULATING HTML GENERATION")
print("-" * 50)

# Симулюємо генерацію HTML
exercise_text = text

# Обробляємо пропуски
for hint, answer in answers.items():
    html_blank = f'<span class="blank" data-hint="{hint}" data-answer="{answer}">_______ ({hint})</span>'
    
    # Екрануємо спеціальні символи
    escaped_hint = re.escape(hint)
    
    # Шаблон для заміни в story-highlight тегах
    pattern1 = rf'(<span class="story-highlight">[^<]*?)___ \({escaped_hint}\)([^<]*?</span>)'
    
    print(f"\nProcessing hint: {hint}")
    print(f"Pattern: {pattern1}")
    
    # Перевіряємо чи знаходить патерн
    matches = re.findall(pattern1, text)
    if matches:
        print(f"  Found {len(matches)} matches")
        exercise_text = re.sub(pattern1, rf'\1{html_blank}\2', exercise_text)
    else:
        print(f"  No matches found!")
        # Спробуємо простіший патерн
        simple_pattern = rf'___ \({escaped_hint}\)'
        if re.search(simple_pattern, text):
            print(f"  Found with simple pattern!")
            exercise_text = re.sub(simple_pattern, html_blank, exercise_text)

print("\n[4] RESULT CHECK")
print("-" * 50)

# Перевіряємо результат
if 'смерть' in exercise_text:
    idx = exercise_text.find('смерть')
    fragment = exercise_text[max(0, idx-100):idx+50]
    print(f"Fragment around 'смерть':")
    print(fragment)
    
    if '****' in fragment:
        print("\n[ERROR] Asterisks still present in result!")
    elif '<span class="blank"' in fragment:
        print("\n[OK] Blank span created correctly!")
    else:
        print("\n[WARNING] No blank span found!")

# Зберігаємо результат для перевірки
output_path = Path(r'F:\AiKlientBank\Lir\test\exercise_test.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"""
<html>
<head>
    <meta charset="utf-8">
    <style>
        .story-highlight {{ background: yellow; }}
        .blank {{ color: red; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>Test Exercise</h1>
    <div>{exercise_text}</div>
</body>
</html>
""")

print(f"\n[5] HTML saved to: {output_path}")
print("Open it to check the result!")
