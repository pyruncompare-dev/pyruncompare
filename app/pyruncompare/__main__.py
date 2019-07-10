"""\
Module load handler for execution via python -m pyruncompare.

Usage:
    %(exename)s [options] [<args>...]
    %(exename)s (-h | --help)

Options:
    -h --help         Show this screen
    -m <module>       Import and run specified module like python -m
    -f <file>         Output Log File [default: out.txt]
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# System Imports
import io
import sys

import docopt

from .tracer import Tracer, log_module_run


def main():
    """
    Main Command Line entry point
    """
    args = docopt.docopt(
        __doc__ % {
            'exename': ''.join(sys.argv[0:1]),
        }
    )
    if args.get('-m'):
        print(repr(args))
        modulename = args['-m']
        outfile = args['-f']
        with io.open(outfile, 'w', encoding='utf-8') as fobj:
            tracer = Tracer(fobj)
            trace_args = args['<args>']
            if trace_args[:1] == ['--']:
                del trace_args[:1]
            log_module_run(tracer, modulename, trace_args)
    else:
        helptxt = __doc__ % {
            'exename': ''.join(sys.argv[0:1]),
        }
        print(
            'Unknown options: %s\n\n%s' % (
                ' '.join(sys.argv[1:]),
                helptxt,
            ),
            file=sys.stderr
        )
        sys.exit(1)


if __name__ == '__main__':
    main()
