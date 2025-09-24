"""
Test: Generate single lesson for testing
Date: 2025-01-06  
Purpose: Quick test of fixed quiz generator
"""
import subprocess
import sys
from pathlib import Path

print("[TEST] Preparing to generate single lesson...")

# Створюємо тестовий скрипт для одного уроку
test_script = '''
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Змінюємо output для тесту
from src.core.orchestrator import SiteOrchestrator
import json

# Створюємо окрему папку для тесту
output_test = Path(r"F:\\AiKlientBank\\Lir\\output_test")
output_test.mkdir(exist_ok=True)

# Читаємо один урок
data_file = Path(r"F:\\AiKlientBank\\Lir\\data\\b1\\06_Унижение_Лира_B1.json")
with open(data_file, "r", encoding="utf-8") as f:
    lesson_data = json.load(f)
    
# Генеруємо HTML для цього уроку
from src.generators.json_generator import JSONGeneratorRefactored

generator = JSONGeneratorRefactored(logger=None)
html_content = generator.generate_lesson_html(lesson_data, data_file.name)

# Зберігаємо файл
output_file = output_test / "test_lesson.html"
output_file.write_text(html_content, encoding="utf-8")
print(f"[OK] Generated: {output_file}")
'''

# Зберігаємо тестовий скрипт
test_file = Path(r"F:\AiKlientBank\Lir\test\generate_single_test.py")
test_file.write_text(test_script, encoding="utf-8")

# Запускаємо через subprocess
print("[TEST] Running generation...")
result = subprocess.run(
    [sys.executable, str(test_file)],
    capture_output=True,
    text=True,
    cwd=r"F:\AiKlientBank\Lir"
)

if result.returncode == 0:
    print("[OK] Single lesson generated successfully")
    
    # Перевіряємо вміст файлу
    output_file = Path(r"F:\AiKlientBank\Lir\output_test\test_lesson.html")
    if output_file.exists():
        content = output_file.read_text(encoding="utf-8")
        
        # Рахуємо quiz-question блоки
        question_count = content.count('class="quiz-question"')
        de_ru_count = content.count('data-mode="de-ru"')
        ru_de_count = content.count('data-mode="ru-de"')
        
        print(f"[INFO] Quiz questions found: {question_count}")
        print(f"[INFO] DE->RU questions: {de_ru_count}")
        print(f"[INFO] RU->DE questions: {ru_de_count}")
        
        # Перевіряємо текст
        if "12 слів у двох напрямках (24 питань)" in content:
            print("[OK] Correct text found in quiz intro!")
        elif "24 питань" in content:
            print("[OK] Found 24 questions mentioned")
        else:
            print("[!] Check quiz intro text")
    else:
        print(f"[ERROR] File not created: {output_file}")
else:
    print(f"[ERROR] Generation failed: {result.stderr}")
    print(f"[INFO] stdout: {result.stdout}")
