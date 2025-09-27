"""JavaScript asset generation for the König Lear reader."""

from __future__ import annotations

from pathlib import Path


class ScriptGenerator:
    """Emit JavaScript bundles from template files."""

    _JS_DIR = Path(__file__).resolve().parent / "assets" / "js"

    def _generate_javascript(self) -> None:
        mapping = {
            "reader.js": self.output_dir / "assets" / "js" / "reader.js",
            "navigation.js": self.output_dir / "assets" / "js" / "navigation.js",
            "book-index.js": self.output_dir / "assets" / "js" / "book-index.js",
        }

        for filename, target in mapping.items():
            content = (self._JS_DIR / filename).read_text(encoding="utf-8")
            self._write_text(target, content)
