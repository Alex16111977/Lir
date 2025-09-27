"""JSON generator wrapper that exposes the modular implementation."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

from .json_generator_modules import JsonGenerator as ModularJsonGenerator


class JSONGenerator(ModularJsonGenerator):
    """Backward compatible wrapper used by the orchestrator."""

    def __init__(self, logger):
        super().__init__(logger)

    def generate(self, data_dir: Path, output_dir: Path) -> bool:
        return self.generate_from_json(data_dir, output_dir)

    # Convenience alias for older code paths
    def get_stats(self) -> Dict[str, int]:
        return self.get_statistics()


__all__ = ["JSONGenerator"]
