"""
Navigation Generator - генерація навігації
"""

from typing import Dict, List


class NavigationGenerator:
    """Генерація навігаційних елементів."""
    
    def generate_breadcrumb(self, path_items: List[Dict[str, str]]) -> str:
        """Генерація хлібних крихт."""
        items = []
        for item in path_items:
            if item.get('url'):
                items.append(f'<a href="{item["url"]}">{item["title"]}</a>')
            else:
                items.append(f'<span>{item["title"]}</span>')
                
        return f"""
        <nav class="breadcrumb">
            {' / '.join(items)}
        </nav>
        """
        
    def generate_sidebar(self, lessons: List[Dict], current_lesson: str = None) -> str:
        """Генерація бічної панелі з уроками."""
        items = []
        
        for lesson in lessons:
            title = lesson.get('title', '')
            url = lesson.get('url', '#')
            is_current = 'current' if title == current_lesson else ''
            
            items.append(f"""
                <li class="sidebar-item {is_current}">
                    <a href="{url}">{self._escape_html(title)}</a>
                </li>
            """)
            
        return f"""
        <aside class="sidebar">
            <h3>Уроки</h3>
            <ul class="sidebar-list">
                {''.join(items)}
            </ul>
        </aside>
        """
        
    def generate_pagination(self, current: int, total: int, base_url: str) -> str:
        """Генерація пагінації."""
        if total <= 1:
            return ""
            
        pages = []
        
        for i in range(1, total + 1):
            if i == current:
                pages.append(f'<span class="page current">{i}</span>')
            else:
                pages.append(f'<a href="{base_url}?page={i}" class="page">{i}</a>')
                
        prev_link = ""
        next_link = ""
        
        if current > 1:
            prev_link = f'<a href="{base_url}?page={current-1}" class="prev">←</a>'
        if current < total:
            next_link = f'<a href="{base_url}?page={current+1}" class="next">→</a>'
            
        return f"""
        <div class="pagination">
            {prev_link}
            {' '.join(pages)}
            {next_link}
        </div>
        """
