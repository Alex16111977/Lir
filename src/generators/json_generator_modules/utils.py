"""
Generator Utils - допоміжні функції
"""

import re
from typing import Dict, List, Any


class GeneratorUtils:
    """Утиліти для генератора."""
    
    @staticmethod
    def count_words(vocabulary: List[Dict[str, Any]]) -> int:
        """Підрахунок слів у словнику."""
        return len([w for w in vocabulary if w.get('german')])
        
    @staticmethod
    def sanitize_filename(text: str) -> str:
        """Очищення назви файлу."""
        # Видалення спеціальних символів
        text = re.sub(r'[^\w\s-]', '', text)
        # Заміна пробілів на підкреслення
        text = re.sub(r'[-\s]+', '_', text)
        return text.lower()
        
    @staticmethod
    def format_level(level: str) -> str:
        """Форматування рівня."""
        levels = {
            'a1': 'A1 - Початківець',
            'a2': 'A2 - Елементарний',
            'b1': 'B1 - Середній',
            'b2': 'B2 - Вище середнього',
            'c1': 'C1 - Просунутий',
            'c2': 'C2 - Професійний'
        }
        return levels.get(level.lower(), level.upper())
        
    @staticmethod
    def get_gradient_by_index(index: int) -> str:
        """Отримати градієнт за індексом."""
        gradients = [
            'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
            'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
            'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
            'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
            'linear-gradient(135deg, #30cfd0 0%, #330867 100%)'
        ]
        return gradients[index % len(gradients)]
        
    @staticmethod
    def group_lessons_by_category(lessons: List[Dict]) -> Dict[str, List]:
        """Групування уроків за категоріями."""
        grouped = {}
        
        for lesson in lessons:
            level = lesson.get('level', 'other')
            if level not in grouped:
                grouped[level] = []
            grouped[level].append(lesson)
            
        return grouped
