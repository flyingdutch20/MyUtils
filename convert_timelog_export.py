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

#    out = text.replace(',', '.')


    bsObj = BeautifulSoup(text, features='html.parser')
    table = bsObj.find("table")
    rows = table.findAll("tr")

    splitname = (args.filename).rsplit('.', 1)
    csvFile = open(splitname[0] + '.csv', 'w', newline='')
    writer = csv.writer(csvFile)

    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(["td", "th"]):
                csvRow.append(cell.get_text().replace(',', '.'))
            writer.writerow(csvRow)
    finally:
        csvFile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
