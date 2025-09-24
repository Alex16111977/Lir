"""
CSS Generator - збереження оригінальних стилів
"""

from pathlib import Path
import config

class CSSGenerator:
    """Генератор CSS стилів"""
    
    def __init__(self, logger):
        self.logger = logger
        self.styles = config.MODERN_STYLES
    
    def generate(self, output_path, collected_styles=None):
        """Згенерувати CSS файли"""
        
        try:
            # Створити основний style.css з оригінальним дизайном
            main_css_path = output_path.parent.parent / "css" / "style.css"
            main_css_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Оригінальний стиль
            main_css = """body {
    font-family: Georgia, serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    min-height: 100vh;
}

.header {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding: 30px;
    text-align: center;
    color: white;
}

.header h1 {
    font-size: 2.5em;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.container {
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
}

.levels {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
    gap: 30px;
}

.level-card {
    background: white;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.level-header {
    padding: 30px;
    color: white;
    text-align: center;
}

.level-a2 .level-header {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.level-b1 .level-header {
    background: linear-gradient(135deg, #e74c3c, #c0392b);
}

.level-header h2 {
    margin: 0 0 10px 0;
    font-size: 2em;
}

.level-badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    padding: 5px 15px;
    border-radius: 20px;
    font-weight: bold;
}

.level-content {
    padding: 30px;
}

.level-content h3 {
    color: #333;
    margin: 0 0 15px 0;
}

.level-content ul {
    list-style: none;
    padding: 0;
    margin: 20px 0;
}

.level-content li {
    padding: 8px 0;
    color: #555;
}

.level-button {
    display: block;
    width: 100%;
    padding: 15px;
    text-align: center;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
    font-size: 1.1em;
    margin-top: 20px;
}

.level-a2 .level-button {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.level-b1 .level-button {
    background: linear-gradient(135deg, #e74c3c, #c0392b);
}

.level-button:hover {
    transform: scale(1.05);
    transition: 0.3s;
}

/* Стилі для внутрішніх сторінок */
.wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background: white;
    min-height: 100vh;
}

.navigation {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}

.navigation a {
    color: #667eea;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 6px;
    transition: all 0.3s;
}

.navigation a:hover {
    background: #667eea;
    color: white;
}

.lesson-header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 30px;
    border-radius: 12px;
    margin-bottom: 30px;
}

.lesson-header h1 {
    margin: 0 0 20px 0;
    font-size: 2.5em;
}

blockquote {
    background: rgba(255,255,255,0.1);
    border-left: 4px solid white;
    padding: 20px;
    margin: 20px 0;
    font-style: italic;
}

.emotions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.emotion {
    background: rgba(255,255,255,0.2);
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9rem;
}

/* Словарь */
.vocabulary {
    padding: 30px;
}

.vocabulary h2 {
    color: #333;
    margin-bottom: 30px;
}

.words {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
}

.word {
    background: #f7f9fc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    transition: all 0.3s;
}

.word:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(102,126,234,0.15);
}

.word-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

.word-number {
    width: 40px;
    height: 40px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}

.german {
    font-size: 1.8rem;
    font-weight: bold;
    color: #2d3748;
}

.transcription {
    color: #718096;
    font-style: italic;
    margin-bottom: 10px;
}

.translation {
    font-size: 1.2rem;
    color: #4a5568;
    margin-bottom: 10px;
}

.type {
    display: inline-block;
    background: #edf2f7;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    margin-bottom: 10px;
}

.character-voice {
    background: linear-gradient(135deg, #f7fafc, #edf2f7);
    border-left: 3px solid #667eea;
    padding: 10px;
    margin: 15px 0;
    border-radius: 0 8px 8px 0;
}

.character {
    font-weight: bold;
    color: #667eea;
    margin-bottom: 5px;
}

.voice-german {
    font-style: italic;
    margin-bottom: 3px;
}

.voice-russian {
    color: #718096;
    font-size: 0.9rem;
}

.gesture {
    background: #f7fafc;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
}

.gesture-icon {
    font-size: 1.5rem;
    margin-right: 10px;
}

.gesture-emotion {
    color: #764ba2;
    font-weight: bold;
    margin: 5px 0;
}

.association {
    color: #718096;
    font-style: italic;
    font-size: 0.9rem;
}

/* Категории */
.category-header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 40px;
    border-radius: 12px;
    margin-bottom: 30px;
    text-align: center;
}

.lessons {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}

.lesson-link {
    background: white;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    text-decoration: none;
    color: #2d3748;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: all 0.3s;
}

.lesson-link:hover {
    border-color: #667eea;
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(102,126,234,0.2);
}

.lesson-icon {
    font-size: 2rem;
    margin-bottom: 10px;
}

.lesson-title {
    font-weight: bold;
    margin-bottom: 10px;
}

.lesson-words {
    color: #718096;
    font-size: 0.9rem;
}

footer {
    text-align: center;
    padding: 40px 20px 20px;
    color: #718096;
    margin-top: 50px;
}
"""
            
            with open(main_css_path, 'w', encoding='utf-8') as f:
                f.write(main_css)
            
            # Створити modern.css
            css_content = self._build_modern_css(collected_styles)
            
            # Створити папку
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Зберегти
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(css_content)
            
            self.logger.success(f"CSS згенеровано: {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Помилка генерації CSS: {e}")
            return False
    
    def _build_modern_css(self, collected_styles):
        """Побудувати modern.css контент"""
        
        css = """/* Lir Modern CSS - Додаткові стилі */

/* Анімації */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animated {
    animation: fadeIn 0.5s ease-out;
}

/* Додаткові утиліти */
.text-center {
    text-align: center;
}

.mt-20 {
    margin-top: 20px;
}

.mb-20 {
    margin-bottom: 20px;
}

.hidden {
    display: none;
}

/* Адаптивність */
@media (max-width: 768px) {
    .levels {
        grid-template-columns: 1fr;
    }
    
    .words {
        grid-template-columns: 1fr;
    }
    
    h1 {
        font-size: 1.8rem;
    }
    
    h2 {
        font-size: 1.5rem;
    }
}
"""
        
        return css
