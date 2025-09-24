#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Анализ словарного запаса König Lear vs существующий словарь
Дата: 06.09.2025
Цель: Найти слова A2/B1 из текста, которых нет в словаре
"""
import re
import sys
from pathlib import Path
from collections import Counter

# Добавляем путь к проекту
sys.path.insert(0, str(Path(__file__).parent.parent))

# Импортируем словарь
from full_stress_dictionary_v2 import FULL_STRESS_DICTIONARY

# Слова A2 уровня, которые часто встречаются в König Lear
A2_CORE_WORDS = {
    # Существительные
    "Mann", "Frau", "Mensch", "Tag", "Nacht", "Morgen", "Abend",
    "Haus", "Zimmer", "Stadt", "Land", "Platz", "Ort",
    "Jahr", "Monat", "Woche", "Stunde", "Minute",
    "Arbeit", "Geld", "Zeit", "Problem", "Frage", "Antwort",
    "Freund", "Feind", "Person", "Leute", "Gruppe",
    "Hand", "Kopf", "Auge", "Ohr", "Mund", "Gesicht",
    "Brot", "Wasser", "Essen", "Trinken",
    "Kleid", "Hemd", "Hose", "Schuh",
    "Buch", "Papier", "Tisch", "Stuhl", "Bett",
    "Auto", "Zug", "Bus", "Straße", "Weg",
    
    # Глаголы
    "machen", "tun", "geben", "nehmen", "haben", "sein",
    "sagen", "fragen", "antworten", "denken", "wissen", "kennen",
    "arbeiten", "spielen", "lernen", "studieren", "lesen", "schreiben",
    "gehen", "kommen", "fahren", "laufen", "stehen", "sitzen",
    "essen", "trinken", "schlafen", "wachen", "aufstehen",
    "kaufen", "verkaufen", "zahlen", "kosten", "bezahlen",
    "beginnen", "anfangen", "aufhören", "beenden",
    "mögen", "wollen", "können", "müssen", "sollen", "dürfen",
    "helfen", "brauchen", "warten", "bleiben", "wohnen",
    "liegen", "zeigen", "bringen", "holen", "tragen",
    "öffnen", "schließen", "stellen", "legen", "setzen",
    
    # Прилагательные  
    "gut", "schlecht", "groß", "klein", "neu", "alt",
    "jung", "schön", "hässlich", "schnell", "langsam",
    "hoch", "niedrig", "lang", "kurz", "breit", "schmal",
    "dick", "dünn", "schwer", "leicht", "stark", "schwach",
    "warm", "kalt", "heiß", "kühl", "trocken", "nass",
    "sauber", "schmutzig", "hell", "dunkel", "laut", "leise",
    "reich", "arm", "teuer", "billig", "voll", "leer",
    "richtig", "falsch", "einfach", "schwierig", "wichtig",
    "nah", "fern", "früh", "spät", "oft", "selten",
    
    # Другие важные слова
    "hier", "dort", "jetzt", "dann", "heute", "morgen",
    "gestern", "immer", "nie", "oft", "manchmal", "wieder",
    "sehr", "viel", "wenig", "mehr", "weniger", "alle",
    "jeder", "einige", "viele", "beide", "kein", "nichts",
    "etwas", "alles", "jemand", "niemand", "man",
    "und", "oder", "aber", "weil", "wenn", "dass",
    "mit", "ohne", "für", "gegen", "bei", "nach", "vor",
    "in", "auf", "unter", "über", "zwischen", "neben"
}

# Слова B1 уровня из König Lear
B1_CORE_WORDS = {
    # Существительные
    "Gedanke", "Gefühl", "Meinung", "Idee", "Vorschlag",
    "Erfolg", "Misserfolg", "Fortschritt", "Entwicklung",
    "Beziehung", "Verhältnis", "Kontakt", "Verbindung",
    "Gesellschaft", "Umgebung", "Umwelt", "Situation",
    "Ereignis", "Erlebnis", "Abenteuer", "Geschichte",
    "Gesundheit", "Krankheit", "Schmerz", "Medizin",
    "Ausbildung", "Beruf", "Karriere", "Erfahrung",
    "Kunst", "Kultur", "Musik", "Theater", "Film",
    "Politik", "Wirtschaft", "Handel", "Geschäft",
    "Natur", "Landschaft", "Berg", "Tal", "Fluss", "See",
    "Wetter", "Klima", "Jahreszeit", "Temperatur",
    "Regel", "Gesetz", "Recht", "Pflicht", "Freiheit",
    
    # Глаголы
    "bedeuten", "erklären", "beschreiben", "erzählen",
    "verstehen", "begreifen", "erkennen", "bemerken",
    "entscheiden", "wählen", "vorschlagen", "empfehlen",
    "versprechen", "erwarten", "hoffen", "befürchten",
    "erlauben", "verbieten", "zwingen", "vermeiden",
    "entwickeln", "verbessern", "verändern", "wachsen",
    "erreichen", "schaffen", "gelingen", "scheitern",
    "untersuchen", "prüfen", "kontrollieren", "beobachten",
    "beschweren", "kritisieren", "loben", "danken",
    "einladen", "besuchen", "empfangen", "verabschieden",
    "organisieren", "planen", "vorbereiten", "durchführen",
    "benutzen", "verwenden", "gebrauchen", "nutzen",
    
    # Прилагательные
    "notwendig", "wichtig", "unwichtig", "nützlich", "praktisch",
    "möglich", "unmöglich", "wahrscheinlich", "sicher", "unsicher",
    "typisch", "normal", "gewöhnlich", "außergewöhnlich", "besonders",
    "modern", "altmodisch", "traditionell", "klassisch",
    "öffentlich", "privat", "persönlich", "gemeinsam",
    "zufrieden", "unzufrieden", "glücklich", "unglücklich",
    "stolz", "bescheiden", "höflich", "unhöflich", "freundlich",
    "müde", "wach", "gesund", "krank", "fit",
    "bekannt", "unbekannt", "berühmt", "beliebt",
    "aktiv", "passiv", "fleißig", "faul", "ordentlich",
    "deutlich", "klar", "unklar", "genau", "ungefähr"
}

def extract_words_from_lear():
    """Извлечь все немецкие слова из текста König Lear"""
    # Здесь был бы текст из документа, но для демонстрации используем образец
    sample_text = """
    König Lear will das Reich unter seinen drei Töchtern aufteilen.
    Er verlangt einen Liebesbeweis. Goneril und Regan heucheln Liebe.
    Cordelia verweigert das Loyalitätsbekenntnis. Lear enterbt sie.
    Die Schwestern verfallen der Gier nach Macht. Sie verstoßen den Vater.
    Mit seinem Narren zieht Lear in den Sturm hinaus.
    Edgar versteckt sich als Bettler. Edmund plant Verrat.
    Am Ende sterben viele. Die Tragödie endet mit Tod und Trauer.
    """
    
    # Извлекаем все слова
    words = re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]+\b|\b[a-zäöüß]+\b', sample_text)
    return words

def analyze_missing_words():
    """Анализ слов, которых нет в словаре"""
    
    # Получаем слова из словаря (без артиклей)
    dict_words = set()
    for key in FULL_STRESS_DICTIONARY.keys():
        # Убираем артикли
        word = key.replace("der ", "").replace("die ", "").replace("das ", "")
        dict_words.add(word.lower())
    
    print("[АНАЛИЗ СЛОВАРНОГО ЗАПАСА]")
    print("=" * 60)
    print(f"Слов в словаре: {len(FULL_STRESS_DICTIONARY)}")
    print(f"Уникальных слов (без артиклей): {len(dict_words)}")
    print()
    
    # Анализ A2 слов
    print("[A2 УРОВЕНЬ - ОТСУТСТВУЮЩИЕ СЛОВА]")
    print("-" * 40)
    
    a2_missing = {
        "Базовые существительные": [],
        "Базовые глаголы": [],
        "Базовые прилагательные": [],
        "Время и место": [],
        "Люди и отношения": []
    }
    
    for word in A2_CORE_WORDS:
        if word.lower() not in dict_words:
            # Категоризация
            if word in ["Mann", "Frau", "Mensch", "Kind", "Leute", "Person"]:
                a2_missing["Люди и отношения"].append(word)
            elif word in ["Tag", "Nacht", "Morgen", "Abend", "Jahr", "Monat", "Woche", "Stunde",
                         "hier", "dort", "jetzt", "dann", "heute", "morgen", "gestern"]:
                a2_missing["Время и место"].append(word)
            elif word in ["machen", "tun", "geben", "nehmen", "haben", "sein", "sagen", "fragen",
                         "denken", "wissen", "kennen", "helfen", "brauchen", "warten"]:
                a2_missing["Базовые глаголы"].append(word)
            elif word in ["gut", "schlecht", "groß", "klein", "neu", "jung", "schön", "schnell",
                         "hoch", "lang", "stark", "warm", "richtig", "einfach", "wichtig"]:
                a2_missing["Базовые прилагательные"].append(word)
            else:
                a2_missing["Базовые существительные"].append(word)
    
    for category, words in a2_missing.items():
        if words:
            print(f"\n{category}: ({len(words)} слов)")
            for i, word in enumerate(words[:10]):  # Показываем первые 10
                print(f"  - {word}")
            if len(words) > 10:
                print(f"  ... и еще {len(words) - 10} слов")
    
    # Анализ B1 слов
    print("\n[B1 УРОВЕНЬ - ОТСУТСТВУЮЩИЕ СЛОВА]")
    print("-" * 40)
    
    b1_missing = {
        "Абстрактные понятия": [],
        "Эмоции и чувства": [],
        "Действия и процессы": [],
        "Описательные слова": [],
        "Общество и культура": []
    }
    
    for word in B1_CORE_WORDS:
        if word.lower() not in dict_words:
            # Категоризация
            if word in ["Gedanke", "Gefühl", "Meinung", "Idee", "Vorschlag", "Erfolg", "Misserfolg"]:
                b1_missing["Абстрактные понятия"].append(word)
            elif word in ["zufrieden", "unzufrieden", "glücklich", "stolz", "müde", "wach"]:
                b1_missing["Эмоции и чувства"].append(word)
            elif word in ["bedeuten", "erklären", "beschreiben", "entwickeln", "verbessern", "verändern"]:
                b1_missing["Действия и процессы"].append(word)
            elif word in ["notwendig", "möglich", "wahrscheinlich", "typisch", "modern", "öffentlich"]:
                b1_missing["Описательные слова"].append(word)
            else:
                b1_missing["Общество и культура"].append(word)
    
    for category, words in b1_missing.items():
        if words:
            print(f"\n{category}: ({len(words)} слов)")
            for i, word in enumerate(words[:10]):  # Показываем первые 10
                print(f"  - {word}")
            if len(words) > 10:
                print(f"  ... и еще {len(words) - 10} слов")
    
    # Подсчет общей статистики
    total_a2_missing = sum(len(words) for words in a2_missing.values())
    total_b1_missing = sum(len(words) for words in b1_missing.values())
    
    print("\n[ИТОГОВАЯ СТАТИСТИКА]")
    print("=" * 60)
    print(f"A2 слов отсутствует: {total_a2_missing}")
    print(f"B1 слов отсутствует: {total_b1_missing}")
    print(f"Всего нужно добавить: {total_a2_missing + total_b1_missing}")
    
    # Рекомендации
    print("\n[РЕКОМЕНДАЦИИ]")
    print("-" * 40)
    print("1. Приоритет A2: Добавить базовые глаголы (machen, tun, geben)")
    print("2. Приоритет A2: Добавить слова времени (Tag, Nacht, Morgen)")
    print("3. Приоритет B1: Добавить абстрактные понятия (Gedanke, Gefühl)")
    print("4. Приоритет B1: Добавить глаголы коммуникации (bedeuten, erklären)")
    
    # Специфичные для König Lear тематические группы
    print("\n[ТЕМАТИЧЕСКИЕ ГРУППЫ ИЗ KÖNIG LEAR]")
    print("-" * 40)
    
    lear_themes = {
        "Семейные отношения": [
            "Eltern", "Kinder", "Geschwister", "Erziehung", "Generation",
            "Verwandtschaft", "Abstammung", "Nachkomme"
        ],
        "Власть и правление": [
            "Regierung", "Thronfolge", "Untertan", "Befehl", "Gehorsam",
            "Autorität", "Kontrolle", "Einfluss"
        ],
        "Предательство и обман": [
            "Betrug", "Täuschung", "List", "Falschheit", "Hinterlist",
            "Intrige", "Komplott", "Verschwörung"
        ],
        "Безумие и разум": [
            "Verrücktheit", "Geisteskrankheit", "Klarheit", "Verwirrung",
            "Halluzination", "Realität", "Traum"
        ],
        "Природа и стихии": [
            "Gewitter", "Blitz", "Donner", "Regen", "Wind", "Sturm",
            "Kälte", "Dunkelheit", "Wildnis"
        ]
    }
    
    for theme, words in lear_themes.items():
        missing = [w for w in words if w.lower() not in dict_words]
        if missing:
            print(f"\n{theme}: ({len(missing)} слов нужно добавить)")
            for word in missing[:5]:
                print(f"  - {word}")

if __name__ == "__main__":
    analyze_missing_words()
