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
    color: #1f2937;
    background: #f1f5f9;
    transition: all 0.3s ease;
    list-style: none;
}

.exercise-accordion-item[open] summary {
    background: #e2e8f0;
    color: #312e81;
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

/* Миттєва візуальна реакція */
.word-item.correct,
.translation-item.correct {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    transform: scale(0.95);
    opacity: 0.9;
    pointer-events: none;
    border-color: #10b981;
    transition: all 0.3s ease;
}

.word-item.incorrect,
.translation-item.incorrect {
    background: linear-gradient(135deg, #ef4444, #dc2626) !important;
    animation: shake 0.5s;
    color: white !important;
    border-color: #ef4444;
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
}

/* Прогрес-бар */
.matching-progress {
    margin: 20px 0;
    text-align: center;
}

.progress-track {
    height: 8px;
    background: #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
    margin: 10px 0;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    transition: width 0.3s ease;
}

.progress-text {
    font-weight: 600;
    color: #4b5563;
    font-size: 14px;
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
    transition: all 0.3s ease;
}

/* Картка слова після правильної відповіді */
.article-item.completed {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7) !important;
    border: 2px solid #22c55e;
    transform: scale(0.98);
    transition: all 0.3s ease;
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
    border: 2px solid #d1d5db;
    cursor: pointer;
    transition: all 0.3s ease;
}

.article-buttons button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.article-buttons button.selected {
    background: #6366f1;
    color: white;
    border-color: #4f46e5;
}

/* Кнопка з правильною відповіддю */
.article-buttons button.correct {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white;
    border-color: #16a34a;
    transform: scale(1.1);
    pointer-events: none;
}

/* Кнопка з неправильною відповіддю */
.article-buttons button.incorrect {
    background: linear-gradient(135deg, #ef4444, #dc2626) !important;
    color: white;
    animation: shake 0.5s;
}

/* Прогрес-бар для вправи артиклів */
.articles-progress {
    margin: 20px 0;
    padding: 15px;
    background: rgba(255,255,255,0.1);
    border-radius: 12px;
}

.articles-progress .progress-track {
    height: 10px;
    background: #e2e8f0;
    border-radius: 5px;
    overflow: hidden;
}

.articles-progress .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    transition: width 0.5s ease;
}

.articles-progress .progress-stats {
    text-align: center;
    margin-top: 10px;
    font-size: 14px;
    color: #4b5563;
}

#articles-correct {
    color: #22c55e;
    font-weight: bold;
    font-size: 18px;
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

/* Interactive Quiz */
.quiz-container {
    max-width: 820px;
    margin: 0 auto;
    padding: 40px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-radius: 24px;
    box-shadow: 0 25px 55px rgba(15, 23, 42, 0.12);
}

/* Quiz Header */
.quiz-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    color: #475569;
}

.question-number {
    font-size: 15px;
    font-weight: 600;
    color: #475569;
    background: rgba(255, 255, 255, 0.7);
    padding: 6px 18px;
    border-radius: 999px;
}

.question-mode {
    font-size: 14px;
    font-weight: 600;
    color: #ffffff;
    background: #8b5cf6;
    padding: 6px 16px;
    border-radius: 999px;
}

/* Word Display */
.quiz-content {
    text-align: center;
    padding: 0 10px;
}

.quiz-content h3 {
    color: #1f2937;
    font-size: 24px;
    margin-bottom: 24px;
    font-weight: 600;
}

.word-display {
    text-align: center;
    margin: 30px 0;
    padding: 28px;
    background: rgba(255, 255, 255, 0.95);
    border-radius: 18px;
    box-shadow: 0 15px 40px rgba(15, 23, 42, 0.08);
}

.german-word,
.russian-word {
    font-size: 40px;
    font-weight: 700;
    color: #1f2937;
    letter-spacing: 0.01em;
}

.transcription {
    display: block;
    margin-top: 12px;
    font-size: 18px;
    color: #64748b;
    font-style: italic;
}

