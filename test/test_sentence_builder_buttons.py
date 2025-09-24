"""
Тест: Перевірка оновленого конструктора речень
Дата: 2025-09-24
Мета: Тестування індивідуальних кнопок підказок та перевірки
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.generators.exercises_generator import ExercisesGenerator


def test_sentence_builder_buttons():
    generator = ExercisesGenerator()

    test_dialogues = [
        {
            "german": "Bindet den Verräter! Seine Augen werden die Rache sehen!",
            "russian": "Свяжите предателя! Его глаза увидят месть!",
        }
    ]

    test_vocabulary = [
        {
            "german": "die Augen",
            "translation": "глаза",
            "character_voice": {
                "german": "Aus mit seinen Augen!",
                "russian": "Вырвать его глаза!",
            },
        },
        {
            "german": "der Verräter",
            "translation": "предатель",
            "character_voice": {
                "german": "Du Verräter!",
                "russian": "Ты предатель!",
            },
        },
    ]

    html = generator._generate_sentence_builder(test_dialogues, None, test_vocabulary)

    assert 'hint-btn' in html, "[FAIL] Кнопка підказки не знайдена"
    assert 'check-sentence-btn' in html, "[FAIL] Кнопка перевірки не знайдена"
    assert 'sentence-controls' in html, "[FAIL] Контейнер контролів не знайдений"
    assert 'showHint' in html, "[FAIL] Атрибут showHint не знайдено"
    assert 'checkSentence' in html, "[FAIL] Атрибут checkSentence не знайдено"
    assert html.count('class="sentence-builder"') == len(test_vocabulary), (
        "[FAIL] Кількість речень не відповідає кількості слів"
    )

    print("[OK] Всі перевірки для конструктора речень пройдено успішно!")
    print(f"[INFO] HTML містить {html.count('hint-btn')} кнопок підказок")
    print(f"[INFO] HTML містить {html.count('check-sentence-btn')} кнопок перевірки")
    print(
        f"[INFO] Вправа генерує {html.count('class=\"sentence-builder\"')} речень для {len(test_vocabulary)} слів"
    )


if __name__ == "__main__":  # pragma: no cover
    test_sentence_builder_buttons()
