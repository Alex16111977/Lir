"""
Генератор веб-читалки з PDF книги "König Lear"
Використовує PyMuPDF для швидкої та якісної конвертації
"""
import fitz  # PyMuPDF
import json
import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime


class BookGenerator:
    """Генератор веб-читалки з PDF"""
    
    def __init__(self, config, logger):
        """Ініціалізація генератора книги"""
        self.config = config
        self.logger = logger
        # Використовуємо base_dir замість BASE_DIR
        base_dir = Path(config.base_dir) if hasattr(config, 'base_dir') else Path.cwd()
        self.pdf_path = base_dir / 'book' / 'Konig Lear.pdf'
        self.output_dir = Path(config.output_dir) / 'book'
        self.chapters = []
        self.metadata = {}
        
    def generate(self):
        """Основна функція генерації книги"""
        try:
            self.logger.info("Starting book generation from PDF...")
            
            # Перевіряємо наявність PDF
            if not self.pdf_path.exists():
                self.logger.error(f"PDF file not found: {self.pdf_path}")
                return False
            
            # Створюємо директорії
            self._create_directories()
            
            # Відкриваємо PDF
            doc = fitz.open(str(self.pdf_path))
            self.logger.info(f"Opened PDF: {doc.page_count} pages")
            
            # Витягуємо метадані
            self.metadata = self._extract_metadata(doc)
            
            # Розбиваємо на глави
            self.chapters = self._split_into_chapters(doc)
            self.logger.info(f"Split into {len(self.chapters)} chapters")
            
            # Генеруємо HTML сторінки
            self._generate_html_pages()
            
            # Генеруємо головну сторінку
            self._generate_index_page()
            
            # Генеруємо стилі
            self._generate_styles()
            
            # Генеруємо JavaScript
            self._generate_javascript()
            
            # Генеруємо навігацію та оглавлення
            self._generate_toc()
            
            # Генеруємо індекс для пошуку
            self._generate_search_index()
            
            doc.close()
            
            self.logger.info(f"Book generation completed! Generated {len(self.chapters)} chapters")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating book: {e}")
            return False
    
    def _create_directories(self):
        """Створює необхідні директорії"""
        dirs = [
            self.output_dir,
            self.output_dir / 'chapters',
            self.output_dir / 'assets' / 'css',
            self.output_dir / 'assets' / 'js',
            self.output_dir / 'assets' / 'images',
            self.output_dir / 'metadata'
        ]
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
    
    def _extract_metadata(self, doc):
        """Витягує метадані з PDF"""
        metadata = {
            'title': 'König Lear',
            'author': 'William Shakespeare',
            'pages': doc.page_count,
            'language': 'de',
            'generated': datetime.now().isoformat(),
            'toc': []
        }
        
        # Спробуємо витягнути оглавлення
        try:
            toc = doc.get_toc()
            for item in toc:
                metadata['toc'].append({
                    'level': item[0],
                    'title': item[1],
                    'page': item[2] - 1  # 0-based index
                })
        except:
            self.logger.warning("Could not extract TOC from PDF")
        
        # Витягуємо метадані документа
        meta = doc.metadata
        if meta:
            metadata['pdf_title'] = meta.get('title', '')
            metadata['pdf_author'] = meta.get('author', '')
            metadata['pdf_subject'] = meta.get('subject', '')
            metadata['pdf_keywords'] = meta.get('keywords', '')
        
        return metadata
    
    def _split_into_chapters(self, doc):
        """Розбиває PDF на логічні глави"""
        chapters = []
        current_chapter = None
        
        # Шаблони для виявлення початку глав
        chapter_patterns = [
            r'^\s*(AUFZUG|AKT|SZENE)\s+[IVX]+',
            r'^\s*(Erster|Zweiter|Dritter|Vierter|Fünfter)\s+(Aufzug|Akt)',
            r'^\s*(Erste|Zweite|Dritte|Vierte|Fünfte)\s+Szene',
            r'^\s*\d+\.\s+(AKT|AUFZUG)',
        ]
        
        page_buffer = []
        chapter_num = 0
        
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text()
            
            # Перевіряємо чи це початок нової глави
            is_new_chapter = False
            chapter_title = None
            
            for pattern in chapter_patterns:
                match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
                if match:
                    is_new_chapter = True
                    chapter_title = match.group(0).strip()
                    break
            
            # Якщо нова глава або перша сторінка
            if is_new_chapter or page_num == 0:
                # Зберігаємо попередню главу
                if page_buffer:
                    chapter_num += 1
                    chapters.append(self._create_chapter(doc, page_buffer, chapter_num, current_chapter))
                
                # Починаємо нову главу
                current_chapter = chapter_title or f'Глава {chapter_num + 1}'
                page_buffer = [page_num]
            else:
                # Додаємо сторінку до поточної глави
                page_buffer.append(page_num)
        
        # Додаємо останню главу
        if page_buffer:
            chapter_num += 1
            chapters.append(self._create_chapter(doc, page_buffer, chapter_num, current_chapter))
        
        # Якщо глав занадто мало, розбиваємо по сторінках
        if len(chapters) < 3:
            return self._split_by_pages(doc)
        
        return chapters
    
    def _create_chapter(self, doc, page_numbers, chapter_num, title):
        """Створює об'єкт глави"""
        chapter = {
            'number': chapter_num,
            'title': title or f'Глава {chapter_num}',
            'pages': page_numbers,
            'content': '',
            'text_content': '',
            'images': []
        }
        
        # Збираємо контент всіх сторінок глави
        for page_num in page_numbers:
            page = doc[page_num]
            
            # Витягуємо текст в HTML форматі
            html_content = page.get_text('html')
            chapter['content'] += self._process_page_html(html_content, page_num)
            
            # Витягуємо чистий текст для пошуку
            chapter['text_content'] += page.get_text()
            
            # Витягуємо зображення
            images = self._extract_images(page, page_num)
            chapter['images'].extend(images)
        
        return chapter
    
    def _split_by_pages(self, doc, pages_per_chapter=10):
        """Альтернативне розбиття по сторінках"""
        chapters = []
        total_pages = doc.page_count
        
        for start_page in range(0, total_pages, pages_per_chapter):
            end_page = min(start_page + pages_per_chapter, total_pages)
            page_buffer = list(range(start_page, end_page))
            
            chapter_num = (start_page // pages_per_chapter) + 1
            chapters.append(self._create_chapter(
                doc, 
                page_buffer, 
                chapter_num,
                f'Teil {chapter_num}'
            ))
        
        return chapters
    
    def _process_page_html(self, html, page_num):
        """Обробляє HTML контент сторінки"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Видаляємо непотрібні стилі
        for tag in soup.find_all(['style', 'script']):
            tag.decompose()
        
        # Додаємо класи для стилізації
        for p in soup.find_all('p'):
            p['class'] = 'book-paragraph'
        
        for span in soup.find_all('span'):
            # Зберігаємо стилі шрифту
            style = span.get('style', '')
            if 'bold' in style or 'font-weight' in style:
                span['class'] = 'text-bold'
            if 'italic' in style:
                span['class'] = 'text-italic'
        
        # Додаємо маркер сторінки
        page_marker = soup.new_tag('div', **{'class': 'page-marker', 'data-page': str(page_num + 1)})
        page_marker.string = f'Seite {page_num + 1}'
        soup.insert(0, page_marker)
        
        return str(soup)
    
    def _extract_images(self, page, page_num):
        """Витягує зображення зі сторінки"""
        images = []
        image_list = page.get_images()
        
        for img_index, img in enumerate(image_list):
            try:
                # Отримуємо зображення
                xref = img[0]
                pix = fitz.Pixmap(page.parent, xref)
                
                if pix.n - pix.alpha < 4:  # GRAY or RGB
                    img_path = self.output_dir / 'assets' / 'images' / f'page_{page_num}_img_{img_index}.png'
                    pix.save(str(img_path))
                    images.append({
                        'path': f'../assets/images/page_{page_num}_img_{img_index}.png',
                        'page': page_num,
                        'index': img_index
                    })
                else:  # CMYK
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    img_path = self.output_dir / 'assets' / 'images' / f'page_{page_num}_img_{img_index}.png'
                    pix1.save(str(img_path))
                    images.append({
                        'path': f'../assets/images/page_{page_num}_img_{img_index}.png',
                        'page': page_num,
                        'index': img_index
                    })
                    pix1 = None
                
                pix = None
                
            except Exception as e:
                self.logger.warning(f"Could not extract image {img_index} from page {page_num}: {e}")
        
        return images
    
    def _generate_html_pages(self):
        """Генерує HTML сторінки для кожної глави"""
        for i, chapter in enumerate(self.chapters):
            chapter_html = self._create_chapter_html(chapter, i, len(self.chapters))
            
            chapter_file = self.output_dir / 'chapters' / f'chapter-{i+1:02d}.html'
            with open(chapter_file, 'w', encoding='utf-8') as f:
                f.write(chapter_html)
    
    def _create_chapter_html(self, chapter, chapter_index, total_chapters):
        """Створює HTML для однієї глави"""
        prev_link = ''
        next_link = ''
        
        if chapter_index > 0:
            prev_link = f'<a href="chapter-{chapter_index:02d}.html" class="nav-prev">← Vorherige</a>'
        
        if chapter_index < total_chapters - 1:
            next_link = f'<a href="chapter-{chapter_index + 2:02d}.html" class="nav-next">Nächste →</a>'
        
        template = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter['title']} - König Lear</title>
    <link rel="stylesheet" href="../assets/css/book.css">
    <link rel="stylesheet" href="../assets/css/reader.css">
</head>
<body>
    <nav class="book-nav">
        <div class="nav-left">
            <a href="../index.html" class="nav-home">📖 Hauptseite</a>
        </div>
        <div class="nav-center">
            <span class="chapter-info">Kapitel {chapter_index + 1} von {total_chapters}</span>
        </div>
        <div class="nav-right">
            {prev_link}
            {next_link}
        </div>
    </nav>
    
    <main class="chapter-content">
        <h1 class="chapter-title">{chapter['title']}</h1>
        <div class="text-content" id="text-content">
            {chapter['content']}
        </div>
    </main>
    
    <aside class="reading-tools">
        <button id="font-size-up" title="Schrift vergrößern">A+</button>
        <button id="font-size-down" title="Schrift verkleinern">A-</button>
        <button id="toggle-theme" title="Thema wechseln">🌙</button>
        <button id="fullscreen" title="Vollbild">⛶</button>
        <button id="bookmark" title="Lesezeichen">🔖</button>
    </aside>
    
    <div class="progress-bar">
        <div class="progress-fill" id="progress-fill"></div>
    </div>
    
    <script src="../assets/js/reader.js"></script>
    <script src="../assets/js/navigation.js"></script>
</body>
</html>'''
        return template
    
    def _generate_index_page(self):
        """Генерує головну сторінку книги"""
        chapters_html = ''
        for i, chapter in enumerate(self.chapters):
            chapters_html += f'''
            <div class="chapter-card">
                <div class="chapter-number">Kapitel {i + 1}</div>
                <h3 class="chapter-link-title">{chapter['title']}</h3>
                <div class="chapter-meta">
                    <span>Seiten: {chapter['pages'][0] + 1}-{chapter['pages'][-1] + 1}</span>
                    <span>({len(chapter['pages'])} Seiten)</span>
                </div>
                <a href="chapters/chapter-{i+1:02d}.html" class="chapter-link">Lesen →</a>
            </div>
            '''
        
        index_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>König Lear - William Shakespeare</title>
    <link rel="stylesheet" href="assets/css/book.css">
    <link rel="stylesheet" href="assets/css/index.css">
</head>
<body>
    <header class="book-header">
        <div class="book-cover">
            <h1 class="book-title">König Lear</h1>
            <p class="book-author">William Shakespeare</p>
            <div class="book-meta">
                <span>📚 {len(self.chapters)} Kapitel</span>
                <span>📄 {self.metadata['pages']} Seiten</span>
            </div>
        </div>
    </header>
    
    <nav class="book-navigation">
        <a href="../index.html" class="back-to-main">← Zurück zum Hauptportal</a>
    </nav>
    
    <main class="book-main">
        <section class="table-of-contents">
            <h2>Inhaltsverzeichnis</h2>
            <div class="chapters-grid">
                {chapters_html}
            </div>
        </section>
        
        <section class="reading-features">
            <h2>Lesefunktionen</h2>
            <div class="features-grid">
                <div class="feature">
                    <span class="feature-icon">🔍</span>
                    <h3>Suche</h3>
                    <p>Volltextsuche im gesamten Buch</p>
                </div>
                <div class="feature">
                    <span class="feature-icon">🔖</span>
                    <h3>Lesezeichen</h3>
                    <p>Speichern Sie Ihre Leseposition</p>
                </div>
                <div class="feature">
                    <span class="feature-icon">🎨</span>
                    <h3>Themen</h3>
                    <p>Hell und Dunkel Modi</p>
                </div>
                <div class="feature">
                    <span class="feature-icon">📱</span>
                    <h3>Responsive</h3>
                    <p>Optimiert für alle Geräte</p>
                </div>
            </div>
        </section>
    </main>
    
    <footer class="book-footer">
        <p>Generiert am {self.metadata['generated'][:10]}</p>
        <p>Lir Website Generator - Deutsch durch König Lear</p>
    </footer>
    
    <script src="assets/js/book-index.js"></script>
</body>
</html>'''
        
        index_file = self.output_dir / 'index.html'
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_html)
    
    def _generate_styles(self):
        """Генерує CSS стилі"""
        # Основні стилі книги
        book_css = ''':root {
    --book-primary: #2c3e50;
    --book-secondary: #34495e;
    --book-accent: #3498db;
    --book-text: #2c3e50;
    --book-bg: #ffffff;
    --book-paper: #fefefe;
    --book-border: #e0e0e0;
}

[data-theme="dark"] {
    --book-primary: #ecf0f1;
    --book-secondary: #bdc3c7;
    --book-accent: #3498db;
    --book-text: #ecf0f1;
    --book-bg: #1a1a1a;
    --book-paper: #2c2c2c;
    --book-border: #444;
}

body {
    margin: 0;
    padding: 0;
    font-family: 'Georgia', serif;
    background: var(--book-bg);
    color: var(--book-text);
    line-height: 1.6;
}

.book-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: var(--book-primary);
    color: white;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.nav-left, .nav-center, .nav-right {
    flex: 1;
    display: flex;
    align-items: center;
}

.nav-center {
    justify-content: center;
}

.nav-right {
    justify-content: flex-end;
    gap: 1rem;
}

.nav-home, .nav-prev, .nav-next {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background 0.3s ease;
}

.nav-home:hover, .nav-prev:hover, .nav-next:hover {
    background: rgba(255,255,255,0.1);
}

.chapter-content {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: var(--book-paper);
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    border-radius: 10px;
}

.chapter-title {
    text-align: center;
    color: var(--book-primary);
    border-bottom: 2px solid var(--book-accent);
    padding-bottom: 1rem;
    margin-bottom: 2rem;
    font-size: 2rem;
}

.text-content {
    font-size: 18px;
    line-height: 1.8;
}

.book-paragraph {
    margin: 1rem 0;
    text-align: justify;
}

.page-marker {
    font-size: 0.8rem;
    color: var(--book-secondary);
    text-align: right;
    margin: 2rem 0;
    padding-top: 1rem;
    border-top: 1px solid var(--book-border);
}

.reading-tools {
    position: fixed;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    z-index: 90;
}

.reading-tools button {
    width: 50px;
    height: 50px;
    border: none;
    background: var(--book-accent);
    color: white;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.reading-tools button:hover {
    transform: scale(1.1);
    box-shadow: 0 3px 10px rgba(0,0,0,0.3);
}

.progress-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--book-border);
    z-index: 100;
}

.progress-fill {
    height: 100%;
    background: var(--book-accent);
    width: 0;
    transition: width 0.3s ease;
}

@media (max-width: 768px) {
    .chapter-content {
        margin: 1rem;
        padding: 1rem;
        border-radius: 0;
    }
    
    .reading-tools {
        position: fixed;
        bottom: 20px;
        right: 50%;
        transform: translateX(50%);
        flex-direction: row;
        top: auto;
    }
    
    .reading-tools button {
        width: 40px;
        height: 40px;
        font-size: 1rem;
    }
    
    .book-nav {
        padding: 0.5rem 1rem;
        flex-wrap: wrap;
    }
    
    .nav-left, .nav-center, .nav-right {
        flex: auto;
        font-size: 0.9rem;
    }
}

.text-bold {
    font-weight: bold;
}

.text-italic {
    font-style: italic;
}'''
        
        book_css_file = self.output_dir / 'assets' / 'css' / 'book.css'
        with open(book_css_file, 'w', encoding='utf-8') as f:
            f.write(book_css)
        
        # Стилі для головної сторінки
        index_css = '''.book-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
}

.book-cover {
    max-width: 600px;
    margin: 0 auto;
}

.book-title {
    font-size: 3rem;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.book-author {
    font-size: 1.5rem;
    margin: 1rem 0;
    opacity: 0.9;
}

.book-meta {
    margin-top: 2rem;
    display: flex;
    gap: 2rem;
    justify-content: center;
    font-size: 1.1rem;
}

.book-navigation {
    padding: 1rem;
    background: var(--book-paper);
    border-bottom: 1px solid var(--book-border);
}

.back-to-main {
    color: var(--book-accent);
    text-decoration: none;
    font-size: 1.1rem;
    transition: color 0.3s ease;
}

.back-to-main:hover {
    color: var(--book-primary);
}

.book-main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

.table-of-contents h2 {
    text-align: center;
    color: var(--book-primary);
    font-size: 2rem;
    margin-bottom: 2rem;
}

.chapters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
}

.chapter-card {
    background: var(--book-paper);
    border: 1px solid var(--book-border);
    border-radius: 10px;
    padding: 1.5rem;
    transition: all 0.3s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.chapter-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.chapter-number {
    font-size: 0.9rem;
    color: var(--book-accent);
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.chapter-link-title {
    color: var(--book-primary);
    margin: 0.5rem 0;
}

.chapter-meta {
    font-size: 0.9rem;
    color: var(--book-secondary);
    margin: 0.5rem 0;
}

.chapter-link {
    display: inline-block;
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    background: var(--book-accent);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s ease;
}

.chapter-link:hover {
    background: var(--book-primary);
}

.reading-features {
    margin-top: 3rem;
}

.reading-features h2 {
    text-align: center;
    color: var(--book-primary);
    font-size: 2rem;
    margin-bottom: 2rem;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.feature {
    text-align: center;
    padding: 1.5rem;
    background: var(--book-paper);
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.feature-icon {
    font-size: 3rem;
    display: block;
    margin-bottom: 1rem;
}

.feature h3 {
    color: var(--book-primary);
    margin: 0.5rem 0;
}

.feature p {
    color: var(--book-secondary);
    font-size: 0.95rem;
}

.book-footer {
    text-align: center;
    padding: 2rem;
    background: var(--book-paper);
    border-top: 1px solid var(--book-border);
    color: var(--book-secondary);
    margin-top: 3rem;
}'''
        
        index_css_file = self.output_dir / 'assets' / 'css' / 'index.css'
        with open(index_css_file, 'w', encoding='utf-8') as f:
            f.write(index_css)
        
        # Reader CSS додатковий
        reader_css = '''/* Додаткові стилі для читача */
.highlight {
    background-color: yellow;
    padding: 2px;
}

.bookmark-marker {
    position: absolute;
    left: -30px;
    font-size: 1.5rem;
    color: var(--book-accent);
}

.search-highlight {
    background-color: #ffeb3b;
    padding: 2px;
    border-radius: 3px;
}

@media print {
    .book-nav, .reading-tools, .progress-bar {
        display: none;
    }
    
    .chapter-content {
        box-shadow: none;
        max-width: 100%;
    }
}'''
        
        reader_css_file = self.output_dir / 'assets' / 'css' / 'reader.css'
        with open(reader_css_file, 'w', encoding='utf-8') as f:
            f.write(reader_css)
    
    def _generate_javascript(self):
        """Генерує JavaScript код"""
        # Основний JavaScript для читача
        reader_js = '''// Функції читання
let currentFontSize = 18;
const MIN_FONT_SIZE = 12;
const MAX_FONT_SIZE = 32;

// Збільшення шрифту
document.getElementById('font-size-up')?.addEventListener('click', () => {
    if (currentFontSize < MAX_FONT_SIZE) {
        currentFontSize += 2;
        document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
        localStorage.setItem('fontSize', currentFontSize);
    }
});

// Зменшення шрифту
document.getElementById('font-size-down')?.addEventListener('click', () => {
    if (currentFontSize > MIN_FONT_SIZE) {
        currentFontSize -= 2;
        document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
        localStorage.setItem('fontSize', currentFontSize);
    }
});

// Перемикання теми
document.getElementById('toggle-theme')?.addEventListener('click', () => {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Оновлюємо іконку кнопки
    const button = document.getElementById('toggle-theme');
    button.textContent = newTheme === 'dark' ? '☀️' : '🌙';
});

// Повноекранний режим
document.getElementById('fullscreen')?.addEventListener('click', () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        document.exitFullscreen();
    }
});

// Закладки
document.getElementById('bookmark')?.addEventListener('click', () => {
    const chapter = window.location.pathname.split('/').pop();
    const scrollPosition = window.scrollY;
    
    const bookmark = {
        chapter: chapter,
        position: scrollPosition,
        date: new Date().toISOString()
    };
    
    localStorage.setItem('bookmark', JSON.stringify(bookmark));
    
    // Візуальний фідбек
    const button = document.getElementById('bookmark');
    button.style.transform = 'scale(1.2)';
    setTimeout(() => {
        button.style.transform = 'scale(1)';
    }, 300);
});

// Прогрес читання
function updateProgress() {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    
    const progressBar = document.getElementById('progress-fill');
    if (progressBar) {
        progressBar.style.width = scrolled + '%';
    }
    
    // Зберігаємо позицію читання
    const chapter = window.location.pathname.split('/').pop();
    localStorage.setItem(`reading-position-${chapter}`, winScroll);
}

window.addEventListener('scroll', updateProgress);

// Відновлення налаштувань при завантаженні
window.addEventListener('load', () => {
    // Відновлюємо розмір шрифту
    const savedFontSize = localStorage.getItem('fontSize');
    if (savedFontSize) {
        currentFontSize = parseInt(savedFontSize);
        document.querySelector('.text-content').style.fontSize = currentFontSize + 'px';
    }
    
    // Відновлюємо тему
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
        const button = document.getElementById('toggle-theme');
        if (button) {
            button.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
        }
    }
    
    // Відновлюємо позицію читання
    const chapter = window.location.pathname.split('/').pop();
    const savedPosition = localStorage.getItem(`reading-position-${chapter}`);
    if (savedPosition) {
        window.scrollTo(0, parseInt(savedPosition));
    }
});

// Клавіші швидкого доступу
document.addEventListener('keydown', (e) => {
    // Alt + → для наступної глави
    if (e.altKey && e.key === 'ArrowRight') {
        const nextLink = document.querySelector('.nav-next');
        if (nextLink) nextLink.click();
    }
    
    // Alt + ← для попередньої глави
    if (e.altKey && e.key === 'ArrowLeft') {
        const prevLink = document.querySelector('.nav-prev');
        if (prevLink) prevLink.click();
    }
    
    // F11 для повноекранного режиму
    if (e.key === 'F11') {
        e.preventDefault();
        document.getElementById('fullscreen').click();
    }
});'''
        
        reader_js_file = self.output_dir / 'assets' / 'js' / 'reader.js'
        with open(reader_js_file, 'w', encoding='utf-8') as f:
            f.write(reader_js)
        
        # JavaScript для навігації
        navigation_js = '''// Навігація між главами

// Плавна прокрутка до якорів
function smoothScrollTo(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Обробка посилань на якорі
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const target = link.getAttribute('href');
        smoothScrollTo(target);
    });
});

// Swipe жести для мобільних пристроїв
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;
    
    if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
            // Swipe вліво - наступна глава
            const nextLink = document.querySelector('.nav-next');
            if (nextLink) nextLink.click();
        } else {
            // Swipe вправо - попередня глава
            const prevLink = document.querySelector('.nav-prev');
            if (prevLink) prevLink.click();
        }
    }
}

// Показувати номер сторінки при наведенні
const pageMarkers = document.querySelectorAll('.page-marker');
pageMarkers.forEach(marker => {
    marker.addEventListener('mouseenter', () => {
        marker.style.opacity = '1';
    });
    
    marker.addEventListener('mouseleave', () => {
        marker.style.opacity = '0.5';
    });
});'''
        
        navigation_js_file = self.output_dir / 'assets' / 'js' / 'navigation.js'
        with open(navigation_js_file, 'w', encoding='utf-8') as f:
            f.write(navigation_js)
        
        # JavaScript для головної сторінки
        book_index_js = '''// JavaScript для головної сторінки книги

// Перевірка на закладки
window.addEventListener('load', () => {
    const bookmark = localStorage.getItem('bookmark');
    
    if (bookmark) {
        const data = JSON.parse(bookmark);
        const continueReading = confirm('Sie haben ein Lesezeichen. Möchten Sie weiterlesen?');
        
        if (continueReading) {
            window.location.href = `chapters/${data.chapter}`;
        }
    }
    
    // Показуємо прогрес читання
    showReadingProgress();
});

function showReadingProgress() {
    const chapters = document.querySelectorAll('.chapter-card');
    
    chapters.forEach((card, index) => {
        const chapterFile = `chapter-${String(index + 1).padStart(2, '0')}.html`;
        const position = localStorage.getItem(`reading-position-${chapterFile}`);
        
        if (position && parseInt(position) > 100) {
            const badge = document.createElement('span');
            badge.className = 'reading-badge';
            badge.textContent = '✓ Gelesen';
            badge.style.cssText = `
                position: absolute;
                top: 10px;
                right: 10px;
                background: #27ae60;
                color: white;
                padding: 5px 10px;
                border-radius: 20px;
                font-size: 0.8rem;
            `;
            card.style.position = 'relative';
            card.appendChild(badge);
        }
    });
}

// Анімація карток глав
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
});

document.querySelectorAll('.chapter-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.5s ease';
    observer.observe(card);
});'''
        
        book_index_js_file = self.output_dir / 'assets' / 'js' / 'book-index.js'
        with open(book_index_js_file, 'w', encoding='utf-8') as f:
            f.write(book_index_js)
    
    def _generate_toc(self):
        """Генерує оглавлення в JSON форматі"""
        toc_data = {
            'title': 'König Lear',
            'author': 'William Shakespeare',
            'chapters': []
        }
        
        for i, chapter in enumerate(self.chapters):
            toc_data['chapters'].append({
                'number': i + 1,
                'title': chapter['title'],
                'file': f'chapters/chapter-{i+1:02d}.html',
                'pages': {
                    'start': chapter['pages'][0] + 1,
                    'end': chapter['pages'][-1] + 1,
                    'count': len(chapter['pages'])
                }
            })
        
        toc_file = self.output_dir / 'metadata' / 'toc.json'
        with open(toc_file, 'w', encoding='utf-8') as f:
            json.dump(toc_data, f, ensure_ascii=False, indent=2)
    
    def _generate_search_index(self):
        """Генерує індекс для повнотекстового пошуку"""
        search_index = {
            'version': '1.0',
            'generated': datetime.now().isoformat(),
            'documents': []
        }
        
        for i, chapter in enumerate(self.chapters):
            # Розбиваємо текст на фрагменти для кращого пошуку
            text_chunks = self._split_text_into_chunks(chapter['text_content'], 500)
            
            for j, chunk in enumerate(text_chunks):
                search_index['documents'].append({
                    'id': f'chapter-{i+1}-chunk-{j+1}',
                    'chapter': i + 1,
                    'chapter_title': chapter['title'],
                    'chunk': j + 1,
                    'content': chunk,
                    'url': f'chapters/chapter-{i+1:02d}.html'
                })
        
        search_file = self.output_dir / 'metadata' / 'search-index.json'
        with open(search_file, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, ensure_ascii=False, indent=2)
    
    def _split_text_into_chunks(self, text, chunk_size):
        """Розбиває текст на частини для пошуку"""
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size])
            if chunk.strip():
                chunks.append(chunk)
        
        return chunks