"""Write static assets required for the generated site."""

from __future__ import annotations

from pathlib import Path


BASE_CSS = """
:root {
    --background: #f5f7fb;
    --text: #1f2933;
    --accent: #4f46e5;
    --accent-light: #6366f1;
}

body {
    margin: 0;
    font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--background);
    color: var(--text);
}

.page-container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 32px 16px 64px;
}

.lesson-header {
    background: linear-gradient(135deg, var(--accent), var(--accent-light));
    color: white;
    padding: 32px;
    border-radius: 18px;
    margin-bottom: 32px;
    box-shadow: 0 12px 32px rgba(99, 102, 241, 0.25);
}

.lesson-meta {
    display: flex;
    gap: 16px;
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    opacity: 0.85;
}

.lesson-quote {
    margin-bottom: 24px;
    padding: 24px;
    background: white;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.1);
    display: flex;
    gap: 16px;
    align-items: center;
}

.lesson-navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin: 24px 0;
}

.nav-btn {
    padding: 12px 18px;
    border-radius: 999px;
    background: white;
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
    box-shadow: 0 8px 24px rgba(79, 70, 229, 0.15);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.nav-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 36px rgba(79, 70, 229, 0.25);
}

.nav-btn.disabled {
    opacity: 0.4;
    pointer-events: none;
}

.section-title {
    font-size: 1.6rem;
    margin-bottom: 16px;
}

.lesson-story,
.lesson-dialogues,
.lesson-emotions,
.lesson-memory,
.lesson-cheatsheet {
    margin-bottom: 40px;
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
}

.dialogue-item header {
    display: flex;
    justify-content: space-between;
    font-weight: 600;
}

.dialogue-translation {
    margin-top: 6px;
    opacity: 0.75;
}

.category-header,
.hero {
    background: linear-gradient(135deg, var(--accent), var(--accent-light));
    color: white;
    padding: 48px 32px;
    text-align: center;
    border-radius: 24px;
    margin-bottom: 40px;
}

.lessons-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 24px;
}

.lesson-card,
.category-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 12px 28px rgba(79, 70, 229, 0.12);
}

.btn {
    display: inline-block;
    margin-top: 12px;
    padding: 12px 18px;
    border-radius: 999px;
    background: var(--accent);
    color: white;
    text-decoration: none;
}
"""

VOCABULARY_CSS = """
.vocabulary-section {
    margin-bottom: 40px;
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
}

.vocabulary-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
}

.word-card {
    background: linear-gradient(135deg, rgba(79,70,229,0.08), rgba(129,140,248,0.2));
    border-radius: 16px;
    padding: 18px;
    color: var(--text);
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.word-title {
    display: flex;
    align-items: baseline;
    gap: 8px;
    font-size: 1.2rem;
    font-weight: 600;
}

.word-transcription {
    opacity: 0.6;
    font-size: 0.9rem;
}

.article-der { color: #2563eb; }
.article-die { color: #db2777; }
.article-das { color: #d97706; }
"""

INDEX_CSS = """
.index-content {
    max-width: 1100px;
    margin: 0 auto;
    padding: 32px 16px 64px;
}

.category-card {
    display: grid;
    gap: 12px;
}

.category-count {
    opacity: 0.7;
}
"""

MAIN_JS = """
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.word-card').forEach((card) => {
        card.addEventListener('mouseenter', () => card.classList.add('hover'));
        card.addEventListener('mouseleave', () => card.classList.remove('hover'));
    });
});
"""


class AssetsWriter:
    """Persist CSS and JS assets for the generated site."""

    def write(self, output_dir: Path, write_file) -> None:
        css_dir = output_dir / "css"
        js_dir = output_dir / "js"

        write_file(css_dir / "style.css", BASE_CSS)
        write_file(css_dir / "vocabulary.css", VOCABULARY_CSS)
        write_file(css_dir / "index.css", INDEX_CSS)

        write_file(js_dir / "main.js", MAIN_JS)
        write_file(js_dir / "vocabulary.js", MAIN_JS)
