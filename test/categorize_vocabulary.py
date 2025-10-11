"""
test/categorize_vocabulary.py
Автоматическое распределение слов по темам
Дата: 10.10.2025
Роль: Преподаватель немецкого языка
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

# ТЕМАТИЧЕСКИЕ КЛЮЧЕВЫЕ СЛОВА
THEME_KEYWORDS = {
    "theme-food": {
        "name": "Еда и напитки",
        "color": "#FF6B6B",
        "emoji": "🍽️",
        "keywords": [
            'essen', 'trinken', 'getränk', 'käse', 'brot', 'fleisch',
            'wurst', 'kuchen', 'gemüse', 'obst', 'restaurant', 'küche',
            'mahlzeit', 'frühstück', 'mittagessen', 'abendessen', 'hunger',
            'durst', 'schmeck', 'lecker', 'süß', 'salzig', 'bitter',
            'pasta', 'pizza', 'wein', 'bier', 'kaffee', 'tee', 'dessert',
            'gericht', 'sauce', 'gewürz', 'braten', 'kochen'
        ]
    },
    "theme-communication": {
        "name": "Коммуникация",
        "color": "#4ECDC4",
        "emoji": "💬",
        "keywords": [
            'telefonieren', 'sprechen', 'sagen', 'erzählen', 'fragen',
            'antworten', 'gespräch', 'nachricht', 'brief', 'email',
            'kommunikation', 'diskutieren', 'erklären', 'verstehen',
            'rufen', 'anruf', 'sprachnachricht', 'videochat', 'schreiben'
        ]
    },
    "theme-transport": {
        "name": "Транспорт",
        "color": "#95E1D3",
        "emoji": "🚗",
        "keywords": [
            'auto', 'fahren', 'zug', 'bus', 'flugzeug', 'reisen',
            'verkehr', 'straße', 'station', 'flughafen', 'fahrrad',
            'transport', 'ticket', 'ampel', 'boot', 'schiff'
        ]
    },
    "theme-art": {
        "name": "Искусство и культура",
        "color": "#F38181",
        "emoji": "🎨",
        "keywords": [
            'kunst', 'musik', 'theater', 'film', 'kino', 'konzert',
            'ausstellung', 'museum', 'kultur', 'maler', 'künstler',
            'bild', 'gemälde', 'literatur', 'buch', 'rockband',
            'instrument', 'klavier', 'lied', 'orchest'
        ]
    },
    "theme-languages": {
        "name": "Языки",
        "color": "#AA96DA",
        "emoji": "🗣️",
        "keywords": [
            'sprache', 'deutsch', 'englisch', 'französisch', 'lernen',
            'übersetzen', 'wort', 'grammatik', 'vokabel', 'aussprache',
            'buchstabe', 'schreiben', 'lesen', 'sprechen', 'verstehen'
        ]
    },
    "theme-science": {
        "name": "Наука и технологии",
        "color": "#FCBAD3",
        "emoji": "🔬",
        "keywords": [
            'wissenschaft', 'forschung', 'technologie', 'computer',
            'internet', 'digital', 'studieren', 'universität', 'labor',
            'studie', 'selbstfahrend', 'robot', 'erfindung', 'methode'
        ]
    },
    "theme-geography": {
        "name": "География и путешествия",
        "color": "#FFFFD2",
        "emoji": "🌍",
        "keywords": [
            'land', 'stadt', 'dorf', 'berg', 'meer', 'fluss', 'see',
            'reise', 'urlaub', 'hotel', 'tourist', 'welt', 'europa',
            'insel', 'strand', 'küste', 'dorf', 'besuchen'
        ]
    },
    "theme-history": {
        "name": "История",
        "color": "#A8D8EA",
        "emoji": "📜",
        "keywords": [
            'geschichte', 'historisch', 'vergangenheit', 'krieg',
            'könig', 'kaiser', 'revolution', 'epoche', 'jahrhundert',
            'museum', 'traditional', 'früher', 'damals', 'alter'
        ]
    },
    "theme-verbs": {
        "name": "Глаголы",
        "color": "#FFAAA5",
        "emoji": "⚡",
        "keywords": []  # Все глаголы автоматически
    },
    "theme-adjectives": {
        "name": "Прилагательные",
        "color": "#FFD3B6",
        "emoji": "✨",
        "keywords": []  # Все прилагательные автоматически
    },
    "theme-time": {
        "name": "Время и числа",
        "color": "#DCEDC1",
        "emoji": "⏰",
        "keywords": [
            'zeit', 'stunde', 'minute', 'tag', 'woche', 'monat', 'jahr',
            'heute', 'morgen', 'gestern', 'jetzt', 'bald', 'spät',
            'früh', 'abend', 'nacht', 'morgen', 'mittag', 'nachmittag'
        ]
    },
    "theme-measurements": {
        "name": "Измерения и количество",
        "color": "#FFC8A2",
        "emoji": "📏",
        "keywords": [
            'groß', 'klein', 'lang', 'kurz', 'breit', 'schmal', 'hoch',
            'tief', 'viel', 'wenig', 'meter', 'kilometer', 'kilogramm',
            'prozent', 'ungefähr', 'circa', 'millionen', 'tausend'
        ]
    },
    "theme-abstract": {
        "name": "Абстрактные понятия",
        "color": "#D4A5A5",
        "emoji": "💭",
        "keywords": [
            'menschen', 'leute', 'leben', 'welt', 'sache', 'ding',
            'problem', 'lösung', 'idee', 'gedanke', 'gefühl', 'wichtig',
            'interessant', 'möglich', 'unmöglich', 'glücklich', 'gesund'
        ]
    }
}

def categorize_word(word, contexts):
    """Определение темы для слова"""
    
    word_lower = word.lower()
    
    # Проверка по ключевым словам
    for theme_id, theme_data in THEME_KEYWORDS.items():
        for keyword in theme_data['keywords']:
            if keyword in word_lower or word_lower in keyword:
                return theme_id
    
    # Проверка по контексту
    context_text = ' '.join([c['phrase'].lower() for c in contexts]).lower()
    
    for theme_id, theme_data in THEME_KEYWORDS.items():
        matches = sum(1 for kw in theme_data['keywords'] if kw in context_text)
        if matches >= 2:  # Минимум 2 совпадения
            return theme_id
    
    # По умолчанию - абстрактные понятия
    return "theme-abstract"

def build_full_vocabulary():
    """Создание полного словаря с распределением по темам"""
    
    print("[+] Загрузка словаря A2-B1...")
    
    vocab_path = Path(__file__).parent.parent / 'test' / 'vocabulary_a2_b1.json'
    
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab_a2_b1 = json.load(f)
    
    print(f"[OK] Загружено: {len(vocab_a2_b1)} слов")
    
    # Инициализация словаря по темам
    vocabulary = {}
    for theme_id, theme_data in THEME_KEYWORDS.items():
        vocabulary[theme_id] = {
            'name': theme_data['name'],
            'color': theme_data['color'],
            'emoji': theme_data['emoji'],
            'words': []
        }
    
    # Распределение слов
    print("\n[+] Распределение слов по темам...")
    
    for word, data in vocab_a2_b1.items():
        theme_id = categorize_word(word, data['contexts'])
        
        word_entry = {
            'german': word,  # TODO: Добавить артикль и множественное число
            'russian': '',  # TODO: Добавить перевод
            'examples': data['contexts'][:2]  # Максимум 2 примера
        }
        
        vocabulary[theme_id]['words'].append(word_entry)
    
    # Статистика
    print("\n[OK] Распределение завершено:")
    total_words = 0
    for theme_id, theme_data in vocabulary.items():
        count = len(theme_data['words'])
        total_words += count
        print(f"  {theme_data['emoji']} {theme_data['name']}: {count} слов")
    
    # Сохранение
    output = Path(__file__).parent.parent / 'test' / 'vocabulary_dict_FULL.json'
    
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False, indent=2)
    
    print(f"\n[OK] Полный словарь сохранён: {output}")
    print(f"[OK] Всего слов в словаре: {total_words}")
    
    return vocabulary

if __name__ == '__main__':
    print("=== РАСПРЕДЕЛЕНИЕ СЛОВАРЯ ПО ТЕМАМ ===\n")
    build_full_vocabulary()
