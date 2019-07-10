"""
Test modules for pyruncompare __main__
"""

import sys


def test_main_bad_arg():
    """
    GIVEN the pyruncompare.__main__ module entry point WHEN calling main
    without a valid option THEN the call executes successfully with a result
    of `None`
    """
    # Setup
    from pyruncompare.__main__ import main
    import pytest
    oldargv = sys.argv
    sys.argv = []
    try:
        with pytest.raises(SystemExit) as excctxt:
            # Exercise
            main()  # pylint: disable=assignment-from-no-return
    finally:
        sys.argv = oldargv
    # Verify
    assert excctxt.value.args[0] == 1  # nosec


def test_main():
    """
    GIVEN the pyruncompare.__main__ module entry point WHEN calling main with
    the arguments -m demo THEN the call executes successfully with a result of
    `None`
    """
    # Setup
    from pyruncompare.__main__ import main
    oldargv = sys.argv
    sys.argv = [sys.argv[0], '-m', 'pyruncompare.demo']
    try:
        # Exercise
        result = main()  # pylint: disable=assignment-from-no-return
    finally:
        sys.argv = oldargv
    # Verify
    assert result is None  # nosec
