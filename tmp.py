from io import StringIO
import json
from pathlib import Path
import re


class DataSplitter:

    def __init__(self, data: any) -> None:
        self.data = data
        self.paths = []

    def splitter(self, data: any, parent: str) -> None:
        for key, value in data.items():
            path = "%s.%s" % (parent, key) if parent else key

            if isinstance(value, dict):
                self.splitter(value, path)
            else:
                self.paths.append([path, value])

    def __call__(self):
        self.splitter(self.data, '')
        return self.paths


target_directory = "./sample/public/locales/"
file_name = "translations.json"

directory_path = Path(target_directory)
translation_file_paths = list(directory_path.glob("**/%s" % file_name))


languages = []
base_paths = []
base_count = 0
path_and_element_array = []
for translation_file_path in translation_file_paths:
    language = str(translation_file_path).split('/')[-2]
    languages.append(language)

    with open(translation_file_path, 'r', encoding="utf-8") as translation_file:
        translation_data = json.load(translation_file)

    data_splitter = DataSplitter(translation_data)
    path_and_element = data_splitter()

    io = StringIO()
    for path, element in path_and_element:
        json.dump(obj=element, fp=io, indent=4, ensure_ascii=False)
        string_element = io.getvalue()
        path = "%s.%s" % (path, language)

        path_and_element_array.append((path, string_element))

        if base_count == 0:
            base_paths.append(path)

        io.truncate(0)
        io.seek(0)

    base_count += 1


language_to_replace = "fr"


# sort
base_language = languages[0]
sorted_path_and_element = []

for base_path in base_paths:
    for path, element in path_and_element_array:
        if path.split('.')[:-1] != base_path.split('.')[:-1]:
            continue
        sorted_path_and_element.append((path, element))

        if not language_to_replace:
            continue

        if base_path == path:
            splited_element = element.split('\n')
            for line in splited_element:
                match = re.search(r'"(.*)"', line)
                if match is None:
                    continue
                element = element.replace(match.group(1), '')

            path = "%s.%s" % ('.'.join(path.split('.')[:-1]), language_to_replace)
            sorted_path_and_element.append((path, element))


# reverse generation
result = ''
before = []

for string_breadcrumb_list, element_value in sorted_path_and_element:
    breadcrumb_list = string_breadcrumb_list.split('.')
    same_paths = list(set(before) & set(breadcrumb_list))
    same_path_indexes = [breadcrumb_list.index(same_path) for same_path in same_paths]

    for index, path in enumerate(breadcrumb_list):
        if index in same_path_indexes:
            continue

        string_indent = index * (' ' * 4)

        if (len(breadcrumb_list) - 1) == index:
            element_value = element_value.replace('\n', "\n%s" % string_indent)
            result += "%s%s: %s\n" % (string_indent, path, element_value)
            continue

        result += "%s%s:\n" % (string_indent, path)

    before = breadcrumb_list

print(result)
with open("reverse_generated.yaml", 'w', encoding="utf-8") as f:
    f.write(result)


"""
Usage:
    $ i18n <command> [options]

Commands:
    - segment : Segment translation file
    - revgene : Reverse generation
    - table   : Output table
    - help    : Display help message

Options:
    -l, --languages            : language [...]
    -al, --additional_language : language
    -o, --output               : directory/file
        segment: directory
        revgene: file(yaml)
        table  : file(.html/.md)

Example:
    $ i18n segment ./public/locales/i18n.yaml --languages ja en --output ./public/locales
    $ i18n revgene ./public/locales translations.json --additional_language fr --output i18n.yaml
    $ i18n table ./public/locales/i18n.yaml --languages ja en --output i18n.html # --output i18n.md

    $ i18n revgene ./public/locales translations.json -al empty -o i18n.yaml \
      i18n table ./public/locales/i18n.yaml -l ja en empty
"""
