#!/usr/bin/env python
"""
Lir Website Generator
Генерація сайту з JSON даних
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.core.orchestrator import Orchestrator
from src.core.config_manager import ConfigManager
from src.core.logger_manager import LoggerManager
# Спроба імпортувати генератор книги
try:
    from src.generators.book_generator import BookGenerator
except ImportError:
    # Використовуємо спрощену версію
    from src.generators.book_generator_full import BookGeneratorFull as BookGenerator

def main():
    """Генерація сайту з JSON"""
    
    config = ConfigManager()
    logger = LoggerManager()
    
    print("=" * 60)
    print("  LIR WEBSITE GENERATOR")
    print("  Генерація сайту з JSON даних")
    print("=" * 60)
    
    # Перевірка JSON
    data_dir = config.base_dir / "data"
    json_count = sum(1 for _ in data_dir.glob("*/*.json"))
    
    if json_count == 0:
        print("[ERROR] Немає JSON файлів в data/")
        return 1
    
    print(f"[OK] Знайдено {json_count} JSON файлів")
    
    # Генерація основного сайту
    orchestrator = Orchestrator(config, logger)
    result = orchestrator.generate()
    
    if result['success']:
        print(f"[OK] Згенеровано {result['files_generated']} файлів")
        print(f"Сайт: {config.output_dir / 'index.html'}")
        
        # Генерація книги
        if hasattr(config, 'BOOK_CONFIG') and config.BOOK_CONFIG.get('enabled', False):
            print("\n[!] Генерація веб-читалки...")
            book_generator = BookGenerator(config, logger)
            book_result = book_generator.generate()
            if book_result:
                print("[OK] Веб-читалка згенерована")
                print(f"Книга: {config.output_dir / 'book' / 'index.html'}")
            else:
                print("[ERROR] Помилка генерації книги")
        
        return 0
    else:
        print("[ERROR] Помилка генерації")
        return 1

if __name__ == "__main__":
    sys.exit(main())
