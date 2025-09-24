#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Генератор PDF для дополнительного словаря A2
Создает красиво оформленный PDF файл со всеми словами
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os
from datetime import datetime

# Путь для сохранения PDF
output_path = r'F:\AiKlientBank\Lir\output\A2_Missing_Dictionary.pdf'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Попробуем зарегистрировать шрифты с поддержкой кириллицы
try:
    # Стандартные Windows шрифты
    pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
    pdfmetrics.registerFont(TTFont('ArialBold', 'C:/Windows/Fonts/arialbd.ttf'))
    font_name = 'Arial'
    font_bold = 'ArialBold'
except:
    # Если не найдены, используем встроенные
    font_name = 'Helvetica'
    font_bold = 'Helvetica-Bold'

# Данные словаря
vocabulary_data = {
    "Модальные глаголы (КРИТИЧНО!)": [
        ["können", "[КЁН-нен]", "мочь", "40+ раз"],
        ["müssen", "[МЮС-сен]", "должен", "35+ раз"],
        ["wollen", "[ВО-лен]", "хотеть", "50+ раз"],
        ["sollen", "[ЗО-лен]", "следует", "25+ раз"],
        ["dürfen", "[ДЮР-фен]", "сметь", "15+ раз"],
        ["mögen", "[МЁ-ген]", "нравиться", "10+ раз"],
    ],
    "Базовые глаголы (ОЧЕНЬ ВАЖНО!)": [
        ["sagen", "[ЗА-ген]", "говорить", "120+ раз"],
        ["machen", "[МА-хен]", "делать", "45+ раз"],
        ["geben", "[ГЕ-бен]", "давать", "40+ раз"],
        ["nehmen", "[НЕ-мен]", "брать", "35+ раз"],
        ["wissen", "[ВИС-сен]", "знать", "30+ раз"],
        ["kennen", "[КЕН-нен]", "знать (быть знакомым)", "25+ раз"],
        ["haben", "[ХА-бен]", "иметь", "80+ раз"],
        ["sein", "[ЗАЙН]", "быть", "100+ раз"],
        ["bleiben", "[БЛАЙ-бен]", "оставаться", "20+ раз"],
        ["bringen", "[БРИН-ген]", "приносить", "15+ раз"],
        ["halten", "[ХАЛЬ-тен]", "держать", "25+ раз"],
        ["lassen", "[ЛАС-сен]", "позволять", "30+ раз"],
        ["stehen", "[ШТЕ-ен]", "стоять", "20+ раз"],
        ["liegen", "[ЛИ-ген]", "лежать", "10+ раз"],
        ["sitzen", "[ЗИ-цен]", "сидеть", "8+ раз"],
        ["denken", "[ДЕН-кен]", "думать", "25+ раз"],
        ["fragen", "[ФРА-ген]", "спрашивать", "15+ раз"],
        ["antworten", "[АНТ-вор-тен]", "отвечать", "10+ раз"],
        ["zeigen", "[ЦАЙ-ген]", "показывать", "12+ раз"],
        ["helfen", "[ХЕЛЬ-фен]", "помогать", "15+ раз"],
        ["brauchen", "[БРАУ-хен]", "нуждаться", "10+ раз"],
        ["tun", "[ТУН]", "делать", "30+ раз"],
        ["meinen", "[МАЙ-нен]", "иметь в виду", "20+ раз"],
        ["scheinen", "[ШАЙ-нен]", "казаться/светить", "15+ раз"],
        ["heißen", "[ХАЙ-сен]", "называться", "10+ раз"],
    ],
    "Наречия и частицы": [
        ["noch", "[НОХ]", "еще", "80+ раз"],
        ["nur", "[НУР]", "только", "60+ раз"],
        ["auch", "[АУХ]", "также", "70+ раз"],
        ["schon", "[ШОН]", "уже", "35+ раз"],
        ["mehr", "[МЕР]", "больше", "45+ раз"],
        ["sehr", "[ЗЕР]", "очень", "25+ раз"],
        ["ganz", "[ГАНЦ]", "совсем/весь", "20+ раз"],
        ["etwa", "[ЕТ-ва]", "примерно", "8+ раз"],
        ["genug", "[ге-НУГ]", "достаточно", "10+ раз"],
        ["weniger", "[ВЕ-ни-гер]", "меньше", "8+ раз"],
        ["fast", "[ФАСТ]", "почти", "12+ раз"],
        ["ziemlich", "[ЦИМ-лих]", "довольно", "6+ раз"],
        ["besser", "[БЕС-сер]", "лучше", "15+ раз"],
        ["vielleicht", "[фи-ЛАЙХТ]", "может быть", "10+ раз"],
    ],
    "Вопросительные слова": [
        ["warum", "[ва-РУМ]", "почему", "25+ раз"],
        ["wohin", "[во-ХИН]", "куда", "15+ раз"],
        ["woher", "[во-ХЕР]", "откуда", "10+ раз"],
        ["wann", "[ВАН]", "когда", "20+ раз"],
        ["womit", "[во-МИТ]", "чем", "10+ раз"],
        ["wofür", "[во-ФЮР]", "для чего", "8+ раз"],
        ["welcher", "[ВЕЛЬ-хер]", "который", "15+ раз"],
        ["wieviel", "[ви-ФИЛЬ]", "сколько", "10+ раз"],
    ],
    "Местоимения": [
        ["jemand", "[ЙЕ-манд]", "кто-то", "12+ раз"],
        ["niemand", "[НИ-манд]", "никто", "15+ раз"],
        ["etwas", "[ЕТ-вас]", "что-то", "20+ раз"],
        ["alles", "[А-лес]", "всё", "25+ раз"],
        ["jeder", "[ЙЕ-дер]", "каждый", "15+ раз"],
        ["keiner", "[КАЙ-нер]", "никто", "10+ раз"],
        ["beide", "[БАЙ-де]", "оба", "12+ раз"],
        ["einige", "[АЙ-ни-ге]", "некоторые", "8+ раз"],
        ["manche", "[МАН-хе]", "некоторые", "6+ раз"],
    ],
    "Предлоги и союзы": [
        ["gegen", "[ГЕ-ген]", "против", "15+ раз"],
        ["ohne", "[О-не]", "без", "20+ раз"],
        ["durch", "[ДУРХ]", "через", "12+ раз"],
        ["trotz", "[ТРОЦ]", "несмотря на", "8+ раз"],
        ["wegen", "[ВЕ-ген]", "из-за", "10+ раз"],
        ["während", "[ВЕ-ренд]", "во время", "8+ раз"],
        ["zwischen", "[ЦВИ-шен]", "между", "10+ раз"],
        ["sowie", "[зо-ВИ]", "а также", "6+ раз"],
        ["obwohl", "[об-ВОЛЬ]", "хотя", "8+ раз"],
        ["damit", "[да-МИТ]", "чтобы", "15+ раз"],
        ["bevor", "[бе-ФОР]", "прежде чем", "6+ раз"],
        ["nachdem", "[НАХ-дем]", "после того как", "5+ раз"],
    ],
    "Числа и количество": [
        ["einmal", "[АЙН-маль]", "один раз", "10+ раз"],
        ["zweimal", "[ЦВАЙ-маль]", "два раза", "5+ раз"],
        ["drei", "[ДРАЙ]", "три", "15+ раз"],
        ["vier", "[ФИР]", "четыре", "8+ раз"],
        ["fünf", "[ФЮНФ]", "пять", "10+ раз"],
        ["zehn", "[ЦЕН]", "десять", "6+ раз"],
        ["hundert", "[ХУН-дерт]", "сто", "20+ раз"],
        ["tausend", "[ТАУ-зенд]", "тысяча", "8+ раз"],
    ],
    "Время": [
        ["der Tag", "[дер ТАГ]", "день", "25+ раз"],
        ["die Nacht", "[ди НАХТ]", "ночь", "30+ раз"],
        ["der Morgen", "[дер МОР-ген]", "утро", "10+ раз"],
        ["der Abend", "[дер А-бенд]", "вечер", "8+ раз"],
        ["die Woche", "[ди ВО-хе]", "неделя", "5+ раз"],
        ["der Monat", "[дер МО-нат]", "месяц", "6+ раз"],
        ["das Jahr", "[дас ЯР]", "год", "10+ раз"],
        ["die Stunde", "[ди ШТУН-де]", "час", "12+ раз"],
    ],
    "Базовые существительные": [
        ["der Mensch", "[дер МЕНШ]", "человек", "20+ раз"],
        ["die Frau", "[ди ФРАУ]", "женщина", "15+ раз"],
        ["der Mann", "[дер МАН]", "мужчина", "25+ раз"],
        ["das Kind", "[дас КИНД]", "ребенок", "18+ раз"],
        ["die Leute", "[ди ЛОЙ-те]", "люди", "12+ раз"],
        ["der Freund", "[дер ФРОЙНД]", "друг", "10+ раз"],
        ["das Haus", "[дас ХАУС]", "дом", "15+ раз"],
        ["die Stadt", "[ди ШТАДТ]", "город", "8+ раз"],
        ["das Land", "[дас ЛАНД]", "страна", "12+ раз"],
        ["die Welt", "[ди ВЕЛЬТ]", "мир", "20+ раз"],
        ["das Ding", "[дас ДИНГ]", "вещь", "10+ раз"],
        ["die Sache", "[ди ЗА-хе]", "дело/вещь", "15+ раз"],
        ["die Hand", "[ди ХАНД]", "рука", "30+ раз"],
        ["der Kopf", "[дер КОПФ]", "голова", "20+ раз"],
        ["das Gesicht", "[дас ге-ЗИХТ]", "лицо", "15+ раз"],
        ["die Stimme", "[ди ШТИМ-ме]", "голос", "12+ раз"],
        ["das Wort", "[дас ВОРТ]", "слово", "25+ раз"],
    ],
    "Базовые прилагательные": [
        ["andere", "[АН-де-ре]", "другой", "20+ раз"],
        ["gleich", "[ГЛАЙХ]", "одинаковый", "10+ раз"],
        ["ganze", "[ГАН-це]", "целый", "15+ раз"],
        ["letzte", "[ЛЕТЦ-те]", "последний", "12+ раз"],
        ["erste", "[ЕРС-те]", "первый", "10+ раз"],
        ["nächste", "[НЕХС-те]", "следующий", "8+ раз"],
        ["einzige", "[АЙН-ци-ге]", "единственный", "10+ раз"],
        ["richtig", "[РИХ-тиг]", "правильный", "12+ раз"],
        ["eigene", "[АЙ-ге-не]", "собственный", "15+ раз"],
        ["beste", "[БЕС-те]", "лучший", "10+ раз"],
        ["schlimme", "[ШЛИМ-ме]", "плохой", "8+ раз"],
        ["schlechte", "[ШЛЕХ-те]", "плохой", "10+ раз"],
    ]
}

