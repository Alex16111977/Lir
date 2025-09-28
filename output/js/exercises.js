
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

        const words = correctAnswer.split(new RegExp('\s+'));
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
