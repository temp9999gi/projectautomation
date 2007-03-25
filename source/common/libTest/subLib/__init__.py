""" HandyXml
    Make simple XML use convenient.
    http://nedbatchelder.com/code/cog

    Copyright 2004-2005, Ned Batchelder.
"""

# $Id: __init__.py 110 2005-08-27 22:35:20Z ned $

#from pyExcel import *

##import os
##plugindir = os.path.split(__file__)[0]
##for f in os.listdir(plugindir):
##    f = os.path.split(f)[-1]
##    if f.endswith('.py'):
##        f = f.split('.')[0]
##    try:
##        exec('import %s'%f)
##    except: pass

# gozerbot package
#
#

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