def create_pdf():
    """Создает PDF файл со словарем"""
    
    # Создаем документ
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Контейнер для элементов
    elements = []
    
    # Стили
    styles = getSampleStyleSheet()
    
    # Создаем кастомные стили
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2E3440'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName=font_bold
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#5E81AC'),
        spaceAfter=12,
        fontName=font_bold
    )
    
    info_style = ParagraphStyle(
        'InfoStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#4C566A'),
        alignment=TA_CENTER,
        fontName=font_name
    )
    
    # Заголовок документа
    title = Paragraph("ДОПОЛНИТЕЛЬНЫЙ СЛОВАРЬ A2", title_style)
    elements.append(title)
    
    subtitle = Paragraph(
        "Слова из König Lear, отсутствующие в основном словаре<br/>116 слов • Уровень A2",
        info_style
    )
    elements.append(subtitle)
    elements.append(Spacer(1, 20))
    
    # Информация о документе
    date_info = Paragraph(
        f"Дата создания: {datetime.now().strftime('%d.%m.%Y')}<br/>Проект: Lir - Немецкий через Короля Лира",
        info_style
    )
    elements.append(date_info)
    elements.append(Spacer(1, 30))
    
    # Счетчик слов
    total_words = 0
    
    # Создаем таблицы для каждой категории
    for category, words in vocabulary_data.items():
        # Заголовок категории
        # Определяем приоритет по названию категории
        if "КРИТИЧНО" in category or "ОЧЕНЬ ВАЖНО" in category:
            priority = "🔴 "
        elif "Вопросительные" in category or "Местоимения" in category or "Предлоги" in category or "Базовые существительные" in category:
            priority = "🟡 "
        else:
            priority = "🟢 "
        
        # Убираем emoji для PDF (могут не отображаться)
        priority_text = ""
        if "КРИТИЧНО" in category or "ОЧЕНЬ ВАЖНО" in category:
            priority_text = "[КРИТИЧНО] "
        elif "Вопросительные" in category or "Местоимения" in category:
            priority_text = "[ВАЖНО] "
        else:
            priority_text = ""
            
        heading = Paragraph(f"{priority_text}{category}", heading_style)
        elements.append(heading)
        
        # Заголовки таблицы
        table_data = [["Немецкий", "Транскрипция", "Русский", "Частота"]]
        
        # Добавляем слова
        table_data.extend(words)
        total_words += len(words)
        
        # Создаем таблицу
        table = Table(table_data, colWidths=[4*cm, 4*cm, 6*cm, 3*cm])
        
        # Стиль таблицы
        table.setStyle(TableStyle([
            # Заголовок
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#5E81AC')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), font_bold),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            
            # Данные
            ('FONTNAME', (0, 1), (-1, -1), font_name),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),  # Немецкий
            ('ALIGN', (1, 1), (1, -1), 'CENTER'),  # Транскрипция
            ('ALIGN', (2, 1), (2, -1), 'LEFT'),  # Русский
            ('ALIGN', (3, 1), (3, -1), 'CENTER'),  # Частота
            
            # Границы
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#4C566A')),
            
            # Чередование цветов строк
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F0F4F8')]),
            
            # Padding
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 20))
    
    # Итоговая статистика
    elements.append(PageBreak())
    
    stats_title = Paragraph("ИТОГОВАЯ СТАТИСТИКА", heading_style)
    elements.append(stats_title)
    
    # Таблица статистики
    stats_data = [
        ["Приоритет", "Категория", "Количество слов"],
        ["КРИТИЧНО", "Модальные глаголы", "6"],
        ["КРИТИЧНО", "Базовые глаголы", "26"],
        ["КРИТИЧНО", "Наречия и частицы", "14"],
        ["ВАЖНО", "Вопросительные слова", "8"],
        ["ВАЖНО", "Местоимения", "9"],
        ["ВАЖНО", "Предлоги и союзы", "13"],
        ["ВАЖНО", "Базовые существительные", "17"],
        ["ПОЛЕЗНО", "Числа", "8"],
        ["ПОЛЕЗНО", "Время", "8"],
        ["ПОЛЕЗНО", "Прилагательные", "12"],
        ["", "", ""],
        ["ИТОГО", "Всего слов уровня A2", str(total_words)],
    ]
    
    stats_table = Table(stats_data, colWidths=[4*cm, 8*cm, 4*cm])
    
    stats_table.setStyle(TableStyle([
        # Заголовок
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4C566A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), font_bold),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        
        # Итоговая строка
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#88C0D0')),
        ('FONTNAME', (0, -1), (-1, -1), font_bold),
        ('FONTSIZE', (0, -1), (-1, -1), 12),
        
        # Остальные стили
        ('FONTNAME', (0, 1), (-1, -2), font_name),
        ('FONTSIZE', (0, 1), (-1, -2), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    elements.append(stats_table)
    
    # Создаем PDF
    doc.build(elements)
    print(f"[OK] PDF создан: {output_path}")
    print(f"[INFO] Всего слов в словаре: {total_words}")
    return output_path

# Запускаем создание PDF
if __name__ == "__main__":
    try:
        pdf_path = create_pdf()
        print(f"[SUCCESS] Словарь A2 сохранен в PDF")
        print(f"[PATH] {pdf_path}")
        
        # Открываем PDF
        import subprocess
        subprocess.run(['start', '', pdf_path], shell=True)
        
    except Exception as e:
        print(f"[ERROR] Ошибка создания PDF: {e}")
        print("[TIP] Установите reportlab: pip install reportlab")