"""
Support for running python traces
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import contextlib
# System Imports
import json
import runpy
import sys
import threading


class Tracer(object):
    """
    Custom Tracer to record execution
    """
    def __init__(self, fileobj):
        self.fileobj = fileobj

    def __call__(self, frame, why, arg):  # pylint: disable=unused-argument
        """Handler for call events."""
        if why == 'call':
            filename = frame.f_globals.get('__file__', None)
            if filename and not self.fileobj.closed:
                print(
                    json.dumps({
                        'filename': filename,
                        'funcname': frame.f_code.co_name,
                    }),
                    file=self.fileobj,
                )
        return None


@contextlib.contextmanager
def run_trace(tracer):
    """
    Context Manager for tracing
    """
    sys.settrace(tracer)
    threading.settrace(tracer)
    yield tracer
    sys.settrace(None)
    threading.settrace(None)


def log_module_run(tracer, modulename, args):
    """
    Load and run the module like python -m with log dump enabled.
    """
    oldargs = list(sys.argv)
    sys.argv = [modulename] + args
    try:
        with run_trace(tracer):
            runpy.run_module(modulename, run_name='__main__', alter_sys=True)
    finally:
        sys.argv = oldargs
