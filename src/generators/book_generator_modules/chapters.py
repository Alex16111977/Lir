"""Chapter extraction and processing helpers."""

from __future__ import annotations

import re
from typing import List

import fitz
from bs4 import BeautifulSoup


class ChapterProcessor:
    """Handle PDF splitting and chapter extraction."""

    def _split_into_chapters(self, doc) -> List[dict]:
        chapters = []
        current_chapter = None

        chapter_patterns = [
            r"^\s*(AUFZUG|AKT|SZENE)\s+[IVX]+",
            r"^\s*(Erster|Zweiter|Dritter|Vierter|Fünfter)\s+(Aufzug|Akt)",
            r"^\s*(Erste|Zweite|Dritte|Vierte|Fünfte)\s+Szene",
            r"^\s*\d+\.\s+(AKT|AUFZUG)",
        ]

        page_buffer: List[int] = []
        chapter_num = 0

        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text()

            is_new_chapter = False
            chapter_title = None

            for pattern in chapter_patterns:
                match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
                if match:
                    is_new_chapter = True
                    chapter_title = match.group(0).strip()
                    break

            if is_new_chapter or page_num == 0:
                if page_buffer:
                    chapter_num += 1
                    chapters.append(
                        self._create_chapter(doc, page_buffer, chapter_num, current_chapter)
                    )

                current_chapter = chapter_title or f"Глава {chapter_num + 1}"
                page_buffer = [page_num]
            else:
                page_buffer.append(page_num)

        if page_buffer:
            chapter_num += 1
            chapters.append(self._create_chapter(doc, page_buffer, chapter_num, current_chapter))

        if len(chapters) < 3:
            return self._split_by_pages(doc)

        return chapters

    def _create_chapter(self, doc, page_numbers, chapter_num, title):
        chapter = {
            "number": chapter_num,
            "title": title or f"Глава {chapter_num}",
            "pages": page_numbers,
            "content": "",
            "text_content": "",
            "images": [],
        }

        for page_num in page_numbers:
            page = doc[page_num]

            html_content = page.get_text("html")
            chapter["content"] += self._process_page_html(html_content, page_num)
            chapter["text_content"] += page.get_text()

            images = self._extract_images(page, page_num)
            chapter["images"].extend(images)

        return chapter

    def _split_by_pages(self, doc, pages_per_chapter: int = 10):
        chapters = []
        total_pages = doc.page_count

        for start_page in range(0, total_pages, pages_per_chapter):
            end_page = min(start_page + pages_per_chapter, total_pages)
            page_buffer = list(range(start_page, end_page))

            chapter_num = (start_page // pages_per_chapter) + 1
            chapters.append(
                self._create_chapter(
                    doc,
                    page_buffer,
                    chapter_num,
                    f"Teil {chapter_num}",
                )
            )

        return chapters

    def _process_page_html(self, html: str, page_num: int) -> str:
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup.find_all(["style", "script"]):
            tag.decompose()

        for paragraph in soup.find_all("p"):
            paragraph["class"] = "book-paragraph"

        for span in soup.find_all("span"):
            style = span.get("style", "")
            if "bold" in style or "font-weight" in style:
                span["class"] = "text-bold"
            if "italic" in style:
                span["class"] = "text-italic"

        page_marker = soup.new_tag(
            "div",
            **{"class": "page-marker", "data-page": str(page_num + 1)},
        )
        page_marker.string = f"Seite {page_num + 1}"
        soup.insert(0, page_marker)

        return str(soup)

    def _extract_images(self, page, page_num: int):
        images = []
        image_list = page.get_images()

        for img_index, img in enumerate(image_list):
            try:
                xref = img[0]
                pix = fitz.Pixmap(page.parent, xref)

                img_path = self.output_dir / "assets" / "images" / f"page_{page_num}_img_{img_index}.png"

                if pix.n - pix.alpha < 4:
                    pix.save(str(img_path))
                else:
                    pix_converted = fitz.Pixmap(fitz.csRGB, pix)
                    pix_converted.save(str(img_path))
                    pix_converted = None

                images.append(
                    {
                        "path": f"../assets/images/page_{page_num}_img_{img_index}.png",
                        "page": page_num,
                        "index": img_index,
                    }
                )
                pix = None
            except Exception as exc:  # pragma: no cover - logging path
                self._log_warning(
                    f"Could not extract image {img_index} from page {page_num}: {exc}"
                )

        return images
