<h1 align="center">Tools for Internationalization</h1>

## ⚙️ Setup

```zsh
$ git clone https://github.com/ogty/tools-for-internationalization
$ source ./tools-for-internationalization/setup.sh # or make
```

## 📖 Usage

```
$ i18n <commands> [options]
```

## 🤖 Commands

| Command   | Description                                                             |
| --------- | ----------------------------------------------------------------------- |
| `segment` | Commands to segment translation files into their respective languages   |
| `revgene` | Command to convert a segmented translation file into a yaml file        |
| `table`   | Command to create a table from segmented translation data               |
| `help`    | Commands to display usage, etc.                                         |

## 🔍 Options

| Name                        | Argument           | Commands                |
| --------------------------- | ------------------ | ----------------------- |
| `-f, --file`                | `<file>`           | segment, revgene, table |
| `-o, --output`              | `<directory/file>` | segment, revgene, table |
| `-l, --languages`           | `<language [...]>` | segment, table          |
| `-al, --additonal_language` | `<language>`       | revgene                 |
| `-d, --directory`           | `<directory>`      | revgene                 |
| `-s, --show`                | -                  | table                   |

## ✏️ Example

**Segment the translation file into each language**

```zsh
$ i18n segment -f ./sample/public/locales/i18n.yaml -l ja en -o ./sample/public/locales
```

**Generate the original translation file (yaml) from the segmented translation file (json)**

```zsh
$ i18n revgene -d ./sample/public/locales -f translations.json -o i18n.yaml
```

**Output translation files to a file as a table**

```zsh
$ i18n table ./sample/public/locales/i18n.yaml -l ja en -o i18n.md
```

**Add new languages to the translation file and output as a table**

```zsh
$ i18n revgene -d ./sample/public/locales -f translations.json -al empty -o i18n.yaml && \
  i18n table -f ./sample/public/locales/i18n.yaml -l ja en empty
```
