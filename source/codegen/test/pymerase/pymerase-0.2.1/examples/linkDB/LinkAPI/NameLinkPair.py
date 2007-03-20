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
  return 'name_link_pair_pk'

def getForeignKeyName():
  return 'name_link_pair_fk'

def getClass():
  return NameLinkPair

def getTableName():
  return "name_link_pair"

def getClassName():
  return "NameLinkPair"

class NameLinkPair(DBClass):
  table_name = "name_link_pair"
  def __init__(self, primary_key=None, db_session=None):
    DBClass.__init__(self, db_session)
    self.fields["name_link_pair_pk"] = Field("name_link_pair_pk", types.IntType, "NameLinkPair_pk")
    self.fields["name"] = Field("name", types.StringType, "name")
    self.fields["url"] = Field("url", types.StringType, "url")
    self.fields["group_fk"] = Field("group_fk", types.IntType, "Group_fk")
    import Group
    self.associations["group"] = DBAssociation(self, Group, 0, 0)
    if self.db_session is not None:
      self.connect()
    if primary_key is not None:
      self.loadSelf(primary_key)
  
  def getPrimaryKeyName(self):
    return 'name_link_pair_pk'
  
  def getForeignKeyName(self):
    return 'name_link_pair_fk'
  
  def getClassName(self):
    return 'NameLinkPair'
  
  def getTableName(self):
    return 'name_link_pair'
  
  def isAutoSequence(self):
    return 1
  
  def getNameLinkPairPk(self):
    return self.fields["name_link_pair_pk"].value
  
  def setNameLinkPairPk(self, value): 
    self.fields["name_link_pair_pk"].setValue(value)
  
  def getName(self):
    return self.fields["name"].value
  
  def setName(self, value): 
    self.fields["name"].setValue(value)
  
  def getUrl(self):
    return self.fields["url"].value
  
  def setUrl(self, value): 
    self.fields["url"].setValue(value)
  
  def getGroupFk(self):
    return self.fields["group_fk"].value
  
  def setGroupFk(self, value): 
    self.fields["group_fk"].setValue(value)
  
  # t=NameLinkPair, o=Group
  def getGroup(self):
    association = self.associations['group']
    return association.getObjects()
  
  def setGroup(self, object):
    association = self.associations['group']
    association.setObjects(object)
  
