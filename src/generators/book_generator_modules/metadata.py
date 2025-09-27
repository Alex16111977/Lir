"""Metadata helpers for the König Lear reader."""

from __future__ import annotations

from datetime import datetime


class MetadataGenerator:
    """Produce TOC and search index payloads."""

    def _generate_toc(self) -> None:
        toc_data = {
            "title": "König Lear",
            "author": "William Shakespeare",
            "chapters": [],
        }

        for index, chapter in enumerate(self.chapters):
            toc_data["chapters"].append(
                {
                    "number": index + 1,
                    "title": chapter["title"],
                    "file": f"chapters/chapter-{index + 1:02d}.html",
                    "pages": {
                        "start": chapter["pages"][0] + 1,
                        "end": chapter["pages"][-1] + 1,
                        "count": len(chapter["pages"]),
                    },
                }
            )

        self._write_json(self.output_dir / "metadata" / "toc.json", toc_data)

    def _generate_search_index(self) -> None:
        search_index = {
            "version": "1.0",
            "generated": datetime.now().isoformat(),
            "documents": [],
        }

        for index, chapter in enumerate(self.chapters):
            text_chunks = self._split_text_into_chunks(chapter["text_content"], 500)

            for chunk_index, chunk in enumerate(text_chunks):
                search_index["documents"].append(
                    {
                        "id": f"chapter-{index + 1}-chunk-{chunk_index + 1}",
                        "chapter": index + 1,
                        "chapter_title": chapter["title"],
                        "chunk": chunk_index + 1,
                        "content": chunk,
                        "url": f"chapters/chapter-{index + 1:02d}.html",
                    }
                )

        self._write_json(self.output_dir / "metadata" / "search-index.json", search_index)
