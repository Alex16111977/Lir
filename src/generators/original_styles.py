"""
Оригінальні стилі для генерації HTML з JSON
Зберігає всі градієнти та дизайн як в оригінальному сайті
"""

MAIN_PAGE_STYLES = '''
body {
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
'''

LESSON_STYLES = '''
body {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Georgia', serif;
    min-height: 100vh;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.scene-moment {
    background: linear-gradient(135deg, #FFD700, #8B4513);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.scene-moment::before {
    content: '👑';
    position: absolute;
    font-size: 200px;
    opacity: 0.1;
    right: -50px;
    top: -50px;
    transform: rotate(-15deg);
}

.scene-moment h1 {
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    margin: 0 0 20px 0;
    font-size: 2.5em;
}

.shakespeare-quote {
    color: #fff;
    font-style: italic;
    font-size: 1.3em;
    margin: 15px 0;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
}

.emotion-tags {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.emotion-tag {
    display: inline-block;
    background: rgba(255,255,255,0.3);
    padding: 5px 15px;
    border-radius: 20px;
    margin: 5px;
    font-weight: bold;
    color: white;
    backdrop-filter: blur(5px);
}

.section {
    background: white;
    border-radius: 15px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.section-title {
    font-size: 1.5em;
    color: #333;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-number {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}

.word-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.word-card {
    background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%); /* Базовий градієнт */
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transform: translateY(0);
    transition: all 0.3s;
    overflow-wrap: break-word;
    word-wrap: break-word;
    word-break: break-all;
    min-width: 0;
    overflow: hidden;
    position: relative;
    border: 1px solid transparent;
}

.word-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

/* Градієнтний фон для чоловічого роду */
.word-card[data-gender="masculine"] {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); /* Світло-блакитний градієнт */
    border: 1px solid #93c5fd;
}

.word-card[data-gender="masculine"]:hover {
    background: linear-gradient(135deg, #bfdbfe 0%, #93c5fd 100%);
    box-shadow: 0 10px 30px rgba(43, 108, 176, 0.3);
}

/* Градієнтний фон для жіночого роду */
.word-card[data-gender="feminine"] {
    background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); /* Світло-рожевий градієнт */
    border: 1px solid #fca5a5;
}

.word-card[data-gender="feminine"]:hover {
    background: linear-gradient(135deg, #fecaca 0%, #fca5a5 100%);
    box-shadow: 0 10px 30px rgba(220, 38, 38, 0.3);
}

/* Градієнтний фон для середнього роду */
.word-card[data-gender="neutral"] {
    background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); /* Світло-зелений градієнт */
    border: 1px solid #6ee7b7;
}

.word-card[data-gender="neutral"]:hover {
    background: linear-gradient(135deg, #a7f3d0 0%, #6ee7b7 100%);
    box-shadow: 0 10px 30px rgba(22, 163, 74, 0.3);
}

.word-german {
    font-size: 1.4em;
    font-weight: bold;
    color: #111827; /* Дуже темний текст для контрасту */
    margin-bottom: 10px;
    word-break: break-all;
    hyphens: auto;
    overflow-wrap: break-word;
    line-height: 1.3;
    max-width: 100%;
    text-shadow: 0 1px 2px rgba(255,255,255,0.8); /* Легка біла тінь для читабельності */
}

.word-transcription {
    color: #4b5563; /* Темно-сірий текст */
    font-size: 1em;
    margin-bottom: 10px;
    font-style: italic;
    word-break: break-all;
    overflow-wrap: break-word;
    max-width: 100%;
}

.word-russian {
    color: #1f2937; /* Темний текст */
    font-size: 1.2em;
    font-weight: 500;
    margin-bottom: 10px;
    word-break: break-word;
    overflow-wrap: break-word;
}

.word-type {
    display: inline-block;
    background: rgba(255, 255, 255, 0.7); /* Напівпрозорий білий фон */
    backdrop-filter: blur(5px);
    padding: 3px 10px;
    border-radius: 10px;
    color: #374151;
    font-size: 0.9em;
    margin-bottom: 15px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    font-weight: 600;
}

.character-voice {
    border-left: 5px solid #764ba2;
    padding-left: 15px;
    margin: 15px 0;
    font-style: italic;
    background: rgba(255,255,255,0.95);
    padding: 15px;
    border-radius: 10px;
    color: #333;
    word-break: break-word;
}

.gesture-anchor {
    background: #fff3cd;
    border: 2px dashed #ffc107;
    padding: 12px;
    border-radius: 10px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin: 15px 0;
    color: #333;
    word-break: break-word;
    flex-wrap: wrap;
}

.gesture-icon {
    font-size: 36px;
    animation: pulse 2s infinite;
    flex-shrink: 0;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

/* Кольорові артиклі - оновлена палітра */
.article-der {
    color: #2B6CB0; /* Синій для der */
    font-weight: 700;
    font-size: 1.1em;
    display: inline-block;
    margin-right: 4px;
}

.article-die {
    color: #DC2626; /* Червоний для die */
    font-weight: 700;
    font-size: 1.1em;
    display: inline-block;
    margin-right: 4px;
}

.article-das {
    color: #16A34A; /* Зелений для das (замість жовтого) */
    font-weight: 700;
    font-size: 1.1em;
    display: inline-block;
    margin-right: 4px;
}

/* Маленькі іконки роду */
.gender-icon {
    font-size: 0.9em;
    opacity: 0.6;
    margin-left: 8px;
    display: inline-block;
}

.word-card[data-gender="masculine"] .gender-icon {
    color: #2B6CB0;
}

.word-card[data-gender="feminine"] .gender-icon {
    color: #DC2626;
}

.word-card[data-gender="neutral"] .gender-icon {
    color: #16A34A;
}

/* Легенда артиклів */
.article-legend {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin: 20px 0;
    padding: 16px;
    background: #f9fafb;
    border-radius: 12px;
}

/* Кольорова легенда для вправ */
.article-color-legend {
    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 12px;
    background: #f9fafb;
    border-radius: 8px;
    margin-bottom: 16px;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 600;
    font-size: 0.95em;
}

.legend-item.masculine {
    color: #2B6CB0;
}

.legend-item.feminine {
    color: #DC2626;
}

.legend-item.neutral {
    color: #16A34A;
}

.legend-card {
    display: flex;
    align-items: center;
    gap: 8px;
}

.legend-color {
    width: 24px;
    height: 24px;
    border-radius: 6px;
}

.legend-color.masculine {
    background: #2B6CB0;
}

.legend-color.feminine {
    background: #DC2626;
}

.legend-color.neutral {
    background: #16A34A;
}

/* Кнопки артиклів у вправах */
.article-buttons button {
    background: white !important;
    border: 2px solid #e0e0e0;
    transition: all 0.3s;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: 600;
}

.article-buttons button[data-article="der"] {
    border-color: #2B6CB0;
    color: #2B6CB0;
}

.article-buttons button[data-article="die"] {
    border-color: #DC2626;
    color: #DC2626;
}

.article-buttons button[data-article="das"] {
    border-color: #16A34A;
    color: #16A34A;
}

/* Hover - легке заповнення */
.article-buttons button[data-article="der"]:hover {
    background: rgba(43, 108, 176, 0.1) !important;
}

.article-buttons button[data-article="die"]:hover {
    background: rgba(220, 38, 38, 0.1) !important;
}

.article-buttons button[data-article="das"]:hover {
    background: rgba(22, 163, 74, 0.1) !important;
}

/* Правильна відповідь */
.article-buttons button.correct {
    color: white !important;
}

.article-buttons button[data-article="der"].correct {
    background: #2B6CB0 !important;
}

.article-buttons button[data-article="die"].correct {
    background: #DC2626 !important;
}

.article-buttons button[data-article="das"].correct {
    background: #16A34A !important;
    color: white !important;
}

/* Адаптивные стили для мобильных устройств */
@media (max-width: 768px) {
    .word-cards {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    .word-card {
        padding: 15px;
        max-width: 100%;
    }
    
    .word-german {
        font-size: 1.2em;
    }
    
    .word-transcription {
        font-size: 0.9em;
    }
    
    .word-russian {
        font-size: 1em;
    }
    
    .gesture-anchor {
        flex-direction: column;
        gap: 8px;
        padding: 10px;
    }
    
    .character-voice {
        padding: 12px;
        padding-left: 12px;
    }
}

@media (max-width: 500px) {
    .word-cards {
        grid-template-columns: 1fr;
        gap: 12px;
    }
    
    .word-card {
        padding: 12px;
        min-width: 100%;
        box-sizing: border-box;
    }
    
    .word-german {
        font-size: 1.1em;
        word-break: break-all;
    }
    
    .word-transcription {
        font-size: 0.85em;
    }
    
    .word-russian {
        font-size: 0.9em;
    }
    
    .word-type {
        font-size: 0.8em;
    }
    
    .article-der,
    .article-die,
    .article-das {
        font-size: 0.9em;
    }
}

.navigation {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
}

.navigation a {
    color: white;
    text-decoration: none;
    font-size: 1.1em;
    padding: 10px 20px;
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    transition: 0.3s;
}

.navigation a:hover {
    background: rgba(255,255,255,0.2);
}
'''

