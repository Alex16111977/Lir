
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

    // 4. Interactive Quiz with instant feedback
    let currentQuestion = 0;
    let correctAnswers = 0;
    let totalQuestions = 10;
    let answeredQuestions = [];

    // Initialize quiz
    window.checkQuizAnswer = function(button, isCorrect) {
        // Prevent double clicking
        if (button.classList.contains('disabled')) return;
        
        // Disable all buttons in current question
        const allButtons = button.parentElement.querySelectorAll('.answer-btn');
        allButtons.forEach(btn => {
            btn.classList.add('disabled');
            // Show correct answer
            if (btn.dataset.correct === 'true') {
                btn.classList.add('show-correct');
            }
        });
        
        // Highlight selected button
        if (isCorrect) {
            button.classList.add('correct');
            correctAnswers++;
        } else {
            button.classList.add('incorrect');
        }
        
        // Save answer
        answeredQuestions.push({
            question: currentQuestion,
            correct: isCorrect
        });
        
        // Update progress
        updateQuizProgress();
        
        // Auto-advance after 1.5 seconds
        setTimeout(() => {
            if (currentQuestion < totalQuestions - 1) {
                currentQuestion++;
                showNextQuestion();
            } else {
                showQuizResults();
            }
        }, 1500);
    };

    function showNextQuestion() {
        const questions = document.querySelectorAll('.quiz-question');
        questions.forEach((q, i) => {
            q.style.display = i === currentQuestion ? 'block' : 'none';
        });
    }

    function updateQuizProgress() {
        const progressFill = document.querySelector('#word-quiz .progress-fill');
        const correctCount = document.getElementById('correct-count');
        const percentage = (answeredQuestions.length / totalQuestions) * 100;
        
        if (progressFill) {
            progressFill.style.width = percentage + '%';
        }
        if (correctCount) {
            correctCount.textContent = correctAnswers;
        }
    }

    function showQuizResults() {
        const questionsDiv = document.getElementById('quiz-questions');
        const resultDiv = document.getElementById('quiz-result');
        const resultText = document.querySelector('.result-text');
        
        if (questionsDiv) questionsDiv.style.display = 'none';
        if (resultDiv) resultDiv.style.display = 'block';
        
        const percentage = Math.round((correctAnswers / totalQuestions) * 100);
        let message = '';
        
        if (percentage >= 80) {
            message = `Чудово! Ви відповіли правильно на ${correctAnswers} з ${totalQuestions} питань (${percentage}%) 🎉`;
        } else if (percentage >= 60) {
            message = `Добре! Ви відповіли правильно на ${correctAnswers} з ${totalQuestions} питань (${percentage}%) 👍`;
        } else {
            message = `Спробуйте ще раз! Ви відповіли правильно на ${correctAnswers} з ${totalQuestions} питань (${percentage}%) 💪`;
        }
        
        if (resultText) {
            resultText.textContent = message;
        }
    }

    window.restartQuiz = function() {
        currentQuestion = 0;
        correctAnswers = 0;
        answeredQuestions = [];
        
        // Clear button states
        document.querySelectorAll('.answer-btn').forEach(btn => {
            btn.classList.remove('correct', 'incorrect', 'disabled', 'show-correct');
        });
        
        // Reset progress
        const progressFill = document.querySelector('#word-quiz .progress-fill');
        if (progressFill) progressFill.style.width = '0%';
        
        const correctCount = document.getElementById('correct-count');
        if (correctCount) correctCount.textContent = '0';
        
        // Show first question
        document.getElementById('quiz-result').style.display = 'none';
        document.getElementById('quiz-questions').style.display = 'block';
        showNextQuestion();
    };

    // Initialize quiz on page load
    document.addEventListener('DOMContentLoaded', function() {
        const quizContainer = document.getElementById('word-quiz');
        if (quizContainer) {
            const questions = document.querySelectorAll('.quiz-question');
            totalQuestions = questions.length || 10;
            const totalCount = document.getElementById('total-count');
            if (totalCount) totalCount.textContent = totalQuestions;
        }
    });

    // Old checkQuiz for compatibility
    function checkQuiz() {
        // Compatibility stub
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
