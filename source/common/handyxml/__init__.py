""" __init__.py
    Make simple XML use convenient.
    http://nedbatchelder.com/code/cog

    Copyright 2000-2007, kusung
"""

""" register all .py files """

__copyright__ = 'this file is in the public domain'

import os

(f, tail) = os.path.split(__file__)
__all__ = []

for i in os.listdir(f):
    if i.endswith('.py'):
        __all__.append(i[:-3])
__all__.remove('__init__')

del f, tail

from handyxml import *

"""
__all__ = []
for subpackage in ['A', 'B', 'C']:
    try:
 exec 'import ' + subpackage
 __all__.append( subpackage )
    except ImportError:
 pass
"""
