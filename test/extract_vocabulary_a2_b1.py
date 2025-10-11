"""
test/extract_vocabulary_a2_b1.py
Извлечение лексики уровня A2-B1
Дата: 10.10.2025
"""

import sys
from pathlib import Path
import json
import re
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))

# СПИСОК СЛОВ A1 ДЛЯ ИСКЛЮЧЕНИЯ (базовая лексика)
A1_WORDS = {
    # Артикли и местоимения
    'der', 'die', 'das', 'ein', 'eine', 'einen', 'einem', 'einer', 'eines',
    'ich', 'du', 'er', 'sie', 'es', 'wir', 'ihr', 'mein', 'dein', 'sein', 
    'unser', 'euer', 'mir', 'dir', 'ihm', 'uns', 'euch', 'ihnen',
    
    # Базовые глаголы
    'sein', 'haben', 'werden', 'machen', 'gehen', 'kommen', 'sehen',
    'sagen', 'können', 'müssen', 'wollen', 'sollen', 'dürfen', 'mögen',
    'ist', 'sind', 'war', 'waren', 'hat', 'haben', 'wird', 'kann',
    'muss', 'will', 'soll', 'darf', 'mag', 'gibt', 'gibt', 'tun',
    
    # Союзы и предлоги
    'und', 'oder', 'aber', 'denn', 'in', 'an', 'auf', 'mit', 'von', 'zu',
    'aus', 'bei', 'nach', 'für', 'um', 'über', 'unter', 'durch', 'ohne',
    'gegen', 'bis', 'seit', 'wegen', 'während', 'als', 'wenn', 'weil',
    'dass', 'damit', 'obwohl', 'wie', 'so', 'auch', 'noch', 'schon',
    
    # Числа
    'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht',
    'neun', 'zehn', 'zwanzig', 'hundert', 'tausend',
    
    # Базовые прилагательные  
    'gut', 'schlecht', 'groß', 'klein', 'alt', 'neu', 'schön', 'viel',
    'wenig', 'mehr', 'viele', 'wenige',
    
    # Другие базовые слова
    'ja', 'nein', 'nicht', 'hier', 'dort', 'jetzt', 'dann', 'immer',
    'nie', 'heute', 'morgen', 'gestern', 'sehr', 'ganz', 'alle',
    'was', 'wer', 'wie', 'wo', 'wann', 'warum', 'welche', 'dieser',
    'diese', 'dieses', 'jener', 'jede', 'jedes', 'alle', 'einige',
    'manche', 'solche', 'andere'
}

def extract_vocabulary(texts_content):
    """Извлечение словаря A2-B1 из текстов"""
    
    print("[+] Извлечение немецких слов...")
    
    word_freq = defaultdict(lambda: {'count': 0, 'contexts': []})
    
    for text_id, content in texts_content.items():
        text = content['text']
        title = content['title']
        
        # Извлечение слов (немецкие буквы)
        words = re.findall(r'[a-zA-ZäöüÄÖÜß]+', text)
        
        for word in words:
            word_lower = word.lower()
            
            # Фильтрация
            if len(word_lower) < 4:  # Слишком короткие
                continue
            
            if word_lower in A1_WORDS:  # Базовая лексика A1
                continue
            
            # Подсчёт и сохранение контекста
            word_freq[word_lower]['count'] += 1
            
            # Найти предложение со словом
            sentences = re.split(r'[.!?]', text)
            for sentence in sentences:
                if word in sentence:
                    # Сохраняем первое вхождение
                    if len(word_freq[word_lower]['contexts']) < 3:
                        context = sentence.strip()[:100]  # Первые 100 символов
                        word_freq[word_lower]['contexts'].append({
                            'text_id': text_id,
                            'text_title': title,
                            'phrase': context
                        })
                    break
    
    # Топ-300 слов
    top_words = sorted(word_freq.items(), key=lambda x: x[1]['count'], reverse=True)[:300]
    
    print(f"\n[OK] Всего уникальных слов (без A1): {len(word_freq)}")
    print(f"[OK] Топ-300 слов для словаря")
    print(f"\n[+] Топ-20 слов:")
    for word, data in top_words[:20]:
        print(f"  - {word}: {data['count']} раз")
    
    # Сохранение
    output = Path(__file__).parent.parent / 'test' / 'vocabulary_a2_b1.json'
    
    result = {word: data for word, data in top_words}
    
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n[OK] Словарь сохранён: {output}")
    print(f"[OK] Сохранено слов: {len(result)}")
    
    return result

if __name__ == '__main__':
    print("=== ИЗВЛЕЧЕНИЕ ЛЕКСИКИ A2-B1 ===\n")
    
    # Чтение текстов
    texts_path = Path(__file__).parent.parent / 'test' / 'doc_files_mapping.json'
    
    with open(texts_path, 'r', encoding='utf-8') as f:
        texts = json.load(f)
    
    print(f"[+] Загружено текстов: {len(texts)}")
    
    extract_vocabulary(texts)
