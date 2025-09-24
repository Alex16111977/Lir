"""
Перевірка наявності exercise в JSON файлах
"""

import json
from pathlib import Path
import sys

# Додаємо батьківську директорію до шляху
sys.path.insert(0, str(Path(__file__).parent.parent))

def check_exercise():
    """Перевірити наявність exercise в JSON файлах"""
    
    # Перевіряємо конкретний файл
    json_file = Path(r'F:\AiKlientBank\Lir\data\b1\15_Смерть_Корделии_и_Лира_B1.json')
    
    print(f"[CHECK] File: {json_file.name}")
    print(f"[CHECK] Exists: {json_file.exists()}")
    
    if not json_file.exists():
        print("[ERROR] File not found!")
        return
    
    # Читаємо JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"\n[INFO] JSON keys: {list(data.keys())}")
    
    # Перевіряємо exercise
    if 'exercise' in data:
        print("\n[OK] Exercise field found!")
        ex = data['exercise']
        
        print(f"  Title: {ex.get('title', 'N/A')}")
        
        # Аналізуємо текст
        text = ex.get('text', '')
        print(f"  Text length: {len(text)} chars")
        
        # Шукаємо німецькі слова в story-highlight
        import re
        pattern = r'<span class="story-highlight">([^<]+)</span>'
        highlights = re.findall(pattern, text)
        
        print(f"\n[ANALYSIS] Story highlights found: {len(highlights)}")
        for i, highlight in enumerate(highlights[:5], 1):
            print(f"  {i}. {highlight}")
        
        # Аналізуємо answers
        answers = ex.get('answers', {})
        print(f"\n[ANALYSIS] Answers: {len(answers)} items")
        for hint, answer in list(answers.items())[:5]:
            print(f"  '{hint}' -> '{answer}'")
        
        # Перевіряємо проблему
        print("\n[PROBLEM CHECK]")
        # Шукаємо німецькі слова, які вже показані (не мають пропусків)
        visible_german = re.findall(r'([A-Z]{2,}[A-Z\s]+)\s*\([^)]+\)', text)
        print(f"  Visible German words (should be blanks): {len(visible_german)}")
        for word in visible_german[:5]:
            print(f"    - {word}")
        
        # Шукаємо пропуски
        blanks = re.findall(r'___\s*\([^)]+\)', text)
        print(f"  Blanks found: {len(blanks)}")
        
    else:
        print("\n[!] Exercise field NOT found!")
        print("[!] Maybe it's added during enrichment?")
        
        # Перевіряємо збагачувач
        print("\n[CHECK] Running enricher...")
        from src.generators.json_enricher import JSONEnricher
        
        enricher = JSONEnricher()
        enriched = enricher.enrich_json(json_file)
        
        if 'exercise' in enriched:
            print("[OK] Exercise added by enricher!")
        else:
            print("[!] Exercise still missing after enrichment!")

if __name__ == "__main__":
    check_exercise()
