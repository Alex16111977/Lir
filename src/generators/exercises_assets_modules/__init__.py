"""
Exercises Assets Generator - Modular Structure
Розбито на модулі для кращої підтримки
"""

from .base import ExercisesAssetsBase
from .drag_drop import DragDropGenerator
from .flashcards import FlashcardsGenerator
from .fill_blanks import FillBlanksGenerator
from .matching import MatchingGenerator
from .quiz import QuizGenerator


class ExercisesAssetsGenerator(
    ExercisesAssetsBase,
    DragDropGenerator,
    FlashcardsGenerator,
    FillBlanksGenerator,
    MatchingGenerator,
    QuizGenerator
):
    """Main exercises assets generator combining all modules."""
    
    def __init__(self):
        super().__init__()
        
    def generate_css(self) -> str:
        """Generate combined CSS for all exercises."""
        css_parts = [
            "/* LIR Exercise System CSS */",
            "/* Generated modular structure */",
            "",
            self._get_base_css(),
            self.generate_drag_drop_css(),
            self.generate_flashcards_css(),
            self.generate_fill_blanks_css(),
            self.generate_matching_css(),
            self.generate_quiz_css()
        ]
        return '\n'.join(css_parts)
        
    def generate_js(self) -> str:
        """Generate combined JavaScript for all exercises."""
        js_parts = [
            "// LIR Exercise System JavaScript",
            "// Generated from modular structure",
            "",
            self._get_base_js(),
            self.generate_drag_drop_js(),
            self.generate_flashcards_js(),
            self.generate_fill_blanks_js(),
            self.generate_matching_js(),
            self.generate_quiz_js()
        ]
        return '\n'.join(js_parts)


# For backward compatibility
__all__ = ['ExercisesAssetsGenerator']
