#!/usr/bin/env python3
"""Convert commas into full stops and create csv"""

import argparse
import os
import string
import csv
from bs4 import BeautifulSoup


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert commas into full stops and create csv',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('filename',
                        metavar='filename',
                        help='Input filename')

    args = parser.parse_args()

    if not os.path.isfile(args.filename):
        parser.error((f'File "{args.filename}" not found'))

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    text = open(args.filename).read().rstrip()

    bsObj = BeautifulSoup(text, features='html.parser')
    lines = bsObj.findAll("a")

    splitname = (args.filename).rsplit('.', 1)
    outfile = open(splitname[0] + '.txt', 'w', newline='')

    out_lines = []

    for line in lines:
        chapter = line.get_text().strip()
        if len(chapter) > 1:
            out_lines.append(chapter + '\n')
    outfile.writelines(out_lines)
    outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
