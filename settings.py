import argparse
from typing import TypedDict


INDENT = 4
PARSER = argparse.ArgumentParser(description="Segment translation files by language")
COMMAND_NAME = "i18nseg"
CHARACTER_CODE = "utf-8"
TABLE_TEMPLATE = "<table><tr><td>Path</td><td>---</td></tr><tr></tr>---</table>"
EMPTY_DATA_NAME = "EMPTY"
EXPORT_FILE_NAME = "translations.json"

argument_type = TypedDict("argument_type", {
    "long": str,
    "short": str,
    "help": str,
    "argument_name": str,
    "type": str or None,
    "action": str or None,
    "nargs": str or None,
})

arguments = [
    argument_type(
        long="--file",
        short="-f",
        help="Path to the translation file",
        type=str,
        argument_name="<FILE>",
    ),
    argument_type(
        long="--output",
        short="-o",
        help="Path to the output directory",
        type=str,
        argument_name="<DIRECTORY>",
    ),
    argument_type(
        long="--file_name",
        short="-n",
        help="Output file name",
        type=str,
        argument_name="<FILE>",
    ),
    argument_type(
        long="--base_language",
        short="-b",
        help="Most reliable language",
        type=str,
        argument_name="<LANGUAGE>",
    ),
    argument_type(
        long="--languages",
        short="-l",
        help="Languages to be segmented",
        type=str,
        nargs="+",
        argument_name="<LANGUAGE [...]>",
    ),
    argument_type(
        long="--reverse",
        short="-r",
        help="Reverse translation",
        action="store_true",
        argument_name="",
    ),
    argument_type(
        long="--table",
        short="-t",
        help="Output translation table",
        action="store_true",
        argument_name="",
    ),
    argument_type(
        long="--empty",
        short="-e",
        help="Output empty translation",
        action="store_true",
        argument_name="",
    )
]

USAGE = f"Usage:\n\t{COMMAND_NAME} [OPTIONS]\n"
OPTIONS = "\nOptions:\n"
for argument in arguments:
    long = argument["long"]
    short = argument["short"]
    OPTIONS += "\t%s, %s %s\n\t\t\t\t\t%s\n" % (
        short, long, argument["argument_name"], argument["help"]
    )

    argument.pop("long")
    argument.pop("short")
    argument.pop("argument_name")

    PARSER.add_argument(long, short, **argument)

HELP_MESSAGE = USAGE + OPTIONS
