#!/usr/bin/env python3
"""
Тест: Проверка исправления проблемы с артиклями
Дата: 06.09.2025
Мета: Проверить, что артикли НЕ появляются перед пропусками в упражнениях
"""

import re
from pathlib import Path

def check_articles_in_html():
    """Проверяет наличие артиклей перед пропусками"""
    
    # Путь к проблемному файлу
    html_file = Path(r'F:\AiKlientBank\Lir\output\b1\gruppe_2_verrat\06_Unizhenie_Lira_B1.html')
    
    if not html_file.exists():
        print(f"[ERROR] Файл не найден: {html_file}")
        return False
        
    # Читаем HTML
    html = html_file.read_text(encoding='utf-8')
    
    # Находим секцию упражнения
    exercise_match = re.search(r'<div class="exercise">(.*?)</div>', html, re.DOTALL)
    
    if not exercise_match:
        print("[ERROR] Секция упражнения не найдена")
        return False
        
    exercise_html = exercise_match.group(1)
    
    # Ищем все пропуски с контекстом
    # Паттерн: текст перед + span с классом blank
    pattern = r'([\w\s]{0,30})<span class="blank"[^>]*data-hint="([^"]*)"[^>]*data-answer="([^"]*)"[^>]*>'
    blanks = re.findall(pattern, exercise_html)
    
    print("\n" + "="*60)
    print("ПРОВЕРКА АРТИКЛЕЙ ПЕРЕД ПРОПУСКАМИ")
    print("="*60)
    
    errors = []
    for i, (text_before, hint, answer) in enumerate(blanks, 1):
        text_before = text_before.strip()
        
        # Проверяем наличие немецких артиклей
        if re.search(r'\b(der|die|das|den|dem|des)\s*$', text_before, re.IGNORECASE):
            errors.append(f"Пропуск '{hint}': артикль найден -> '{text_before}'")
            print(f"[ERROR] #{i}. {hint} -> АРТИКЛЬ: '{text_before}' перед пропуском")
        else:
            print(f"[OK] #{i}. {hint} -> чисто")
            
    # Также проверим story секцию
    story_match = re.search(r'<div class="story-text">(.*?)</div>', html, re.DOTALL)
    if story_match:
        story_html = story_match.group(1)
        highlights = re.findall(r'<span class="story-highlight">([^<]+)</span>', story_html)
        
        print("\n" + "="*60)
        print("ПРОВЕРКА STORY HIGHLIGHTS")
        print("="*60)
        
        for h in highlights[:5]:
            if re.match(r'^(der|die|das|den|dem|des)\s+', h):
                print(f"[ERROR] Артикль в highlight: {h}")
                errors.append(f"Story: артикль в '{h}'")
            else:
                print(f"[OK] Без артикля: {h}")
    
    # Итог
    print("\n" + "="*60)
    if errors:
        print(f"[!] НАЙДЕНО ПРОБЛЕМ: {len(errors)}")
        for err in errors:
            print(f"    - {err}")
        return False
    else:
        print("[OK] ПРОБЛЕМА РЕШЕНА! Артиклей перед пропусками НЕТ!")
        return True
        
    print("="*60)
    
if __name__ == "__main__":
    success = check_articles_in_html()
    
    # Сохраняем результат в файл
    report_file = Path(r'F:\AiKlientBank\Lir\test\articles_check_report.txt')
    with open(report_file, 'w', encoding='utf-8') as f:
        if success:
            f.write("[OK] Проблема с артиклями РЕШЕНА!\n")
            f.write("Артикли НЕ появляются перед пропусками в упражнениях.\n")
        else:
            f.write("[ERROR] Проблема с артиклями ЕЩЁ ЕСТЬ!\n")
            f.write("Найдены артикли перед пропусками.\n")
            
    print(f"\n[+] Отчет сохранен: {report_file}")
