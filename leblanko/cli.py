import argparse

from leblanko import SQLParser


def main():
    parser = argparse.ArgumentParser(description="Find tables in query files.")
    parser.add_argument(
        "pathname",
        type=str,
        help="Return a possibly-empty dict of path names that match pathname, with extracted SQL tables.",
    )

    args = parser.parse_args()

    parsed = SQLParser.inspect(args.pathname)

    for filepath, tables in parsed.items():
        print("--- {:>15}\n\t{}".format(filepath, tables))


if __name__ == "__main__":
    main()
