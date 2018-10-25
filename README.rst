metex
=====

Utilities for generating **m**\ aximum **e**\ ntropy **tex**\ tures,
according to `Victor and Conte 2012
<https://doi.org/10.1364/JOSAA.29.001313>`.

Requirements
------------
 - Python 3
 - numpy
 - matplotlib

Installation
------------

.. code-block:: bash
   cd /home/username/src
   git clone git@gitlab.com:epiasini/metex.git
   cd metex
   python3 setup.py install --user

This should install the `metex` package on your `PYTHONPATH` and
should also install a script called `metex` to your regular `PATH`.

Usage
-----

Save 10 samples of a 100x150 texture in folder named 'fig', with
parameter 'alpha' set to -0.6. Name each sample 'fig_[n].jpg', where
[n] takes on values 0,...,9:

.. code-block:: bash
   metex --folder=fig --prefix=fig_ --n_samples=10 --alpha=-0.6 100 150


Documentation
-------------

.. code-block:: bash
   metex --help

(also see `core/metex.py`).
