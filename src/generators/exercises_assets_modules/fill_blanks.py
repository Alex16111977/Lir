"""
Fill in the blanks exercises module
"""


class FillBlanksGenerator:
    """Generator for fill in the blanks exercises."""
    
    def generate_fill_blanks_css(self) -> str:
        """Generate CSS for fill in the blanks."""
        return """
/* Fill in the Blanks Styles */
.fill-blanks-exercise {
    padding: 20px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.fill-blanks-sentence {
    font-size: 18px;
    line-height: 2;
    margin: 20px 0;
}

.blank-input {
    display: inline-block;
    min-width: 100px;
    padding: 5px 10px;
    margin: 0 5px;
    border: none;
    border-bottom: 2px solid #667eea;
    background: transparent;
    font-size: 18px;
    text-align: center;
    transition: all 0.3s;
}

.blank-input:focus {
    outline: none;
    border-bottom-color: #764ba2;
    background: rgba(102, 126, 234, 0.05);
}

.blank-input.correct {
    border-bottom-color: #48bb78;
    background: rgba(72, 187, 120, 0.1);
}

.blank-input.incorrect {
    border-bottom-color: #f56565;
    background: rgba(245, 101, 101, 0.1);
    animation: shake 0.3s;
}

.check-button {
    display: inline-block;
    padding: 10px 20px;
    margin: 10px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    transition: transform 0.2s;
}

.check-button:hover {
    transform: scale(1.05);
}

.fill-blanks-result {
    margin: 20px 0;
    padding: 15px;
    border-radius: 8px;
    font-size: 16px;
    text-align: center;
}

.fill-blanks-result.success {
    background: #48bb78;
    color: white;
}

.fill-blanks-result.partial {
    background: #ed8936;
    color: white;
}
"""

    def generate_fill_blanks_js(self) -> str:
        """Generate JavaScript for fill in the blanks."""
        return """
// Fill in the Blanks Exercise Handler
class FillBlanksExercise {
    constructor(container) {
        this.container = container;
        this.blanks = [];
        this.answers = {};
        this.init();
    }
    
    init() {
        this.setupBlanks();
        this.attachEventListeners();
    }
    
    setupBlanks() {
        const inputs = this.container.querySelectorAll('.blank-input');
        inputs.forEach((input, index) => {
            this.blanks.push(input);
            this.answers[index] = input.dataset.answer;
            
            input.addEventListener('input', () => {
                input.classList.remove('correct', 'incorrect');
            });
        });
    }
    
    attachEventListeners() {
        const checkBtn = this.container.querySelector('.check-button');
        if (checkBtn) {
            checkBtn.addEventListener('click', () => this.checkAnswers());
        }
        
        const resetBtn = this.container.querySelector('.reset-button');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => this.reset());
        }
    }
    
    checkAnswers() {
        let correct = 0;
        let total = this.blanks.length;
        
        this.blanks.forEach((input, index) => {
            const userAnswer = input.value.trim().toLowerCase();
            const correctAnswer = this.answers[index].toLowerCase();
            
            if (userAnswer === correctAnswer) {
                input.classList.add('correct');
                input.classList.remove('incorrect');
                correct++;
            } else {
                input.classList.add('incorrect');
                input.classList.remove('correct');
            }
        });
        
        this.showResult(correct, total);
    }
    
    showResult(correct, total) {
        const existingResult = this.container.querySelector('.fill-blanks-result');
        if (existingResult) {
            existingResult.remove();
        }
        
        const result = document.createElement('div');
        result.className = 'fill-blanks-result';
        
        if (correct === total) {
            result.className += ' success';
            result.textContent = 'Perfect! All answers are correct!';
        } else {
            result.className += ' partial';
            result.textContent = `You got ${correct} out of ${total} correct. Try again!`;
        }
        
        this.container.appendChild(result);
    }
    
    reset() {
        this.blanks.forEach(input => {
            input.value = '';
            input.classList.remove('correct', 'incorrect');
        });
        
        const result = this.container.querySelector('.fill-blanks-result');
        if (result) {
            result.remove();
        }
    }
}

// Initialize fill blanks exercises
document.addEventListener('DOMContentLoaded', () => {
    const exercises = document.querySelectorAll('.fill-blanks-exercise');
    exercises.forEach(ex => new FillBlanksExercise(ex));
});
"""