import json
import os
from typing import Dict, List

import yaml


class LanguageSegmenter:
    """Segment translation files by language

    Variables:
        base_data (dict): Base translation data
        base_language (str): Base language
        segmented_data (dict): Segmented translation data
        breadcrumb_list (list): Breadcrumb list
    """

    base_data = {}

    base_language = ""

    segmented_data = {}

    breadcrumb_list = []

    def __init__(self, import_file_name: str, languages: List[str], base_language: str = None) -> None:
        """Initialization handles file loading and segmenting

        Args:
            import_file_name (str): Used to read yaml file
            languages (List[str]): Selection of the language described in the yaml file
            base_language (str, optional): Most reliable language. Defaults to None.
        """
        self.languages = languages
        LanguageSegmenter.base_language = languages[0] if base_language is None else base_language
        with open(import_file_name, "r", encoding="utf-8") as f:
            LanguageSegmenter.base_data = yaml.safe_load(f)

        [self.Processer(language) for language in self.languages]
        self.BreadcrumbListGenerator()

    def write(self, path: str) -> None:
        """Output internationalization-compliant files.

        Args:
            path (str): Path to the location to be created
        """
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
        """Function to get data from a string connected by dots

        Args:
            path (str): Paths connected by dots
            data (Dict[str, any]): Data traced by the path
            language (str): Languages to be retrieved from data

        Returns:
            any: It is the type of data for the translation.
        """
        for key in path.split("."):
            data = data[key]
        return data[language]
    
    def output_table(self, languages: List[str]) -> None:
        """Outputs a translation table

        Args:
            languages (List[str]): Selecting the language of output
        """
        print("<table>")
        print('<tr align="center">\n<td>Path</td>\n<td>', end="")
        print("</td>\n<td>".join(list(map(lambda language: language.upper(), languages))), end="")
        print("</td>\n</tr><tr></tr>")
        for path in LanguageSegmenter.breadcrumb_list:
            print(f"<tr></tr><tr>\n<td>\n\n```\n{path}\n```\n\n</td>\n")
            for language in languages:
                data = self.get_value(path, LanguageSegmenter.base_data, language)
                if isinstance(data, str):
                    data = f'"{data}"'
                else:
                    data = json.loads(str(data).replace("'", '"'))
                    data = json.dumps(data, indent=2, ensure_ascii=False)
                print(f"<td>\n\n```js\n{data}\n```\n\n</td>")
            print("\n</tr>")
        print("</table>")

    class Processer:
        """
        Class containing recursive functions for language-specific segmenting
        """

        def __init__(self, language: str):
            """Executed at initialization. Result reflects class variables of parent class.

            Args:
                language (str): Specify a single language
            """
            self.language = language
            self.result = {}

            self.segmenter(LanguageSegmenter.base_data)
            LanguageSegmenter.segmented_data[self.language] = self.result

        def segmenter(self, translation_data: Dict[str, any]) -> Dict[str, any]:
            """Recursive functions for segmenting translation data

            Args:
                translation_data (Dict[str, any]): key, value in value data

            Returns:
                Dict[str, any]: Elements of translation data
            """
            element = {}
            for key, value in translation_data.items():
                if self.language in value:
                    element[key] = value[self.language]
                else:
                    element[key] = self.segmenter(value)

            self.result = element
            return element

    class BreadcrumbListGenerator:
        """
        Class containing recursive functions for breadcrumb list creation
        """

        def __init__(self) -> None:
            """_summary_
            """
            self.generate_breadcrumb_list(LanguageSegmenter.base_data)

        def generate_breadcrumb_list(self, data: Dict[str, any], parent: str = None) -> None:
            """Create breadcrumb list at initialization

            Args:
                data (Dict[str, any]): key, value in value data
                parent (str, optional): Route information up to now. Defaults to None.
            """
            for key, value in data.items():
                if LanguageSegmenter.base_language in value:
                    LanguageSegmenter.breadcrumb_list.append(f"{parent}.{key}")
                else:
                    path = key if parent is None else f"{parent}.{key}"
                    self.generate_breadcrumb_list(value, parent=path)


if __name__ == "__main__":
    languages = ["jp", "en"]
    segmenter = LanguageSegmenter(import_file_name="./sample.yaml", languages=languages)
    segmenter.write("./public/locales")
    segmenter.output_table(languages) # $ python3 main.py >> README.md
