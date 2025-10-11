"""
test/test_step1.py
Тест шага 1
"""

import json
from pathlib import Path

# Перевірка маппінгу
mapping_path = Path(r'F:\AiKlientBank\Lir\test\doc_files_mapping.json')

if not mapping_path.exists():
    print("[ERROR] Маппинг не создан")
else:
    with open(mapping_path, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
    
    assert len(mapping) > 0, "[ERROR] Нет файлов в маппинге"
    assert all('title' in v for v in mapping.values()), "[ERROR] Не все файлы имеют название"
    
    print(f"[OK] Шаг 1 ПРОЙДЕН: {len(mapping)} текстов найдено")
    print(f"[OK] Файл: {mapping_path}")
    print(f"[OK] Примеры названий:")
    for i, (text_id, data) in enumerate(list(mapping.items())[:5], 1):
        print(f"  {i}. {data['title']}")
