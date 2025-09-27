"""
Quiz exercises module
"""


class QuizGenerator:
    """Generator for quiz exercises."""
    
    def generate_quiz_css(self) -> str:
        """Generate CSS for quiz."""
        return """
/* Quiz Exercise Styles */
.quiz-exercise {
    padding: 30px;
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.quiz-question {
    margin-bottom: 30px;
}

.quiz-question-text {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 20px;
    color: #1f2937;
}

.quiz-options {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.quiz-option {
    padding: 15px 20px;
    background: #f7f9fc;
    border: 2px solid transparent;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
    padding-left: 50px;
}

.quiz-option:hover {
    background: #e5e7eb;
    border-color: #667eea;
}

.quiz-option::before {
    content: '';
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    border: 2px solid #667eea;
    border-radius: 50%;
    background: white;
}

.quiz-option.selected::before {
    background: #667eea;
    box-shadow: inset 0 0 0 4px white;
}

.quiz-option.correct {
    background: #48bb78;
    border-color: #2f855a;
    color: white;
}

.quiz-option.incorrect {
    background: #f56565;
    border-color: #c53030;
    color: white;
}

.quiz-submit {
    padding: 12px 30px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
}

.quiz-submit:hover {
    transform: scale(1.05);
}

.quiz-result {
    margin-top: 20px;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
}

.quiz-result.perfect {
    background: #48bb78;
    color: white;
}

.quiz-result.good {
    background: #4299e1;
    color: white;
}

.quiz-result.needs-improvement {
    background: #ed8936;
    color: white;
}
"""

    def generate_quiz_js(self) -> str:
        """Generate JavaScript for quiz."""
        return """
// Quiz Exercise Handler
class QuizExercise {
    constructor(container) {
        this.container = container;
        this.questions = [];
        this.answers = {};
        this.score = 0;
        this.init();
    }
    
    init() {
        this.setupQuestions();
        this.attachEventListeners();
    }
    
    setupQuestions() {
        const questionElements = this.container.querySelectorAll('.quiz-question');
        questionElements.forEach((question, index) => {
            const options = question.querySelectorAll('.quiz-option');
            this.questions.push({
                element: question,
                options: options,
                correctAnswer: question.dataset.correct
            });
            
            options.forEach(option => {
                option.addEventListener('click', () => this.selectOption(index, option));
            });
        });
    }
    
    selectOption(questionIndex, option) {
        // Clear previous selection for this question
        this.questions[questionIndex].options.forEach(opt => {
            opt.classList.remove('selected');
        });
        
        // Select new option
        option.classList.add('selected');
        this.answers[questionIndex] = option.dataset.value;
    }
    
    attachEventListeners() {
        const submitBtn = this.container.querySelector('.quiz-submit');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => this.submitQuiz());
        }
        
        const resetBtn = this.container.querySelector('.quiz-reset');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => this.resetQuiz());
        }
    }
    
    submitQuiz() {
        this.score = 0;
        
        this.questions.forEach((question, index) => {
            const userAnswer = this.answers[index];
            const correctAnswer = question.correctAnswer;
            
            question.options.forEach(option => {
                if (option.dataset.value === correctAnswer) {
                    option.classList.add('correct');
                } else if (option.classList.contains('selected') && option.dataset.value !== correctAnswer) {
                    option.classList.add('incorrect');
                }
            });
            
            if (userAnswer === correctAnswer) {
                this.score++;
            }
        });
        
        this.showResult();
    }
    
    showResult() {
        const existingResult = this.container.querySelector('.quiz-result');
        if (existingResult) {
            existingResult.remove();
        }
        
        const result = document.createElement('div');
        result.className = 'quiz-result';
        
        const percentage = (this.score / this.questions.length) * 100;
        
        if (percentage === 100) {
            result.className += ' perfect';
            result.textContent = 'Perfect score! Excellent work!';
        } else if (percentage >= 70) {
            result.className += ' good';
            result.textContent = `Good job! You got ${this.score} out of ${this.questions.length} correct!`;
        } else {
            result.className += ' needs-improvement';
            result.textContent = `You got ${this.score} out of ${this.questions.length}. Keep practicing!`;
        }
        
        this.container.appendChild(result);
    }
    
    resetQuiz() {
        this.answers = {};
        this.score = 0;
        
        this.questions.forEach(question => {
            question.options.forEach(option => {
                option.classList.remove('selected', 'correct', 'incorrect');
            });
        });
        
        const result = this.container.querySelector('.quiz-result');
        if (result) {
            result.remove();
        }
    }
}

// Initialize quiz exercises
document.addEventListener('DOMContentLoaded', () => {
    const quizzes = document.querySelectorAll('.quiz-exercise');
    quizzes.forEach(quiz => new QuizExercise(quiz));
});
"""