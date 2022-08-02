from typing import List
import unittest


def process(test_data: List[List[str]]) -> str:
    result = ""
    before = []
    for string_breadcrumb_list, element_value in test_data:
        breadcrumb_list = string_breadcrumb_list.split(".")
        breadcrumb_list_length = len(breadcrumb_list)
        same_paths = list(set(before) & set(breadcrumb_list))
        same_path_indexes = [breadcrumb_list.index(same_path) for same_path in same_paths]

        for index, path in enumerate(breadcrumb_list):
            if not index in same_path_indexes:
                string_indent = index * "  "
                if (breadcrumb_list_length - 1) == index:
                    result += "%s%s: %s\n" % (string_indent, path, element_value)
                else:
                    result += "%s%s:\n" % (string_indent, path)

        before = breadcrumb_list

    return result


class TestReverseGeneration(unittest.TestCase):

    def test_pattern_1(self) -> None:
        test_data = [
            ["a.b", '"DATA1"'],
            ["a.b.c", '"DATA2"'],
            ["a.b.c.d.e", '"DATA3"'],
        ]
        objective_results = """a:
  b: \"DATA1\"
    c: \"DATA2\"
      d:
        e: \"DATA3\"
"""
        self.assertEqual(process(test_data), objective_results)

    def test_pattern_2(self) -> None:
        test_data = [
            ["header.title.ja", "タイトル"],
            ["header.title.en", "Title"],
            ["header.items.ja", "[\n      \"ログイン\"\n    ]"],
            ["header.items.en", "[\n      \"Log in\"\n    ]"],
        ]
        objective_results = """header:
  title:
    ja: タイトル
    en: Title
  items:
    ja: [
      \"ログイン\"
    ]
    en: [
      \"Log in\"
    ]
"""
        self.assertEqual(process(test_data), objective_results)
