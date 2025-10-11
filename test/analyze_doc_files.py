"""
test/analyze_doc_files.py
Анализ текстов из файла Группа 1
Дата: 10.10.2025
"""

import sys
from pathlib import Path
import json
import re

sys.path.insert(0, str(Path(__file__).parent.parent))

def analyze_texts():
    """Анализ текстов из файла"""
    
    # Читаємо файл з усіма текстами
    texts_file = Path(r'F:\AiKlientBank\Lir\texts\Группа 1\Группа 1 немецкие тексты.txt')
    
    print(f"[+] Чтение файла: {texts_file}")
    
    if not texts_file.exists():
        print(f"[ERROR] Файл не найден: {texts_file}")
        return []
    
    with open(texts_file, 'r', encoding='utf-8') as f:
        full_text = f.read()
    
    # Розділяємо на окремі тексти (за подвійним перенесенням рядка)
    texts = [t.strip() for t in full_text.split('\n\n') if t.strip()]
    
    print(f"[OK] Найдено текстов: {len(texts)}")
    
    # Створення маппінгу
    file_mapping = {}
    
    for i, text in enumerate(texts, 1):
        # Перше речення як назва
        first_sentence = text.split('.')[0].strip()
        
        # Створюємо ID з першого слова
        first_words = first_sentence.split()[:3]
        title_base = ' '.join(first_words)
        
        file_id = f"text-{i}"
        
        file_mapping[file_id] = {
            'title': title_base,
            'text': text,
            'characters': len(text),
            'words': len(text.split())
        }
        
        print(f"  [{i:2d}] {title_base[:50]}... ({len(text)} символов)")
    
    # Сохранение маппинга
    output = Path(__file__).parent.parent / 'test' / 'doc_files_mapping.json'
    
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(file_mapping, f, ensure_ascii=False, indent=2)
    
    print(f"\n[OK] Маппинг сохранён: {output}")
    print(f"[OK] Всего текстов для обработки: {len(file_mapping)}")
    
    return file_mapping

if __name__ == '__main__':
    print("=== АНАЛИЗ ТЕКСТОВ ===\n")
    analyze_texts()
