"""Modular implementation of the König Lear book generator."""

from __future__ import annotations

import fitz

from .base import BookGeneratorBase
from .chapters import ChapterProcessor
from .html_pages import HtmlPageBuilder
from .metadata import MetadataGenerator
from .scripts import ScriptGenerator
from .styles import StyleGenerator

__all__ = ["BookGenerator"]


class BookGenerator(
    BookGeneratorBase,
    ChapterProcessor,
    HtmlPageBuilder,
    StyleGenerator,
    ScriptGenerator,
    MetadataGenerator,
):
    """Compose mixins into the public generator."""

    def generate(self) -> bool:
        try:
            self._log_info("Starting book generation from PDF...")

            if not self.pdf_path.exists():
                self._log_error(f"PDF file not found: {self.pdf_path}")
                return False

            self._create_directories()

            doc = fitz.open(str(self.pdf_path))
            self._log_info(f"Opened PDF: {doc.page_count} pages")

            self.metadata = self._extract_metadata(doc)
            self.chapters = self._split_into_chapters(doc)
            self._log_info(f"Split into {len(self.chapters)} chapters")

            self._generate_html_pages()
            self._generate_index_page()
            self._generate_styles()
            self._generate_javascript()
            self._generate_toc()
            self._generate_search_index()

            doc.close()
            self._log_info(
                f"Book generation completed! Generated {len(self.chapters)} chapters"
            )
            return True
        except Exception as exc:  # pragma: no cover - orchestration path
            self._log_error(f"Error generating book: {exc}")
            return False
