import argparse

EXPORT_FILE_NAME = "translations.json"
EMPTY_DATA_NAME = "EMPTY"
TABLE_TEMPLATE = "<table><tr><td>Path</td><td>---</td></tr><tr></tr>---</table>"
HELP_MESSAGE = """
Usage:
    ./i18nseg [OPTIONS]

Options:
    -f, --file FILE
                    Path to the translation file
    -l, --languages LANGUAGE ...
                    Languages to be segmented
    -b, --base_language LANGUAGE
                    Most reliable language
    -o, --output DIRECTORY
                    Path to the output directory
    -t, --table
                    Output translation table
    -n, --file_name FILE
                    Output file name
    -h, --help
                    Show this help message and exit
"""

parser = argparse.ArgumentParser(description="Segment translation files by language")
parser.add_argument("--file",          "-f", type=str, help="Path to the translation file")
parser.add_argument("--output",        "-o", type=str, help="Path to the output directory")
parser.add_argument("--file_name",     "-n", type=str, help="Output file name")
parser.add_argument("--base_language", "-b", type=str, help="Most reliable language")
parser.add_argument("--languages",     "-l", type=str, nargs="+", help="Languages to be segmented")
parser.add_argument("--reverse",       "-r", action="store_true", help="Reverse translation")
parser.add_argument("--table",         "-t", action="store_true", help="Output translation table")
parser.add_argument("--empty",         "-e", action="store_true", help="Output empty translation")
