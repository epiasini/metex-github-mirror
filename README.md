# Metex - Maximum Entropy TEXtures
[![License](https://img.shields.io/pypi/l/metex)](https://www.gnu.org/licenses/gpl-3.0.txt)
[![PyPI version](https://img.shields.io/pypi/v/metex.svg)](https://pypi.python.org/pypi/metex/)
[![Build status](https://img.shields.io/gitlab/pipeline/epiasini/metex)](https://gitlab.com/epiasini/metex/pipelines)

Utilities for generating **m**aximum **e**ntropy **tex**tures,
according to [Victor and Conte
2012](https://doi.org/10.1364/JOSAA.29.001313).

Metex can be used as a standalone software from the command line, or
as a Python package to generate and manipulate textures.

## Requirements

* Python 3
* numpy ≥ 1.7
* matplotlib

## Installation
To install the latest release, run:

```bash
pip install metex
```
(depending on your system, you may need to use `pip3` instead of `pip`
in the command above).

This should install the `metex` package on your `PYTHONPATH`, as well
as an executable script called `metex` to your regular `PATH`.

### Testing
(requires `setuptools`). If `metex` is already installed on your
system, look for the copy of the `test_library.py` and
`test_cli_interface.sh` scripts installed alongside the rest of the
`metex` files and execute it. For example:

``` bash
python /usr/lib/python3.X/site-packages/metex/test/test_library.py
/bin/bash /usr/lib/python3.X/site-packages/metex/test/test_cli_interface.sh
```

## Usage (command line)

Generate one sample of a fully random, square 10x10 texture, which
will be saved to the current folder as '0.png':
```bash
metex 10
```

Save 10 samples of a 100x150 texture in folder named 'fig', with
parameter 'alpha' set to -0.6. Name each sample 'fig_[n].png', where
[n] takes on values 0,...,9:

```bash
metex --folder=fig --prefix=fig_ --n_samples=10 --alpha=-0.6 100 150
```

For more information on the command line parameters,
```bash
metex --help
```
(also see `metex/core.py`).

## Usage (library)

The library implements a `Texture` class that represents the maximum
entropy distribution of textures with a given level of a statistic and
a given size. Objects of class `Texture` can be sampled, generating
objects of class `TextureSample`. This is a subclass of
`numpy.ndarray` with support for array-like manipulation, image
generation for use in experiments (via matplotlib) and terminal-based
pretty-printing (for messing around).

```
>>> import metex
>>> texture = metex.Texture(height=15, width=25, beta1=0.7)
>>> sample = texture.sample()
>>> print(sample)

⬛⬛⬛⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬜⬛⬛⬜⬜
⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
>>> print(sample[:5,:])

⬛⬛⬛⬛⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
>>> print(sample[:,:5])

⬛⬛⬛⬛⬛
⬜⬛⬛⬛⬛
⬜⬜⬜⬜⬛
⬛⬜⬛⬜⬜
⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜
⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜
⬛⬜⬜⬛⬛
⬜⬜⬛⬜⬜
⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬛
```
The exact rendering of the texture will depend on your terminal.


## Changelog
See the [CHANGELOG.md](CHANGELOG.md) file for a list of changes from
older versions.

## Authors
`metex` is maintained by Eugenio Piasini.