NAVIGATION_STYLES = '''
body {
    font-family: Georgia, serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #667eea, #764ba2);
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.header {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 15px;
    margin-bottom: 30px;
    text-align: center;
}

.header h1 {
    color: white;
    margin: 0;
    font-size: 2.5em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.header p {
    color: rgba(255,255,255,0.9);
    margin: 10px 0 0 0;
    font-size: 1.2em;
}

.navigation {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
}

.navigation a {
    color: white;
    text-decoration: none;
    font-size: 1.1em;
    padding: 10px 20px;
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    transition: 0.3s;
}

.navigation a:hover {
    background: rgba(255,255,255,0.2);
}

.groups {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.group {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}

.group-header {
    background: linear-gradient(135deg, #f093fb, #f5576c);
    padding: 20px;
    color: white;
}

.group-header h2 {
    margin: 0;
    font-size: 1.8em;
}

.group-lessons {
    padding: 20px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 15px;
}

.lesson-card {
    display: block;
    padding: 15px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    text-decoration: none;
    border-radius: 10px;
    transition: transform 0.3s;
}

.lesson-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

.lesson-number {
    font-size: 0.9em;
    opacity: 0.8;
    margin-bottom: 5px;
}

.lesson-title {
    font-size: 1.1em;
    font-weight: bold;
}
'''
