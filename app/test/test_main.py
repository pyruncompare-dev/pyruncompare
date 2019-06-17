"""
Test modules for pyruncompare __main__
"""


def test_main_bad_arg():
    """
    GIVEN the pyruncompare.__main__ module entry point WHEN calling main
    without a valid option THEN the call executes successfully with a result
    of `None`
    """
    # Setup
    from pyruncompare.__main__ import main
    from unittest import mock
    fake_docopt = mock.patch(
        'pyruncompare.__main__.docopt', return_value={}
    )
    with fake_docopt:
        # Exercise
        result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result is None


def test_main():
    """
    GIVEN the pyruncompare.__main__ module entry point WHEN calling main with
    the arguments -m demo THEN the call executes successfully with a result of
    `None`
    """
    # Setup
    from pyruncompare.__main__ import main
    from unittest import mock
    fake_docopt = mock.patch(
        'pyruncompare.__main__.docopt', return_value={
            '-m': 'pyruncompare.demo'
        }
    )
    with fake_docopt:
        # Exercise
        result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result is None
