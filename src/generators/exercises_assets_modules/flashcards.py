"""
Flashcards exercises module
"""


class FlashcardsGenerator:
    """Generator for flashcards exercises."""
    
    def generate_flashcards_css(self) -> str:
        """Generate CSS for flashcards."""
        return """
/* Flashcards Styles */
.flashcards-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
}

.flashcard {
    width: 300px;
    height: 200px;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s;
    cursor: pointer;
}

.flashcard.flipped {
    transform: rotateY(180deg);
}

.flashcard-face {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.flashcard-front {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

.flashcard-back {
    background: linear-gradient(135deg, #f093fb, #f5576c);
    color: white;
    transform: rotateY(180deg);
}

.flashcard-content {
    text-align: center;
    font-size: 20px;
    font-weight: 600;
}
"""

    def generate_flashcards_js(self) -> str:
        """Generate JavaScript for flashcards."""
        return """
// Flashcards Exercise Handler
class FlashcardsExercise {
    constructor(container) {
        this.container = container;
        this.currentCard = 0;
        this.cards = [];
        this.init();
    }
    
    init() {
        this.setupCards();
        this.attachEventListeners();
    }
    
    setupCards() {
        const cardElements = this.container.querySelectorAll('.flashcard');
        cardElements.forEach(card => {
            card.addEventListener('click', () => this.flipCard(card));
            this.cards.push(card);
        });
    }
    
    flipCard(card) {
        card.classList.toggle('flipped');
    }
    
    attachEventListeners() {
        const nextBtn = this.container.querySelector('.next-card');
        const prevBtn = this.container.querySelector('.prev-card');
        
        if (nextBtn) {
            nextBtn.addEventListener('click', () => this.nextCard());
        }
        
        if (prevBtn) {
            prevBtn.addEventListener('click', () => this.prevCard());
        }
    }
    
    nextCard() {
        if (this.currentCard < this.cards.length - 1) {
            this.cards[this.currentCard].style.display = 'none';
            this.currentCard++;
            this.cards[this.currentCard].style.display = 'block';
        }
    }
    
    prevCard() {
        if (this.currentCard > 0) {
            this.cards[this.currentCard].style.display = 'none';
            this.currentCard--;
            this.cards[this.currentCard].style.display = 'block';
        }
    }
}

// Initialize flashcards
document.addEventListener('DOMContentLoaded', () => {
    const containers = document.querySelectorAll('.flashcards-container');
    containers.forEach(container => new FlashcardsExercise(container));
});
"""