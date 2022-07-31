import json
import os
from typing import Dict, List

import yaml


class LanguageSegmenter:

    base_data = {}
    base_language = ""
    segmented_data = {}
    breadcrumb_list = []

    def __init__(self, import_file_name: str, languages: List[str], base_language: str = None) -> None:
        self.languages = languages
        LanguageSegmenter.base_language = languages[0] if base_language is None else base_language
        with open(import_file_name, "r", encoding="utf-8") as f:
            LanguageSegmenter.base_data = yaml.safe_load(f)

        [self.Processer(language) for language in self.languages]
        self.BreadcrumbListGenerator()

    def write(self, path: str) -> None:
        for language in self.languages:
            locales_path = os.path.join(path, language)
            os.makedirs(locales_path, exist_ok=True)
            with open(os.path.join(locales_path, "translations.json"), "w") as f:
                json.dump(
                    fp=f,
                    obj=LanguageSegmenter.segmented_data[language],
                    indent=4,
                    ensure_ascii=False,
                )

    def get_value(self, path: str, data: Dict[str, any], language: str) -> any:
        for key in path.split("."):
            data = data[key]
        return data[language]
    
    def output_table(self, language: str) -> None:
        # TODO
        print("<table>")
        for path in LanguageSegmenter.breadcrumb_list:
            data = self.get_value(path, LanguageSegmenter.base_data, language)
            if isinstance(data, str):
                data = f'"{data}"'
            else:
                data = json.loads(str(data).replace("'", '"'))
                data = json.dumps(data, indent=4, ensure_ascii=False)
            print(f"<tr></tr><tr>\n<td>\n\n```\n\n{path}\n\n```\n\n</td>\n<td>\n\n```js\n\n{data}\n\n```\n\n</td>\n</tr>")
        print("</table>")
    
    class Processer:

        def __init__(self, language: str):
            self.language = language
            self.result = {}

            self.segmenter(LanguageSegmenter.base_data)
            LanguageSegmenter.segmented_data[self.language] = self.result

        def segmenter(self, translation_data: Dict[str, dict]) -> Dict[str, any]:
            element = {}
            for key, value in translation_data.items():
                if self.language in value:
                    element[key] = value[self.language]
                else:
                    element[key] = self.segmenter(value)

            self.result = element
            return element

    class BreadcrumbListGenerator:

        def __init__(self) -> None:
            self.generate_breadcrumb_list(LanguageSegmenter.base_data)

        def generate_breadcrumb_list(self, data: Dict[str, dict], parent: str = None) -> None:
            for key, value in data.items():
                if LanguageSegmenter.base_language in value:
                    LanguageSegmenter.breadcrumb_list.append(f"{parent}.{key}")
                else:
                    path = key if parent is None else f"{parent}.{key}"
                    self.generate_breadcrumb_list(value, parent=path)


if __name__ == "__main__":
    segmenter = LanguageSegmenter(import_file_name="./sample.yaml", languages=["jp", "en"])
    segmenter.write("./public/locales")
    segmenter.output_table("jp") # $ python3 main.py >> README.md
