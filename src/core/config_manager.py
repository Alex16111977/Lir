"""
Config Manager - управління конфігурацією
"""

from pathlib import Path
import config

class ConfigManager:
    """Менеджер конфігурації"""
    
    def __init__(self):
        self.base_dir = config.BASE_DIR
        self.data_dir = config.DATA_DIR
        self.output_dir = config.OUTPUT_DIR
        self.backup_dir = config.BACKUP_DIR
        self.logs_dir = config.LOGS_DIR
        
        self.categories = config.CATEGORIES
        self.a2_groups = config.A2_GROUPS
        self.b1_groups = config.B1_GROUPS
        self.thematic_groups = config.THEMATIC_GROUPS
        
        self.generation = config.GENERATION
        
        # Налаштування книги
        self.BOOK_CONFIG = config.BOOK_CONFIG if hasattr(config, 'BOOK_CONFIG') else None
        
        self._validate_paths()
    
    def _validate_paths(self):
        """Перевірка існування необхідних папок"""
        
        # Створення папок якщо не існують
        for dir_path in [self.output_dir, self.backup_dir, self.logs_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def get_json_files(self, category=None):
        """Отримати список JSON файлів"""
        
        json_files = []
        
        if category:
            # Конкретна категорія
            cat_dir = self.data_dir / category
            if cat_dir.exists():
                json_files = list(cat_dir.glob("*.json"))
        else:
            # Всі файли
            for cat in self.categories:
                cat_dir = self.data_dir / cat
                if cat_dir.exists():
                    json_files.extend(cat_dir.glob("*.json"))
        
        return json_files
    
    def get_css_output_path(self):
        """Шлях для modern.css"""
        css_path = self.output_dir / self.generation['css_output']
        css_path.parent.mkdir(parents=True, exist_ok=True)
        return css_path
