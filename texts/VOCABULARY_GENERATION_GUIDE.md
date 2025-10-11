# 📚 ПОВНИЙ ОПИС ГЕНЕРАЦІЇ ТЕМАТИЧНОГО СЛОВАРЯ
**Файл: thematic_vocabulary_full.html**  
**Версія: 3.0**  
**Дата: 10.10.2025**  
**Розмір: ~125 KB**  
**Слів: 45+ (можливо розширення до 300+)**

---

## 🎯 ЗАГАЛЬНИЙ ОГЛЯД

### Що це за файл?
`F:\AiKlientBank\Lir\texts\thematic_vocabulary_full.html` - це повний тематичний словник німецької мови для вивчення через тексти "Короля Ліра".

### Основні характеристики:
- **13 тематичних категорій** (їжа, комунікація, транспорт, мистецтво, тощо)
- **45+ німецьких слів** рівня A2-B1 (можливість розширення до 300+)
- **Інтерактивні посилання** на тексти з прикладами
- **Адаптивний дизайн** (десктоп + мобільні)
- **Градієнтні стилі** (фіолетові тони)
- **Smooth scroll** до розділів

---

## 📁 СТРУКТУРА ПРОЕКТУ

### Головні файли:

```
F:\AiKlientBank\Lir\
├── test/
│   ├── vocabulary_dict.json              # 🔑 ГОЛОВНИЙ СЛОВНИК
│   ├── doc_files_mapping.json            # Маппінг реальних назв текстів
│   ├── generate_full_vocabulary.py       # 🚀 ОСНОВНИЙ ГЕНЕРАТОР
│   ├── generate_tables.py                # Генерація HTML таблиць
│   ├── categorize_vocabulary.py          # Розподіл слів по темах
│   ├── extract_vocabulary_a2_b1.py       # Витягування лексики з текстів
│   └── analyze_doc_files.py              # Аналіз вихідних .doc файлів
│
├── texts/
│   ├── thematic_vocabulary_full.html     # 📄 РЕЗУЛЬТАТ ГЕНЕРАЦІЇ
│   └── Группа 1/                         # Вихідні німецькі тексти (.doc)
│
└── data/
    └── [JSON файли уроків]               # Структуровані дані уроків
```

---

## 🔑 КЛЮЧОВІ ФАЙЛИ

### 1. vocabulary_dict.json
**Розташування:** `F:\AiKlientBank\Lir\test\vocabulary_dict.json`  
**Призначення:** Головний словник з усіма словами та прикладами

**Структура:**
```json
{
  "theme-food": {
    "name": "Еда и напитки",
    "color": "#FF6B6B",
    "emoji": "🍽️",
    "words": [
      {
        "german": "das Getränk, -e",
        "russian": "напиток",
        "examples": [
          {
            "text_id": "text-pumpkin",
            "text_title": "Pumpkin Spice Latte",
            "phrase": "ein beliebtes Getränk im Herbst"
          }
        ]
      }
    ]
  },
  "theme-communication": { ... },
  "theme-transport": { ... }
}
```

**13 тем в словнику:**
1. `theme-food` 🍽️ - Їжа та напої
2. `theme-communication` 💬 - Комунікація
3. `theme-transport` 🚗 - Транспорт
4. `theme-art` 🎨 - Мистецтво та культура
5. `theme-languages` 🗣️ - Мови
6. `theme-science` 🔬 - Наука та технології
7. `theme-geography` 🌍 - Географія та подорожі
8. `theme-history` 📜 - Історія
9. `theme-verbs` ⚡ - Дієслова
10. `theme-adjectives` ✨ - Прикметники
11. `theme-time` ⏰ - Час та числа
12. `theme-measurements` 📏 - Виміри та кількість
13. `theme-abstract` 💭 - Абстрактні поняття

### 2. doc_files_mapping.json
**Розташування:** `F:\AiKlientBank\Lir\test\doc_files_mapping.json`  
**Призначення:** Маппінг ID текстів до реальних назв

**Структура:**
```json
{
  "text-1": {
    "title": "Der Pumpkin Spice Latte",
    "file_path": "F:\\AiKlientBank\\Lir\\texts\\Группа 1\\Text1.doc",
    "file_size": 12.5
  },
  "text-2": { ... }
}
```

### 3. generate_full_vocabulary.py
**Розташування:** `F:\AiKlientBank\Lir\test\generate_full_vocabulary.py`  
**Призначення:** Основний скрипт генерації HTML

