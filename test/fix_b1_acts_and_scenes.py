"""
Исправляем нумерацию B1 уроков:
- Возвращаем правильные АКТЫ согласно структуре пьесы
- Но оставляем номера СЦЕН = номерам уроков (1-15)
"""
import json
from pathlib import Path

# Правильное соответствие уроков актам (но сцены = номера уроков)
CORRECT_STRUCTURE = {
    "01_Тронный_зал_B1.json": {"act": "I", "scene": "1", "title": "ТРОННЫЙ ЗАЛ"},
    "02_Испытание_любви_B1.json": {"act": "I", "scene": "2", "title": "ИСПЫТАНИЕ ЛЮБВИ"},
    "03_Изгнание_Корделии_B1.json": {"act": "I", "scene": "3", "title": "ИЗГНАНИЕ КОРДЕЛИИ"},
    "04_Интрига_Эдмунда_B1.json": {"act": "II", "scene": "4", "title": "ИНТРИГА ЭДМУНДА"},  # АКТ II!
    "05_Обман_Глостера_B1.json": {"act": "II", "scene": "5", "title": "ОБМАН ГЛОСТЕРА"},     # АКТ II!
    "06_Унижение_Лира_B1.json": {"act": "II", "scene": "6", "title": "УНИЖЕНИЕ ЛИРА"},       # АКТ II!
    "07_Буря_и_безумие_B1.json": {"act": "III", "scene": "7", "title": "БУРЯ И БЕЗУМИЕ"},
    "08_Встреча_с_Томом_B1.json": {"act": "III", "scene": "8", "title": "ВСТРЕЧА С ТОМОМ"},
    "09_Ослепление_Глостера_B1.json": {"act": "III", "scene": "9", "title": "ОСЛЕПЛЕНИЕ ГЛОСТЕРА"},
    "10_Дуврские_скалы_B1.json": {"act": "IV", "scene": "10", "title": "ДУВРСКИЕ СКАЛЫ"},
    "11_Примирение_с_Корделией_B1.json": {"act": "IV", "scene": "11", "title": "ПРИМИРЕНИЕ С КОРДЕЛИЕЙ"},
    "12_Прозрение_Лира_B1.json": {"act": "IV", "scene": "12", "title": "ПРОЗРЕНИЕ ЛИРА"},
    "13_Битва_B1.json": {"act": "V", "scene": "13", "title": "БИТВА"},
    "14_Дуэль_братьев_B1.json": {"act": "V", "scene": "14", "title": "ДУЭЛЬ БРАТЬЕВ"},
    "15_Смерть_Корделии_и_Лира_B1.json": {"act": "V", "scene": "15", "title": "ФИНАЛ"}
}

b1_dir = Path(r'F:\AiKlientBank\Lir\data\b1')
updated = 0

print("[INFO] Исправляем акты и сцены в B1 уроках:")
print("=" * 80)

for filename, correct_info in CORRECT_STRUCTURE.items():
    file_path = b1_dir / filename
    
    if not file_path.exists():
        print(f"[ERROR] Файл не найден: {filename}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    old_title = data.get('title', '')
    
    # Формируем правильный заголовок
    new_title = f"🎭 АКТ {correct_info['act']}, СЦЕНА {correct_info['scene']}: {correct_info['title']}"
    
    if old_title != new_title:
        data['title'] = new_title
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] {filename}")
        print(f"     OLD: {old_title}")
        print(f"     NEW: {new_title}")
        updated += 1
    else:
        print(f"[SKIP] {filename} - уже корректно")

print("=" * 80)
print(f"[DONE] Обновлено файлов: {updated}")
