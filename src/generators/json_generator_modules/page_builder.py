"""
Page Builder - генерація HTML сторінок
"""

from pathlib import Path
from typing import Dict, List, Any
from .base import transliterate_filename


class PageBuilder:
    """Побудова HTML сторінок."""
    
    def generate_lesson_page(self, lesson_data: Dict[str, Any], group_info: Dict[str, str]) -> str:
        """Генерація сторінки уроку."""
        
        # Метадані уроку
        title = lesson_data.get('title', 'Урок')
        level = lesson_data.get('level', 'A2')
        vocabulary = lesson_data.get('vocabulary', [])
        
        # HTML сторінки
        html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self._escape_html(title)} | {level}</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/vocabulary.css">
    <link rel="stylesheet" href="../../css/exercises.css">
</head>
<body>
    <div class="container">
        <!-- Шапка -->
        <header class="lesson-header">
            <div class="breadcrumb">
                <a href="../../index.html">Головна</a> /
                <a href="../index.html">{level}</a> /
                <span>{self._escape_html(title)}</span>
            </div>
            <h1>{self._escape_html(title)}</h1>
            <div class="lesson-meta">
                <span class="level-badge {level.lower()}">{level}</span>
                <span class="word-count">📚 {len(vocabulary)} слів</span>
            </div>
        </header>
        
        <!-- Навігація між уроками -->
        {self._generate_lesson_navigation(lesson_data, group_info)}
        
        <!-- Словник -->
        {self.generate_vocabulary_section(vocabulary)}
        
        <!-- Вправи -->
        {self._generate_exercises_section(lesson_data)}
        
        <!-- Підвал -->
        <footer>
            <div class="footer-content">
                <p>© 2025 LIR - Навчання німецької через "Короля Ліра"</p>
            </div>
        </footer>
    </div>
    
    <!-- Скрипти -->
    <script src="../../js/vocabulary.js"></script>
    <script src="../../js/exercises.js"></script>
</body>
</html>"""
        return html
        
    def generate_index_page(self, categories: Dict[str, List]) -> str:
        """Генерація головної сторінки."""
        
        html = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LIR - Німецька через Короля Ліра</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/index.css">
</head>
<body>
    <div class="hero-section">
        <h1 class="hero-title">
            <span class="highlight">LIR</span> - Learn It Right
        </h1>
        <p class="hero-subtitle">Вивчайте німецьку через "Короля Ліра"</p>
        <div class="stats">
            <div class="stat-item">
                <span class="stat-number">51</span>
                <span class="stat-label">урок</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">612+</span>
                <span class="stat-label">слів</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">3</span>
                <span class="stat-label">рівні</span>
            </div>
        </div>
    </div>
    
    <div class="container">
        <!-- Категорії уроків -->
        <section class="categories-section">
            <h2>Виберіть рівень</h2>
            <div class="categories-grid">
                {self._generate_category_cards(categories)}
            </div>
        </section>
        
        <!-- Додаткові ресурси -->
        <section class="resources-section">
            <h2>Додаткові матеріали</h2>
            <div class="resources-grid">
                <a href="book/index.html" class="resource-card">
                    <span class="resource-icon">📖</span>
                    <h3>Веб-читалка</h3>
                    <p>Читайте "Короля Ліра" німецькою</p>
                </a>
                <a href="exercises/index.html" class="resource-card">
                    <span class="resource-icon">✏️</span>
                    <h3>Вправи</h3>
                    <p>Інтерактивні завдання для практики</p>
                </a>
            </div>
        </section>
    </div>
    
    <footer>
        <div class="footer-content">
            <p>© 2025 LIR - Learn It Right</p>
        </div>
    </footer>
</body>
</html>"""
        return html
        
    def _generate_lesson_navigation(self, lesson_data: Dict, group_info: Dict) -> str:
        """Генерація навігації між уроками."""
        return f"""
        <nav class="lesson-nav">
            <a href="#" class="nav-btn prev">← Попередній урок</a>
            <a href="../index.html" class="nav-btn center">До списку уроків</a>
            <a href="#" class="nav-btn next">Наступний урок →</a>
        </nav>
        """
        
    def _generate_exercises_section(self, lesson_data: Dict) -> str:
        """Генерація секції вправ."""
        if not hasattr(self, 'exercises_generator'):
            return ""
            
        return f"""
        <section class="exercises-section">
            <h2 class="section-title">
                <span class="icon">✏️</span> Вправи
            </h2>
            <div class="exercises-container">
                {self.exercises_generator.generate_exercises_html(lesson_data)}
            </div>
        </section>
        """
        
    def _generate_category_cards(self, categories: Dict) -> str:
        """Генерація карток категорій."""
        cards = []
        
        for category, lessons in categories.items():
            card = f"""
            <div class="category-card {category.lower()}">
                <h3>{category.upper()}</h3>
                <p>{len(lessons)} уроків</p>
                <a href="{category.lower()}/index.html" class="btn">Переглянути</a>
            </div>
            """
            cards.append(card)
            
        return ''.join(cards)
