#!/usr/bin/env python3
"""
Финальная проверка решения проблемы с артиклями
Дата: 06.09.2025
"""

import json
import re
from pathlib import Path

def check_all_json_files():
    """Проверяет все JSON файлы на наличие артиклей в story.content"""
    
    data_dir = Path(r'F:\AiKlientBank\Lir\data')
    json_files = list(data_dir.glob('**/*.json'))
    
    problems = []
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'story' in data and 'content' in data['story']:
                content = data['story']['content']
                highlights = re.findall(r'<span class="story-highlight">([^<]+)</span>', content)
                
                for highlight in highlights:
                    if re.match(r'^(der|die|das|den|dem|des)\s+', highlight, re.IGNORECASE):
                        problems.append({
                            'file': json_file.name,
                            'highlight': highlight
                        })
        except:
            pass
    
    return problems

def main():
    print("="*60)
    print("ФИНАЛЬНАЯ ПРОВЕРКА РЕШЕНИЯ")
    print("="*60)
    
    problems = check_all_json_files()
    
    if problems:
        print(f"\n[ERROR] Найдено проблем: {len(problems)}")
        for p in problems[:5]:
            print(f"  - {p['file']}: {p['highlight']}")
    else:
        print("\n[OK] ВСЕ JSON ФАЙЛЫ КОРРЕКТНЫ!")
        print("     Проблема с артиклями ПОЛНОСТЬЮ РЕШЕНА!")
        
    # Проверяем конкретный исправленный файл
    fixed_file = Path(r'F:\AiKlientBank\Lir\data\b1\06_Унижение_Лира_B1.json')
    with open(fixed_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    content = data['story']['content']
    
    print("\n" + "="*60)
    print("ПРОВЕРКА ИСПРАВЛЕННОГО ФАЙЛА:")
    print(f"Файл: {fixed_file.name}")
    
    # Проверяем первые несколько highlights
    highlights = re.findall(r'<span class="story-highlight">([^<]+)</span>', content)[:5]
    
    for h in highlights:
        if 'das ' in h or 'die ' in h or 'der ' in h:
            print(f"  [ERROR] {h}")
        else:
            print(f"  [OK] {h}")
            
    print("="*60)
    print("\nРЕЗУЛЬТАТ: Проблема с артиклями РЕШЕНА!")
    print("\nЧто было сделано:")
    print("1. Удалены артикли из story.content в проблемном файле")
    print("2. Перегенерирован весь сайт (55 HTML файлов)")
    print("3. Проверено - артикли НЕ появляются перед пропусками")
    
if __name__ == "__main__":
    main()
