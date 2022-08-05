<h1 align="center">Tools for Internationalization</h1>

## 🎈 機能

- ✅ 翻訳ファイルをそれぞれの言語に分割
- ✅ 分割した翻訳ファイルを元のファイルに戻す
- ✅ 追加言語の自動翻訳

## ⚙️ セットアップ

```zsh
$ git clone https://github.com/ogty/tools-for-internationalization
$ source ./tools-for-internationalization/setup.sh # or make
```

## 📖 使い方

```
$ i18n <commands> [options]
```

## 🤖 コマンド

| コマンド   | 説明                                              |
| --------- | ------------------------------------------------ |
| `segment` | 翻訳ファイルを各言語に分割するコマンド                 |
| `revgene` | 分割された翻訳ファイルを yaml ファイルに変換するコマンド |
| `table`   | 分割された翻訳データから表を作成するコマンド            |
| `help`    | 使い方などを表示するコマンド                          |

## 🔍 オプション

| Name                           | Argument           | Commands                |
| ------------------------------ | ------------------ | ----------------------- |
| `-f, --file`                   | `<file>`           | segment, revgene, table |
| `-o, --output`                 | `<directory/file>` | segment, revgene, table |
| `-l, --languages`              | `<language [...]>` | segment, table          |
| `-al, --additonal_language`    | `<language>`       | revgene                 |
| `-d, --directory`              | `<directory>`      | revgene                 |
| `-at, --automatic_translation` | -                  | revgene                 |
| `-s, --show`                   | -                  | table                   |

## ✏️ 例

**翻訳ファイルを各言語に分割する**

```zsh
$ i18n segment -f ./sample/public/locales/i18n.yaml -l ja en -o ./sample/public/locales
```

**分割された翻訳ファイル(json)から元の翻訳ファイル(yaml)を生成する**

```zsh
$ i18n revgene -d ./sample/public/locales -f translations.json -o i18n.yaml
```

**翻訳ファイルを表としてファイルに出力する**

```zsh
$ i18n table -f ./sample/public/locales/i18n.yaml -l ja en -o i18n.md
```

**翻訳ファイルに新しい言語を追加し、表として出力する**

```zsh
$ i18n revgene -d ./sample/public/locales -f translations.json -al fr -o i18n.yaml && \
  i18n table -f ./sample/public/locales/i18n.yaml -l ja en fr
```
