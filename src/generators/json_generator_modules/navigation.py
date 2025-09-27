"""Navigation helpers for the JSON lesson pages."""

from __future__ import annotations

from typing import Dict, List, Optional

from .base import LessonContext


class NavigationGenerator:
    """Build navigation blocks for lesson pages."""

    def _build_navigation(self, lessons: List[LessonContext], index: int) -> Dict[str, Optional[LessonContext]]:
        prev_ctx = lessons[index - 1] if index > 0 else None
        next_ctx = lessons[index + 1] if index + 1 < len(lessons) else None
        return {"prev": prev_ctx, "next": next_ctx}

    def _navigation_html(self, navigation: Dict[str, Optional[LessonContext]]) -> str:
        links = []
        prev_ctx = navigation.get("prev")
        next_ctx = navigation.get("next")

        if prev_ctx:
            links.append(
                f'<a class="nav-btn prev" href="{prev_ctx.safe_id}.html">← {prev_ctx.data.get("title", "Попередній урок")}</a>'
            )
        else:
            links.append('<span class="nav-btn prev disabled">← Немає</span>')

        links.append('<a class="nav-btn index" href="../index.html">Список уроків</a>')

        if next_ctx:
            links.append(
                f'<a class="nav-btn next" href="{next_ctx.safe_id}.html">{next_ctx.data.get("title", "Наступний урок")} →</a>'
            )
        else:
            links.append('<span class="nav-btn next disabled">Немає →</span>')

        return f"""
        <nav class="lesson-navigation">
            {' '.join(links)}
        </nav>
        """
