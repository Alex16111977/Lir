"""Utility mixin with data loading helpers for the JSON generator."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List

from .base import LessonContext, transliterate_filename


class GeneratorUtils:
    """Utility helpers mixed into the main generator."""

    def _collect_lessons(self, data_dir: Path) -> Dict[str, List[LessonContext]]:
        """Load all JSON lessons grouped by category."""

        lessons: Dict[str, List[LessonContext]] = {cat: [] for cat in self.categories}

        for category in self.categories:
            category_dir = data_dir / category
            if not category_dir.exists():
                self._log("warning", f"[JSON] Категорія {category} відсутня")
                continue

            for json_file in sorted(category_dir.glob("*.json")):
                lesson_data = self._load_json(json_file)
                if not lesson_data:
                    continue

                lesson_id = lesson_data.get("id") or json_file.stem
                safe_id = lesson_data.get("safe_id") or transliterate_filename(lesson_id)
                group = lesson_data.get("group", "ungrouped")

                lessons[category].append(
                    LessonContext(
                        data=lesson_data,
                        category=category,
                        group=group,
                        source=json_file,
                        safe_id=safe_id,
                    )
                )

        return lessons

    def _group_by(self, lessons: Iterable[LessonContext]) -> Dict[str, List[LessonContext]]:
        grouped: Dict[str, List[LessonContext]] = defaultdict(list)
        for ctx in lessons:
            grouped[ctx.group or "ungrouped"].append(ctx)
        return grouped
