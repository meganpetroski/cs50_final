#!/usr/bin/env python3

from argparse import ArgumentParser
from helpers import lines


def main():

    # Parse command-line arguments
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--lines", action="store_true", help="compare lines")
    parser.add_argument("FILE1", help="file to compare")
    parser.add_argument("FILE2", help="file to compare")
    args = vars(parser.parse_args())

    # Read files
    try:
        with open(args["FILE1"], "r") as file:
            file1 = file.read()
    except IOError:
        sys.exit(f"Could not read {args['FILE1']}")
    try:
        with open(args["FILE2"], "r") as file:
            file2 = file.read()
    except IOError:
        sys.exit(f"Could not read {args['FILE2']}")

    # Compare files
    if args["lines"]:
        matches = lines(file1, file2)

    # Output sorted matches
    for match in sorted(matches, key=len, reverse=True):
        print(match)


def positive(string):
    """Convert string to a positive integer."""
    value = int(string)
    if value <= 0:
        raise argparse.ArgumentTypeError()
    return value


if __name__ == "__main__":
    main()
