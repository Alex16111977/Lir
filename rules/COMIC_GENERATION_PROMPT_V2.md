# ПРОМТ ДЛЯ ГЕНЕРАЦИИ СТРАНИЦ КОМИКСА "KÖNIG LEAR"
## Версия 2.0 - ПОЛНЫЙ ТЕХНИЧЕСКИЙ ПРОМТ

---

## 🎯 ЦЕЛЬ ЗАДАЧИ
Создать HTML страницы комикса "König Lear" для изучения немецкого языка через классическую литературу. Каждая страница - это полноценная сцена с диалогами, визуальными эффектами и словарем.

---

## 📁 СТРУКТУРА ФАЙЛОВ

### Пути сохранения:
- **ТОМ 2:** `F:\AiKlientBank\Lir\comic\volumes\volume_2_wahnsinn\`
- **ТОМ 3:** `F:\AiKlientBank\Lir\comic\volumes\volume_3_weisheit\`

### Именование файлов:
```
issue_XX_название_page_Y.html
Где: XX - номер выпуска (06-10 для тома 2, 11-15 для тома 3)
     название - короткое название выпуска латиницей
     Y - номер страницы (1-6)
```

---

## 🎨 ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ

### 1. СТРУКТУРА HTML СТРАНИЦЫ

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>König Lear - Band {VOLUME}, Ausgabe {ISSUE}: {ISSUE_NAME}</title>
    <link rel="stylesheet" href="../../css/comic-base.css">
    <link rel="stylesheet" href="../../css/speech-bubbles.css">
</head>
<body>
    <!-- Заголовок страницы -->
    <div class="page-header">
        <h1>König Lear: {PAGE_TITLE}</h1>
        <p>Band {VOLUME}: {VOLUME_NAME} • Ausgabe {ISSUE}: {ISSUE_NAME} • Seite {PAGE}</p>
    </div>

    <!-- Страница комикса -->
    <div class="comic-page" data-volume="{VOLUME}" data-issue="{ISSUE}" data-page="{PAGE}">
        <!-- ПАНЕЛИ (6 штук на страницу) -->
    </div>

    <!-- Словарь страницы -->
    <div class="page-vocabulary">
        <h3>Wörter dieser Seite:</h3>
        <ul class="vocabulary-list">
            <!-- СЛОВАРЬ (10-12 слов) -->
        </ul>
    </div>
</body>
</html>
```

### 2. ТИПЫ ПАНЕЛЕЙ (ОБЯЗАТЕЛЬНО 6 НА СТРАНИЦУ)

```html
<!-- Полная панель (занимает всю ширину) -->
<div class="panel panel-full panel-{volume_name}">

<!-- Половинная панель (50% ширины) -->
<div class="panel panel-half panel-{volume_name}">

<!-- Треть панели (33% ширины) -->
<div class="panel panel-third panel-{volume_name}">
```

### 3. ТИПЫ РЕЧЕВЫХ ПУЗЫРЕЙ

```html
<!-- Обычная речь -->
<div class="speech-bubble bubble-speech bubble-{position}">

<!-- Крик -->
<div class="speech-bubble bubble-shout bubble-{position}">

<!-- Шепот -->
<div class="speech-bubble bubble-whisper bubble-{position}">

<!-- Мысль -->
<div class="speech-bubble bubble-thought bubble-{position}">
```

Позиции: `bubble-center`, `bubble-top-left`, `bubble-top-right`, `bubble-bottom-left`, `bubble-bottom-right`

### 4. КАЖДЫЙ ПУЗЫРЬ СОДЕРЖИТ:

```html
<div class="bubble-german">{НЕМЕЦКИЙ_ТЕКСТ}</div>
<div class="bubble-translation">{РУССКИЙ_ПЕРЕВОД}</div>
```

### 5. ЗВУКОВЫЕ ЭФФЕКТЫ

```html
<!-- Большой эффект -->
<div class="sfx sfx-large" style="position">{ЭФФЕКТ}</div>

<!-- Обычный эффект -->
<div class="sfx" style="position">{эффект}</div>

<!-- Маленький эффект -->
<div class="sfx sfx-small" style="position">*эффект*</div>
```

