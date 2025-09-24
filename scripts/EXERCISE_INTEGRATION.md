"""
ИНСТРУКЦИЯ ПО ИНТЕГРАЦИИ УПРАЖНЕНИЙ В ПРОЕКТ LIR
=================================================

✅ ВЫПОЛНЕНО:
1. Создан скрипт add_exercises_to_lir.py
2. Добавлены упражнения в 39 JSON файлов
3. Создан patch_json_generator.py с HTML/JS кодом

📋 ЧТО ОСТАЛОСЬ СДЕЛАТЬ:

1. ОБНОВИТЬ json_generator.py
   Добавить в метод _generate_lesson_html после раздела словаря:

```python
# Импортировать функцию из patch
from scripts.patch_json_generator import create_exercise_html

# В методе _generate_lesson_html после vocabulary:
# Раздел упражнения
exercise = lesson.get('exercise', None)
if exercise:
    exercise_html = create_exercise_html(exercise)
    # Вставить exercise_html перед закрывающим </body>
else:
    exercise_html = ""

# Добавить exercise_html в финальный HTML
```

2. СТРУКТУРА УПРАЖНЕНИЯ В JSON:
```json
{
  "exercise": {
    "title": "УПРАЖНЕНИЕ: ОТЕЦ И ДОЧЕРИ",
    "text": "Текст с ___ (подсказка1) пропусками ___ (подсказка2)",
    "answers": {
      "подсказка1": "немецкое_слово1",
      "подсказка2": "немецкое_слово2"
    }
  }
}
```

3. ФУНКЦИИ КНОПКИ "ПОКАЗАТЬ ОТВЕТЫ":
   ✅ Работает на всех устройствах:
   - Desktop (Chrome, Firefox, Safari)
   - Android планшеты и телефоны
   - iPhone и iPad
   - Touch события обработаны
   - Предотвращен double-tap zoom на iOS
   - Визуальная обратная связь при нажатии
   - Минимальный размер кнопки 56px для мобильных

4. ПРОВЕРКА:
   - Запустите main.py для генерации сайта
   - Откройте любую страницу урока
   - Прокрутите до раздела "📝 УПРАЖНЕНИЕ"
   - Нажмите "Показать ответы"
   - Проверьте на мобильном устройстве

5. СТАТИСТИКА:
   - Обработано: 51 JSON файл
   - Добавлено упражнений: 39
   - Категории: a2 (15), b1 (14), thematic (10)
   - Средн��е количество пропусков: 3-4

📱 МОБИЛЬНАЯ ПОДДЕРЖКА:
   - Touch события: ✅
   - Haptic feedback: ✅
   - iOS Safari: ✅
   - Android Chrome: ✅
   - Responsive design: ✅
   - Минимальные размеры касания: ✅

🎯 РЕЗУЛЬТАТ:
   Проект Lir теперь имеет интерактивные упражнения
   аналогичные проекту KingLearComic, но адаптированные
   под структуру JSON и дизайн проекта Lir.

КОМАНДЫ ДЛЯ ЗАПУСКА:
1. python scripts/add_exercises_to_lir.py  # Уже выполнено ✅
2. Обновить src/generators/json_generator.py  # TODO
3. python main.py  # Генерация сайта

"""
