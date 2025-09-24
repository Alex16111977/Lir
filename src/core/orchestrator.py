"""
Orchestrator - координатор генерації сайту з JSON
"""

from pathlib import Path
from datetime import datetime
import shutil

class Orchestrator:
    """Оркестратор - генерує сайт з JSON"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
    
    def generate(self):
        """Генерація сайту з JSON даних"""
        
        self.logger.info("Початок генерації з JSON")
        
        result = {
            'success': False,
            'files_generated': 0,
            'errors': 0
        }
        
        try:
            # Імпортуємо генератор
            from src.generators.json_generator import JSONGenerator
            json_gen = JSONGenerator(self.logger)
            
            # Очищаємо output
            if self.config.output_dir.exists():
                shutil.rmtree(self.config.output_dir)
            
            # Генерація з JSON
            self.logger.info("Генерація HTML з JSON даних...")
            if json_gen.generate_from_json(self.config.data_dir, self.config.output_dir):
                stats = json_gen.get_statistics()
                result['files_generated'] = stats['files_generated']
                result['success'] = True
                self.logger.success(f"Згенеровано {result['files_generated']} файлів")
            else:
                result['errors'] += 1
                self.logger.error("Помилка генерації з JSON")
                
        except Exception as e:
            self.logger.error(f"Помилка генерації: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            result['errors'] += 1
        
        return result