---

## 📚 ПРАВИЛА ТРАНСКРИПЦИИ (КРИТИЧНО!)

### Источник: `F:\AiKlientBank\Lir\test\full_stress_dictionary_v2.py`

1. **БОЛЬШИЕ буквы** = ударный слог
2. **малые буквы** = безударные слоги  
3. **дефисы** = разделяют слоги

### Префиксы БЕЗ ударения:
- be-, ge-, er-, ver-, zer-, ent-, emp-
- Пример: `verstehen [фер-ШТЕ-ен]`

### Префиксы С ударением:
- auf-, aus-, ein-, mit-, vor-, zu-
- Пример: `aufstehen [АУФ-ште-ен]`

### Простые слова:
- Ударение на первом слоге
- Пример: `Vater [ФА-тер]`

### Сложные слова:
- Ударение на первой части
- Пример: `Königreich [КЁ-ниг-райх]`

---

## 🎭 ЭМОЦИОНАЛЬНЫЕ ГРАДИЕНТЫ CSS

```css
/* ТОМ 2 - Безумие (темно-синий → фиолетовый) */
.panel-wahnsinn { 
    background: linear-gradient(135deg, #1a1a2e, #7f39fb, #0c0c1f); 
}

/* ТОМ 3 - Мудрость (светло-зеленый → белый) */
.panel-weisheit { 
    background: linear-gradient(135deg, #a8e6cf, #dcedc1, #ffffff); 
}
```

---

## 📖 ДЕТАЛЬНЫЙ ПЛАН СТРАНИЦ

### ТОМ 2: WAHNSINN (Безумие) - Выпуски 6-10

#### ВЫПУСК 6: "DER STURM" (Буря) - 6 страниц

##### issue_06_sturm_page_1.html - "In der Wildnis"
**Панели:**
1. **ПОЛНАЯ** - Лир против стихии
2. **ТРЕТЬ** - Ветер воет
3. **ТРЕТЬ** - Дождь хлещет
4. **ТРЕТЬ** - Молнии сверкают
5. **ПОЛОВИНА** - Лир кричит в небо
6. **ПОЛОВИНА** - Шут прячется

**Диалоги:**
- ЛИР: "Blaset, ihr WINDE! Ich fürchte euch NICHT!"
- ЛИР: "Der REGEN sind meine Tränen!"
- ЛИР: "DONNER! BLITZ! Ich bin der KÖNIG!"
- ШУТ: "Herr, lasst uns SCHUTZ suchen!"
- ЛИР: "Die NATUR ist meine einzige Familie!"
- ШУТ: "Der WAHNSINN nimmt ihn..."

**Словарь:**
- der Sturm - буря - [дер ШТУРМ]
- der Regen - дождь - [дер РЕ-ген]
- der Wind - ветер - [дер ВИНД]
- der Donner - гром - [дер ДО-нер]
- der Blitz - молния - [дер БЛИЦ]
- wahnsinnig - безумный - [ВАН-зи-ниг]
- schreien - кричать - [ШРАЙ-ен]
- die Wildnis - дикая природа - [ди ВИЛЬД-нис]
- der Schutz - защита - [дер ШУТЦ]
- toben - бушевать - [ТО-бен]

##### issue_06_sturm_page_2.html - "Der Wahnsinn beginnt"
**Панели:**
1. **ПОЛНАЯ** - Лир срывает одежду
2. **ПОЛОВИНА** - Безумие в глазах
3. **ПОЛОВИНА** - Шут плачет
4. **ТРЕТЬ** - Эдгар появляется как Tom
5. **ТРЕТЬ** - Три безумца
6. **ТРЕТЬ** - Молния освещает сцену

**Диалоги:**
- ЛИР: "Ich ZERRREISSE diese falschen Kleider!"
- ЛИР: "NACKT kam ich zur Welt!"
- ШУТ: "Mein HERR verliert seinen VERSTAND!"
- TOM: "Armer Tom FRIERT!"
- ЛИР: "Ein PHILOSOPH! Sprich zu mir!"
- TOM: "Die DÄMONEN verfolgen mich!"

