# ІНСТРУКЦІЯ ДЛЯ ПРОЕКТУ Lir Website Generator
(Система генерації навчального сайту "Німецька через Короля Ліра")  
**Версія: 3.0 | Оновлено: 06.09.2025**

## 🚀 КРИТИЧНЕ ВІДКРИТТЯ - РІШЕННЯ ПРОБЛЕМИ СТВОРЕННЯ ФАЙЛІВ!

### ✅ SUBPROCESS.RUN() ПРАЦЮЄ ДЛЯ СТВОРЕННЯ ФАЙЛІВ!

**ВАЖЛИВЕ ВІДКРИТТЯ (06.09.2025):** subprocess.run() в python-runner МОЖЕ створювати файли на диску!

```python
# ✅ ЦЕЙ КОД ПРАЦЮЄ і СТВОРЮЄ файли:
import subprocess
import sys

result = subprocess.run(
    [sys.executable, 'main.py'],
    capture_output=True,
    text=True,  
    cwd=r'F:\AiKlientBank\Lir'
)
# ВСІ 55 HTML файлів будуть створені на диску!
print(f"Exit code: {result.returncode}")
print(f"Створено файлів: {result.stdout}")
```

### 📊 ПОРІВНЯННЯ МЕТОДІВ:

| Метод | Створює файли? | Примітка |
|--------|---------------|----------|
| **subprocess.run()** | ✅ ТАК | ПОВНИЙ доступ до файлової системи |
| exec() | ❌ НІ | Код виконується, але файли в пам'яті |
| with open() | ❌ НІ | Файли не записуються на диск |
| **filesystem:write_file** | ✅ ТАК | Прямий запис через MCP API |

### 🎯 ПРАКТИЧНІ ПРИКЛАДИ:

#### 1️⃣ Генерація сайту (створює 55 файлів):
```python
import subprocess
import sys

# ПРАЦЮЄ! Створює всі HTML файли
result = subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\main.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)

if result.returncode == 0:
    print("[OK] Сайт згенеровано!")
```

#### 2️⃣ Запуск тестових скриптів:
```python
# Генерація звіту з створенням HTML файлу
result = subprocess.run(
    [sys.executable, 'test/generate_transcription_report.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)
```

#### 3️⃣ Комбінований підхід:
```python
# Аналіз через exec() (не створює файли)
exec(open('test/analyze_data.py').read())

# Генерація через subprocess (створює файли)
subprocess.run([sys.executable, 'main.py'], cwd=r'F:\AiKlientBank\Lir')
```

---

## 🎯 СТИЛЬ РОБОТИ ІІ

DO NOT GIVE ME HIGH LEVEL STUFF! Якщо прошу виправлення або пояснення, хочу РЕАЛЬНИЙ КОД або ПОЯСНЕННЯ!
НЕ хочу "Here's how you can blablabla"
Be casual unless otherwise specified
Be terse - коротко і по суті
Suggest solutions that I didn't think about—anticipate my needs
Treat me as an expert
Be accurate and thorough
Give the answer immediately - детальні пояснення ПІСЛЯ відповіді якщо потрібно
Value good arguments over authorities, the source is irrelevant
Consider new technologies and contrarian ideas, not just conventional wisdom
High levels of speculation or prediction OK, just flag it for me
No moral lectures
WHEN UPDATING THE CODEBASE BE 100% SURE TO NOT BREAK ANYTHING
Спілкуйся зі мною завжди українською

## 🔴 ОБОВ'ЯЗКОВО НА ПОЧАТКУ КОЖНОЇ СЕСІЇ:

1. ПЕРЕВІР структуру проекту через list_directory()
2. ПЕРЕВІР що в корені ТІЛЬКИ 2 файли: config.py та main.py  
3. НЕ СТВОРЮЙ нові файли в корені проекту
4. ВСІ тестові скрипти → ТІЛЬКИ в папку test/
5. ВСЯ документація → ТІЛЬКИ в папку rules/
6. Для створення файлів використовуй subprocess.run() або filesystem:write_file
7. НЕ створюй .bat, .cmd, .sh файли
8. Якщо порушиш Critical Rule = зламаєш проект!

## 📁 МІЙ ШЛЯХ ДО ПРОЕКТУ: F:\AiKlientBank\Lir

## 🛠️ ІНСТРУМЕНТИ:

### Для роботи з кодом:
- **filesystem:read_file** - для читання файлів
- **filesystem:write_file** - для створення файлів (НЕ в корені!)
- **filesystem:edit_file** - для редагування коду
- **filesystem:list_directory** - для перегляду структури
- **filesystem:search_files** - для пошуку в проекті
- **filesystem:create_directory** - для створення директорій (тільки в test/ або rules/)