/* Answer Buttons - ГРАДІЄНТНИЙ ДИЗАЙН */
.answer-buttons {
    display: grid;
    gap: 15px;
    margin: 30px auto;
    max-width: 900px;
}

/* Адаптивна сітка для різних пристроїв */
@media (max-width: 575px) {
    .answer-buttons {
        grid-template-columns: 1fr;
    }
}

@media (min-width: 576px) and (max-width: 991px) {
    .answer-buttons {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 992px) {
    .answer-buttons {
        grid-template-columns: repeat(4, 1fr);
    }
    /* Якщо тільки 2 варіанти */
    .answer-buttons:has(.answer-btn:nth-child(2):last-child) {
        grid-template-columns: repeat(2, 1fr);
        max-width: 600px;
    }
    /* Якщо 3 варіанти */
    .answer-buttons:has(.answer-btn:nth-child(3):last-child) {
        grid-template-columns: repeat(3, 1fr);
        max-width: 750px;
    }
}

.answer-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 18px 24px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    text-align: center;
    min-height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.answer-btn:hover:not(.disabled) {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6);
    background: linear-gradient(135deg, #7c8ff0 0%, #8a5bb0 100%);
}

.answer-btn:active {
    transform: translateY(0);
    box-shadow: 0 2px 10px rgba(102, 126, 234, 0.4);
}

/* Correct/Incorrect States */
.answer-btn.correct {
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    animation: correctPulse 0.6s ease;
}

.answer-btn.incorrect {
    background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    animation: shake 0.5s ease;
}

.answer-btn.disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

@keyframes correctPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

/* Quiz Progress */
.quiz-progress {
    margin-bottom: 30px;
    background: rgba(255, 255, 255, 0.9);
    padding: 20px 24px;
    border-radius: 18px;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
}

.quiz-progress .progress-bar {
    height: 20px;
    background: #e2e8f0;
    border-radius: 999px;
    overflow: hidden;
}

.quiz-progress .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #8b5cf6, #6366f1);
    transition: width 0.5s ease;
}

.quiz-progress .progress-text {
    text-align: center;
    color: #475569;
    margin-top: 12px;
    font-size: 16px;
    font-weight: 600;
}

/* Quiz Results */
.quiz-results {
    text-align: center;
    padding: 32px;
    background: rgba(255, 255, 255, 0.92);
    border-radius: 18px;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.12);
}

.result-text {
    color: #475569;
    font-size: 16px;
    line-height: 1.6;
}

.result-text h3 {
    font-size: 26px;
    margin-bottom: 12px;
    color: #1f2937;
}

.result-text p {
    margin: 6px 0;
    color: #475569;
    font-size: 16px;
}

.result-details {
    margin-top: 16px;
    display: grid;
    gap: 4px;
    color: #4a5568;
    font-weight: 500;
}

.result-emoji {
    font-size: 28px;
    margin-top: 18px;
}

.restart-btn {
    margin-top: 24px;
    padding: 14px 36px;
    border: 2px solid transparent;
    border-radius: 999px;
    background: #ffffff;
    color: #4c1d95;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 12px 32px rgba(99, 102, 241, 0.18);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}

.restart-btn:hover {
    transform: translateY(-1px);
    border-color: #c4b5fd;
    box-shadow: 0 16px 40px rgba(99, 102, 241, 0.25);
}

/* Animations */
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
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

/* Контроли для кожного речення */
.sentence-controls {
    display: flex;
    gap: 10px;
    margin-top: 15px;
    align-items: center;
    padding: 10px;
    background: rgba(139, 92, 246, 0.05);
    border-radius: 8px;
}

.hint-btn {
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s;
    box-shadow: 0 2px 8px rgba(251, 191, 36, 0.3);
}

.hint-btn:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(251, 191, 36, 0.4);
}

.hint-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    background: #9ca3af;
}

.check-sentence-btn {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

.check-sentence-btn:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}

.check-sentence-btn:disabled {
    background: #6b7280;
    cursor: not-allowed;
}

.sentence-feedback {
    margin-left: auto;
    font-weight: 600;
    font-size: 14px;
    padding: 4px 12px;
    border-radius: 6px;
    min-width: 120px;
    text-align: center;
}

