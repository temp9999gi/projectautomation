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

TRANSLATOR_NAME = "iPymerase"

def printClasses(classList):
  """
  Given a list of classes, prints out class name and list index of class.
  """
  counter = 0
  for cls in classList:
    print "classList[%s] = %s" % (counter, cls.getName(TRANSLATOR_NAME))
    counter += 1


def printAttributes(attribList):
  """
  Given a list of attributes, prints out attribute name and the
  index of the attribute in the list.
  """
  counter = 0
  for attrib in attribList:
    print "attribList[%s] = %s" % (counter, attrib.getName(TRANSLATOR_NAME))
    counter += 1


def printAssociations(assocList):
  """
  Given a list of associations, prints out association name
  and the index of the association in the list.
  """
  counter = 0
  for assoc in assocList:
    print "assocList[%s] = %s" % (counter, assoc.getName(TRANSLATOR_NAME))
    counter += 1


def getClassByName(classList, className, translator=TRANSLATOR_NAME):
  """
  Given a list of classes and a className
  returns class matching className
    or
  returns None
  """
  for cls in classList:
    if cls.getName(translator) == className:
      return cls

  return None


def getAttribByName(attribList, attribName, translator=TRANSLATOR_NAME):
  """
  Given a list of attributes and an attribute name
  returns attrib with name matching attribName
    or
  returns None
  """
  for attrib in attribList:
    if attrib.getName(translator) == attribName:
      return attrib

  return None


def getAssocByName(assocList, assocName, translator=TRANSLATOR_NAME):
  """
  Given a list of associations and an association name
  returns association with name matching assocName
    or
  returns None
  """
  for assoc in assocList:
    if assoc.getName(translator) == assocName:
      return assoc

  return None


