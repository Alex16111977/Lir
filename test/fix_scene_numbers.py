"""
Исправляем нумерацию сцен в B1 уроках
Номер сцены = номер урока (1-15)
"""
import json
from pathlib import Path

# Мапинг: номер урока -> корректный номер сцены
SCENE_NUMBERS = {
    "01_Тронный_зал_B1.json": "1",
    "02_Испытание_любви_B1.json": "2", 
    "03_Изгнание_Корделии_B1.json": "3",
    "04_Интрига_Эдмунда_B1.json": "4",
    "05_Обман_Глостера_B1.json": "5",
    "06_Унижение_Лира_B1.json": "6",
    "07_Буря_и_безумие_B1.json": "7",  # Было СЦЕНА 2, станет СЦЕНА 7
    "08_Встреча_с_Томом_B1.json": "8",  # Было СЦЕНА 4, станет СЦЕНА 8
    "09_Ослепление_Глостера_B1.json": "9",  # Было СЦЕНА 7, станет СЦЕНА 9
    "10_Дуврские_скалы_B1.json": "10",
    "11_Примирение_с_Корделией_B1.json": "11",
    "12_Прозрение_Лира_B1.json": "12",
    "13_Битва_B1.json": "13",  # Было СЦЕНА 2, станет СЦЕНА 13
    "14_Дуэль_братьев_B1.json": "14",  # Было СЦЕНА 3, станет СЦЕНА 14
    "15_Смерть_Корделии_и_Лира_B1.json": "15"  # Было СЦЕНА 3, станет СЦЕНА 15
}

b1_dir = Path(r'F:\AiKlientBank\Lir\data\b1')
updated = 0

print("[INFO] Обновляем номера сцен (1-15):")
print("=" * 80)

for filename, scene_num in SCENE_NUMBERS.items():
    file_path = b1_dir / filename
    
    if not file_path.exists():
        print(f"[ERROR] Файл не найден: {filename}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    old_title = data.get('title', '')
    
    # Извлекаем акт и название
    if 'АКТ' in old_title:
        parts = old_title.split(',')
        if len(parts) >= 2:
            act_part = parts[0]  # "🎭 АКТ III"
            
            # Извлекаем название после двоеточия
            if ':' in old_title:
                title_name = old_title.split(':')[-1].strip()
            else:
                title_name = parts[-1].strip()
            
            # Формируем новый заголовок с номером сцены = номеру урока
            new_title = f"{act_part}, СЦЕНА {scene_num}: {title_name}"
            
            if old_title != new_title:
                data['title'] = new_title
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                print(f"[OK] Урок {scene_num:2}: {filename}")
                print(f"     OLD: {old_title}")
                print(f"     NEW: {new_title}")
                updated += 1
            else:
                print(f"[SKIP] Урок {scene_num:2}: Уже корректно")

print("=" * 80)
print(f"[DONE] Обновлено файлов: {updated}")