### Для запуску Python:
- **subprocess.run()** - ✅ СТВОРЮЄ файли на диску!
- **exec()** - ❌ НЕ створює файли (тільки для аналізу)

### Для перевірки результатів:
- **puppeteer:puppeteer_navigate** - відкрити згенерований HTML
- **puppeteer:puppeteer_screenshot** - зробити скріншот сайту
- **puppeteer:puppeteer_evaluate** - виконати JavaScript для перевірки

## 🚫 КРИТИЧНО ВАЖЛИВО - СТРУКТУРА ПРОЕКТУ ФІНАЛЬНА:

### ЗАБОРОНЕНО в корені проекту:
- ❌ НЕ створювати README.md, INSTALL.md, FAQ.md
- ❌ НЕ створювати test.py, demo.py, check.py
- ❌ НЕ створювати run.bat, start.bat, generate.bat
- ❌ НЕ створювати будь-які інші файли
- ✅ ТІЛЬКИ config.py та main.py мають бути в корені!

### ПРАВИЛЬНА структура:
```
F:\AiKlientBank\Lir\
├── config.py         # Конфігурація (НЕ ЧІПАТИ)
├── main.py          # Головний файл (НЕ ЧІПАТИ)
├── src/             # Модулі системи
├── data/            # JSON файли (51 файл, поле "vocabulary")
├── output/          # Результати генерації
├── test/            # ВСІ тести ТУТ!
├── rules/           # ВСЯ документація ТУТ!
├── backup/          # Резервні копії
├── logs/            # Логи
└── [БІЛЬШЕ НІЧОГО В КОРЕНІ!]
```

## 🚨 ПРАВИЛЬНІ СПОСОБИ ЗАПУСКУ:

### Для генерації сайту (створює файли):
```python
# ✅ ПРАВИЛЬНО - створює файли:
import subprocess
import sys

result = subprocess.run(
    [sys.executable, 'main.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)
```

### Для аналізу даних (НЕ створює файли):
```python
# Для читання та аналізу використовуй exec():
exec(open('test/analyze_data.py', encoding='utf-8').read())
```

### Для створення окремих файлів:
```python
# Через filesystem:
filesystem:write_file(
    path="F:\\AiKlientBank\\Lir\\test\\report.txt",
    content="Вміст файлу"
)
```

## ⚠️ КРИТИЧНІ ПРАВИЛА ГЕНЕРАЦІЇ:

✅ **ПРАВИЛЬНИЙ підхід:**
- Читай JSON з папки data/ (поле "vocabulary", НЕ "words")
- Генеруй HTML в папку output/
- Використовуй subprocess.run() для запуску main.py
- Зберігай структуру даних
- НЕ змінюй формат JSON

❌ **ЗАБОРОНЕНО:**
- Змінювати структуру проекту
- Додавати файли в корінь
- Створювати .bat файли
- Видаляти папку data/
- Модифікувати config.py або main.py без потреби

## 📋 ПРАВИЛА ПРОЕКТУ:

- **JSON файлів:** 51 в data/ (vocabulary поле!)
- **Генерується:** 55+ HTML файлів в output/
- **Слів німецькою:** 612
- **Категорії:** a2/, b1/, thematic/
- **Python версія:** 3.13
- **Основні залежності:** beautifulsoup4

## 🏗️ СТРУКТУРА МОДУЛІВ:

```
F:\AiKlientBank\Lir\src\
├── core/              # Ядро
│   ├── config_manager.py      # Управління конфігурацією
│   ├── logger_manager.py      # Логування
│   └── orchestrator.py        # Координатор генерації
├── generators/        # Генератори
│   ├── json_generator.py      # Генерація HTML з JSON
│   ├── json_enricher.py       # Збагачення JSON
│   ├── css_generator.py       # Генерація CSS
│   ├── js_generator.py        # Генерація JS
│   └── original_styles.py     # Оригінальні стилі
└── analyzers/         # Аналізатори
    └── site_analyzer.py       # Аналіз даних
```

## 🎯 СПЕЦИФІКА ПРОЕКТУ:

- 51 JSON файл з уроками німецької
- 3 категорії: a2/, b1/, thematic/
- 612+ німецьких слів з транскрипціями
- Навчальний контент через "Короля Ліра"
- Градієнтні картки (фіолетові, помаранчеві, рожеві)
- Responsive дизайн
- Поле "vocabulary" в JSON (НЕ "words"!)

## 📊 АЛГОРИТМ РОБОТИ:

1. Читання JSON файлів з data/ (vocabulary)
2. Збагачення даних (json_enricher.py)
3. Генерація HTML сторінок
4. Створення CSS/JS
5. Збереження в output/
6. Логування в logs/

## ✅ ОЧІКУВАНІ РЕЗУЛЬТАТИ:

