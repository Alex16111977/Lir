"""CSS asset generation for the König Lear reader."""

from __future__ import annotations

from pathlib import Path


class StyleGenerator:
    """Produce stylesheet bundles for the reader and index."""

    _CSS_DIR = Path(__file__).resolve().parent / "assets" / "css"

    def _generate_styles(self) -> None:
        for name in ("book.css", "index.css", "reader.css"):
            source = self._CSS_DIR / name
            content = source.read_text(encoding="utf-8")
            target = self.output_dir / "assets" / "css" / name
            self._write_text(target, content)
