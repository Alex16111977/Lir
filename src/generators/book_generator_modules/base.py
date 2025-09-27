"""Base utilities for the modular book generator."""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Iterable, List


class BookGeneratorBase:
    """Provide shared helpers for book generation."""

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

        base_dir = Path(getattr(config, "base_dir", Path.cwd()))
        output_dir = Path(getattr(config, "output_dir", Path.cwd() / "output"))

        self.pdf_path = base_dir / "book" / "Konig Lear.pdf"
        self.output_dir = output_dir / "book"
        self.chapters = []
        self.metadata = {}

    # ------------------------------------------------------------------
    # Logging helpers
    def _log_info(self, message: str) -> None:
        if self.logger:
            self.logger.info(message)
        else:
            print(message)

    def _log_error(self, message: str) -> None:
        if self.logger:
            self.logger.error(message)
        else:
            print(f"ERROR: {message}")

    def _log_warning(self, message: str) -> None:
        if self.logger:
            self.logger.warning(message)
        else:
            print(f"WARNING: {message}")

    # ------------------------------------------------------------------
    # Filesystem helpers
    def _create_directories(self) -> None:
        dirs = [
            self.output_dir,
            self.output_dir / "chapters",
            self.output_dir / "assets" / "css",
            self.output_dir / "assets" / "js",
            self.output_dir / "assets" / "images",
            self.output_dir / "metadata",
        ]

        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)

    def _write_text(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)

    def _write_json(self, path: Path, payload: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)

    # ------------------------------------------------------------------
    # Metadata helpers
    def _extract_metadata(self, doc) -> dict:
        metadata = {
            "title": "König Lear",
            "author": "William Shakespeare",
            "pages": doc.page_count,
            "language": "de",
            "generated": datetime.now().isoformat(),
            "toc": [],
        }

        try:
            toc = doc.get_toc()
            for item in toc:
                metadata["toc"].append(
                    {
                        "level": item[0],
                        "title": item[1],
                        "page": item[2] - 1,
                    }
                )
        except Exception:
            self._log_warning("Could not extract TOC from PDF")

        doc_meta = doc.metadata
        if doc_meta:
            metadata["pdf_title"] = doc_meta.get("title", "")
            metadata["pdf_author"] = doc_meta.get("author", "")
            metadata["pdf_subject"] = doc_meta.get("subject", "")
            metadata["pdf_keywords"] = doc_meta.get("keywords", "")

        return metadata

    # ------------------------------------------------------------------
    # Search helpers
    def _split_text_into_chunks(self, text: str, chunk_size: int) -> List[str]:
        words = text.split()
        chunks: List[str] = []

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i : i + chunk_size])
            if chunk.strip():
                chunks.append(chunk)

        return chunks

    @staticmethod
    def _iter_pairs(items: Iterable) -> Iterable:
        iterator = iter(items)
        return zip(iterator, iterator)
