"""
Module load handler for execution via python -m pyruncompare.

Usage:
    %(exename)s [options] [<args>...]
    %(exename)s (-h | --help)

Options:
    -h --help         Show this screen
    -m <module>       Import and run specified module like python -m
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# System Imports
import io
import sys

from .tracer import Tracer, log_module_run


def main():
    """
    Main Command Line entry point
    """
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == '-m':
        modulename = args[1]
        with io.open('out.txt', 'w', encoding='utf-8') as fobj:
            tracer = Tracer(fobj)
            log_module_run(tracer, modulename, args[2:])
    else:
        helptxt = __doc__ % {
            'exename': ''.join(sys.argv[0:1]),
        }
        print(
            'Unknown options: %r\n\n%s' % (args, helptxt), file=sys.stderr
        )
        sys.exit(1)
