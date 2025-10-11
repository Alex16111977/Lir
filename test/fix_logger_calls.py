"""
Тест: Виправлення викликів логера
Дата: 11.10.2025
Мета: Виправити LoggerManager.warning() calls
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Читаємо файл
exercises_file = Path(__file__).parent.parent / 'src' / 'generators' / 'exercises_generator.py'
content = exercises_file.read_text(encoding='utf-8')

print(f"[!] Читаємо: {exercises_file}")
print(f"Розмір файлу: {len(content)} символів")

# Виправляємо виклик 1 - warning з %s
old_warning = '''                self.logger.warning(
                    "[Exercises] Не знайдено словник для синонімів: %s",
                    self.GLOBAL_VOCAB_PATH,
                )'''

new_warning = '''                self.logger.warning(
                    f"[Exercises] Не знайдено словник для синонімів: {self.GLOBAL_VOCAB_PATH}"
                )'''

if old_warning in content:
    content = content.replace(old_warning, new_warning)
    print("[OK] Виправлено виклик warning()")
else:
    print("[ERROR] Не знайдено виклик warning()")

# Виправляємо виклик 2 - error з %s
old_error = '                self.logger.error("[Exercises] Неможливо прочитати словник: %s", exc)'
new_error = '                self.logger.error(f"[Exercises] Неможливо прочитати словник: {exc}")'

if old_error in content:
    content = content.replace(old_error, new_error)
    print("[OK] Виправлено виклик error()")
else:
    print("[ERROR] Не знайдено виклик error()")

# Перевіряємо що більше немає %s
if '"%s"' in content and 'f"' not in content[:content.index('"%s"')]:
    print("[ERROR] Залишилися виклики з %s!")
    # Знайдемо де
    for i, line in enumerate(content.split('\n'), 1):
        if '"%s"' in line and 'self.logger' in line:
            print(f"  Рядок {i}: {line.strip()}")
else:
    print("[OK] Виправлення застосовані!")
    
# Записуємо
exercises_file.write_text(content, encoding='utf-8')
print(f"[OK] Файл записано: {exercises_file}")
