"""
Тест: Виправлення warning() виклику
Дата: 11.10.2025
Мета: Виправити останній LoggerManager.warning()
"""
import sys
from pathlib import Path
import re
sys.path.insert(0, str(Path(__file__).parent.parent))

# Читаємо файл
exercises_file = Path(__file__).parent.parent / 'src' / 'generators' / 'exercises_generator.py'
content = exercises_file.read_text(encoding='utf-8')

print(f"[!] Читаємо: {exercises_file}")

# Шукаємо виклик warning з %s через regex
pattern = r'self\.logger\.warning\(\s*"[^"]*%s[^"]*",\s*[^)]+\)'

matches = list(re.finditer(pattern, content))
print(f"Знайдено {len(matches)} викликів warning() з %s")

if matches:
    for match in matches:
        old_code = match.group()
        print(f"\nСтарий код:\n{old_code}\n")
        
        # Замінюємо %s на f-string
        # Витягуємо частини
        parts = re.match(
            r'self\.logger\.warning\(\s*"([^"]*%s[^"]*)",\s*([^)]+)\)',
            old_code
        )
        if parts:
            template = parts.group(1)
            variable = parts.group(2).strip().rstrip(',')
            
            # Замінюємо %s на {}
            new_template = template.replace('%s', '{}')
            new_code = f'self.logger.warning(f"{new_template}".format({variable}))'
            
            # Або простіший варіант з {variable}
            new_template2 = template.replace('%s', f'{{{variable}}}')
            new_code2 = f'self.logger.warning(f"{new_template2}")'
            
            print(f"Новий код:\n{new_code2}\n")
            content = content.replace(old_code, new_code2)
    
    exercises_file.write_text(content, encoding='utf-8')
    print("[OK] Файл записано!")
else:
    print("[OK] Не знайдено викликів warning() з %s")