**Що робить:**
1. Завантажує `vocabulary_dict.json`
2. Завантажує `doc_files_mapping.json`
3. Генерує HTML з:
   - Оглавленням (TOC) з карточками тем
   - Таблицями слів для кожної теми
   - Інтерактивними посиланнями
4. Зберігає в `texts/thematic_vocabulary_full.html`

---

## 🚀 ПРОЦЕС ГЕНЕРАЦІЇ

### Крок 1: Підготовка даних

#### 1.1. Аналіз вихідних .doc файлів
```python
# Файл: test/analyze_doc_files.py
# Призначення: Сканування папки texts/Группа 1/

Результат: doc_files_mapping.json
```

**Що робить:**
- Сканує папку `texts/Группа 1/`
- Знаходить всі файли `*.doc`
- Створює маппінг: `text-id` → `{title, file_path, file_size}`

**Запуск:**
```python
import subprocess
import sys

subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\test\analyze_doc_files.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)
```

#### 1.2. Витягування текстів з .doc
```python
# Файл: test/extract_doc_content.py (якщо існує)
# Призначення: Читання вмісту .doc файлів

Використовує: python-docx library
```

#### 1.3. Витягування лексики A2-B1
```python
# Файл: test/extract_vocabulary_a2_b1.py
# Призначення: Витягування німецьких слів

ВИКЛЮЧАЄ слова A1 (базова лексика):
- der, die, das, ein, eine
- ich, du, er, sie, es
- sein, haben, werden
- und, oder, aber
- ja, nein, nicht
```

**Що робить:**
1. Читає тексти з .doc файлів
2. Витягує всі німецькі слова (regex: `[a-zA-ZäöüÄÖÜß]+`)
3. Фільтрує:
   - Слова коротші 4 символів
   - Базові слова A1
4. Підраховує частоту
5. Зберігає контексти (приклади з текстів)
6. Створює `vocabulary_a2_b1.json` (топ-300 слів)

#### 1.4. Розподіл слів по темах
```python
# Файл: test/categorize_vocabulary.py
# Призначення: Автоматична категоризація

Алгоритм:
1. Для кожної теми є ключові слова (keywords)
2. Перевірка слова на збіг з keywords
3. Перевірка контексту (приклади) на збіг
4. Якщо 2+ збігів → присвоюємо тему
5. Інакше → "theme-abstract" (за замовчуванням)
```

**Ключові слова для тем:**
```python
THEME_KEYWORDS = {
    "theme-food": [
        'essen', 'trinken', 'getränk', 'käse', 'brot', 
        'fleisch', 'restaurant', 'küche', 'lecker', ...
    ],
    "theme-communication": [
        'telefonieren', 'sprechen', 'sagen', 'gespräch', 
        'nachricht', 'brief', 'email', ...
    ],
    # ... інші теми
}
```

### Крок 2: Генерація HTML

#### 2.1. Основний генератор
```python
# Файл: test/generate_full_vocabulary.py
# Функція: main()

Послідовність:
1. load_text_mapping()      # Завантаження маппінгу текстів
2. load vocabulary_dict.json # Завантаження словника
3. generate_html_header()    # HTML початок + CSS
4. generate_toc()            # Оглавлення з карточками
5. generate_tables()         # Таблиці слів
6. generate_html_footer()    # HTML кінець
7. save to thematic_vocabulary_full.html
```

#### 2.2. Генерація оглавлення (TOC)
```python
def generate_toc(vocabulary):
    """
    Створює секцію з карточками тем
    
    Для кожної теми:
    - Emoji (🍽️, 💬, 🚗, ...)
    - Назва теми
    - Кількість слів
    - Посилання на якір (#theme-food)
    - Колір рамки (border-left)
    """
```

**HTML структура карточки:**
```html
<a href="#theme-food" class="toc-card" style="border-left: 5px solid #FF6B6B;">
    <div class="card-emoji">🍽️</div>
    <div class="card-content">
        <h3 class="card-title">Їжа та напої</h3>
        <p class="card-count">25 слів</p>
    </div>
</a>
```

#### 2.3. Генерація таблиць слів
```python
def generate_tables(vocabulary, text_mapping):
    """
    Для кожної теми створює:
    
    1. Заголовок теми (emoji + назва + опис)
    2. HTML таблицю:
       - Колонка 1: Німецьке слово
       - Колонка 2: Переклад (russian)
       - Колонка 3: Приклади з текстів
    3. Футер з кнопкою "До змісту"
    """
```

