from setuptools import setup
import os
import codecs

NAME = 'metex'
INSTALL_REQUIRES = ['numpy>=1.7', 'matplotlib']

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r', encoding="utf-8") as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup (name=NAME,
       version=get_version(os.path.join(NAME, "__init__.py")),
       url="https://gitlab.com/epiasini/metex",
       description="Maximum Entropy Textures",
       long_description=read("README.md"),
       long_description_content_type="text/markdown",
       install_requires=INSTALL_REQUIRES,
       python_requires=">=3",
       author="Eugenio Piasini",
       author_email="eugenio.piasini@gmail.com",
       license="GPLv3+",
       classifiers=[
           "Development Status :: 4 - Beta",
           "Intended Audience :: Science/Research",
           "Topic :: Scientific/Engineering",
           "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
           "Programming Language :: Python :: 3",
           "Operating System :: OS Independent",
           "Environment :: Console"           
       ],
       packages=["metex",
                 "metex.test"],
       scripts=["scripts/metex"],
       test_suite="metex.test",
       include_package_data=True)
