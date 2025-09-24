"""
Найдем где обрабатываются файлы B1 и добавляются акты и сцены
"""

with open(r'F:\AiKlientBank\Lir\src\generators\json_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

print("Ищем где обрабатываются B1 файлы...")
print("="*50)

# Сначала найдем generate_from_json
in_method = False
method_lines = []
for i, line in enumerate(lines):
    if 'def generate_from_json' in line:
        in_method = True
        print(f"[OK] Метод generate_from_json начинается на строке {i+1}\n")
    
    if in_method:
        method_lines.append((i+1, line))
        # Найдем обработку B1
        if 'b1' in line.lower():
            print(f"Строка {i+1}: {line}")
        # Ищем где добавляются акты
        if 'act_scenes' in line.lower() or 'АКТ' in line:
            print(f"Строка {i+1}: {line}")
        # Остановим после 300 строк метода
        if len(method_lines) > 300:
            break

print("\n\nИщем map актов и сцен...")
# Проверим есть ли где-то маппинг актов
for i, line in enumerate(lines):
    if 'act_scenes' in line.lower() and '=' in line:
        print(f"Найден map на строке {i+1}:")
        # Покажем следующие 50 строк
        for j in range(i, min(i+50, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
