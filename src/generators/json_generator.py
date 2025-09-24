"""
JSON Generator - генерація HTML з JSON даних з оригінальним дизайном
Включає упражнення та навігацію
"""

import json
import re
from pathlib import Path
from typing import Dict, List

from src.generators.exercises_assets import ExercisesAssetsGenerator
from src.generators.exercises_generator import ExercisesGenerator

def transliterate_filename(text):
    """Транслітерує кириличну назву для безпечного URL"""
    translit_table = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
        # Великі літери
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    
    result = []
    for char in text:
        if char in translit_table:
            result.append(translit_table[char])
        elif char.isalnum() or char in '._-':
            result.append(char)
        elif char == ' ':
            result.append('_')
        else:
            result.append('_')
    
    # Очищення
    filename = ''.join(result)
    filename = re.sub(r'_+', '_', filename)
    filename = filename.strip('_')
    
    return filename

class JSONGenerator:
    """Генератор HTML з JSON файлів"""
    
    def __init__(self, logger):
        self.logger = logger
        self.files_generated = 0
        self.words_processed = 0
        self.exercises_generator = ExercisesGenerator(logger)
    
    def _create_exercise_html(self, exercise_data):
        """
        Створює HTML для упражнення з повною підтримкою мобільних пристроїв
        """
        if not exercise_data:
            return ""
        
        title = exercise_data.get('title', 'Упражнение')
        text = exercise_data.get('text', '')
        answers = exercise_data.get('answers', {})
        
        # Преобразуємо текст з пропусками в HTML
        exercise_text = text
        
        # Обробляємо пропуски з урахуванням HTML тегів
        import re
        for hint, answer in answers.items():
            # Створюємо HTML blank елемент
            html_blank = f'<span class="blank" data-hint="{hint}" data-answer="{answer}">_______ ({hint})</span>'
            
            # Екрануємо спеціальні символи в hint для regex
            escaped_hint = re.escape(hint)
            
            # Замінюємо пропуски всередині <span class="story-highlight"> тегів
            # Шаблон: <span class="story-highlight">...DER ___ (смерть)...</span>
            pattern1 = rf'(<span class="story-highlight">[^<]*?)___ \({escaped_hint}\)([^<]*?</span>)'
            exercise_text = re.sub(pattern1, rf'\1{html_blank}\2', exercise_text)
            
            # Замінюємо прості пропуски поза тегами (якщо такі є)
            pattern2 = rf'(?<!>)___ \({escaped_hint}\)(?!<)'
            exercise_text = re.sub(pattern2, html_blank, exercise_text)
        
        # Преобразуємо answers в JSON для JavaScript
        answers_json = json.dumps(answers, ensure_ascii=False)
        
        html = f'''
        <!-- РОЗДІЛ 5: УПРАЖНЕННЯ -->
        <section class="section">
            <h2 class="section-title">
                <span class="section-number">5</span>
                <span>📝 {title}</span>
            </h2>
            
            <div class="exercise-container">
                <div class="exercise-section">
                    <div class="exercise-text">
                        {exercise_text}
                    </div>
                    
                    <button class="show-answer-btn" onclick="toggleAnswers(this)" type="button">
                        Показать ответы
                    </button>
                </div>
            </div>
        </section>
        
        <script>
            // Відповіді для вправи  
            const exerciseAnswers = {answers_json};
            
            function toggleAnswers(button) {{
                const blanks = document.querySelectorAll('.blank');
                const isShowing = button.textContent === 'Скрыть ответы';
                
                blanks.forEach(blank => {{
                    const hint = blank.dataset.hint;
                    const answer = exerciseAnswers[hint];
                    
                    if (isShowing) {{
                        blank.innerHTML = `_______ (${{hint}})`;
                        blank.classList.remove('filled');
                    }} else {{
                        if (answer) {{
                            blank.innerHTML = `<strong>${{answer}}</strong>`;
                            blank.classList.add('filled');
                        }}
                    }}
                }});
                
                button.textContent = isShowing ? 'Показать ответы' : 'Скрыть ответы';
                button.classList.toggle('success');
            }}
        </script>

        <!-- INTERACTIVE_EXERCISES_PLACEHOLDER -->

        <!-- НАВІГАЦІЯ ПІСЛЯ УПРАЖНЕННЯ -->
        <div class="bottom-navigation">
            <a href="../index.html" class="nav-btn">
                <span class="nav-icon">📚</span>
                <span>К урокам</span>
            </a>
            <a href="../../index.html" class="nav-btn nav-btn-home">
                <span class="nav-icon">🏠</span>
                <span>На главную</span>
            </a>
        </div>
        
        <style>
            /* Стилі для упражнення */
            .exercise-container {{
                margin-top: 30px;
            }}
            
            .exercise-section {{
                background: linear-gradient(135deg, #fff9e6 0%, #fff4d6 100%);
                border: 2px solid #f6ad55;
                padding: 30px;
                border-radius: 15px;
                position: relative;
            }}
            
            .exercise-text {{
                color: #4a5568;
                font-size: 1.15em;
                line-height: 1.9;
                text-align: justify;
                margin-bottom: 25px;
            }}
            
            .exercise-text .blank {{
                display: inline-block;
                min-width: 100px;
                border-bottom: 2px solid #f6ad55;
                margin: 0 4px;
                color: #a0aec0;
                font-style: italic;
                font-size: 0.9em;
                padding: 0 4px;
                transition: all 0.3s ease;
            }}
            
            .exercise-text .blank.filled {{
                color: #d97706;
                font-weight: 600;
                font-style: normal;
                border-bottom-color: #22c55e;
            }}
            
            .show-answer-btn {{
                background: linear-gradient(135deg, #f6ad55 0%, #ed8936 100%);
                color: white;
                border: none;
                padding: 18px 36px;
                border-radius: 12px;
                font-size: 1.15em;
                font-weight: 600;
                cursor: pointer;
                margin: 0 auto;
                display: block;
                transition: all 0.3s ease;
                box-shadow: 0 4px 12px rgba(237, 137, 54, 0.3);
                touch-action: manipulation;
                -webkit-tap-highlight-color: transparent;
                -webkit-user-select: none;
                user-select: none;
                min-height: 56px;
                min-width: 200px;
                -webkit-appearance: none;
                appearance: none;
            }}
            
            .show-answer-btn:hover {{
                transform: translateY(-2px);
                box-shadow: 0 6px 16px rgba(237, 137, 54, 0.4);
            }}
            
            .show-answer-btn:active {{
                transform: scale(0.98);
                box-shadow: 0 2px 8px rgba(237, 137, 54, 0.3);
            }}
            
            .show-answer-btn.success {{
                background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
            }}
            
            /* Навігація після упражнення */
            .bottom-navigation {{
                margin-top: 50px;
                padding: 30px 0;
                display: flex;
                justify-content: center;
                gap: 20px;
                border-top: 2px solid #e2e8f0;
            }}
            
            .nav-btn {{
                display: inline-flex;
                align-items: center;
                gap: 10px;
                padding: 15px 30px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                border-radius: 25px;
                font-size: 1.1em;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(118, 75, 162, 0.3);
                touch-action: manipulation;
                -webkit-tap-highlight-color: transparent;
                min-height: 56px;
            }}
            
            .nav-btn:hover {{
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(118, 75, 162, 0.4);
            }}
            
            .nav-btn:active {{
                transform: scale(0.98);
            }}
            
            .nav-btn-home {{
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
            }}
            
            .nav-btn-home:hover {{
                box-shadow: 0 6px 20px rgba(245, 87, 108, 0.4);
            }}
            
            .nav-icon {{
                font-size: 1.3em;
            }}
            
            /* Mobile optimizations */
            @media (max-width: 768px) {{
                .exercise-section {{
                    padding: 20px;
                }}
                
                .exercise-text {{
                    font-size: 1.05em;
                }}
                
                .exercise-text .blank {{
                    min-width: 80px;
                }}
                
                .show-answer-btn {{
                    width: 90%;
                    max-width: 300px;
                    padding: 16px 24px;
                    font-size: 1.1em;
                }}
                
                .bottom-navigation {{
                    flex-direction: column;
                    align-items: center;
                    gap: 15px;
                    padding: 20px;
                }}
                
                .nav-btn {{
                    width: 90%;
                    max-width: 300px;
                    justify-content: center;
                }}
            }}
            
            /* iOS specific */
            @supports (-webkit-touch-callout: none) {{
                .show-answer-btn,
                .nav-btn {{
                    -webkit-appearance: none;
                    appearance: none;
                }}
            }}
        </style>
        
        <script>
        // Device detection
        const isTouchDevice = ('ontouchstart' in window) || 
                              (navigator.maxTouchPoints > 0) || 
                              (navigator.msMaxTouchPoints > 0);
        
        // Exercise answers data
        const exerciseAnswers = {answers_json};
        
        // Function to toggle answers
        function toggleAnswers(button) {{
            // Prevent double tap
            if (button.dataset.processing === 'true') return;
            button.dataset.processing = 'true';
            
            const exerciseText = button.parentElement.querySelector('.exercise-text');
            const blanks = exerciseText.querySelectorAll('.blank');
            
            if (button.textContent === 'Показать ответы') {{
                // Show answers
                blanks.forEach(blank => {{
                    const hint = blank.getAttribute('data-hint');
                    const answer = exerciseAnswers[hint];
                    if (answer) {{
                        blank.innerHTML = answer + ' (' + hint + ')';
                        blank.classList.add('filled');
                    }}
                }});
                button.textContent = 'Скрыть ответы';
                button.classList.add('success');
            }} else {{
                // Hide answers
                blanks.forEach(blank => {{
                    const hint = blank.getAttribute('data-hint');
                    blank.innerHTML = '_______ (' + hint + ')';
                    blank.classList.remove('filled');
                }});
                button.textContent = 'Показать ответы';
                button.classList.remove('success');
            }}
            
            // Haptic feedback for mobile
            if (navigator.vibrate && isTouchDevice) {{
                navigator.vibrate(15);
            }}
            
            // Reset processing flag
            setTimeout(() => {{
                button.dataset.processing = 'false';
            }}, 300);
        }}
        
        // Initialize button handlers
        document.addEventListener('DOMContentLoaded', function() {{
            const answerBtn = document.querySelector('.show-answer-btn');
            
            if (answerBtn) {{
                // Visual feedback for mobile
                if (isTouchDevice) {{
                    answerBtn.addEventListener('touchstart', function() {{
                        this.style.transform = 'scale(0.98)';
                        this.style.opacity = '0.9';
                    }});
                    
                    answerBtn.addEventListener('touchend', function() {{
                        setTimeout(() => {{
                            this.style.transform = 'scale(1)';
                            this.style.opacity = '1';
                        }}, 100);
                    }});
                }}
            }}
            
            // Navigation buttons mobile support
            const navBtns = document.querySelectorAll('.nav-btn');
            navBtns.forEach(btn => {{
                if (isTouchDevice) {{
                    btn.addEventListener('touchstart', function() {{
                        this.style.transform = 'scale(0.98)';
                    }});
                    
                    btn.addEventListener('touchend', function() {{
                        this.style.transform = 'scale(1)';
                    }});
                }}
            }});
        }});
        
        // Prevent iOS double-tap zoom
        if (/iPad|iPhone|iPod/.test(navigator.userAgent)) {{
            let lastTouchEnd = 0;
            document.addEventListener('touchend', function(event) {{
                const now = Date.now();
                if (now - lastTouchEnd <= 300) {{
                    event.preventDefault();
                }}
                lastTouchEnd = now;
            }}, false);
        }}
        </script>
        '''
        
        return html
    
    def generate_from_json(self, data_dir, output_dir):
        """Генерувати HTML сайт з JSON даних"""
        
        try:
            # Завантажити всі JSON файли
            all_lessons = self._load_all_json(data_dir)
            
            if not all_lessons:
                self.logger.error("Немає JSON даних для генерації")
                return False
            
            # Створити структуру папок
            self._create_structure(output_dir)
            
            # Генерація HTML для кожного уроку
            for category, lessons in all_lessons.items():
                # Визначити групи для категорії
                groups = self._get_category_groups(category, lessons)
                
                for group_name, group_lessons in groups.items():
                    group_dir = output_dir / category / group_name
                    group_dir.mkdir(parents=True, exist_ok=True)
                    
                    for lesson in group_lessons:
                        html = self._generate_lesson_html(lesson, category)
                        # Використовуємо safe_id для імені файлу
                        safe_filename = lesson.get('safe_id', transliterate_filename(lesson.get('id', 'lesson')))
                        filename = safe_filename + '.html'
                        output_file = group_dir / filename
                        
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(html)
                        
                        self.files_generated += 1
                        
                        # Підрахунок слів
                        vocab = lesson.get('vocabulary', [])
                        self.words_processed += len([w for w in vocab if w.get('german')])
                
                # Індекс категорії
                cat_index = self._generate_category_index(lessons, category, groups)
                with open(output_dir / category / "index.html", 'w', encoding='utf-8') as f:
                    f.write(cat_index)
                self.files_generated += 1
            
            # Головна сторінка з оригінальним дизайном
            main_index = self._generate_main_index(all_lessons)
            with open(output_dir / "index.html", 'w', encoding='utf-8') as f:
                f.write(main_index)
            self.files_generated += 1
            
            # Створити CSS файли
            self._create_css_files(output_dir)
            
            self.logger.success(f"Згенеровано {self.files_generated} HTML файлів з {self.words_processed} словами")
            return True
            
        except Exception as e:
            self.logger.error(f"Помилка генерації з JSON: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            return False
    
    def _load_all_json(self, data_dir):
        """Завантажити всі JSON файли"""
        
        all_lessons = {}
        categories = ['a2', 'b1', 'thematic']
        
        for category in categories:
            cat_dir = data_dir / category
            if not cat_dir.exists():
                continue
            
            lessons = []
            for json_file in sorted(cat_dir.glob("*.json")):
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        lesson = json.load(f)
                        # Додати ID з імені файлу якщо немає
                        if 'id' not in lesson:
                            lesson['id'] = json_file.stem
                        # Додаємо safe_id одразу при завантаженні
                        lesson['safe_id'] = transliterate_filename(lesson['id'])
                        lessons.append(lesson)
                except Exception as e:
                    self.logger.error(f"Помилка читання {json_file}: {e}")
            
            if lessons:
                all_lessons[category] = lessons
                self.logger.info(f"Завантажено {len(lessons)} уроків з {category}")
        
        return all_lessons
    
    def _get_category_groups(self, category, lessons):
        """Визначити групи для категорії"""
        
        groups = {}
        
        if category == 'a2':
            # Розподілити уроки по групах A2
            groups = {
                'gruppe_1_familie': [],
                'gruppe_2_emotionen': [],
                'gruppe_3_handlungen': [],
                'gruppe_4_orte': [],
                'gruppe_5_zeit': []
            }
            
            # Розподілити уроки по групах (по 3 в кожній)
            for i, lesson in enumerate(lessons):
                if i < 3:
                    groups['gruppe_1_familie'].append(lesson)
                elif i < 6:
                    groups['gruppe_2_emotionen'].append(lesson)
                elif i < 9:
                    groups['gruppe_3_handlungen'].append(lesson)
                elif i < 12:
                    groups['gruppe_4_orte'].append(lesson)
                else:
                    groups['gruppe_5_zeit'].append(lesson)
                    
        elif category == 'b1':
            # Розподілити уроки по групах B1
            groups = {
                'gruppe_1_hof': [],
                'gruppe_2_verrat': [],
                'gruppe_3_wahnsinn': [],
                'gruppe_4_erkenntnis': [],
                'gruppe_5_finale': []
            }
            
            for i, lesson in enumerate(lessons):
                if i < 3:
                    groups['gruppe_1_hof'].append(lesson)
                elif i < 6:
                    groups['gruppe_2_verrat'].append(lesson)
                elif i < 9:
                    groups['gruppe_3_wahnsinn'].append(lesson)
                elif i < 12:
                    groups['gruppe_4_erkenntnis'].append(lesson)
                else:
                    groups['gruppe_5_finale'].append(lesson)
                    
        elif category == 'thematic':
            # Всі тематичні в одній папці
            groups = {'lessons': lessons}
        
        return groups
    
    def _create_structure(self, output_dir):
        """Створити структуру папок"""
        
        dirs = [
            output_dir / "css",
            output_dir / "js",
            output_dir / "a2",
            output_dir / "b1",
            output_dir / "thematic"
        ]
        
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
    
    def _generate_lesson_html(self, lesson, category):
        """Генерація HTML для уроку з УСІМА розділами включаючи упражнення"""
        
        from src.generators.original_styles import LESSON_STYLES
        
        # Дані з JSON
        title = lesson.get('title', 'Урок')
        icon = lesson.get('icon', '📚')
        quote = lesson.get('quote', '')
        emotions = lesson.get('emotions', [])
        vocabulary = lesson.get('vocabulary', [])
        story = lesson.get('story', {})
        dialogues = lesson.get('dialogues', [])
        memory_trick = lesson.get('memory_trick', {})
        cheat_sheet = lesson.get('cheat_sheet', [])
        exercise = lesson.get('exercise', None)
        
        html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{title}</title>
    <link rel="stylesheet" href="../../css/exercises.css"/>
    <style>
        {LESSON_STYLES}
        
        /* Додаткові стилі для нових розділів */
        .story-container {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            border-left: 5px solid #764ba2;
        }}
        
        .story-highlight {{
            background: #ffeaa7;
            padding: 2px 5px;
            border-radius: 3px;
            font-weight: bold;
        }}
        
        .emotional-peak {{
            background: #ff6b6b;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            font-weight: bold;
        }}
        
        .dialogue-practice {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }}
        
        .dialogue-line {{
            margin-bottom: 25px;
            padding: 15px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        .dialogue-line strong {{
            color: #764ba2;
            font-size: 1.1em;
        }}
        
        .dialogue-line .german {{
            font-size: 1.2em;
            color: #2c3e50;
            margin: 10px 0;
        }}
        
        .dialogue-line .russian {{
            color: #7f8c8d;
            font-style: italic;
        }}
        
        .dialogue-line .emotion {{
            margin-top: 10px;
            color: #e74c3c;
        }}
        
        .cheat-sheet-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        
        .cheat-sheet-table th {{
            background: #764ba2;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        
        .cheat-sheet-table td {{
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }}
        
        .memory-trick {{
            background: #fff3cd;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border: 2px solid #ffc107;
        }}
        
        .story-title {{
            color: #764ba2;
            font-size: 1.5em;
            margin-bottom: 15px;
        }}
        
        /* Стилі для кнопки копіювання */
        .copy-button {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 25px;
            font-size: 1.1em;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: all 0.3s;
            z-index: 1000;
            font-family: 'Georgia', serif;
            -webkit-tap-highlight-color: transparent;
            -webkit-touch-callout: none;
            touch-action: manipulation;
        }}
        
        .copy-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 7px 20px rgba(0,0,0,0.4);
        }}
        
        .copy-button:active {{
            transform: scale(0.95);
        }}
        
        .copy-button.success {{
            background: linear-gradient(135deg, #00b894, #00cec9);
        }}
        
        /* Адаптація для мобільних */
        @media (max-width: 768px) {{
            .copy-button {{
                top: 10px;
                right: 10px;
                padding: 12px 20px;
                font-size: 1em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Навігація -->
        <div class="navigation">
            <a href="../index.html">← К урокам {category.upper()}</a>
            <a href="../../index.html">🏠 На главную</a>
        </div>
        
        <!-- Кнопка копіювання -->
        <button id="copyLessonBtn" class="copy-button" onclick="copyLesson()">
            📋 Копировать урок
        </button>
        
        <!-- SCENE MOMENT -->
        <div class="scene-moment">
            <h1>{icon} {title}</h1>
            <p class="shakespeare-quote">"{quote}"</p>
            <div class="emotion-tags">'''
        
        for emotion in emotions:
            html += f'''
                <span class="emotion-tag">{emotion}</span>'''
        
        html += '''
            </div>
        </div>
        
        <!-- РОЗДІЛ 1: СЛОВА -->
        <section class="section">
            <h2 class="section-title">
                <span class="section-number">1</span>
                <span>📚 Слова момента</span>
            </h2>
            <div class="word-cards">'''
        
        # Генерація карточок слів
        for word in vocabulary:
            if not word.get('german'):
                continue
                
            html += f'''
                <div class="word-card">
                    <div class="word-german">{word.get('german', '')}</div>
                    <div class="word-transcription">{word.get('transcription', '')}</div>
                    <div class="word-russian">{word.get('translation', '')}</div>'''
            
            if word.get('type'):
                html += f'''
                    <div class="word-type">{word['type']}</div>'''
            
            # Character voice
            voice = word.get('character_voice', {})
            if voice and voice.get('character'):
                html += f'''
                    <div class="character-voice">
                        <strong>{voice['character']}:</strong><br/>
                        "{voice.get('german', '')}"<br/>
                        ({voice.get('russian', '')})
                    </div>'''
            
            # Gesture
            gesture = word.get('gesture', {})
            if gesture and gesture.get('gesture'):
                html += f'''
                    <div class="gesture-anchor">
                        <span class="gesture-icon">{gesture.get('icon', '🎭')}</span>
                        <div>
                            <strong>Жест-якорь:</strong> {gesture['gesture']}<br/>
                            <strong>Эмоция:</strong> {gesture.get('emotion', '')}<br/>
                            <strong>Ассоциация:</strong> {gesture.get('association', '')}
                        </div>
                    </div>'''
            
            html += '''
                </div>'''
        
        html += '''
            </div>
        </section>
        
        <!-- РОЗДІЛ 2: ТЕАТРАЛЬНИЙ МОМЕНТ -->
        <section class="section">
            <h2 class="section-title">
                <span class="section-number">2</span>
                <span>🎭 Театральный момент</span>
            </h2>
            <div class="story-container">
                <h3 class="story-title">''' + story.get('title', 'ТЕАТРАЛЬНЫЙ МОМЕНТ') + '''</h3>
                <div class="story-text">''' + story.get('content', '') + '''
                </div>'''
        
        if story.get('emotional_peak'):
            html += f'''
                <div class="emotional-peak">
                    {story.get('emotional_peak', '')}
                </div>'''
        
        html += '''
            </div>
        </section>
        
        <!-- РОЗДІЛ 3: ДІАЛОГИ -->
        <section class="section">
            <h2 class="section-title">
                <span class="section-number">3</span>
                <span>💬 Живые диалоги сцены</span>
            </h2>
            <div class="dialogue-practice">'''
        
        # Генерація діалогів
        for dialogue in dialogues:
            html += f'''
                <div class="dialogue-line">
                    <strong>{dialogue.get('character', '')}:</strong>
                    <p class="german">{dialogue.get('german', '')}</p>
                    <p class="russian">({dialogue.get('russian', '')})</p>
                    <p class="emotion">{dialogue.get('emotion', '')}</p>
                </div>'''
        
        html += '''
            </div>
        </section>
        
        <!-- РОЗДІЛ 4: ШПАРГАЛКА -->
        <section class="section">
            <h2 class="section-title">
                <span class="section-number">4</span>
                <span>📌 Эмоциональная шпаргалка</span>
            </h2>
            <div class="cheat-sheet">'''
        
        # Таблиця якщо є дані
        if cheat_sheet:
            html += '''
                <h3>ЯКОРЯ ПАМЯТИ</h3>
                <table class="cheat-sheet-table">
                    <thead>
                        <tr>
                            <th>Немецкий</th>
                            <th>Русский</th>
                            <th>Эмоция момента</th>
                            <th>Жест-якорь</th>
                            <th>Персонаж</th>
                        </tr>
                    </thead>
                    <tbody>'''
            
            for item in cheat_sheet:
                html += f'''
                        <tr>
                            <td><strong>{item.get('german', '')}</strong></td>
                            <td>{item.get('russian', '')}</td>
                            <td>{item.get('emotion_moment', '')}</td>
                            <td>{item.get('gesture_anchor', '')}</td>
                            <td>{item.get('character_moment', '')}</td>
                        </tr>'''
            
            html += '''
                    </tbody>
                </table>'''
        
        # Memory trick
        if memory_trick:
            if isinstance(memory_trick, dict):
                master = memory_trick.get('master_trick', '')
                chain = memory_trick.get('emotion_chain', '')
                ritual = memory_trick.get('ritual', '')
            else:
                master = memory_trick
                chain = ''
                ritual = ''
            
            html += f'''
                <div class="memory-trick">
                    💡 <strong>Мастер-трюк запоминания:</strong><br/>
                    {master}<br/><br/>'''
            
            if chain:
                html += f'''
                    <strong>Цепочка эмоций:</strong> {chain}<br/><br/>'''
            
            if ritual:
                html += f'''
                    <strong>Ритуал:</strong> {ritual}'''
            
            html += '''
                </div>'''
        
        html += '''
            </div>
        </section>'''

        exercises_html = ""
        try:
            exercise_bundle = self.exercises_generator.generate_all_exercises(lesson)
            exercises_html = self.exercises_generator.create_exercises_section(exercise_bundle)
        except Exception as exc:
            if self.logger:
                self.logger.warning(f"[Exercises] Помилка генерації інтерактивних вправ: {exc}")

        # Додаємо упражнення якщо є
        if exercise:
            exercise_html = self._create_exercise_html(exercise)
            if exercises_html:
                exercise_html = exercise_html.replace(
                    "<!-- INTERACTIVE_EXERCISES_PLACEHOLDER -->",
                    exercises_html,
                )
            html += exercise_html
        elif exercises_html:
            html += exercises_html
        
        html += '''
    </div>

    <script src="../../js/exercises.js" defer></script>

    <!-- JavaScript для копіювання уроку -->
    <script>
    function copyLesson() {
        // Збір всіх даних уроку
        let lessonContent = '';
        
        // Заголовок
        const titleElement = document.querySelector('.scene-moment h1');
        if (titleElement) {
            lessonContent += '=== ' + titleElement.textContent + ' ===\\n\\n';
        }
        
        // Цитата
        const quoteElement = document.querySelector('.shakespeare-quote');
        if (quoteElement) {
            lessonContent += 'Цитата: ' + quoteElement.textContent + '\\n\\n';
        }
        
        // Емоції
        const emotionTags = document.querySelectorAll('.emotion-tag');
        if (emotionTags.length > 0) {
            lessonContent += 'Эмоции: ';
            emotionTags.forEach((tag, index) => {
                lessonContent += tag.textContent;
                if (index < emotionTags.length - 1) lessonContent += ', ';
            });
            lessonContent += '\\n\\n';
        }
        
        // Слова
        lessonContent += '=== СЛОВА МОМЕНТА ===\\n\\n';
        const wordCards = document.querySelectorAll('.word-card');
        wordCards.forEach(card => {
            const german = card.querySelector('.word-german');
            const transcription = card.querySelector('.word-transcription');
            const russian = card.querySelector('.word-russian');
            const type = card.querySelector('.word-type');
            
            if (german) {
                lessonContent += german.textContent;
                if (transcription && transcription.textContent) {
                    lessonContent += ' ' + transcription.textContent;
                }
                if (russian) {
                    lessonContent += ' - ' + russian.textContent;
                }
                if (type && type.textContent) {
                    lessonContent += ' (' + type.textContent + ')';
                }
                lessonContent += '\\n';
                
                // Додаткова інформація
                const characterVoice = card.querySelector('.character-voice');
                if (characterVoice) {
                    lessonContent += '  ' + characterVoice.textContent.replace(/\\n/g, ' ').trim() + '\\n';
                }
                
                const gesture = card.querySelector('.gesture-anchor');
                if (gesture) {
                    lessonContent += '  ' + gesture.textContent.replace(/\\n/g, ' ').trim() + '\\n';
                }
                
                lessonContent += '\\n';
            }
        });
        
        // Театральний момент
        const storyTitle = document.querySelector('.story-title');
        const storyText = document.querySelector('.story-text');
        if (storyTitle || storyText) {
            lessonContent += '\\n=== ТЕАТРАЛЬНЫЙ МОМЕНТ ===\\n\\n';
            if (storyTitle) {
                lessonContent += storyTitle.textContent + '\\n\\n';
            }
            if (storyText) {
                lessonContent += storyText.textContent.trim() + '\\n';
            }
            
            const emotionalPeak = document.querySelector('.emotional-peak');
            if (emotionalPeak) {
                lessonContent += '\\nЭмоциональный пик: ' + emotionalPeak.textContent.trim() + '\\n';
            }
        }
        
        // Діалоги
        const dialogues = document.querySelectorAll('.dialogue-line');
        if (dialogues.length > 0) {
            lessonContent += '\\n=== ЖИВЫЕ ДИАЛОГИ ===\\n\\n';
            dialogues.forEach(dialogue => {
                const character = dialogue.querySelector('strong');
                const germanText = dialogue.querySelector('.german');
                const russianText = dialogue.querySelector('.russian');
                const emotionText = dialogue.querySelector('.emotion');
                
                if (character) {
                    lessonContent += character.textContent + '\\n';
                }
                if (germanText) {
                    lessonContent += germanText.textContent + '\\n';
                }
                if (russianText) {
                    lessonContent += russianText.textContent + '\\n';
                }
                if (emotionText) {
                    lessonContent += emotionText.textContent + '\\n';
                }
                lessonContent += '\\n';
            });
        }
        
        // Шпаргалка
        const cheatSheetTable = document.querySelector('.cheat-sheet-table');
        if (cheatSheetTable) {
            lessonContent += '\\n=== ЭМОЦИОНАЛЬНАЯ ШПАРГАЛКА ===\\n\\n';
            const rows = cheatSheetTable.querySelectorAll('tbody tr');
            rows.forEach(row => {
                const cells = row.querySelectorAll('td');
                if (cells.length >= 5) {
                    lessonContent += cells[0].textContent + ' - ' + cells[1].textContent;
                    lessonContent += ' | Эмоция: ' + cells[2].textContent;
                    lessonContent += ' | Жест: ' + cells[3].textContent;
                    lessonContent += ' | Персонаж: ' + cells[4].textContent + '\\n';
                }
            });
        }
        
        // Memory trick
        const memoryTrick = document.querySelector('.memory-trick');
        if (memoryTrick) {
            lessonContent += '\\n' + memoryTrick.textContent.trim() + '\\n';
        }
        
        // Функція копіювання з підтримкою iOS
        function copyToClipboard(text) {
            const btn = document.getElementById('copyLessonBtn');
            const originalText = btn.textContent;
            
            // Спробуємо сучасний метод
            if (navigator.clipboard && window.isSecureContext) {
                navigator.clipboard.writeText(text).then(() => {
                    showSuccess();
                }).catch(() => {
                    fallbackCopy();
                });
            } else {
                // Fallback для iOS та старих браузерів
                fallbackCopy();
            }
            
            function fallbackCopy() {
                // Створюємо textarea
                const textarea = document.createElement('textarea');
                textarea.value = text;
                textarea.style.position = 'fixed';
                textarea.style.top = '0';
                textarea.style.left = '0';
                textarea.style.width = '2em';
                textarea.style.height = '2em';
                textarea.style.padding = '0';
                textarea.style.border = 'none';
                textarea.style.outline = 'none';
                textarea.style.boxShadow = 'none';
                textarea.style.background = 'transparent';
                textarea.style.fontSize = '16px'; // Запобігає zoom на iOS
                
                document.body.appendChild(textarea);
                
                // Для iOS потрібен особливий підхід
                if (navigator.userAgent.match(/ipad|iphone/i)) {
                    const range = document.createRange();
                    range.selectNodeContents(textarea);
                    const selection = window.getSelection();
                    selection.removeAllRanges();
                    selection.addRange(range);
                    textarea.setSelectionRange(0, 999999);
                } else {
                    textarea.select();
                }
                
                try {
                    const successful = document.execCommand('copy');
                    if (successful) {
                        showSuccess();
                    } else {
                        showManualCopy();
                    }
                } catch (err) {
                    showManualCopy();
                }
                
                document.body.removeChild(textarea);
            }
            
            function showSuccess() {
                btn.textContent = '✅ Скопировано!';
                btn.classList.add('success');
                setTimeout(() => {
                    btn.textContent = originalText;
                    btn.classList.remove('success');
                }, 2000);
            }
            
            function showManualCopy() {
                // Показуємо текст для ручного копіювання
                const modal = document.createElement('div');
                modal.style.cssText = `
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
                    z-index: 10000;
                    max-width: 90%;
                    max-height: 80vh;
                `;
                
                modal.innerHTML = `
                    <h3 style="margin-top: 0;">Выделите и скопируйте текст:</h3>
                    <textarea readonly style="
                        width: 100%;
                        min-width: 300px;
                        height: 300px;
                        padding: 10px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        font-size: 14px;
                        resize: vertical;
                    ">${text.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</textarea>
                    <button onclick="this.parentElement.remove()" style="
                        margin-top: 10px;
                        padding: 10px 20px;
                        background: #764ba2;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                    ">Закрыть</button>
                `;
                
                document.body.appendChild(modal);
                
                // Автоматично виділяємо текст
                const textarea = modal.querySelector('textarea');
                textarea.select();
                textarea.setSelectionRange(0, 999999);
            }
        }
        
        copyToClipboard(lessonContent);
    }
    </script>
</body>
</html>'''
        
        return html
    
    def _generate_category_index(self, lessons, category, groups):
        """Генерація індексної сторінки категорії"""
        
        from src.generators.original_styles import NAVIGATION_STYLES
        
        cat_names = {
            'a2': 'Базовый курс A2',
            'b1': 'Продвинутый курс B1',
            'thematic': 'Тематические уроки'
        }
        
        group_names = {
            'gruppe_1_familie': 'Группа 1: Семейные отношения',
            'gruppe_2_emotionen': 'Группа 2: Эмоции героев',
            'gruppe_3_handlungen': 'Группа 3: Действия и поступки',
            'gruppe_4_orte': 'Группа 4: Места событий',
            'gruppe_5_zeit': 'Группа 5: Время в пьесе',
            'gruppe_1_hof': 'Группа 1: Королевский двор',
            'gruppe_2_verrat': 'Группа 2: Предательство',
            'gruppe_3_wahnsinn': 'Группа 3: Безумие и буря',
            'gruppe_4_erkenntnis': 'Группа 4: Прозрение героев',
            'gruppe_5_finale': 'Группа 5: Трагический финал',
            'lessons': 'Все уроки'
        }
        
        html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cat_names.get(category, category.upper())}</title>
    <style>
        {NAVIGATION_STYLES}
    </style>
</head>
<body>
    <div class="container">
        <div class="navigation">
            <a href="../index.html">← На главную</a>
        </div>
        
        <header class="header">
            <h1>{cat_names.get(category, category.upper())}</h1>
            <p>{len(lessons)} уроков в курсе</p>
        </header>
        
        <div class="groups">'''
        
        for group_name, group_lessons in groups.items():
            if not group_lessons:
                continue
                
            html += f'''
            <div class="group">
                <div class="group-header">
                    <h2>{group_names.get(group_name, group_name)}</h2>
                </div>
                <div class="group-lessons">'''
            
            for i, lesson in enumerate(group_lessons, 1):
                safe_id = lesson.get('safe_id', transliterate_filename(lesson.get('id', 'lesson')))
                html += f'''
                    <a href="{group_name}/{safe_id}.html" class="lesson-card">
                        <div class="lesson-number">Урок {i}</div>
                        <div class="lesson-title">{lesson.get('icon', '📚')} {lesson.get('title', lesson['id'])}</div>
                    </a>'''
            
            html += '''
                </div>
            </div>'''
        
        html += '''
        </div>
    </div>
</body>
</html>'''
        
        return html
    
    def _generate_main_index(self, all_lessons):
        """Генерація головної сторінки"""
        
        from src.generators.original_styles import MAIN_PAGE_STYLES
        
        html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Немецкий через Короля Лира - Интерактивный курс</title>
    <link href="css/style.css" rel="stylesheet"/>
</head>
<body>
    <header class="header">
        <h1>🎭 Немецкий через Короля Лира</h1>
        <p>Интерактивный курс с театральными ассоциациями</p>
    </header>
    
    <main class="container">
        <div class="levels">
            <div class="level-card level-a2">
                <div class="level-header">
                    <h2>Базовый курс</h2>
                    <span class="level-badge">Уровень A2</span>
                </div>
                <div class="level-content">
                    <h3>📚 15 сцен для начинающих</h3>
                    <p>Базовая лексика через эмоциональные сцены из "Короля Лира"</p>
                    <ul>
                        <li>✓ 3 сцены: Семейные отношения</li>
                        <li>✓ 3 сцены: Эмоции героев</li>
                        <li>✓ 3 сцены: Действия и поступки</li>
                        <li>✓ 3 сцены: Места событий</li>
                        <li>✓ 3 сцены: Время в пьесе</li>
                    </ul>
                    <a class="level-button" href="a2/index.html">Начать изучение A2 →</a>
                </div>
            </div>
            
            <div class="level-card level-b1">
                <div class="level-header">
                    <h2>Продвинутый курс</h2>
                    <span class="level-badge">Уровень B1</span>
                </div>
                <div class="level-content">
                    <h3>🎬 15 сцен трагедии</h3>
                    <p>Сложная лексика в контексте драматических моментов</p>
                    <ul>
                        <li>✓ 3 сцены: Королевский двор</li>
                        <li>✓ 3 сцены: Предательство</li>
                        <li>✓ 3 сцены: Безумие и буря</li>
                        <li>✓ 3 сцены: Прозрение героев</li>
                        <li>✓ 3 сцены: Трагический финал</li>
                    </ul>
                    <a class="level-button" href="b1/index.html">Начать изучение B1 →</a>
                </div>
            </div>
        </div>
        
        <!-- Рожевий блок тематичних курсів -->
        <div style="margin-top: 40px;">
            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                        border-radius: 20px; padding: 30px; text-align: center; 
                        box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                <h2 style="color: white; margin-bottom: 15px; font-size: 2em;">
                    📚 Тематические курсы
                </h2>
                <p style="color: white; margin-bottom: 20px; font-size: 1.1em;">
                    21 специализированный урок по существительным и глаголам
                </p>
                <a href="thematic/index.html" style="display: inline-block; 
                   padding: 15px 40px; background: white; color: #f5576c; 
                   text-decoration: none; border-radius: 25px; font-weight: bold; 
                   font-size: 1.2em; box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                   transition: transform 0.3s;">
                   Перейти к тематическим курсам →
                </a>
            </div>
        </div>
        
        <!-- Блок с книгою König Lear -->
        <div style="margin-top: 40px;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        border-radius: 20px; padding: 30px; text-align: center; 
                        box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                <h2 style="color: white; margin-bottom: 15px; font-size: 2em;">
                    📖 König Lear - Оригинал
                </h2>
                <p style="color: white; margin-bottom: 20px; font-size: 1.1em;">
                    Читайте оригинальный текст трагедии на немецком языке
                </p>
                <a href="book/index.html" style="display: inline-block; 
                   padding: 15px 40px; background: white; color: #764ba2; 
                   text-decoration: none; border-radius: 25px; font-weight: bold; 
                   font-size: 1.2em; box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                   transition: transform 0.3s;"
                   onmouseover="this.style.transform='translateY(-3px)'"
                   onmouseout="this.style.transform='translateY(0)'">
                   📖 Читать König Lear →
                </a>
            </div>
        </div>
    </main>
</body>
</html>'''
        
        return html
    
    def _create_css_files(self, output_dir):
        """Створити CSS файли"""

        from src.generators.original_styles import MAIN_PAGE_STYLES

        css_dir = output_dir / "css"
        css_dir.mkdir(parents=True, exist_ok=True)

        # Створити style.css для головної сторінки
        with open(css_dir / "style.css", 'w', encoding='utf-8') as f:
            f.write(MAIN_PAGE_STYLES)

        assets_generator = ExercisesAssetsGenerator()

        with open(css_dir / "exercises.css", 'w', encoding='utf-8') as f:
            f.write(assets_generator.generate_css())

        js_dir = output_dir / "js"
        js_dir.mkdir(parents=True, exist_ok=True)

        with open(js_dir / "exercises.js", 'w', encoding='utf-8') as f:
            f.write(assets_generator.generate_js())

        self.logger.info("CSS та JS файли для вправ створено")
    
    def get_statistics(self):
        """Отримати статистику"""
        
        return {
            'files_generated': self.files_generated,
            'words_processed': self.words_processed
        }
