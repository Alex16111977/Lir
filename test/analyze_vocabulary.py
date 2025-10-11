"""
test/analyze_vocabulary.py
Аналіз словникового запасу з текстів
Дата: 10.10.2025
"""

import sys
from pathlib import Path
import re
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))

def extract_words_from_texts():
    """Витягування слів з текстів"""
    
    # Читання базового HTML
    html_path = Path(__file__).parent.parent / 'texts' / 'thematic_vocabulary.html'
    
    print(f"[+] Читання файлу: {html_path}")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"[+] Розмір файлу: {len(content)} символів")
    
    # Витягування текстів з <p> тегів
    texts = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
    print(f"[+] Знайдено параграфів: {len(texts)}")
    
    # Словник для підрахунку
    word_freq = defaultdict(int)
    
    for text in texts:
        # Розділення на слова (німецькі букви)
        words = re.findall(r'[a-zA-ZäöüÄÖÜß]+', text)
        
        for word in words:
            if len(word) > 3:  # Мінімум 4 літери
                word_freq[word.lower()] += 1
    
    # Топ-200 найчастіших слів
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:200]
    
    print(f"\n[OK] Знайдено {len(word_freq)} унікальних слів")
    print(f"[OK] Топ-10 найчастіших слів:")
    for word, count in top_words[:10]:
        print(f"  - {word}: {count} разів")
    
    return top_words, word_freq

def main():
    print("=== АНАЛІЗ СЛОВНИКОВОГО ЗАПАСУ ===\n")
    
    top_words, all_words = extract_words_from_texts()
    
    # Збереження результату
    output = Path(__file__).parent.parent / 'test' / 'vocabulary_analysis.txt'
    with open(output, 'w', encoding='utf-8') as f:
        f.write("ТОП-200 СЛІВ\n")
        f.write("=" * 50 + "\n\n")
        for word, count in top_words:
            f.write(f"{word}\t{count}\n")
        
        f.write("\n\nВСІ СЛОВА (A-Z)\n")
        f.write("=" * 50 + "\n\n")
        for word in sorted(all_words.keys()):
            f.write(f"{word}\t{all_words[word]}\n")
    
    print(f"\n[OK] Результати збережено в: {output}")
    print(f"[OK] Всього унікальних слів: {len(all_words)}")

if __name__ == '__main__':
    main()
