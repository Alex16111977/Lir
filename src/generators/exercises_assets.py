"""
Exercises Assets Generator - Wrapper for backward compatibility
Використовує модульну структуру з exercises_assets_modules
"""

from .exercises_assets_modules import ExercisesAssetsGenerator as ModularGenerator


# Клас для зворотної сумісності
class ExercisesAssetsGenerator(ModularGenerator):
    """Wrapper class for backward compatibility."""
    
    def __init__(self):
        super().__init__()
        
    # Додаткові методи для сумісності зі старим API якщо потрібно
    def generate_assets(self):
        """Old method name for compatibility."""
        return {
            'css': self.generate_css(),
            'js': self.generate_js()
        }


# Re-export для сумісності
__all__ = ['ExercisesAssetsGenerator']
