import unittest

from src.generators.exercises_assets import ExercisesAssetsGenerator


class ExercisesAssetsGeneratorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = ExercisesAssetsGenerator()

    def test_generate_css_contains_core_classes(self) -> None:
        css = self.generator.generate_css()
        self.assertIn('.exercises-section', css)
        self.assertIn('.synonym-item', css)
        self.assertIn('.drop-zone', css)

    def test_generate_js_defines_handlers(self) -> None:
        js_code = self.generator.generate_js()
        for function_name in (
            'checkMatching',
            'checkArticles',
            'checkSynonyms',
            'checkQuiz',
            'checkContext',
            'checkBuilder',
        ):
            with self.subTest(function=function_name):
                self.assertIn(function_name, js_code)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
