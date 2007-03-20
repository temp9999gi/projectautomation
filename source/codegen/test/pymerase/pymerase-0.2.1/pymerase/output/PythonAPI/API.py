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
#
#       Authors: Diane Trout
# Last Modified: $Date: 2006/12/18 15:54:02 $
#
from __future__ import nested_scopes

import imp
import os
import pprint
import string
import sys
import types
import traceback

import fkeyTypes

from mx import DateTime
from mx.DateTime.Parser import DateTimeFromString

import warnings
from warnings import warn
class DebugWarning(Warning):
  pass
warnings.filterwarnings('ignore', category=DebugWarning, append=1)

class Attribute:
  """Stores information about object attributes.

  Including name, type, null, and a cached copy of the value.
  """
  def __init__(self, name, type=None, friendlyName=None):
    self.name = name
    self.friendlyName = friendlyName
    self.type = type
    self.modified = 0
    self.value = None
    self.nullAllowed = 1

    # Orientated more for serialization interface
    self.loaded_value = None

  def setValue(self, value, loading = 0):
    """
    Sets the value of the field after checking to make sure the types
    are compatible.
    """
    # FIXME: type checking needs work
    # FIXME: if self.type isn't none we can type check
    # FIXME: if value is none, 
    # FIXME:   can we be null?
    # FIXME:   if yes: skip remainder of type checking
    # FIXME:   if no: throw error
    # FIXME: does values type match our 
    # FIXME:
    if self.type is not None:
      # check for null
      if value is None:
        if not self.nullAllowed:
          error_msg = "Field %s must not be null" % ( self.name )
          raise ValueError(error_msg)
      # try to typecast datetime types
      elif self.type == DateTime.DateTimeType and (type(value) == types.StringType or type(value) == types.UnicodeType):
        value = DateTimeFromString(value)
      # FIXME: postgresql returns bigints for sequences
      # FIXME:  which breaks this type checking code
      # FIXME: I'm not sure this coercion is a good idea since
      # FIXME: it might cause size problems
      elif self.type == types.IntType and type(value) == types.LongType:
        pass
      # FIXME: the following code fragment was added 'cause it
      # FIXME: it seems that you can't add subclassed objects to
      # FIXME: things expecting their base classes.
      # FIXME: also changed advisor link from faculty to employee to try
      # FIXME: and create some inheritance.
      #elif self.type == types.ClassType and issubclass(value, self.type):
      #    pass
      elif self.type != type(value):
        error_msg = "Incompatible type for field %s, expecting %s, got %s"
        error_msg = error_msg % (self.name,
                                 str(self.type),
                                 str(type(value)))
        raise ValueError(error_msg)
      
    if not loading:
      warn("modified %s to %s" % (self.name , str(value)), DebugWarning)
      self.modified = 1

    self.value = value

  def isModified(self):
    if self.modified:
      return 1
    else:
      return 0

  def isNotNull(self):
    return not self.nullAllowed

  def __str__(self):
    return pprint.pformat(self.__dict__)
                         
class Association:
  """Represents links to collections of other classes.
  """
  #def __init__(self, column_id, localTable, foreign_table, pkey, type, table, class_reference):
  def __init__(self, localTable, foreignTable, type, containgReference, classToCreateReference):
    # Information about the foreign key
    self.localTable = localTable
    self.foreignTable = foreignTable
    self.associationType = type

    # information about the object we're embedded in
    self.containgReference = containgReference
    self.classToCreateReference = classToCreateReference
    
    # FIXME: This probably needs to be converted to a weak reference
    self.serializedObjects = None
    self.memoryObjects = []

  def __len__(self):
    count = 0
    if self.serializedObjects is not None:
      count += len(self.serializedObjects)
    count += len(self.memoryObjects)
    return count
      
  def getObjects(self):
    if self.serializedObjects is None:
      self.serializedObjects = self.__loadObjects()
      
    return self.serializedObjects + self.memoryObjects

  def appendObjects(self, object):
    if self.associationType == fkeyTypes.OneToOne:
      if len(self) >= 1:
        msg = "One to one links cannot have more than one linked object"
        raise ValueError(msg)
    #if not isinstance(object, self.class_reference):
    elif type(object) != types.InstanceType:
      msg = "Requires class instance"
      raise ValueError(msg)
#    # FIXME: type checking is not working for subclasses
#    elif not issubclass(object.__class__, self.class_reference):
#      msg = "Got object [%s], was expecting [%s]"
#      msg %= (str(object.__class__), str(self.class_reference))
#              
#      raise ValueError(msg)
#    
    self.memoryObjects.append(object)

class SerializableClass:
  """Base class for all the classes that are database backed.
  """
  def __init__(self, db_session=None):
    self.loaded = 0

    # FIXME: I don't like this code, but it prevents a base class from
    # FIXME: reinitializing the list of fields & links back to null
    # FIXME: perhaps we should seperate the class information
    # FIXME: from the writer interface?
    if not hasattr(self, 'attributes'):
      self.attributes = {}
    if not hasattr(self, 'associations'):
      self.associations = {}

    self.db_session = db_session

