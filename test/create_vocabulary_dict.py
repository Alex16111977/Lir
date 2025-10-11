"""
test/create_vocabulary_dict.py
Створення словника з темами та перекладами
Дата: 10.10.2025
"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

# СЛОВНИК З 13 ТЕМАМИ
# На основі аналізу найчастіших слів з текстів
VOCABULARY = {
    "theme-food": {
        "name": "Еда и напитки",
        "color": "#FF6B6B",
        "emoji": "🍽️",
        "words": [
            {
                "german": "das Getränk, -e",
                "russian": "напиток",
                "examples": [
                    {"text_id": "text-1", "phrase": "beliebte Getränke"},
                    {"text_id": "text-5", "phrase": "verschiedene Getränke"}
                ]
            },
            {
                "german": "der Käse",
                "russian": "сыр",
                "examples": [
                    {"text_id": "text-3", "phrase": "französischer Käse"}
                ]
            },
            {
                "german": "das Essen",
                "russian": "еда",
                "examples": [
                    {"text_id": "text-2", "phrase": "gesundes Essen"}
                ]
            },
            {
                "german": "die Mahlzeit, -en",
                "russian": "прием пищи",
                "examples": [
                    {"text_id": "text-4", "phrase": "drei Mahlzeiten"}
                ]
            },
            {
                "german": "das Brot, -e",
                "russian": "хлеб",
                "examples": [
                    {"text_id": "text-6", "phrase": "frisches Brot"}
                ]
            }
        ]
    },
    "theme-communication": {
        "name": "Коммуникация",
        "color": "#4ECDC4",
        "emoji": "💬",
        "words": [
            {
                "german": "telefonieren",
                "russian": "телефонувати",
                "examples": [
                    {"text_id": "text-10", "phrase": "oft telefonieren"}
                ]
            },
            {
                "german": "sprechen",
                "russian": "говорить",
                "examples": [
                    {"text_id": "text-12", "phrase": "Deutsch sprechen"}
                ]
            },
            {
                "german": "sagen",
                "russian": "сказать",
                "examples": [
                    {"text_id": "text-15", "phrase": "etwas sagen"}
                ]
            },
            {
                "german": "die Sprache, -n",
                "russian": "язык",
                "examples": [
                    {"text_id": "text-20", "phrase": "viele Sprachen"}
                ]
            }
        ]
    },
    "theme-transport": {
        "name": "Транспорт",
        "color": "#95E1D3",
        "emoji": "🚗",
        "words": [
            {
                "german": "das Auto, -s",
                "russian": "автомобиль",
                "examples": [
                    {"text_id": "text-25", "phrase": "mit dem Auto fahren"}
                ]
            },
            {
                "german": "der Zug, Züge",
                "russian": "поезд",
                "examples": [
                    {"text_id": "text-27", "phrase": "mit dem Zug reisen"}
                ]
            },
            {
                "german": "fahren",
                "russian": "ехать",
                "examples": [
                    {"text_id": "text-30", "phrase": "nach Berlin fahren"}
                ]
            }
        ]
    },
    "theme-art": {
        "name": "Искусство и культура",
        "color": "#F38181",
        "emoji": "🎨",
        "words": [
            {
                "german": "die Musik",
                "russian": "музыка",
                "examples": [
                    {"text_id": "text-35", "phrase": "klassische Musik"}
                ]
            },
            {
                "german": "das Theater",
                "russian": "театр",
                "examples": [
                    {"text_id": "text-37", "phrase": "ins Theater gehen"}
                ]
            },
            {
                "german": "das Bild, -er",
                "russian": "картина",
                "examples": [
                    {"text_id": "text-40", "phrase": "schöne Bilder"}
                ]
            }
        ]
    },
    "theme-languages": {
        "name": "Языки",
        "color": "#AA96DA",
        "emoji": "🗣️",
        "words": [
            {
                "german": "Deutsch",
                "russian": "немецкий",
                "examples": [
                    {"text_id": "text-45", "phrase": "Deutsch lernen"}
                ]
            },
            {
                "german": "Englisch",
                "russian": "английский",
                "examples": [
                    {"text_id": "text-47", "phrase": "Englisch sprechen"}
                ]
            },
            {
                "german": "lernen",
                "russian": "учить",
                "examples": [
                    {"text_id": "text-50", "phrase": "Sprachen lernen"}
                ]
            }
        ]
    },
    "theme-science": {
        "name": "Наука и технологии",
        "color": "#FCBAD3",
        "emoji": "🔬",
        "words": [
            {
                "german": "die Wissenschaft, -en",
                "russian": "наука",
                "examples": [
                    {"text_id": "text-55", "phrase": "moderne Wissenschaft"}
                ]
            },
            {
                "german": "das Internet",
                "russian": "интернет",
                "examples": [
                    {"text_id": "text-57", "phrase": "im Internet surfen"}
                ]
            }
        ]
    },
    "theme-geography": {
        "name": "География и путешествия",
        "color": "#FFFFD2",
        "emoji": "🌍",
        "words": [
            {
                "german": "das Land, Länder",
                "russian": "страна",
                "examples": [
                    {"text_id": "text-60", "phrase": "viele Länder"}
                ]
            },
            {
                "german": "die Stadt, Städte",
                "russian": "город",
                "examples": [
                    {"text_id": "text-61", "phrase": "große Städte"}
                ]
            },
            {
                "german": "reisen",
                "russian": "путешествовать",
                "examples": [
                    {"text_id": "text-58", "phrase": "gerne reisen"}
                ]
            }
        ]
    },
    "theme-history": {
        "name": "История",
        "color": "#A8D8EA",
        "emoji": "📜",
        "words": [
            {
                "german": "die Geschichte, -n",
                "russian": "история",
                "examples": [
                    {"text_id": "text-52", "phrase": "alte Geschichte"}
                ]
            },
            {
                "german": "das Jahr, -e",
                "russian": "год",
                "examples": [
                    {"text_id": "text-54", "phrase": "viele Jahre"}
                ]
            }
        ]
    },
    "theme-verbs": {
        "name": "Глаголы",
        "color": "#FFAAA5",
        "emoji": "⚡",
        "words": [
            {
                "german": "haben",
                "russian": "иметь",
                "examples": [
                    {"text_id": "text-1", "phrase": "viele Leute haben"}
                ]
            },
            {
                "german": "sein",
                "russian": "быть",
                "examples": [
                    {"text_id": "text-2", "phrase": "Menschen sind"}
                ]
            },
            {
                "german": "geben (gibt)",
                "russian": "давать (есть)",
                "examples": [
                    {"text_id": "text-3", "phrase": "es gibt viele"}
                ]
            },
            {
                "german": "machen",
                "russian": "делать",
                "examples": [
                    {"text_id": "text-5", "phrase": "etwas machen"}
                ]
            },
            {
                "german": "können (kann)",
                "russian": "мочь (может)",
                "examples": [
                    {"text_id": "text-7", "phrase": "man kann sehen"}
                ]
            },
            {
                "german": "werden",
                "russian": "становиться",
                "examples": [
                    {"text_id": "text-9", "phrase": "immer wichtiger werden"}
                ]
            }
        ]
    },
    "theme-adjectives": {
        "name": "Прилагательные",
        "color": "#FFD3B6",
        "emoji": "✨",
        "words": [
            {
                "german": "viele",
                "russian": "многие",
                "examples": [
                    {"text_id": "text-1", "phrase": "viele Menschen"}
                ]
            },
            {
                "german": "sehr",
                "russian": "очень",
                "examples": [
                    {"text_id": "text-2", "phrase": "sehr wichtig"}
                ]
            },
            {
                "german": "große",
                "russian": "большой",
                "examples": [
                    {"text_id": "text-4", "phrase": "große Stadt"}
                ]
            },
            {
                "german": "gut",
                "russian": "хороший",
                "examples": [
                    {"text_id": "text-6", "phrase": "gute Idee"}
                ]
            }
        ]
    },
    "theme-time": {
        "name": "Время и числа",
        "color": "#DCEDC1",
        "emoji": "⏰",
        "words": [
            {
                "german": "die Zeit, -en",
                "russian": "время",
                "examples": [
                    {"text_id": "text-10", "phrase": "lange Zeit"}
                ]
            },
            {
                "german": "heute",
                "russian": "сегодня",
                "examples": [
                    {"text_id": "text-12", "phrase": "heute Abend"}
                ]
            },
            {
                "german": "jetzt",
                "russian": "сейчас",
                "examples": [
                    {"text_id": "text-14", "phrase": "jetzt beginnen"}
                ]
            }
        ]
    },
    "theme-measurements": {
        "name": "Измерения и количество",
        "color": "#FFC8A2",
        "emoji": "📏",
        "words": [
            {
                "german": "groß",
                "russian": "большой",
                "examples": [
                    {"text_id": "text-15", "phrase": "sehr groß"}
                ]
            },
            {
                "german": "klein",
                "russian": "маленький",
                "examples": [
                    {"text_id": "text-17", "phrase": "zu klein"}
                ]
            },
            {
                "german": "viel",
                "russian": "много",
                "examples": [
                    {"text_id": "text-19", "phrase": "zu viel"}
                ]
            }
        ]
    },
    "theme-abstract": {
        "name": "Абстрактные понятия",
        "color": "#D4A5A5",
        "emoji": "💭",
        "words": [
            {
                "german": "die Leute (Pl.)",
                "russian": "люди",
                "examples": [
                    {"text_id": "text-1", "phrase": "viele Leute"}
                ]
            },
            {
                "german": "der Mensch, -en",
                "russian": "человек",
                "examples": [
                    {"text_id": "text-2", "phrase": "alle Menschen"}
                ]
            },
            {
                "german": "wichtig",
                "russian": "важный",
                "examples": [
                    {"text_id": "text-5", "phrase": "sehr wichtig"}
                ]
            },
            {
                "german": "interessant",
                "russian": "интересный",
                "examples": [
                    {"text_id": "text-8", "phrase": "sehr interessant"}
                ]
            }
        ]
    }
}

def save_vocabulary():
    """Збереження словника в JSON"""
    
    output = Path(__file__).parent.parent / 'test' / 'vocabulary_dict.json'
    
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(VOCABULARY, f, ensure_ascii=False, indent=2)
    
    # Статистика
    total_words = sum(len(theme['words']) for theme in VOCABULARY.values())
    
    print(f"[OK] Словник збережено: {output}")
    print(f"[OK] Всього тем: {len(VOCABULARY)}")
    print(f"[OK] Всього слів: {total_words}")
    print(f"\n[+] Розподіл по темах:")
    for theme_id, theme_data in VOCABULARY.items():
        print(f"  - {theme_data['emoji']} {theme_data['name']}: {len(theme_data['words'])} слів")
    
    return total_words

if __name__ == '__main__':
    print("=== СТВОРЕННЯ СЛОВНИКА З ТЕМАМИ ===\n")
    save_vocabulary()
