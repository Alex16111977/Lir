"""
Повний аналіз німецьких слів проекту Lir (без pandas)
Автор: AI Assistant
Дата: 23.08.2025
Версія: 2.0
"""

import json
import sys
import os
import csv
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

# Встановлюємо базовий шлях
BASE_PATH = Path(r'F:\AiKlientBank\Lir')
DATA_PATH = BASE_PATH / 'data'
REPORT_PATH = BASE_PATH / 'reports' / 'vocabulary_analysis'

class VocabularyAnalyzer:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.all_words = []
        self.statistics = {
            'total': {'files': 0, 'words': 0, 'unique': 0},
            'a2': {'files': 0, 'words': 0, 'types': {}},
            'b1': {'files': 0, 'words': 0, 'types': {}},
            'thematic': {'files': 0, 'words': 0, 'types': {}}
        }
        self.duplicates = defaultdict(list)
        self.characters_stats = Counter()
        
    def extract_from_json(self, filepath):
        """Витягує слова з JSON файлу"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            words = []
            level = filepath.parent.name
            filename = filepath.stem
            
            if 'vocabulary' in data:
                for idx, word in enumerate(data['vocabulary']):
                    word_entry = {
                        'id': f"{level}_{filename}_{idx}",
                        'german': word.get('german', ''),
                        'russian': word.get('translation', ''),
                        'transcription': word.get('transcription', ''),
                        'type': word.get('type', 'невідомо'),
                        'level': level.upper(),
                        'lesson': filename,
                        'character': '',
                        'emotion': '',
                        'gesture': ''
                    }
                    
                    # Витягуємо character_voice
                    if 'character_voice' in word:
                        word_entry['character'] = word['character_voice'].get('character', '')
                        if word_entry['character']:
                            self.characters_stats[word_entry['character']] += 1
                    
                    # Витягуємо gesture
                    if 'gesture' in word:
                        word_entry['emotion'] = word['gesture'].get('emotion', '')
                        word_entry['gesture'] = word['gesture'].get('gesture', '')
                    
                    words.append(word_entry)
                    
            return words
        except Exception as e:
            print(f"[ERROR] Файл {filepath}: {e}")
            return []
    
    def analyze_all_data(self):
        """Аналізує всі JSON файли"""
        print("[START] Аналіз даних...")
        print("-" * 50)
        
        for level in ['a2', 'b1', 'thematic']:
            level_path = DATA_PATH / level
            if not level_path.exists():
                print(f"[SKIP] Папка {level} не існує")
                continue
            
            json_files = list(level_path.glob('*.json'))
            print(f"[{level.upper()}] Знайдено {len(json_files)} файлів")
            
            for filepath in json_files:
                words = self.extract_from_json(filepath)
                self.all_words.extend(words)
                
                # Оновлюємо статистику
                self.statistics[level]['files'] += 1
                self.statistics[level]['words'] += len(words)
                self.statistics['total']['files'] += 1
                self.statistics['total']['words'] += len(words)
                
                # Рахуємо типи слів
                for word in words:
                    word_type = word['type']
                    if word_type not in self.statistics[level]['types']:
                        self.statistics[level]['types'][word_type] = 0
                    self.statistics[level]['types'][word_type] += 1
                
                print(f"  [{filepath.stem}]: {len(words)} слів")
        
        # Знаходимо унікальні та дублікати
        german_words = {}
        for word in self.all_words:
            german = word['german'].lower()
            if german in german_words:
                if german not in self.duplicates:
                    self.duplicates[german] = [german_words[german]]
                self.duplicates[german].append(word)
            else:
                german_words[german] = word
        
        self.statistics['total']['unique'] = len(german_words)
        print("-" * 50)
        print(f"[OK] Всього проаналізовано: {self.statistics['total']['words']} слів")
    
    def generate_csv_report(self):
        """Створює CSV звіт замість Excel"""
        # Головний CSV з усіма словами
        output_file = REPORT_PATH / f'words_full_report_{self.timestamp}.csv'
        
        with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            fieldnames = ['id', 'german', 'russian', 'transcription', 'type', 
                         'level', 'lesson', 'character', 'emotion', 'gesture']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            # Сортуємо слова
            sorted_words = sorted(self.all_words, key=lambda x: (x['level'], x['german'].lower()))
            writer.writerows(sorted_words)
        
        print(f"[OK] CSV звіт збережено: {output_file.name}")
        
        # CSV зі статистикою
        stats_file = REPORT_PATH / f'statistics_summary_{self.timestamp}.csv'
        with open(stats_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Рівень', 'Файлів', 'Слів', 'Середнє слів/урок'])
            
            for level in ['a2', 'b1', 'thematic']:
                if self.statistics[level]['files'] > 0:
                    avg = round(self.statistics[level]['words'] / self.statistics[level]['files'], 1)
                    writer.writerow([level.upper(), 
                                   self.statistics[level]['files'],
                                   self.statistics[level]['words'],
                                   avg])
            
            # Загальна статистика
            if self.statistics['total']['files'] > 0:
                avg_total = round(self.statistics['total']['words'] / self.statistics['total']['files'], 1)
                writer.writerow(['ВСЬОГО',
                               self.statistics['total']['files'],
                               self.statistics['total']['words'],
                               avg_total])
        
        print(f"[OK] CSV статистика збережена: {stats_file.name}")
        return output_file
    
    def generate_text_vocabulary(self):
        """Створює текстовий словник"""
        output_file = REPORT_PATH / f'vocabulary_list_{self.timestamp}.txt'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("НІМЕЦЬКО-РОСІЙСЬКИЙ СЛОВНИК\n")
            f.write("Проект: Німецька через Короля Ліра\n")
            f.write(f"Дата створення: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
            f.write("="*70 + "\n\n")
            
            # Загальна статистика
            f.write("СТАТИСТИКА:\n")
            f.write(f"  Всього слів: {self.statistics['total']['words']}\n")
            f.write(f"  Унікальних: {self.statistics['total']['unique']}\n")
            f.write(f"  Дублікатів: {len(self.duplicates)}\n")
            f.write(f"  Файлів оброблено: {self.statistics['total']['files']}\n")
            f.write("-"*70 + "\n\n")
            
            # По рівнях
            for level in ['a2', 'b1', 'thematic']:
                level_words = [w for w in self.all_words if w['level'] == level.upper()]
                if not level_words:
                    continue
                
                f.write(f"\n[{level.upper()}] РІВЕНЬ - {len(level_words)} слів\n")
                f.write("="*50 + "\n")
                
                # Групуємо по уроках
                lessons = defaultdict(list)
                for word in level_words:
                    lessons[word['lesson']].append(word)
                
                for lesson, words in sorted(lessons.items()):
                    f.write(f"\n  {lesson} ({len(words)} слів):\n")
                    f.write("  " + "-"*40 + "\n")
                    
                    # Сортуємо по алфавіту
                    words.sort(key=lambda x: x['german'].lower())
                    
                    for word in words:
                        f.write(f"    {word['german']:<25} - {word['russian']:<25}")
                        if word['type'] and word['type'] != 'невідомо':
                            f.write(f" ({word['type']})")
                        if word['transcription']:
                            f.write(f" {word['transcription']}")
                        f.write("\n")
            
            # Топ персонажів
            if self.characters_stats:
                f.write("\n" + "="*70 + "\n")
                f.write("ТОП ПЕРСОНАЖІВ КОРОЛЯ ЛІРА:\n")
                f.write("-"*40 + "\n")
                for char, count in self.characters_stats.most_common(10):
                    if char:
                        f.write(f"  {char:<20} - {count} слів\n")
        
        print(f"[OK] Текстовий словник збережено: {output_file.name}")
        return output_file
    
    def save_statistics_json(self):
        """Зберігає статистику в JSON"""
        output_file = REPORT_PATH / f'statistics_{self.timestamp}.json'
        
        stats = {
            'metadata': {
                'created': datetime.now().isoformat(),
                'version': '2.0',
                'author': 'VocabularyAnalyzer'
            },
            'summary': self.statistics,
            'duplicates_count': len(self.duplicates),
            'unique_words': self.statistics['total']['unique'],
            'characters': dict(self.characters_stats),
            'word_types': {
                level: self.statistics[level]['types']
                for level in ['a2', 'b1', 'thematic']
            }
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] JSON статистика збережена: {output_file.name}")
        return output_file
    
    def print_summary(self):
        """Виводить фінальний звіт в консоль"""
        print("\n" + "="*70)
        print("ФІНАЛЬНИЙ ЗВІТ")
        print("="*70)
        
        print(f"\nЗАГАЛЬНА СТАТИСТИКА:")
        print(f"  - Всього слів: {self.statistics['total']['words']}")
        print(f"  - Унікальних слів: {self.statistics['total']['unique']}")
        print(f"  - Дублікатів: {len(self.duplicates)}")
        print(f"  - Файлів оброблено: {self.statistics['total']['files']}")
        
        print(f"\nРОЗПОДІЛ ПО РІВНЯХ:")
        for level in ['a2', 'b1', 'thematic']:
            if self.statistics[level]['files'] > 0:
                print(f"  [{level.upper()}]:")
                print(f"    - Файлів: {self.statistics[level]['files']}")
                print(f"    - Слів: {self.statistics[level]['words']}")
                avg = round(self.statistics[level]['words'] / self.statistics[level]['files'], 1)
                print(f"    - Середнє: {avg} слів/урок")
        
        print(f"\nТОП-5 ПЕРСОНАЖІВ:")
        for char, count in self.characters_stats.most_common(5):
            if char:
                print(f"  - {char}: {count} слів")
        
        print(f"\n[+] ФАЙЛИ СТВОРЕНО:")
        print(f"  - CSV звіт: words_full_report_{self.timestamp}.csv")
        print(f"  - Текстовий словник: vocabulary_list_{self.timestamp}.txt")
        print(f"  - JSON статистика: statistics_{self.timestamp}.json")
    
    def run(self):
        """Головний метод запуску"""
        print("\n" + "="*70)
        print("ЗАПУСК АНАЛІЗУ СЛОВНИКОВОГО ЗАПАСУ")
        print("="*70)
        
        # Аналізуємо дані
        self.analyze_all_data()
        
        # Генеруємо звіти
        print("\n[ГЕНЕРАЦІЯ ЗВІТІВ]")
        self.generate_csv_report()
        self.generate_text_vocabulary()
        self.save_statistics_json()
        
        # Виводимо підсумок
        self.print_summary()
        
        print("\n" + "="*70)
        print("[OK] АНАЛІЗ ЗАВЕРШЕНО УСПІШНО!")
        print("="*70)
        
        return True

# Точка входу
if __name__ == "__main__":
    analyzer = VocabularyAnalyzer()
    analyzer.run()
