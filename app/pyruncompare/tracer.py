"""
Support for running python traces
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# System Imports
import contextlib
import json
import runpy
import sys
import threading

# External Imports
import six


class Tracer(object):
    """
    Custom Tracer to record execution
    """
    def __init__(self, fileobj):
        self.fileobj = fileobj

    @contextlib.contextmanager
    def run_trace(self):
        """
        Context Manager for tracing
        """
        sys.settrace(self)  # noqa: DUO111
        threading.settrace(self)
        yield self
        sys.settrace(None)  # noqa: DUO111
        threading.settrace(None)

    def __call__(self, frame, why, arg):  # pylint: disable=unused-argument
        """Handler for call events."""
        if why == 'call':
            filename = frame.f_globals.get('__file__', None)
            if filename and not self.fileobj.closed:
                print(
                    six.u(json.dumps({
                        'filename': filename,
                        'funcname': frame.f_code.co_name,
                        'locals': _get_locals(frame),
                    })),
                    file=self.fileobj,
                )


def _get_locals(frame):
    """
    Json compatible locals
    """
    return {key: _safe_repr(val) for key, val in frame.f_locals.items()}


def _safe_repr(val):
    """
    Handle repr issues
    """
    try:
        primitive = not hasattr(val, '__dict__')
    except ValueError:
        primitive = False
    if primitive:
        if isinstance(val, type('')):
            if len(val) > 120:
                val = val[:117] + '...'
            return repr(val)
        if isinstance(val, type(b'')):
            if len(val) > 120:
                return '<large byte sequence>'
            return repr(val)
        oktype = isinstance(val, int)
        oktype = oktype or isinstance(val, float)
        oktype = oktype or isinstance(val, bool)
        if oktype:
            return repr(val)
    return '<no-repr>'


def log_module_run(tracer, modulename, args):
    """
    Load and run the module like python -m with log dump enabled.
    """
    oldargs = list(sys.argv)
    sys.argv = [modulename] + args
    try:
        with tracer.run_trace():
            runpy.run_module(modulename, run_name='__main__', alter_sys=True)
    finally:
        sys.argv = oldargs
