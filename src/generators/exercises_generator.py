"""Interactive exercises generator for lesson pages."""

from __future__ import annotations

import json
import random
import re
from html import escape
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


class ExercisesGenerator:
    """Generate HTML snippets for interactive lesson exercises."""

    GLOBAL_VOCAB_PATH = (
        Path(__file__).resolve().parents[2]
        / "KingLearComic"
        / "data"
        / "vocabulary"
        / "vocabulary.json"
    )

    def __init__(self, logger: Any = None) -> None:
        self.logger = logger
        self.exercises_generated = 0
        self._global_vocabulary = self._load_global_vocabulary()
        self._translation_map = self._build_translation_map(self._global_vocabulary)
        self._antonym_mapping = self._build_antonym_mapping(self._translation_map)
        self._synonym_lookup, self._synonym_pool = self._build_synonym_pool()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def generate_all_exercises(self, lesson_data: Dict[str, Any]) -> Dict[str, str]:
        """Generate all exercises for the given lesson."""

        vocabulary = lesson_data.get("vocabulary", []) or []
        if not vocabulary:
            return {}

        exercises = {
            "word_matching": self._generate_word_matching(vocabulary),
            "articles": self._generate_articles(vocabulary),
            "synonyms": self._generate_synonyms_antonyms(vocabulary),
            "quiz": self._generate_vocabulary_quiz(vocabulary),
            "context": self._generate_context_translation(vocabulary),
            "builder": self._generate_sentence_builder(
                lesson_data.get("dialogues", []), lesson_data.get("story")
            ),
        }

        self.exercises_generated += sum(1 for value in exercises.values() if value)
        return exercises

    def create_exercises_section(self, exercises: Dict[str, str]) -> str:
        """Wrap individual exercises into a single HTML accordion."""

        valid_items = {key: value for key, value in exercises.items() if value}
        if not valid_items:
            return ""

        titles = {
            "word_matching": "🔗 Подбор слов",
            "articles": "🎯 Артикли и род",
            "synonyms": "🌈 Синонимы и антонимы",
            "quiz": "🧠 Викторина по словам",
            "context": "📝 Контекстный перевод",
            "builder": "🧩 Конструктор предложений",
        }

        accordion_items = []
        for key, title in titles.items():
            content = valid_items.get(key)
            if not content:
                continue
            accordion_items.append(
                f"""
                <details class="exercise-accordion-item">
                    <summary>{escape(title)}</summary>
                    <div class="exercise-content">
                        {content}
                    </div>
                </details>
                """
            )

        if not accordion_items:
            return ""

        return (
            "\n        <!-- РОЗДЕЛ: ИНТЕРАКТИВНЫЕ УПРАЖНЕНИЯ -->\n"
            "        <section class=\"exercises-section\">\n"
            "            <h2 class=\"section-title\">\n"
            "                <span class=\"icon\">📚</span> Упражнения\n"
            "            </h2>\n"
            "            <div class=\"exercises-accordion\">\n"
            + "\n".join(accordion_items)
            + "\n            </div>\n        </section>\n        "
        )

    # ------------------------------------------------------------------
    # Vocabulary helpers
    # ------------------------------------------------------------------
    def _load_global_vocabulary(self) -> List[Dict[str, Any]]:
        if not self.GLOBAL_VOCAB_PATH.exists():
            if self.logger:
                self.logger.warning(
                    "[Exercises] Не знайдено словник для синонимів: %s",
                    self.GLOBAL_VOCAB_PATH,
                )
            return []

        try:
            data = json.loads(self.GLOBAL_VOCAB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            if self.logger:
                self.logger.error("[Exercises] Неможливо прочитати словник: %s", exc)
            return []

        vocabulary = data.get("vocabulary", [])
        if not vocabulary and self.logger:
            self.logger.warning("[Exercises] Словник не містить лексики")
        return vocabulary

    def _build_translation_map(
        self, vocabulary: Iterable[Dict[str, Any]]
    ) -> Dict[str, List[Dict[str, Any]]]:
        mapping: Dict[str, List[Dict[str, Any]]] = {}
        for entry in vocabulary:
            translation = (entry.get("translation") or "").strip().lower()
            german = entry.get("german")
            if not translation or not german:
                continue
            mapping.setdefault(translation, []).append(entry)
        return mapping

    def _build_antonym_mapping(
        self, translation_map: Dict[str, List[Dict[str, Any]]]
    ) -> Dict[str, Dict[str, Any]]:
        mapping: Dict[str, Dict[str, Any]] = {}

        def add_pair(pos: str, neg: str) -> None:
            pos = pos.strip().lower()
            neg = neg.strip().lower()
            if pos in translation_map and neg in translation_map:
                mapping[pos] = translation_map[neg][0]
                mapping[neg] = translation_map[pos][0]

        # Пошук автоматичних пар: не- та без-
        for translation in list(translation_map.keys()):
            if translation.startswith("не") and len(translation) > 2:
                base = translation[2:]
                add_pair(base, translation)
            if translation.startswith("без ") and len(translation) > 4:
                base = translation.replace("без ", "", 1)
                add_pair(base, translation)

        # Ручні пари антонімів для ключових понять сюжету
        manual_pairs = {
            "храбрый": "трусливый",
            "любить": "ненавидеть",
            "справедливость": "несправедливость",
            "мир": "война",
            "друг": "враг",
            "верность": "предательство",
            "свет": "тьма",
            "радость": "печаль",
            "добрый": "злой",
            "счастливый": "несчастный",
        }
        for positive, negative in manual_pairs.items():
            add_pair(positive, negative)

        return mapping

    def _build_synonym_pool(self) -> (
        Dict[str, List[Dict[str, Any]]],
        List[Dict[str, Any]],
    ):
        lookup: Dict[str, List[Dict[str, Any]]] = {}
        pool: List[Dict[str, Any]] = []

        for translation, entries in self._translation_map.items():
            antonym_entry = self._antonym_mapping.get(translation)
            if not antonym_entry:
                continue
            antonym_word = antonym_entry.get("german")
            antonym_translation = antonym_entry.get("translation", "")
            german_words = [entry.get("german") for entry in entries if entry.get("german")]
            if len(german_words) < 2 or not antonym_word:
                continue

            for idx, base_word in enumerate(german_words):
                synonyms = [word for i, word in enumerate(german_words) if i != idx]
                if not synonyms:
                    continue
                payload = {
                    "word": base_word,
                    "synonyms": synonyms,
                    "translation": translation,
                    "antonym": antonym_word,
                    "antonym_translation": antonym_translation,
                }
                lookup.setdefault(base_word.lower(), []).append(payload)
                pool.append(payload)

        return lookup, pool

    # ------------------------------------------------------------------
    # Individual exercise generators
    # ------------------------------------------------------------------
    def _generate_word_matching(self, vocabulary: List[Dict[str, Any]]) -> str:
        selectable = [word for word in vocabulary if word.get("german") and word.get("translation")]
        if not selectable:
            return ""

        sample = random.sample(selectable, min(8, len(selectable)))
        translations = [escape(word.get("translation", "")) for word in sample]
        random.shuffle(translations)

        words_html = []
        for idx, word in enumerate(sample):
            words_html.append(
                f"""
                <div class=\"word-item prompt\" data-pair-id=\"{idx}\" data-type=\"prompt\" 
                     onclick=\"handleWordClick(this, 'prompt')\">
                    <span class=\"word-main\">{escape(word.get('german', ''))}</span>
                    <small class=\"word-hint\">{escape(word.get('transcription', ''))}</small>
                </div>
                """
            )

        translations_html = []
        for idx, translation in enumerate(translations):
            # Знайдемо правильний pair-id для цього перекладу
            correct_pair_id = next((i for i, word in enumerate(sample) 
                                   if escape(word.get('translation', '')) == translation), 0)
            translations_html.append(
                f"""
                <div class=\"translation-item match\" data-pair-id=\"{correct_pair_id}\" 
                     data-type=\"match\" onclick=\"handleWordClick(this, 'match')\">
                    {translation}
                </div>
                """
            )

        total_pairs = len(sample)

        return f"""\n            <div class=\"exercise-block\" id=\"word-matching\">\n                <h3 class=\"exercise-title\">🔗 Подбор слов</h3>\n                <p class=\"exercise-intro\">Нажмите на немецкое слово, затем на его русский перевод. При правильном ответе пара станет зелёной.</p>\n                \n                <!-- Прогрес-бар -->\n                <div class=\"matching-progress\">\n                    <div class=\"progress-track\">\n                        <div class=\"progress-fill\" style=\"width: 0%\"></div>\n                    </div>\n                    <div class=\"progress-text\">0 з {total_pairs}</div>\n                </div>\n                \n                <div class=\"matching-container\">\n                    <div class=\"words-column\">\n{"".join(words_html)}\n                    </div>\n                    <div class=\"translations-column\">\n{"".join(translations_html)}\n                    </div>\n                </div>\n                <!-- Кнопка видалена - миттєва перевірка! -->\n            </div>\n            """

    def _generate_articles(self, vocabulary: List[Dict[str, Any]]) -> str:
        nouns = []
        for word in vocabulary:
            german = word.get("german", "")
            translation = word.get("translation", "")
            if not german or not translation:
                continue
            parts = german.split()
            if parts and parts[0].lower() in {"der", "die", "das"}:
                nouns.append(
                    {
                        "article": parts[0].lower(),
                        "noun": " ".join(parts[1:]) or parts[0],
                        "translation": translation,
                    }
                )
        if not nouns:
            return ""

        sample = random.sample(nouns, min(9, len(nouns)))
        cards_html = []
        for item in sample:
            cards_html.append(
                f"""
                <div class=\"article-item\" data-correct=\"{escape(item['article'])}\">
                    <div class=\"article-word\">
                        <span class=\"noun\">{escape(item['noun'])}</span>
                        <small>{escape(item['translation'])}</small>
                    </div>
                    <div class=\"article-buttons\">
                        <button type=\"button\" data-article=\"der\" onclick=\"checkArticleInstant(this, 'der')\">der</button>
                        <button type=\"button\" data-article=\"die\" onclick=\"checkArticleInstant(this, 'die')\">die</button>
                        <button type=\"button\" data-article=\"das\" onclick=\"checkArticleInstant(this, 'das')\">das</button>
                    </div>
                </div>
                """
            )
            
        total_items = len(sample)

        return (
            "\n            <div class=\"exercise-block\" id=\"articles\">\n"
            "                <h3 class=\"exercise-title\">🎯 Артикли и род</h3>\n"
            "                <p class=\"exercise-intro\">Выберите правильный артикль для существительных из урока.</p>\n"
            f"""                
                <!-- Прогрес-бар -->
                <div class=\"articles-progress\">
                    <div class=\"progress-track\">
                        <div class=\"progress-fill\" style=\"width: 0%\"></div>
                    </div>
                    <div class=\"progress-stats\">
                        <span id=\"articles-correct\">0</span> з <span id=\"articles-total\">{total_items}</span>
                    </div>
                </div>\n"""
            "                <div class=\"articles-grid\">\n"
            + "".join(cards_html)
            + "\n                </div>\n"
            "                <!-- Кнопка видалена - миттєва перевірка! -->\n"
            "            </div>\n            "
        )

    def _generate_synonyms_antonyms(self, vocabulary: List[Dict[str, Any]]) -> str:
        pairs = self._select_synonym_pairs(vocabulary)
        if not pairs:
            return ""

        items_html = []
        for pair in pairs:
            items_html.append(
                f"""
                <div class=\"synonym-item\">
                    <div class=\"word-center\">
                        <span class=\"word-main\">{escape(pair['word'])}</span>
                        <small>{escape(pair['translation'])}</small>
                    </div>
                    <div class=\"options\">
                        <input type=\"text\" placeholder=\"Синоним\" data-correct=\"{escape(pair['synonym'])}\" data-hint=\"{escape(pair['translation'])}\">
                        <input type=\"text\" placeholder=\"Антоним\" data-correct=\"{escape(pair['antonym'])}\" data-hint=\"{escape(pair['antonym_translation'])}\">
                    </div>
                </div>
                """
            )

        return (
            "\n            <div class=\"exercise-block\" id=\"synonyms\">\n"
            "                <h3 class=\"exercise-title\">🌈 Синонимы и антонимы</h3>\n"
            "                <p class=\"exercise-intro\">Подберите синоним из урока и вспомните противоположное значение.</p>\n"
            + "".join(items_html)
            + "\n                <button class=\"check-btn\" data-action=\"check-synonyms\" type=\"button\">Проверить</button>\n"
            "            </div>\n            "
        )

    def _generate_vocabulary_quiz(self, vocabulary: List[Dict[str, Any]]) -> str:
        """Generate a bidirectional quiz for German and Russian vocabulary."""

        selectable = [
            word
            for word in vocabulary
            if word.get("german") and word.get("translation")
        ]
        if not selectable:
            return ""

        random.shuffle(selectable)

        translation_pool = [
            entry.get("translation", "")
            for entry in selectable
            if entry.get("translation")
        ]
        german_pool = [
            entry.get("german", "")
            for entry in selectable
            if entry.get("german")
        ]

        de_ru_words = selectable[:]
        random.shuffle(de_ru_words)
        de_ru_words = de_ru_words[: min(5, len(de_ru_words))]

        ru_de_words = selectable[:]
        random.shuffle(ru_de_words)
        ru_de_words = ru_de_words[: min(5, len(ru_de_words))]

        total_questions = len(de_ru_words) + len(ru_de_words)
        if not total_questions:
            return ""

        questions_html: List[str] = []
        question_index = 0

        for word in de_ru_words:
            questions_html.append(
                self._render_de_ru_question(
                    word,
                    question_index,
                    total_questions,
                    translation_pool,
                    is_first=question_index == 0,
                )
            )
            question_index += 1

        for word in ru_de_words:
            questions_html.append(
                self._render_ru_de_question(
                    word,
                    question_index,
                    total_questions,
                    german_pool,
                    is_first=question_index == 0,
                )
            )
            question_index += 1

        questions_markup = "\n".join(questions_html)

        return (
            f"""
            <div class="exercise-block quiz-container" id="word-quiz">
                <h3 class="exercise-title">🧠 Викторина по словам</h3>

                <div class="quiz-progress">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 0%"></div>
                    </div>
                    <div class="progress-text">
                        Правильних: <span id="correct-count">0</span> / <span id="total-count">{total_questions}</span>
                    </div>
                </div>

                <div id="quiz-questions">
                    {questions_markup}
                </div>

                <div id="quiz-result" class="quiz-results" style="display: none;">
                    <div class="result-text"></div>
                    <button onclick="restartQuiz()" class="restart-btn" type="button">Спробувати знову</button>
                </div>
            </div>
            """
        )

    def _render_de_ru_question(
        self,
        word: Dict[str, Any],
        question_index: int,
        total_questions: int,
        translations: List[str],
        *,
        is_first: bool,
    ) -> str:
        """Render a single DE→RU quiz question."""

        correct_answer = word.get("translation", "")
        options = self._build_quiz_options(correct_answer, translations)
        transcription = word.get("transcription") or ""
        transcription_html = (
            f'<span class="transcription">{escape(transcription)}</span>'
            if transcription
            else ""
        )

        buttons = self._render_answer_buttons(options, correct_answer)
        display = "block" if is_first else "none"

        return (
            f"""
        <div class="quiz-question" data-question-id="{question_index}" data-mode="de-ru" style="display: {display};">
            <div class="quiz-header">
                <span class="question-number">Питання {question_index + 1} з {total_questions}</span>
                <span class="question-mode">DE → RU</span>
            </div>

            <div class="quiz-content">
                <h3>Що означає німецьке слово?</h3>

                <div class="word-display">
                    <span class="german-word">{escape(word.get('german', ''))}</span>
                    {transcription_html}
                </div>

                <div class="answer-buttons">
{buttons}
                </div>
            </div>
        </div>
            """
        )

    def _render_ru_de_question(
        self,
        word: Dict[str, Any],
        question_index: int,
        total_questions: int,
        german_words: List[str],
        *,
        is_first: bool,
    ) -> str:
        """Render a single RU→DE quiz question."""

        correct_answer = word.get("german", "")
        options = self._build_quiz_options(correct_answer, german_words)
        buttons = self._render_answer_buttons(options, correct_answer)
        display = "block" if is_first else "none"

        return (
            f"""
        <div class="quiz-question" data-question-id="{question_index}" data-mode="ru-de" style="display: {display};">
            <div class="quiz-header">
                <span class="question-number">Питання {question_index + 1} з {total_questions}</span>
                <span class="question-mode">RU → DE</span>
            </div>

            <div class="quiz-content">
                <h3>Як німецькою буде:</h3>

                <div class="word-display">
                    <span class="russian-word">{escape(word.get('translation', ''))}</span>
                </div>

                <div class="answer-buttons">
{buttons}
                </div>
            </div>
        </div>
            """
        )

    def _render_answer_buttons(
        self, options: List[str], correct_answer: str
    ) -> str:
        """Render answer buttons for quiz options."""

        buttons: List[str] = []
        for option in options:
            value = option or ""
            is_correct = "true" if value == correct_answer else "false"
            buttons.append(
                f'                    <button class="answer-btn" data-correct="{is_correct}" onclick="checkAnswer(this, {is_correct})">{escape(value)}</button>'
            )
        return "\n".join(buttons)

    def _build_quiz_options(
        self, correct_answer: str, pool: Iterable[str], size: int = 4
    ) -> List[str]:
        """Return shuffled answer options including distractors."""

        options: List[str] = [correct_answer] if correct_answer else []
        candidates = [value for value in pool if value and value != correct_answer]
        random.shuffle(candidates)

        for value in candidates:
            if len(options) >= size:
                break
            if value not in options:
                options.append(value)

        while len(options) < size and candidates:
            candidate = random.choice(candidates)
            options.append(candidate)

        if correct_answer and correct_answer not in options:
            options.append(correct_answer)

        if len(options) > size:
            options = options[:size]

        random.shuffle(options)
        return options

    def _generate_context_translation(self, vocabulary: List[Dict[str, Any]]) -> str:
        contexts = []
        for word in vocabulary:
            voice = word.get("character_voice") or {}
            german_text = voice.get("german")
            russian_text = voice.get("russian")
            target = self._normalize_german_word(word.get("german", ""))
            if not german_text or not russian_text or not target:
                continue
            pattern = re.compile(rf"\b{re.escape(target)}\b", re.IGNORECASE)
            if not pattern.search(german_text):
                continue
            blanked = pattern.sub("_____", german_text, count=1)
            contexts.append(
                {
                    "sentence": blanked,
                    "answer": target,
                    "hint": russian_text,
                }
            )
            if len(contexts) >= 3:
                break

        if not contexts:
            return ""

        rows = []
        for context in contexts:
            rows.append(
                f"""
                <div class=\"context-item\">
                    <p class=\"context-german\">{escape(context['sentence'])}</p>
                    <p class=\"context-hint\">Подсказка: {escape(context['hint'])}</p>
                    <input type=\"text\" placeholder=\"Введите слово\" data-correct=\"{escape(context['answer'])}\">
                </div>
                """
            )

        return (
            "\n            <div class=\"exercise-block\" id=\"context\">\n"
            "                <h3 class=\"exercise-title\">📝 Контекстный перевод</h3>\n"
            + "".join(rows)
            + "\n                <button class=\"check-btn\" data-action=\"check-context\" type=\"button\">Проверить</button>\n"
            "            </div>\n            "
        )

    def _generate_sentence_builder(
        self, dialogues: Iterable[Dict[str, Any]], story: Optional[Dict[str, Any]]
    ) -> str:
        sentences = self._collect_dialogue_sentences(dialogues)
        if not sentences and story:
            sentences = self._collect_story_sentences(story)
        if not sentences:
            return ""

        blocks = []
        for sentence in sentences[:2]:
            shuffled = sentence["parts"][:]
            random.shuffle(shuffled)
            word_pool = "".join(
                f"<span class=\"draggable\" draggable=\"true\">{escape(word)}</span>"
                for word in shuffled
            )
            blocks.append(
                f"""
                <div class=\"sentence-builder\">
                    <p class=\"translation\">{escape(sentence['translation'])}</p>
                    <div class=\"word-pool\">{word_pool}</div>
                    <div class=\"drop-zone\" data-correct=\"{escape(' '.join(sentence['parts']))}\">
                        <span class=\"placeholder\">Перетащите слова сюда</span>
                    </div>
                </div>
                """
            )

        return (
            "\n            <div class=\"exercise-block\" id=\"builder\">\n"
            "                <h3 class=\"exercise-title\">🧩 Конструктор предложений</h3>\n"
            + "".join(blocks)
            + "\n                <button class=\"check-btn\" data-action=\"check-builder\" type=\"button\">Проверить</button>\n"
            "            </div>\n            "
        )

    # ------------------------------------------------------------------
    # Synonym helpers
    # ------------------------------------------------------------------
    def _select_synonym_pairs(self, vocabulary: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        pairs: List[Dict[str, str]] = []
        used_words = set()

        for word in vocabulary:
            german = (word.get("german") or "").strip()
            translation = (word.get("translation") or "").strip()
            if not german or not translation:
                continue

            options = self._synonym_lookup.get(german.lower())
            if not options:
                continue
            choice = random.choice(options)
            synonym = random.choice(choice["synonyms"])
            antonym = choice["antonym"]
            antonym_translation = choice["antonym_translation"] or self._translation_for_german(antonym)
            if not synonym or not antonym:
                continue

            pairs.append(
                {
                    "word": german,
                    "synonym": synonym,
                    "translation": translation,
                    "antonym": antonym,
                    "antonym_translation": antonym_translation or "Противоположное значение",
                }
            )
            used_words.add(german.lower())
            if len(pairs) >= 3:
                break

        if len(pairs) < 3:
            fallback = [item for item in self._synonym_pool if item["word"].lower() not in used_words]
            random.shuffle(fallback)
            for item in fallback:
                synonym = random.choice(item["synonyms"])
                antonym_translation = item["antonym_translation"] or self._translation_for_german(item["antonym"])
                pairs.append(
                    {
                        "word": item["word"],
                        "synonym": synonym,
                        "translation": item["translation"],
                        "antonym": item["antonym"],
                        "antonym_translation": antonym_translation or "Противоположное значение",
                    }
                )
                used_words.add(item["word"].lower())
                if len(pairs) >= 3:
                    break

        return pairs[:3]

    def _translation_for_german(self, german: str) -> str:
        german = (german or "").strip().lower()
        if not german:
            return ""
        for entries in self._translation_map.values():
            for entry in entries:
                if entry.get("german", "").strip().lower() == german:
                    return entry.get("translation", "") or ""
        return ""

    # ------------------------------------------------------------------
    # Sentence helpers
    # ------------------------------------------------------------------
    def _collect_dialogue_sentences(
        self, dialogues: Iterable[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        sentences: List[Dict[str, Any]] = []
        for dialogue in dialogues or []:
            german = (dialogue.get("german") or "").strip()
            russian = (dialogue.get("russian") or "").strip()
            if not german or not russian:
                continue
            german_parts = [part.strip() for part in re.split(r"[.!?]+", german) if part.strip()]
            russian_parts = [part.strip() for part in re.split(r"[.!?]+", russian) if part.strip()]
            for idx, sentence in enumerate(german_parts):
                tokens = self._tokenize_sentence(sentence)
                if len(tokens) < 3:
                    continue
                translation = russian_parts[idx] if idx < len(russian_parts) else russian
                sentences.append({"parts": tokens, "translation": translation})
                if len(sentences) >= 3:
                    return sentences
        return sentences

    def _collect_story_sentences(self, story: Dict[str, Any]) -> List[Dict[str, Any]]:
        content = (story or {}).get("content")
        if not content:
            return []
        # Видаляємо HTML теги
        text = re.sub(r"<[^>]+>", " ", content)
        sentences = []
        for fragment in re.split(r"[.!?]+", text):
            fragment = fragment.strip()
            if not fragment:
                continue
            tokens = self._tokenize_sentence(fragment)
            if len(tokens) < 3:
                continue
            sentences.append({"parts": tokens, "translation": fragment})
            if len(sentences) >= 2:
                break
        return sentences

    def _tokenize_sentence(self, sentence: str) -> List[str]:
        tokens = re.findall(r"[A-Za-zÄÖÜäöüß]+(?:-[A-Za-zÄÖÜäöüß]+)?", sentence)
        return tokens

    # ------------------------------------------------------------------
    # Misc helpers
    # ------------------------------------------------------------------
    def _normalize_german_word(self, german: str) -> str:
        german = (german or "").strip()
        if not german:
            return ""
        for article in ("der ", "die ", "das ", "den ", "dem ", "des "):
            if german.lower().startswith(article):
                german = german[len(article) :]
                break
        return german.strip()


__all__ = ["ExercisesGenerator"]
