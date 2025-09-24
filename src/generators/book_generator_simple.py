"""
Альтернативний генератор книги з PDF (без PyMuPDF)
Використовує pypdf для роботи з PDF
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime

try:
    import PyPDF2
    USE_PYPDF2 = True
except ImportError:
    USE_PYPDF2 = False
    print("[!] PyPDF2 не встановлено, спробуємо текстовий підхід")

class BookGeneratorSimple:
    """Простий генератор веб-читалки з PDF"""
    
    def __init__(self, config_manager, logger):
        """Ініціалізація генератора"""
        self.config = config_manager
        self.logger = logger
        base_dir = Path(config_manager.base_dir) if hasattr(config_manager, 'base_dir') else Path.cwd()
        self.pdf_path = base_dir / 'book' / 'Konig Lear.pdf'
        self.output_dir = Path(config_manager.output_dir) / 'book'
        self.chapters = []
        self.metadata = {}
        
    def generate(self):
        """Основна функція генерації книги"""
        try:
            self.logger.info("Початок генерації веб-читалки (спрощена версія)...")
            
            # Перевірка PDF
            if not self.pdf_path.exists():
                self.logger.error(f"PDF не знайдено: {self.pdf_path}")
                # Створимо демо-версію з прикладовим текстом
                return self._generate_demo_version()
            
            # Створення структури папок
            self._create_directory_structure()
            
            if USE_PYPDF2:
                # Використовуємо PyPDF2
                self._generate_with_pypdf2()
            else:
                # Генеруємо демо-версію
                self._generate_demo_version()
            
            # Генерація стилів та JavaScript
            self._generate_styles()
            self._generate_javascript()
            
            self.logger.info(f"[OK] Згенеровано веб-читалку")
            return True
            
        except Exception as e:
            self.logger.error(f"[ERROR] Помилка генерації книги: {e}")
            # У випадку помилки генеруємо демо-версію
            return self._generate_demo_version()
    
    def _generate_demo_version(self):
        """Генерує демо-версію читалки"""
        self.logger.info("Генерація демо-версії веб-читалки...")
        
        # Створення структури папок
        self._create_directory_structure()
        
        # Створення демо-глав
        self.chapters = [
            {
                'number': 1,
                'title': 'Akt I - Der Anfang',
                'content': self._get_demo_content_1()
            },
            {
                'number': 2,
                'title': 'Akt I - Szene 2',
                'content': self._get_demo_content_2()
            },
            {
                'number': 3,
                'title': 'Akt II - Die Intrige',
                'content': self._get_demo_content_3()
            },
            {
                'number': 4,
                'title': 'Akt III - Der Sturm',
                'content': self._get_demo_content_4()
            },
            {
                'number': 5,
                'title': 'Akt IV - Die Verwandlung',
                'content': self._get_demo_content_5()
            },
            {
                'number': 6,
                'title': 'Akt V - Das Ende',
                'content': self._get_demo_content_6()
            }
        ]
        
        self.metadata = {
            'title': 'König Lear',
            'author': 'William Shakespeare',
            'translator': 'August Wilhelm Schlegel',
            'pages': 100,
            'language': 'de',
            'created': datetime.now().isoformat()
        }
        
        # Генерація HTML сторінок
        self._generate_html_pages()
        self._generate_index_page()
        self._generate_styles()
        self._generate_javascript()
        self._generate_navigation_metadata()
        
        return True
    
    def _get_demo_content_1(self):
        """Демо контент для першої глави"""
        return """
        <h2>Der Thronsaal in König Lears Schloss</h2>
        <p class="book-paragraph">
        König Lear hat beschlossen, sein Reich unter seinen drei Töchtern aufzuteilen. 
        Er versammelt den Hof und verkündet seine Absicht, sich von der Last der Herrschaft 
        zurückzuziehen.
        </p>
        <p class="book-paragraph">
        <strong>LEAR:</strong> Unterdessen wollen wir aussprechen unsre dunklere Absicht. 
        Gebt mir die Karte dort! - Wisst, dass wir unser Königreich in drei geteilt.
        </p>
        <p class="book-paragraph">
        Die ältesten Töchter, Goneril und Regan, überhäufen ihren Vater mit falschen 
        Liebesbekundungen. Doch Cordelia, die jüngste, weigert sich, ihre Liebe in 
        übertriebenen Worten auszudrücken.
        </p>
        <p class="book-paragraph">
        <strong>CORDELIA:</strong> Ich liebe Eure Majestät nach meiner Schuldigkeit, 
        nicht mehr noch minder.
        </p>
        <p class="book-paragraph">
        Lear, erzürnt über Cordelias scheinbare Undankbarkeit, verstößt sie und teilt 
        ihr Erbe zwischen Goneril und Regan auf. Der Graf von Kent versucht, für Cordelia 
        einzutreten, wird aber ebenfalls verbannt.
        </p>
        """
    
    def _get_demo_content_2(self):
        """Демо контент для другої глави"""
        return """
        <h2>Im Schloss des Grafen von Gloucester</h2>
        <p class="book-paragraph">
        Edmund, der uneheliche Sohn des Grafen von Gloucester, schmiedet einen Plan, 
        um seinen legitimen Bruder Edgar zu enterben.
        </p>
        <p class="book-paragraph">
        <strong>EDMUND:</strong> Du, Natur, bist meine Göttin; deinen Gesetzen ist mein 
        Dienst geweiht. Warum soll ich die Plage der Gewohnheit dulden?
        </p>
        <p class="book-paragraph">
        Er fälscht einen Brief, der Edgar als Verschwörer gegen seinen Vater darstellt. 
        Gloucester glaubt der Täuschung und Edgar muss fliehen.
        </p>
        <p class="book-paragraph">
        Unterdessen beginnt König Lear zu erkennen, dass seine Töchter Goneril und Regan 
        nicht die liebevollen Kinder sind, für die er sie hielt.
        </p>
        """
    
    def _get_demo_content_3(self):
        """Демо контент для третьої глави"""
        return """
        <h2>Die Heide im Sturm</h2>
        <p class="book-paragraph">
        Ein gewaltiger Sturm tobt über der Heide. König Lear, von seinen Töchtern verstoßen, 
        irrt wahnsinnig umher, begleitet nur von seinem treuen Narren.
        </p>
        <p class="book-paragraph">
        <strong>LEAR:</strong> Blast, Winde, blast! Und ihr, Katarakte und Orkane, speiet 
        bis ihr unsre Türme überflutet und die Hähne ertränkt habt!
        </p>
        <p class="book-paragraph">
        Edgar, als armer Tom verkleidet, trifft auf Lear. Der König, der selbst den Verstand 
        verliert, findet in dem scheinbar wahnsinnigen Bettler einen Seelenverwandten.
        </p>
        <p class="book-paragraph">
        <strong>EDGAR (als Tom):</strong> Tom ist kalt! O tu es nicht, tu es nicht! 
        Hilf, der böse Feind verfolgt mich!
        </p>
        """
    
    def _get_demo_content_4(self):
        """Демо контент для четвертої глави"""
        return """
        <h2>Die Klippen von Dover</h2>
        <p class="book-paragraph">
        Gloucester, dem die Augen ausgestochen wurden, weil er Lear helfen wollte, 
        wird von seinem Sohn Edgar (immer noch verkleidet) zu den Klippen von Dover geführt.
        </p>
        <p class="book-paragraph">
        <strong>GLOUCESTER:</strong> Es gibt keinen Weg mehr für mich. Die Götter sind 
        grausam, und das Leben ist mir zur Last geworden.
        </p>
        <p class="book-paragraph">
        Edgar täuscht seinen blinden Vater und rettet ihn vor dem Selbstmord, indem er 
        ihm vorgaukelt, er sei von den Klippen gesprungen und durch ein Wunder gerettet worden.
        </p>
        <p class="book-paragraph">
        Währenddessen sammelt Cordelia mit französischen Truppen eine Armee, um ihren 
        Vater zu retten.
        </p>
        """
    
    def _get_demo_content_5(self):
        """Демо контент для п'ятої глави"""
        return """
        <h2>Das Wiedersehen</h2>
        <p class="book-paragraph">
        Cordelia findet ihren wahnsinnigen Vater und pflegt ihn liebevoll. Lear erwacht 
        aus seinem Wahn und erkennt langsam seine jüngste Tochter.
        </p>
        <p class="book-paragraph">
        <strong>LEAR:</strong> Ich bin ein sehr törichter, zärtlicher alter Mann, 
        achtzig Jahre und darüber... Ich fürchte, ich bin nicht bei vollem Verstande.
        </p>
        <p class="book-paragraph">
        <strong>CORDELIA:</strong> O seht mich an, Herr, und haltet Eure Hände zum 
        Segen über mich!
        </p>
        <p class="book-paragraph">
        Doch das Glück währt nicht lange. Die Schlacht zwischen den französischen und 
        britischen Truppen naht.
        </p>
        """
    
    def _get_demo_content_6(self):
        """Демо контент для шостої глави"""
        return """
        <h2>Das tragische Ende</h2>
        <p class="book-paragraph">
        Die Schlacht ist verloren. Cordelia und Lear werden gefangen genommen. Edmund 
        befiehlt heimlich ihre Hinrichtung.
        </p>
        <p class="book-paragraph">
        Edgar besiegt Edmund im Zweikampf und enthüllt seine wahre Identität. Goneril 
        vergiftet Regan und nimmt sich dann selbst das Leben. Edmund, im Sterben liegend, 
        versucht seinen Befehl zu widerrufen, aber es ist zu spät.
        </p>
        <p class="book-paragraph">
        <strong>LEAR (mit der toten Cordelia):</strong> Heult, heult, heult, heult! 
        O ihr seid Menschen von Stein! Hätt' ich eure Zungen und Augen, ich wollte sie 
        brauchen, dass das Himmelsgewölbe bersten sollte!
        </p>
        <p class="book-paragraph">
        König Lear stirbt vor Gram über den Tod Cordelias. Edgar und Albany bleiben zurück, 
        um das verwüstete Königreich wieder aufzubauen.
        </p>
        <p class="book-paragraph">
        <strong>EDGAR:</strong> Wir, die wir jung sind, werden nie so viel sehen, 
        noch so lange leben.
        </p>
        """
    
    def _generate_with_pypdf2(self):
        """Генерація з використанням PyPDF2"""
        try:
            import PyPDF2
            
            # Відкриття PDF
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                self.metadata = {
                    'title': 'König Lear',
                    'author': 'William Shakespeare',
                    'pages': len(pdf_reader.pages),
                    'language': 'de',
                    'created': datetime.now().isoformat()
                }
                
                # Розбиття на глави (по 10 сторінок)
                pages_per_chapter = 10
                chapter_num = 1
                
                for i in range(0, len(pdf_reader.pages), pages_per_chapter):
                    chapter_content = ""
                    
                    for j in range(i, min(i + pages_per_chapter, len(pdf_reader.pages))):
                        page = pdf_reader.pages[j]
                        text = page.extract_text()
                        
                        # Форматування тексту
                        text = re.sub(r'\s+', ' ', text)
                        chapter_content += f'<p class="book-paragraph">{text}</p>\n'
                    
                    self.chapters.append({
                        'number': chapter_num,
                        'title': f'Teil {chapter_num}',
                        'content': chapter_content
                    })
                    
                    chapter_num += 1
            
            # Генерація HTML
            self._generate_html_pages()
            self._generate_index_page()
            self._generate_navigation_metadata()
            
        except Exception as e:
            self.logger.warning(f"Помилка PyPDF2: {e}, використовую демо-версію")
            return self._generate_demo_version()
    
    def _create_directory_structure(self):
        """Створює структуру папок для книги"""
        dirs = [
            self.output_dir,
            self.output_dir / 'chapters',
            self.output_dir / 'assets',
            self.output_dir / 'assets' / 'css',
            self.output_dir / 'assets' / 'js',
            self.output_dir / 'metadata'
        ]
        
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def _generate_html_pages(self):
        """Генерує HTML сторінки для кожної глави"""
        for chapter in self.chapters:
            html_content = self._create_chapter_html(chapter)
            
            chapter_file = self.output_dir / 'chapters' / f'chapter-{chapter["number"]:02d}.html'
            with open(chapter_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
    
    def _create_chapter_html(self, chapter):
        """Створює HTML для глави"""
        prev_link = ""
        next_link = ""
        
        if chapter['number'] > 1:
            prev_link = f'<a href="chapter-{chapter["number"]-1:02d}.html" class="nav-prev">⬅️ Zurück</a>'
        
        if chapter['number'] < len(self.chapters):
            next_link = f'<a href="chapter-{chapter["number"]+1:02d}.html" class="nav-next">Weiter ➡️</a>'
        
        html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter['title']} - König Lear</title>
    <link rel="stylesheet" href="../assets/css/book.css">
