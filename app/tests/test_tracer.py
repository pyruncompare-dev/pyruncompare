"""
Test modules for pyruncompare __main__
"""

import io
import tempfile


def test_recursive_module():
    """
    GIVEN a module `py` with recursive module initthe pyruncompare.__main__
    module entry point WHEN calling main
    without a valid option THEN the call executes successfully with a result
    of `None`
    """
    # Setup
    from pyruncompare.tracer import Tracer
    import pyruncompare.demo.__main__
    tmpobj = tempfile.NamedTemporaryFile()
    with io.open(tmpobj.name, 'w', encoding='utf-8') as fobj:
        tracer = Tracer(fobj)
        with tracer.run_trace():
            pyruncompare.demo.__main__.main()
