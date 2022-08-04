import unittest


class TestFileMatch(unittest.TestCase):

    def test_file_match(self) -> None:
        with open("./sample/public/locales/i18n.yaml", 'r', encoding="utf-8") as f:
            original_translation_file = f.read()

        with open("./sample/public/locales/_i18n.yaml", 'r', encoding="utf-8") as f:
            reverse_generated_file = f.read()

        self.assertEqual(original_translation_file, reverse_generated_file)
