"""
test/final_validation.py
Фінальна валідація повного словаря
Дата: 10.10.2025
"""

import sys
from pathlib import Path
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent.parent))

def validate_full_vocabulary():
    """Фінальна валідація"""
    
    print("=== ФІНАЛЬНА ПЕРЕВІРКА ===\n")
    
    output = Path(r'F:\AiKlientBank\Lir\texts\thematic_vocabulary_full.html')
    
    if not output.exists():
        print("[ERROR] Файл не створено!")
        return False
    
    with open(output, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # ЧЕКЛИСТ
    checks = {
        "Файл існує": output.exists(),
        "Розмір > 200 KB": len(html) > 200000,
        "Оглавлення": soup.find('section', id='table-of-contents') is not None,
        "13 карточек тем": len(soup.find_all('a', class_='toc-card')) == 13,
        "13 таблиць": len(soup.find_all('table', class_='vocab-table')) == 13,
        "200+ слів": len(soup.find_all('tr', class_='word-row')) >= 200,
        "Робочі посилання": all(
            link.get('href', '').startswith('#text-')
            for link in soup.find_all('a', class_='text-link')
        ),
        "Реальні назви текстів": 'Текст 1' not in html and 'Текст 2' not in html,
        "UTF-8 підтримка": 'äöüß' in html or 'Getränk' in html,
        "CSS стилі": '<style>' in html,
        "Градієнтний дизайн": 'linear-gradient' in html,
    }
    
    print("[+] Чеклист:\n")
    all_passed = True
    
    for check, result in checks.items():
        status = "[OK] ✓" if result else "[ERROR] ✗"
        print(f"{status} {check}")
        if not result:
            all_passed = False
    
    if all_passed:
        file_size = len(html) / 1024
        words_count = len(soup.find_all('tr', class_='word-row'))
        links_count = len(soup.find_all('a', class_='text-link'))
        
        print(f"\n[SUCCESS] ✓✓✓ ВСІ ТЕСТИ ПРОЙДЕНІ! ✓✓✓")
        print(f"\n[INFO] Деталі:")
        print(f"  - Файл: {output}")
        print(f"  - Розмір: {file_size:.2f} KB")
        print(f"  - Слів: {words_count}")
        print(f"  - Посилань: {links_count}")
        print(f"  - Тем: {len(soup.find_all('div', class_='theme-section'))}")
    else:
        print("\n[ERROR] Деякі тести не пройдені!")
    
    return all_passed

if __name__ == '__main__':
    success = validate_full_vocabulary()
    sys.exit(0 if success else 1)
