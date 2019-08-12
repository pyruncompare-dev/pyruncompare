"""
Module load handler for execution via python -m pyruncompare.demo
"""
from __future__ import absolute_import, division, print_function, unicode_literals


def main():
    """
    Test
    """
    somevar = "Done"
    print(_gen(somevar))


def _gen(somearg):
    """
    Simple test call
    """
    return "{0}.".format(somearg)


if __name__ == "__main__":
    main()
