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
import linecache
import os
import runpy
import sys
import threading


class Tracer(object):
    """
    Custom Tracer to record execution
    """
    def __init__(self):
        self.fileobj = io.open('out.txt', 'w', encoding='utf-8')

    def __call__(self, frame, why, arg):  # pylint: disable=unused-argument
        """Handler for call events."""
        if why == 'call':
            filename = frame.f_globals.get('__file__', None)
            if filename:
                return self.localtrace
            else:
                return None
        return None

    def localtrace(self, frame, why, arg):  # pylint: disable=unused-argument
        """
        Records trace line by line
        """
        if why == "line":
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print(
                "%s(%d): %s" % (
                    bname, lineno,
                    linecache.getline(filename, lineno)
                ), end='',
                file=self.fileobj,
            )
        return self.localtrace

    def end(self):
        """
        Called at completion.
        """
        self.fileobj.close()


def main():
    """
    Main Command Line entry point
    """
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == '-m':
        modulename = args[1]
        log_module_run(modulename, args[2:])
    else:
        helptxt = __doc__ % {
            'exename': ''.join(sys.argv[0:1]),
        }
        print(
            'Unknown options: %r\n\n%s' % (args, helptxt), file=sys.stderr
        )
        sys.exit(1)


def log_module_run(modulename, args):
    """
    Load and run the module like python -m with log dump enabled.
    """
    oldargs = list(sys.argv)
    sys.argv = [modulename] + args
    tracer = Tracer()
    sys.settrace(tracer)
    threading.settrace(tracer)
    try:
        runpy.run_module(modulename, run_name='__main__', alter_sys=True)
    finally:
        tracer.end()
        sys.settrace(None)
        threading.settrace(None)
        sys.argv = oldargs


if __name__ == '__main__':
    main()
