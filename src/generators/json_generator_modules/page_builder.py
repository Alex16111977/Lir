"""Build lesson pages using modular sections."""

from __future__ import annotations

from html import escape
from typing import Dict, Iterable, List

from .base import LessonContext


class PageBuilder:
    """Combine template blocks into full HTML documents."""

    def _build_lesson_page(self, ctx: LessonContext, navigation_html: str, exercises_html: str) -> str:
        data = ctx.data
        vocabulary = data.get("vocabulary", []) or []
        self._update_vocabulary_stats(vocabulary)

        sections: List[str] = []
        sections.append(self.templates.quote_section(data.get("quote", ""), data.get("icon", "")))
        sections.append(self.templates.emotions_section(data.get("emotions", [])))
        sections.append(self._vocabulary_section(vocabulary))

        story = data.get("story", {}) or {}
        sections.append(
            self.templates.story_section(
                story.get("title", ""),
                story.get("content", ""),
                story.get("emotional_peak", ""),
            )
        )

        dialogues = [
            self.templates.dialogue_row(
                character=escape(row.get("character", "")),
                emotion=escape(row.get("emotion", "")),
                german=escape(row.get("german", "")),
                russian=escape(row.get("russian", "")),
            )
            for row in data.get("dialogues", [])
            if row
        ]
        sections.append(self.templates.dialogues_section(dialogues))

        memory = data.get("memory_trick")
        if isinstance(memory, dict):
            memory_title = memory.get("title", "Пам'ятка")
            memory_content = memory.get("content") or memory.get("text") or ""
            if memory_content:
                sections.append(self.templates.memory_section(memory_title, memory_content))
        elif isinstance(memory, str):
            sections.append(self.templates.memory_section("Пам'ятка", memory))

        cheat_sheet = data.get("cheat_sheet")
        if isinstance(cheat_sheet, list):
            cheat_content = "".join(
                f"<li>{escape(str(item))}</li>" for item in cheat_sheet if item
            )
            if cheat_content:
                sections.append(self.templates.cheat_sheet_section(f"<ul>{cheat_content}</ul>"))
        elif isinstance(cheat_sheet, str):
            sections.append(self.templates.cheat_sheet_section(cheat_sheet))

        if exercises_html:
            sections.append(exercises_html)

        header = self.templates.lesson_header(
            title=escape(data.get("title", ctx.safe_id)),
            level=data.get("level", ""),
            word_count=len([item for item in vocabulary if item.get("german")]),
        )

        return self.templates.lesson_document(
            title=escape(data.get("title", ctx.safe_id)),
            level=data.get("level", ""),
            head_extra="",
            header=header,
            navigation=navigation_html,
            sections=sections,
            scripts=self.templates.scripts_block(),
        )

    def _category_index_page(self, *, title: str, lessons: Iterable[Dict[str, str]]) -> str:
        lesson_cards = [
            self.templates.category_lesson_card(
                title=escape(item["title"]),
                url=f"{item['safe_id']}.html",
                words=item.get("words", 0),
            )
            for item in lessons
        ]
        return self.templates.category_index(title=title, lessons=lesson_cards)
