"""
Патч для добавления упражнений и навигации в json_generator.py
"""
import sys
from pathlib import Path

def patch_json_generator():
    """
    Патчит json_generator.py для добавления упражнений и навигации
    """
    file_path = Path(r'F:\AiKlientBank\Lir\src\generators\json_generator.py')
    
    # Читаем файл
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Проверяем, есть ли уже упражнения
    if 'self._create_exercise_html(' in content:
        print("[SKIP] Упражнения уже добавлены в generate_lesson")
        return False
    
    # Находим место для вставки упражнений
    # Ищем конец метода generate_lesson перед return html
    
    # Паттерн для поиска конца generate_lesson
    import re
    
    # Найдем метод generate_lesson
    pattern = r'(def generate_lesson\(.*?\n(?:.*?\n)*?)(        return html)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    
    if not match:
        print("[ERROR] Не найден метод generate_lesson")
        return False
    
    # Вставляем код перед return html
    insertion_code = '''
        # Добавляем упражнение если оно есть
        exercise_data = data.get('exercise')
        if exercise_data:
            html += self._create_exercise_html(exercise_data)
        
        # Добавляем навигационные кнопки ВСЕГДА
        html += \'\'\'
        <!-- НАВІГАЦІЯ ВНИЗУ СТОРІНКИ -->
        <div class="bottom-navigation" style="
            margin-top: 50px;
            padding: 30px 0;
            display: flex;
            justify-content: center;
            gap: 20px;
            border-top: 2px solid #e2e8f0;
            background: white;
        ">
            <a href="../index.html" class="nav-btn" style="
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
            " onmouseover="this.style.transform=\'translateY(-2px)\'" 
              onmouseout="this.style.transform=\'translateY(0)\'">
                <span style="font-size: 1.3em;">📚</span>
                <span>К урокам</span>
            </a>
            <a href="../../index.html" class="nav-btn nav-btn-home" style="
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
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
            " onmouseover="this.style.transform=\'translateY(-2px)\'"
              onmouseout="this.style.transform=\'translateY(0)\'">
                <span style="font-size: 1.3em;">🏠</span>
                <span>На главную</span>
            </a>
        </div>\'\'\'
        
'''
    
    # Заменяем
    new_content = content.replace(
        match.group(2), 
        insertion_code + match.group(2)
    )
    
    # Также добавим JavaScript для упражнений
    js_code = '''
        <script>
        function toggleAnswers(button) {
            const blanks = document.querySelectorAll('.blank');
            const isShowing = button.textContent.includes('Скрыть');
            
            if (isShowing) {
                // Скрываем ответы
                blanks.forEach(blank => {
                    blank.classList.remove('filled');
                    const hint = blank.getAttribute('data-hint');
                    blank.textContent = `_______ (${hint})`;
                });
                button.textContent = 'Показать ответы';
                button.classList.remove('success');
            } else {
                // Показываем ответы
                const exerciseSection = button.closest('.exercise-section');
                const exerciseData = exerciseSection.dataset.answers;
                
                if (exerciseData) {
                    const answers = JSON.parse(exerciseData);
                    blanks.forEach(blank => {
                        const hint = blank.getAttribute('data-hint');
                        if (answers[hint]) {
                            blank.classList.add('filled');
                            blank.textContent = answers[hint];
                        }
                    });
                }
                
                button.textContent = 'Скрыть ответы';
                button.classList.add('success');
            }
        }
        </script>
'''
    
    # Добавляем JavaScript перед закрывающим </body>
    if 'toggleAnswers' not in new_content:
        new_content = new_content.replace('</body>', js_code + '\n</body>')
    
    # Сохраняем обновленный файл
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("[OK] json_generator.py обновлен!")
    print("[+] Добавлена генерация упражнений")
    print("[+] Добавлены навигационные кнопки")
    print("[+] Добавлен JavaScript для упражнений")
    return True

if __name__ == "__main__":
    patch_json_generator()
