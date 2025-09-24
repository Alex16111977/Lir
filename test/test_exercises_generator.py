import json
import random
from pathlib import Path
import unittest

from src.generators.exercises_generator import ExercisesGenerator


class ExercisesGeneratorTestCase(unittest.TestCase):
    """Validate HTML snippets created for lessons."""

    def setUp(self) -> None:
        random.seed(0)
        lesson_path = Path('data/a2/01_Отец_и_дочери_A2.json')
        self.lesson_data = json.loads(lesson_path.read_text(encoding='utf-8'))
        self.generator = ExercisesGenerator()

    def test_generate_all_exercises_returns_html_blocks(self) -> None:
        bundle = self.generator.generate_all_exercises(self.lesson_data)
        self.assertEqual(set(bundle.keys()), {
            'word_matching',
            'articles',
            'synonyms',
            'quiz',
            'context',
            'builder',
        })

        section = self.generator.create_exercises_section(bundle)
        self.assertIn('exercises-section', section)
        for block_id in ('word-matching', 'articles', 'synonyms', 'quiz', 'context', 'builder'):
            with self.subTest(block_id=block_id):
                self.assertIn(block_id, section)

        # Individual HTML blocks should not be empty strings
        for name, html in bundle.items():
            with self.subTest(name=name):
                self.assertTrue(html.strip())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
