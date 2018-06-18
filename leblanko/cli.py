import argparse

from leblanko import TableFinder


def main():
    """ LeBlanko main command line interface (CLI). """
    parser = argparse.ArgumentParser(description="Find tables in query files.")
    parser.add_argument(
        "pathnames",
        type=str,
        help="Return a possibly-empty dict of path names that match pathname, with extracted SQL tables.",
        nargs="*",
    )

    args = parser.parse_args()

    parsed = TableFinder.parse_files(args.pathnames)

    for filepath, tables in parsed.items():
        print("--- {:>15}\n\t{}".format(filepath, tables))


if __name__ == "__main__":
    main()
