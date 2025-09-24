"""
Тест миттєвої перевірки артиклів
Дата: 2025-09-06
Мета: Перевірка що вправа "Артикли и род" працює без кнопки "Проверить"
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generators.exercises_generator import ExercisesGenerator
from src.generators.exercises_assets import ExercisesAssetsGenerator

print("[TEST] Генерація вправи з артиклями...")

# Тестові дані
test_vocab = [
    {"german": "der Tisch", "translation": "стіл"},
    {"german": "die Katze", "translation": "кішка"},  
    {"german": "das Haus", "translation": "дім"},
    {"german": "der Stuhl", "translation": "стілець"},
    {"german": "die Blume", "translation": "квітка"},
    {"german": "das Buch", "translation": "книга"}
]

# Генеруємо вправу
gen = ExercisesGenerator()
html = gen._generate_articles(test_vocab)

# Перевірки
assert "check-btn" not in html, "[ERROR] Кнопка 'Проверить' не видалена!"
assert "onclick=" in html, "[ERROR] onclick обробники не додано!"
assert "checkArticleInstant" in html, "[ERROR] Функція checkArticleInstant не викликається!"
assert "articles-progress" in html, "[ERROR] Прогрес-бар не додано!"
assert "articles-total" in html, "[ERROR] Лічильник total не додано!"
assert "articles-correct" in html, "[ERROR] Лічильник correct не додано!"

print("[OK] Всі перевірки пройдено!")
print("[OK] HTML містить onclick обробники")
print("[OK] Кнопка 'Проверить' видалена") 
print("[OK] Прогрес-бар додано")

# Генеруємо CSS та JS
assets_gen = ExercisesAssetsGenerator()
css = assets_gen.generate_css()
js = assets_gen.generate_js()

# Перевіряємо CSS
assert "articles-progress" in css, "[ERROR] CSS для прогрес-бару не додано!"
assert "article-item.completed" in css, "[ERROR] CSS для completed не додано!"
assert "@keyframes shake" in css, "[ERROR] Анімація shake не додана!"

print("[OK] CSS стилі додано")

# Перевіряємо JS
assert "checkArticleInstant" in js, "[ERROR] JS функція checkArticleInstant не додана!"
assert "articlesAnswered" in js, "[ERROR] Лічильник articlesAnswered не додано!"
assert "updateArticlesProgress" in js, "[ERROR] Функція updateArticlesProgress не додана!"

print("[OK] JavaScript логіка додана")

# Виводимо початок HTML для візуальної перевірки
print("\n[HTML PREVIEW]")
print(html[:500])
print("...")

print("\n[SUCCESS] Вправа 'Артикли и род' успішно модифікована!")
print("- Кнопка 'Проверить' видалена")
print("- onclick обробники додано до кнопок")
print("- Прогрес-бар з лічильником додано")  
print("- CSS стилі для візуальної реакції додано")
print("- JavaScript для миттєвої перевірки додано")
