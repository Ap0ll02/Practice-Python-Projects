"""
Loading A Python File.

Author: Jack Ratermann
Date: May 26, 2024
"""
import locale
import sys


def load(file):
    """
    Load a python file.

    Parameters: file
    Returns: a list from the file
    """
    try:
        with open(file, encoding=locale.getpreferredencoding()) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e_io:
        print(e_io + " Error Opening " + file, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    print("congrats\n")
