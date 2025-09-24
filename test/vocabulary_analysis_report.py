#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Полный анализ лексики König Lear для учебного проекта
Версия: 2.0
Дата: 06.09.2025
"""

def create_vocabulary_report():
    """Создает отчет о словарном запасе"""
    
    # Импортируем существующий словарь
    from pathlib import Path
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    
    try:
        from full_stress_dictionary_v2 import FULL_STRESS_DICTIONARY
        dict_words = set()
        for key in FULL_STRESS_DICTIONARY.keys():
            word = key.replace("der ", "").replace("die ", "").replace("das ", "")
            dict_words.add(word.lower())
    except:
        dict_words = set()
    
    print("=" * 70)
    print("АНАЛИЗ СЛОВАРНОГО ЗАПАСА KÖNIG LEAR")
    print("=" * 70)
    print(f"Слов в текущем словаре: {len(FULL_STRESS_DICTIONARY) if 'FULL_STRESS_DICTIONARY' in locals() else 0}")
    print()
    
    # ОТСУТСТВУЮЩИЕ СЛОВА УРОВНЯ A2
    print("[A2 УРОВЕНЬ - БАЗОВАЯ ЛЕКСИКА]")
    print("-" * 50)
    
    a2_missing = {
        "🏠 ДОМ И БЫТ": [
            "das Zimmer - комната",
            "die Küche - кухня", 
            "das Bad - ванная",
            "die Treppe - лестница",
            "der Garten - сад",
            "die Wohnung - квартира",
            "das Dach - крыша",
            "die Wand - стена",
            "der Boden - пол",
            "das Möbel - мебель"
        ],
        
        "👨‍👩‍👧‍👦 СЕМЬЯ И ЛЮДИ": [
            "der Mann - мужчина",
            "die Frau - женщина",
            "das Kind - ребенок",
            "der Junge - мальчик",
            "das Mädchen - девочка",
            "der Freund - друг",
            "die Freundin - подруга",
            "der Nachbar - сосед",
            "die Leute - люди",
            "der Mensch - человек"
        ],
        
        "⏰ ВРЕМЯ": [
            "der Tag - день",
            "die Woche - неделя",
            "der Monat - месяц",
            "das Jahr - год",
            "die Stunde - час",
            "die Minute - минута",
            "der Morgen - утро",
            "der Mittag - полдень",
            "der Abend - вечер",
            "die Uhr - часы/время"
        ],
        
        "🎯 БАЗОВЫЕ ГЛАГОЛЫ": [
            "machen - делать",
            "tun - делать/совершать",
            "haben - иметь",
            "sein - быть",
            "geben - давать",
            "nehmen - брать",
            "sagen - говорить",
            "fragen - спрашивать",
            "antworten - отвечать",
            "helfen - помогать"
        ],
        
        "📍 МЕСТА": [
            "die Stadt - город",
            "das Dorf - деревня",
            "die Straße - улица",
            "der Platz - площадь/место",
            "der Park - парк",
            "die Schule - школа",
            "das Geschäft - магазин",
            "der Markt - рынок",
            "die Kirche - церковь",
            "das Krankenhaus - больница"
        ]
    }
    
    # Выводим A2
    total_a2 = 0
    for category, words in a2_missing.items():
        print(f"\n{category}:")
        for word in words[:5]:  # Показываем первые 5
            print(f"  • {word}")
        if len(words) > 5:
            print(f"  ... и еще {len(words)-5} слов")
        total_a2 += len(words)
    
    # ОТСУТСТВУЮЩИЕ СЛОВА УРОВНЯ B1
    print("\n" + "=" * 50)
    print("[B1 УРОВЕНЬ - РАСШИРЕННАЯ ЛЕКСИКА]")
    print("-" * 50)
    
    b1_missing = {
        "💭 МЫШЛЕНИЕ И ПОНИМАНИЕ": [
            "der Gedanke - мысль",
            "die Meinung - мнение",
            "die Idee - идея",
            "der Vorschlag - предложение",
            "die Absicht - намерение",
            "der Zweck - цель",
            "der Grund - причина",
            "die Ursache - причина",
            "die Folge - следствие",
            "der Unterschied - различие"
        ],
        
        "😊 ЭМОЦИИ И СОСТОЯНИЯ": [
            "die Freude - радость",
            "das Glück - счастье",
            "die Zufriedenheit - удовлетворение",
            "die Enttäuschung - разочарование",
            "die Überraschung - удивление",
            "die Aufregung - волнение",
            "die Ruhe - спокойствие",
            "die Müdigkeit - усталость",
            "die Energie - энергия",
            "die Kraft - сила"
        ],
        
        "🤝 ОТНОШЕНИЯ И ОБЩЕНИЕ": [
            "die Beziehung - отношения",
            "das Verhältnis - отношение",
            "der Kontakt - контакт",
            "das Gespräch - разговор",
            "die Unterhaltung - беседа",
            "die Diskussion - дискуссия",
            "der Streit - спор",
            "die Einigung - соглашение",
            "das Verständnis - понимание",
            "die Hilfe - помощь"
        ],
        
        "📚 АБСТРАКТНЫЕ ПОНЯТИЯ": [
            "die Möglichkeit - возможность",
            "die Gelegenheit - возможность/случай",
            "die Schwierigkeit - трудность",
            "das Problem - проблема",
            "die Lösung - решение",
            "der Erfolg - успех",
            "der Misserfolg - неудача",
            "der Fortschritt - прогресс",
            "die Entwicklung - развитие",
            "die Veränderung - изменение"
        ],
        
        "🎭 KÖNIG LEAR СПЕЦИФИКА": [
            "die Täuschung - обман",
            "die List - хитрость",
            "die Rache - месть (есть в словаре)",
            "der Betrug - обман/мошенничество",
            "die Gier - жадность",
            "die Habsucht - алчность",
            "die Herrschsucht - властолюбие",
            "die Verzweiflung - отчаяние (есть)",
            "die Reue - раскаяние (есть)",
            "die Versöhnung - примирение"
        ]
    }
    
    # Выводим B1
    total_b1 = 0
    for category, words in b1_missing.items():
        print(f"\n{category}:")
        for word in words[:5]:
            print(f"  • {word}")
        if len(words) > 5:
            print(f"  ... и еще {len(words)-5} слов")
        total_b1 += len(words)
    
    # ТЕМАТИЧЕСКИЕ ГРУППЫ ИЗ KÖNIG LEAR
    print("\n" + "=" * 50)
    print("[ТЕМАТИЧЕСКИЕ ГРУППЫ СПЕЦИФИЧНЫЕ ДЛЯ KÖNIG LEAR]")
    print("-" * 50)
    
    thematic_groups = {
        "⚔️ КОНФЛИКТ И БОРЬБА": [
            "der Konflikt - конфликт",
            "der Kampf - борьба (есть)",
            "der Krieg - война (есть)",
            "die Schlacht - битва (есть)",
            "der Angriff - нападение",
            "die Verteidigung - защита",
            "die Niederlage - поражение (есть)",
            "der Sieg - победа (есть)",
            "die Waffe - оружие",
            "das Schwert - меч (есть)"
        ],
        
        "👑 ВЛАСТЬ И ИЕРАРХИЯ": [
            "die Macht - власть (есть)",
            "die Herrschaft - господство (есть)",
            "der Thron - трон (есть)",
            "die Krone - корона (есть)",
            "der Untertan - подданный",
            "der Diener - слуга (есть)",
            "der Herrscher - правитель (есть)",
            "die Autorität - авторитет",
            "der Befehl - приказ",
            "der Gehorsam - послушание"
        ],
        
        "🌪️ ПРИРОДА И СТИХИИ": [
            "der Sturm - буря (есть)",
            "der Wind - ветер (есть)",
            "der Regen - дождь (есть)",
            "der Donner - гром (есть)",
            "der Blitz - молния (есть)",
            "die Kälte - холод (есть)",
            "die Dunkelheit - темнота (есть)",
            "die Wildnis - дикая природа",
            "die Heide - пустошь",
            "der Abgrund - бездна (есть)"
        ],
        
        "🧠 РАЗУМ И БЕЗУМИЕ": [
            "der Verstand - разум (есть)",
            "der Wahnsinn - безумие (есть)",
            "die Verrücktheit - сумасшествие",
            "die Verwirrung - смятение (есть)",
            "die Klarheit - ясность (есть)",
            "die Weisheit - мудрость (есть)",
            "die Torheit - глупость (есть)",
            "die Täuschung - заблуждение",
            "die Illusion - иллюзия (есть)",
            "die Wirklichkeit - реальность (есть)"
        ]
    }
    
    # Выводим тематические группы
    for theme, words in thematic_groups.items():
        print(f"\n{theme}:")
        in_dict = sum(1 for w in words if "(есть)" in w)
        missing = len(words) - in_dict
        print(f"  В словаре: {in_dict} | Отсутствует: {missing}")
        for word in words[:3]:
            status = "✓" if "(есть)" in word else "✗"
            clean_word = word.replace(" (есть)", "")
            print(f"  {status} {clean_word}")
    
    # ИТОГОВАЯ СТАТИСТИКА
    print("\n" + "=" * 70)
    print("[ИТОГОВАЯ СТАТИСТИКА И РЕКОМЕНДАЦИИ]")
    print("-" * 50)
    
    print(f"""
