from setuptools import setup
import os
import codecs

NAME = 'metex'
VERSION_FILE = 'VERSION'
INSTALL_REQUIRES = ['numpy>=1.7', 'matplotlib']

here = os.path.abspath(os.path.dirname(__file__))

# get current version
with open(os.path.join(here, NAME, VERSION_FILE)) as version_file:
    VERSION = version_file.read().strip()

# get long description from README
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup (name=NAME,
       version=VERSION,
       url="https://gitlab.com/epiasini/metex",
       description="Maximum Entropy Textures",
       long_description=LONG_DESCRIPTION,
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
