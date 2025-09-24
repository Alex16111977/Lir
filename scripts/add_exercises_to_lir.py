"""
Добавление упражнений ко всем урокам Lir
Генерирует упражнения из story и dialogues
"""
import json
import re
from pathlib import Path
import random

def extract_german_words_from_story(story_data):
    """
    Извлекает немецкие слова из истории
    Ищет паттерны вида: **слово** или <strong>слово</strong>
    """
    words_found = {}
    
    narrative = story_data.get('narrative', '')
    if not narrative:
        return words_found
    
    # Паттерны для поиска выделенных слов
    patterns = [
        r'\*\*([^*]+)\*\*',  # **слово**
        r'<strong>([^<]+)</strong>',  # <strong>слово</strong>
        r'<b>([^<]+)</b>',  # <b>слово</b>
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, narrative)
        for match in matches:
            # Разделяем немецкое и русское если есть скобки
            if '(' in match and ')' in match:
                parts = match.split('(')
                german = parts[0].strip()
                russian = parts[1].replace(')', '').strip()
                words_found[russian] = german
            else:
                # Используем само слово как ключ
                words_found[match.lower()] = match
    
    return words_found

def extract_words_from_vocabulary(vocabulary):
    """
    Извлекает слова из словаря урока
    """
    words_dict = {}
    
    for word_data in vocabulary:
        german = word_data.get('german', '')
        translation = word_data.get('translation', '')
        
        if german and translation:
            # Убираем артикли для глаголов и прилагательных
            clean_german = german
            if word_data.get('type') == 'глагол':
                clean_german = german
            elif word_data.get('type') == 'существительное':
                # Оставляем артикль для существительных
                clean_german = german
            
            words_dict[translation.lower()] = clean_german
    
    return words_dict

def create_exercise_from_dialogues(dialogues, vocab_words):
    """
    Создает упражнение из диалогов
    """
    if not dialogues:
        return None
    
    exercise_lines = []
    answers = {}
    
    for dialogue in dialogues[:3]:  # Берем первые 3 диалога
        character = dialogue.get('character', 'Персонаж')
        russian = dialogue.get('russian', '')
        
        if not russian:
            continue
        
        # Ищем слова которые можем заменить на пропуски
        words_replaced = 0
        modified_text = russian
        
        for rus_word, ger_word in vocab_words.items():
            if rus_word in russian.lower() and words_replaced < 2:
                # Создаем пропуск
                placeholder = f"___ ({rus_word})"
                # Заменяем слово на пропуск (с учетом регистра)
                pattern = re.compile(re.escape(rus_word), re.IGNORECASE)
                if pattern.search(modified_text):
                    modified_text = pattern.sub(placeholder, modified_text, count=1)
                    answers[rus_word] = ger_word
                    words_replaced += 1
        
        if words_replaced > 0:
            exercise_lines.append(f"{character}: «{modified_text}»")
    
    if not exercise_lines:
        return None
    
    return {
        "text": " ".join(exercise_lines),
        "answers": answers
    }

def create_exercise_from_story(story_data, vocab_words):
    """
    Создает упражнение из истории
    """
    narrative = story_data.get('narrative', '')
    if not narrative:
        return None
    
    # Берем часть текста для упражнения
    sentences = narrative.split('.')
    selected_sentences = sentences[:5]  # Первые 5 предложений
    
    exercise_text = '. '.join(selected_sentences) + '.'
    answers = {}
    
    # Заменяем ключевые слова на пропуски
    words_to_replace = list(vocab_words.items())[:8]  # Максимум 8 пропусков
    
    for rus_word, ger_word in words_to_replace:
        if rus_word in exercise_text.lower():
            placeholder = f"___ ({rus_word})"
            pattern = re.compile(re.escape(rus_word), re.IGNORECASE)
            if pattern.search(exercise_text):
                exercise_text = pattern.sub(placeholder, exercise_text, count=1)
                answers[rus_word] = ger_word
    
    if not answers:
        # Если не нашли слов, создаем упражнение с любыми словами из словаря
        for i, (rus_word, ger_word) in enumerate(words_to_replace[:5]):
            placeholder = f"___ ({rus_word})"
            exercise_text = exercise_text[:50*i] + placeholder + exercise_text[50*i+len(rus_word):]
            answers[rus_word] = ger_word
    
    return {
        "text": exercise_text,
        "answers": answers
    }

def process_json_file(json_path):
    """
    Обрабатывает один JSON файл и добавляет упражнение
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Извлекаем слова из словаря
    vocabulary = data.get('vocabulary', [])
    vocab_words = extract_words_from_vocabulary(vocabulary)
    
    # Извлекаем слова из истории
    story = data.get('story', {})
    story_words = extract_german_words_from_story(story)
    
    # Объединяем слова
    all_words = {**vocab_words, **story_words}
    
    if not all_words:
        print(f"  [SKIP] Нет слов для упражнения")
        return False
    
    # Создаем упражнение
    exercise = None
    
    # Пробуем создать из диалогов
    dialogues = data.get('dialogues', [])
    if dialogues:
        exercise = create_exercise_from_dialogues(dialogues, all_words)
    
    # Если не получилось, создаем из истории
    if not exercise and story:
        exercise = create_exercise_from_story(story, all_words)
    
    # Если есть упражнение, добавляем в JSON
    if exercise:
        # Добавляем заголовок
        title = data.get('title', 'Упражнение')
        # Убираем эмодзи и номер из заголовка
        clean_title = re.sub(r'📚\s*СЦЕНА\s*\d+:\s*', '', title)
        
        data['exercise'] = {
            'title': f"УПРАЖНЕНИЕ: {clean_title}",
            'text': exercise['text'],
            'answers': exercise['answers']
        }
        
        # Сохраняем обновленный JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"  [OK] Добавлено упражнение с {len(exercise['answers'])} пропусками")
        return True
    else:
        print(f"  [ERROR] Не удалось создать упражнение")
        return False

def main():
    """
    Обрабатывает все JSON файлы в проекте Lir
    """
    print("=" * 60)
    print("ДОБАВЛЕНИЕ УПРАЖНЕНИЙ В ПРОЕКТ LIR")
    print("=" * 60)
    
    base_dir = Path(r'F:\AiKlientBank\Lir\data')
    categories = ['a2', 'b1', 'thematic']
    
    total_processed = 0
    total_exercises = 0
    
    for category in categories:
        cat_dir = base_dir / category
        if not cat_dir.exists():
            print(f"\n[SKIP] Папка {category} не найдена")
            continue
        
        print(f"\n[CATEGORY] {category.upper()}")
        print("-" * 40)
        
        json_files = sorted(cat_dir.glob("*.json"))
        
        for json_file in json_files:
            print(f"\n[FILE] {json_file.name}")
            
            try:
                if process_json_file(json_file):
                    total_exercises += 1
                total_processed += 1
                
            except Exception as e:
                print(f"  [ERROR] {e}")
    
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ:")
    print(f"  Обработано файлов: {total_processed}")
    print(f"  Добавлено упражнений: {total_exercises}")
    print("=" * 60)
    
    if total_exercises > 0:
        print("\n[SUCCESS] Упражнения добавлены!")
        print("[NEXT] Обновите json_generator.py для отображения упражнений")
        print("[NEXT] Запустите main.py для генерации сайта")
    else:
        print("\n[WARNING] Упражнения не были добавлены")

if __name__ == "__main__":
    main()
