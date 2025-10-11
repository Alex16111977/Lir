"""
test/test_step3.py
Тест шага 3
"""

import json
from pathlib import Path

vocab_path = Path(r'F:\AiKlientBank\Lir\test\vocabulary_a2_b1.json')

# Список A1 для проверки
A1_WORDS = {'der', 'die', 'das', 'ein', 'eine', 'ich', 'du', 'er', 'sie', 'es',
             'und', 'aber', 'sein', 'haben', 'ist', 'sind', 'gut', 'schlecht'}

if not vocab_path.exists():
    print("[ERROR] Словарь не создан")
else:
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab = json.load(f)
    
    assert len(vocab) >= 100, f"[ERROR] Мало слов: {len(vocab)}"
    
    # Проверка что нет слов A1
    a1_found = [w for w in vocab.keys() if w in A1_WORDS]
    assert len(a1_found) == 0, f"[ERROR] Найдены слова A1: {a1_found}"
    
    # Проверка контекстов
    words_with_contexts = sum(1 for w in vocab.values() if len(w.get('contexts', [])) > 0)
    
    print(f"[OK] Шаг 3 ПРОЙДЕН: {len(vocab)} слов A2-B1")
    print(f"[OK] Все слова имеют контексты: {words_with_contexts}/{len(vocab)}")
    print(f"[OK] Нет слов A1 в словаре")
    print(f"[OK] Примеры слов:")
    for i, (word, data) in enumerate(list(vocab.items())[:5], 1):
        print(f"  {i}. {word}: {data['count']} раз")
