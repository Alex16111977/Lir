"""
test/generate_toc.py
Генерація HTML оглавлення для словаря
Дата: 10.10.2025
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

def generate_toc_section(vocabulary):
    """Генерація оглавлення"""
    
    total_words = sum(len(theme['words']) for theme in vocabulary.values())
    
    html = """
    <!-- ОГЛАВЛЕНИЕ СЛОВАРЯ -->
    <section id="table-of-contents" class="toc-section">
        <div class="section-header">
            <h2>📑 Содержание тематического словаря</h2>
            <p class="stats">
                Всего: <strong id="total-words">{total_words}</strong> уникальных немецких слов 
                из <strong>61</strong> текстов в <strong>13</strong> тематических группах
            </p>
            <p class="description">
                Каждое слово снабжено переводом и примерами использования из реальных текстов. 
                Кликните на карточку темы, чтобы перейти к соответствующей таблице слов.
            </p>
        </div>
        
        <div class="toc-grid">
""".replace('{total_words}', str(total_words))
    
    for theme_id, theme_data in vocabulary.items():
        word_count = len(theme_data['words'])
        html += f"""
            <a href="#{theme_id}" class="toc-card" style="border-left: 5px solid {theme_data['color']};">
                <span class="emoji">{theme_data['emoji']}</span>
                <h3>{theme_data['name']}</h3>
                <p class="word-count" id="count-{theme_id}">{word_count} слов</p>
            </a>
"""
    
    html += """
        </div>
    </section>
"""
    
    return html

def main():
    print("=== ГЕНЕРАЦІЯ ОГЛАВЛЕННЯ ===\n")
    
    # Завантаження словника
    vocab_path = Path(__file__).parent.parent / 'test' / 'vocabulary_dict.json'
    
    print(f"[+] Читання словника: {vocab_path}")
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocabulary = json.load(f)
    
    print(f"[OK] Словник завантажено: {len(vocabulary)} тем")
    
    # Генерація
    print("[+] Генерація HTML...")
    toc_html = generate_toc_section(vocabulary)
    
    # Збереження
    output = Path(__file__).parent.parent / 'test' / 'toc_section.html'
    with open(output, 'w', encoding='utf-8') as f:
        f.write(toc_html)
    
    print(f"[OK] Оглавлення згенеровано: {output}")
    print(f"[OK] Розмір: {len(toc_html)} символів")
    print(f"\n[+] Статистика:")
    print(f"  - Карточок тем: {toc_html.count('<a href=\"#theme-')}")
    print(f"  - Емодзі: {toc_html.count('class=\"emoji\"')}")

if __name__ == '__main__':
    main()
