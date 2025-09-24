
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
