"""
Site Analyzer - аналіз структури сайту
"""

from pathlib import Path
from bs4 import BeautifulSoup
import re

class SiteAnalyzer:
    """Аналізатор сайту"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
    
    def analyze(self):
        """Провести аналіз сайту"""
        
        stats = {
            'html_files': 0,
            'inline_styles': 0,
            'external_css': 0,
            'js_files': 0,
            'categories': {},
            'total_size': 0,
            'issues': []
        }
        
        # Аналіз HTML файлів
        html_files = self.config.get_html_files()
        stats['html_files'] = len(html_files)
        
        for html_file in html_files:
            self._analyze_html_file(html_file, stats)
        
        # Аналіз категорій
        for category in self.config.categories:
            cat_files = self.config.get_html_files(category)
            stats['categories'][category] = len(cat_files)
        
        # CSS файли
        css_dir = self.config.website_dir / "css"
        if css_dir.exists():
            stats['external_css'] = len(list(css_dir.glob("*.css")))
        
        # JS файли
        js_dir = self.config.website_dir / "js"
        if js_dir.exists():
            stats['js_files'] = len(list(js_dir.glob("*.js")))
        
        # Розмір сайту
        for file in self.config.website_dir.rglob("*"):
            if file.is_file():
                stats['total_size'] += file.stat().st_size
        
        # Конвертувати розмір в MB
        stats['total_size_mb'] = round(stats['total_size'] / (1024 * 1024), 2)
        
        self.logger.info(f"Аналіз завершено: {stats['html_files']} файлів, {stats['inline_styles']} inline стилів")
        
        return stats
    
    def _analyze_html_file(self, file_path, stats):
        """Аналіз одного HTML файлу"""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Підрахунок inline стилів
            inline_count = len(soup.find_all(style=True))
            stats['inline_styles'] += inline_count
            
            # Перевірка проблем
            if inline_count > 50:
                stats['issues'].append(f"{file_path.name}: багато inline стилів ({inline_count})")
            
            # Перевірка на modern.css
            has_modern = soup.find('link', {'href': re.compile(r'modern\.css')})
            if has_modern:
                stats['issues'].append(f"{file_path.name}: вже має modern.css")
            
            # Перевірка дублікатів style тегів
            style_tags = soup.find_all('style')
            if len(style_tags) > 1:
                stats['issues'].append(f"{file_path.name}: дубльовані style теги ({len(style_tags)})")
            
        except Exception as e:
            self.logger.error(f"Помилка аналізу {file_path}: {e}")
            stats['issues'].append(f"{file_path.name}: помилка читання")
