"""
test/test_step4.py
Тест шага 4
"""

import json
from pathlib import Path

vocab_full_path = Path(r'F:\AiKlientBank\Lir\test\vocabulary_dict_FULL.json')

if not vocab_full_path.exists():
    print("[ERROR] Полный словарь не создан")
else:
    with open(vocab_full_path, 'r', encoding='utf-8') as f:
        vocab = json.load(f)
    
    total = sum(len(theme['words']) for theme in vocab.values())
    
    assert len(vocab) == 13, f"[ERROR] Не 13 тем: {len(vocab)}"
    assert total >= 200, f"[ERROR] Мало слов: {total}"
    
    print(f"[OK] Шаг 4 ПРОЙДЕН: {total} слов в {len(vocab)} темах")
    print(f"[OK] Топ-5 тем по количеству слов:")
    
    sorted_themes = sorted(vocab.items(), key=lambda x: len(x[1]['words']), reverse=True)
    for i, (theme_id, theme_data) in enumerate(sorted_themes[:5], 1):
        print(f"  {i}. {theme_data['emoji']} {theme_data['name']}: {len(theme_data['words'])} слов")
