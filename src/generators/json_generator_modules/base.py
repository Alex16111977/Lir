"""Base utilities for the modular JSON → HTML generator."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


TRANSLIT_TABLE = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "Yo",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "Y",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "H",
    "Ц": "Ts",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ъ": "",
    "Ы": "Y",
    "Ь": "",
    "Э": "E",
    "Ю": "Yu",
    "Я": "Ya",
}


def transliterate_filename(text: str) -> str:
    """Return a filesystem friendly slug for a JSON lesson identifier."""

    safe = []
    for char in text:
        if char in TRANSLIT_TABLE:
            safe.append(TRANSLIT_TABLE[char])
        elif char.isalnum() or char in {".", "_", "-"}:
            safe.append(char)
        elif char.isspace():
            safe.append("_")
        else:
            safe.append("_")

    slug = "".join(safe)
    slug = re.sub(r"_+", "_", slug)
    return slug.strip("_") or "lesson"


@dataclass
class LessonContext:
    """Normalized information about a lesson."""

    data: Dict[str, Any]
    category: str
    group: str
    source: Path
    safe_id: str


class JsonGeneratorBase:
    """Common helpers reused by the specialised generator mixins."""

    categories: Iterable[str] = ("a2", "b1", "thematic")

    def __init__(self, logger: Any | None = None) -> None:
        self.logger = logger
        self.files_generated = 0
        self.words_processed = 0

    # ------------------------------------------------------------------
    # Logging helpers
    # ------------------------------------------------------------------
    def _log(self, level: str, message: str) -> None:
        if not self.logger:
            return

        log_method = getattr(self.logger, level, None)
        if callable(log_method):
            log_method(message)
        elif hasattr(self.logger, "info"):
            self.logger.info(message)

    # ------------------------------------------------------------------
    # Filesystem helpers
    # ------------------------------------------------------------------
    def _write_file(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        self.files_generated += 1
        self._log("info", f"[JSON] Saved: {path}")

    def _load_json(self, path: Path) -> Optional[Dict[str, Any]]:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            self._log("error", f"[JSON] Неможливо прочитати {path.name}: {exc}")
        except OSError as exc:
            self._log("error", f"[JSON] Помилка доступу до {path}: {exc}")
        return None

    # ------------------------------------------------------------------
    # Statistics helpers
    # ------------------------------------------------------------------
    def _update_vocabulary_stats(self, vocabulary: Iterable[Dict[str, Any]]) -> None:
        self.words_processed += sum(1 for item in vocabulary if item.get("german"))
