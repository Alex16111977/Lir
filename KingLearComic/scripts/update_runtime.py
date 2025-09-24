"""Проверка и обновление runtime файлов.

Скрипт використовував абсолютні Windows-шляхи і падав при запуску
на інших системах. Тепер він визначає директорію проекту відносно
розташування самого файлу і працює крос-платформенно.
"""

from __future__ import annotations

from pathlib import Path


def _load_file(path: Path) -> str:
    """Повертає вміст файлу або піднімає зрозумілу помилку."""

    if not path.exists():
        raise FileNotFoundError(f"Файл не знайдено: {path}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    base_dir = Path(__file__).resolve().parent.parent
    source_file = base_dir / "static" / "js" / "journey_runtime.js"
    output_file = base_dir / "output" / "static" / "js" / "journey_runtime.js"

    print("[INFO] Аналіз файлів...")
    print("=" * 60)

    try:
        source_content = _load_file(source_file)
        output_content = _load_file(output_file)
    except FileNotFoundError as error:
        print(f"[ERROR] {error}")
        print("[HINT] Запустіть генерацію сайту перед оновленням runtime.")
        return 1

    source_has_hint = "russianHint" in source_content
    output_has_hint = "russianHint" in output_content

    print("static/js/journey_runtime.js:")
    print(f"  - Розмір: {len(source_content)} символів")
    print(f"  - russianHint: {'ЗНАЙДЕНО' if source_has_hint else 'НЕ ЗНАЙДЕНО'}")
    if source_has_hint:
        print(f"  - Входжень: {source_content.count('russianHint')}")

    print("\noutput/static/js/journey_runtime.js:")
    print(f"  - Розмір: {len(output_content)} символів")
    print(f"  - russianHint: {'ЗНАЙДЕНО' if output_has_hint else 'НЕ ЗНАЙДЕНО'}")
    if output_has_hint:
        print(f"  - Входжень: {output_content.count('russianHint')}")

    if output_has_hint and not source_has_hint:
        print("\n[ACTION] Копіювання оновленого файлу з output до static...")
        source_file.write_text(output_content, encoding="utf-8")
        print("[OK] Файл скопійовано!")
        print("[OK] Перегенеруйте сайт, щоб застосувати зміни.")
    elif source_has_hint:
        print("\n[OK] Початковий файл вже містить russianHint")
    else:
        print("\n[ERROR] russianHint не знайдено ні в одному файлі!")
        return 1

    return 0


if __name__ == "__main__":  # pragma: no cover - допоміжний скрипт
    raise SystemExit(main())