.sentence-feedback.correct {
    color: #10b981;
    background: rgba(16, 185, 129, 0.1);
}

.sentence-feedback.incorrect {
    color: #ef4444;
    background: rgba(239, 68, 68, 0.1);
}

/* Стани drop-zone */
.drop-zone.hint-active {
    background: linear-gradient(135deg, rgba(254, 243, 199, 0.2), rgba(251, 191, 36, 0.1));
    border: 2px solid #f59e0b;
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.3);
}

/* Підказка tooltip */
.hint-tooltip {
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: white;
    padding: 10px 15px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    z-index: 1000;
    white-space: nowrap;
    animation: fadeIn 0.3s;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    margin-bottom: 5px;
}

.hint-tooltip::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    border: 6px solid transparent;
    border-top-color: #f59e0b;
}

/* Прогрес для конструктора */
.builder-progress {
    margin-bottom: 25px;
    padding: 20px;
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(236, 72, 153, 0.05));
    border-radius: 12px;
    border: 1px solid rgba(139, 92, 246, 0.2);
}

.builder-progress-bar {
    height: 12px;
    background: #e2e8f0;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}

.builder-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    width: 0%;
    box-shadow: 0 2px 8px rgba(139, 92, 246, 0.4);
}

.builder-stats {
    text-align: center;
    margin-top: 12px;
    color: #6b7280;
    font-size: 14px;
    font-weight: 600;
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

    // 1. Word matching with instant feedback
    let selectedPrompt = null;
    let selectedMatch = null;
    let correctPairs = 0;
    
    window.handleWordClick = function(element, type) {
        // Якщо карточка вже правильна - ігнорувати
        if (element.classList.contains('correct')) return;
        
        // Видалити попередній вибір того ж типу
        document.querySelectorAll(`.word-item.${type}.selected`)
            .forEach(el => el.classList.remove('selected'));
        
        element.classList.add('selected');
        
        if (type === 'prompt') {
            selectedPrompt = element;
            if (selectedMatch && !selectedMatch.classList.contains('correct')) {
                checkMatch(selectedPrompt, selectedMatch);
            }
        } else {
            selectedMatch = element;
            if (selectedPrompt && !selectedPrompt.classList.contains('correct')) {
                checkMatch(selectedPrompt, selectedMatch);
            }
        }
    };
    
    function checkMatch(promptCard, matchCard) {
        const isCorrect = promptCard.dataset.pairId === matchCard.dataset.pairId;
        
        if (isCorrect) {
            // Правильна відповідь
            promptCard.classList.add('correct');
            matchCard.classList.add('correct');
            promptCard.classList.remove('selected');
            matchCard.classList.remove('selected');
            
            correctPairs++;
            updateProgress();
            
            // Перевірка завершення
            const totalPairs = document.querySelectorAll('#word-matching .word-item.prompt').length;
            if (correctPairs === totalPairs) {
                setTimeout(() => {
                    showResult('Вітаємо! Ви виконали вправу!');
                }, 500);
            }
        } else {
            // Неправильна відповідь
            promptCard.classList.add('incorrect');
            matchCard.classList.add('incorrect');
            
            setTimeout(() => {
                promptCard.classList.remove('incorrect', 'selected');
                matchCard.classList.remove('incorrect', 'selected');
            }, 500);
        }
        
        selectedPrompt = null;
        selectedMatch = null;
    }
    
    function updateProgress() {
        const progressFill = document.querySelector('#word-matching .progress-fill');
        const progressText = document.querySelector('#word-matching .progress-text');
        const totalPairs = document.querySelectorAll('#word-matching .word-item.prompt').length;
        
        if (progressFill) {
            progressFill.style.width = `${(correctPairs/totalPairs)*100}%`;
        }
        if (progressText) {
            progressText.textContent = `${correctPairs} з ${totalPairs}`;
        }
    }

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

    // 2. Articles - Миттєва перевірка артиклів
    let articlesAnswered = 0;
    let articlesTotal = 0;
    
    // Ініціалізація при завантаженні
    document.addEventListener('DOMContentLoaded', function() {
        const items = document.querySelectorAll('.article-item');
        articlesTotal = items.length;
        const totalElement = document.getElementById('articles-total');
        if (totalElement) {
            totalElement.textContent = articlesTotal;
        }
    });
    
    window.checkArticleInstant = function(button, selectedArticle) {
        // Отримуємо батьківські елементи
        const buttonsContainer = button.parentElement;
        const articleItem = buttonsContainer.parentElement;
        const correctArticle = articleItem.getAttribute('data-correct');
        
        // Перевіряємо чи вже відповідали
        if (articleItem.classList.contains('completed')) {
            return;
        }
        
        // Видаляємо попередні класи з кнопок
        buttonsContainer.querySelectorAll('button').forEach(btn => {
            btn.classList.remove('correct', 'incorrect');
        });
        
        if (selectedArticle === correctArticle) {
            // Правильна відповідь
            button.classList.add('correct');
            articleItem.classList.add('completed');
            articlesAnswered++;
            
            // Блокуємо всі кнопки для цього слова
            buttonsContainer.querySelectorAll('button').forEach(btn => {
                btn.disabled = true;
            });
            
            // Оновлюємо прогрес
            updateArticlesProgress();
            
            // Перевірка завершення
            if (articlesAnswered === articlesTotal) {
                setTimeout(() => {
                    showResult('Вітаємо! Ви правильно визначили всі артиклі! 🎉');
                }, 500);
            }
        } else {
            // Неправильна відповідь
            button.classList.add('incorrect');
            
            // Прибираємо червоний колір через 500мс
            setTimeout(() => {
                button.classList.remove('incorrect');
            }, 500);
        }
    };
    
    function updateArticlesProgress() {
        // Оновлюємо лічильник
        const correctElement = document.getElementById('articles-correct');
        if (correctElement) {
            correctElement.textContent = articlesAnswered;
        }
        
        // Оновлюємо прогрес-бар
        const progressFill = document.querySelector('.articles-progress .progress-fill');
        if (progressFill) {
            const percentage = articlesTotal > 0 ? (articlesAnswered / articlesTotal) * 100 : 0;
            progressFill.style.width = percentage + '%';
        }
    }

    // Стара функція checkArticles більше не потрібна
    function checkArticles() {
        // Залишено для сумісності, якщо хтось викличе старий спосіб
        showResult('Миттєва перевірка вже включена!');
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

    // 4. Interactive Quiz with dual modes
    let currentQuestion = 0;
    let correctAnswers = 0;
    let totalQuestions = 0;
    let answeredQuestions = [];
    let deRuCorrect = 0;
    let ruDeCorrect = 0;
    let deRuTotal = 0;
    let ruDeTotal = 0;

    function showQuestion(index) {
        const questions = document.querySelectorAll('#word-quiz .quiz-question');
        questions.forEach((question, idx) => {
            question.style.display = idx === index ? 'block' : 'none';
        });
    }

    function updateQuizProgress() {
        const progressFill = document.querySelector('#word-quiz .progress-fill');
        const correctCount = document.getElementById('correct-count');
        const answered = answeredQuestions.length;
        const percentage = totalQuestions ? (answered / totalQuestions) * 100 : 0;

        if (progressFill) {
            progressFill.style.width = `${percentage}%`;
        }
        if (correctCount) {
            correctCount.textContent = correctAnswers;
        }
    }

    function showResults() {
        const questionsWrapper = document.getElementById('quiz-questions');
        const resultWrapper = document.getElementById('quiz-result');
        const resultText = resultWrapper ? resultWrapper.querySelector('.result-text') : null;

        if (questionsWrapper) {
            questionsWrapper.style.display = 'none';
        }
        if (resultWrapper) {
            resultWrapper.style.display = 'block';
        }

        const percentage = totalQuestions ? Math.round((correctAnswers / totalQuestions) * 100) : 0;

        let encouragement = '💪 Спробуйте ще раз! Практика - запорука успіху!';
        if (percentage >= 80) {
            encouragement = '🎉 Чудово! Ви відмінно знаєте слова!';
        } else if (percentage >= 60) {
            encouragement = '👍 Добре! Продовжуйте практикуватися!';
        }

        const message = `
            <h3>Результати вікторини</h3>
            <p>Загальний результат: ${correctAnswers} з ${totalQuestions} (${percentage}%)</p>
            <div class="result-details">
                <p>DE → RU: ${deRuCorrect} з ${deRuTotal}</p>
                <p>RU → DE: ${ruDeCorrect} з ${ruDeTotal}</p>
            </div>
            <p class="result-emoji">${encouragement}</p>
        `;

        if (resultText) {
            resultText.innerHTML = message;
        }
    }

    function initializeQuiz() {
        const quizContainer = document.getElementById('word-quiz');
        if (!quizContainer) {
            return;
        }

        const questions = quizContainer.querySelectorAll('.quiz-question');
        if (!questions.length) {
            return;
        }

        currentQuestion = 0;
        correctAnswers = 0;
        deRuCorrect = 0;
        ruDeCorrect = 0;
        deRuTotal = 0;
        ruDeTotal = 0;
        answeredQuestions = [];
        totalQuestions = questions.length;

        questions.forEach((question, index) => {
            const mode = question.dataset.mode;
            if (mode === 'de-ru') {
                deRuTotal += 1;
            } else if (mode === 'ru-de') {
                ruDeTotal += 1;
            }

            question.style.display = index === 0 ? 'block' : 'none';
            question.classList.remove('completed');
            question.querySelectorAll('.answer-btn').forEach(btn => {
                btn.classList.remove('correct', 'incorrect', 'disabled');
            });
        });

        const totalCount = document.getElementById('total-count');
        if (totalCount) {
            totalCount.textContent = totalQuestions;
        }

        const progressFill = document.querySelector('#word-quiz .progress-fill');
        if (progressFill) {
            progressFill.style.width = '0%';
        }

        const correctCount = document.getElementById('correct-count');
        if (correctCount) {
            correctCount.textContent = '0';
        }

        const resultWrapper = document.getElementById('quiz-result');
        if (resultWrapper) {
            resultWrapper.style.display = 'none';
            const resultText = resultWrapper.querySelector('.result-text');
            if (resultText) {
                resultText.innerHTML = '';
            }
        }

        const questionsWrapper = document.getElementById('quiz-questions');
        if (questionsWrapper) {
            questionsWrapper.style.display = 'block';
        }

        updateQuizProgress();
    }

    window.checkAnswer = function(button, isCorrect) {
        if (!button) {
            return;
        }
        if (button.classList.contains('disabled')) {
            return;
        }

        const question = button.closest('.quiz-question');
        if (!question || question.classList.contains('completed')) {
            return;
        }

        const mode = question.dataset.mode || 'de-ru';
        const buttons = question.querySelectorAll('.answer-btn');

        buttons.forEach(btn => {
            btn.classList.add('disabled');
            if (btn.dataset.correct === 'true') {
                btn.classList.add('correct');
            }
        });

        if (isCorrect) {
            button.classList.add('correct');
            correctAnswers += 1;
            if (mode === 'de-ru') {
                deRuCorrect += 1;
            } else if (mode === 'ru-de') {
                ruDeCorrect += 1;
            }
        } else {
            button.classList.add('incorrect');
        }

        answeredQuestions.push({
            question: currentQuestion,
            correct: Boolean(isCorrect),
            mode: mode
        });

        question.classList.add('completed');
        updateQuizProgress();

        setTimeout(() => {
            if (currentQuestion < totalQuestions - 1) {
                currentQuestion += 1;
                showQuestion(currentQuestion);
            } else {
                showResults();
            }
        }, 1500);
    };

    window.checkQuizAnswer = window.checkAnswer;

    window.restartQuiz = function() {
        initializeQuiz();
    };

    document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('word-quiz')) {
            initializeQuiz();
        }
    });

    function checkQuiz() {
        showResult('Використовуйте нову інтерактивну вікторину!');
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
