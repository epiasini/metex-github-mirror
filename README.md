# metex

Utilities for generating **m**aximum **e**ntropy **tex**tures,
according to [Victor and Conte 2012](https://doi.org/10.1364/JOSAA.29.001313).

## Requirements

* Python 3
* numpy
* matplotlib

## Installation

```bash
cd /home/username/src
git clone https://gitlab.com/epiasini/metex.git
cd metex
pip install .
```

This should install the `metex` package on your `PYTHONPATH` and
should also install a script called `metex` to your regular `PATH`.

## Usage (command line)

Generate one sample of a fully random, square 10x10 texture, which
will be saved to the current folder as '0.png':
```bash
metex 10
```

Save 10 samples of a 100x150 texture in folder named 'fig', with
parameter 'alpha' set to -0.6. Name each sample 'fig_[n].jpg', where
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
>>> texture = metex.Texture(height=15, width=25, theta2=0.7)
>>> sample = texture.sample()
>>> print(sample)
⬛⬜⬜⬜⬛⬛⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜⬛
⬜⬛⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬜⬜
⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬜⬜⬛⬛⬜⬛⬜⬜⬛⬜⬛⬜
⬛⬜⬜⬛⬛⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜
⬜⬛⬜⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬛⬜⬜⬛⬜⬛⬛⬜⬛⬛⬛⬜
⬛⬜⬜⬛⬜⬛⬜⬛⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛
⬛⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬛⬜⬛⬜⬛
⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛⬜⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬛⬜⬛⬛⬜⬛⬜⬛⬜⬜⬜⬛⬛⬛⬛⬜⬛⬜⬛⬛⬛⬛⬛⬜
⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬛⬜⬛⬜⬛⬜⬜⬛⬜⬛⬛⬛⬜⬜⬛
⬛⬛⬜⬜⬛⬛⬛⬛⬜⬛⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜⬛
⬛⬜⬛⬜⬛⬛⬛⬜⬛⬜⬛⬛⬛⬛⬜⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜
⬛⬛⬛⬜⬛⬜⬛⬛⬛⬜⬛⬛⬜⬛⬜⬜⬛⬛⬛⬛⬜⬛⬛⬜⬛
⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬛⬜⬜⬜⬛⬜⬛⬛⬛⬛⬜⬛⬜⬜⬛
```
(the exact rendering of the texture will depend on your terminal)
