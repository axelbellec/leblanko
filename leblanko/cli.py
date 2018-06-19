import argparse

from leblanko import TableFinder
from leblanko import JsonExporter, MarkdownExporter, DefaultExporter

CLI_DESCRIPTION = """
Find tables in query files.
Return a possibly-empty dict of path names that match pathname, with extracted SQL tables.
"""


def main():
    """ LeBlanko main command line interface (CLI). """
    parser = argparse.ArgumentParser(description=CLI_DESCRIPTION)
    parser.add_argument(
        "pathnames",
        type=str,
        help="",
        nargs="*"
    )
    parser.add_argument("--json", help="export to JSON", action="store_true")
    parser.add_argument("--md", help="export to Markdown", action="store_true")

    args = parser.parse_args()

    if not args.pathnames:
        parser.print_help()

    summary = TableFinder.parse_files(args.pathnames)

    if args.json:
        json_exporter = JsonExporter()
        print(json_exporter.export(summary))
    if args.md:
        md_exporter = MarkdownExporter()
        print(md_exporter.export(summary))

    if not args.json and not args.md:
        default_exporter = DefaultExporter()
        print(default_exporter.export(summary))


if __name__ == "__main__":
    main()
