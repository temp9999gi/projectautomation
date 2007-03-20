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


from __future__ import nested_scopes
import types
from bool import Bool
import mx.DateTime
from warnings import warn
from dbAPI import *

def getPrimaryKeyName():
  return 'group_pk'

def getForeignKeyName():
  return 'group_fk'

def getClass():
  return Group

def getTableName():
  return "group"

def getClassName():
  return "Group"

class Group(DBClass):
  table_name = "group"
  def __init__(self, primary_key=None, db_session=None):
    DBClass.__init__(self, db_session)
    self.fields["group_pk"] = Field("group_pk", types.IntType, "Group_pk")
    self.fields["name"] = Field("name", types.StringType, "name")
    import NameLinkPair
    self.associations["name_link_pair"] = DBAssociation(self, NameLinkPair, 1, 1)
    if self.db_session is not None:
      self.connect()
    if primary_key is not None:
      self.loadSelf(primary_key)
  
  def getPrimaryKeyName(self):
    return 'group_pk'
  
  def getForeignKeyName(self):
    return 'group_fk'
  
  def getClassName(self):
    return 'Group'
  
  def getTableName(self):
    return 'group'
  
  def isAutoSequence(self):
    return 1
  
  def getGroupPk(self):
    return self.fields["group_pk"].value
  
  def setGroupPk(self, value): 
    self.fields["group_pk"].setValue(value)
  
  def getName(self):
    return self.fields["name"].value
  
  def setName(self, value): 
    self.fields["name"].setValue(value)
  
  # t=Group, o=NameLinkPair
  def getNameLinkPair(self):
    association = self.associations['name_link_pair']
    return association.getObjects()
  
  def setNameLinkPair(self, object):
    association = self.associations['name_link_pair']
    association.setObjects(object)
  
  def appendNameLinkPair(self, object):
    association = self.associations['name_link_pair']
    association.appendObjects(object)
  
