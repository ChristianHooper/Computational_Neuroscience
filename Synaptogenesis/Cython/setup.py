
from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize(["voxel_class.pyx", "voxel_render.pyx"], 
                          compiler_directives={'language_level': "3"}),
    include_dirs=[numpy.get_include()]
)
# Compile File: python setup.py build_ext --inplace

# --inplace Same directroy
# build_ext Builds extension
