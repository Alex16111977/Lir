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
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 25px;
}

.word-card {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transform: translateY(0);
    transition: transform 0.3s;
}

.word-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}

.word-german {
    font-size: 2em;
    font-weight: bold;
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    margin-bottom: 10px;
}

.word-transcription {
    color: #fff;
    font-size: 1.2em;
    margin-bottom: 10px;
    opacity: 0.9;
}

.word-russian {
    color: #fff;
    font-size: 1.3em;
    font-weight: 500;
    margin-bottom: 10px;
}

.word-type {
    display: inline-block;
    background: rgba(255,255,255,0.3);
    padding: 3px 10px;
    border-radius: 10px;
    color: white;
    font-size: 0.9em;
    margin-bottom: 15px;
}

.character-voice {
    border-left: 5px solid #764ba2;
    padding-left: 20px;
    margin: 20px 0;
    font-style: italic;
    background: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 10px;
    color: #333;
}

.gesture-anchor {
    background: #fff3cd;
    border: 2px dashed #ffc107;
    padding: 15px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    gap: 15px;
    margin: 15px 0;
    color: #333;
}

.gesture-icon {
    font-size: 40px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
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
