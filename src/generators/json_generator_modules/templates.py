"""
HTML Templates - шаблони HTML сторінок
"""


class HTMLTemplates:
    """Шаблони для генерації HTML."""
    
    @staticmethod
    def get_head(title: str, level: str = "") -> str:
        """HTML head секція."""
        return f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="LIR - Вивчайте німецьку через Короля Ліра">
    <title>{title}{' | ' + level if level else ''}</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/vocabulary.css">
    <link rel="stylesheet" href="../../css/exercises.css">
        """
        
    @staticmethod
    def get_footer() -> str:
        """HTML footer."""
        return """
    <footer class="main-footer">
        <div class="footer-content">
            <div class="footer-section">
                <h4>LIR - Learn It Right</h4>
                <p>Інноваційна платформа для вивчення німецької мови через класичну літературу</p>
            </div>
            <div class="footer-section">
                <h4>Ресурси</h4>
                <ul>
                    <li><a href="/book">Веб-читалка</a></li>
                    <li><a href="/exercises">Вправи</a></li>
                    <li><a href="/vocabulary">Словник</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Контакти</h4>
                <p>© 2025 LIR Project</p>
            </div>
        </div>
    </footer>
        """
        
    @staticmethod
    def get_scripts() -> str:
        """JavaScript підключення."""
        return """
    <script src="../../js/vocabulary.js"></script>
    <script src="../../js/exercises.js"></script>
    <script src="../../js/navigation.js"></script>
        """
