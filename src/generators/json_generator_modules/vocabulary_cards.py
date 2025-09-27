"""Vocabulary section generator."""

from __future__ import annotations

from html import escape
from typing import Any, Dict, Iterable


ARTICLE_CLASSES = {
    "der": ("article-der", "🔷"),
    "die": ("article-die", "🔴"),
    "das": ("article-das", "🟡"),
}


def _split_article(german: str) -> Dict[str, str]:
    parts = german.split(" ", 1)
    if len(parts) == 2 and parts[0].lower() in ARTICLE_CLASSES:
        article = parts[0].lower()
        return {
            "article": article,
            "word": parts[1],
            "css": ARTICLE_CLASSES[article][0],
            "icon": ARTICLE_CLASSES[article][1],
        }
    return {"article": "", "word": german, "css": "", "icon": ""}


class VocabularyCardsGenerator:
    """Render vocabulary cards with article highlighting."""

    def _vocabulary_section(self, vocabulary: Iterable[Dict[str, Any]]) -> str:
        items = [word for word in vocabulary if word.get("german")]
        if not items:
            return ""

        cards = [self._word_card(word, index) for index, word in enumerate(items)]
        return f"""
        <section class="vocabulary-section">
            <h2 class="section-title">📚 Словник ({len(cards)})</h2>
            <div class="vocabulary-grid">
                {''.join(cards)}
            </div>
        </section>
        """

    def _word_card(self, word: Dict[str, Any], index: int) -> str:
        german = word.get("german", "").strip()
        info = _split_article(german)
        translation = escape(word.get("translation", ""))
        transcription = escape(word.get("transcription", "")) if word.get("transcription") else ""

        voice = word.get("character_voice", {})
        voice_block = ""
        if voice.get("german") and voice.get("russian"):
            voice_block = f"""
                <div class="voice-line">
                    <span class="voice-de">{escape(voice['german'])}</span>
                    <span class="voice-ru">{escape(voice['russian'])}</span>
                </div>
            """

        gesture = word.get("gesture", {})
        gesture_block = ""
        if gesture.get("gesture"):
            gesture_block = f"""
                <div class="gesture">
                    <span class="gesture-icon">{escape(gesture.get('icon', ''))}</span>
                    <span>{escape(gesture['gesture'])}</span>
                </div>
            """

        article_html = ""
        if info["article"]:
            article_html = f'<span class="{info["css"]}">{info["icon"]} {info["article"]}</span>'

        return f"""
        <article class="word-card" data-index="{index}">
            <header class="word-title">
                {article_html}
                <span class="word-german">{escape(info['word'])}</span>
                <span class="word-transcription">{transcription}</span>
            </header>
            <div class="word-body">
                <p class="word-translation">{translation}</p>
                {voice_block}
                {gesture_block}
            </div>
        </article>
        """
