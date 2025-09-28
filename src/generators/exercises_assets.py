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

/* Word Matching - FULL HEIGHT WITHOUT SCROLL */
.word-selection-container {
    margin-top: 16px;
}

.word-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;  /* Увеличить gap с 20px до 24px */
    /* КРИТИЧНО: Увеличить высоту для размещения всех 12 слов */
    min-height: 680px;  /* Изменить с height: 520px на min-height: 680px */
    background: rgba(255, 255, 255, 0.5);
    border-radius: 12px;
    padding: 20px;  /* Увеличить padding с 16px до 20px */
}

.word-column {
    display: flex;
    flex-direction: column;
    height: 100%;  /* Изменить с overflow: hidden на height: 100% */
}

.word-column h4 {
    text-align: center;
    color: #4b5563;
    font-weight: 600;
    margin: 0 0 14px 0;  /* Увеличить margin с 12px до 14px */
    padding-bottom: 10px;  /* Увеличить с 8px до 10px */
    border-bottom: 2px solid #e2e8f0;
    font-size: 14px;  /* Увеличить с 13px до 14px */
    flex-shrink: 0;  /* Добавить flex-shrink: 0 */
}

.word-list {
    /* БЕЗ скролла - все слова должны быть видимы */
    flex: 1;
    padding: 6px;  /* Увеличить с 4px до 6px */
    display: flex;
    flex-direction: column;
    gap: 8px;  /* Увеличить gap с 6px до 8px для лучшего spacing */
    overflow: visible;  /* Оставить visible - без прокрутки */
}

/* Компактные но читаемые размеры слов */
.word-item {
    background: white;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 14px;  /* Увеличить padding с 8px 12px до 10px 14px */
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: left;
    font-size: 14px;
    min-height: 44px;  /* Увеличить с 38px до 44px */
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex-shrink: 0;  /* Добавить flex-shrink: 0 чтобы элементы не сжимались */
}

.word-item:hover:not(.correct):not(.disabled) {
    border-color: #a78bfa;
    background: #f9fafb;
    transform: translateX(2px);
}

