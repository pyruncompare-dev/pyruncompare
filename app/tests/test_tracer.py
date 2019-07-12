"""
Test modules for pyruncompare __main__
"""

import io
import json
import tempfile


def test_basic_trace():
    """
    GIVEN the tracer with a temporary file output WHEN calling run_trace
    against the demo module THEN the `_gen` method should be located in the
    output.
    """
    # Setup
    from pyruncompare.tracer import Tracer
    import pyruncompare.demo.__main__
    tmpobj = tempfile.NamedTemporaryFile()
    with io.open(tmpobj.name, 'w', encoding='utf-8') as fobj:
        tracer = Tracer(fobj)
        # Exercise
        with tracer.run_trace():
            pyruncompare.demo.__main__.main()
    # Verify
    found = False
    with io.open(tmpobj.name, 'r', encoding='utf-8') as fobj:
        for line in fobj:
            data = json.loads(line)
            if data['funcname'] == '_gen':
                found = True
                break
    assert found  # nosec