**Словарь:**
- zerreißen - рвать - [цер-РАЙ-сен]
- nackt - голый - [НАКТ]
- der Verstand - разум - [дер фер-ШТАНД]
- frieren - мерзнуть - [ФРИ-рен]
- der Philosoph - философ - [дер фи-ло-ЗОФ]
- die Dämonen - демоны - [ди де-МО-нен]
- verrückt - сумасшедший - [фер-РЮКТ]
- die Kälte - холод - [ди КЕЛЬ-те]
- zittern - дрожать - [ЦИ-терн]
- weinen - плакать - [ВАЙ-нен]

#### ВЫПУСК 7: "DIE HÖHLE" (Пещера) - 5 страниц

##### issue_07_hoehle_page_1.html - "Zuflucht im Sturm"
**Панели:**
1. **ПОЛНАЯ** - Вход в пещеру
2. **ПОЛОВИНА** - Глостер с факелом
3. **ПОЛОВИНА** - Встреча в темноте
4. **ТРЕТЬ** - Лир не узнает Глостера
5. **ТРЕТЬ** - Слепота души
6. **ТРЕТЬ** - Огонь в пещере

**Диалоги:**
- ГЛОСТЕР: "Majestät, hier ist SCHUTZ!"
- ЛИР: "Wer bist du, SCHATTEN?"
- ГЛОСТЕР: "Ich bin Euer treuer DIENER!"
- ЛИР: "Ich kenne keine TREUE mehr!"
- TOM: "In der HÖHLE wohnen Geister!"
- ШУТ: "Die DUNKELHEIT verschlingt uns alle!"

**Словарь:**
- die Höhle - пещера - [ди ХЁ-ле]
- der Schatten - тень - [дер ША-тен]
- die Treue - верность - [ди ТРОЙ-е]
- die Dunkelheit - темнота - [ди ДУН-кель-хайт]
- das Feuer - огонь - [дас ФОЙ-ер]
- der Diener - слуга - [дер ДИ-нер]
- erkennen - узнавать - [ер-КЕ-нен]
- verschlingen - поглощать - [фер-ШЛИН-ген]
- brennen - гореть - [БРЕ-нен]
- die Zuflucht - убежище - [ди ЦУ-флухт]

### ТОМ 3: WEISHEIT (Мудрость) - Выпуски 11-15

#### ВЫПУСК 11: "WIEDERSEHEN" (Встреча) - 6 страниц

##### issue_11_wiedersehen_page_1.html - "Erwachen"
**Панели:**
1. **ПОЛНАЯ** - Корделия у постели отца
2. **ПОЛОВИНА** - Лир просыпается
3. **ПОЛОВИНА** - Не узнает дочь
4. **ТРЕТЬ** - Слезы Корделии
5. **ТРЕТЬ** - Воспоминание
6. **ТРЕТЬ** - Узнавание

**Диалоги:**
- КОРДЕЛИЯ: "VATER, erwacht!"
- ЛИР: "Bin ich im HIMMEL?"
- КОРДЕЛИЯ: "Nein, Ihr seid bei mir!"
- ЛИР: "Ich kenne diese STIMME..."
- КОРДЕЛИЯ: "Ich bin Eure TOCHTER!"
- ЛИР: "Cordelia? VERZEIH mir!"

**Словарь:**
- erwachen - просыпаться - [ер-ВА-хен]
- der Himmel - небо - [дер ХИ-мель]
- die Stimme - голос - [ди ШТИ-ме]
- verzeihen - прощать - [фер-ЦАЙХ-ен]
- die Tränen - слезы - [ди ТРЕ-нен]
- erkennen - узнавать - [ер-КЕ-нен]
- umarmen - обнимать - [ум-АР-мен]
- die Erinnerung - воспоминание - [ди ер-И-не-рунг]
- die Liebe - любовь - [ди ЛИ-бе]
- vergeben - простить - [фер-ГЕ-бен]

---

## ⚠️ КРИТИЧЕСКИЕ ТРЕБОВАНИЯ