.word-item.selected {
    background: linear-gradient(135deg, #eef2ff, #e0e7ff);
    border-color: #6366f1;
    transform: scale(1.01);
}

.word-item.correct {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    border-color: #16a34a;
    transform: scale(0.97);
    opacity: 0.9;
    pointer-events: none;
}

.word-item.incorrect {
    background: linear-gradient(135deg, #ef4444, #dc2626) !important;
    color: white !important;
    animation: shake 0.5s;
}

.word-item .word-main {
    font-weight: 600;
    display: block;
    font-size: 15px;  /* Увеличить с 14px до 15px */
    line-height: 1.3;  /* Увеличить с 1.2 до 1.3 */
}

.word-item .transcription {
    font-size: 12px;  /* Увеличить с 11px до 12px */
    color: #6b7280;
    margin-top: 3px;  /* Увеличить с 2px до 3px */
    font-style: italic;
    opacity: 0.85;  /* Добавить opacity для лучшей читаемости */
}

.word-item.correct .transcription {
    color: rgba(255, 255, 255, 0.9);
}

/* Responsive для Word Matching */
@media (max-width: 1024px) {
    .word-columns {
        min-height: 600px;  /* Уменьшить высоту для планшетов */
        padding: 16px;
        gap: 20px;
    }
    
    .word-item {
        padding: 8px 12px;
        min-height: 40px;
    }
    
    .word-item .word-main {
        font-size: 14px;
    }
    
    .word-item .transcription {
        font-size: 11px;
    }
    
    .word-list {
        gap: 6px;
    }
}

/* Responsive для мобильных */
@media (max-width: 640px) {
    /* На мобильных - одна колонка с прокруткой */
    .word-columns {
        grid-template-columns: 1fr;
        min-height: auto;
        max-height: 650px;
        overflow-y: auto;  /* Добавить скролл только на мобильных */
    }
    
    .word-column {
        max-height: none;
    }
    
    .word-column:first-child {
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .word-list {
        gap: 10px;
    }
}

/* Кастомный скролл для мобильных */
@media (max-width: 640px) {
    .word-columns::-webkit-scrollbar {
        width: 6px;
    }
    
    .word-columns::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 3px;
    }
    
    .word-columns::-webkit-scrollbar-thumb {
        background: #a78bfa;
        border-radius: 3px;
    }
}

/* Articles */

/* Кольорова система для родів */
.article-color-legend {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 20px;
    padding: 12px;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 8px;
}

.legend-item {
    font-size: 14px;
    font-weight: 600;
    padding: 5px 10px;
    border-radius: 6px;
}

.legend-item.masculine {
    color: #2B6CB0;
    background: rgba(43, 108, 176, 0.1);
}

.legend-item.feminine {
    color: #C53030;
    background: rgba(197, 48, 48, 0.1);
}

.legend-item.neutral {
    color: #D69E2E;
    background: rgba(236, 201, 75, 0.1);
}

/* Кольорові кнопки артиклів */
.article-buttons button[data-article="der"] {
    border-color: #2B6CB0;
    color: #2B6CB0;
}

.article-buttons button[data-article="die"] {
    border-color: #C53030;
    color: #C53030;
}

.article-buttons button[data-article="das"] {
    border-color: #D69E2E;
    color: #D69E2E;
}

.article-buttons button[data-article="der"]:hover {
    background: #2B6CB0;
    color: white;
}

.article-buttons button[data-article="die"]:hover {
    background: #C53030;
    color: white;
}

.article-buttons button[data-article="das"]:hover {
    background: #ECC94B;
    color: #333;
}

/* Правильна відповідь */
.article-buttons button[data-article="der"].correct {
    background: #2B6CB0 !important;
    color: white !important;
}

.article-buttons button[data-article="die"].correct {
    background: #C53030 !important;
    color: white !important;
}

.article-buttons button[data-article="das"].correct {
    background: #ECC94B !important;
    color: #333 !important;
}

/* Кольорові артиклі у словнику */
.word-german .article-der {
    color: #2B6CB0;
    font-weight: bold;
}

.word-german .article-die {
    color: #C53030;
    font-weight: bold;
}

.word-german .article-das {
    color: #D69E2E;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

/* Тонка кольорова лінія зліва від картки */
.word-card[data-gender="masculine"] {
    border-left: 3px solid #2B6CB0;
}

.word-card[data-gender="feminine"] {
    border-left: 3px solid #C53030;
}

.word-card[data-gender="neutral"] {
    border-left: 3px solid #ECC94B;
}

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
        transform: translateX(-50%) translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateX(-50%) translateY(0);
    }
}

@keyframes bounceIn {
    0% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(0.8);
    }
    60% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1.05);
    }
    100% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
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
    background: rgba(255, 255, 255, 0.05);
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
    transform: translateX(-50%) translateY(0);
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
    background: linear-gradient(135deg, rgba(209, 250, 229, 0.3), rgba(16, 185, 129, 0.1));
    border: 2px solid #10b981;
    animation: correctPulse 0.6s;
}

.drop-zone.incorrect {
    background: linear-gradient(135deg, rgba(254, 226, 226, 0.3), rgba(239, 68, 68, 0.1));
    border: 2px solid #ef4444;
    animation: shake 0.5s;
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

    .word-pool {
        justify-content: center;
    }
}

