#!/usr/bin/env python
"""
Оновлення вправи "Подбор слов" для оптимізації під планшети.
Дата: 27.09.2025
Мета: Двоколоночний дизайн без прокрутки для 12 слів
"""

import sys
from pathlib import Path
import re

# Додаємо батьківську директорію до sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

def update_word_matching_method():
    """Оновлюємо метод _generate_word_matching"""
    
    exercises_generator_path = Path(__file__).parent.parent / "src" / "generators" / "exercises_generator.py"
    
    if not exercises_generator_path.exists():
        print("[ERROR] Файл exercises_generator.py не знайдено!")
        return False
    
    # Читаємо файл
    content = exercises_generator_path.read_text(encoding="utf-8")
    
    # Новий оптимізований метод (з правильним форматуванням)
    new_method = '''def _generate_word_matching(self, vocabulary: List[Dict[str, Any]]) -> str:
        """[OPTIMIZED] Двухколоночный вид для планшетов без прокрутки."""
        selectable = [word for word in vocabulary if word.get("german") and word.get("translation")]
        if not selectable:
            return ""

        # Используем ВСЕ слова (обычно 12 в уроке)
        sample = selectable if len(selectable) <= 20 else random.sample(selectable, 20)
        
        # Разделяем на две колонки
        german_words_html = []
        russian_words_html = []
        
        # Немецкие слова в левую колонку
        for idx, word in enumerate(sample):
            german_words_html.append(
                f"""
                <button class=\\"word-item german-word\\" data-pair-id=\\"{idx}\\" 
                        onclick=\\"handleWordPairClick(this, {idx}, 'german')\\" type=\\"button\\">
                    <span class=\\"word-main\\">{escape(word.get('german', ''))}</span>
                    <small class=\\"transcription\\">{escape(word.get('transcription', ''))}</small>
                </button>
                """
            )
        
        # Перемешиваем переводы для правой колонки
        shuffled_pairs = [(idx, word) for idx, word in enumerate(sample)]
        random.shuffle(shuffled_pairs)
        
        for idx, word in shuffled_pairs:
            # Русские переводы в правую колонку
            russian_words_html.append(
                f"""
                <button class=\\"word-item russian-word\\" data-pair-id=\\"{idx}\\"
                        onclick=\\"handleWordPairClick(this, {idx}, 'russian')\\" type=\\"button\\">
                    <span class=\\"word-main\\">{escape(word.get('translation', ''))}</span>
                </button>
                """
            )
        
        total_pairs = len(sample)

        return f"""\\n            <div class=\\"exercise-block\\" id=\\"word-matching\\">\\n                <h3 class=\\"exercise-title\\">🔗 Подбор слов</h3>\\n                <p class=\\"exercise-intro\\">Выберите немецкое слово слева и его русский перевод справа</p>\\n                \\n                <!-- Прогресс-бар -->\\n                <div class=\\"matching-progress\\">\\n                    <div class=\\"progress-track\\">\\n                        <div class=\\"progress-fill\\" style=\\"width: 0%\\"></div>\\n                    </div>\\n                    <div class=\\"progress-text\\">0 из {total_pairs}</div>\\n                </div>\\n                \\n                <div class=\\"word-selection-container\\">\\n                    <div class=\\"word-columns\\">\\n                        <div class=\\"word-column german-words\\">\\n                            <h4>НЕМЕЦКИЕ</h4>\\n                            <div class=\\"word-list\\">\\n{"".join(german_words_html)}\\n                            </div>\\n                        </div>\\n                        <div class=\\"word-column russian-words\\">\\n                            <h4>РУССКИЕ</h4>\\n                            <div class=\\"word-list\\">\\n{"".join(russian_words_html)}\\n                            </div>\\n                        </div>\\n                    </div>\\n                </div>\\n            </div>\\n            """'''
    
    # Знаходимо і замінюємо метод
    pattern = r'def _generate_word_matching\(self.*?\n(?:.*?\n)*?^\s{4}""".*?""".*?(?:.*?\n)*?return f""".*?"""'
    
    # Використовуємо більш простий підхід - знайти початок методу і замінити до наступного методу
    start_pattern = r'def _generate_word_matching\(self, vocabulary: List\[Dict\[str, Any\]\]\) -> str:'
    start_match = re.search(start_pattern, content)
    
    if not start_match:
        print("[ERROR] Не вдалося знайти метод _generate_word_matching!")
        return False
    
    # Знаходимо наступний метод
    next_method_pattern = r'\n    def _generate_articles\('
    next_match = re.search(next_method_pattern, content[start_match.start():])
    
    if not next_match:
        print("[ERROR] Не вдалося знайти наступний метод!")
        return False
    
    # Замінюємо весь блок методу
    new_content = (
        content[:start_match.start()] + 
        '    ' + new_method + '\n' +
        content[start_match.start() + next_match.start():]
    )
    
    # Зберігаємо оновлений файл
    exercises_generator_path.write_text(new_content, encoding="utf-8")
    print("[OK] Метод _generate_word_matching оновлено!")
    return True


