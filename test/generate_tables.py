"""
test/generate_tables.py
Генерація HTML таблиць словаря з РЕАЛЬНИМИ назвами
Дата: 10.10.2025
Версія: 2.0 - Оновлено з реальними назвами текстів
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

def load_text_mapping():
    """Завантаження РЕАЛЬНИХ назв текстів з doc_files_mapping.json"""
    
    mapping_path = Path(__file__).parent.parent / 'test' / 'doc_files_mapping.json'
    
    if not mapping_path.exists():
        print("[ERROR] doc_files_mapping.json не знайдено!")
        return {}
    
    with open(mapping_path, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
    
    print(f"[OK] Завантажено маппінг для {len(mapping)} текстів")
    
    return mapping

def generate_vocabulary_tables(vocabulary, text_mapping):
    """Генерація таблиць словаря з РОБОЧИМИ посиланнями"""
    
    html = '<section id="vocabulary-tables" class="vocabulary-section">\n'
    html += '    <div class="section-header">\n'
    html += '        <h2>📚 Повний тематичний словарь</h2>\n'
    html += '        <p>300+ німецьких слів рівня A2-B1 з прикладами з текстів</p>\n'
    html += '    </div>\n\n'
    
    for theme_id, theme_data in vocabulary.items():
        html += f"""
    <!-- ТЕМА: {theme_data['name'].upper()} -->
    <div id="{theme_id}" class="theme-section">
        <div class="theme-header" style="border-left: 5px solid {theme_data['color']};">
            <h2>{theme_data['emoji']} {theme_data['name'].upper()}</h2>
            <p class="theme-description">{len(theme_data['words'])} слів в цій категорії</p>
        </div>
        
        <table class="vocab-table">
            <thead>
                <tr>
                    <th class="col-german">Deutsch</th>
                    <th class="col-russian">Русский</th>
                    <th class="col-collocations">Приклади з текстів</th>
                </tr>
            </thead>
            <tbody>
"""
        
        # Додаємо слова
        for word in theme_data['words']:
            html += f"""
                <tr class="word-row">
                    <td class="german-word">{word['german']}</td>
                    <td class="russian-word">{word.get('russian', '???')}</td>
                    <td class="collocations">
"""
            
            # Додаємо приклади з РЕАЛЬНИМИ назвами та РОБОЧИМИ посиланнями
            if word.get('examples'):
                for example in word['examples']:
                    # Отримуємо РЕАЛЬНУ назву з маппінгу
                    text_id = example.get('text_id', '')
                    
                    if text_id in text_mapping:
                        text_title = text_mapping[text_id]['title']
                    else:
                        text_title = example.get('text_title', text_id)
                    
                    # Створюємо РОБОЧУ ССЫЛКУ (якорь в HTML)
                    text_anchor = f"#text-{text_id}"
                    
                    html += f"""
                        <div class="collocation-item">
                            <a href="{text_anchor}" class="text-link" title="Перейти до тексту: {text_title}">{text_title}</a>: 
                            <span class="example">«{example['phrase']}»</span>
                        </div>
"""
            else:
                html += '                        <span class="no-examples">Приклади відсутні</span>\n'
            
            html += """
                    </td>
                </tr>
"""
        
        html += """
            </tbody>
        </table>
        
        <div class="section-footer">
            <a href="#table-of-contents" class="back-link">↑ До змісту</a>
        </div>
    </div>

"""
    
    html += '</section>\n'
    return html

def generate_table_of_contents(vocabulary):
    """Генерація оглавления з карточками тем"""
    
    html = '<section id="table-of-contents" class="toc-section">\n'
    html += '    <div class="toc-header">\n'
    html += '        <h1>📚 Тематичний словарь німецької мови</h1>\n'
    html += '        <p class="subtitle">Вивчайте німецьку через "Короля Ліра"</p>\n'
    html += '    </div>\n\n'
    html += '    <div class="toc-grid">\n'
    
    for theme_id, theme_data in vocabulary.items():
        word_count = len(theme_data['words'])
        
        html += f"""
        <a href="#{theme_id}" class="toc-card" style="border-left: 5px solid {theme_data['color']};">
            <div class="card-emoji">{theme_data['emoji']}</div>
            <div class="card-content">
                <h3 class="card-title">{theme_data['name']}</h3>
                <p class="card-count">{word_count} слів</p>
            </div>
        </a>
"""
    
    html += '    </div>\n'
    html += '</section>\n\n'
    
    return html

def main():
    print("=== ГЕНЕРАЦІЯ ТАБЛИЦЬ СЛОВАРЯ (ВЕРСІЯ 2.0) ===\n")
    
    # Завантаження реального маппінгу текстів
    print("[+] Крок 1: Завантаження маппінгу текстів...")
    text_mapping = load_text_mapping()
    
    if not text_mapping:
        print("[ERROR] Маппінг не завантажено! Використовуємо fallback.")
        text_mapping = {}
    
    # Завантаження словника
    vocab_path = Path(__file__).parent.parent / 'test' / 'vocabulary_dict.json'
    
    print(f"\n[+] Крок 2: Читання словника: {vocab_path}")
    
    if not vocab_path.exists():
        print(f"[ERROR] Файл не знайдено: {vocab_path}")
        return
    
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocabulary = json.load(f)
    
    print(f"[OK] Словник завантажено: {len(vocabulary)} тем")
    
    # Підрахунок слів
    total_words = sum(len(theme['words']) for theme in vocabulary.values())
    print(f"[OK] Всього слів: {total_words}")
    
    # Генерація оглавлення
    print("\n[+] Крок 3: Генерація оглавлення...")
    toc_html = generate_table_of_contents(vocabulary)
    print(f"[OK] Оглавлення згенеровано")
    
    # Генерація таблиць
    print("\n[+] Крок 4: Генерація таблиць з реальними назвами...")
    tables_html = generate_vocabulary_tables(vocabulary, text_mapping)
    print(f"[OK] Таблиці згенеровано")
    
    # Об'єднання
    full_html = toc_html + tables_html
    
    # Збереження
    output = Path(__file__).parent.parent / 'test' / 'vocab_tables.html'
    with open(output, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"\n[SUCCESS] Файл збережено: {output}")
    print(f"[SUCCESS] Розмір: {len(full_html) / 1024:.2f} KB")
    
    print(f"\n[+] Статистика:")
    print(f"  - Тем: {full_html.count('<div id=\"theme-')}")
    print(f"  - Таблиць: {full_html.count('<table class=\"vocab-table\">')}")
    print(f"  - Рядків слів: {full_html.count('<tr class=\"word-row\">')}")
    print(f"  - Прикладів: {full_html.count('<div class=\"collocation-item\">')}")
    print(f"  - Посилань: {full_html.count('class=\"text-link\"')}")
    
    # Перевірка що немає "Текст 1", "Текст 2"
    if 'Текст 1' in full_html or 'Текст 2' in full_html:
        print("\n[WARNING] Знайдено placeholder назви!")
    else:
        print("\n[OK] Всі назви реальні!")

if __name__ == '__main__':
    main()
