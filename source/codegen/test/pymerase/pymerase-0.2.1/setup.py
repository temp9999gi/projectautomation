#!/usr/bin/env python
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2002 by:                                                 #
#    * California Institute of Technology                                 #
#                                                                         #
#    All Rights Reserved.                                                 #
#                                                                         #
# Permission is hereby granted, free of charge, to any person             #
# obtaining a copy of this software and associated documentation files    #
# (the "Software"), to deal in the Software without restriction,          #
# including without limitation the rights to use, copy, modify, merge,    #
# publish, distribute, sublicense, and/or sell copies of the Software,    #
# and to permit persons to whom the Software is furnished to do so,       #
# subject to the following conditions:                                    #
#                                                                         #
# The above copyright notice and this permission notice shall be          #
# included in all copies or substantial portions of the Software.         #
#                                                                         #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,         #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF      #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                   #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS     #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN      #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN       #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE        #
# SOFTWARE.                                                               #
###########################################################################
#
#       Authors: Brandon King
# Last Modified: $Date: 2006/12/18 15:54:02 $
#

from distutils.core import setup
from distutils.core import Extension
import glob
import os
import re
import string
import shutil
import sys

from ParseCVS import CvsTreeUtil

def createPackageConfig(dtdFile):
  if not dtdFile[0:5] in ('file:', 'http:'):
    dtdFile = 'file:' + dtdFile
  configFile = open('pymerase/config.py', 'r')
  configLines = configFile.readlines()
  configFile.close()

  newConfig = []
  for l in configLines:
    if re.match('table_dtd=',l):
      newConfig.append(re.sub('^table_dtd=.*', 'table_dtd="%s"' % (dtdFile), l))
    else:
      newConfig.append(l)

  print string.join(newConfig, '')
  savePackageConfig(newConfig)
  return configLines

def savePackageConfig(configLines):
  """save the contents of the pyermase.config file
  """
  configFile = open('pymerase/config.py', 'w')
  configFile.write(string.join(configLines, ''))
  configFile.close()

  
util = CvsTreeUtil()


########################################
# Setup Configuration
PACKAGES=["pymerase",
          "pymerase.input",
          "pymerase.util",
          "pymerase.output",
          "pymerase.output.dbAPI",
#          "pymerase.output.webUtil",
#          "pymerase.output.webUtil.templates",
#          "pymerase.output.PyTkWidgets",
#          "pymerase.output.PyTkWidgets.lib",
#          "pymerase.output.PythonAPI",
          "pymerase.output.CppAPI",
          "smw",
          "smw.metamodel",
          "smw.repository"]



########################################
# Process Commandline Args

#list of items to remove from sys.argv when done
rmList = []

#set prefix to None for later error checking
binPath = None
docPath = None
dtdFile = None

#look for custom command line args
for item in sys.argv:
  #If prefix command line arg exists, set new prefix and mark
  # item to be removed from sys.argv
  if item[:10] == '--binPath=':
    binPath = item[10:]
    rmList.append(item)

  if item[:10] == '--docPath=':
    docPath = item[10:]
    rmList.append(item)

  if item[:10] == '--dtdFile=':
    dtdFile = item[10:]
    rmList.append(item)

#Remove processed items from sys.argv
for item in rmList:
  sys.argv.remove(item)

print sys.argv
#If user overrides command line args, then don't need to
# use logic to figure them out.
##BIN PATH##
if binPath is None:
  #Set default for linux 2.x systems
  if sys.platform == 'linux2':
    binPath = '/usr/bin'
  #set default for all others
  #FIXME: should add more defaults
  #NOTE: can override with command line
  elif sys.platform == 'win32':
    binPath = '..\\Program Files\\Pymerase\\bin'
  else:
    binPath = 'pymerase'
    

##DOC PATH##
if docPath is None:
  #Set default for linux 2.x systems
  if sys.platform == 'linux2':
    docPath = '/usr/share/doc/pymerase'
  #set default for all others
  #FIXME: should add more defaults
  #NOTE: can override with command line
  elif sys.platform == 'win32':
    docPath = '..\\Program Files\\Pymerase\\docs'
  else:
    docPath = 'pymerase'

if dtdFile is None:
  if sys.platform == 'win32':
    dtdFile = '..\\Program Files\\Pymerase\\sgml\\dtd\\table.dtd'
  else:
    dtdFile = '/usr/share/sgml/dtd/table.dtd'
  
    
#################################
# Setup Data Files
BIN_TUPLE=(binPath,
       ['bin/pymerase', 'bin/pymerasegui.py'])

README_TUPLE=(docPath, ['README', 'INSTALL'])

DTD_TUPLE=(dtdFile, ['examples/table.dtd'])

# ignore this until someone fixes it.
#WEBUTIL_TEMPLATES_TUPLE=(os.path.join(prefix, 'templates/webUtil'),
#       glob.glob("pymerase/output/webUtil/templates/*.html"))

DATA_FILES=[BIN_TUPLE,
            README_TUPLE,
            DTD_TUPLE,
#            WEBUTIL_TEMPLATES_TUPLE
            ]

#util (CvsTreeUtil) will setup all files checked into cvs
#  for the examples directory...
DATA_FILES.extend(util.getSetupDataFiles(docPath, 'examples'))
#FIXME: Grabs .cvsignore files, need to add filter

oldConfig = createPackageConfig(dtdFile)

#Run setup! =o)
setup(name="Pymerase",
      version="0.2.1",
      description="Pymerase is a tool intended to generate a python " \
      "object model, relational database, and an object-relational " \
      "model connecting the two.",
      author="Diane Trout",
      author_email="diane@caltech.edu",
      url="http://pymerase.sf.net/",
      packages=PACKAGES,
      data_files=DATA_FILES)

savePackageConfig(oldConfig)
