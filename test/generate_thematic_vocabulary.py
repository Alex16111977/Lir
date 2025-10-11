"""
Генератор тематического HTML словаря немецкого языка
Версия: 1.0
Дата: 10.10.2025
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

def read_texts():
    """Читання текстів з файлу"""
    file_path = Path(__file__).parent.parent / 'texts' / 'Группа 1' / 'Группа 1 немецкие тексты.txt'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Розділення текстів по подвійному переносу рядка
    texts = [t.strip() for t in content.split('\n\n') if t.strip()]
    
    print(f"[OK] Прочитано {len(texts)} текстів")
    return texts

def assign_text_ids(texts):
    """Присвоєння ID текстам"""
    text_mapping = {}
    
    # Маппінг перших слів до ID
    id_map = {
        "Der Pumpkin": "text-pumpkin",
        "Eine neue Studie": "text-telefonieren",
        "Ampeln sind": "text-ampeln",
        "Baba au Rhum": "text-baba",
        "Ein Künstler aus Brasilien": "text-museum-british",
        "Über 9 Millionen": "text-serbisch",
        "Der nigerianische": "text-nigeria-artist",
        "Prozvonit": "text-prozvonit",
        "Eine Rockband": "text-ukraine-band",
        "Das Bukchon": "text-bukchon",
        "Camembert ist": "text-camembert",
        "Gewürze wie": "text-gewuerze",
        "In Griechenland": "text-griechenland",
        "Katharine Hepburn": "text-hepburn",
        "Es gibt viele Nachrichten": "text-venedig",
        "Um auf dem Mars": "text-mars",
        "Menschen arbeiten": "text-seine",
        "Viele Leute mögen das Oktoberfest": "text-bamberg",
        "Shizo ist": "text-shizo",
        "Rosé ist": "text-rose",
        "Es gibt eine Gruppe": "text-nanas",
        "Bike-Polo": "text-bikepolo",
        "Jedes Jahr besuchen": "text-moschee",
        "Einige Menschen machen": "text-sport",
        "Adam liebt": "text-adam",
        "Viele Menschen wollen wissen": "text-leben",
        "An den Küsten": "text-leuchttuerme",
        "Es gibt einen neuen": "text-pizza",
        "Südafrika ist": "text-suedafrika",
        "In Dublin": "text-dublin",
        "In China gibt": "text-china",
        "Früher zeigten": "text-seeungeheuer",
        "Eine behinderte": "text-roboter",
        "Die meisten Bienen": "text-honig",
        "Produktiv zu sein": "text-produktivitaet",
        "Sansibar ist": "text-sansibar",
        "LaLa war": "text-lala",
        "Viele ältere Menschen": "text-aeltere",
        "Viele Leute mögen es": "text-kanada",
        "Azenhas do Mar": "text-azenhas",
        "Der Weltglücksbericht": "text-glueck",
        "Im Druk Amitabha": "text-kungfu",
        "Persönliche Rekorde": "text-rekorde",
        "Hast du schon einmal an eine Scheune": "text-scheunen",
        "Ein Sushi-Restaurant": "text-sushi",
        "Hättest du Angst": "text-vampir",
        "Die Trinkgewohnheiten": "text-trinken",
        "Die irische": "text-kneecap",
        "Maurizio ist": "text-banane",
        "Es gibt neue Emojis": "text-emojis",
        "Kennst du den neuen": "text-reisepass",
        "Kairo hat": "text-kairo",
        "Die Honu": "text-honu",
        "In der kleinen Stadt Coober": "text-coober",
        "Warst du schon": "text-schatz",
        "Die globale": "text-erwaermung",
        "Ungefähr zwei": "text-mond",
        "Tee und Kaffee": "text-tea-coffee",
        "Nutzer im Internet": "text-wurm",
        "Soriano nel": "text-kastanien",
        "Wusstest du, dass Rehe": "text-rehe",
        "Hochzeiten in Südkorea": "text-hochzeit",
        "Ein Museum in Tokio": "text-tokio",
        "Hast du schon einmal von Sake": "text-sake"
    }
    
    for i, text in enumerate(texts):
        # Знайти відповідний ID
        text_id = None
        for key, value in id_map.items():
            if text.startswith(key):
                text_id = value
                break
        
        if not text_id:
            text_id = f"text-{i+1}"
        
        # Отримати назву (перші 50 символів)
        title = text[:50].strip()
        if len(text) > 50:
            title += "..."
        
        text_mapping[text_id] = {
            'id': text_id,
            'title': title,
            'content': text,
            'index': i
        }
    
    print(f"[OK] Призначено ID для {len(text_mapping)} текстів")
    return text_mapping

def generate_html(text_mapping):
    """Генерація HTML файлу"""
    
    html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Немецкий тематический словарь - Группа 1</title>
    <style>
        /* === ГЛОБАЛЬНЫЕ СТИЛИ === */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-gradient: linear-gradient(135deg, #87CEEB 0%, #E0F6FF 100%);
            --text-dark: #2C3E50;
            --text-light: #7f8c8d;
            --link-color: #3498DB;
            --link-hover: #2980B9;
            --shadow: 0 4px 6px rgba(0,0,0,0.1);
            --shadow-hover: 0 8px 20px rgba(0,0,0,0.15);
        }

        body {
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            background: var(--primary-gradient);
            color: var(--text-dark);
            line-height: 1.6;
            min-height: 100vh;
        }

        /* === ЛИПКАЯ НАВИГАЦИЯ === */
        .sticky-nav {
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: var(--shadow);
            z-index: 1000;
            padding: 1rem 0;
        }

        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-container h1 {
            font-size: 1.8rem;
            color: var(--text-dark);
        }

        .nav-buttons {
            display: flex;
            gap: 1rem;
        }

        .nav-buttons button {
            padding: 0.75rem 1.5rem;
            background: var(--link-color);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .nav-buttons button:hover {
            background: var(--link-hover);
            transform: translateY(-2px);
            box-shadow: var(--shadow-hover);
        }

        /* === ОСНОВНОЙ КОНТЕНТ === */
        .main-content {
            max-width: 1400px;
            margin: 3rem auto;
            padding: 0 2rem;
        }

        .section-header {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: var(--shadow);
            margin-bottom: 2rem;
        }

        .section-header h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #34495E;
        }

        .stats {
            font-size: 1.2rem;
            color: var(--text-light);
        }

        /* === КАРТОЧКИ ТЕКСТОВ === */
        .text-card {
            background: white;
            margin: 2rem 0;
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: var(--shadow);
            border-left: 6px solid var(--link-color);
            transition: all 0.3s ease;
        }

        .text-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-hover);
        }

        .text-card:target {
            animation: highlight 2s ease;
            border-left-width: 10px;
        }

        @keyframes highlight {
            0%, 100% { background: white; }
            50% { background: #fff9e6; }
        }

        .text-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid #ecf0f1;
        }

        .text-header h3 {
            font-size: 1.8rem;
            color: var(--text-dark);
        }

        .text-number {
            padding: 0.5rem 1rem;
            background: var(--link-color);
            color: white;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .text-content {
            line-height: 1.8;
            font-size: 1.05rem;
            color: var(--text-dark);
        }

        .text-content p {
            margin: 1rem 0;
        }

        .text-footer {
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid #e0e0e0;
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .footer-link {
            padding: 0.5rem 1rem;
            background: var(--link-color);
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            font-size: 0.95rem;
        }

        .footer-link:hover {
            background: var(--link-hover);
            transform: translateY(-2px);
        }

        /* === ПЛАВАЮЩИЕ ЭЛЕМЕНТЫ === */
        .floating-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: var(--link-color);
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: var(--shadow-hover);
            display: none;
            z-index: 999;
            transition: all 0.3s ease;
        }

        .floating-btn:hover {
            background: var(--link-hover);
            transform: scale(1.1);
        }

        .progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            width: 0%;
            z-index: 1001;
            transition: width 0.3s ease;
        }

        /* === АДАПТИВНОСТЬ === */
        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 1rem;
            }
            
            .nav-container h1 {
                font-size: 1.3rem;
                text-align: center;
            }
            
            .nav-buttons {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .text-card {
                padding: 1.5rem;
            }
            
            .text-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }
        }
    </style>
</head>
<body>
    <!-- ЛИПКАЯ НАВИГАЦИЯ -->
    <nav id="main-nav" class="sticky-nav">
        <div class="nav-container">
            <h1>🇩🇪 Немецкие тексты - Группа 1</h1>
            <div class="nav-buttons">
                <button onclick="scrollToTop()">⬆ Наверх</button>
                <button onclick="scrollToElement('texts-section')">📖 К текстам</button>
            </div>
        </div>
    </nav>

    <!-- ОСНОВНОЙ КОНТЕНТ -->
    <div class="main-content">
        <div class="section-header">
            <h2>📚 Коллекция немецких текстов</h2>
            <p class="stats">
                Всего текстов: <strong>{total_texts}</strong> | 
                Уровень: <strong>A2-B1</strong>
            </p>
        </div>

        <!-- РАЗДЕЛ С ТЕКСТАМИ -->
        <section id="texts-section">
"""
    
    # Додаємо всі тексти
    for text_id, text_data in text_mapping.items():
        html += f"""
            <article id="{text_data['id']}" class="text-card">
                <div class="text-header">
                    <h3>📄 {text_data['title']}</h3>
                    <span class="text-number">#{text_data['index'] + 1}</span>
                </div>
                
                <div class="text-content">
                    <p>{text_data['content']}</p>
                </div>
                
                <div class="text-footer">
                    <button onclick="scrollToTop()" class="footer-link">⬆ Наверх</button>
                    <a href="#main-nav" class="footer-link">📑 К началу</a>
                </div>
            </article>
"""
    
    html += """
        </section>
    </div>

    <!-- ПЛАВАЮЩИЕ ЭЛЕМЕНТЫ -->
    <button id="scroll-top-btn" class="floating-btn" onclick="scrollToTop()">↑</button>
    <div id="reading-progress" class="progress-bar"></div>

    <!-- JAVASCRIPT -->
    <script>
        // === ПЛАВНАЯ ПРОКРУТКА ===
        function scrollToElement(id) {
            const element = document.getElementById(id);
            if (element) {
                element.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }

        function scrollToTop() {
            window.scrollTo({ 
                top: 0, 
                behavior: 'smooth' 
            });
        }

        // === ПОКАЗ/СКРЫТИЕ КНОПКИ "НАВЕРХ" ===
        window.addEventListener('scroll', function() {
            const btn = document.getElementById('scroll-top-btn');
            const scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
            
            if (scrollPosition > 300) {
                btn.style.display = 'block';
            } else {
                btn.style.display = 'none';
            }
            
            // === ПРОГРЕСС БАР ===
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById("reading-progress").style.width = scrolled + "%";
        });

        // === ПОДСВЕТКА ПРИ TARGET ===
        window.addEventListener('hashchange', function() {
            const targetId = window.location.hash.substring(1);
            if (targetId) {
                const element = document.getElementById(targetId);
                if (element) {
                    element.classList.add('just-targeted');
                    setTimeout(() => {
                        element.classList.remove('just-targeted');
                    }, 2000);
                }
            }
        });

        // === СТАТИСТИКА ===
        console.log('[OK] Всего текстов:', document.querySelectorAll('.text-card').length);
    </script>
</body>
</html>"""
    
    # Підставити кількість текстів
    html = html.replace('{total_texts}', str(len(text_mapping)))
    
    return html

def save_html(html_content, output_path):
    """Збереження HTML файлу"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    file_size = Path(output_path).stat().st_size / 1024
    print(f"[OK] Файл збережено: {output_path}")
    print(f"[OK] Розмір файлу: {file_size:.2f} KB")

def main():
    print("=== ГЕНЕРАЦІЯ ТЕМАТИЧНОГО СЛОВАРЯ ===\n")
    
    # Крок 1: Читання текстів
    print("[1/4] Читання текстів...")
    texts = read_texts()
    
    # Крок 2: Присвоєння ID
    print("\n[2/4] Присвоєння ID текстам...")
    text_mapping = assign_text_ids(texts)
    
    # Крок 3: Генерація HTML
    print("\n[3/4] Генерація HTML...")
    html_content = generate_html(text_mapping)
    print(f"[OK] HTML згенеровано")
    
    # Крок 4: Збереження
    print("\n[4/4] Збереження файлу...")
    output_path = Path(__file__).parent.parent / 'texts' / 'thematic_vocabulary.html'
    save_html(html_content, output_path)
    
    print("\n=== ГОТОВО! ===")
    print(f"Файл доступний за адресою: file:///{output_path}")

if __name__ == '__main__':
    main()
