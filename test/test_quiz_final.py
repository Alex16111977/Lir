"""
Фінальний тест інтерактивної вікторини
Дата: 06.09.2025
"""
import subprocess
import sys
from pathlib import Path
import webbrowser

print("\n" + "="*60)
print("[FINAL TEST] Перевірка інтерактивної вікторини") 
print("="*60 + "\n")

# 1. Генерація сайту
print("[STEP 1] Генерація сайту...")
result = subprocess.run(
    [sys.executable, 'main.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)

if result.returncode == 0:
    print("[OK] Сайт згенеровано успішно!")
    
    # 2. Перевірка файлів
    output_dir = Path(r'F:\AiKlientBank\Lir\output')
    html_files = list(output_dir.glob('**/*.html'))
    print(f"[OK] Згенеровано {len(html_files)} HTML файлів")
    
    # 3. Знаходимо файл з вікториною
    lesson_file = None
    for html_file in html_files:
        if 'lesson' in html_file.name:
            content = html_file.read_text(encoding='utf-8')
            if 'quiz-container' in content:
                lesson_file = html_file
                print(f"[OK] Знайдено урок з вікториною: {lesson_file.name}")
                break
    
    # 4. Перевірка елементів
    if lesson_file:
        checks = [
            ('quiz-container', 'Контейнер вікторини'),
            ('answer-btn', 'Кнопки відповідей'),
            ('checkQuizAnswer', 'JavaScript функція'),
            ('progress-bar', 'Прогрес-бар'),
            ('word-display', 'Відображення слів'),
            ('quiz-result', 'Блок результатів')
        ]
        
        all_passed = True
        for check, desc in checks:
            if check in content:
                print(f"  [OK] {desc}")
            else:
                print(f"  [FAIL] {desc}")
                all_passed = False
        
        if all_passed:
            print("\n[SUCCESS] Всі компоненти вікторини присутні!")
            print(f"\n[URL] file:///{lesson_file}")
            
            # Відкрити в браузері
            try:
                webbrowser.open(f'file:///{lesson_file}')
                print("[OK] Відкрито в браузері")
            except:
                print("[INFO] Відкрийте файл вручну в браузері")
    
    # 5. Відкрити демо сторінку
    demo_file = Path(r'F:\AiKlientBank\Lir\test\quiz_demo.html')
    if demo_file.exists():
        print(f"\n[DEMO] Тестова сторінка: file:///{demo_file}")
else:
    print(f"[ERROR] Помилка генерації")
    print(result.stderr[:500] if result.stderr else "No error details")

print("\n" + "="*60)
print("[COMPLETE] Тестування завершено!")
print("="*60)