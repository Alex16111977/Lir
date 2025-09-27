"""
Matching exercises module
"""


class MatchingGenerator:
    """Generator for matching exercises."""
    
    def generate_matching_css(self) -> str:
        """Generate CSS for matching."""
        return """
/* Matching Exercise Styles */
.matching-exercise {
    padding: 20px;
    background: white;
    border-radius: 12px;
}

.matching-columns {
    display: flex;
    gap: 40px;
    justify-content: center;
    margin: 20px 0;
}

.matching-column {
    flex: 1;
    max-width: 300px;
}

.matching-item {
    padding: 12px;
    margin: 10px 0;
    background: linear-gradient(135deg, #a8edea, #fed6e3);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
}

.matching-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.matching-item.selected {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

.matching-item.matched {
    background: #48bb78;
    color: white;
    cursor: default;
}

.matching-line {
    position: absolute;
    background: #667eea;
    height: 2px;
    transform-origin: left center;
    pointer-events: none;
    z-index: 10;
}

.matching-score {
    text-align: center;
    font-size: 18px;
    margin: 20px 0;
}
"""

    def generate_matching_js(self) -> str:
        """Generate JavaScript for matching."""
        return """
// Matching Exercise Handler
class MatchingExercise {
    constructor(container) {
        this.container = container;
        this.selectedItem = null;
        this.matches = new Map();
        this.score = 0;
        this.total = 0;
        this.init();
    }
    
    init() {
        this.setupItems();
        this.calculateTotal();
    }
    
    setupItems() {
        const leftItems = this.container.querySelectorAll('.matching-column:first-child .matching-item');
        const rightItems = this.container.querySelectorAll('.matching-column:last-child .matching-item');
        
        leftItems.forEach(item => {
            item.addEventListener('click', () => this.selectItem(item, 'left'));
        });
        
        rightItems.forEach(item => {
            item.addEventListener('click', () => this.selectItem(item, 'right'));
        });
    }
    
    calculateTotal() {
        const leftItems = this.container.querySelectorAll('.matching-column:first-child .matching-item');
        this.total = leftItems.length;
    }
    
    selectItem(item, side) {
        if (item.classList.contains('matched')) {
            return;
        }
        
        if (!this.selectedItem) {
            // First selection
            this.selectedItem = { element: item, side: side };
            item.classList.add('selected');
        } else {
            // Second selection
            if (this.selectedItem.side === side) {
                // Same side - deselect and select new
                this.selectedItem.element.classList.remove('selected');
                this.selectedItem = { element: item, side: side };
                item.classList.add('selected');
            } else {
                // Different sides - check match
                this.checkMatch(this.selectedItem.element, item);
                this.selectedItem.element.classList.remove('selected');
                this.selectedItem = null;
            }
        }
    }
    
    checkMatch(item1, item2) {
        const match1 = item1.dataset.match;
        const match2 = item2.dataset.match;
        
        if (match1 === match2) {
            item1.classList.add('matched');
            item2.classList.add('matched');
            this.matches.set(match1, true);
            this.score++;
            this.drawLine(item1, item2);
            this.updateScore();
        } else {
            // Wrong match animation
            item1.classList.add('incorrect');
            item2.classList.add('incorrect');
            setTimeout(() => {
                item1.classList.remove('incorrect');
                item2.classList.remove('incorrect');
            }, 1000);
        }
    }
    
    drawLine(item1, item2) {
        // Simple visual feedback - could be enhanced with actual line drawing
        const line = document.createElement('div');
        line.className = 'matching-line';
        // Line drawing logic would go here
    }
    
    updateScore() {
        const scoreElement = this.container.querySelector('.matching-score');
        if (scoreElement) {
            scoreElement.textContent = `Score: ${this.score}/${this.total}`;
        }
        
        if (this.score === this.total) {
            this.showSuccess();
        }
    }
    
    showSuccess() {
        const message = document.createElement('div');
        message.className = 'success-message';
        message.textContent = 'Perfect! All pairs matched!';
        this.container.appendChild(message);
    }
}

// Initialize matching exercises
document.addEventListener('DOMContentLoaded', () => {
    const exercises = document.querySelectorAll('.matching-exercise');
    exercises.forEach(ex => new MatchingExercise(ex));
});
"""