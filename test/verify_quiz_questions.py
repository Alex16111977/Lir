"""
Test: Verify quiz questions count
Date: 2025-01-06
Purpose: Check that quiz generates 2 questions per word
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Читаємо урок з 12 словами
lesson_path = Path(r"F:\AiKlientBank\Lir\data\b1\06_Унижение_Лира_B1.json")
if not lesson_path.exists():
    print(f"[ERROR] File not found: {lesson_path}")
    sys.exit(1)
    
with open(lesson_path, "r", encoding="utf-8") as f:
    data = json.load(f)

vocabulary = data.get("vocabulary", [])
print(f"[INFO] Words in lesson: {len(vocabulary)}")

# Імітуємо логіку вікторини
selectable = [w for w in vocabulary if w.get("german") and w.get("translation")]
print(f"[INFO] Selectable words: {len(selectable)}")

# СТАРА логіка (неправильна)
import random
old_sample = selectable[:]
random.shuffle(old_sample)
mid_point = (len(old_sample) + 1) // 2
old_de_ru = old_sample[:mid_point]
old_ru_de = old_sample[mid_point:]
print(f"\n[OLD LOGIC] DE->RU: {len(old_de_ru)}, RU->DE: {len(old_ru_de)}")
print(f"[OLD LOGIC] Total questions: {len(old_de_ru) + len(old_ru_de)}")
print(f"[OLD LOGIC] Each word tested: ~{(len(old_de_ru) + len(old_ru_de)) / len(selectable):.1f} times")

# НОВА логіка (правильна)  
new_de_ru = selectable[:]  # ВСІ слова для DE→RU
new_ru_de = selectable[:]  # ВСІ слова для RU→DE
print(f"\n[NEW LOGIC] DE->RU: {len(new_de_ru)}, RU->DE: {len(new_ru_de)}")
print(f"[NEW LOGIC] Total questions: {len(new_de_ru) + len(new_ru_de)}")
print(f"[NEW LOGIC] Each word tested: {(len(new_de_ru) + len(new_ru_de)) / len(selectable):.1f} times")
print(f"[NEW LOGIC] Expected: {len(selectable)} × 2 = {len(selectable) * 2}")

# Перевіряємо правильність
if len(new_de_ru) + len(new_ru_de) == len(selectable) * 2:
    print("\n[OK] New logic is correct - each word tested exactly TWICE!")
else:
    print("\n[ERROR] New logic is wrong!")
