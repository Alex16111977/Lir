"""
Скрипт для исправления нумерации актов и сцен в B1 уроках
Приводит в соответствие с реальной структурой "Короля Лира"
Дата: 07.01.2025
"""

import json
from pathlib import Path

# Правильная структура актов и сцен по пьесе "Король Лир"
CORRECT_STRUCTURE = {
    "01_Тронный_зал_B1.json": {
        "act": "I",
        "scene": "1", 
        "title": "ТРОННЫЙ ЗАЛ",
        "description": "Деление королевства"
    },
    "02_Испытание_любви_B1.json": {
        "act": "I",
        "scene": "1",
        "title": "ИСПЫТАНИЕ ЛЮБВИ",
        "description": "Испытание дочерей"
    },
    "03_Изгнание_Корделии_B1.json": {
        "act": "I",
        "scene": "1",
        "title": "ИЗГНАНИЕ КОРДЕЛИИ",
        "description": "Изгнание Корделии и Кента"
    },
    "04_Интрига_Эдмунда_B1.json": {
        "act": "I",
        "scene": "2",
        "title": "ИНТРИГА ЭДМУНДА",
        "description": "Замок Глостера"
    },
    "05_Обман_Глостера_B1.json": {
        "act": "I",
        "scene": "2",
        "title": "ОБМАН ГЛОСТЕРА",
        "description": "Эдмунд обманывает отца"
    },
    "06_Унижение_Лира_B1.json": {
        "act": "I",
        "scene": "4",
        "title": "УНИЖЕНИЕ ЛИРА",
        "description": "Конфликт с Гонерильей"
    },
    "07_Буря_и_безумие_B1.json": {
        "act": "III",
        "scene": "2",
        "title": "БУРЯ И БЕЗУМИЕ",
        "description": "Лир в буре"
    },
    "08_Встреча_с_Томом_B1.json": {
        "act": "III",
        "scene": "4",
        "title": "ВСТРЕЧА С ТОМОМ",
        "description": "Эдгар как Том из Бедлама"
    },
    "09_Ослепление_Глостера_B1.json": {
        "act": "III",
        "scene": "7",
        "title": "ОСЛЕПЛЕНИЕ ГЛОСТЕРА",
        "description": "Жестокость Корнуолла и Реганы"
    },
    "10_Дуврские_скалы_B1.json": {
        "act": "IV",
        "scene": "6",
        "title": "ДУВРСКИЕ СКАЛЫ",
        "description": "Мнимое самоубийство Глостера"
    },
    "11_Примирение_с_Корделией_B1.json": {
        "act": "IV",
        "scene": "7",
        "title": "ПРИМИРЕНИЕ С КОРДЕЛИЕЙ",
        "description": "Встреча отца и дочери"
    },
    "12_Прозрение_Лира_B1.json": {
        "act": "IV",
        "scene": "6",
        "title": "ПРОЗРЕНИЕ ЛИРА",
        "description": "Безумие и мудрость"
    },
    "13_Битва_B1.json": {
        "act": "V",
        "scene": "2",
        "title": "БИТВА",
        "description": "Война и поражение"
    },
    "14_Дуэль_братьев_B1.json": {
        "act": "V",
        "scene": "3",
        "title": "ДУЭЛЬ БРАТЬЕВ",
        "description": "Эдгар против Эдмунда"
    },
    "15_Смерть_Корделии_и_Лира_B1.json": {
        "act": "V",
        "scene": "3",
        "title": "ФИНАЛ",
        "description": "Трагическая развязка"
    }
}

def analyze_current_structure():
    """Анализирует текущую структуру B1 уроков"""
    b1_dir = Path(r'F:\AiKlientBank\Lir\data\b1')
    
    print("[ANALYSIS] Текущая структура B1 уроков:")
    print("=" * 80)
    
    for file_path in sorted(b1_dir.glob('*.json')):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            title = data.get('title', 'NO TITLE')
            filename = file_path.name
            
            correct = CORRECT_STRUCTURE.get(filename, {})
            correct_act = correct.get('act', '?')
            correct_scene = correct.get('scene', '?')
            
            # Извлекаем текущие акт и сцену из title
            current_act = '?'
            current_scene = '?'
            
            if 'АКТ' in title:
                parts = title.split(',')
                if len(parts) > 0:
                    act_part = parts[0].strip()
                    if 'АКТ' in act_part:
                        current_act = act_part.split('АКТ')[1].strip().split()[0]
                    
                    if len(parts) > 1:
                        scene_part = parts[1].strip()
                        if 'СЦЕНА' in scene_part:
                            current_scene = scene_part.split('СЦЕНА')[1].split(':')[0].strip()
            
            # Проверяем соответствие
            match = '✓' if (current_act == correct_act and current_scene == correct_scene) else '✗'
            
            print(f"\n{filename}")
            print(f"  Текущее: АКТ {current_act}, СЦЕНА {current_scene}")
            print(f"  Должно:  АКТ {correct_act}, СЦЕНА {correct_scene}")
            print(f"  Статус:  [{match}] {correct.get('description', '')}")
    
    print("\n" + "=" * 80)

def fix_act_scene_numbering(dry_run=True):
    """Исправляет нумерацию актов и сцен в B1 уроках"""
    b1_dir = Path(r'F:\AiKlientBank\Lir\data\b1')
    updated_count = 0
    
    print(f"\n[FIX] {'DRY RUN' if dry_run else 'UPDATING'} B1 уроков:")
    print("=" * 80)
    
    for filename, correct_info in CORRECT_STRUCTURE.items():
        file_path = b1_dir / filename
        
        if not file_path.exists():
            print(f"[!] Файл не найден: {filename}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        old_title = data.get('title', '')
        
        # Формируем новый заголовок
        new_title = f"🎭 АКТ {correct_info['act']}, СЦЕНА {correct_info['scene']}: {correct_info['title']}"
        
        if old_title != new_title:
            print(f"\n{filename}")
            print(f"  OLD: {old_title}")
            print(f"  NEW: {new_title}")
            
            if not dry_run:
                data['title'] = new_title
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"  [OK] Обновлено")
            else:
                print(f"  [DRY] Будет обновлено")
                
            updated_count += 1
        else:
            print(f"\n{filename}: [OK] Уже корректно")
    
    print(f"\n{'=' * 80}")
    print(f"[SUMMARY] {'Будет обновлено' if dry_run else 'Обновлено'}: {updated_count} файлов")
    return updated_count

if __name__ == "__main__":
    # Анализируем текущую структуру
    analyze_current_structure()
    
    # Запускаем исправление в dry-run режиме
    print("\n" + "=" * 80)
    print("[INFO] Запуск исправления в DRY-RUN режиме")
    print("=" * 80)
    
    updated = fix_act_scene_numbering(dry_run=True)
    
    if updated > 0:
        print("\n[?] Применить изменения? (раскомментируйте строку ниже)")
        # fix_act_scene_numbering(dry_run=False)
        print("# fix_act_scene_numbering(dry_run=False)")
