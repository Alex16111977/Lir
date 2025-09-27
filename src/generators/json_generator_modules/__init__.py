"""Modular JSON generator entry point."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from .assets import AssetsWriter
from .base import JsonGeneratorBase, LessonContext
from .navigation import NavigationGenerator
from .page_builder import PageBuilder
from .templates import HTMLTemplates
from .utils import GeneratorUtils
from .vocabulary_cards import VocabularyCardsGenerator

from ..exercises_assets import ExercisesAssetsGenerator
from ..exercises_generator import ExercisesGenerator


class JsonGenerator(
    JsonGeneratorBase,
    GeneratorUtils,
    VocabularyCardsGenerator,
    NavigationGenerator,
    PageBuilder,
):
    """High level orchestrator that renders JSON lessons to HTML."""

    def __init__(self, logger) -> None:
        super().__init__(logger)
        self.templates = HTMLTemplates()
        self.assets_writer = AssetsWriter()
        self.exercises_generator = ExercisesGenerator(logger)
        self.exercises_assets = ExercisesAssetsGenerator()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def generate_from_json(self, data_dir: Path, output_dir: Path) -> bool:
        lessons_by_category = self._collect_lessons(Path(data_dir))
        if not any(lessons_by_category.values()):
            self._log("error", "[JSON] Немає даних для генерації")
            return False

        output_dir = Path(output_dir)
        self._prepare_output(output_dir)

        for category, lessons in lessons_by_category.items():
            if not lessons:
                continue
            grouped = self._group_by(lessons)
            category_dir = output_dir / category
            category_dir.mkdir(parents=True, exist_ok=True)

            lesson_cards: List[Dict[str, str]] = []
            for group_name, group_lessons in grouped.items():
                group_dir = category_dir / group_name
                group_dir.mkdir(parents=True, exist_ok=True)

                for index, ctx in enumerate(group_lessons):
                    navigation = self._navigation_html(self._build_navigation(group_lessons, index))
                    exercises = self._build_exercises(ctx)
                    html = self._build_lesson_page(ctx, navigation, exercises)
                    self._write_file(group_dir / f"{ctx.safe_id}.html", html)

                    lesson_cards.append(
                        {
                            "title": ctx.data.get("title", ctx.safe_id),
                            "safe_id": ctx.safe_id,
                            "words": len([v for v in ctx.data.get("vocabulary", []) if v.get("german")]),
                        }
                    )

            category_index = self._category_index_page(
                title=f"Категорія {category.upper()}",
                lessons=sorted(lesson_cards, key=lambda item: item["title"]),
            )
            self._write_file(category_dir / "index.html", category_index)

        main_index = self._build_main_index(lessons_by_category)
        self._write_file(output_dir / "index.html", main_index)

        self._write_assets(output_dir)
        return True

    def get_statistics(self) -> Dict[str, int]:
        return {"files_generated": self.files_generated, "words_processed": self.words_processed}

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _prepare_output(self, output_dir: Path) -> None:
        (output_dir / "css").mkdir(parents=True, exist_ok=True)
        (output_dir / "js").mkdir(parents=True, exist_ok=True)

    def _write_assets(self, output_dir: Path) -> None:
        self.assets_writer.write(output_dir, self._write_file)

        exercises_css = self.exercises_assets.generate_css()
        exercises_js = self.exercises_assets.generate_js()

        self._write_file(output_dir / "css" / "exercises.css", exercises_css)
        self._write_file(output_dir / "js" / "exercises.js", exercises_js)

    def _build_main_index(self, lessons_by_category: Dict[str, List[LessonContext]]) -> str:
        hero = self.templates.hero_block()
        cards: List[str] = []

        for category, lessons in lessons_by_category.items():
            if not lessons:
                continue
            first = lessons[0]
            description = first.data.get("category_description", f"Категорія {category.upper()}")
            cards.append(
                self.templates.category_card(
                    title=category.upper(),
                    description=description,
                    url=f"{category}/index.html",
                    count=len(lessons),
                )
            )

        return self.templates.index_page(hero=hero, categories=cards)

    def _build_exercises(self, ctx: LessonContext) -> str:
        exercises = self.exercises_generator.generate_all_exercises(ctx.data)
        return self.exercises_generator.create_exercises_section(exercises)
