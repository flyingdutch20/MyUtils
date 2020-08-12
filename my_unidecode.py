import unidecode

def convert(text):
    return unidecode.unidecode(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys
    convert(sys.stdin)
