"""Compatibility wrapper for the modular König Lear book generator."""

from __future__ import annotations

from .book_generator_modules import BookGenerator as _ModularBookGenerator

__all__ = ["BookGenerator"]


class BookGenerator(_ModularBookGenerator):
    """Keep the public API stable for existing callers."""

    def __init__(self, config, logger):
        super().__init__(config, logger)
