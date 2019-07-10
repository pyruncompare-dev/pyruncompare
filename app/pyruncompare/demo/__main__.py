"""
Module load handler for execution via python -m pyruncompare.demo

Usage:
    %(exename)s [options] [<args>...]
    %(exename)s (-h | --help)

Options:
    -h --help         Show this screen
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

import docopt


def main():
    """
    Test
    """
    args = docopt.docopt(
        __doc__ % {
            'exename': ''.join(sys.argv[:1]),
        }
    )
    print(repr(args))


if __name__ == '__main__':
    main()
