"""
Тест: Вправа "Підбір слів" з миттєвою реакцією
Дата: 24.09.2025
Мета: Перевірка генерації сайту з оновленою вправою без кнопки
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import main

# Генеруємо тестову сторінку
print("[TEST] Генеруємо сайт з оновленою вправою...")
main()
print("[OK] Сайт згенеровано!")

# Перевіряємо існування файлів
output_dir = Path(r"F:\AiKlientBank\Lir\output")
html_files = list(output_dir.glob("**/*.html"))
print(f"[OK] Згенеровано HTML файлів: {len(html_files)}")

# Відкриваємо в браузері для перевірки
import webbrowser
test_file = Path(r"F:\AiKlientBank\Lir\output\a2\lesson-01-basics.html")
if test_file.exists():
    webbrowser.open(f"file:///{test_file}")
    print(f"[OK] Відкрито: {test_file.name}")
else:
    print(f"[ERROR] Файл не знайдено: {test_file}")
