"""
Улучшенная версия - ВСЕГДА добавляет упражнения ко всем урокам Lir
Если нет story/dialogues, создает упражнение из vocabulary
"""
import json
import re
from pathlib import Path
import random

def extract_words_from_vocabulary(vocabulary):
    """Извлекает слова из словаря урока"""
    words_dict = {}
    
    for word_data in vocabulary:
        german = word_data.get('german', '')
        translation = word_data.get('translation', '')
        
        if german and translation:
            # Убираем артикли для глаголов
            clean_german = german
            if word_data.get('type') == 'глагол':
                clean_german = german
            elif word_data.get('type') == 'существительное':
                # Оставляем артикль для существительных
                clean_german = german
            
            words_dict[translation.lower()] = clean_german
    
    return words_dict

def create_simple_exercise_from_vocabulary(vocabulary):
    """
    Создает простое упражнение из словаря
    ВСЕГДА возвращает упражнение, даже если мало слов
    """
    words = extract_words_from_vocabulary(vocabulary)
    
    if not words:
        # Если словаря нет, создаем минимальное упражнение
        return {
            'text': 'Изучите слова этого урока и попробуйте составить с ними предложения на немецком языке.',
            'answers': {}
        }
    
    # Берем первые 5-8 слов для упражнения
    word_items = list(words.items())[:8]
    
    # Создаем текст упражнения
    exercise_sentences = []
    answers = {}
    
    # Генерируем простые предложения с пропусками
    templates = [
        "Das ist ___ ({}).",
        "Ich habe ___ ({}).",
        "Wo ist ___ ({})?",
        "Er sagt: ___ ({})!",
        "Sie braucht ___ ({}).",
        "Wir sehen ___ ({}).",
        "Das war ___ ({}).",
        "Hier ist ___ ({})."
    ]
    
    for i, (rus_word, ger_word) in enumerate(word_items):
        if i < len(templates):
            sentence = templates[i].format(rus_word)
            exercise_sentences.append(sentence)
            answers[rus_word] = ger_word
    
    # Если слов мало, добавляем общую фразу
    if len(answers) < 3:
        exercise_sentences.append("Повторите слова: " + ", ".join([f"___ ({r})" for r, g in word_items[:3]]))
        for r, g in word_items[:3]:
            answers[r] = g
    
    return {
        'text': ' '.join(exercise_sentences),
        'answers': answers
    }

def create_exercise_from_dialogues(dialogues, vocab_words):
    """Создает упражнение из диалогов"""
    if not dialogues:
        return None
    
    exercise_lines = []
    answers = {}
    
    for dialogue in dialogues[:3]:  # Берем первые 3 диалога
        character = dialogue.get('character', 'Персонаж')
        russian = dialogue.get('russian', '')
        german = dialogue.get('german', '')
        
        if not russian or not german:
            continue
        
        # Ищем слова которые можем заменить на пропуски
        words_replaced = 0
        modified_text = russian
        
        for rus_word, ger_word in vocab_words.items():
            if rus_word in russian.lower() and words_replaced < 2:
                placeholder = f"___ ({rus_word})"
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
        'text': ' '.join(exercise_lines),
        'answers': answers
    }

def create_exercise_from_story(story_data, vocab_words):
    """Создает упражнение из истории"""
    content = story_data.get('content', '')
    if not content:
        narrative = story_data.get('narrative', '')
        if narrative:
            content = narrative
    
    if not content:
        return None
    
    # Берем первые несколько предложений
    sentences = content.split('.')[:5]
    exercise_text = '. '.join(sentences) + '.'
    answers = {}
    
    # Заменяем ключевые слова на пропуски
    words_to_replace = list(vocab_words.items())[:8]
    
    for rus_word, ger_word in words_to_replace:
        if rus_word in exercise_text.lower():
            placeholder = f"___ ({rus_word})"
            pattern = re.compile(re.escape(rus_word), re.IGNORECASE)
            if pattern.search(exercise_text):
                exercise_text = pattern.sub(placeholder, exercise_text, count=1)
                answers[rus_word] = ger_word
    
    if not answers:
        return None
    
    return {
        'text': exercise_text,
        'answers': answers
    }

def process_json_file(json_path):
    """
    Обрабатывает один JSON файл и добавляет упражнение
    ВСЕГДА добавляет упражнение, даже если данных мало
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Проверяем, есть ли уже упражнение
    if 'exercise' in data:
        print(f"  [SKIP] Упражнение уже существует")
        return False
    
    # Извлекаем слова из словаря
    vocabulary = data.get('vocabulary', [])
    vocab_words = extract_words_from_vocabulary(vocabulary)
    
    # Пробуем создать упражнение разными способами
    exercise = None
    
    # 1. Пробуем из диалогов
    dialogues = data.get('dialogues', [])
    if dialogues and vocab_words:
        exercise = create_exercise_from_dialogues(dialogues, vocab_words)
    
    # 2. Если не получилось, пробуем из истории
    if not exercise:
        story = data.get('story', {})
        if story and vocab_words:
            exercise = create_exercise_from_story(story, vocab_words)
    
    # 3. Если все еще нет упражнения, создаем из словаря
    # ЭТО ГАРАНТИРУЕТ, что упражнение ВСЕГДА будет создано
    if not exercise:
        exercise = create_simple_exercise_from_vocabulary(vocabulary)
    
    # Добавляем заголовок
    title = data.get('title', 'Упражнение')
    # Убираем эмодзи и номер из заголовка
    clean_title = re.sub(r'📚\s*СЦЕНА\s*\d+:\s*', '', title)
    clean_title = re.sub(r'[📚🎭💬📌]\s*', '', clean_title)
    
    data['exercise'] = {
        'title': f"УПРАЖНЕНИЕ: {clean_title}",
        'text': exercise['text'],
        'answers': exercise['answers']
    }
    
    # Сохраняем обновленный JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    answers_count = len(exercise['answers'])
    if answers_count > 0:
        print(f"  [OK] Добавлено упражнение с {answers_count} пропусками")
    else:
        print(f"  [OK] Добавлено упражнение (общее задание)")
    return True

def main():
    """Обрабатывает все JSON файлы в проекте Lir"""
    print("=" * 60)
    print("ДОБАВЛЕНИЕ УПРАЖНЕНИЙ В ПРОЕКТ LIR (v2.0)")
    print("=" * 60)
    
    base_dir = Path(r'F:\AiKlientBank\Lir\data')
    categories = ['a2', 'b1', 'thematic']
    
    total_processed = 0
    total_exercises = 0
    failed_files = []
    
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
                failed_files.append(str(json_file))
    
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ:")
    print(f"  Обработано файлов: {total_processed}")
    print(f"  Добавлено упражнений: {total_exercises}")
    
    if failed_files:
        print(f"\nФайлы с ошибками:")
        for f in failed_files:
            print(f"  - {f}")
    
    print("=" * 60)
    
    if total_exercises > 0:
        print("\n[SUCCESS] Упражнения добавлены!")
        print("[INFO] Теперь ВСЕ файлы должны иметь упражнения")
    else:
        print("\n[INFO] Новых упражнений не добавлено")

if __name__ == "__main__":
    main()
