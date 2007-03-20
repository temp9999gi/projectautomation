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

"""Creates a report of each Class/Table"""


#Imported System Packages.
import os
import string
import re

from pymerase.output.CppAPI.Templates import Template
from pymerase.output.CppAPI.CppUtil import CppUtil

from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociationEnds

from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning
import warnings
from warnings import warn

############################
# Globals

TRANSLATOR_NAME='CreateCppAPI'

# C++ Code Util
util = CppUtil()

def saveFile(dest, fileName, cppFile):
  if not os.path.exists(dest):
    os.mkdir(dest)

  if os.path.exists(dest) and os.path.isdir(dest):
    filePath = os.path.join(dest, fileName)
    
    f = open(filePath, 'w')
    f.write(cppFile)
    f.close()
  else:
    warn("Error %s is not a directory" % (dest), RuntimeWarning)

############################
# Writer components

def write(destination, classList):
  """
  Create Report in destination dirctory.
  """
  
  ###################################
  #Iterate through the tables/classes and process the data
  for cls in classList:
    templateUtil = Template()
    className = cls.getName(TRANSLATOR_NAME)
    headerFileName = className + '.h'
    cppFileName = className + '.cpp'

    ############################
    # HEADER FILE - PREP
    
    # Get Header Template
    cppHeader = templateUtil.getCppClassHeaderTemplate()
    cppHeader = re.sub("%CLASS_NAME%", className, cppHeader)

    # Header constructor
    constructorCode = []
    constructorCode.append("%s();" % (className))
    constructorCode.append("    %PUBLIC%")
    constructorCode = string.join(constructorCode, '\n')
    cppHeader = re.sub("%PUBLIC%", constructorCode, cppHeader)

    ############################
    # C++ FILE - PREP

    # Get C++ Template
    cppCode = templateUtil.getCppClassTemplate()
    cppCode = re.sub("%CLASS_NAME%", className, cppCode)

    # Create C++ Class Constructor
    cppCode = re.sub("%CLASS_DEF%", util.getClassConstructor(className), cppCode)
    
    # Process attributes for given class
    for attribute in getAllAttributes(classList, cls, TRANSLATOR_NAME):
      type = attribute.getType().getCppTypeStr()
      name = attribute.getName(TRANSLATOR_NAME)
      setterName = attribute.getSetterName(TRANSLATOR_NAME)
      getterName = attribute.getGetterName(TRANSLATOR_NAME)

      ############################
      # HEADER FILE - ATTRIBUTES
      
      #create c++ variables
      varCode = []
      varCode.append("%s %s;" % (type, name))
      varCode.append("    %PRIVATE%")
      varCode = string.join(varCode, '\n')
      
      cppHeader = re.sub("%PRIVATE%", varCode, cppHeader)

      #create c++ setter functions
      setterCode = []
      setterCode.append("%s %s(%s %s);" % ('void', setterName, type, name))
      setterCode.append("    %PUBLIC%")
      setterCode = string.join(setterCode, '\n')

      cppHeader = re.sub("%PUBLIC%", setterCode, cppHeader)

      #create c++ getter functions
      getterCode = []
      getterCode.append("%s %s();" % (type, getterName))
      getterCode.append("    %PUBLIC%")
      getterCode = string.join(getterCode, '\n')

      cppHeader = re.sub("%PUBLIC%", getterCode, cppHeader)

      ############################
      # C++ FILE - ATTRIBUTES
      cppCode = re.sub("%CLASS_DEF%",
                       util.getSetterFunction(className, setterName, name, type, name),
                       cppCode)

      cppCode = re.sub("%CLASS_DEF%",
                       util.getGetterFunction(className, getterName, type, name),
                       cppCode)

    # Process associations for a given class
    for assocEnd in getAllAssociationEnds(classList, cls, TRANSLATOR_NAME):
      name = assocEnd.getName(TRANSLATOR_NAME)
      setterName = assocEnd.getSetterName(TRANSLATOR_NAME)
      getterName = assocEnd.getGetterName(TRANSLATOR_NAME)
      oppClassName = assocEnd.getOppositeEnd().getClassName(TRANSLATOR_NAME)
      varName = "var%s" % (oppClassName)


      ############################
      # HEADER FILE - ASSOCIATIONS

      #If this isn't the header file of the class being used...
      if className != oppClassName:
        #include class header
        cppHeader = re.sub("%INCLUDE%",
                           "#include \"%s.h\"\n%s" % (oppClassName, "%INCLUDE%"),
                           cppHeader)


      #create c++ variables
      varCode = []
      varCode.append("%s %s;" % (oppClassName, varName))
      varCode.append("    %PRIVATE%")
      varCode = string.join(varCode, '\n')

      cppHeader = re.sub("%PRIVATE%", varCode, cppHeader)
      
      #create c++ setter functions
      setterCode = []
      setterCode.append("%s %s(%s %s);" % ('void', setterName, oppClassName, name))
      setterCode.append("    %PUBLIC%")
      setterCode = string.join(setterCode, '\n')

      cppHeader = re.sub("%PUBLIC%", setterCode, cppHeader)

      #create c++ getter functions
      getterCode = []
      getterCode.append("%s %s();" % (oppClassName, getterName))
      getterCode.append("    %PUBLIC%")
      getterCode = string.join(getterCode, '\n')

      cppHeader = re.sub("%PUBLIC%", getterCode, cppHeader)

      ############################
      # C++ FILE - ASSOCIATIONS
      cppCode = re.sub("%CLASS_DEF%",
                       util.getSetterFunction(className, setterName, name, oppClassName, varName),
                       cppCode)

      cppCode = re.sub("%CLASS_DEF%",
                       util.getGetterFunction(className, getterName, oppClassName, varName),
                       cppCode)


    ############################
    # REMOVE %TEMPLATE% TAGS

    #Header
    cppHeader = re.sub("%PUBLIC%", "", cppHeader)
    cppHeader = re.sub("%PRIVATE%", "", cppHeader)
    cppHeader = re.sub("%INCLUDE%", "", cppHeader)

    #C++ Code
    cppCode = re.sub("%CLASS_DEF%", "", cppCode)

    ############################
    # Save Class Header

    #Header
    saveFile(destination, headerFileName, cppHeader)

    #C++ Code
    saveFile(destination, cppFileName, cppCode)
    