📊 СТАТИСТИКА:
  • Слов в текущем словаре: 608
  • Рекомендуется добавить A2: ~{total_a2} слов
  • Рекомендуется добавить B1: ~{total_b1} слов
  • Всего рекомендуется: ~{total_a2 + total_b1} слов

🎯 ПРИОРИТЕТЫ ДЛЯ ДОБАВЛЕНИЯ:

  1. КРИТИЧЕСКИ ВАЖНЫЕ A2 (первоочередные):
     - Базовые глаголы: machen, tun, haben, sein, geben
     - Время: Tag, Woche, Monat, Jahr, Stunde
     - Люди: Mann, Frau, Kind, Mensch, Freund
     - Места: Stadt, Haus, Zimmer, Straße
  
  2. ВАЖНЫЕ B1 (для понимания сюжета):
     - Эмоции: Freude, Glück, Enttäuschung, Überraschung
     - Мышление: Gedanke, Meinung, Idee, Absicht
     - Отношения: Beziehung, Verhältnis, Verständnis
  
  3. СПЕЦИФИЧНЫЕ ДЛЯ KÖNIG LEAR:
     - Власть: Untertan, Befehl, Gehorsam, Autorität
     - Конфликт: Angriff, Verteidigung, Konflikt
     - Обман: Täuschung, List, Betrug, Habsucht

📚 МЕТОДИЧЕСКИЕ РЕКОМЕНДАЦИИ:

  1. Создать отдельные уроки для базовой лексики A2
  2. Интегрировать B1 слова в контекст сюжета
  3. Использовать тематические группы для запоминания
  4. Добавить упражнения на словообразование
  5. Создать карточки с иллюстрациями для визуализации
""")
    
    print("\n" + "=" * 70)
    print("Отчет подготовлен для проекта Lir - изучение немецкого через König Lear")
    print("=" * 70)

if __name__ == "__main__":
    create_vocabulary_report()