**HTML структура таблиці:**
```html
<table class="vocab-table">
    <thead>
        <tr>
            <th>Deutsch</th>
            <th>Русский</th>
            <th>Приклади з текстів</th>
        </tr>
    </thead>
    <tbody>
        <tr class="word-row">
            <td class="german-word">das Getränk, -e</td>
            <td class="russian-word">напиток</td>
            <td class="collocations">
                <div class="collocation-item">
                    <a href="#text-pumpkin" class="text-link">Pumpkin Spice Latte</a>: 
                    <span class="example">«ein beliebtes Getränk im Herbst»</span>
                </div>
            </td>
        </tr>
    </tbody>
</table>
```

#### 2.4. Генерація стилів (CSS)
Стилі вбудовані в `<style>` тег всередині HTML:

**Основні компоненти:**
- **Gradient фон:** `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Карточки тем:** білі з тінню, hover ефект
- **Таблиці:** rounded corners, hover на рядках
- **Посилання:** gradient колір з hover
- **Адаптивність:** `@media (max-width: 768px)`

### Крок 3: Збереження та валідація

```python
# 1. Збереження файлу
output = Path(r'F:\AiKlientBank\Lir\texts\thematic_vocabulary_full.html')
with open(output, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Статистика
print(f"Тем: {html.count('<div id=\"theme-')}")
print(f"Таблиць: {html.count('<table class=\"vocab-table\">')}")
print(f"Слів: {html.count('<tr class=\"word-row\">')}")

# 3. Валідація
assert 'Текст 1' not in html  # Немає placeholder назв
assert len(html) > 100000      # Мінімум 100 KB
```

---

## 🔄 ЯК ДОДАТИ НОВІ СЛОВА В СЛОВНИК

### Метод 1: Ручне додавання в vocabulary_dict.json

1. **Відкрити файл:**
```
F:\AiKlientBank\Lir\test\vocabulary_dict.json
```

2. **Знайти потрібну тему:**
```json
"theme-food": {
    "name": "Еда и напитки",
    "words": [ ... ]
}
```

3. **Додати нове слово:**
```json
{
    "german": "der Kuchen, -",
    "russian": "торт, пиріг",
    "examples": [
        {
            "text_id": "text-5",
            "text_title": "Deutsche Küche",
            "phrase": "Ein leckerer Kuchen zum Kaffee"
        }
    ]
}
```

4. **Зберегти файл** (UTF-8 encoding!)

5. **Запустити генерацію:**
```python
import subprocess
import sys

subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\test\generate_full_vocabulary.py'],
    cwd=r'F:\AiKlientBank\Lir'
)
```

### Метод 2: Автоматичне витягування з нових текстів

**Якщо додано нові .doc файли в `texts/Группа 1/`:**

1. **Запустити аналіз:**
```python
subprocess.run([sys.executable, 'test/analyze_doc_files.py'])
```

2. **Витягнути лексику:**
```python
subprocess.run([sys.executable, 'test/extract_vocabulary_a2_b1.py'])
```

3. **Розподілити по темах:**
```python
subprocess.run([sys.executable, 'test/categorize_vocabulary.py'])
```

4. **Замінити словник:**
```python
subprocess.run([sys.executable, 'test/replace_vocabulary.py'])
```

5. **Згенерувати HTML:**
```python
subprocess.run([sys.executable, 'test/generate_full_vocabulary.py'])
```

---

## 📊 СТРУКТУРА ДАНИХ

### Формат слова в словнику:

```json
{
    "german": "das Wort, -e или -̈er",
    "russian": "переклад українською/російською",
    "examples": [
        {
            "text_id": "text-1",           // ID тексту
            "text_title": "Назва тексту",   // Реальна назва
            "phrase": "приклад з тексту"    // Контекст використання
        }
    ]
}
```

### Правила для німецьких слів:

1. **Іменники:**
   - З артиклем: `der Mann`, `die Frau`, `das Kind`
   - З множиною: `der Mann, -̈er` → Männer
   - Без множини: `die Milch, (Sg.)` → тільки однина

2. **Дієслова:**
   - Інфінітив: `gehen`, `laufen`, `sprechen`
   - З приставкою: `ausgehen`, `mitkommen`

3. **Прикметники:**
   - Базова форма: `groß`, `klein`, `schön`

4. **Інші частини мови:**
   - Як є: `aber`, `und`, `weil`

---

## 🎨 ДИЗАЙН ТА СТИЛІЗАЦІЯ

### Кольорова палітра тем:

| Тема | Колір | Опис |
|------|-------|------|
| Їжа | `#FF6B6B` | Червоно-рожевий |
| Комунікація | `#4ECDC4` | Бірюзовий |
| Транспорт | `#95E1D3` | М'ятний |
| Мистецтво | `#F38181` | Коралловий |
| Мови | `#AA96DA` | Фіолетовий |
| Наука | `#FCBAD3` | Світло-рожевий |
| Географія | `#FFFFD2` | Жовтий |
| Історія | `#A8D8EA` | Блакитний |
| Дієслова | `#FFAAA5` | Персиковий |
| Прикметники | `#FFD3B6` | Бежевий |
| Час | `#DCEDC1` | Світло-зелений |
| Виміри | `#FFC8A2` | Помаранчевий |
| Абстрактне | `#D4A5A5` | Пудровий |

