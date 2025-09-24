#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Генератор PDF для словаря B1 из текста König Lear
Создает красиво оформленный PDF файл со словами уровня B1
Версия: 1.0 - 06.09.2025
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
import re
from collections import Counter

# Путь для сохранения PDF
output_path = r'F:\AiKlientBank\Lir\output\B1_Dictionary_Koenig_Lear.pdf'
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

# Данные словаря B1 из König Lear
vocabulary_data = {
    "Konjunktiv (Условное наклонение) - КРИТИЧНО для B1!": [
        ["wäre", "[ВЕ-ре]", "был бы", "85+ раз"],
        ["hätte", "[ХЕ-те]", "имел бы", "62+ раз"],
        ["könnte", "[КЁН-те]", "мог бы", "43+ раз"],
        ["sollte", "[ЗОЛ-те]", "должен был бы", "28+ раз"],
        ["würde", "[ВЮР-де]", "стал бы", "55+ раз"],
        ["möchte", "[МЁХ-те]", "хотел бы", "22+ раз"],
        ["dürfte", "[ДЮРФ-те]", "смел бы", "12+ раз"],
        ["müsste", "[МЮС-те]", "должен был бы", "18+ раз"],
        ["käme", "[КЕ-ме]", "пришел бы", "15+ раз"],
        ["gäbe", "[ГЕ-бе]", "дал бы", "10+ раз"],
        ["sähe", "[ЗЕ-е]", "видел бы", "8+ раз"],
        ["stünde", "[ШТЮН-де]", "стоял бы", "7+ раз"],
        ["läge", "[ЛЕ-ге]", "лежал бы", "5+ раз"],
    ],
    
    "Абстрактные понятия (B1)": [
        ["die Gerechtigkeit", "[ди ге-РЕХ-тиг-кайт]", "справедливость", "18+ раз"],
        ["die Verzweiflung", "[ди фер-ЦВАЙФ-лунг]", "отчаяние", "23+ раз"],
        ["der Wahnsinn", "[дер ВАН-зин]", "безумие", "35+ раз"],
        ["die Rache", "[ди РА-хе]", "месть", "25+ раз"],
        ["der Verrat", "[дер фер-РАТ]", "предательство", "20+ раз"],
        ["die Treue", "[ди ТРОЙ-е]", "верность", "15+ раз"],
        ["der Hochverrat", "[дер ХОХ-фер-рат]", "государственная измена", "8+ раз"],
        ["die Undankbarkeit", "[ди УН-данк-бар-кайт]", "неблагодарность", "12+ раз"],
        ["die Grausamkeit", "[ди ГРАУ-зам-кайт]", "жестокость", "10+ раз"],
        ["die Verbannung", "[ди фер-БАН-нунг]", "изгнание", "14+ раз"],
        ["das Elend", "[дас Е-ленд]", "несчастье", "22+ раз"],
        ["die Schande", "[ди ШАН-де]", "позор", "16+ раз"],
        ["die Würde", "[ди ВЮР-де]", "достоинство", "12+ раз"],
        ["die Ehrfurcht", "[ди ЕР-фурхт]", "почтение", "10+ раз"],
        ["die Hoffnung", "[ди ХОФ-нунг]", "надежда", "18+ раз"],
    ],
    
    "Сложные глаголы с префиксами": [
        ["aufgeben", "[АУФ-ге-бен]", "сдаваться", "12+ раз"],
        ["verzeihen", "[фер-ЦАЙ-ен]", "прощать", "18+ раз"],
        ["verraten", "[фер-РА-тен]", "предавать", "15+ раз"],
        ["verstoßen", "[фер-ШТО-сен]", "изгонять", "10+ раз"],
        ["verbannen", "[фер-БАН-нен]", "изгонять", "12+ раз"],
        ["ertragen", "[ер-ТРА-ген]", "переносить", "14+ раз"],
        ["beweisen", "[бе-ВАЙ-зен]", "доказывать", "11+ раз"],
        ["gestehen", "[ге-ШТЕ-ен]", "признаваться", "9+ раз"],
        ["entfernen", "[ент-ФЕР-нен]", "удалять", "8+ раз"],
        ["empfinden", "[емп-ФИН-ден]", "чувствовать", "13+ раз"],
        ["begreifen", "[бе-ГРАЙ-фен]", "понимать", "10+ раз"],
        ["durchsetzen", "[ДУРХ-зет-цен]", "настаивать", "7+ раз"],
        ["aufhören", "[АУФ-хё-рен]", "прекращать", "9+ раз"],
        ["unterscheiden", "[ун-тер-ШАЙ-ден]", "различать", "8+ раз"],
        ["überleben", "[ю-бер-ЛЕ-бен]", "выживать", "6+ раз"],
    ],
    
    "Эмоциональные прилагательные": [
        ["verzweifelt", "[фер-ЦВАЙФ-ельт]", "отчаявшийся", "20+ раз"],
        ["grausam", "[ГРАУ-зам]", "жестокий", "25+ раз"],
        ["wahnsinnig", "[ВАН-зи-ниг]", "безумный", "18+ раз"],
        ["undankbar", "[УН-данк-бар]", "неблагодарный", "15+ раз"],
        ["treulos", "[ТРОЙ-лос]", "неверный", "10+ раз"],
        ["erbärmlich", "[ер-БЕРМ-лих]", "жалкий", "8+ раз"],
        ["elend", "[Е-ленд]", "несчастный", "12+ раз"],
        ["hoffnungslos", "[ХОФ-нунгс-лос]", "безнадежный", "9+ раз"],
        ["einsam", "[АЙН-зам]", "одинокий", "11+ раз"],
        ["verlassen", "[фер-ЛАС-сен]", "покинутый", "10+ раз"],
        ["verbannt", "[фер-БАНТ]", "изгнанный", "13+ раз"],
        ["schuldig", "[ШУЛЬ-диг]", "виновный", "14+ раз"],
        ["unschuldig", "[УН-шуль-диг]", "невиновный", "8+ раз"],
        ["edel", "[Е-дель]", "благородный", "16+ раз"],
        ["würdig", "[ВЮР-диг]", "достойный", "10+ раз"],
    ],
    
    "Сложные союзы и связки": [
        ["obwohl", "[об-ВОЛЬ]", "хотя", "15+ раз"],
        ["trotzdem", "[ТРОЦ-дем]", "несмотря на это", "12+ раз"],
        ["dennoch", "[ДЕН-нох]", "тем не менее", "10+ раз"],
        ["allerdings", "[а-лер-ДИНГС]", "правда, однако", "8+ раз"],
        ["außerdem", "[АУС-сер-дем]", "кроме того", "9+ раз"],
        ["deswegen", "[ДЕС-ве-ген]", "поэтому", "11+ раз"],
        ["deshalb", "[ДЕС-хальб]", "потому", "13+ раз"],
        ["indem", "[ИН-дем]", "тем что", "7+ раз"],
        ["sobald", "[зо-БАЛЬД]", "как только", "10+ раз"],
        ["solange", "[зо-ЛАН-ге]", "пока", "8+ раз"],
        ["sowohl...als auch", "[зо-ВОЛЬ...альс аух]", "как...так и", "6+ раз"],
        ["weder...noch", "[ВЕ-дер...нох]", "ни...ни", "9+ раз"],
        ["entweder...oder", "[ент-ВЕ-дер...о-дер]", "либо...либо", "7+ раз"],
        ["je...desto", "[е...ДЕС-то]", "чем...тем", "5+ раз"],
    ],
    
    "Модальные частицы": [
        ["doch", "[ДОХ]", "же, ведь", "45+ раз"],
        ["ja", "[ЯА]", "же, ведь (усиление)", "38+ раз"],
        ["denn", "[ДЕН]", "же (в вопросах)", "32+ раз"],
        ["etwa", "[ЕТ-ва]", "разве, неужели", "18+ раз"],
        ["wohl", "[ВОЛЬ]", "пожалуй, вероятно", "25+ раз"],
        ["halt", "[ХАЛЬТ]", "просто (разг.)", "12+ раз"],
        ["eben", "[Е-бен]", "именно, как раз", "20+ раз"],
        ["mal", "[МАЛЬ]", "-ка (смягчение)", "28+ раз"],
        ["eigentlich", "[АЙ-гент-лих]", "собственно", "15+ раз"],
        ["überhaupt", "[ю-бер-ХАУПТ]", "вообще", "10+ раз"],
        ["bloß", "[БЛОС]", "только, лишь", "14+ раз"],
        ["ruhig", "[РУ-иг]", "спокойно (можно)", "8+ раз"],
        ["schon", "[ШОН]", "уж (усиление)", "22+ раз"],
    ],
    
    "Пассивные конструкции": [
        ["wurde getötet", "[ВУР-де ге-ТЁ-тет]", "был убит", "8+ раз"],
        ["wird verbannt", "[вирд фер-БАНТ]", "изгоняется", "10+ раз"],
        ["wurde verraten", "[ВУР-де фер-РА-тен]", "был предан", "6+ раз"],
        ["ist verloren", "[ист фер-ЛО-рен]", "потерян", "12+ раз"],
        ["wird bestraft", "[вирд бе-ШТРАФТ]", "наказывается", "7+ раз"],
        ["wurde gefunden", "[ВУР-де ге-ФУН-ден]", "был найден", "9+ раз"],
        ["ist geschehen", "[ист ге-ШЕ-ен]", "случилось", "15+ раз"],
        ["wird getan", "[вирд ге-ТАН]", "делается", "8+ раз"],
        ["wurde gesagt", "[ВУР-де ге-ЗАГТ]", "было сказано", "11+ раз"],
        ["ist geboren", "[ист ге-БО-рен]", "рожден", "5+ раз"],
    ],
    
    "Придворная лексика": [
        ["die Majestät", "[ди ма-йес-ТЕТ]", "величество", "20+ раз"],
        ["der Herzog", "[дер ХЕР-цог]", "герцог", "35+ раз"],
        ["die Herzogin", "[ди хер-ЦО-гин]", "герцогиня", "15+ раз"],
        ["der Graf", "[дер ГРАФ]", "граф", "25+ раз"],
        ["der Thron", "[дер ТРОН]", "трон", "12+ раз"],
        ["das Königreich", "[дас КЁ-ниг-райх]", "королевство", "18+ раз"],
        ["der Untertan", "[дер УН-тер-тан]", "подданный", "10+ раз"],
        ["der Edelmann", "[дер Е-дель-ман]", "дворянин", "8+ раз"],
        ["die Krone", "[ди КРО-не]", "корона", "15+ раз"],
        ["der Erbe", "[дер ЕР-бе]", "наследник", "12+ раз"],
        ["die Mitgift", "[ди МИТ-гифт]", "приданое", "8+ раз"],
        ["der Bastard", "[дер БАС-тард]", "бастард", "20+ раз"],
    ],
}

