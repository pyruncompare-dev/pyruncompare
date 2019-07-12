"""
Test modules for pyruncompare __main__
"""

# External Imports
import pytest


def test_main_bad_arg():
    """
    GIVEN the pyruncompare.__main__ module entry point WHEN calling main
    without a valid option THEN the call executes successfully with a result
    of `None`
    """
    # Setup
    from pyruncompare.__main__ import main
    import mock
    fake_docopt = mock.patch(
        'pyruncompare.__main__.docopt', return_value={
        }
    )
    with fake_docopt, pytest.raises(SystemExit) as excctxt:
        # Exercise
        main()
    # Verify
    assert excctxt.value.args[0] == 1  # nosec


@pytest.mark.parametrize('filename,expected', [
    ('out.txt', None),
    ('-', None),
])
def test_main(filename, expected):
    """
    GIVEN the pyruncompare.__main__ module entry point WHEN calling main with
    the arguments -m demo THEN the call executes successfully with a result of
    `None`
    """
    # Setup
    from pyruncompare.__main__ import main
    import mock
    fake_docopt = mock.patch(
        'pyruncompare.__main__.docopt', return_value={
            '-f': filename,
            '-m': 'pyruncompare.demo',
            '<args>': ['--'],
        }
    )
    with fake_docopt:
        # Exercise
        result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result == expected  # nosec
