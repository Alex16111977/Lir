"""Assets generator for interactive exercises."""

from __future__ import annotations


class ExercisesAssetsGenerator:
    """Provide CSS and JavaScript bundles for interactive exercises."""

    def generate_css(self) -> str:
        """Return CSS styles for exercises accordion and blocks."""

        return """
/* ===== СТИЛИ ДЛЯ ИНТЕРАКТИВНЫХ УПРАЖНЕНИЙ ===== */

.exercises-section {
    margin: 40px 0;
    padding: 30px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    color: #1f2937;
}

.exercises-section .section-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 24px;
    color: #ffffff;
    margin-bottom: 20px;
}

.exercises-section .section-title .icon {
    font-size: 30px;
}

.exercises-accordion {
    margin-top: 15px;
}

.exercise-accordion-item {
    background: #ffffff;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0 12px 32px rgba(76, 29, 149, 0.18);
    overflow: hidden;
}

.exercise-accordion-item summary {
    cursor: pointer;
    padding: 18px 22px;
    font-size: 18px;
    font-weight: 600;
    color: #4338ca;
    background: rgba(99, 102, 241, 0.08);
    transition: all 0.3s ease;
    list-style: none;
}

.exercise-accordion-item[open] summary {
    background: rgba(99, 102, 241, 0.16);
}

.exercise-accordion-item summary::-webkit-details-marker {
    display: none;
}

.exercise-accordion-item summary::after {
    content: '▾';
    float: right;
    transition: transform 0.3s ease;
}

.exercise-accordion-item[open] summary::after {
    transform: rotate(180deg);
}

.exercise-content {
    padding: 20px 24px 30px 24px;
}

.exercise-block {
    background: #f9fafb;
    border-radius: 14px;
    padding: 20px;
    border: 1px solid rgba(148, 163, 184, 0.4);
}

.exercise-title {
    font-size: 20px;
    margin-bottom: 10px;
    color: #1f2937;
}

.exercise-intro {
    margin: 0 0 15px 0;
    color: #4b5563;
}

.check-btn {
    margin-top: 20px;
    padding: 12px 28px;
    background: linear-gradient(135deg, #6366f1 0%, #7c3aed 100%);
    border: none;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 8px 20px rgba(79, 70, 229, 0.35);
}

.check-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(79, 70, 229, 0.4);
}

.check-btn:active {
    transform: translateY(0);
}

/* Word Matching */
.matching-container {
    display: flex;
    gap: 24px;
    flex-wrap: wrap;
}

.words-column,
.translations-column {
    flex: 1;
    min-width: 260px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.word-item,
.translation-item {
    background: white;
    border-radius: 10px;
    padding: 14px 16px;
    border: 2px solid transparent;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 8px 20px rgba(148, 163, 184, 0.25);
}

.word-item:hover,
.translation-item:hover {
    border-color: #c7d2fe;
}

.word-item.selected,
.word-item.paired,
.translation-item.selected {
    border-color: #6366f1;
    background: #eef2ff;
}

.word-item.correct,
.translation-item.correct {
    border-color: #10b981;
    background: #d1fae5;
}

.word-item.incorrect,
.translation-item.incorrect {
    border-color: #ef4444;
    background: #fee2e2;
}

/* Articles */
.articles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 18px;
}

.article-item {
    background: white;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    border: 2px solid transparent;
    transition: border-color 0.2s ease;
}

.article-word .noun {
    display: block;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 6px;
}

.article-word small {
    color: #6b7280;
}

.article-buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 10px;
}

.article-buttons button {
    padding: 8px 16px;
    border-radius: 8px;
    background: #f3f4f6;
    border: 1px solid #d1d5db;
    cursor: pointer;
    transition: all 0.2s ease;
}

.article-buttons button.selected {
    background: #6366f1;
    color: white;
    border-color: #4f46e5;
}

.article-buttons button.correct {
    background: #10b981;
    border-color: #059669;
}

.article-buttons button.incorrect {
    background: #ef4444;
    border-color: #dc2626;
    color: white;
}

/* Synonyms */
.synonym-item {
    background: white;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 14px;
    display: flex;
    gap: 18px;
    align-items: center;
    box-shadow: 0 6px 14px rgba(79, 70, 229, 0.12);
}

.word-center {
    min-width: 160px;
    text-align: center;
}

.word-center .word-main {
    display: block;
    font-weight: 600;
    font-size: 20px;
    color: #4338ca;
}

.word-center small {
    color: #6b7280;
}

.synonym-item input {
    padding: 10px 14px;
    border-radius: 8px;
    border: 2px solid #d1d5db;
    font-size: 16px;
    width: 220px;
    transition: border-color 0.2s ease, background 0.2s ease;
}

.synonym-item input:focus {
    outline: none;
    border-color: #6366f1;
    background: #eef2ff;
}

.synonym-item input.correct {
    border-color: #10b981;
    background: #ecfdf5;
}

.synonym-item input.incorrect {
    border-color: #ef4444;
    background: #fef2f2;
}

/* Quiz */
.quiz-question {
    background: white;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: 0 8px 18px rgba(148, 163, 184, 0.18);
}

.quiz-question .question {
    margin-bottom: 14px;
    font-size: 18px;
    color: #1f2937;
}

.quiz-options {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.quiz-options label {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #f9fafb;
    border-radius: 8px;
    padding: 10px 12px;
    border: 2px solid transparent;
    cursor: pointer;
    transition: border-color 0.2s ease, background 0.2s ease;
}

.quiz-options label.correct {
    border-color: #10b981;
    background: #ecfdf5;
}

.quiz-options label.incorrect {
    border-color: #ef4444;
    background: #fee2e2;
}

.quiz-options input[type="radio"] {
    accent-color: #6366f1;
}

/* Context */
.context-item {
    background: white;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 14px;
    box-shadow: 0 6px 16px rgba(79, 70, 229, 0.12);
}

.context-german {
    font-weight: 600;
    color: #1f2937;
    margin-bottom: 8px;
}

.context-hint {
    color: #6b7280;
    margin-bottom: 12px;
}

.context-item input {
    width: 100%;
    padding: 10px 14px;
    border-radius: 8px;
    border: 2px solid #d1d5db;
    font-size: 16px;
    transition: border-color 0.2s ease, background 0.2s ease;
}

.context-item input.correct {
    border-color: #10b981;
    background: #ecfdf5;
}

.context-item input.incorrect {
    border-color: #ef4444;
    background: #fef2f2;
}

/* Sentence builder */
.sentence-builder {
    background: white;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 8px 18px rgba(148, 163, 184, 0.18);
}

.sentence-builder .translation {
    margin-bottom: 12px;
    color: #374151;
}

.word-pool {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 12px;
}

.draggable {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 14px;
    background: #6366f1;
    color: white;
    border-radius: 8px;
    cursor: grab;
    user-select: none;
    transition: transform 0.2s ease;
}

.draggable:active {
    cursor: grabbing;
    transform: scale(0.96);
}

.drop-zone {
    min-height: 56px;
    border: 2px dashed #c7d2fe;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
    background: #f5f3ff;
}

.drop-zone.drag-over {
    border-color: #4338ca;
    background: #ede9fe;
}

.drop-zone.correct {
    border-color: #10b981;
}

.drop-zone.incorrect {
    border-color: #ef4444;
}

.drop-zone .placeholder {
    color: #9ca3af;
}

/* Responsive */
@media (max-width: 768px) {
    .exercises-section {
        padding: 22px;
    }

    .exercise-content {
        padding: 16px 18px 24px 18px;
    }

    .synonym-item {
        flex-direction: column;
        align-items: stretch;
    }

    .synonym-item input {
        width: 100%;
    }

    .matching-container {
        flex-direction: column;
    }

    .word-pool {
        justify-content: center;
    }
}
"""

    def generate_js(self) -> str:
        """Return vanilla JS responsible for exercise interactions."""

        return """
/* ===== JAVASCRIPT ДЛЯ ИНТЕРАКТИВНЫХ УПРАЖНЕНИЙ ===== */

(function() {
    'use strict';

    function showResult(message) {
        if (typeof window !== 'undefined') {
            window.alert(message);
        }
    }

    // 1. Word matching
    document.addEventListener('click', function(event) {
        const wordItem = event.target.closest('.word-item');
        const translationItem = event.target.closest('.translation-item');

        if (wordItem) {
            document.querySelectorAll('.word-item').forEach(item => {
                item.classList.remove('selected');
            });
            wordItem.classList.add('selected');
            document.body.dataset.selectedWordId = wordItem.dataset.id;
        }

        if (translationItem) {
            const selectedId = document.body.dataset.selectedWordId;
            if (!selectedId) {
                return;
            }
            const word = document.querySelector(`.word-item[data-id="${selectedId}"]`);
            if (!word) {
                return;
            }

            // Remove previous binding for this word
            if (word.dataset.selectedId) {
                const previousTranslation = document.querySelector(`.translation-item[data-id="${word.dataset.selectedId}"]`);
                if (previousTranslation) {
                    previousTranslation.classList.remove('selected');
                    delete previousTranslation.dataset.selectedBy;
                }
            }

            // If translation already linked to another word - unlink it
            if (translationItem.dataset.selectedBy) {
                const previousWord = document.querySelector(`.word-item[data-id="${translationItem.dataset.selectedBy}"]`);
                if (previousWord) {
                    delete previousWord.dataset.selectedId;
                    previousWord.classList.remove('paired');
                }
            }

            translationItem.classList.add('selected');
            translationItem.dataset.selectedBy = selectedId;
            word.dataset.selectedId = translationItem.dataset.id;
            word.dataset.selected = translationItem.dataset.trans;
            word.classList.add('paired');
            document.body.dataset.selectedWordId = '';
        }
    });

    document.addEventListener('click', function(event) {
        const action = event.target.closest('[data-action]');
        if (!action) {
            return;
        }

        switch (action.dataset.action) {
            case 'check-matching':
                checkMatching();
                break;
            case 'check-articles':
                checkArticles();
                break;
            case 'check-synonyms':
                checkSynonyms();
                break;
            case 'check-quiz':
                checkQuiz();
                break;
            case 'check-context':
                checkContext();
                break;
            case 'check-builder':
                checkBuilder();
                break;
            default:
                break;
        }
    });

    function resetClasses(selector) {
        document.querySelectorAll(selector).forEach(element => {
            element.classList.remove('correct', 'incorrect');
        });
    }

    function checkMatching() {
        resetClasses('.word-item');
        resetClasses('.translation-item');
        const words = document.querySelectorAll('.word-item');
        let correct = 0;

        words.forEach(word => {
            const selected = word.dataset.selected;
            const answer = word.dataset.answer;
            const translationId = word.dataset.selectedId;
            if (!selected || !answer) {
                return;
            }
            const translationItem = translationId ? document.querySelector(`.translation-item[data-id="${translationId}"]`) : null;
            const isCorrect = selected === answer;
            if (isCorrect) {
                word.classList.add('correct');
                if (translationItem) {
                    translationItem.classList.add('correct');
                }
                correct += 1;
            } else {
                word.classList.add('incorrect');
                if (translationItem) {
                    translationItem.classList.add('incorrect');
                }
            }
        });

        showResult(`Правильно: ${correct} из ${words.length}`);
    }

    // 2. Articles
    document.addEventListener('click', function(event) {
        if (!event.target.matches('.article-buttons button')) {
            return;
        }
        const button = event.target;
        const container = button.closest('.article-buttons');
        container.querySelectorAll('button').forEach(item => item.classList.remove('selected'));
        button.classList.add('selected');
    });

    function checkArticles() {
        resetClasses('.article-buttons button');
        const items = document.querySelectorAll('.article-item');
        let correct = 0;

        items.forEach(item => {
            const selected = item.querySelector('.article-buttons button.selected');
            if (!selected) {
                return;
            }
            if (selected.dataset.article === item.dataset.correct) {
                selected.classList.add('correct');
                item.classList.add('correct');
                correct += 1;
            } else {
                selected.classList.add('incorrect');
                item.classList.add('incorrect');
            }
        });

        showResult(`Правильно: ${correct} из ${items.length}`);
    }

    // 3. Synonyms & Antonyms
    function checkSynonyms() {
        const inputs = document.querySelectorAll('#synonyms input');
        let correct = 0;
        inputs.forEach(input => {
            const expected = (input.dataset.correct || '').trim().toLowerCase();
            const value = (input.value || '').trim().toLowerCase();
            if (!expected) {
                return;
            }
            if (value === expected) {
                input.classList.add('correct');
                input.classList.remove('incorrect');
                correct += 1;
            } else {
                input.classList.add('incorrect');
                input.classList.remove('correct');
            }
        });
        showResult(`Правильно: ${correct} из ${inputs.length}`);
    }

    // 4. Quiz
    function checkQuiz() {
        const questions = document.querySelectorAll('.quiz-question');
        let correct = 0;
        questions.forEach(question => {
            const options = question.querySelectorAll('label');
            options.forEach(option => option.classList.remove('correct', 'incorrect'));
            const selected = question.querySelector('input[type="radio"]:checked');
            if (!selected) {
                return;
            }
            if (selected.dataset.correct === 'true') {
                selected.parentElement.classList.add('correct');
                correct += 1;
            } else {
                selected.parentElement.classList.add('incorrect');
            }
        });
        showResult(`Правильно: ${correct} из ${questions.length}`);
    }

    // 5. Context
    function checkContext() {
        const inputs = document.querySelectorAll('#context input');
        let correct = 0;
        inputs.forEach(input => {
            const expected = (input.dataset.correct || '').trim().toLowerCase();
            const value = (input.value || '').trim().toLowerCase();
            if (!expected) {
                return;
            }
            if (value === expected) {
                input.classList.add('correct');
                input.classList.remove('incorrect');
                correct += 1;
            } else {
                input.classList.add('incorrect');
                input.classList.remove('correct');
            }
        });
        showResult(`Правильно: ${correct} из ${inputs.length}`);
    }

    // 6. Sentence builder
    document.addEventListener('dragstart', function(event) {
        const draggable = event.target.closest('.draggable');
        if (!draggable) {
            return;
        }
        event.dataTransfer.effectAllowed = 'move';
        event.dataTransfer.setData('text/plain', draggable.textContent || '');
        draggable.classList.add('dragging');
    });

    document.addEventListener('dragend', function(event) {
        const draggable = event.target.closest('.draggable');
        if (!draggable) {
            return;
        }
        draggable.classList.remove('dragging');
    });

    document.addEventListener('dragover', function(event) {
        const zone = event.target.closest('.drop-zone');
        if (!zone) {
            return;
        }
        event.preventDefault();
        zone.classList.add('drag-over');
    });

    document.addEventListener('dragleave', function(event) {
        const zone = event.target.closest('.drop-zone');
        if (!zone) {
            return;
        }
        zone.classList.remove('drag-over');
    });

    document.addEventListener('drop', function(event) {
        const zone = event.target.closest('.drop-zone');
        if (!zone) {
            return;
        }
        event.preventDefault();
        zone.classList.remove('drag-over');
        const dragging = document.querySelector('.draggable.dragging');
        if (!dragging) {
            return;
        }
        const clone = dragging.cloneNode(true);
        clone.classList.remove('dragging');
        dragging.remove();
        zone.appendChild(clone);
        const placeholder = zone.querySelector('.placeholder');
        if (placeholder) {
            placeholder.remove();
        }
    });

    function checkBuilder() {
        const builders = document.querySelectorAll('.sentence-builder');
        let correct = 0;
        builders.forEach(builder => {
            const zone = builder.querySelector('.drop-zone');
            if (!zone) {
                return;
            }
            const words = Array.from(zone.querySelectorAll('.draggable')).map(item => item.textContent || '');
            const assembled = words.join(' ').trim();
            const answer = (zone.dataset.correct || '').trim();
            if (!answer) {
                return;
            }
            if (assembled === answer) {
                zone.classList.remove('incorrect');
                zone.classList.add('correct');
                correct += 1;
            } else {
                zone.classList.remove('correct');
                zone.classList.add('incorrect');
            }
        });
        showResult(`Правильно: ${correct} из ${builders.length}`);
    }
})();
"""


__all__ = ["ExercisesAssetsGenerator"]