### CSS класи:

```css
.toc-card          /* Карточка теми в оглавленні */
.vocab-table       /* Таблиця слів */
.word-row          /* Рядок зі словом */
.german-word       /* Німецьке слово */
.russian-word      /* Переклад */
.collocation-item  /* Приклад з текстом */
.text-link         /* Посилання на текст */
.back-link         /* Кнопка "До змісту" */
```

---

## 🔍 ВАЛІДАЦІЯ ТА ТЕСТУВАННЯ

### Автоматична валідація:
```python
# Файл: test/final_validation.py

Перевірки:
1. ✅ Файл існує
2. ✅ Розмір > 100 KB
3. ✅ 13 тем в оглавленні
4. ✅ 13 таблиць
5. ✅ 45+ рядків слів
6. ✅ Робочі посилання (#text-id)
7. ✅ Реальні назви текстів (НЕ "Текст 1")
8. ✅ UTF-8 encoding (äöüß)
```

**Запуск валідації:**
```python
subprocess.run([sys.executable, 'test/final_validation.py'])
```

### Ручна перевірка:

1. **Відкрити в браузері:**
```
file:///F:/AiKlientBank/Lir/texts/thematic_vocabulary_full.html
```

2. **Перевірити:**
   - Всі карточки тем відображаються
   - Кліки по карточках працюють (scroll до теми)
   - Посилання в прикладах працюють
   - Стилі коректні
   - Адаптив на мобільних

---

## 🚀 ШВИДКИЙ СТАРТ

### Для генерації з нуля:

```python
import subprocess
import sys

cwd = r'F:\AiKlientBank\Lir'

# 1. Аналіз .doc файлів
subprocess.run([sys.executable, 'test/analyze_doc_files.py'], cwd=cwd)

# 2. Витягування лексики
subprocess.run([sys.executable, 'test/extract_vocabulary_a2_b1.py'], cwd=cwd)

# 3. Категоризація
subprocess.run([sys.executable, 'test/categorize_vocabulary.py'], cwd=cwd)

# 4. Фінальна генерація
subprocess.run([sys.executable, 'test/generate_full_vocabulary.py'], cwd=cwd)

print("[SUCCESS] Словник згенеровано!")
```

### Для швидкого оновлення (якщо vocabulary_dict.json готовий):

```python
import subprocess
import sys

subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\test\generate_full_vocabulary.py'],
    cwd=r'F:\AiKlientBank\Lir'
)
```

---

## 📝 ТИПОВІ ПРОБЛЕМИ ТА РІШЕННЯ

### Проблема 1: Не створюється файл
**Причина:** exec() замість subprocess.run()  
**Рішення:**
```python
# ❌ НЕ ПРАЦЮЄ
exec(open('test/generate_full_vocabulary.py').read())

# ✅ ПРАЦЮЄ
import subprocess
subprocess.run([sys.executable, 'test/generate_full_vocabulary.py'])
```

### Проблема 2: Не відображаються німецькі символи
**Причина:** Неправильне encoding  
**Рішення:**
```python
# ✅ ЗАВЖДИ використовуй UTF-8
with open(file, 'w', encoding='utf-8') as f:
    f.write(html)
```

### Проблема 3: Посилання не працюють
**Причина:** Неправильні якорі  
**Перевірка:**
```html
<!-- Посилання має відповідати якорю -->
<a href="#text-pumpkin">...</a>
<div id="text-pumpkin">...</div>
```

### Проблема 4: "Текст 1" замість реальних назв
**Причина:** Не завантажений doc_files_mapping.json  
**Рішення:**
```python
# Спочатку створити маппінг
subprocess.run([sys.executable, 'test/analyze_doc_files.py'])

# Потім генерувати
subprocess.run([sys.executable, 'test/generate_full_vocabulary.py'])
```

