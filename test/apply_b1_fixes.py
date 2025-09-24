"""
Применяем исправления нумерации актов и сцен в B1 уроках
"""
import json
from pathlib import Path

# Правильная структура
CORRECT_STRUCTURE = {
    "01_Тронный_зал_B1.json": {"act": "I", "scene": "1", "title": "ТРОННЫЙ ЗАЛ"},
    "02_Испытание_любви_B1.json": {"act": "I", "scene": "1", "title": "ИСПЫТАНИЕ ЛЮБВИ"},
    "03_Изгнание_Корделии_B1.json": {"act": "I", "scene": "1", "title": "ИЗГНАНИЕ КОРДЕЛИИ"},
    "04_Интрига_Эдмунда_B1.json": {"act": "I", "scene": "2", "title": "ИНТРИГА ЭДМУНДА"},
    "05_Обман_Глостера_B1.json": {"act": "I", "scene": "2", "title": "ОБМАН ГЛОСТЕРА"},
    "06_Унижение_Лира_B1.json": {"act": "I", "scene": "4", "title": "УНИЖЕНИЕ ЛИРА"},
    "07_Буря_и_безумие_B1.json": {"act": "III", "scene": "2", "title": "БУРЯ И БЕЗУМИЕ"},
    "08_Встреча_с_Томом_B1.json": {"act": "III", "scene": "4", "title": "ВСТРЕЧА С ТОМОМ"},
    "09_Ослепление_Глостера_B1.json": {"act": "III", "scene": "7", "title": "ОСЛЕПЛЕНИЕ ГЛОСТЕРА"},
    "10_Дуврские_скалы_B1.json": {"act": "IV", "scene": "6", "title": "ДУВРСКИЕ СКАЛЫ"},
    "11_Примирение_с_Корделией_B1.json": {"act": "IV", "scene": "7", "title": "ПРИМИРЕНИЕ С КОРДЕЛИЕЙ"},
    "12_Прозрение_Лира_B1.json": {"act": "IV", "scene": "6", "title": "ПРОЗРЕНИЕ ЛИРА"},
    "13_Битва_B1.json": {"act": "V", "scene": "2", "title": "БИТВА"},
    "14_Дуэль_братьев_B1.json": {"act": "V", "scene": "3", "title": "ДУЭЛЬ БРАТЬЕВ"},
    "15_Смерть_Корделии_и_Лира_B1.json": {"act": "V", "scene": "3", "title": "ФИНАЛ"}
}

b1_dir = Path(r'F:\AiKlientBank\Lir\data\b1')
updated_count = 0

print("[INFO] Применяем исправления для B1 уроков...")
print("=" * 80)

for filename, correct_info in CORRECT_STRUCTURE.items():
    file_path = b1_dir / filename
    
    if not file_path.exists():
        print(f"[ERROR] Файл не найден: {filename}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    old_title = data.get('title', '')
    new_title = f"🎭 АКТ {correct_info['act']}, СЦЕНА {correct_info['scene']}: {correct_info['title']}"
    
    if old_title != new_title:
        data['title'] = new_title
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] {filename}")
        print(f"     OLD: {old_title}")
        print(f"     NEW: {new_title}")
        updated_count += 1
    else:
        print(f"[SKIP] {filename} - уже корректно")

print("=" * 80)
print(f"[DONE] Обновлено файлов: {updated_count}")
