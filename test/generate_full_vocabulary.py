"""
test/generate_full_vocabulary.py
Фінальна генерація повного тематичного словаря
Дата: 10.10.2025
Версія: 3.0 - З реальними назвами та робочими посиланнями
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

def load_text_mapping():
    """Завантаження реальних назв текстів"""
    mapping_path = Path(__file__).parent.parent / 'test' / 'doc_files_mapping.json'
    
    if not mapping_path.exists():
        print("[WARNING] doc_files_mapping.json не знайдено!")
        return {}
    
    with open(mapping_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_html_header():
    """Генерація HTML заголовка"""
    return """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тематичний словарь німецької мови | Король Лір</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }

        /* ОГЛАВЛЕННЯ */
        .toc-section {
            padding: 60px 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .toc-header {
            text-align: center;
            margin-bottom: 50px;
        }

        .toc-header h1 {
            font-size: 3em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            font-size: 1.3em;
            opacity: 0.9;
        }

        .toc-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-top: 40px;
        }

        .toc-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            text-decoration: none;
            color: #333;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .toc-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }

        .card-emoji {
            font-size: 3em;
            flex-shrink: 0;
        }

        .card-content {
            flex: 1;
        }

        .card-title {
            font-size: 1.3em;
            margin-bottom: 8px;
            color: #2c3e50;
        }

        .card-count {
            color: #7f8c8d;
            font-size: 0.95em;
        }

        /* СЛОВАРЬ */
        .vocabulary-section {
            padding: 40px;
        }

        .section-header {
            text-align: center;
            padding: 40px 0;
            border-bottom: 3px solid #667eea;
            margin-bottom: 50px;
        }

        .section-header h2 {
            font-size: 2.5em;
            color: #2c3e50;
            margin-bottom: 15px;
        }

        .section-header p {
            font-size: 1.2em;
            color: #7f8c8d;
        }

        /* ТЕМИ */
        .theme-section {
            margin-bottom: 60px;
            scroll-margin-top: 20px;
        }

        .theme-header {
            padding: 30px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 15px;
            margin-bottom: 25px;
        }

        .theme-header h2 {
            font-size: 2em;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .theme-description {
            color: #7f8c8d;
            font-size: 1.1em;
        }

        /* ТАБЛИЦІ */
        .vocab-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            border-radius: 10px;
            overflow: hidden;
        }

        .vocab-table thead {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .vocab-table th {
            padding: 18px;
            text-align: left;
            font-weight: 600;
            font-size: 1.1em;
        }

        .vocab-table td {
            padding: 20px 18px;
            border-bottom: 1px solid #ecf0f1;
        }

        .word-row:hover {
            background: #f8f9fa;
        }

        .german-word {
            font-weight: 700;
            font-size: 1.15em;
            color: #2c3e50;
        }

        .russian-word {
            color: #555;
            font-size: 1.05em;
        }

        /* ПРИКЛАДИ */
        .collocations {
            line-height: 1.8;
        }

        .collocation-item {
            margin-bottom: 10px;
        }

        .text-link {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.2s;
        }

        .text-link:hover {
            color: #764ba2;
            text-decoration: underline;
        }

        .example {
            color: #555;
            font-style: italic;
        }

        .no-examples {
            color: #95a5a6;
            font-style: italic;
        }

        /* ФУТЕР */
        .section-footer {
            margin-top: 30px;
            text-align: center;
        }

        .back-link {
            display: inline-block;
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-weight: 600;
            transition: all 0.3s;
        }

        .back-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        /* АДАПТИВ */
        @media (max-width: 768px) {
            .toc-header h1 {
                font-size: 2em;
            }

            .toc-grid {
                grid-template-columns: 1fr;
            }

            .vocab-table {
                font-size: 0.9em;
            }

            .vocab-table th,
            .vocab-table td {
                padding: 12px;
            }
        }

        /* SMOOTH SCROLL */
        html {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body>
    <div class="container">
"""

def generate_html_footer():
    """Генерація HTML футера"""
    return """
    </div>
</body>
</html>
"""

def generate_toc(vocabulary):
    """Генерація оглавлення"""
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

def generate_tables(vocabulary, text_mapping):
    """Генерація таблиць словаря"""
    html = '<section id="vocabulary-tables" class="vocabulary-section">\n'
    html += '    <div class="section-header">\n'
    html += '        <h2>📚 Повний тематичний словарь</h2>\n'
    html += '        <p>300+ німецьких слів рівня A2-B1 з прикладами з текстів</p>\n'
    html += '    </div>\n\n'
    
    for theme_id, theme_data in vocabulary.items():
        html += f"""
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
        
        for word in theme_data['words']:
            html += f"""
                <tr class="word-row">
                    <td class="german-word">{word['german']}</td>
                    <td class="russian-word">{word.get('russian', '???')}</td>
                    <td class="collocations">
"""
            
            if word.get('examples'):
                for example in word['examples']:
                    text_id = example.get('text_id', '')
                    
                    if text_id in text_mapping:
                        text_title = text_mapping[text_id]['title']
                    else:
                        text_title = example.get('text_title', text_id)
                    
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

def main():
    print("=== ФІНАЛЬНА ГЕНЕРАЦІЯ ПОВНОГО СЛОВАРЯ ===\n")
    
    # 1. Завантаження даних
    print("[+] Крок 1: Завантаження даних...")
    
    text_mapping = load_text_mapping()
    print(f"[OK] Маппінг текстів: {len(text_mapping)} текстів")
    
    vocab_path = Path(__file__).parent.parent / 'test' / 'vocabulary_dict.json'
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocabulary = json.load(f)
    
    total_words = sum(len(theme['words']) for theme in vocabulary.values())
    print(f"[OK] Словник: {len(vocabulary)} тем, {total_words} слів")
    
    # 2. Генерація HTML
    print("\n[+] Крок 2: Генерація HTML...")
    
    html = generate_html_header()
    html += generate_toc(vocabulary)
    html += generate_tables(vocabulary, text_mapping)
    html += generate_html_footer()
    
    print(f"[OK] HTML згенеровано: {len(html) / 1024:.2f} KB")
    
    # 3. Збереження
    output = Path(__file__).parent.parent / 'texts' / 'thematic_vocabulary_full.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"\n[SUCCESS] Файл збережено: {output}")
    print(f"[SUCCESS] Розмір: {output.stat().st_size / 1024:.2f} KB")
    
    # 4. Статистика
    print(f"\n[+] Фінальна статистика:")
    print(f"  - Тем: {html.count('<div id=\"theme-')}")
    print(f"  - Таблиць: {html.count('<table class=\"vocab-table\">')}")
    print(f"  - Карток в оглавленні: {html.count('class=\"toc-card\"')}")
    print(f"  - Рядків слів: {html.count('<tr class=\"word-row\">')}")
    print(f"  - Прикладів: {html.count('<div class=\"collocation-item\">')}")
    print(f"  - Посилань: {html.count('class=\"text-link\"')}")
    
    # 5. Валідація
    print(f"\n[+] Валідація:")
    
    has_placeholders = 'Текст 1' in html or 'Текст 2' in html
    has_real_titles = len([t for t in text_mapping.values()]) > 0
    
    if not has_placeholders:
        print("[OK] ✓ Немає placeholder назв")
    else:
        print("[WARNING] ✗ Знайдено placeholder назви!")
    
    if has_real_titles:
        print("[OK] ✓ Використано реальні назви текстів")
    else:
        print("[WARNING] ✗ Маппінг текстів порожній!")
    
    print("\n[SUCCESS] ГЕНЕРАЦІЯ ЗАВЕРШЕНА!")

if __name__ == '__main__':
    main()
