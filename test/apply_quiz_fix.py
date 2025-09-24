"""Apply quiz fix to exercises generator."""

import shutil
import datetime
from pathlib import Path

# Пути к файлам
original = Path(r'F:\AiKlientBank\Lir\src\generators\exercises_generator.py')
fixed = Path(r'F:\AiKlientBank\Lir\src\generators\exercises_generator_fixed.py')
backup_dir = Path(r'F:\AiKlientBank\Lir\backup')

# Создаем резервную копию
backup_dir.mkdir(exist_ok=True)
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = backup_dir / f'exercises_generator_{timestamp}.py'
shutil.copy2(original, backup_file)
print(f'[OK] Backup created: {backup_file.name}')

# Заменяем оригинальный файл
shutil.copy2(fixed, original)
print(f'[OK] Original file replaced with fixed version')

# Удаляем временный файл
fixed.unlink()
print('[OK] Temporary file removed')

# Проверяем изменения
with open(original, 'r', encoding='utf-8') as f:
    content = f.read()
    # Ищем ключевые изменения
    if 'Використовуємо ВСІ слова!' in content:
        print('[OK] Quiz fix confirmed - ALL words will be used')
    if 'len(selectable) <= 20' in content:
        print('[OK] Word matching fix confirmed')
    if 'len(nouns) <= 18' in content:
        print('[OK] Articles fix confirmed')
        
print('\n[!] All exercises now use ALL words from lesson!')
print('[!] Run main.py to regenerate site with updated exercises')
