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

class fk_util:
  """Convenance utility for help with pymerase links"""

  def __init__(self):
    pass
  
  def getLocalLinks(self, table):
    """
    Given Table/Class returns list of links declared in that table.
    """ 
  
    tableName = table.getName() 
    assoc = table.getAssociations()
    linkList = []
    for a in assoc:
      if a.getContainingClassName() == tableName:
        linkList.append(a)
        
    return linkList

  def getForeignLinks(self, table):
    """
    Given Table/Class returns list of links declared in a foreign table.
    """
    tableName = table.getName()
    assoc = table.getAssociations()
    linkList = []
    for a in assoc:
      if a.getContainingClassName() != tableName:
        linkList.append(a)

    return linkList
    

  def getLinkTable(self, tables, assoc):
    """
    Given a list of tables and an association which links to one
    of the tables, find the table and return it.
    """
    targetTable = assoc.getTargetClassName()
    for tbl in tables:
      if tbl.getName() == targetTable:
        return tbl
    #return None
    msg = "getLinkTable [FATAL] No matching table"
    raise ValueError, msg