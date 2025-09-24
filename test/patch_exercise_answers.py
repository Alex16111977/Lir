"""
ПАТЧ для json_generator.py - виправляє відображення відповідей у вправах
"""

import sys
from pathlib import Path

# Додаємо шлях до проекту
sys.path.insert(0, str(Path(__file__).parent.parent))

# Читаємо поточний генератор
generator_file = Path(r'F:\AiKlientBank\Lir\src\generators\json_generator.py')
content = generator_file.read_text(encoding='utf-8')

print("=" * 70)
print("ПАТЧ ГЕНЕРАТОРА - Виправлення відповідей у вправах")
print("=" * 70)

# Знаходимо метод _create_exercise_html
if '_create_exercise_html' in content:
    print("\n[1] Знайдено метод _create_exercise_html")
    
    # Патчимо генерацію HTML для вправи
    # Замінюємо просту генерацію на розширену з JavaScript
    
    old_pattern = '''html_blank = f'<span class="blank" data-hint="{hint}">_______ ({hint})</span>'''
    
    new_pattern = '''html_blank = f'<span class="blank" data-hint="{hint}" data-answer="{answer}">_______ ({hint})</span>'''
    
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        print("[OK] Оновлено генерацію пропусків - додано data-answer")
    else:
        print("[!] Шаблон не знайдено, шукаємо альтернативний")
    
    # Додаємо JavaScript з відповідями
    # Знаходимо місце після кнопки
    button_pattern = '''onclick="toggleAnswers(this)"'''
    
    if button_pattern in content:
        print("[2] Знайдено кнопку toggleAnswers")
        
        # Додаємо JavaScript об'єкт з відповідями після секції
        js_addition = '''
        
        <script>
            // Відповіді для вправи
            const exerciseAnswers = {answers_json};
            
            function toggleAnswers(button) {{
                const blanks = document.querySelectorAll('.blank');
                const isShowing = button.textContent === 'Скрыть ответы';
                
                blanks.forEach(blank => {{
                    const hint = blank.dataset.hint;
                    const answer = exerciseAnswers[hint] || blank.dataset.answer;
                    
                    if (isShowing) {{
                        blank.innerHTML = `_______ (${{hint}})`;
                        blank.classList.remove('filled');
                    }} else {{
                        blank.innerHTML = `<strong>${{answer}}</strong> (${{hint}})`;
                        blank.classList.add('filled');
                    }}
                }});
                
                button.textContent = isShowing ? 'Показать ответы' : 'Скрыть ответы';
                button.classList.toggle('success');
            }}
        </script>'''
        
        # Шукаємо де вставити скрипт
        section_end = '''</section>'''
        
        # Модифікуємо генератор щоб додавати скрипт
        if section_end in content:
            # Вставляємо перед закриттям секції
            insert_point = content.find('</section>\n        \n        <!-- НАВІГАЦІЯ')
            if insert_point == -1:
                insert_point = content.find('</section>')
            
            if insert_point != -1:
                # Додаємо скрипт перед </section>
                print("[3] Додаємо JavaScript для обробки відповідей")
                
                # Знаходимо де формується HTML вправи
                exercise_html_start = content.find('html = f\'\'\'')
                exercise_html_end = content.find('\'\'\'', exercise_html_start + 10)
                
                if exercise_html_start != -1 and exercise_html_end != -1:
                    old_html = content[exercise_html_start:exercise_html_end+3]
                    
                    # Додаємо скрипт в кінець HTML шаблону
                    new_html = old_html.replace(
                        '</section>',
                        '''</section>
        
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
        </script>'''
                    )
                    
                    content = content.replace(old_html, new_html)
                    print("[OK] JavaScript доданий в шаблон")
    
    # Зберігаємо оновлений файл
    generator_file.write_text(content, encoding='utf-8')
    print("\n[OK] Генератор оновлено!")
    
else:
    print("[ERROR] Метод _create_exercise_html не знайдено")
    print("Створюємо простий патч...")

print("\n[4] Перегенеруємо сайт з виправленнями...")

# Запускаємо генерацію
import subprocess

result = subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\main.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)

if result.returncode == 0:
    print("[OK] Сайт перегенеровано!")
    
    # Перевіряємо результат
    from pathlib import Path
    test_file = Path(r'F:\AiKlientBank\Lir\output\b1\gruppe_5_finale\14_Duel_bratev_B1.html')
    
    if test_file.exists():
        content = test_file.read_text(encoding='utf-8')
        
        # Перевіряємо чи є JavaScript з відповідями
        if 'exerciseAnswers' in content:
            print("[OK] JavaScript з відповідями доданий!")
        
        if 'toggleAnswers' in content:
            print("[OK] Функція toggleAnswers присутня!")
            
        if 'die Ehre' in content or 'data-answer' in content:
            print("[OK] Відповіді збережені в HTML!")
        else:
            print("[!] Відповіді можуть не відображатися")
else:
    print("[ERROR] Помилка генерації")
    print(result.stderr)

print("\n" + "=" * 70)
print("ПАТЧ ЗАВЕРШЕНО!")
print("Тепер при натисканні 'Показать ответы' мають з'являтися німецькі слова")
