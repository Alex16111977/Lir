"""
test/replace_vocabulary.py
Замена словаря на полную версию
Дата: 10.10.2025
"""

import sys
from pathlib import Path
import shutil

sys.path.insert(0, str(Path(__file__).parent.parent))

def replace_vocabulary():
    """Замена vocabulary_dict.json на полную версию"""
    
    source = Path(r'F:\AiKlientBank\Lir\test\vocabulary_dict_FULL.json')
    target = Path(r'F:\AiKlientBank\Lir\test\vocabulary_dict.json')
    backup = Path(r'F:\AiKlientBank\Lir\test\vocabulary_dict_OLD.json')
    
    print("[+] Замена словаря...")
    
    # Бэкап старого
    if target.exists():
        shutil.copy(target, backup)
        print(f"[OK] Бэкап создан: {backup}")
    
    # Замена
    shutil.copy(source, target)
    
    print(f"[OK] Словарь заменён: {target}")
    print(f"[OK] Исходный файл: {source}")
    
    # Проверка
    import json
    with open(target, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total = sum(len(theme['words']) for theme in data.values())
    print(f"[OK] Проверка: {total} слов в новом словаре")

if __name__ == '__main__':
    print("=== ЗАМЕНА СЛОВАРЯ ===\n")
    replace_vocabulary()
