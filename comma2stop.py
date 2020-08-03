#!/usr/bin/env python3
"""Convert commas into full stops"""

import argparse
import os
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert commas into full stops',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    if os.path.isfile(args.text):
        text = open(args.text).read().rstrip()

    #TODO extract data out of HTML using BeautifulSoup

    out = text.replace(',', '.')

    #TODO generate csv file for output

    splitname = (args.text).rsplit('.', 1)
    outname = splitname[0] + '-converted.' + splitname[1]
    outfile = open(outname, 'w')
    outfile.write(out)
    outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
