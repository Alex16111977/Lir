
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Змінюємо output для тесту
from src.core.orchestrator import SiteOrchestrator
import json

# Створюємо окрему папку для тесту
output_test = Path(r"F:\AiKlientBank\Lir\output_test")
output_test.mkdir(exist_ok=True)

# Читаємо один урок
data_file = Path(r"F:\AiKlientBank\Lir\data\b1\06_Унижение_Лира_B1.json")
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
