"""
Генератор карток словника з кольоровими артиклями
"""

from html import escape
from typing import Dict, List, Any


class VocabularyCardsGenerator:
    """Генерація карток словника."""
    
    def generate_vocabulary_section(self, vocabulary: List[Dict[str, Any]]) -> str:
        """Генерація секції словника з кольоровими артиклями."""
        if not vocabulary:
            return ""
            
        cards = []
        for i, word in enumerate(vocabulary):
            card = self._generate_word_card(word, i)
            if card:
                cards.append(card)
                
        if not cards:
            return ""
            
        return f"""
        <section class="vocabulary-section">
            <h2 class="section-title">
                <span class="icon">📚</span> Словник ({len(cards)} слів)
            </h2>
            
            <!-- Легенда кольорів артиклів -->
            <div class="article-color-legend">
                <span class="legend-item masculine">🔷 der = чоловічий</span>
                <span class="legend-item feminine">🔴 die = жіночий</span>
                <span class="legend-item neutral">🟡 das = середній</span>
            </div>
            
            <div class="vocabulary-grid">
                {''.join(cards)}
            </div>
        </section>
        """
        
    def _generate_word_card(self, word: Dict[str, Any], index: int = 0) -> str:
        """Генерація однієї картки слова з кольоровим артиклем."""
        german = word.get('german', '').strip()
        if not german:
            return ""
            
        # Визначаємо артикль та колір
        article_info = self._get_article_info(german)
        
        # Дані картки
        translation = escape(word.get('translation', ''))
        transcription = word.get('transcription', '')
        examples = word.get('examples', {})
        
        # HTML артикля з кольором
        if article_info['article']:
            article_html = f'<span class="{article_info["class"]}">{article_info["article"]}</span> '
            german_display = article_html + escape(article_info['word'])
            data_gender = f'data-gender="{article_info["gender"]}"'
        else:
            german_display = escape(german)
            data_gender = ''
            
        # Транскрипція
        trans_html = ''
        if transcription:
            trans_html = f'<div class="transcription">[{escape(transcription)}]</div>'
            
        # Приклади
        example_html = ''
        if examples:
            de_example = examples.get('de', '')
            ru_example = examples.get('ru', '')
            if de_example:
                example_html = f"""
                <div class="examples">
                    <div class="example-de">{escape(de_example)}</div>
                    <div class="example-ru">{escape(ru_example)}</div>
                </div>
                """
                
        # Вибір градієнта
        gradient_index = index % len(self.CARD_GRADIENTS)
        gradient = self.CARD_GRADIENTS[gradient_index]
                
        return f"""
        <div class="word-card" {data_gender} style="background: {gradient};">
            <div class="word-content">
                <div class="german">{german_display}</div>
                {trans_html}
                <div class="translation">{translation}</div>
                {example_html}
            </div>
        </div>
        """
        
    def generate_article_filter(self) -> str:
        """Генерація фільтра за артиклями."""
        return """
        <div class="article-filter">
            <button class="filter-btn active" data-filter="all">Всі слова</button>
            <button class="filter-btn" data-filter="masculine">🔷 der</button>
            <button class="filter-btn" data-filter="feminine">🔴 die</button>
            <button class="filter-btn" data-filter="neutral">🟡 das</button>
            <button class="filter-btn" data-filter="none">Без артикля</button>
        </div>
        """
        
    def generate_vocabulary_stats(self, vocabulary: List[Dict[str, Any]]) -> str:
        """Генерація статистики словника."""
        if not vocabulary:
            return ""
            
        stats = {
            'der': 0,
            'die': 0,
            'das': 0,
            'none': 0
        }
        
        for word in vocabulary:
            german = word.get('german', '').lower().strip()
            if german.startswith('der '):
                stats['der'] += 1
            elif german.startswith('die '):
                stats['die'] += 1
            elif german.startswith('das '):
                stats['das'] += 1
            else:
                stats['none'] += 1
                
        return f"""
        <div class="vocabulary-stats">
            <h3>Статистика словника:</h3>
            <ul>
                <li>🔷 der (чоловічий): {stats['der']} слів</li>
                <li>🔴 die (жіночий): {stats['die']} слів</li>
                <li>🟡 das (середній): {stats['das']} слів</li>
                <li>📝 Без артикля: {stats['none']} слів</li>
                <li><strong>Всього: {len(vocabulary)} слів</strong></li>
            </ul>
        </div>
        """