- **Файлів згенеровано:** 55+
- **HTML сторінок:** index.html + уроки
- **Категорій:** 3 (A2, B1, Thematic)
- **Груп уроків:** 17
- **Слів німецькою:** 612

## 🔍 ПЕРЕВІРКА РЕЗУЛЬТАТІВ:

### Через Puppeteer:
```javascript
// Відкрити згенерований сайт
puppeteer:puppeteer_navigate({
    url: "file:///F:/AiKlientBank/Lir/output/index.html"
})

// Зробити скріншот
puppeteer:puppeteer_screenshot({
    name: "lir_generated",
    width: 1920,
    height: 1080
})

// Перевірити кількість сторінок
puppeteer:puppeteer_evaluate({
    script: `
        const links = document.querySelectorAll('a[href$=".html"]');
        console.log('HTML links:', links.length);
        links.length
    `
})
```

### Через файлову систему:
```python
# Перевірка створених файлів
from pathlib import Path

output_dir = Path(r'F:\AiKlientBank\Lir\output')
html_files = list(output_dir.glob('**/*.html'))
print(f"Створено HTML файлів: {len(html_files)}")
```

## 🚫 КРИТИЧНІ ЗАБОРОНИ:

- НЕ створюй файли в корені проекту!
- НЕ створюй .BAT файли!
- НЕ змінюй структуру проекту!
- НЕ видаляй папку data/!
- НЕ модифікуй config.py та main.py без потреби!
- НЕ використовуй Unicode символи в консолі (✓, ✗, →)!
- Використовуй: [OK], [ERROR], [!], [+], [-]

## 🧪 ПРАВИЛА ТЕСТУВАННЯ:

### ВСІ тести ТІЛЬКИ в test/:
```python
# Шаблон тестового файлу
"""
Тест: [назва]
Дата: [дата]
Мета: [що тестуємо]
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Тестовий код...
```

### Запуск тестів з створенням файлів:
```python
# Через subprocess для створення файлів
result = subprocess.run(
    [sys.executable, 'test/generate_report.py'],
    cwd=r'F:\AiKlientBank\Lir'
)
```

### Іменування тестів:
- test_*.py - unit тести
- check_*.py - перевірки
- debug_*.py - налагодження
- validate_*.py - валідація
- generate_*.py - генератори звітів

## 📁 ДОКУМЕНТАЦІЯ ПРОЕКТУ:

### ВСЯ документація в rules/:
- **INSTRUCTION.md** - Ця інструкція (оновлена!)
- **CRITICAL_RULES.md** - Критичні правила
- **PYTHON_RUNNER_LIMITATION.md** - Обмеження python-runner (оновлено!)
- **PROJECT_STRUCTURE.md** - Структура проекту
- **TESTING_RULES.md** - Правила тестування
- **USAGE_RULES.md** - Правила використання
- **MEMORY_RULES.md** - Для Memory-MCP
- **README.md** - Головна документація

## 🔄 ШВИДКИЙ ЗАПУСК:

### Для генерації сайту (СТВОРЮЄ файли):
```python
# ПРАВИЛЬНО - через subprocess:
import subprocess
import sys

result = subprocess.run(
    [sys.executable, r'F:\AiKlientBank\Lir\main.py'],
    capture_output=True,
    text=True,
    cwd=r'F:\AiKlientBank\Lir'
)

# Результат: 55+ файлів в output/
```

### Для аналізу (НЕ створює файли):
```python
# Через exec() для аналізу:
exec(open('main.py', encoding='utf-8').read())
```

## 💡 ПІДСУМОК КРИТИЧНОГО ВІДКРИТТЯ:

**subprocess.run() - це РІШЕННЯ проблеми створення файлів!**

- ✅ subprocess.run() - СТВОРЮЄ файли
- ❌ exec() - НЕ створює файли
- ✅ filesystem:write_file - СТВОРЮЄ файли
- ❌ with open() в python-runner - НЕ створює файли

## ПАМ'ЯТАЙ:

- subprocess.run() ПРАЦЮЄ для створення файлів!
- Структура проекту ФІНАЛЬНА - не змінювати
- ВСІ файли генеруються з data/ в output/
- НІКОЛИ не створюй файли в корені проекту
- НІКОЛИ не створюй .bat файли
- ЗАВЖДИ тести в test/
- ЗАВЖДИ документація в rules/
- JSON файли мають поле "vocabulary" (НЕ "words")
- Простота та надійність - головні принципи!

---

**Версія інструкції:** 3.0
**Дата оновлення:** 06.09.2025
**Статус проекту:** Production Ready
**КРИТИЧНЕ ОНОВЛЕННЯ:** subprocess.run() ПРАЦЮЄ для створення файлів!
