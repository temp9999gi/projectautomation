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
#       Authors: Diane Trout
# Last Modified: $Date: 2006/12/18 15:54:02 $
#
""" The purpose of this module is to store type information.

In this case a superset of python and SQL type information, and to
provide the textual representation of the code needed to instantiate
those objects.

types to support:
  bool
  datetime
  float
  int4
  name?
  serial (int4 with special sql handling)
  text (postgres extention)
  varchar(128)
"""
import re

def isVarchar(type):
    """
    Checks to see if is of type varchar
    """
    match = re.search('varchar', type)
    match2 = re.search('character varying', type)
    if match != None or match2 != None:
        return 1
    else:
        return 0

def isChar(type):
    """
    Checks to see if is of type varchar
    """
    match1 = re.search('varchar', type)
    match2 = re.search('char', type)
    if match1 == None and match2 != None:
        return 1
    else:
        return 0

def getVarcharLen(type):
    """
    Returns the length of the varchar(###)
    """
    left = re.search('\(', type)
    right = re.search('\)', type)
    #Capture length value stored in varchar(###)
    maxlength = type[left.end():right.start()]
    return maxlength

NativeTypes = {'python': ('serial', 'String', 'Date', 'float', 'double', 'int.*')}
               
        
class PymeraseType:
  def __init__(self, type_string):
    if type_string is None:
      raise ValueError("bad type")
    self.type_string = type_string

  def getTypeString(self):
    """Return type string without any processing
    """
    return self.type_string

  def getSQLType(self):
    varchar_match = re.match("varchar[\[(]([0-9]*)[\])]", self.type_string)
    char_match = re.match("char[a-z]*[\[(]([0-9]*)[\])]", self.type_string)
    if varchar_match is not None:
      return "character varying(%s)" % varchar_match.group(1)
    elif char_match is not None:
      return "character(%s)" % char_match.group(1)
    elif re.match("datetime", self.type_string):
      return "timestamp with time zone"
    elif re.match("bool", self.type_string):
      return "boolean"
    elif re.match("int.*", self.type_string):
      return "integer"
    elif re.match("float.*", self.type_string):
      return "double precision"
    elif re.match("double.*", self.type_string):
      return "double precision"
    elif re.match("text", self.type_string):
      return "text"
    elif re.match("serial", self.type_string):
      return "serial"
    elif re.match("name", self.type_string):
      return "name"
    # added to handlge XMI java string class
    elif re.match("[Ss]tring", self.type_string):
      return "text"
    elif re.match("Date", self.type_string) or re.match("Time", self.type_string):
      return "timestamp with time zone"
    elif re.match("char", self.type_string):
      return "character(1)"
    else:
      raise NotImplementedError("Type %s is unknown" % self.type_string)
    
  def getPythonTypeStr(self):
    if re.match("serial", self.type_string):
      return "types.IntType"
    elif re.match(".*char.*", self.type_string):
      return "types.StringType"
    elif re.match("text", self.type_string):
      return "types.StringType"
    elif re.match("name", self.type_string):
      return "types.StringType"
    # FIXME: Should I be breaking this into Int and Long
    elif re.match("int.*", self.type_string):
      return "types.IntType"
    elif re.match("float", self.type_string):
      return "types.FloatType"
    elif re.match("double.*", self.type_string):
      return "types.FloatType"
    elif re.match("bool", self.type_string):
      # FIXME: should there be a better way of representing this in python?
      return "Bool"
      # return "types.IntType"
    elif re.match("datetime", self.type_string):
      return "mx.DateTime.mxDateTime.DateTimeType"
    # added to handlge XMI java string class
    elif re.match("[Ss]tring", self.type_string):
      return "types.StringType"
    elif re.match("Date", self.type_string) or re.match("Time", self.type_string):
      return "mx.DateTime.mxDateTime.DateTimeType"
    elif re.match("char", self.type_string):
      return "character(1)"
    else:
      return "None"

  def getJavaTypeStr(self):
    if re.match("serial", self.type_string):
      return "int"
    elif re.match(".*char.*", self.type_string):
      return "String"
    elif re.match("text", self.type_string):
      return "String"
    elif re.match("name", self.type_string):
      return "String"
    elif re.match("int.*", self.type_string):
      return "int"
    elif re.match("float", self.type_string):
      return "float"
    elif re.match("double.*", self.type_string):
      return "double"
    elif re.match("bool", self.type_string):
      return "boolean"
    elif re.match("datetime", self.type_string):
      return "Date"
      # added to handle XMI java string class
    elif re.match("[Ss]tring", self.type_string):
      return "String"
    elif re.match("Date", self.type_string) or re.match("Time", self.type_string):
      return "Date"
    elif re.match("char", self.type_string):
      return "char"
    else:
      return "None"

  def getCppTypeStr(self):
    if re.match("serial", self.type_string):
      return "unsigned long"
    elif re.match(".*char.*", self.type_string):
      return "string"
    elif re.match("text", self.type_string):
      return "string"
    elif re.match("name", self.type_string):
      return "string"
    # FIXME: Should this be a long or int?
    elif re.match("int.*", self.type_string):
      return "int"
    elif re.match("float", self.type_string):
      return "float"
    elif re.match("double.*", self.type_string):
      return "double"
    elif re.match("bool", self.type_string):
      return "bool"
    elif re.match("datetime", self.type_string):
      #FIXME: Should be a date time object in C++, string for now.
      return "string"
    elif re.match("[Ss]tring", self.type_string):
      return "string"
    elif re.match("Date", self.type_string) or re.match("Time", self.type_string):
      #FIXME: Should be a date time object in C++, string for now.
      return "string"
    elif re.match("char", self.type_string):
      return "char"
    else:
      raise NotImplementedError("Type %s is unknown" % self.type_string)
  
  def isNativeType(self, language="python"):
    """return true if type is a 'native' type of a langage
    """
    for re_string in NativeTypes["python"]:
      if re.match(re_string, self.type_string):
        return 1
    else:
      return 0
    #return self.type_string in NativeTypes["python"]
  
  
