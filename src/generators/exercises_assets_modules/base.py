"""
Base module for exercises assets generator
Contains base classes and shared constants
"""

from pathlib import Path
from typing import Dict, List, Any, Optional


class ExercisesAssetsBase:
    """Base class for exercises assets generation."""
    
    # Exercise types
    EXERCISE_TYPES = {
        'drag_drop': 'Drag and Drop',
        'flashcards': 'Flashcards',
        'fill_blanks': 'Fill in the Blanks',
        'matching': 'Matching',
        'quiz': 'Quiz',
        'audio': 'Audio Exercises'
    }
    
    # Color schemes
    COLORS = {
        'primary': '#667eea',
        'secondary': '#764ba2',
        'success': '#48bb78',
        'danger': '#f56565',
        'warning': '#ed8936',
        'info': '#4299e1'
    }
    
    def __init__(self):
        """Initialize base class."""
        self.assets_generated = 0
        
    def _get_base_css(self) -> str:
        """Get base CSS styles."""
        return """
/* Base Exercise Styles */
.exercises-section {
    margin: 40px 0;
    padding: 40px;
    background: #f7f9fc;
    border-radius: 24px;
    color: #1f2937;
    box-shadow: 0 20px 45px rgba(15, 23, 42, 0.08);
}

.exercises-section .section-title {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 26px;
    color: #1f2937;
    margin-bottom: 24px;
}

.exercises-section .section-title .icon {
    font-size: 32px;
    color: #8b5cf6;
}
"""
        
    def _get_base_js(self) -> str:
        """Get base JavaScript."""
        return """
// Base Exercise JavaScript
class ExerciseBase {
    constructor(container) {
        this.container = container;
        this.score = 0;
        this.total = 0;
    }
    
    updateScore() {
        const scoreDisplay = this.container.querySelector('.score');
        if (scoreDisplay) {
            scoreDisplay.textContent = `Score: ${this.score}/${this.total}`;
        }
    }
}
"""