@media (max-width: 640px) {
    .matching-container {
        flex-direction: column;
    }

    .words-column,
    .translations-column {
        min-width: 100%;
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

        // 1. Word matching with two columns
    let selectedGerman = null;
    let selectedRussian = null;
    let correctPairs = 0;
    let matchedPairs = new Set();

    window.handleWordPairClick = function(element, pairId, type) {
        // Проверяем, не выбрана ли уже эта пара
        if (element.classList.contains('correct')) return;
        if (matchedPairs.has(pairId)) return;
        
        // Убираем предыдущий выбор того же типа
        document.querySelectorAll(`.word-item.${type}-word.selected`)
            .forEach(el => el.classList.remove('selected'));
        
        element.classList.add('selected');
        
        if (type === 'german') {
            selectedGerman = element;
            // Если уже выбран русский перевод - проверяем
            if (selectedRussian && !selectedRussian.classList.contains('correct')) {
                checkWordMatch();
            }
        } else {
            selectedRussian = element;
            // Если уже выбрано немецкое слово - проверяем
            if (selectedGerman && !selectedGerman.classList.contains('correct')) {
                checkWordMatch();
            }
        }
    };
    
    function checkWordMatch() {
        if (!selectedGerman || !selectedRussian) return;
        
        const germanPairId = selectedGerman.dataset.pairId;
        const russianPairId = selectedRussian.dataset.pairId;
        
        if (germanPairId === russianPairId) {
            // Правильная пара
            selectedGerman.classList.add('correct');
            selectedRussian.classList.add('correct');
            selectedGerman.classList.remove('selected');
            selectedRussian.classList.remove('selected');
            
            matchedPairs.add(parseInt(germanPairId));
            correctPairs++;
            
            updateMatchingProgress();
            
            // Проверка завершения
            const totalPairs = document.querySelectorAll('#word-matching .german-word').length;
            if (correctPairs === totalPairs) {
                setTimeout(() => {
                    showResult('🎉 Отлично! Все пары найдены правильно!');
                }, 500);
            }
        } else {
            // Неправильная пара
            selectedGerman.classList.add('incorrect');
            selectedRussian.classList.add('incorrect');
            
            setTimeout(() => {
                selectedGerman.classList.remove('incorrect', 'selected');
                selectedRussian.classList.remove('incorrect', 'selected');
            }, 600);
        }
        
        // Сбрасываем выбор
        selectedGerman = null;
        selectedRussian = null;
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

    // 6. Sentence builder with individual controls
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

        zone.classList.remove('incorrect', 'correct', 'hint-active');

        const builder = zone.closest('.sentence-builder');
        if (builder) {
            const feedback = builder.querySelector('.sentence-feedback');
            if (feedback) {
                feedback.textContent = '';
                feedback.classList.remove('correct', 'incorrect');
            }
            const index = resolveBuilderIndex(builder);
            if (sentenceStates[index]) {
                return;
            }
            const checkBtn = builder.querySelector('.check-sentence-btn');
            if (checkBtn) {
                checkBtn.disabled = false;
                checkBtn.textContent = '✓ Перевірити';
            }
        }
    });

    function resolveBuilderIndex(builder) {
        if (!builder) {
            return -1;
        }
        const dataIndex = builder.dataset.sentenceIdx;
        const parsed = Number.parseInt(dataIndex || '', 10);
        if (!Number.isNaN(parsed)) {
            return parsed;
        }
        const builders = Array.from(document.querySelectorAll('.sentence-builder'));
        return builders.indexOf(builder);
    }

    function initializeSentenceBuilder() {
        const builders = document.querySelectorAll('.sentence-builder');
        sentenceStates = {};
        hintUsage = {};
        totalSentences = builders.length;
        correctSentences = 0;
        completionShown = false;

        builders.forEach((builder, idx) => {
            sentenceStates[idx] = false;
            hintUsage[idx] = 0;

            const dropZone = builder.querySelector('.drop-zone');
            if (dropZone) {
                dropZone.classList.remove('correct', 'incorrect', 'hint-active');
                dropZone.style.pointerEvents = '';
                if (!dropZone.children.length) {
                    const placeholder = document.createElement('span');
                    placeholder.className = 'placeholder';
                    placeholder.textContent = 'Перетащите слова сюда';
                    dropZone.appendChild(placeholder);
                }
            }

            const feedback = builder.querySelector('.sentence-feedback');
            if (feedback) {
                feedback.textContent = '';
                feedback.classList.remove('correct', 'incorrect');
            }

            const hintBtn = builder.querySelector('.hint-btn');
            if (hintBtn) {
                hintBtn.disabled = false;
                hintBtn.textContent = '💡 Підказка';
            }

            const checkBtn = builder.querySelector('.check-sentence-btn');
            if (checkBtn) {
                checkBtn.disabled = false;
                checkBtn.textContent = '✓ Перевірити';
            }
        });

        updateBuilderProgress();
    }

    function ensureProgressInfo() {
        const container = document.querySelector('.sentence-builder-section');
        if (!container) {
            return null;
        }
        let progressInfo = container.querySelector('.progress-info');
        if (!progressInfo) {
            progressInfo = document.createElement('div');
            progressInfo.className = 'progress-info';
            progressInfo.style.cssText = `
                margin: 20px 0;
                padding: 15px;
                background: rgba(139, 92, 246, 0.1);
                border-radius: 12px;
                text-align: center;
                font-size: 16px;
                font-weight: 600;
                color: #8b5cf6;
            `;
            const progressBlock = container.querySelector('.builder-progress');
            if (progressBlock) {
                container.insertBefore(progressInfo, progressBlock);
            } else {
                container.insertBefore(progressInfo, container.firstChild);
            }
        }
        return progressInfo;
    }

    function updateBuilderProgress() {
        const percentage = totalSentences ? Math.round((correctSentences / totalSentences) * 100) : 0;
        const progressFill = document.querySelector('.sentence-builder-section .builder-progress-fill');
        if (progressFill) {
            progressFill.style.width = `${percentage}%`;
        }
        const stats = document.querySelector('.sentence-builder-section .builder-stats');
        if (stats) {
            stats.textContent = `Виконано: ${correctSentences} з ${totalSentences}`;
        }
        const progressInfo = ensureProgressInfo();
        if (progressInfo) {
            progressInfo.innerHTML = `
                📊 Прогрес: ${correctSentences} з ${totalSentences} речень (${percentage}%)
                ${correctSentences === totalSentences && totalSentences > 0 ? '<br>🎉 Вітаємо! Всі речення виконано!' : ''}
            `;
        }
        if (correctSentences === totalSentences && totalSentences > 0 && !completionShown) {
            completionShown = true;
            setTimeout(() => {
                showCompletionMessage();
            }, 500);
        }
    }

    function getRandomBuilderMessage(type) {
        const messages = {
            correct: ['✅ Чудово!', '✅ Відмінно!', '✅ Супер!', '✅ Браво!', '✅ Молодець!'],
            incorrect: ['❌ Спробуйте ще!', '❌ Майже!', '❌ Не здавайтеся!', '❌ Подумайте ще!']
        };
        const pool = messages[type] || [];
        return pool[Math.floor(Math.random() * pool.length)] || '';
    }

    window.showHint = function(button) {
        const builder = button.closest('.sentence-builder');
        if (!builder) {
            return;
        }
        const index = resolveBuilderIndex(builder);
        if (index < 0) {
            return;
        }
        const dropZone = builder.querySelector('.drop-zone');
        if (!dropZone) {
            return;
        }
        const correctAnswer = (dropZone.dataset.correct || '').trim();
        if (!correctAnswer) {
            return;
        }

        hintUsage[index] = (hintUsage[index] || 0) + 1;

        const words = correctAnswer.split(new RegExp('\\s+'));
        let hintWords;
        if (hintUsage[index] === 1) {
            hintWords = words.slice(0, Math.min(2, words.length));
        } else if (hintUsage[index] === 2) {
            hintWords = words.slice(0, Math.ceil(words.length / 2));
        } else {
            hintWords = words.slice(0, Math.max(words.length - 1, 1));
        }
        const hintText = `${hintWords.join(' ')}...`;

        dropZone.classList.add('hint-active');

        const existingTooltip = button.querySelector('.hint-tooltip');
        if (existingTooltip) {
            existingTooltip.remove();
        }

        const tooltip = document.createElement('div');
        tooltip.className = 'hint-tooltip';
        tooltip.innerHTML = `
            <strong>Підказка ${Math.min(hintUsage[index], 3)}/3:</strong><br>
            "${hintText}"
        `;

        button.style.position = 'relative';
        button.appendChild(tooltip);

        setTimeout(() => {
            tooltip.remove();
            dropZone.classList.remove('hint-active');
        }, 4000);

        if (hintUsage[index] >= 3) {
            button.disabled = true;
            button.textContent = '💡 Використано';
        }
    };

    window.checkSentence = function(button) {
        const builder = button.closest('.sentence-builder');
        if (!builder) {
            return;
        }
        const dropZone = builder.querySelector('.drop-zone');
        const feedback = builder.querySelector('.sentence-feedback');
        if (!dropZone || !feedback) {
            return;
        }

        const index = resolveBuilderIndex(builder);
        if (!(index in sentenceStates)) {
            sentenceStates[index] = false;
        }

        const droppedWords = Array.from(dropZone.querySelectorAll('.draggable'))
            .map(item => (item.textContent || '').trim());
        const assembled = droppedWords.join(' ').trim();
        const correctAnswer = (dropZone.dataset.correct || '').trim();

        dropZone.classList.remove('incorrect', 'correct', 'hint-active');
        feedback.textContent = '';
        feedback.classList.remove('correct', 'incorrect');

        if (!correctAnswer) {
            return;
        }

        if (assembled === correctAnswer) {
            dropZone.classList.add('correct');
            feedback.textContent = getRandomBuilderMessage('correct');
            feedback.classList.add('correct');
            sentenceStates[index] = true;
            const hintBtn = builder.querySelector('.hint-btn');
            if (hintBtn) {
                hintBtn.disabled = true;
            }
            button.disabled = true;
            button.textContent = '✓ Виконано';
            dropZone.style.pointerEvents = 'none';
        } else {
            dropZone.classList.add('incorrect');
            feedback.textContent = getRandomBuilderMessage('incorrect');
            feedback.classList.add('incorrect');
            sentenceStates[index] = false;

            setTimeout(() => {
                dropZone.classList.remove('incorrect');
                if (!sentenceStates[index]) {
                    feedback.textContent = '';
                    feedback.classList.remove('incorrect');
                }
            }, 2000);
        }

        correctSentences = Object.values(sentenceStates).filter(Boolean).length;
        updateBuilderProgress();
    };

    function showCompletionMessage() {
        if (document.querySelector('.sentence-builder-complete')) {
            return;
        }
        const modal = document.createElement('div');
        modal.className = 'sentence-builder-complete';
        modal.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, #8b5cf6, #ec4899);
            color: white;
            padding: 30px;
            border-radius: 20px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            z-index: 10000;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            animation: bounceIn 0.5s;
        `;
        modal.innerHTML = `
            🎉 Вітаємо! 🎉<br>
            Ви успішно виконали всі завдання!<br>
            <button class="close-modal" style="
                margin-top: 20px;
                padding: 10px 20px;
                background: white;
                color: #8b5cf6;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
            ">Закрити</button>
        `;
        const closeButton = modal.querySelector('.close-modal');
        if (closeButton) {
            closeButton.addEventListener('click', () => {
                modal.remove();
            });
        }
        document.body.appendChild(modal);
    }

    document.addEventListener('DOMContentLoaded', function() {
        initializeSentenceBuilder();
    });

    function checkBuilder() {
        document.querySelectorAll('.sentence-builder .check-sentence-btn').forEach(button => {
            if (!button.disabled) {
                window.checkSentence(button);
            }
        });
    }
})();
"""


__all__ = ["ExercisesAssetsGenerator"]