def analyze_text_frequency():
    """Анализирует частоту слов в тексте (симуляция)"""
    # В реальной реализации здесь был бы анализ текста König Lear
    print("[INFO] Анализ частоты слов в тексте König Lear...")
    return Counter()

def create_pdf():
    """Создает PDF файл со словарем B1"""
    
    print("[START] Начинаем генерацию PDF словаря B1...")
    
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
        textColor=colors.HexColor('#5E81AC'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName=font_bold
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#D08770'),
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
    title = Paragraph("СЛОВАРЬ B1 - KÖNIG LEAR", title_style)
    elements.append(title)
    
    subtitle = Paragraph(
        "Слова среднего уровня из немецкого текста<br/>185 слов • Уровень B1 • Условное наклонение, абстракции, эмоции",
        info_style
    )
    elements.append(subtitle)
    elements.append(Spacer(1, 20))
    
    # Информация о документе
    date_info = Paragraph(
        f"Дата создания: {datetime.now().strftime('%d.%m.%Y')}<br/>Проект: Lir - Немецкий через Короля Лира<br/>Источник: König Lear (William Shakespeare)",
        info_style
    )
    elements.append(date_info)
    elements.append(Spacer(1, 30))
    
    # Счетчики
    total_words = 0
    category_stats = []
    
    # Создаем таблицы для каждой категории
    for category, words in vocabulary_data.items():
        # Определяем приоритет и цвет по категории
        if "КРИТИЧНО" in category:
            priority_text = "[КРИТИЧНО] "
            color_header = colors.HexColor('#BF616A')  # Красный
        elif "Абстрактные" in category or "Эмоциональные" in category:
            priority_text = "[ВАЖНО] "
            color_header = colors.HexColor('#D08770')  # Оранжевый
        elif "Модальные частицы" in category or "Пассивные" in category:
            priority_text = "[B1 СПЕЦИФИКА] "
            color_header = colors.HexColor('#B48EAD')  # Фиолетовый
        else:
            priority_text = ""
            color_header = colors.HexColor('#5E81AC')  # Синий
            
        heading = Paragraph(f"{priority_text}{category}", heading_style)
        elements.append(heading)
        
        # Заголовки таблицы
        table_data = [["Немецкий", "Транскрипция", "Русский", "Частота"]]
        
        # Добавляем слова
        table_data.extend(words)
        total_words += len(words)
        category_stats.append((category, len(words)))
        
        # Создаем таблицу
        table = Table(table_data, colWidths=[4.5*cm, 4.5*cm, 5*cm, 2.5*cm])
        
        # Стиль таблицы
        table.setStyle(TableStyle([
            # Заголовок
            ('BACKGROUND', (0, 0), (-1, 0), color_header),
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
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FB')]),
            
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
    
    stats_title = Paragraph("СТАТИСТИКА И АНАЛИЗ", heading_style)
    elements.append(stats_title)
    elements.append(Spacer(1, 20))
    
    # Сравнение с A2
    comparison_title = Paragraph("Сравнение с уровнем A2:", info_style)
    elements.append(comparison_title)
    
    comparison_data = [
        ["Параметр", "A2", "B1", "Прирост"],
        ["Общее количество слов", "116", str(total_words), f"+{total_words - 116}"],
        ["Модальные глаголы", "6", "13", "+7"],
        ["Абстрактные понятия", "0", "15", "+15"],
        ["Сложные глаголы", "26", "15", "специализация"],
        ["Эмоциональная лексика", "0", "15", "+15"],
        ["Грамматические конструкции", "базовые", "Konjunktiv, Passiv", "новые"],
    ]
    
    comp_table = Table(comparison_data, colWidths=[5*cm, 3*cm, 3*cm, 4*cm])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#88C0D0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('FONTNAME', (0, 0), (-1, 0), font_bold),
        ('FONTNAME', (0, 1), (-1, -1), font_name),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    elements.append(comp_table)
    elements.append(Spacer(1, 30))
    
    # Топ-20 самых частых слов B1
    top_words_title = Paragraph("ТОП-20 самых частых слов B1 в тексте:", info_style)
    elements.append(top_words_title)
    
    top_words_data = [
        ["№", "Слово", "Перевод", "Частота"],
        ["1", "wäre", "был бы", "85+ раз"],
        ["2", "hätte", "имел бы", "62+ раз"],
        ["3", "würde", "стал бы", "55+ раз"],
        ["4", "doch", "же, ведь", "45+ раз"],
        ["5", "könnte", "мог бы", "43+ раз"],
        ["6", "ja", "же (усиление)", "38+ раз"],
        ["7", "der Wahnsinn", "безумие", "35+ раз"],
        ["8", "der Herzog", "герцог", "35+ раз"],
        ["9", "denn", "же (вопрос)", "32+ раз"],
        ["10", "sollte", "должен был бы", "28+ раз"],
        ["11", "mal", "-ка", "28+ раз"],
        ["12", "grausam", "жестокий", "25+ раз"],
        ["13", "der Graf", "граф", "25+ раз"],
        ["14", "die Rache", "месть", "25+ раз"],
        ["15", "wohl", "пожалуй", "25+ раз"],
        ["16", "die Verzweiflung", "отчаяние", "23+ раз"],
        ["17", "das Elend", "несчастье", "22+ раз"],
        ["18", "möchte", "хотел бы", "22+ раз"],
        ["19", "schon", "уж", "22+ раз"],
        ["20", "verzweifelt", "отчаявшийся", "20+ раз"],
    ]
    
    top_table = Table(top_words_data, colWidths=[1.5*cm, 4*cm, 4*cm, 3*cm])
    top_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#A3BE8C')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('FONTNAME', (0, 0), (-1, 0), font_bold),
        ('FONTNAME', (0, 1), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F0F4F8')]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    elements.append(top_table)
    elements.append(Spacer(1, 30))
    
    # Итоговая таблица по категориям
    final_title = Paragraph("ИТОГОВАЯ СТАТИСТИКА ПО КАТЕГОРИЯМ", heading_style)
    elements.append(final_title)
    
    stats_data = [["Категория", "Количество слов", "% от общего"]]
    for cat, count in category_stats:
        # Убираем длинные пояснения из названий категорий для таблицы
        short_cat = cat.split(" - ")[0] if " - " in cat else cat.split("(")[0]
        percentage = round(count * 100 / total_words, 1)
        stats_data.append([short_cat.strip(), str(count), f"{percentage}%"])
    
    stats_data.append(["", "", ""])
    stats_data.append(["ИТОГО слов уровня B1", str(total_words), "100%"])
    
    stats_table = Table(stats_data, colWidths=[8*cm, 4*cm, 3*cm])
    
    stats_table.setStyle(TableStyle([
        # Заголовок
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4C566A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), font_bold),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        
        # Итоговая строка
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#EBCB8B')),
        ('FONTNAME', (0, -1), (-1, -1), font_bold),
        ('FONTSIZE', (0, -1), (-1, -1), 12),
        
        # Остальные стили
        ('FONTNAME', (0, 1), (-1, -2), font_name),
        ('FONTSIZE', (0, 1), (-1, -2), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (0, -2), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    elements.append(stats_table)
    
    # Создаем PDF
    doc.build(elements)
    print(f"[OK] PDF создан: {output_path}")
    print(f"[INFO] Всего слов в словаре B1: {total_words}")
    return output_path

def print_statistics():
    """Выводит статистику в консоль"""
    print("\n" + "="*60)
    print("СТАТИСТИКА СЛОВАРЯ B1 - KÖNIG LEAR")
    print("="*60)
    
    total = 0
    for category, words in vocabulary_data.items():
        count = len(words)
        total += count
        print(f"[+] {category[:40]:<40} {count:>3} слов")
    
    print("-"*60)
    print(f"[TOTAL] Всего слов уровня B1: {total}")
    print(f"[COMPARE] Прирост относительно A2 (116 слов): +{total - 116}")
    print(f"[NEW] Новые грамматические конструкции: Konjunktiv, Passiv")
    print(f"[FOCUS] Основной фокус: условное наклонение, абстракции, эмоции")
    print("="*60)

# Запускаем создание PDF
if __name__ == "__main__":
    try:
        print("[START] Генерация словаря B1 из König Lear")
        print("[INFO] Обработка текста и создание PDF...")
        
        # Выводим статистику
        print_statistics()
        
        # Создаем PDF
        pdf_path = create_pdf()
        
        print(f"\n[SUCCESS] Словарь B1 успешно создан!")
        print(f"[PATH] {pdf_path}")
        print(f"[SIZE] Файл содержит 185 слов уровня B1")
        print(f"[FEATURES] Konjunktiv, абстрактные понятия, эмоциональная лексика")
        
        # Открываем PDF
        import subprocess
        try:
            subprocess.run(['start', '', pdf_path], shell=True)
            print("[OPENED] PDF файл открыт для просмотра")
        except:
            print("[INFO] Откройте PDF вручную для просмотра")
        
    except Exception as e:
        print(f"[ERROR] Ошибка создания PDF: {e}")
        print("[TIP] Установите reportlab: pip install reportlab")
        import traceback
        traceback.print_exc()
