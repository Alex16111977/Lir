"""HTML rendering utilities for the modular book generator."""

from __future__ import annotations


class HtmlPageBuilder:
    """Render chapter and index pages."""

    def _generate_html_pages(self) -> None:
        for index, chapter in enumerate(self.chapters):
            chapter_html = self._create_chapter_html(chapter, index, len(self.chapters))
            chapter_file = self.output_dir / "chapters" / f"chapter-{index + 1:02d}.html"
            self._write_text(chapter_file, chapter_html)

    def _create_chapter_html(self, chapter, chapter_index: int, total_chapters: int) -> str:
        prev_link = ""
        next_link = ""

        if chapter_index > 0:
            prev_link = (
                f'<a href="chapter-{chapter_index:02d}.html" class="nav-prev">← Vorherige</a>'
            )

        if chapter_index < total_chapters - 1:
            next_link = (
                f'<a href="chapter-{chapter_index + 2:02d}.html" class="nav-next">Nächste →</a>'
            )

        template = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter['title']} - König Lear</title>
    <link rel="stylesheet" href="../assets/css/book.css">
    <link rel="stylesheet" href="../assets/css/reader.css">
</head>
<body>
    <nav class="book-nav">
        <div class="nav-left">
            <a href="../index.html" class="nav-home">📖 Hauptseite</a>
        </div>
        <div class="nav-center">
            <span class="chapter-info">Kapitel {chapter_index + 1} von {total_chapters}</span>
        </div>
        <div class="nav-right">
            {prev_link}
            {next_link}
        </div>
    </nav>

    <main class="chapter-content">
        <h1 class="chapter-title">{chapter['title']}</h1>
        <div class="text-content" id="text-content">
            {chapter['content']}
        </div>
    </main>

    <aside class="reading-tools">
        <button id="font-size-up" title="Schrift vergrößern">A+</button>
        <button id="font-size-down" title="Schrift verkleinern">A-</button>
        <button id="toggle-theme" title="Thema wechseln">🌙</button>
        <button id="fullscreen" title="Vollbild">⛶</button>
        <button id="bookmark" title="Lesezeichen">🔖</button>
    </aside>

    <div class="progress-bar">
        <div class="progress-fill" id="progress-fill"></div>
    </div>

    <script src="../assets/js/reader.js"></script>
    <script src="../assets/js/navigation.js"></script>
</body>
</html>"""
        return template

    def _generate_index_page(self) -> None:
        chapters_html = ""
        for index, chapter in enumerate(self.chapters):
            chapters_html += f"""
            <div class="chapter-card">
                <div class="chapter-number">Kapitel {index + 1}</div>
                <h3 class="chapter-link-title">{chapter['title']}</h3>
                <div class="chapter-meta">
                    <span>Seiten: {chapter['pages'][0] + 1}-{chapter['pages'][-1] + 1}</span>
                    <span>({len(chapter['pages'])} Seiten)</span>
                </div>
                <a href="chapters/chapter-{index + 1:02d}.html" class="chapter-link">Lesen →</a>
            </div>
            """

        index_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>König Lear - William Shakespeare</title>
    <link rel="stylesheet" href="assets/css/book.css">
    <link rel="stylesheet" href="assets/css/index.css">
</head>
<body>
    <header class="book-header">
        <div class="book-cover">
            <h1 class="book-title">König Lear</h1>
            <p class="book-author">William Shakespeare</p>
            <div class="book-meta">
                <span>Seiten: {self.metadata.get('pages', 0)}</span>
                <span>Generiert: {self.metadata['generated'][:10]}</span>
            </div>
        </div>
    </header>

    <nav class="book-navigation">
        <a href="../index.html" class="back-to-main">← Zurück zum Hauptportal</a>
    </nav>

    <main class="book-main">
        <section class="table-of-contents">
            <h2>Inhaltsverzeichnis</h2>
            <div class="chapters-grid">
                {chapters_html}
            </div>
        </section>

        <section class="reading-features">
            <h2>Lesefunktionen</h2>
            <div class="features-grid">
                <div class="feature">
                    <span class="feature-icon">🔍</span>
                    <h3>Suche</h3>
                    <p>Volltextsuche im gesamten Buch</p>
                </div>
                <div class="feature">
                    <span class="feature-icon">🔖</span>
                    <h3>Lesezeichen</h3>
                    <p>Speichern Sie Ihre Leseposition</p>
                </div>
                <div class="feature">
                    <span class="feature-icon">🎨</span>
                    <h3>Themen</h3>
                    <p>Hell und Dunkel Modi</p>
                </div>
                <div class="feature">
                    <span class="feature-icon">📱</span>
                    <h3>Responsive</h3>
                    <p>Optimiert für alle Geräte</p>
                </div>
            </div>
        </section>
    </main>

    <footer class="book-footer">
        <p>Generiert am {self.metadata['generated'][:10]}</p>
        <p>Lir Website Generator - Deutsch durch König Lear</p>
    </footer>

    <script src="assets/js/book-index.js"></script>
</body>
</html>"""

        index_file = self.output_dir / "index.html"
        self._write_text(index_file, index_html)
