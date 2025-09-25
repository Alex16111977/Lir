"""
Исправляем нумерацию A2 уроков:
- Устанавливаем правильные АКТЫ согласно тематике
- Номера СЦЕН = номерам уроков (1-15)
"""
import json
from pathlib import Path

# Правильное соответствие A2 уроков актам (тематическая структура)
CORRECT_STRUCTURE = {
    # Группа 1: Семейные отношения (АКТ I)
    "01_Отец_и_дочери_A2.json": {"act": "I", "scene": "1", "title": "ОТЕЦ И ДОЧЕРИ"},
    "02_Братья_A2.json": {"act": "I", "scene": "2", "title": "БРАТЬЯ"},
    "03_Предательство_семьи_A2.json": {"act": "I", "scene": "3", "title": "ПРЕДАТЕЛЬСТВО СЕМЬИ"},
    
    # Группа 2: Эмоции героев (АКТ II)
    "04_Гнев_A2.json": {"act": "II", "scene": "4", "title": "ГНЕВ - ЯРОСТЬ ЛИРА"},
    "05_Страх_A2.json": {"act": "II", "scene": "5", "title": "СТРАХ - УЖАС В НОЧИ"},
    "06_Любовь_A2.json": {"act": "II", "scene": "6", "title": "ЛЮБОВЬ В ТРАГЕДИИ"},
    
    # Группа 3: Действия и поступки (АКТ III)
    "07_Путешествие_A2.json": {"act": "III", "scene": "7", "title": "ПУТЕШЕСТВИЕ"},
    "08_Поиск_A2.json": {"act": "III", "scene": "8", "title": "ПОИСК"},
    "09_Письма_A2.json": {"act": "III", "scene": "9", "title": "ПИСЬМА - ИНТРИГИ И ПОСЛАНИЯ"},
    
    # Группа 4: Места событий (АКТ IV)
    "10_Замок_A2.json": {"act": "IV", "scene": "10", "title": "ЗАМОК - СТЕНЫ ВЛАСТИ"},
    "11_Лес_A2.json": {"act": "IV", "scene": "11", "title": "ЛЕС - БУРЯ И БЕЗУМИЕ"},
    "12_Темница_A2.json": {"act": "IV", "scene": "12", "title": "ТЕМНИЦА"},
    
    # Группа 5: Время в пьесе (АКТ V)
    "13_Прошлое_A2.json": {"act": "V", "scene": "13", "title": "ПРОШЛОЕ"},
    "14_Настоящее_A2.json": {"act": "V", "scene": "14", "title": "НАСТОЯЩЕЕ"},
    "15_Будущее_A2.json": {"act": "V", "scene": "15", "title": "БУДУЩЕЕ"}
}

a2_dir = Path(r'F:\AiKlientBank\Lir\data\a2')
updated = 0

print("[INFO] Исправляем акты и сцены в A2 уроках:")
print("=" * 80)

for filename, correct_info in CORRECT_STRUCTURE.items():
    file_path = a2_dir / filename
    
    if not file_path.exists():
        print(f"[ERROR] Файл не найден: {filename}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    old_title = data.get('title', '')
    
    # Формируем правильный заголовок с актом и сценой
    new_title = f"📚 АКТ {correct_info['act']}, СЦЕНА {correct_info['scene']}: {correct_info['title']}"
    
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
print("\n[STRUCTURE] Финальная структура A2:")
print("  Группа 1 (АКТ I): Семейные отношения - уроки 1-3")
print("  Группа 2 (АКТ II): Эмоции героев - уроки 4-6")  
print("  Группа 3 (АКТ III): Действия и поступки - уроки 7-9")
print("  Группа 4 (АКТ IV): Места событий - уроки 10-12")
print("  Группа 5 (АКТ V): Время в пьесе - уроки 13-15")
