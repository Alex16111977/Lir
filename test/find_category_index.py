"""
Найдем где создаются карточки уроков для B1 категории
"""

with open(r'F:\AiKlientBank\Lir\src\generators\json_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

print("Ищем где генерируется HTML для B1 категории...")
print("="*50)

# Найдем метод _generate_category_index
for i, line in enumerate(lines):
    if 'def _generate_category_index' in line:
        print(f"\n[OK] Найден метод _generate_category_index на строке {i+1}")
        # Показываем следующие 100 строк
        for j in range(i, min(i+100, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
