from Cython.Build import cythonize
from distutils.core import setup
import os

if not os.path.exists('definitions.pxi'):
    os.system('make definitions.pxi')

setup(
    name='yappcap',
    version='0.0.2',
    description='A very Pythonic libpcap wrapper that aims to include as much of the API as is practical',
    author='Terry Wilson',
    url='https://github.com/otherwiseguy/yappcap',
    ext_modules=cythonize('yappcap.pyx')
)
