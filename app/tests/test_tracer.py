"""
Test modules for pyruncompare __main__
"""

import io
import json
import sys
import tempfile

import mock


def test_basic_trace():
    """
    GIVEN the tracer with a temporary file output WHEN calling run_trace
    against a mocked _gen call THEN the `_gen` method should be located in the
    output.
    """
    # Setup
    from pyruncompare.tracer import Tracer

    tmpobj = tempfile.NamedTemporaryFile()
    with io.open(tmpobj.name, "w", encoding="utf-8") as fobj:
        tracer = Tracer(fobj)
        why = "call"
        frame = mock.Mock()
        frame.f_globals = {"__file__": "test.py"}
        frame.f_locals = {}
        frame.f_code.co_name = "_gen"
        arg = mock.Mock()
        # Exercise
        tracer(frame, why, arg)
    # Verify
    found = False
    with io.open(tmpobj.name, "r", encoding="utf-8") as fobj:
        for line in fobj:
            data = json.loads(line)
            if data["funcname"] == "_gen":
                found = True
                break
    assert found  # nosec


def test_get_locals():
    """
    GIVEN a set of known primitives WHEN calling `_get_locals` THEN the expected
    representation of the locals should be returned.
    """
    # Setup
    from pyruncompare.tracer import _get_locals

    frame = mock.Mock()
    frame.f_locals = {
        "string": "string",
        "bigstring": "a" * 4096,
        "bytes": u"string".encode("utf-16"),
        "bigbytes": ("a" * 4096).encode("utf-16"),
        "int": 0,
        "float": 0.5,
        "boolean": True,
        "obj": frame,
    }
    # Execute
    result = _get_locals(frame)
    # Verify
    if sys.version_info[0] >= 3:
        expect_bigbytes = "<large byte sequence>"
    else:
        expect_bigbytes = repr("%s..." % (("a" * 4096).encode("utf-16")[:117],))
    expect = {
        "string": repr("string"),
        "bigstring": repr("%s..." % ("a" * 117,)),
        "bytes": repr("string".encode("utf-16")),
        "bigbytes": expect_bigbytes,
        "int": "0",
        "float": "0.5",
        "boolean": "True",
        "obj": "<no-repr>",
    }
    assert result == expect
