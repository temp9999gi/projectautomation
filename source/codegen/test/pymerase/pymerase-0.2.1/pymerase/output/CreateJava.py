###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2001 by:                                                 #
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
#       Authors: $Author: kusung25 $
# Last Modified: $Date: 2006/12/18 15:54:02 $
"""Creates Java API"""

from __future__ import nested_scopes


import os
import sys
import string
import re
import types
import shutil
from pymerase.util.Template import Template
from pymerase.util.output import *
from pymerase.util.SortMetaInfo import forwardDeclarationSort
from pymerase.util.Template import Template
from pymerase.output.dbAPI import fkeyTypes

import warnings
from pymerase.util.Warnings import DebugWarning
from warnings import warn



############################
# helper files
def getMITCopyright():
  return """
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) %4s by:                                                 #
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
""" % (str(2003))

TRANSLATOR_NAME='CreateJava'
SQL_TRANSLATOR_NAME='CreateSQL'

class JavaTemplate(Template):
  def __init__(self, classMetaInfo, TranslatorName):
    Template.__init__(self)
    self.classMetaInfo = classMetaInfo
    self.TranslatorName = TranslatorName
    
  def ClassName(self):
    return self.classMetaInfo.getName(self.TranslatorName)

  def ExtendsClause(self):
    if not self.classMetaInfo.isRootClass():
      baseClasses = self.classMetaInfo.getBaseClassNames(self.TranslatorName)
      return "extends " + string.join(baseClasses, ", ")
    else:
      return ""

  def writeDebugPrint(self, indent):
    c =[]
    c +=['/**']
    c +=[' * Prints a string represenation of this class to aid in debugging']
    c +=[' */']
    c +=['public void debugPrint()']
    c +=['{']
    c +=['  System.out.println("class %(ClassName())s");' % (self)]
    c +=['  debugDumpAttributes();']
    c +=['  System.out.println();']
    c +=['}']
    c +=['']
    c +=['']
    c +=['protected void debugDumpAttributes()']
    c +=['{']
    if not self.classMetaInfo.isRootClass():
      c +=['  super.debugDumpAttributes();']
    else:
      c +=['  System.out.println("  _id: " + _id);']

    for attribute in self.classMetaInfo.getAttributes():
      name = attribute.getName(self.TranslatorName)
      c +=['  System.out.println(" '+name+': " +'+ name + ');']
    c += ['}']
    return string.join(addIndentToStrings(indent, c), os.linesep)
    
#######################################
# Output Translater Interface
def writeClass(destination, classMetaInfo):
  """Generate the java classes.
  """
  c = []
  c += ['/** ']
  c += [' * Create a new %(ClassName())s']
  c += [' *']
  c += [' * All collections will be initialized (as empty).']
  c += [' */']
  c += ['']
  c += ['public %(ClassName())s %(ExtendsClause())s']
  c += ['{']
  c += ['  #writeNoArgCtor']
  if len(classMetaInfo.getAttributes()) > 0:
    c += ['  #writeArgCtor']
  c +=['']
  c +=['  /**']
  c +=['   * Getter / Setter Pairs']
  c +=['   */']
  c +=['']
  c +=['']
  c +=['  /**']
  c +=['   * Collection adder/removers']
  c +=['   */']
  c +=['']
  c +=['']
  c +=['  /**']
  c +=['   * Debugging']
  c +=['   */']
  c +=['%(writeDebugPrint(2))s']
  c +=['']
  c +=['  /**']
  c +=['   * Attributes']
  c +=['   */ ']
  #for attribute in classMetaInfo.getAttributes():
  #  c += ['   %()']
  c +=['']
  c +=['  /**']
  c +=['   * Extra attributes to hold the primary key of the different object']
  c +=['   * references.']
  c +=['   */']
  c +=['']
  c +=['']
  c +=['  /**']
  c +=['   * Extra Object Relational Bridge (OJB) attributes for mapping back']
  c +=['   * to classses which have a 1:N relation with this specific class.']
  c +=['   */']
  c +=['']
  c +=['']
  c +=['  /**']
  c +=['   * Primary Key in database']
  c +=['   */ ']
  #c +=['   protected int _id;']
  c +=['};']

  template_engine = JavaTemplate(classMetaInfo, None)
  
  template = string.join(c, os.linesep)
  destination_filename = os.path.join(destination,
                                      template_engine.ClassName()+".java")
  template_engine.writeFile(template, destination_filename)
  return

  c += ['/**']
  c += [' * Create a new %(ClassName)s with all fields initialized.']
  c += [' */']
  c += ['%(DefaultConstructor)s']
  c += ['']
  

def write(destination, parsedInput):
  # Write out all the individual package members

  if not os.path.exists(destination):
    os.mkdir(destination)
  elif not os.path.isdir(destination):
    msg = 'PATH(%s) is not a directory!' % (destination)
    raise ValueError(msg)

  package_information = []
  for class_info in parsedInput:
    try:
      package_information.append(writeClass(destination, class_info))
    except NotImplementedError, e:
      warn('Skipping %s' % ( t.getName() ), DebugWarning)