</head>
<body>
    <nav class="book-nav">
        <a href="../index.html" class="nav-home">📖 Inhalt</a>
        {prev_link}
        <span class="chapter-info">Teil {chapter['number']} von {len(self.chapters)}</span>
        {next_link}
    </nav>
    
    <main class="chapter-container">
        <article class="chapter-content">
            <h1 class="chapter-title">{chapter['title']}</h1>
            <div class="text-content">
                {chapter['content']}
            </div>
        </article>
    </main>
    
    <aside class="reading-tools">
        <button id="font-size-up" title="Schrift vergrößern">A+</button>
        <button id="font-size-down" title="Schrift verkleinern">A-</button>
        <button id="toggle-theme" title="Thema wechseln">🌙</button>
    </aside>
    
    <script src="../assets/js/reader.js"></script>
</body>
</html>'''
        
        return html
    
    def _generate_index_page(self):
        """Генерує головну сторінку книги"""
        toc_html = ""
        
        for chapter in self.chapters:
            toc_html += f'''
            <div class="toc-item">
                <a href="chapters/chapter-{chapter['number']:02d}.html">
                    <span class="chapter-num">{chapter['number']}.</span>
                    <span class="chapter-name">{chapter['title']}</span>
                </a>
            </div>'''
        
        html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>König Lear - William Shakespeare</title>
    <link rel="stylesheet" href="assets/css/book.css">
</head>
<body>
    <div class="book-cover">
        <header class="book-header">
            <h1 class="book-title">König Lear</h1>
            <p class="book-author">William Shakespeare</p>
            <p class="book-translator">Übersetzt von August Wilhelm Schlegel</p>
        </header>
        
        <div class="action-buttons">
            <a href="chapters/chapter-01.html" class="btn-start">📖 Lesen beginnen</a>
        </div>
    </div>
    
    <nav class="table-of-contents">
        <h2>Inhaltsverzeichnis</h2>
        <div id="toc-container">
            {toc_html}
        </div>
    </nav>
    
    <footer class="book-footer">
        <a href="../index.html">← Zurück zur Hauptseite</a>
    </footer>
    
    <script src="assets/js/book-index.js"></script>
</body>
</html>'''
        
        with open(self.output_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(html)
    
    def _generate_styles(self):
        """Генерує CSS стилі"""
        css = '''/* Стилі для веб-читалки */
:root {
    --primary: #2c3e50;
    --secondary: #34495e;
    --accent: #3498db;
    --text: #2c3e50;
    --bg: #ffffff;
    --paper: #fefefe;
}

body.dark-theme {
    --primary: #ecf0f1;
    --text: #ecf0f1;
    --bg: #1a1a1a;
    --paper: #2c2c2c;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Georgia', serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
}

.book-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: var(--primary);
    color: white;
    position: sticky;
    top: 0;
    z-index: 100;
}

.book-nav a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
}

.book-nav a:hover {
    background: rgba(255,255,255,0.1);
}

.chapter-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
}

.chapter-content {
    background: var(--paper);
    padding: 3rem;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    border-radius: 10px;
}

.chapter-title {
    text-align: center;
    color: var(--primary);
    font-size: 2.5rem;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 3px solid var(--accent);
}

.text-content {
    font-size: 18px;
    line-height: 1.8;
}

.book-paragraph {
    margin-bottom: 1.5rem;
    text-indent: 2rem;
}

.book-cover {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
    margin: 2rem;
    border-radius: 10px;
}

.book-title {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.book-author {
    font-size: 1.5rem;
    opacity: 0.9;
    margin-bottom: 0.5rem;
}

.action-buttons {
    margin-top: 2rem;
}

.btn-start {
    display: inline-block;
    padding: 1rem 2rem;
    background: white;
    color: #667eea;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    transition: transform 0.3s;
}

.btn-start:hover {
    transform: translateY(-3px);
}

.table-of-contents {
    max-width: 900px;
    margin: 3rem auto;
    padding: 2rem;
    background: white;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
}

.toc-item {
    padding: 0.75rem;
    border-bottom: 1px solid #eee;
}

.toc-item:hover {
    background: #f8f9fa;
}

.toc-item a {
    display: flex;
    gap: 1rem;
    text-decoration: none;
    color: #2c3e50;
}

.chapter-num {
    font-weight: bold;
    color: #3498db;
}

.reading-tools {
    position: fixed;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.reading-tools button {
    padding: 0.75rem;
    border: none;
    background: var(--accent);
    color: white;
    border-radius: 50%;
    cursor: pointer;
    width: 40px;
    height: 40px;
}

@media (max-width: 768px) {
    .chapter-content {
        padding: 1.5rem;
    }
    
    .reading-tools {
        bottom: 20px;
        top: auto;
        transform: none;
        flex-direction: row;
    }
}'''
        
        with open(self.output_dir / 'assets' / 'css' / 'book.css', 'w', encoding='utf-8') as f:
            f.write(css)
    
    def _generate_javascript(self):
        """Генерує JavaScript"""
        js = '''// Функції для читалки
let currentFontSize = 18;

document.getElementById('font-size-up')?.addEventListener('click', () => {
    currentFontSize += 2;
    if (currentFontSize > 32) currentFontSize = 32;
    document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
});

document.getElementById('font-size-down')?.addEventListener('click', () => {
    currentFontSize -= 2;
    if (currentFontSize < 12) currentFontSize = 12;
    document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
});

document.getElementById('toggle-theme')?.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
});'''
        
        with open(self.output_dir / 'assets' / 'js' / 'reader.js', 'w', encoding='utf-8') as f:
            f.write(js)
        
        # Book index JS
        book_index_js = '''// Головна сторінка книги
console.log('Book index loaded');'''
        
        with open(self.output_dir / 'assets' / 'js' / 'book-index.js', 'w', encoding='utf-8') as f:
            f.write(book_index_js)
    
    def _generate_navigation_metadata(self):
        """Генерує метадані навігації"""
        nav_data = {
            'chapters': [],
            'metadata': self.metadata
        }
        
        for chapter in self.chapters:
            nav_data['chapters'].append({
                'number': chapter['number'],
                'title': chapter['title'],
                'url': f'chapters/chapter-{chapter["number"]:02d}.html'
            })
        
        with open(self.output_dir / 'metadata' / 'navigation.json', 'w', encoding='utf-8') as f:
            json.dump(nav_data, f, ensure_ascii=False, indent=2)
