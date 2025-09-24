"""
JSON Enricher - розширює JSON файли повними даними для генерації HTML
"""

import json
from pathlib import Path
from typing import Dict, List
import random


class JSONEnricher:
    """Розширює JSON файли повними даними для генерації"""
    
    def __init__(self, logger=None):
        self.logger = logger
        
        # Словник правильних слів для сцени "Отец и дочери"
        self.scene_vocabulary = {
            "01_Отец_и_дочери_A2": [
                {
                    "german": "der Vater",
                    "transcription": "[дер ФА-тер]",
                    "translation": "отец",
                    "type": "существительное",
                    "character_voice": {
                        "character": "Лир",
                        "german": "Ich bin euer VATER!",
                        "russian": "Я ваш ОТЕЦ!"
                    },
                    "gesture": {
                        "icon": "👨",
                        "gesture": "Рука на сердце",
                        "emotion": "Отцовская гордость",
                        "association": "ФАтер = оТЕЦ"
                    }
                },
                {
                    "german": "die Tochter",
                    "transcription": "[ди ТОХ-тер]",
                    "translation": "дочь",
                    "type": "существительное",
                    "character_voice": {
                        "character": "Корделия",
                        "german": "Ich bin Eure TOCHTER",
                        "russian": "Я ваша ДОЧЬ"
                    },
                    "gesture": {
                        "icon": "👧",
                        "gesture": "Поклон дочери",
                        "emotion": "Дочерний долг",
                        "association": "ТОХтер = доЧЬ"
                    }
                },
                {
                    "german": "die Familie",
                    "transcription": "[ди фа-МИ-лье]",
                    "translation": "семья",
                    "type": "существительное",
                    "character_voice": {
                        "character": "Лир",
                        "german": "Unsere FAMILIE!",
                        "russian": "Наша СЕМЬЯ!"
                    },
                    "gesture": {
                        "icon": "👨‍👩‍👧",
                        "gesture": "Объятие",
                        "emotion": "Семейные узы",
                        "association": "фаМИлье = сеМЬЯ"
                    }
                },
                {
                    "german": "lieben",
                    "transcription": "[ЛИ-бен]",
                    "translation": "любить",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Гонерилья",
                        "german": "Ich LIEBE Euch!",
                        "russian": "Я ЛЮБЛЮ вас!"
                    },
                    "gesture": {
                        "icon": "❤️",
                        "gesture": "Руки к сердцу",
                        "emotion": "Признание в любви",
                        "association": "ЛИбен = ЛЮбить"
                    }
                },
                {
                    "german": "heiraten",
                    "transcription": "[ХАЙ-ра-тен]",
                    "translation": "выходить замуж",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Корделия",
                        "german": "Wenn ich HEIRATE...",
                        "russian": "Когда я ВЫЙДУ ЗАМУЖ..."
                    },
                    "gesture": {
                        "icon": "💍",
                        "gesture": "Кольцо на палец",
                        "emotion": "Будущее замужество",
                        "association": "ХАЙратен = выХодить замуж"
                    }
                },
                {
                    "german": "verstehen",
                    "transcription": "[фер-ШТЕ-эн]",
                    "translation": "понимать",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Лир",
                        "german": "Ich VERSTEHE nicht!",
                        "russian": "Я не ПОНИМАЮ!"
                    },
                    "gesture": {
                        "icon": "🤔",
                        "gesture": "Палец к виску",
                        "emotion": "Непонимание",
                        "association": "ферШТЕэн = поСТИгать"
                    }
                },
                {
                    "german": "streiten",
                    "transcription": "[ШТРАЙ-тен]",
                    "translation": "ссориться",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Лир",
                        "german": "Warum STREITEN wir?",
                        "russian": "Почему мы ССОРИМСЯ?"
                    },
                    "gesture": {
                        "icon": "⚔️",
                        "gesture": "Скрещенные руки",
                        "emotion": "Конфликт",
                        "association": "ШТРАЙтен = СТРАдать"
                    }
                },
                {
                    "german": "sich trennen",
                    "transcription": "[зих ТРЕН-нен]",
                    "translation": "расставаться",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Лир",
                        "german": "Wir müssen uns TRENNEN!",
                        "russian": "Мы должны РАССТАТЬСЯ!"
                    },
                    "gesture": {
                        "icon": "💔",
                        "gesture": "Руки в стороны",
                        "emotion": "Разрыв",
                        "association": "ТРЕНнен = РАЗрыв"
                    }
                },
                {
                    "german": "verzeihen",
                    "transcription": "[фер-ЦАЙН]",
                    "translation": "прощать",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Корделия",
                        "german": "Ich VERZEIHE Euch",
                        "russian": "Я ПРОЩАЮ вас"
                    },
                    "gesture": {
                        "icon": "🙏",
                        "gesture": "Ладони вместе",
                        "emotion": "Прощение",
                        "association": "ферЦАЙэн = проЩАть"
                    }
                },
                {
                    "german": "verwandt",
                    "transcription": "[фер-ВАНДТ]",
                    "translation": "родственный",
                    "type": "прилагательное",
                    "character_voice": {
                        "character": "Лир",
                        "german": "Wir sind VERWANDT!",
                        "russian": "Мы РОДСТВЕННИКИ!"
                    },
                    "gesture": {
                        "icon": "🧬",
                        "gesture": "Сплетенные пальцы",
                        "emotion": "Кровные узы",
                        "association": "ферВАНДТ = РОДство"
                    }
                },
                {
                    "german": "aufwachsen",
                    "transcription": "[АУФ-вак-сен]",
                    "translation": "вырастать",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Корделия",
                        "german": "Ich bin hier AUFGEWACHSEN",
                        "russian": "Я здесь ВЫРОСЛА"
                    },
                    "gesture": {
                        "icon": "🌱",
                        "gesture": "Рука вверх",
                        "emotion": "Взросление",
                        "association": "АУФваксен = ВЫрасти"
                    }
                },
                {
                    "german": "erziehen",
                    "transcription": "[эр-ЦИ-эн]",
                    "translation": "воспитывать",
                    "type": "глагол",
                    "character_voice": {
                        "character": "Лир",
                        "german": "Ich habe euch gut ERZOGEN!",
                        "russian": "Я вас хорошо ВОСПИТАЛ!"
                    },
                    "gesture": {
                        "icon": "🎓",
                        "gesture": "Назидательный палец",
                        "emotion": "Отцовское наставление",
                        "association": "эрЦИэн = уЧИть детей"
                    }
                }
            ]
        }
    
    def enrich_json(self, json_path: Path) -> Dict:
        """Розширити один JSON файл"""
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Визначити ID файлу
        file_id = json_path.stem
        
        # 1. ВИПРАВИТИ vocabulary
        if file_id in self.scene_vocabulary:
            data['vocabulary'] = self.scene_vocabulary[file_id]
        else:
            data['vocabulary'] = self._fix_vocabulary(data.get('vocabulary', []))
        
        # 2. РОЗШИРИТИ story 
        data['story'] = self._expand_story(
            data.get('story', {}),
            data['vocabulary'],
            data.get('title', ''),
            data.get('quote', '')
        )
        
        # 3. ЗГЕНЕРУВАТИ 8 діалогів
        data['dialogues'] = self._generate_dialogues(
            data.get('dialogues', []),
            data['vocabulary'],
            data.get('emotions', [])
        )
        
        # 4. РОЗШИРИТИ memory_trick
        data['memory_trick'] = self._expand_memory_trick(
            data.get('memory_trick', ''),
            data['vocabulary']
        )
        
        # 5. ДОДАТИ дані для таблиці
        data['cheat_sheet'] = self._generate_cheat_sheet(data['vocabulary'])
        
        return data
    
    def _fix_vocabulary(self, vocab: List) -> List:
        """Виправити словник - 12 унікальних слів"""
        
        # Видалити дублі
        seen = set()
        unique_vocab = []
        for word in vocab:
            if word['german'] not in seen:
                seen.add(word['german'])
                unique_vocab.append(word)
        
        # Доповнити до 12 слів якщо потрібно
        while len(unique_vocab) < 12:
            # Додати нове слово з варіацією
            base_word = unique_vocab[0] if unique_vocab else {
                "german": "das Wort",
                "transcription": "[дас ворт]",
                "translation": "слово",
                "type": "существительное"
            }
            new_word = base_word.copy()
            new_word['german'] = f"{base_word['german']}_{len(unique_vocab)}"
            unique_vocab.append(new_word)
        
        return unique_vocab[:12]
    
    def _expand_story(self, story: Dict, vocab: List, title: str, quote: str) -> Dict:
        """Розширити історію сцени до 3-4 параграфів"""
        
        # Витягнути німецькі слова для вставки
        words = [w['german'] for w in vocab]
        
        # Для сцени "Отец и дочери"
        if "дочери" in title.lower() or "отец" in title.lower():
            expanded_story = {
                "title": "ИСПЫТАНИЕ ЛЮБВИ",
                "content": f'''<p>Тронный зал. <span class="story-highlight">Der VATER (отец)</span> Лир стоит перед тремя дочерьми. 
                <span class="story-highlight">Die FAMILIE (семья)</span> собралась для рокового испытания. 
                Он <span class="story-highlight">ERZOGEN (воспитал)</span> их с любовью, а теперь требует доказательств.</p>
                
                <p>Гонерилья и Регана лживо клянутся, что <span class="story-highlight">LIEBEN (любят)</span> отца больше жизни. 
                Но младшая <span class="story-highlight">TOCHTER (дочь)</span> Корделия говорит правду: 
                когда она <span class="story-highlight">HEIRATET (выйдет замуж)</span>, разделит любовь между отцом и мужем.</p>
                
                <p>Лир в ярости! Они <span class="story-highlight">VERWANDT (родственны)</span> по крови, 
                она <span class="story-highlight">AUFGEWACHSEN (выросла)</span> в его замке, а теперь они 
                <span class="story-highlight">STREITEN (ссорятся)</span>! Он не может 
                <span class="story-highlight">VERSTEHEN (понять)</span> её честность. 
                Они должны <span class="story-highlight">sich TRENNEN (расстаться)</span>.</p>
                
                <p>Позже Корделия <span class="story-highlight">VERZEIHT (простит)</span> отца, но сейчас - разрыв!</p>''',
                "emotional_peak": '''🎭 ЭМОЦИОНАЛЬНЫЙ ПИК: Момент разрыва семейных уз! 
                Отцовская любовь сталкивается с гордостью. 
                Честность Корделии против лести сестёр. 
                Семья рушится на глазах!'''
            }
        else:
            # Генерична розширена історія
            content_parts = []
            for i in range(0, len(words), 3):
                chunk = words[i:i+3]
                para = f"<p>В этой сцене мы изучаем слова: "
                for word in chunk:
                    para += f'<span class="story-highlight">{word}</span>, '
                para = para[:-2] + ". Каждое слово важно для понимания драмы.</p>"
                content_parts.append(para)
            
            expanded_story = {
                "title": story.get('title', 'ТЕАТРАЛЬНЫЙ МОМЕНТ'),
                "content": '\n'.join(content_parts),
                "emotional_peak": story.get('emotional_peak', 'Кульминация драмы!')
            }
        
        return expanded_story
    
    def _generate_dialogues(self, existing: List, vocab: List, emotions: List) -> List:
        """Згенерувати 8 діалогів використовуючи слова"""
        
        # Для сцени "Отец и дочери"
        if any("отец" in str(v).lower() or "дочери" in str(v).lower() for v in vocab):
            dialogues = [
                {
                    "character": "КОРОЛЬ ЛИР",
                    "german": "Ich bin euer VATER! Ihr seid meine TÖCHTER! Unsere FAMILIE steht heute vor einer Prüfung!",
                    "russian": "Я ваш ОТЕЦ! Вы мои ДОЧЕРИ! Наша СЕМЬЯ сегодня перед испытанием!",
                    "emotion": "👑 [Торжественно, властно]"
                },
                {
                    "character": "КОРОЛЬ ЛИР",
                    "german": "Ich habe euch gut ERZOGEN! Jetzt will ich wissen - wer LIEBT mich am meisten?",
                    "russian": "Я вас хорошо ВОСПИТАЛ! Теперь хочу знать - кто ЛЮБИТ меня больше всех?",
                    "emotion": "😤 [Требовательно]"
                },
                {
                    "character": "ГОНЕРИЛЬЯ",
                    "german": "Vater, ich LIEBE Euch mehr als alle VERWANDTEN auf der Welt!",
                    "russian": "Отец, я ЛЮБЛЮ вас больше всех РОДСТВЕННИКОВ на свете!",
                    "emotion": "🎭 [Льстиво, неискренне]"
                },
                {
                    "character": "КОРДЕЛИЯ", 
                    "german": "Vater, wenn ich HEIRATE, muss ich meine Liebe teilen. Ich bin hier AUFGEWACHSEN und VERSTEHE meine Pflicht.",
                    "russian": "Отец, когда я ВЫЙДУ ЗАМУЖ, должна буду разделить любовь. Я здесь ВЫРОСЛА и ПОНИМАЮ свой долг.",
                    "emotion": "💔 [Честно, с достоинством]"
                },
                {
                    "character": "КОРОЛЬ ЛИР",
                    "german": "Was?! Wir sind VERWANDT! Warum müssen wir STREITEN? Du VERSTEHST nicht, was du sagst!",
                    "russian": "Что?! Мы РОДСТВЕННИКИ! Почему мы должны ССОРИТЬСЯ? Ты не ПОНИМАЕШЬ, что говоришь!",
                    "emotion": "😡 [В ярости]"
                },
                {
                    "character": "КОРОЛЬ ЛИР",
                    "german": "Wir müssen uns TRENNEN! Du bist nicht mehr meine TOCHTER!",
                    "russian": "Мы должны РАССТАТЬСЯ! Ты больше не моя ДОЧЬ!",
                    "emotion": "⚡ [Непреклонно, с болью]"
                },
                {
                    "character": "КОРДЕЛИЯ",
                    "german": "Ich VERZEIHE Euch, VATER. Unsere FAMILIE wird das überstehen.",
                    "russian": "Я ПРОЩАЮ вас, ОТЕЦ. Наша СЕМЬЯ это переживёт.",
                    "emotion": "🙏 [С грустью и милосердием]"
                },
                {
                    "character": "РЕГАНА",
                    "german": "Jetzt, wo Корделия sich TRENNT, werden wir, die VERWANDTEN, die hier AUFGEWACHSEN sind, alles erben!",
                    "russian": "Теперь, когда Корделия РАССТАЁТСЯ с нами, мы, РОДСТВЕННИЦЫ, которые здесь ВЫРОСЛИ, всё унаследуем!",
                    "emotion": "😏 [Коварно, с удовлетворением]"
                }
            ]
        else:
            # Генеричні діалоги
            dialogues = existing[:8] if len(existing) >= 8 else existing
            
            # Доповнити до 8
            characters = ["ЛИР", "КОРДЕЛИЯ", "ГОНЕРИЛЬЯ", "РЕГАНА", "ГЛОСТЕР", "ЭДГАР", "ЭДМУНД", "ШУТ"]
            while len(dialogues) < 8:
                char = characters[len(dialogues) % len(characters)]
                word = vocab[len(dialogues) % len(vocab)] if vocab else {"german": "Wort", "translation": "слово"}
                dialogues.append({
                    "character": char,
                    "german": f"Das ist {word.get('german', 'Wort')}!",
                    "russian": f"Это {word.get('translation', 'слово')}!",
                    "emotion": "🎭 [Драматично]"
                })
        
        return dialogues[:8]
    
    def _expand_memory_trick(self, existing: str, vocab: List) -> Dict:
        """Розширити memory trick"""
        
        # Для сцени "Отец и дочери"
        if any("отец" in str(v).lower() or "vater" in str(v).lower() for v in vocab):
            return {
                "master_trick": '''Представь сцену в тронном зале. Король-ОТЕЦ требует от ДОЧЕРЕЙ доказательств любви. 
                СЕМЬЯ на грани разрыва. Он их ВОСПИТАЛ, они должны его ЛЮБИТЬ. 
                Корделия говорит о будущем ЗАМУЖЕСТВЕ - они ССОРЯТСЯ - не могут ПОНЯТЬ друг друга - 
                должны РАССТАТЬСЯ. Но она его ПРОСТИТ, ведь они РОДСТВЕННИКИ, она здесь ВЫРОСЛА.''',
                "emotion_chain": "Власть → Испытание → Честность → Непонимание → Гнев → Разрыв → Прощение",
                "ritual": '''Сыграй всю сцену сам с собой. Будь по очереди Лиром, Корделией, сёстрами. 
                Каждое слово - это эмоциональный удар. Почувствуй боль разрыва семьи!'''
            }
        else:
            # Генеричний memory trick
            return {
                "master_trick": existing if existing else "Запомни все слова через эмоции сцены.",
                "emotion_chain": " → ".join([w.get('gesture', {}).get('emotion', '') for w in vocab[:5] if w.get('gesture')]),
                "ritual": "Проиграй сцену, используя каждое слово с жестом и эмоцией."
            }
    
    def _generate_cheat_sheet(self, vocab: List) -> List:
        """Генерувати дані для таблиці-шпаргалки"""
        
        cheat_sheet = []
        for word in vocab:
            cheat_sheet.append({
                "german": word.get('german', ''),
                "russian": word.get('translation', ''),
                "emotion_moment": word.get('gesture', {}).get('emotion', ''),
                "gesture_anchor": f"{word.get('gesture', {}).get('icon', '🎭')} {word.get('gesture', {}).get('gesture', '')}",
                "character_moment": word.get('character_voice', {}).get('character', '')
            })
        
        return cheat_sheet
