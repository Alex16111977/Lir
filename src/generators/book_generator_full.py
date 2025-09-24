"""
Генератор HTML для КОЖНОЇ сторінки PDF книги
Створює окремий HTML файл для кожної з 160 сторінок
"""

import fitz
import json
import os
from pathlib import Path
from datetime import datetime
import html
import shutil

class BookGeneratorFull:
    """Генератор HTML для КОЖНОЇ сторінки PDF"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        base_dir = Path(config.base_dir) if hasattr(config, 'base_dir') else Path.cwd()
        self.pdf_path = base_dir / 'book' / 'Konig Lear.pdf'
        self.output_dir = Path(config.output_dir) / 'book'
        self.pages_dir = self.output_dir / 'pages'  # НЕ chapters!
        self.pages_data = []
        
    def generate(self):
        """Головна функція - генерує ВСІ сторінки"""
        try:
            # 1. Перевірка PDF
            if not self.pdf_path.exists():
                self.logger.error(f"PDF not found: {self.pdf_path}")
                return False
            
            # 2. Створення директорій
            self._create_directories()
            
            # 3. Відкриваємо PDF
            doc = fitz.open(str(self.pdf_path))
            total_pages = doc.page_count
            self.logger.info(f"[!] Processing {total_pages} pages...")
            
            # 4. Генеруємо КОЖНУ сторінку
            for page_num in range(total_pages):
                page = doc[page_num]
                page_data = self._process_page(page, page_num, total_pages)
                self.pages_data.append(page_data)
                
                # Генеруємо HTML
                html_content = self._generate_page_html(page_data, page_num, total_pages)
                
                # Зберігаємо
                output_file = self.pages_dir / f'page-{page_num + 1:03d}.html'
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                # Прогрес кожні 10 сторінок
                if (page_num + 1) % 10 == 0:
                    self.logger.info(f"  Processed {page_num + 1}/{total_pages} pages...")
            
            doc.close()
            
            # 5. Генеруємо головну сторінку
            self._generate_main_index(total_pages)
            
            # 6. Генеруємо стилі та JS
            self._generate_assets()
            
            # 7. Зберігаємо метадані
            self._save_metadata(total_pages)
            
            self.logger.info(f"[OK] Generated {total_pages} HTML pages!")
            return True
            
        except Exception as e:
            self.logger.error(f"Error: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            return False
    
    def _create_directories(self):
        """Створює необхідні директорії"""
        dirs = [
            self.output_dir,
            self.pages_dir,  # pages, не chapters!
            self.output_dir / 'assets' / 'css',
            self.output_dir / 'assets' / 'js',
            self.output_dir / 'assets' / 'images',
            self.output_dir / 'metadata'
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
    
    def _process_page(self, page, page_num, total_pages):
        """Витягує РЕАЛЬНИЙ контент зі сторінки PDF"""
        # Витягуємо текст
        text_plain = page.get_text()
        text_html = page.get_text('html')
        
        # Витягуємо зображення
        images = []
        for img_index, img in enumerate(page.get_images()):
            try:
                xref = img[0]
                pix = fitz.Pixmap(page.parent, xref)
                if pix.n - pix.alpha < 4:  # RGB або Grayscale
                    img_path = self.output_dir / 'assets' / 'images' / f'page-{page_num + 1:03d}-img-{img_index + 1}.png'
                    pix.save(str(img_path))
                    images.append(f'../assets/images/page-{page_num + 1:03d}-img-{img_index + 1}.png')
                pix = None
            except:
                pass
        
        return {
            'page_num': page_num + 1,
            'text_plain': text_plain,
            'text_html': text_html,
            'images': images,
            'has_content': len(text_plain.strip()) > 0
        }
    
    def _generate_page_html(self, page_data, page_num, total_pages):
        """Генерує HTML для однієї сторінки"""
        current = page_num + 1
        prev_page = f'page-{page_num:03d}.html' if page_num > 0 else None
        next_page = f'page-{page_num + 2:03d}.html' if page_num < total_pages - 1 else None
        
        # Обробляємо текст
        content = page_data['text_plain']
        if not content.strip():
            content = '<p style="color: #999; text-align: center;">[Ця сторінка порожня або містить лише зображення]</p>'
        else:
            # Escape HTML і зберігаємо переноси рядків та структуру
            content = html.escape(content)
            # Зберігаємо параграфи
            paragraphs = content.split('\n\n')
            content = ''.join([f'<p>{p.replace(chr(10), "<br>")}</p>' for p in paragraphs if p.strip()])
        
        # HTML шаблон
        return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seite {current} - König Lear</title>
    <link rel="stylesheet" href="../assets/css/book.css">
</head>
<body>
    <nav class="book-nav">
        <a href="../index.html" class="nav-home">📖 Inhalt</a>
        <div class="nav-pagination">
            {f'<a href="{prev_page}" class="nav-prev">← Seite {current - 1}</a>' if prev_page else '<span></span>'}
            <span class="page-info">Seite {current} von {total_pages}</span>
            {f'<a href="{next_page}" class="nav-next">Seite {current + 1} →</a>' if next_page else '<span></span>'}
        </div>
    </nav>
    
    <main class="page-content">
        <div class="page-text">
            {content}
        </div>
        
        {''.join([f'<img src="{img}" class="page-image" alt="Seite {current} Bild">' for img in page_data['images']]) if page_data['images'] else ''}
    </main>
    
    <aside class="reading-tools">
        <button onclick="changeFontSize(2)" title="Schrift vergrößern">A+</button>
        <button onclick="changeFontSize(-2)" title="Schrift verkleinern">A-</button>
        <button onclick="toggleTheme()" title="Thema wechseln">🌙</button>
        <button onclick="goToPage()" title="Zu Seite springen">📄</button>
    </aside>
    
    <script src="../assets/js/reader.js"></script>
</body>
</html>'''
    
    def _generate_main_index(self, total_pages):
        """Генерує головну сторінку книги з навігацією по всіх сторінках"""
        
        # Створюємо блоки по 50 сторінок для навігації
        chapters_nav = ''
        for start in range(0, total_pages, 50):
            end = min(start + 50, total_pages)
            chapters_nav += f'''
            <div class="pages-block">
                <h3>Seiten {start + 1} - {end}</h3>
                <div class="pages-links">'''
            
            for p in range(start, end):
                if (p - start) % 10 == 0 and p > start:
                    chapters_nav += '<br>'
                chapters_nav += f'<a href="pages/page-{p + 1:03d}.html" class="page-link">{p + 1}</a> '
            
            chapters_nav += '''
                </div>
            </div>'''
        
        index_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>König Lear - {total_pages} Seiten</title>
    <link rel="stylesheet" href="assets/css/book-index.css">
</head>
<body>
    <div class="header">
        <h1>König Lear</h1>
        <p class="author">William Shakespeare</p>
        <p class="pages-count">{total_pages} Seiten</p>
    </div>
    
    <div class="quick-nav">
        <a href="pages/page-001.html">Anfang</a>
        <a href="pages/page-{total_pages//2:03d}.html">Mitte</a>
        <a href="pages/page-{total_pages:03d}.html">Ende</a>
    </div>
    
    <div class="search-box">
        <input type="number" id="pageNum" min="1" max="{total_pages}" placeholder="Seite nummer">
        <button onclick="goToPage()">Gehe zu Seite</button>
    </div>
    
    <h2>Alle Seiten:</h2>
    {chapters_nav}
    
    <script>
        function goToPage() {{
            const num = document.getElementById('pageNum').value;
            if (num >= 1 && num <= {total_pages}) {{
                window.location.href = 'pages/page-' + String(num).padStart(3, '0') + '.html';
            }}
        }}
    </script>
</body>
</html>'''
        
        with open(self.output_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
    
    def _generate_assets(self):
        """Генерує CSS та JS файли"""
        
        # CSS для сторінок книги
        book_css = '''/* Стилі для сторінок книги */
body {
    font-family: Georgia, serif;
    margin: 0;
    padding: 0;
    background: #f5f5f5;
    color: #333;
}

.book-nav {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.nav-home {
    color: white;
    text-decoration: none;
    font-size: 18px;
}

.nav-pagination {
    display: flex;
    gap: 20px;
    align-items: center;
}

.nav-prev, .nav-next {
    color: white;
    text-decoration: none;
    padding: 5px 15px;
    background: rgba(255,255,255,0.2);
    border-radius: 5px;
    transition: background 0.3s;
}

.nav-prev:hover, .nav-next:hover {
    background: rgba(255,255,255,0.3);
}

.page-info {
    font-weight: bold;
}

.page-content {
    max-width: 900px;
    margin: 30px auto;
    padding: 40px;
    background: white;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    min-height: 600px;
}

.page-text {
    line-height: 1.8;
    font-size: 18px;
}

.page-text p {
    margin-bottom: 1.2em;
}

.page-image {
    max-width: 100%;
    height: auto;
    margin: 20px 0;
}

.reading-tools {
    position: fixed;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.reading-tools button {
    width: 50px;
    height: 50px;
    border: none;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    border-radius: 50%;
    cursor: pointer;
    font-size: 20px;
    transition: all 0.3s;
}

.reading-tools button:hover {
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transform: scale(1.1);
}

/* Dark theme */
body.dark-theme {
    background: #1a1a1a;
    color: #e0e0e0;
}

body.dark-theme .page-content {
    background: #2a2a2a;
    color: #e0e0e0;
}

body.dark-theme .reading-tools button {
    background: #3a3a3a;
    color: #e0e0e0;
}'''
        
        css_file = self.output_dir / 'assets' / 'css' / 'book.css'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(book_css)
        
        # CSS для головної сторінки
        index_css = '''/* Стилі для головної сторінки книги */
body {
    font-family: Georgia, serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background: #f5f5f5;
}

.header {
    text-align: center;
    padding: 40px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.header h1 {
    margin: 0;
    font-size: 48px;
}

.author {
    font-size: 24px;
    margin: 10px 0;
}

.pages-count {
    font-size: 18px;
    opacity: 0.9;
}

.quick-nav {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 30px 0;
}

.quick-nav a {
    padding: 12px 30px;
    background: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: all 0.3s;
    font-size: 16px;
}

.quick-nav a:hover {
    background: #2980b9;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(52, 152, 219, 0.3);
}

.search-box {
    text-align: center;
    margin: 30px 0;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.search-box input {
    padding: 10px 15px;
    width: 200px;
    font-size: 16px;
    border: 2px solid #ddd;
    border-radius: 5px;
    margin-right: 10px;
}

.search-box button {
    padding: 10px 20px;
    background: #27ae60;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
    border-radius: 5px;
    transition: all 0.3s;
}

.search-box button:hover {
    background: #229954;
}

h2 {
    text-align: center;
    color: #333;
    margin: 30px 0 20px;
}

.pages-block {
    margin: 20px 0;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.pages-block h3 {
    color: #667eea;
    margin-bottom: 15px;
}

.pages-links {
    line-height: 2.5;
}

.page-link {
    display: inline-block;
    width: 40px;
    text-align: center;
    margin: 2px;
    padding: 8px;
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    text-decoration: none;
    color: #495057;
    border-radius: 3px;
    transition: all 0.2s;
}

.page-link:hover {
    background: #667eea;
    color: white;
    transform: scale(1.1);
}'''
        
        index_css_file = self.output_dir / 'assets' / 'css' / 'book-index.css'
        with open(index_css_file, 'w', encoding='utf-8') as f:
            f.write(index_css)
        
        # JavaScript для читалки
        reader_js = '''// Reader functionality
let currentFontSize = 18;

function changeFontSize(delta) {
    currentFontSize += delta;
    currentFontSize = Math.max(12, Math.min(currentFontSize, 32));
    document.querySelector('.page-text').style.fontSize = currentFontSize + 'px';
    localStorage.setItem('fontSize', currentFontSize);
}

function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    const isDark = document.body.classList.contains('dark-theme');
    localStorage.setItem('darkTheme', isDark);
    
    const themeButton = document.querySelector('[onclick="toggleTheme()"]');
    if (themeButton) {
        themeButton.textContent = isDark ? '☀️' : '🌙';
    }
}

function goToPage() {
    const pageNum = prompt('Zu welcher Seite möchten Sie springen?');
    if (pageNum && !isNaN(pageNum)) {
        const targetPage = 'page-' + String(pageNum).padStart(3, '0') + '.html';
        window.location.href = targetPage;
    }
}

// Load saved preferences
document.addEventListener('DOMContentLoaded', function() {
    const savedFontSize = localStorage.getItem('fontSize');
    if (savedFontSize) {
        currentFontSize = parseInt(savedFontSize);
        document.querySelector('.page-text').style.fontSize = currentFontSize + 'px';
    }
    
    const isDark = localStorage.getItem('darkTheme') === 'true';
    if (isDark) {
        document.body.classList.add('dark-theme');
        const themeButton = document.querySelector('[onclick="toggleTheme()"]');
        if (themeButton) {
            themeButton.textContent = '☀️';
        }
    }
});

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
        const prevLink = document.querySelector('.nav-prev');
        if (prevLink) prevLink.click();
    } else if (e.key === 'ArrowRight') {
        const nextLink = document.querySelector('.nav-next');
        if (nextLink) nextLink.click();
    }
});'''
        
        js_file = self.output_dir / 'assets' / 'js' / 'reader.js'
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(reader_js)
    
    def _save_metadata(self, total_pages):
        """Зберігає метадані про згенеровані файли"""
        metadata = {
            'generated_at': datetime.now().isoformat(),
            'total_pages': total_pages,
            'pdf_file': str(self.pdf_path.name),
            'output_dir': str(self.output_dir),
            'pages': [f'page-{i+1:03d}.html' for i in range(total_pages)]
        }
        
        metadata_file = self.output_dir / 'metadata' / 'generation_info.json'
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
