"""
Детальна перевірка вправи в HTML
"""
from pathlib import Path
import re

html_file = Path(r'F:\AiKlientBank\Lir\output\b1\gruppe_5_finale\14_Duel_bratev_B1.html')
content = html_file.read_text(encoding='utf-8')

print("=" * 70)
print("ДЕТАЛЬНИЙ АНАЛІЗ ВПРАВИ В HTML")
print("=" * 70)

# Знаходимо секцію з вправою
if 'УПРАЖНЕНИЕ' in content:
    # Знаходимо початок і кінець секції вправи
    start = content.find('УПРАЖНЕНИЕ')
    # Знаходимо де починається сама вправа
    exercise_start = content.find('<div class="exercise-text">', start)
    
    if exercise_start != -1:
        # Знаходимо кінець тексту вправи
        exercise_end = content.find('</div>', exercise_start)
        
        # Витягуємо текст вправи
        exercise_html = content[exercise_start:exercise_end + 6]
        
        # Очищаємо від HTML тегів для аналізу
        clean_text = re.sub(r'<[^>]+>', '', exercise_html)
        clean_text = clean_text.strip()
        
        print("\n[ТЕКСТ ВПРАВИ В HTML]:")
        print(clean_text[:500])
        
        # Перевіряємо які слова є
        print("\n[СЛОВА В ВПРАВІ]:")
        german_words = ['die Ehre', 'das Duell', 'herausfordern', 'der Zweikampf', 
                       'die Klinge', 'töten', 'sterben', 'gestehen']
        
        for word in german_words:
            if word in exercise_html:
                print(f"  [OK] {word}")
            else:
                print(f"  [!] {word} - ВІДСУТНЄ")
        
        # Перевіряємо формат пропусків
        print("\n[ФОРМАТ ПРОПУСКІВ]:")
        blanks = re.findall(r'<span class="blank"[^>]*>([^<]+)</span>', exercise_html)
        for blank in blanks[:5]:
            print(f"  - {blank}")
    else:
        print("[ERROR] Не знайдено exercise-text!")
else:
    print("[ERROR] Вправи немає в HTML!")

# Порівнюємо з тим що має бути з JSON
import json

json_file = Path(r'F:\AiKlientBank\Lir\data\b1\14_Дуэль_братьев_B1.json')
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

if 'exercise' in data:
    expected_text = data['exercise']['text']
    print("\n[ОЧІКУВАНИЙ ТЕКСТ З JSON]:")
    print(expected_text[:500])
    
    # Перевіряємо чи співпадають
    if expected_text[:100] in content:
        print("\n[OK] Текст з JSON є в HTML!")
    else:
        print("\n[ERROR] Текст з JSON ВІДСУТНІЙ в HTML!")
        print("HTML має інший текст вправи")