---

## 🔮 МОЖЛИВОСТІ ДЛЯ РОЗШИРЕННЯ

### 1. Збільшення кількості слів (до 300+)
- Додати більше .doc файлів в `texts/Группа 1/`
- Запустити повний цикл витягування лексики
- Оновити `vocabulary_dict.json`

### 2. Додавання аудіо вимови
```json
{
    "german": "das Wort",
    "russian": "слово",
    "audio": "audio/wort.mp3",  // Додати поле
    "examples": [ ... ]
}
```

### 3. Додавання перекладів
- Автоматичний переклад через API
- Ручне заповнення поля `russian`

### 4. Пошук по словнику
```html
<input type="search" id="vocab-search" placeholder="Пошук слова...">
<script>
    // JavaScript для фільтрації таблиць
</script>
```

### 5. Експорт в інші формати
- PDF (через wkhtmltopdf)
- XLSX (таблиці Excel)
- Anki cards (для запам'ятовування)

---

## 📚 ДОДАТКОВІ РЕСУРСИ

### Документація проекту:
- `rules/INSTRUCTION.md` - Загальна інструкція
- `rules/CRITICAL_RULES.md` - Критичні правила
- `rules/PYTHON_RUNNER_LIMITATION.md` - Обмеження python-runner

### Корисні файли:
- `test/vocabulary_analysis.txt` - Аналіз словника
- `test/FINAL_VOCABULARY_ANALYSIS.txt` - Фінальний звіт
- `test/teacher_analysis_report.txt` - Звіт викладача

### Команди для перевірки:
```python
# Статистика словника
exec(open('test/analyze_vocabulary.py', encoding='utf-8').read())

# Перевірка артиклів
subprocess.run([sys.executable, 'test/check_articles_fix.py'])

# Аналіз прогалин
subprocess.run([sys.executable, 'test/vocabulary_analysis_report.py'])
```

---

## ✅ ЧЕКЛИСТ ПЕРЕД ГЕНЕРАЦІЄЮ

- [ ] `vocabulary_dict.json` оновлений
- [ ] `doc_files_mapping.json` існує
- [ ] Всі .doc файли в `texts/Группа 1/`
- [ ] Python 3.13+ встановлений
- [ ] `python-docx` library встановлена
- [ ] UTF-8 encoding для всіх файлів
- [ ] Немає placeholder назв ("Текст 1", "Текст 2")
- [ ] Всі теми мають слова (мінімум 3-5)

---

## 🎓 ДЛЯ AI АСИСТЕНТА

### Коли користувач каже "згенеруй словник":

1. **Перевірити наявність файлів:**
```python
from pathlib import Path

vocab_dict = Path(r'F:\AiKlientBank\Lir\test\vocabulary_dict.json')
assert vocab_dict.exists(), "[ERROR] vocabulary_dict.json не знайдено!"
```

2. **Запустити генерацію:**
```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\test\generate_full_vocabulary.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)

if result.returncode == 0:
    print("[SUCCESS] Словник згенеровано!")
    print(result.stdout)
else:
    print("[ERROR] Помилка генерації:")
    print(result.stderr)
```

3. **Валідувати результат:**
```python
output = Path(r'F:\AiKlientBank\Lir\texts\thematic_vocabulary_full.html')

assert output.exists(), "[ERROR] Файл не створено!"
assert output.stat().st_size > 100000, "[ERROR] Файл занадто малий!"

print(f"[OK] Файл: {output}")
print(f"[OK] Розмір: {output.stat().st_size / 1024:.2f} KB")
```

### Коли користувач каже "додай слово":

1. **Прочитати vocabulary_dict.json**
2. **Знайти відповідну тему**
3. **Додати слово в масив `words`**
4. **Зберегти з UTF-8**
5. **Запустити `generate_full_vocabulary.py`**

---

## 📞 КОНТАКТИ ТА ПІДТРИМКА

**Автор проекту:** Lir Website Generator  
**Версія системи:** 3.0  
**Дата створення:** 10.10.2025  
**Python версія:** 3.13+  
**Залежності:** beautifulsoup4, python-docx

---

**Цей документ є вичерпним описом процесу генерації тематичного словаря.**  
**При будь-яких змінах в структурі - оновлюй цей файл!**

---

_Згенеровано AI Assistant на базі аналізу проекту Lir_  
_Останнє оновлення: 10.10.2025 23:45_
