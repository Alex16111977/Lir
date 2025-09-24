"""
Генератор сторінок комікса König Lear
Створює HTML сторінки для всіх томів та випусків
"""
import os
from pathlib import Path

BASE_DIR = Path(r"F:\AiKlientBank\Lir\comic\volumes")

def create_page_html(volume_num, volume_name, issue_num, issue_name, page_num, page_title, panels, vocabulary):
    """Створює HTML сторінку комікса"""
    
    # Формуємо панелі
    panels_html = ""
    for panel in panels:
        panels_html += f"""
        <!-- Панель {panel['number']}: {panel['description']} -->
        <div class="panel panel-{panel['size']} panel-{volume_name}">
            <div class="panel-number">{panel['number']}</div>
            <div class="panel-content">"""
        
        if 'speech' in panel:
            panels_html += f"""
                <div class="speech-bubble bubble-{panel['bubble_type']} bubble-{panel['bubble_position']}">
                    <div class="bubble-german">{panel['speech']['de']}</div>
                    <div class="bubble-translation">{panel['speech']['ru']}</div>
                </div>"""
        
        if 'sfx' in panel:
            panels_html += f"""
                <div class="sfx">{panel['sfx']}</div>"""
        
        panels_html += """
            </div>
        </div>"""
    
    # Формуємо словник
    vocabulary_html = ""
    for word in vocabulary:
        vocabulary_html += f"""
            <li class="vocabulary-item">
                <div class="word-german">{word['de']}</div>
                <div class="word-translation">{word['ru']}</div>
                <div class="word-transcription">{word['transcription']}</div>
            </li>"""
    
    # Повний HTML
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>König Lear - Band {volume_num}, Ausgabe {issue_num}: {issue_name}</title>
    <link rel="stylesheet" href="../../css/comic-base.css">
    <link rel="stylesheet" href="../../css/speech-bubbles.css">
</head>
<body>
    <!-- Заголовок страницы -->
    <div class="page-header">
        <h1>König Lear: {page_title}</h1>
        <p>Band {volume_num}: {volume_name.upper()} • Ausgabe {issue_num}: {issue_name} • Seite {page_num}</p>
    </div>

    <!-- Страница комикса -->
    <div class="comic-page" data-volume="{volume_num}" data-issue="{issue_num}" data-page="{page_num}">
        {panels_html}
    </div>

    <!-- Словарь страницы -->
    <div class="page-vocabulary">
        <h3>Wörter dieser Seite:</h3>
        <ul class="vocabulary-list">
            {vocabulary_html}
        </ul>
    </div>
</body>
</html>"""
    
    return html

# Конфігурація для випуску 2
issue_2_pages = [
    {
        'page_num': 1,
        'page_title': 'Das wahre Gesicht',
        'panels': [
            {
                'number': 1,
                'size': 'large',
                'description': 'Лир приезжает к Гонерилье',
                'sfx': '*kalt Empfang*'
            },
            {
                'number': 2,
                'size': 'medium',
                'description': 'Холодный прием',
                'speech': {
                    'de': 'Euer Gefolge ist zu groß!',
                    'ru': 'Ваша свита слишком велика!'
                },
                'bubble_type': 'speech',
                'bubble_position': 'top-right'
            },
            {
                'number': 3,
                'size': 'medium',
                'description': 'Требование уменьшить свиту',
                'speech': {
                    'de': 'Was? Mein Gefolge?',
                    'ru': 'Что? Моя свита?'
                },
                'bubble_type': 'speech',
                'bubble_position': 'center'
            },
            {
                'number': 4,
                'size': 'large',
                'description': 'Шок Лира',
                'speech': {
                    'de': 'Reduziert auf 50 Mann!',
                    'ru': 'Сократите до 50 человек!'
                },
                'bubble_type': 'shout',
                'bubble_position': 'top-left'
            },
            {
                'number': 5,
                'size': 'medium',
                'description': 'Я еще король?',
                'speech': {
                    'de': 'Bin ich noch König oder nicht?!',
                    'ru': 'Я еще король или нет?!'
                },
                'bubble_type': 'shout',
                'bubble_position': 'center'
            }
        ],
        'vocabulary': [
            {'de': 'das Gefolge', 'ru': 'свита', 'transcription': '[дас ге-ФОЛ-ге]'},
            {'de': 'zu groß', 'ru': 'слишком большой', 'transcription': '[цу ГРОС]'},
            {'de': 'reduzieren', 'ru': 'сокращать', 'transcription': '[ре-ду-ЦИ-рен]'},
            {'de': 'der Empfang', 'ru': 'прием', 'transcription': '[дер эм-ПФАНГ]'},
            {'de': 'kalt', 'ru': 'холодный', 'transcription': '[кальт]'},
            {'de': 'fordern', 'ru': 'требовать', 'transcription': '[ФОР-дерн]'},
            {'de': 'erschrocken', 'ru': 'испуганный', 'transcription': '[эр-ШРОК-кен]'},
            {'de': 'noch', 'ru': 'еще', 'transcription': '[нох]'}
        ]
    }
]

# Створюємо сторінки випуску 2
for page in issue_2_pages:
    html = create_page_html(
        volume_num=1,
        volume_name='macht',
        issue_num=2,
        issue_name='Die Lüge',
        page_num=page['page_num'],
        page_title=page['page_title'],
        panels=page['panels'],
        vocabulary=page['vocabulary']
    )
    
    # Зберігаємо файл
    filename = f"issue_02_luege_page_{page['page_num']}.html"
    filepath = BASE_DIR / "volume_1_macht" / filename
    
    filepath.write_text(html, encoding='utf-8')
    print(f"[OK] Created: {filename}")

print(f"\n[OK] Issue 2 pages generated!")
