"""
Базовий клас для JSON генератора
Містить основну функціональність та константи
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from html import escape


def transliterate_filename(text):
    """Транслітерує кириличну назву для безпечного URL"""
    translit_table = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
        # Великі літери
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    
    result = []
    for char in text:
        if char in translit_table:
            result.append(translit_table[char])
        elif char.isalnum() or char in '._-':
            result.append(char)
        elif char == ' ':
            result.append('_')
        else:
            result.append('_')
    
    filename = ''.join(result)
    filename = re.sub(r'_+', '_', filename)
    filename = filename.strip('_')
    
    return filename


class JsonGeneratorBase:
    """Базова функціональність генератора."""
    
    # Кольорова система артиклів
    ARTICLE_COLORS = {
        'der': {
            'class': 'article-der',
            'color': '#2B6CB0',
            'gender': 'masculine',
            'label': '🔷 der = чоловічий'
        },
        'die': {
            'class': 'article-die',
            'color': '#C53030',
            'gender': 'feminine', 
            'label': '🔴 die = жіночий'
        },
        'das': {
            'class': 'article-das',
            'color': '#ECC94B',
            'gender': 'neutral',
            'label': '🟡 das = середній'
        }
    }
    
    # Градієнти для карток
    CARD_GRADIENTS = [
        'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)', 
        'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
        'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
        'linear-gradient(135deg, #30cfd0 0%, #330867 100%)'
    ]
    
    def __init__(self, config, logger):
        """Ініціалізація базового класу."""
        self.config = config
        self.logger = logger
        self.files_generated = 0
        self.total_words = 0
        
        # Директорії
        self.output_dir = Path(config.output_dir)
        self.data_dir = Path(config.data_dir)
        
        # Створюємо вихідну директорію
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def _log(self, message: str, level: str = 'info') -> None:
        """Логування повідомлень."""
        if self.logger:
            getattr(self.logger, level)(f"[JsonGenerator] {message}")
            
    def _save_file(self, path: Path, content: str) -> bool:
        """Збереження файлу."""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
            self.files_generated += 1
            self._log(f"Saved: {path.name}")
            return True
        except Exception as e:
            self._log(f"Error saving {path}: {e}", 'error')
            return False
            
    def _load_json(self, path: Path) -> Optional[Dict[str, Any]]:
        """Завантаження JSON файлу."""
        try:
            content = path.read_text(encoding='utf-8')
            return json.loads(content)
        except Exception as e:
            self._log(f"Error loading {path}: {e}", 'error')
            return None
            
    def _get_article_info(self, german_word: str) -> Dict[str, str]:
        """Отримати інформацію про артикль слова."""
        word_lower = german_word.lower().strip()
        
        for article, info in self.ARTICLE_COLORS.items():
            if word_lower.startswith(f"{article} "):
                return {
                    'article': article,
                    'word': german_word[len(article)+1:].strip(),
                    'class': info['class'],
                    'color': info['color'],
                    'gender': info['gender']
                }
                
        return {
            'article': '',
            'word': german_word,
            'class': '',
            'color': '',
            'gender': ''
        }
        
    def _escape_html(self, text: str) -> str:
        """Безпечне екранування HTML."""
        return escape(str(text))
        
    def generate(self) -> int:
        """Основний метод генерації (буде перевизначений в підкласах)."""
        raise NotImplementedError("Цей метод має бути реалізований в підкласі")
