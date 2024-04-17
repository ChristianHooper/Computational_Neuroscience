from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('SynaptogenesisCy.pyx'))

# Compile File: python setup.py build_ext --inplace

# --inplace Same directroy
# build_ext Builds extension
