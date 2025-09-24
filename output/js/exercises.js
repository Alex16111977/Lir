
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
