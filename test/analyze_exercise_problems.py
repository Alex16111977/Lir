#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Анализ проблем с упражнениями - дубликаты и звездочки
"""

import json
import re
from pathlib import Path

def analyze_exercise(json_file):
    """Анализирует упражнение в JSON файле"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        exercise = data.get('exercise', {})
        if not isinstance(exercise, dict):
            return None
        
        text = exercise.get('text', '')
        answers = exercise.get('answers', {})
        
        problems = []
        
        # 1. Проверка на дубликаты подсказок: ___ (hint) (hint)
        doubles = re.findall(r'(___ \([^)]+\) \([^)]+\))', text)
        if doubles:
            problems.append({
                'type': 'DOUBLE_HINTS',
                'examples': doubles,
                'count': len(doubles)
            })
        
        # 2. Проверка на звездочки вместо подчеркиваний: *****_______ 
        stars_pattern = re.findall(r'(\*{3,}[_\s]*\([^)]+\)[^)]*\([^)]+\))', text)
        if stars_pattern:
            problems.append({
                'type': 'STARS_WITH_DOUBLE',
                'examples': stars_pattern,
                'count': len(stars_pattern)
            })
        
        # 3. Проверка на паттерн DER/DIE/DAS с звездочками
        article_stars = re.findall(r'((?:DER|DIE|DAS)\s+\*{3,}[^)]+\))', text)
        if article_stars:
            problems.append({
                'type': 'ARTICLE_WITH_STARS', 
                'examples': article_stars,
                'count': len(article_stars)
            })
        
        # 4. Проверка соответствия answers и пропусков
        gaps_in_text = re.findall(r'___ \(([^)]+)\)', text)
        mismatched = []
        for gap in gaps_in_text:
            if gap not in answers:
                mismatched.append(gap)
        
        if mismatched:
            problems.append({
                'type': 'MISMATCHED_ANSWERS',
                'missing': mismatched,
                'count': len(mismatched)
            })
        
        if problems:
            return {
                'file': json_file.name,
                'problems': problems,
                'text_sample': text[:200] + '...' if len(text) > 200 else text
            }
        
    except Exception as e:
        return {
            'file': json_file.name,
            'error': str(e)
        }
    
    return None

def main():
    print("[АНАЛИЗ] Проблемы с упражнениями")
    print("=" * 80)
    
    base_dir = Path(r'F:\AiKlientBank\Lir\data')
    
    all_problems = {
        'a2': [],
        'b1': [],
        'thematic': []
    }
    
    for folder in ['a2', 'b1', 'thematic']:
        folder_path = base_dir / folder
        if not folder_path.exists():
            continue
        
        print(f"\n[{folder.upper()}] Анализ папки...")
        
        json_files = list(folder_path.glob('*.json'))
        
        for json_file in json_files:
            result = analyze_exercise(json_file)
            if result:
                all_problems[folder].append(result)
        
        print(f"  Найдено проблемных файлов: {len(all_problems[folder])}")
    
    # Детальный отчет
    print("\n" + "=" * 80)
    print("[ДЕТАЛЬНЫЙ ОТЧЕТ]")
    print("=" * 80)
    
    for folder, problems_list in all_problems.items():
        if not problems_list:
            continue
        
        print(f"\n[{folder.upper()}] Проблемные файлы ({len(problems_list)}):")
        
        for problem_info in problems_list[:3]:  # Показываем первые 3
            print(f"\n  Файл: {problem_info['file']}")
            
            if 'error' in problem_info:
                print(f"    ERROR: {problem_info['error']}")
                continue
            
            for problem in problem_info.get('problems', []):
                print(f"    [{problem['type']}] Найдено: {problem['count']}")
                
                if problem['type'] == 'DOUBLE_HINTS':
                    for ex in problem['examples'][:2]:
                        print(f"      Пример: {ex}")
                
                elif problem['type'] == 'STARS_WITH_DOUBLE':
                    for ex in problem['examples'][:2]:
                        # Обрезаем длинные примеры
                        if len(ex) > 60:
                            print(f"      Пример: {ex[:60]}...")
                        else:
                            print(f"      Пример: {ex}")
                
                elif problem['type'] == 'ARTICLE_WITH_STARS':
                    for ex in problem['examples'][:2]:
                        print(f"      Пример: {ex}")
                
                elif problem['type'] == 'MISMATCHED_ANSWERS':
                    print(f"      Отсутствуют ответы для: {', '.join(problem['missing'][:3])}")
    
    # Общая статистика
    print("\n" + "=" * 80)
    print("[СТАТИСТИКА]")
    total = sum(len(p) for p in all_problems.values())
    print(f"Всего проблемных файлов: {total}")
    
    # Рекомендации
    print("\n[РЕКОМЕНДАЦИИ]")
    print("1. Запустить скрипт исправления для удаления дубликатов")
    print("2. Заменить звездочки на подчеркивания")
    print("3. Проверить соответствие answers и пропусков")
    
    return all_problems

if __name__ == '__main__':
    problems = main()
