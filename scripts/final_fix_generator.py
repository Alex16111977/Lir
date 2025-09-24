"""
ФИНАЛЬНЫЙ ФИКС: добавление упражнений и навигации в json_generator.py
"""
import re
from pathlib import Path

def fix_json_generator():
    """Добавляет упражнения и навигацию в генератор"""
    
    file_path = Path(r'F:\AiKlientBank\Lir\src\generators\json_generator.py')
    
    # Читаем файл
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("[START] Фиксим json_generator.py...")
    
    # Проверяем есть ли уже обработка упражнений
    if "data.get('exercise')" in content and "bottom-navigation" in content:
        print("[OK] Упражнения и навигация уже добавлены!")
        return True
    
    # Код для вставки перед </body> в методе generate
    insert_before_body = '''
        # Добавляем упражнение если есть в JSON
        if 'exercise' in data:
            exercise = data['exercise']
            title = exercise.get('title', 'Упражнение')
            text = exercise.get('text', '')
            answers = exercise.get('answers', {})
            
            # Преобразуем текст с пропусками
            exercise_text = text
            for hint, answer in answers.items():
                placeholder = f'___ ({hint})'
                html_blank = f'<span class="blank" data-hint="{hint}" data-answer="{answer}">_______ ({hint})</span>'
                exercise_text = exercise_text.replace(placeholder, html_blank)
            
            html += f"""
        <!-- УПРАЖНЕНИЕ -->
        <section class="section" style="margin-top: 40px;">
            <h2 class="section-title" style="
                font-size: 1.8em;
                color: #1a202c;
                margin-bottom: 30px;
                display: flex;
                align-items: center;
                gap: 15px;
            ">
                <span style="
                    background: linear-gradient(135deg, #f6ad55 0%, #ed8936 100%);
                    color: white;
                    width: 45px;
                    height: 45px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: bold;
                ">5</span>
                <span>📝 {title}</span>
            </h2>
            
            <div class="exercise-container" style="
                background: linear-gradient(135deg, #fff9e6 0%, #fff4d6 100%);
                border: 2px solid #f6ad55;
                padding: 30px;
                border-radius: 15px;
            ">
                <div class="exercise-text" style="
                    color: #4a5568;
                    font-size: 1.15em;
                    line-height: 1.9;
                    margin-bottom: 25px;
                ">
                    {exercise_text}
                </div>
                
                <button onclick="toggleAnswers(this)" style="
                    background: linear-gradient(135deg, #f6ad55 0%, #ed8936 100%);
                    color: white;
                    border: none;
                    padding: 15px 30px;
                    border-radius: 10px;
                    font-size: 1.1em;
                    font-weight: 600;
                    cursor: pointer;
                    display: block;
                    margin: 0 auto;
                    transition: all 0.3s ease;
                ">
                    Показать ответы
                </button>
            </div>
        </section>
        """
        
        # Навигационные кнопки ВСЕГДА
        html += """
        <!-- НАВИГАЦИЯ ВНИЗУ СТРАНИЦЫ -->
        <div class="bottom-navigation" style="
            margin-top: 50px;
            padding: 30px 0;
            display: flex;
            justify-content: center;
            gap: 20px;
            border-top: 2px solid #e2e8f0;
            background: white;
        ">
            <a href="../index.html" style="
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
                box-shadow: 0 4px 15px rgba(118, 75, 162, 0.3);
            ">
                <span style="font-size: 1.3em;">📚</span>
                <span>К урокам</span>
            </a>
            <a href="../../index.html" style="
                display: inline-flex;
                align-items: center;
                gap: 10px;
                padding: 15px 30px;
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                text-decoration: none;
                border-radius: 25px;
                font-size: 1.1em;
                font-weight: 600;
                box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
            ">
                <span style="font-size: 1.3em;">🏠</span>
                <span>На главную</span>
            </a>
        </div>
        """
        
        html += """
    </div>
    
    <style>
        .blank {
            display: inline-block;
            min-width: 100px;
            border-bottom: 2px solid #f6ad55;
            margin: 0 4px;
            color: #a0aec0;
            font-style: italic;
            padding: 2px 4px;
            transition: all 0.3s ease;
        }
        
        .blank.filled {
            color: #d97706;
            font-weight: 600;
            font-style: normal;
            border-bottom-color: #22c55e;
        }
    </style>
    
    <script>
    function toggleAnswers(button) {
        const blanks = document.querySelectorAll('.blank');
        const isShowing = button.textContent.includes('Скрыть');
        
        if (isShowing) {
            blanks.forEach(blank => {
                blank.classList.remove('filled');
                const hint = blank.getAttribute('data-hint');
                blank.textContent = `_______ (${hint})`;
            });
            button.textContent = 'Показать ответы';
            button.style.background = 'linear-gradient(135deg, #f6ad55 0%, #ed8936 100%)';
        } else {
            blanks.forEach(blank => {
                const answer = blank.getAttribute('data-answer');
                if (answer) {
                    blank.classList.add('filled');
                    blank.textContent = answer;
                }
            });
            button.textContent = 'Скрыть ответы';
            button.style.background = 'linear-gradient(135deg, #22c55e 0%, #16a34a 100%)';
        }
    }
    '''
    
    # Находим все места где есть </body> и заменяем
    # Но только в методе generate (первое вхождение после def generate)
    
    # Находим начало метода generate
    generate_start = content.find('def generate(')
    if generate_start == -1:
        print("[ERROR] Метод generate не найден")
        return False
    
    # Находим первый </body> после начала метода generate
    body_close = content.find('</body>', generate_start)
    if body_close == -1:
        print("[ERROR] </body> не найден в методе generate")
        return False
    
    # Находим строку перед </body> для вставки
    # Ищем html += ... перед </body>
    before_body = content.rfind('html +=', generate_start, body_close)
    if before_body == -1:
        print("[ERROR] Не найдено место для вставки")
        return False
    
    # Находим конец этой строки
    line_end = content.find('\n', before_body)
    
    # Вставляем наш код
    new_content = content[:line_end] + '\n' + insert_before_body + content[line_end:]
    
    # Сохраняем
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("[OK] json_generator.py обновлен!")
    print("[+] Добавлена генерация упражнений")
    print("[+] Добавлены навигационные кнопки")
    print("[+] Добавлен JavaScript для интерактивности")
    
    return True

if __name__ == "__main__":
    fix_json_generator()
