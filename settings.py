EXPORT_FILE_NAME = "translations.json"
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
