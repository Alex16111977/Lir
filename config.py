"""
Конфігурація Lir Website Generator
Генерація сайту з JSON даних
"""

from pathlib import Path

# === БАЗОВІ ШЛЯХИ ===
BASE_DIR = Path(__file__).parent
SRC_DIR = BASE_DIR / "src"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"  # Результати генерації
BACKUP_DIR = BASE_DIR / "backup"
LOGS_DIR = BASE_DIR / "logs"
TEST_DIR = BASE_DIR / "test"

# === КАТЕГОРІЇ САЙТУ ===
CATEGORIES = ["a2", "b1", "thematic"]

# Структура папок A2
A2_GROUPS = [
    "gruppe_1_familie",
    "gruppe_2_emotionen", 
    "gruppe_3_handlungen",
    "gruppe_4_orte",
    "gruppe_5_zeit"
]

# Структура папок B1
B1_GROUPS = [
    "gruppe_1_macht",
    "gruppe_2_verrat",
    "gruppe_3_wahnsinn",
    "gruppe_4_natur",
    "gruppe_5_tod"
]

# Структура папок Thematic
THEMATIC_GROUPS = [
    "gruppe_1_charaktere",
    "gruppe_2_emotionen_gefuhle",
    "gruppe_3_orte_natur",
    "gruppe_4_handlungen_ereignisse",
    "gruppe_5_symbole_metaphern",
    "gruppe_6_dialog_monolog",
    "gruppe_7_zeit_schicksal"
]

# === НАЛАШТУВАННЯ КНИГИ ===
BOOK_CONFIG = {
    'enabled': True,
    'regenerate_on_change': True,
    'pdf_path': 'book/Konig Lear.pdf',
    'output_dir': 'output/book',
    'chapter_split': 'auto',  # або 'manual', 'page'
    'images_quality': 'high',
    'language': 'de',
    'toc_detection': True
}

# === ДАНІ JSON ===
JSON_DATA = {
    "a2": {
        "count": 15,
        "description": "Базовий курс A2 - 15 сцен"
    },
    "b1": {
        "count": 15,
        "description": "Продвинутий курс B1 - 15 сцен"
    },
    "thematic": {
        "count": 21,
        "description": "Тематичні уроки - 21 урок"
    }
}

# === НАЛАШТУВАННЯ ГЕНЕРАЦІЇ ===
GENERATION = {
    "css_output": "css/modern/modern.css",
    "use_original_styles": True,  # Використовувати оригінальні стилі
    "minify_output": False,       # Мініфікація HTML/CSS
}

# === НАЛАШТУВАННЯ КНИГИ ===
BOOK_CONFIG = {
    "enabled": True,                    # Увімкнути генерацію книги
    "regenerate_on_change": True,       # Регенерувати при зміні PDF
    "pdf_path": "book/Konig Lear.pdf",  # Шлях до PDF
    "output_dir": "output/book",        # Папка виводу
    "chapter_split": "auto",            # auto, manual, page
    "pages_per_chapter": 10,            # Сторінок на главу (якщо page)
    "images_quality": "high",           # low, medium, high
    "language": "de",                   # Мова книги
    "toc_detection": True               # Автоматичне виявлення оглавлення
}

# === ЛОГУВАННЯ ===
LOGGING = {
    "console_level": "ERROR",  # Тільки помилки в консоль
    "file_level": "INFO",      # Все в файл
    "format": "[%(levelname)s] %(message)s"
}

# === ВАЛІДАЦІЯ ===
def validate_project_structure():
    """Перевірка структури проекту"""
    
    errors = []
    warnings = []
    
    # Перевірка необхідних папок
    required_dirs = [SRC_DIR, DATA_DIR, OUTPUT_DIR, BACKUP_DIR, LOGS_DIR]
    for dir_path in required_dirs:
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            warnings.append(f"Створено папку: {dir_path.name}")
    
    # Перевірка JSON даних
    json_count = 0
    for category in CATEGORIES:
        cat_dir = DATA_DIR / category
        if cat_dir.exists():
            json_files = list(cat_dir.glob("*.json"))
            json_count += len(json_files)
    
    if json_count == 0:
        errors.append("Немає JSON даних в папці data/")
    elif json_count != 51:
        warnings.append(f"JSON файлів: {json_count} (має бути 51)")
    
    return errors, warnings

# === СТАТИСТИКА ===
def get_data_statistics():
    """Отримати статистику даних"""
    
    stats = {
        'json_files': 0,
        'by_category': {}
    }
    
    for category in CATEGORIES:
        cat_dir = DATA_DIR / category
        if cat_dir.exists():
            count = len(list(cat_dir.glob("*.json")))
            stats['by_category'][category] = count
            stats['json_files'] += count
    
    return stats

if __name__ == "__main__":
    print("=" * 60)
    print("  КОНФІГУРАЦІЯ LIR GENERATOR")
    print("=" * 60)
    
    # Валідація
    errors, warnings = validate_project_structure()
    
    if errors:
        print("\n[ERROR] Критичні помилки:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("\n[!] Попередження:")
        for warning in warnings:
            print(f"  - {warning}")
    
    # Статистика
    stats = get_data_statistics()
    print(f"\n[!] JSON файлів: {stats['json_files']}")
    for cat, count in stats['by_category'].items():
        print(f"  {cat}: {count} файлів")
    
    print(f"\n[!] Вихідна папка: {OUTPUT_DIR}")
    print("[!] Запуск: python main.py")
    
    if not errors:
        print("\n[OK] Конфігурація валідна!")
