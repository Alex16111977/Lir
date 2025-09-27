"""HTML template snippets used by the generator."""

from __future__ import annotations

from typing import Iterable


class HTMLTemplates:
    """Provide reusable template blocks for lesson pages."""

    def lesson_document(
        self,
        *,
        title: str,
        level: str,
        head_extra: str,
        header: str,
        navigation: str,
        sections: Iterable[str],
        scripts: str,
    ) -> str:
        body = "\n".join(filter(None, sections))
        return f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {level}</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/vocabulary.css">
    <link rel="stylesheet" href="../../css/exercises.css">
    {head_extra}
</head>
<body>
    <div class="page-container">
        {header}
        {navigation}
        {body}
    </div>
    {scripts}
</body>
</html>"""

    def lesson_header(self, *, title: str, level: str, word_count: int) -> str:
        return f"""
        <header class="lesson-header">
            <div class="lesson-meta">
                <span class="lesson-level">{level.upper()}</span>
                <span class="lesson-words">📚 {word_count} слів</span>
            </div>
            <h1>{title}</h1>
        </header>
        """

    def quote_section(self, quote: str, icon: str) -> str:
        if not quote:
            return ""
        icon_html = f'<span class="quote-icon">{icon}</span>' if icon else ""
        return f"""
        <section class="lesson-quote">
            {icon_html}
            <blockquote>{quote}</blockquote>
        </section>
        """

    def emotions_section(self, emotions: Iterable[str]) -> str:
        items = [item for item in emotions if item]
        if not items:
            return ""
        return f"""
        <section class="lesson-emotions">
            <h2>Емоції сцени</h2>
            <ul>{''.join(f'<li>{value}</li>' for value in items)}</ul>
        </section>
        """

    def story_section(self, title: str, content: str, peak: str) -> str:
        if not content:
            return ""
        header = f"<h2>{title}</h2>" if title else ""
        peak_block = f'<aside class="story-peak">{peak}</aside>' if peak else ""
        return f"""
        <section class="lesson-story">
            {header}
            <div class="story-content">{content}</div>
            {peak_block}
        </section>
        """

    def dialogues_section(self, rows: Iterable[str]) -> str:
        rows = list(filter(None, rows))
        if not rows:
            return ""
        return f"""
        <section class="lesson-dialogues">
            <h2>Діалоги</h2>
            <div class="dialogue-list">
                {''.join(rows)}
            </div>
        </section>
        """

    def dialogue_row(self, *, character: str, emotion: str, german: str, russian: str) -> str:
        return f"""
            <article class="dialogue-item">
                <header>
                    <span class="dialogue-character">{character}</span>
                    <span class="dialogue-emotion">{emotion}</span>
                </header>
                <p class="dialogue-line">{german}</p>
                <p class="dialogue-translation">{russian}</p>
            </article>
        """

    def memory_section(self, title: str, content: str) -> str:
        if not content:
            return ""
        return f"""
        <section class="lesson-memory">
            <h2>{title or 'Пам\'ятка'}</h2>
            <div class="memory-content">{content}</div>
        </section>
        """

    def cheat_sheet_section(self, data: str) -> str:
        if not data:
            return ""
        return f"""
        <section class="lesson-cheatsheet">
            <h2>🧠 Шпаргалка</h2>
            <div class="cheatsheet-content">{data}</div>
        </section>
        """

    def index_page(self, *, hero: str, categories: Iterable[str]) -> str:
        return f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LIR – Навчання німецької</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/index.css">
</head>
<body>
    {hero}
    <main class="index-content">
        {''.join(categories)}
    </main>
</body>
</html>"""

    def hero_block(self) -> str:
        return """
        <section class="hero">
            <h1>LIR – Learn It Right</h1>
            <p>Вивчайте німецьку мову через сюжет Короля Ліра.</p>
        </section>
        """

    def category_card(self, *, title: str, description: str, url: str, count: int) -> str:
        return f"""
        <section class="category-card">
            <h2>{title}</h2>
            <p>{description}</p>
            <p class="category-count">{count} уроків</p>
            <a class="btn" href="{url}">Відкрити</a>
        </section>
        """

    def category_index(self, *, title: str, lessons: Iterable[str]) -> str:
        return f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/index.css">
</head>
<body>
    <header class="category-header">
        <h1>{title}</h1>
        <a href="../index.html" class="btn">← На головну</a>
    </header>
    <main class="lessons-grid">
        {''.join(lessons)}
    </main>
</body>
</html>"""

    def category_lesson_card(self, *, title: str, url: str, words: int) -> str:
        return f"""
        <article class="lesson-card">
            <h3>{title}</h3>
            <p>📚 {words} слів</p>
            <a href="{url}" class="btn">Перейти</a>
        </article>
        """

    def scripts_block(self) -> str:
        return """
    <script src="../../js/vocabulary.js"></script>
    <script src="../../js/exercises.js"></script>
    """