### ОБЯЗАТЕЛЬНО:
1. **6 панелей на КАЖДОЙ странице** (не 4, не 5, именно 6!)
2. **Минимум 2 диалога на панель** (немецкий + русский)
3. **10-12 слов в словаре** на каждой странице
4. **Разные типы панелей** (full, half, third)
5. **Разные типы пузырей** (speech, shout, whisper, thought)
6. **Звуковые эффекты** на каждой странице (минимум 3)
7. **Позиционирование через style=""** для эффектов
8. **Правильные транскрипции** из словаря

### ЗАПРЕЩЕНО:
1. ❌ Пустые панели без диалогов
2. ❌ Меньше 6 панелей на странице
3. ❌ Одинаковые размеры всех панелей
4. ❌ Неправильные транскрипции (проверять по словарю!)
5. ❌ Диалоги только на одном языке
6. ❌ Страницы без звуковых эффектов

---

## 🔄 АЛГОРИТМ ГЕНЕРАЦИИ

1. **Создать структуру страницы** с правильным заголовком
2. **Добавить 6 панелей** разных размеров
3. **В каждую панель добавить:**
   - Номер панели
   - Минимум 1 речевой пузырь с диалогом
   - Звуковые эффекты где уместно
4. **Создать словарь** из 10-12 слов
5. **Проверить транскрипции** по словарю
6. **Сохранить файл** с правильным именем

---

## 📊 КОНТРОЛЬНЫЙ ЧЕКЛИСТ

Перед сохранением каждой страницы проверить:

- [ ] Правильное имя файла (issue_XX_name_page_Y.html)
- [ ] Правильный путь (volume_2_wahnsinn или volume_3_weisheit)
- [ ] Ровно 6 панелей
- [ ] Минимум 12 диалоговых строк (6 немецких + 6 русских)
- [ ] Минимум 3 звуковых эффекта
- [ ] 10-12 слов в словаре
- [ ] Правильные транскрипции по словарю
- [ ] Разнообразие типов панелей и пузырей
- [ ] Эмоциональная насыщенность сцены

---

## 🎯 РЕЗУЛЬТАТ

После выполнения должно быть создано:

### ТОМ 2 (WAHNSINN):
- 5 выпусков (6-10)
- 27 HTML страниц
- Темная цветовая схема
- Сцены безумия и бури

### ТОМ 3 (WEISHEIT):
- 5 выпусков (11-15)
- 28 HTML страниц
- Светлая цветовая схема
- Сцены прозрения и прощения

**ВСЕГО: 55 новых страниц**

---

## 💡 ПРИМЕР КОДА ДЛЯ ГЕНЕРАЦИИ

```python
import os
from pathlib import Path

# Базовые пути
BASE_DIR = Path(r"F:\AiKlientBank\Lir\comic\volumes")
VOLUME_2 = BASE_DIR / "volume_2_wahnsinn"
VOLUME_3 = BASE_DIR / "volume_3_weisheit"

# Загрузить словарь
exec(open(r'F:\AiKlientBank\Lir\test\full_stress_dictionary_v2.py', encoding='utf-8').read())

def create_comic_page(volume_num, volume_name, issue_num, issue_name, 
                      page_num, page_title, panels, vocabulary):
    """Создает HTML страницу комикса по шаблону"""
    
    # Проверка: должно быть ровно 6 панелей
    assert len(panels) == 6, f"Должно быть 6 панелей, а не {len(panels)}!"
    
    # Проверка: минимум 10 слов в словаре
    assert len(vocabulary) >= 10, f"Минимум 10 слов в словаре!"
    
    # Генерация HTML...
    return html
```

---

## 📝 ФИНАЛЬНЫЕ ЗАМЕЧАНИЯ

1. **Качество > Скорость**: Лучше сделать меньше страниц, но качественно
2. **Проверяйте транскрипции**: Используйте словарь, не выдумывайте
3. **Эмоциональность**: Каждая страница должна передавать эмоции
4. **Разнообразие**: Не копируйте структуру, делайте каждую страницу уникальной
5. **Тестирование**: Открывайте созданные страницы в браузере для проверки

---

**АВТОР ПРОМТА:** AI Prompt Engineer
**ВЕРСИЯ:** 2.0
**ДАТА:** 06.09.2025
**СТАТУС:** Production Ready