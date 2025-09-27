"""
Drag and Drop exercises module
"""

from typing import Dict, Any


class DragDropGenerator:
    """Generator for drag and drop exercises."""
    
    def generate_drag_drop_css(self) -> str:
        """Generate CSS for drag and drop."""
        return """
/* Drag and Drop Styles */
.drag-drop-exercise {
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    margin: 20px 0;
}

.draggable {
    display: inline-block;
    padding: 10px 15px;
    margin: 5px;
    background: white;
    border: 2px solid #667eea;
    border-radius: 8px;
    cursor: move;
    transition: all 0.3s;
    user-select: none;
}

.draggable:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.draggable.dragging {
    opacity: 0.5;
    transform: scale(0.95);
}

.drop-zone {
    min-height: 50px;
    min-width: 120px;
    padding: 10px;
    margin: 10px;
    border: 3px dashed #ccc;
    border-radius: 8px;
    background: rgba(255,255,255,0.9);
    transition: all 0.3s;
    display: inline-block;
}

.drop-zone.drag-over {
    background: #e0ffe0;
    border-color: #48bb78;
    transform: scale(1.05);
}

.drop-zone.correct {
    background: #48bb78;
    border-color: #2f855a;
    color: white;
    animation: pulse 0.5s;
}

.drop-zone.incorrect {
    background: #f56565;
    border-color: #c53030;
    animation: shake 0.5s;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

.success-message {
    text-align: center;
    font-size: 24px;
    color: #48bb78;
    margin: 20px;
    animation: fadeIn 0.5s;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
"""

    def generate_drag_drop_js(self) -> str:
        """Generate JavaScript for drag and drop."""
        return """
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
"""