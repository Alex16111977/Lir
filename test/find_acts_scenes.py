"""
Скрипт для поиска где генерируются акты и сцены
"""

with open(r'F:\AiKlientBank\Lir\src\generators\json_generator.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Поиск generate_from_json...")
for i, line in enumerate(lines):
    if 'def generate_from_json' in line:
        print(f"\n[OK] Найден метод на строке {i+1}")
        # Покажем 200 строк от начала
        for j in range(i, min(i+200, len(lines))):
            if 'АКТ' in lines[j] or 'gruppe' in lines[j] or 'act_scenes' in lines[j]:
                print(f"Строка {j+1}: {lines[j].strip()}")
        break

print("\n\nПоиск где добавляются акты и сцены...")
# Ищем где могут добавляться акты
act_scenes_map = {}
for i, line in enumerate(lines):
    if 'АКТ' in line and 'СЦЕНА' in line:
        print(f"Строка {i+1}: {line.strip()}")
        
# Специально ищем структуру для B1
print("\n\nПоиск B1 структуры...")
for i, line in enumerate(lines):
    if 'b1' in line.lower() and ('gruppe' in line or 'group' in line):
        print(f"Строка {i+1}: {line.strip()}")