def update_css_styles():
    """Оновлюємо CSS стилі для планшетів"""
    
    exercises_assets_path = Path(__file__).parent.parent / "src" / "generators" / "exercises_assets.py"
    
    if not exercises_assets_path.exists():
        print("[ERROR] Файл exercises_assets.py не знайдено!")
        return False
    
    # Читаємо файл
    content = exercises_assets_path.read_text(encoding="utf-8")
    
    # Оновлені CSS стилі для Word Matching (спрощений патерн пошуку)
    css_update = '''/* Word Matching - OPTIMIZED FOR TABLET WITHOUT SCROLL */
.word-selection-container {
    margin-top: 16px;
}

.word-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    /* Фіксована висота для 12 слів */
    height: 520px; 
    background: rgba(255, 255, 255, 0.5);
    border-radius: 12px;
    padding: 16px;
}

.word-column {
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.word-column h4 {
    text-align: center;
    color: #4b5563;
    font-weight: 600;
    margin: 0 0 12px 0;
    padding-bottom: 8px;
    border-bottom: 2px solid #e2e8f0;
    font-size: 13px;
}

.word-list {
    /* БЕЗ скролла - всі слова видно */
    flex: 1;
    padding: 4px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    overflow: visible;
}

/* Оптимізовані розміри для планшетів */
.word-item {
    background: white;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    padding: 8px 12px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: left;
    font-size: 14px;
    min-height: 38px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.word-item:hover:not(.correct):not(.disabled) {
    border-color: #a78bfa;
    background: #f9fafb;
    transform: translateX(2px);
}

.word-item.selected {
    background: linear-gradient(135deg, #eef2ff, #e0e7ff);
    border-color: #6366f1;
    transform: scale(1.01);
}

.word-item.correct {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    border-color: #16a34a;
    transform: scale(0.97);
    opacity: 0.9;
    pointer-events: none;
}

.word-item.incorrect {
    background: linear-gradient(135deg, #ef4444, #dc2626) !important;
    color: white !important;
    animation: shake 0.5s;
}

.word-item .word-main {
    font-weight: 600;
    display: block;
    font-size: 14px;
    line-height: 1.2;
}

.word-item .transcription {
    font-size: 11px;
    color: #6b7280;
    margin-top: 2px;
    font-style: italic;
}

.word-item.correct .transcription {
    color: rgba(255, 255, 255, 0.9);
}'''
    
    # Знаходимо секцію Word Matching і замінюємо 
    pattern = r'/\* Word Matching.*?\*/'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("[WARN] Не знайдено секцію Word Matching в CSS, додаємо нову...")
        # Якщо не знайдено, просто додаємо після .check-btn:active
        content = content.replace('.check-btn:active {', '.check-btn:active {')
        # Вставляємо після стилів кнопок
        insert_pos = content.find('.check-btn:active {')
        if insert_pos != -1:
            end_pos = content.find('}', insert_pos) + 1
            content = content[:end_pos] + '\n\n' + css_update + '\n' + content[end_pos:]
    else:
        # Знайдено, замінюємо до наступної секції
        start = match.start()
        # Шукаємо наступну секцію (/* Articles */)
        next_section = re.search(r'/\* Articles', content[start:])
        if next_section:
            end = start + next_section.start()
            content = content[:start] + css_update + '\n\n' + content[end:]
        else:
            print("[ERROR] Не вдалося знайти кінець секції Word Matching!")
            return False
    
    # Зберігаємо оновлений файл
    exercises_assets_path.write_text(content, encoding="utf-8")
    print("[OK] CSS стилі оновлено!")
    return True


def update_javascript():
    """Оновлюємо JavaScript для нової логіки"""
    
    exercises_assets_path = Path(__file__).parent.parent / "src" / "generators" / "exercises_assets.py"
    
    if not exercises_assets_path.exists():
        print("[ERROR] Файл exercises_assets.py не знайдено!")
        return False
    
    # Читаємо файл
    content = exercises_assets_path.read_text(encoding="utf-8")
    
    # Оновлений JavaScript для Word matching (відновлений з вашого файлу)
    js_update = '''    // 1. Word matching with two columns
    let selectedGerman = null;
    let selectedRussian = null;
    let correctPairs = 0;
    let matchedPairs = new Set();'''
    
    # Знаходимо початок секції Word matching в JS
    pattern = r'// 1\. Word matching.*?let selectedGerman'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        # Замінюємо початкові змінні
        start = match.start()
        end = content.find('window.handleWordPairClick', start)
        if end != -1:
            content = content[:start] + js_update + '\n\n    ' + content[end:]
            print("[OK] JavaScript оновлено!")
        else:
            print("[WARN] JavaScript вже має правильну структуру")
    else:
        print("[WARN] JavaScript секція Word matching не знайдена")
    
    # Зберігаємо
    exercises_assets_path.write_text(content, encoding="utf-8")
    return True


def main():
    print("[+] Починаємо оновлення упражнення 'Подбор слов'...")
    
    success = True
    
    # 1. Оновлюємо метод _generate_word_matching
    if not update_word_matching_method():
        success = False
    
    # 2. Оновлюємо CSS стилі
    if not update_css_styles():
        success = False
    
    # 3. Оновлюємо JavaScript
    if not update_javascript():
        success = False
    
    if success:
        print("\n[OK] ВСІ оновлення успішно застосовані!")
        print("[!] Тепер запустіть main.py для генерації сайту з новим дизайном")
        print(f"[!] python main.py")
    else:
        print("\n[ERROR] Деякі оновлення не вдалося застосувати")
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
