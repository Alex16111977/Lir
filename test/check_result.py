from pathlib import Path

output = Path(r"F:\AiKlientBank\Lir\texts\thematic_vocabulary_full.html")

if output.exists():
    with open(output, "r", encoding="utf-8") as f:
        content = f.read()
    
    size = len(content) / 1024
    has_toc = "table-of-contents" in content
    has_tables = "vocab-table" in content
    cards = content.count('<a href="#theme-')
    words = content.count('<tr class="word-row">')
    
    print(f"[OK] Файл: {output.name}")
    print(f"[OK] Розмір: {size:.2f} KB")
    print(f"[OK] Оглавлення: {'ТАК' if has_toc else 'НІ'}")
    print(f"[OK] Таблиці: {'ТАК' if has_tables else 'НІ'}")
    print(f"[OK] Карточки: {cards}")
    print(f"[OK] Слова: {words}")
else:
    print("[ERROR] Файл не знайдено")
