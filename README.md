# pyruncompare

[![Azure Status](https://dev.azure.com/timgates/timgates/_apis/build/status/pyruncompare-dev.pyruncompare?branchName=master)](https://dev.azure.com/timgates/timgates/_build/latest?definitionId=5&branchName=master)
[![Travis Status](https://travis-ci.org/pyruncompare-dev/pyruncompare.svg?branch=master)](https://travis-ci.org/pyruncompare-dev/pyruncompare)
[![Appveyor Status](https://ci.appveyor.com/api/projects/status/h9552855me50ha76/branch/master?svg=true)](https://ci.appveyor.com/project/timgates42/pyruncompare)
[![PyPI version](https://img.shields.io/pypi/v/pyruncompare.svg)](https://pypi.org/project/pyruncompare)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyruncompare.svg)](https://pypi.org/project/pyruncompare)
[![PyPI downloads per month](https://img.shields.io/pypi/dm/pyruncompare.svg)](https://pypi.org/project/pyruncompare)
[![Documentation Status](https://readthedocs.org/projects/pyruncompare/badge/?version=latest)](https://pyruncompare.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/pyruncompare-dev/pyruncompare/badge.svg)](https://coveralls.io/github/pyruncompare-dev/pyruncompare/)
[![Black](https://camo.githubusercontent.com/28a51fe3a2c05048d8ca8ecd039d6b1619037326/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667)](https://github.com/psf/black)

Execute a python module or function and log all calls and locals to formats that can be compared for execution variations.

This allows programatic inspection looking for common mistakes in the variables, the specific example that inspired this project was looking for python 2to3 issues to do with python byte strings being handled incorrectly. By logging all primitive typed local variables, these could be scanned for the appearance of "b'...." or 'b"....' that signified a string representation of a byte sequence.

# Execution

pyruncompare supports a nested module runner system to inject itself into tracing, e.g.

```
python -m pyruncompare -m cookiecutter
```

Can be used to trace an execution of the cookiecutter __main__ module execution.

More details can be found in the
[Online Documentation.](https://pyruncompare.readthedocs.io/en/latest/)

# Installation

You can install pyruncompare for
[Python](https://www.python.org/) via
[pip](https://pypi.org/project/pip/)
from [PyPI](https://pypi.org/).

```
$ pip install pyruncompare
```




## Prerequisites:
- docopt
- six


## Download from PyPI.org

https://pypi.org/project/pyruncompare/



# Contributing

Contributions are very welcome, consider using the
[file an issue](https://github.com/pyruncompare-dev/pyruncompare/issues)
to discuss the work before beginning, but if you already have a Pull Request
ready then this is no problem, please submit it and it will be very gratefully
considered. The [Contribution Guidelines](CONTRIBUTING.md)
outlines the pyruncompare commitment to ensuring all
contributions receive appropriate recognition.

# License


Distributed under the terms of the [GPLv3](https://opensource.org/licenses/GPL-3.0)
license, "pyruncompare" is free and open source software


# Issues

If you encounter any problems, please
[file an issue](https://github.com/pyruncompare-dev/pyruncompare/issues)
along with a detailed description.

# Additional Documentation:

* [Online Documentation](https://pyruncompare.readthedocs.io/en/latest/)
* [News](NEWS.rst).
* [Template Updates](COOKIECUTTER_UPDATES.md).
* [Code of Conduct](CODE_OF_CONDUCT.md).
* [Contribution Guidelines](CONTRIBUTING.md).
