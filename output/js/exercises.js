// LIR Exercise System JavaScript
// Generated from modular structure


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


// Drag and Drop Exercise Handler
class DragDropExercise {
    constructor(container) {
        this.container = container;
        this.score = 0;
        this.total = 0;
        this.init();
    }
    
    init() {
        this.setupDragElements();
        this.setupDropZones();
        this.attachEventListeners();
    }
    
    setupDragElements() {
        const draggables = this.container.querySelectorAll('.draggable');
        draggables.forEach(elem => {
            elem.draggable = true;
            elem.addEventListener('dragstart', this.handleDragStart.bind(this));
            elem.addEventListener('dragend', this.handleDragEnd.bind(this));
        });
        this.total = draggables.length;
    }
    
    setupDropZones() {
        const dropZones = this.container.querySelectorAll('.drop-zone');
        dropZones.forEach(zone => {
            zone.addEventListener('dragover', this.handleDragOver.bind(this));
            zone.addEventListener('drop', this.handleDrop.bind(this));
            zone.addEventListener('dragleave', this.handleDragLeave.bind(this));
        });
    }
    
    handleDragStart(e) {
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/html', e.target.innerHTML);
        e.dataTransfer.setData('answer', e.target.dataset.answer);
        e.target.classList.add('dragging');
    }
    
    handleDragEnd(e) {
        e.target.classList.remove('dragging');
    }
    
    handleDragOver(e) {
        if (e.preventDefault) e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
        e.target.classList.add('drag-over');
        return false;
    }
    
    handleDragLeave(e) {
        e.target.classList.remove('drag-over');
    }
    
    handleDrop(e) {
        if (e.stopPropagation) e.stopPropagation();
        e.target.classList.remove('drag-over');
        
        const answer = e.dataTransfer.getData('answer');
        const expected = e.target.dataset.expected;
        
        if (answer === expected) {
            e.target.classList.add('correct');
            e.target.innerHTML = e.dataTransfer.getData('text/html');
            this.score++;
            this.updateScore();
        } else {
            e.target.classList.add('incorrect');
            setTimeout(() => {
                e.target.classList.remove('incorrect');
            }, 1000);
        }
        
        return false;
    }
    
    updateScore() {
        const scoreDisplay = this.container.querySelector('.score');
        if (scoreDisplay) {
            scoreDisplay.textContent = `Score: ${this.score}/${this.total}`;
        }
        
        if (this.score === this.total) {
            this.showSuccess();
        }
    }
    
    showSuccess() {
        const message = document.createElement('div');
        message.className = 'success-message';
        message.innerHTML = 'Excellent! All correct!';
        this.container.appendChild(message);
    }
    
    attachEventListeners() {
        const resetBtn = this.container.querySelector('.reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => this.reset());
        }
    }
    
    reset() {
        this.score = 0;
        const dropZones = this.container.querySelectorAll('.drop-zone');
        dropZones.forEach(zone => {
            zone.innerHTML = '';
            zone.classList.remove('correct', 'incorrect');
        });
        
        const successMsg = this.container.querySelector('.success-message');
        if (successMsg) successMsg.remove();
        
        this.updateScore();
    }
}

// Initialize all drag-drop exercises on page
document.addEventListener('DOMContentLoaded', () => {
    const exercises = document.querySelectorAll('.drag-drop-exercise');
    exercises.forEach(ex => new DragDropExercise(ex));
});


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
