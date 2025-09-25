"""
Исправляем нумерацию сцен в A2 уроках  
Номер сцены = номер урока (1-15)
"""
import json
from pathlib import Path

a2_dir = Path(r'F:\AiKlientBank\Lir\data\a2')
updated = 0

print("[INFO] Обновляем номера сцен в A2 уроках (1-15):")
print("=" * 80)

# Сначала проверим текущую структуру
for file_path in sorted(a2_dir.glob('*.json')):
    lesson_num = int(file_path.name.split('_')[0])
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    old_title = data.get('title', '')
    
    # Извлекаем название после номера и подчеркивания
    lesson_name = file_path.stem.split('_', 1)[1].replace('_A2', '').replace('_', ' ')
    
    # Формируем новый заголовок: 🎭 СЦЕНА [номер]: [НАЗВАНИЕ]
    # Убираем лишние символы и форматируем название
    if lesson_name == "Отец и дочери":
        new_title = f"🎭 СЦЕНА {lesson_num}: ОТЕЦ И ДОЧЕРИ"
    elif lesson_name == "Братья":
        new_title = f"🎭 СЦЕНА {lesson_num}: БРАТЬЯ"
    elif lesson_name == "Предательство семьи":
        new_title = f"🎭 СЦЕНА {lesson_num}: ПРЕДАТЕЛЬСТВО СЕМЬИ"
    elif lesson_name == "Гнев":
        new_title = f"🎭 СЦЕНА {lesson_num}: ГНЕВ - ЯРОСТЬ ЛИРА"
    elif lesson_name == "Страх":
        new_title = f"🎭 СЦЕНА {lesson_num}: СТРАХ - УЖАС В НОЧИ"
    elif lesson_name == "Любовь":
        new_title = f"🎭 СЦЕНА {lesson_num}: ЛЮБОВЬ В ТРАГЕДИИ"
    elif lesson_name == "Путешествие":
        new_title = f"🎭 СЦЕНА {lesson_num}: ПУТЕШЕСТВИЕ"
    elif lesson_name == "Поиск":
        new_title = f"🎭 СЦЕНА {lesson_num}: ПОИСК"
    elif lesson_name == "Письма":
        new_title = f"🎭 СЦЕНА {lesson_num}: ПИСЬМА - ИНТРИГИ И ПОСЛАНИЯ"
    elif lesson_name == "Замок":
        new_title = f"🎭 СЦЕНА {lesson_num}: ЗАМОК - СТЕНЫ ВЛАСТИ"
    elif lesson_name == "Лес":
        new_title = f"🎭 СЦЕНА {lesson_num}: ЛЕС - БУРЯ И БЕЗУМИЕ"
    elif lesson_name == "Темница":
        new_title = f"🎭 СЦЕНА {lesson_num}: ТЕМНИЦА"
    elif lesson_name == "Прошлое":
        new_title = f"🎭 СЦЕНА {lesson_num}: ПРОШЛОЕ"
    elif lesson_name == "Настоящее":
        new_title = f"🎭 СЦЕНА {lesson_num}: НАСТОЯЩЕЕ"
    elif lesson_name == "Будущее":
        new_title = f"🎭 СЦЕНА {lesson_num}: БУДУЩЕЕ"
    else:
        new_title = f"🎭 СЦЕНА {lesson_num}: {lesson_name.upper()}"
    
    if old_title != new_title:
        data['title'] = new_title
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] Урок {lesson_num:2}: {file_path.name}")
        print(f"     OLD: {old_title}")
        print(f"     NEW: {new_title}")
        updated += 1
    else:
        print(f"[SKIP] Урок {lesson_num:2}: Уже корректно")

print("=" * 80)
print(f"[DONE] Обновлено файлов: {updated}")
