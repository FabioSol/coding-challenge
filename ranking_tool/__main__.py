"""
Command-line interface for the ranking tool.

Usage:
    python -m ranking_tool rank path/to/input.txt

This script parses match results from a file and prints the calculated rankings.
"""

import argparse
import os

from ranking_tool.core import League

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ranking-tool',
                                     description='Ranking tool written in Python')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    rank_parser = subparsers.add_parser('rank', help='calculates the rank of the given input')
    rank_parser.add_argument("file_path", type=str, help="Path to the file to be ranked")

    args = parser.parse_args()
    match args.command:
        case 'rank':
            if not os.path.exists(args.file_path):
                parser.error(f"File not found: {args.file_path}")
            with open(args.file_path, 'r', newline=None) as f:
                data = f.read()

            try:
                league = League.from_string(data)
                print(league)
            except Exception as e:
                parser.error(str(e))

        case _:
            parser.print_help()
