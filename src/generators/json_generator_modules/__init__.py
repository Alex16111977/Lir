"""
JSON Generator - модульна структура
Розбито на окремі модулі для кращої підтримки
"""

from .base import JsonGeneratorBase
from .vocabulary_cards import VocabularyCardsGenerator
from .page_builder import PageBuilder
from .navigation import NavigationGenerator
from .templates import HTMLTemplates
from .utils import GeneratorUtils

# Головний клас для зворотної сумісності
class JsonGenerator(
    JsonGeneratorBase,
    VocabularyCardsGenerator,
    PageBuilder,
    NavigationGenerator
):
    """Головний генератор JSON → HTML."""
    
    def __init__(self, config, logger):
        super().__init__(config, logger)
        self.templates = HTMLTemplates()
        self.utils = GeneratorUtils()
        
        # Ініціалізація генераторів вправ
        from src.generators.exercises_generator import ExercisesGenerator
        from src.generators.exercises_assets import ExercisesAssetsGenerator
        
        self.exercises_generator = ExercisesGenerator(config, logger)
        self.exercises_assets = ExercisesAssetsGenerator(config, logger)
        self.exercises_assets.generate_all_assets()

__all__ = [
    'JsonGenerator',
    'JsonGeneratorBase',
    'VocabularyCardsGenerator',
    'PageBuilder',
    'NavigationGenerator',
    'HTMLTemplates',
    'GeneratorUtils'
]
