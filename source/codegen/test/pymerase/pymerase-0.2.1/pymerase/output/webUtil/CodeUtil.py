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

import os
import sys
import string
import re

from pymerase.util.fk_util import fk_util
from pymerase.util import PymeraseType
from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociations
from pymerase.ClassMembers import getBasePrimaryKeyName

class CodeUtil:
  """
  Utilities for writing python code
  """
  def __init__(self):
    pass

  def insertSessionInfo(self, code, label, indent = "\t"):
    """
    Inserts session information into code and returns it.
    """
    insert = indent + "self.info[\'%s\'] = None" % (label) + os.linesep
    insert += "#--INSERT_MENU_STATUS--#"
    
    code = re.sub('#--INSERT_MENU_STATUS--#', insert, code)
    
    return code
  

  def insertMenuStatus(self, code, label, indent = "\t"):
    """
    Inserts menuStatus information into code and returns it.
    """
    insert = indent + "self.menuStatus[\'%s\'] = self.DISPLAY_OFF" % (label)\
             + os.linesep
    insert += "#--INSERT_MENU_STATUS--#"
    code = re.sub('#--INSERT_MENU_STATUS--#', insert, code)
    
    return code
  
  
  def insertTableStage(self, code, tableName, stage, indent = "\t"):
    """
    Inserts menuStatus information into code and returns it.
    """
    insert = indent + "self.tableStage[\'%s\'] = \'%s\'" % (tableName, stage) \
             + os.linesep
    insert += "#--INSERT_TABLE_STAGE--#"
    
    code = re.sub('#--INSERT_TABLE_STAGE--#', insert, code)
    
    return code
  
  
  def insertStageComplete(self, code, stage, tableList,  indent = "\t"):
    """
    Inserts menuStatus information into code and returns it.
    """
    insert = indent + "self.stageComplete[\'%s\'] = %s" % (stage, tableList) \
             + os.linesep
    #log.writeln('InsertStageComplete', log.LOG_INFO, insert)
    insert += "#--INSERT_STAGE_COMPLETE--#"
    
    code = re.sub('#--INSERT_STAGE_COMPLETE--#', insert, code)
    
    return code


  def insertElifIsfrom(self, tableName, code):
    """
    Code is handled differently based on which form was sent from
    
    Replaces #--INSERT_ELIF_ISFROM--# string in template code
    and returns the code
    """
    insert = []

    insert.append("  elif util.isFromForm('%s', form):" % (tableName))
    insert.append("    mysession = util.loadSessionStatus(form['session'].value)")
    insert.append("    html = getMainMenuTemplate(mysession)")
    insert.append("")
    insert.append("    mysession.info['form'] = \'MainMenu\'")
    insert.append("")
    insert.append("    ###################")
    insert.append("    #Add new code here#")
    insert.append("    ###################")
    insert.append("")
    insert.append("    util.saveSessionStatus(mysession)")
    insert.append("")
    insert.append("    htmlUtil.printHeader()")
    insert.append("    print html")
    insert.append("")

    insert = string.join(insert, os.linesep)

    insert += os.linesep + "#--INSERT_ELIF_ISFROM--#"

    code = re.sub("#--INSERT_ELIF_ISFROM--#", insert, code)

    return code


  def insertMenuList(self, code, tables, assocObj):
    """
    Given a list of tables and a foreign key (link)
    insert MenuList handler into code and return it.
    """
    fkUtil = fk_util()

    foreignObjPk = assocObj.getTargetAttributeName()
    foreignObjName = assocObj.getTargetClassName()
    
    insertCode = []
    insertCode.append("  ############################################")
    insertCode.append("  # %s Pull Down Menu Code" % (foreignObjName))
    insertCode.append("  ############################################")
    insertCode.append("  fObjList = dbs.getAllObjects(dbs.%s)" % (foreignObjName))
    insertCode.append("  fObjAttrib = []")
    insertCode.append("  fObjPk = []")
    insertCode.append("  selected = None")
    insertCode.append("")
    insertCode.append("  for fObj in fObjList:")
    insertCode.append("    text = \"\"")

    fTbl = fkUtil.getLinkTable(tables, assocObj)
    fAttribList = getAllAttributes(tables, fTbl)
    for fAttrib in fAttribList:
      insertCode.append("    text += str(fObj.%s()) + \" | \"" % (fAttrib.getGetterName()))
    insertCode.append("")
    insertCode.append("    #remove trailing \" | \"")
    insertCode.append("    text = text[:-3]")
    insertCode.append("    if len(text) > 72:")
    insertCode.append("      fObjAttrib.append(text[:72] + \"...\")")
    insertCode.append("    else:")
    insertCode.append("      fObjAttrib.append(text)")
    insertCode.append("")
    insertCode.append("    fObjPk.append(fObj.get%s())" % (foreignObjPk))
    insertCode.append("    try:")
    insertCode.append("      if fObj.%s() == obj.%s():" \
                  % (foreignObjPk, assocObj.getGetterName()))
    insertCode.append("        selected = str(fObj.get%s())" % (foreignObjPk))
    insertCode.append("    except:")
    insertCode.append("      pass")
    insertCode.append("")
    insertCode.append("")
    insertCode.append("  listHtml = htmlUtil.insertMenuList(\'<!--INSERT_FORM_HERE-->\',")
    insertCode.append("                                 \"%s\"," % (assocObj.getName()))
    insertCode.append("                                 \"%s\"," % (assocObj.getName()))
    insertCode.append("                                 fObjAttrib,")
    insertCode.append("                                 fObjPk,")
    insertCode.append("                                 fObjPk,")
    insertCode.append("                                 selected)")
    insertCode.append("")
    insertCode.append("  html = re.sub(\'<!--INSERT_%s_HERE-->\', listHtml, html)" \
                  % (assocObj.getName()))
    insertCode.append("  #####################")
    insertCode.append("")
    insertCode.append("#--INSERT_LINK_MENU_CODE--#")

    insertCode = string.join(insertCode, os.linesep)

    code = re.sub("#--INSERT_LINK_MENU_CODE--#", insertCode, code)

    return code


  def insertTableMenuList(self, code, tables, table):
    """
    Inserts Table Menu Code into code and returns it.
    """
    insertCode = []
    insertCode.append("  menuItem = []")
    insertCode.append("  pkList = []")
    insertCode.append("  for obj in objList:")
    insertCode.append("    item = \"\"")
    attribList = getAllAttributes(tables, table)
    for attrib in attribList:
      insertCode.append("    item += str(obj.%s())" % (attrib.getGetterName()))
      insertCode.append("    item += \" | \"")
    insertCode.append("    item = item[:-3]")
    insertCode.append("    if len(item) <= 72:")
    insertCode.append("      menuItem.append(item)")
    insertCode.append("    else:")
    insertCode.append("      menuItem.append(item[:72] + \"...\")")
    insertCode.append("")
    insertCode.append("    pk = str(obj.get%s())" % (getBasePrimaryKeyName(tables, table)))
    insertCode.append("    pkList.append(pk)")
    insertCode.append("")
    insertCode.append("  html = htmlUtil.insertMenuList(html,")
    insertCode.append("                                 'Select Entry to Edit',")
    insertCode.append("                                 'selection',")
    insertCode.append("                                 menuItem,")
    insertCode.append("                                 pkList,")
    insertCode.append("                                 pkList)")

    insertCode = string.join(insertCode, os.linesep)

    code = re.sub("#--INSERT_TABLE_MENU_LIST--#", insertCode, code)

    return code


  def insertTableName(self, code, tableName):
    """
    Inserts tableName into code and returns code.
    """
    return re.sub('#--TABLE_NAME--#', tableName, code)


  def insertFormLoader(self, code, attrib):
    """
    Inserts code to load current DB data into HTML form.

    returns code
    """
    pyType = attrib.getType().getSQLType()
    loadCode = []
    
    if PymeraseType.isVarchar(pyType)\
       or PymeraseType.isChar(pyType)\
       or pyType == "integer"\
       or pyType == "double precision"\
       or pyType == "name":
    
      loadCode.append("  %s_old = \"\\\"%s\\\" value=\\\"\\\"\"" \
                      % (attrib.getName(), attrib.getName()))
      loadCode.append("  if type(obj.%s()) != type(None):" % (attrib.getGetterName()))
      loadCode.append("    %s_new = \"\\\"%s\\\" value=\\\"%s\\\"\" %% (obj.%s())" \
                      % (attrib.getName(), attrib.getName(), '%s', attrib.getGetterName()))
      loadCode.append("    html = re.sub(%s_old, %s_new, html)" \
                      % (attrib.getName(), attrib.getName()))
      loadCode.append("")
      loadCode.append("#--INSERT_FORM_LOADER--#")
      
      loadCode =  string.join(loadCode, os.linesep)

    elif pyType == "text":
      
      loadCode.append("  %s_old = \"<textarea name=\\\"%s\\\" rows=\\\"6\\\" cols=\\\"72\\\"></textarea>\""\
                      % (attrib.getName(), attrib.getName()))
      loadCode.append("  %s_new = \"<textarea name=\\\"description\\\" rows=\\\"6\\\" cols=\\\"72\\\">%s</textarea>\" %% (obj.%s())" % (attrib.getName(), '%s', attrib.getGetterName()))
      loadCode.append("  html = re.sub(%s_old, %s_new, html)" \
                      % (attrib.getName(), attrib.getName()))
      loadCode.append("")
      loadCode.append("#--INSERT_FORM_LOADER--#")
      
      loadCode =  string.join(loadCode, os.linesep)

    elif pyType == "timestamp with time zone":
      loadCode.append("  %s_old = \"\\\"%s\\\" value=\\\"\\\"\"" \
                      % (attrib.getName(), attrib.getName()))
      loadCode.append("  %s_new = \"\\\"%s\\\" value=\\\"%s\\\"\" %% (str(obj.%s()) + \'+08:00\')" \
                      % (attrib.getName(), attrib.getName(), '%s', attrib.getGetterName()))
      loadCode.append("  html = re.sub(%s_old, %s_new, html)" \
                      % (attrib.getName(), attrib.getName()))
      loadCode.append("")
      loadCode.append("#--INSERT_FORM_LOADER--#")
      
      loadCode =  string.join(loadCode, os.linesep)
    else:
      print "insertFormLoader(...) [WARN] Unknown type (%s)" % (pyType)
      return code
      
    code = re.sub('#--INSERT_FORM_LOADER--#',
                  loadCode, 
                  code)
    return code


  def insertProcessEditRecord(self, code, attrib):
    """
    Writes python code which loads form into existing DBAPI object.
    """
    commitCode = []

    attribType = attrib.getType().getSQLType()
    
    if attribType == "integer" or attribType == "serial":
      commitCode.append("  if form.has_key(\'%s\'):" % (attrib.getName()))
      commitCode.append("    obj.%s(int(form[\'%s\'].value))" % (attrib.getSetterName(), attrib.getName()))
      
    elif attribType == "double precision":
      commitCode.append("  if form.has_key(\'%s\'):" % (attrib.getName()))
      commitCode.append("    obj.%s(float(form[\'%s\'].value))" % (attrib.getSetterName(), attrib.getName()))

    else:
      commitCode.append("  if form.has_key(\'%s\'):" % (attrib.getName()))
      commitCode.append("    obj.%s(form[\'%s\'].value)" % (attrib.getSetterName(), attrib.getName()))

    commitCode.append("")
    commitCode.append("#--INSERT_PROCESS_EDIT_RECORD--#")
    
    commitCode = string.join(commitCode, os.linesep)

    return re.sub("#--INSERT_PROCESS_EDIT_RECORD--#", commitCode, code)


  def insertProcessNewRecord(self, code, attrib):
    """
    Writes python code which loads form into existing DBAPI object.
    """
    commitCode = []

    attribType = attrib.getType().getSQLType()
    
    if attribType == "integer" or attribType == "serial" or attribType == "boolean":
      commitCode.append("  if form.has_key(\'%s\'):" % (attrib.getName()))
      commitCode.append("    if form[\'%s\'].value != \"\":" % (attrib.getName()))
      commitCode.append("      obj.%s(int(form[\'%s\'].value))" \
                        % (attrib.getSetterName(), attrib.getName()))
      
    elif attribType == "double precision":
      commitCode.append("  if form.has_key(\'%s\'):" % (attrib.getName()))
      commitCode.append("    if form[\'%s\'].value != \"\":" % (attrib.getName()))
      commitCode.append("      obj.%s(float(form[\'%s\'].value))" \
                        % (attrib.getSetterName(), attrib.getName()))

    else:
      commitCode.append("  if form.has_key(\'%s\'):" % (attrib.getName()))
      commitCode.append("    if form[\'%s\'].value != \"\":" % (attrib.getName()))
      commitCode.append("      obj.%s(form[\'%s\'].value)" \
                        % (attrib.getSetterName(), attrib.getName()))

    commitCode.append("")
    commitCode.append("#--INSERT_PROCESS_NEW_RECORD--#")
    
    commitCode = string.join(commitCode, os.linesep)

    return re.sub("#--INSERT_PROCESS_NEW_RECORD--#", commitCode, code)


  def insertFormId(self, code, attrib):
    """
    Inserts Code which...
    Inserts Primary Key ID into HTML Form of loaded DB object.

    returns code
    """
    idCode = []
    
    idCode.append("  myId = \'ID(%s):<br>\' %% (obj.%s())" \
                  % ('%s', attrib.getGetterName()))
    idCode.append("  hiddenHtml = htmlUtil.getHiddenInputBox(myId, '%s', str(obj.%s()))" % (attrib.getName(), attrib.getGetterName()))
    idCode.append("  html = re.sub(\"<!--INSERT_%s_HERE-->\", hiddenHtml, html)" % (attrib.getName()))
    idCode.append("")
    idCode.append("#--INSERT_ID--#")

    idCode = string.join(idCode, os.linesep)

    return re.sub("#--INSERT_ID--#", idCode, code)


  def insertGetData(self, code, attributes, indent = 2):
    """
    Inserts code which retrieves data from API

    returns code
    """
    ind = " " * indent
    list = []
    for attrib in attributes:
      text = ind + "%s = obj.%s()" % (attrib.getName(), attrib.getGetterName())
      list.append(text)
      if attrib.isPrimaryKey():
        text = ind + "primaryKey = %s" % (attrib.getName())
        list.append(text)

    list = string.join(list, os.linesep)

    return re.sub('#--INSERT_GET_DATA--#', list, code)


  def insertGetData2(self, code, attributes, indent = 4):
    """
    Inserts code which retrieves data from API

    returns code
    """
    ind = " " * indent
    list = []
    for attrib in attributes:
      text = ind + "%s = obj.%s()" % (attrib.getName(), attrib.getGetterName())
      list.append(text)
      if attrib.isPrimaryKey():
        text = ind + "primaryKey = %s" % (attrib.getName())
        list.append(text)

    list = string.join(list, os.linesep)

    return re.sub('#--INSERT_GET_DATA2--#', list, code)


  def insertHeaderList(self, code, attributes):
    """
    Insert code that becomes the header for html table

    returns code
    """
    list = []
    for attrib in attributes:
      text = "  headerList.append(\"<strong>%s</strong>\")" % (attrib.getName())
      list.append(text)
      
    list = string.join(list, os.linesep)

    return re.sub('#--INSERT_HEADER_LIST--#', list, code)

  
  def insertHtmlBodyList(self, code, attributes, assocList):
    """
    Insert code that becomes the header for html table
    
    returns code
    """
    list = []
    for attrib in attributes:
      if attrib.getName() not in assocList:
        text = "  htmlBody.append(%s)" % (attrib.getName())
        list.append(text)
      else:
        text = "  htmlBody.append(%sLink)" % (attrib.getName())
        list.append(text)
     
    list = string.join(list, os.linesep)
     
    return re.sub('#--INSERT_HTML_BODY_LIST--#', list, code)


  def insertTableRowData(self, code, attributes, assocList):
    """
    Insert code that becomes the body of html table
    
    returns code
    """
    list = []
    for attrib in attributes:
      if attrib.getName() not in assocList:
        text = "    tblRow.append(obj.%s())" % (attrib.getGetterName())
        list.append(text)
      else:
        text = "    tblRow.append(%sLink)" % (attrib.getName())
        list.append(text)
     
    list = string.join(list, os.linesep)
     
    return re.sub('#--INSERT_TABLE_ROW_DATA--#', list, code)


  def insertLinkForm(self, code, assocList, indent = 2):
    """
    Insert newCode into code to handle following foreign keys

    returns code
    """
    newCode = []

    ind = " " * indent

    for assoc in assocList:
      newCode.append(ind + "####################################")
      newCode.append(ind + "# %s HTML Link Code           #" % (assoc.getContainingClassName()))
      newCode.append(ind + "####################################")
      newCode.append(ind + "if %s is not None:" % (assoc.getName()))
      newCode.append(ind + "  %sLink = []" % (assoc.getName()))
      
      newCode.append(ind + "  %sLink.append(\"<form action=\\\"./%s_web.py\\\""\
                     "method=\\\"POST\\\" enctype=\\\"multipart/form-data\\\">\")" % \
                     (assoc.getName(),
                      assoc.getTargetClassName()))
      
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"submit\\\" value=\\\"%s (%s)\\\">\" %% "\
                     "(%s))" % (assoc.getName(),
                                 assoc.getTargetClassName(),
                                 '%s',
                                 assoc.getName()))
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"hidden\\\"" \
                     "name=\\\"session\\\" value=\\\"%s\\\">\" %% (mysession.info['session']))"\
                     % (assoc.getName(), '%s'))
      
      newCode.append(ind + "  %sLink.append(\"<input type=\\\"hidden\\\" name=\\\"handler\\\""\
                     "value=\\\"viewLink\\\">\")" % (assoc.getName()))
      
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"hidden\\\" name=\\\"reqObj\\\""\
                     "value=\\\"%s\\\">\")" % (assoc.getName(), assoc.getContainingClassName()))
                     
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"hidden\\\""\
                     "name=\\\"selection\\\" value=\\\"%s\\\">\" %% (primaryKey))"\
                     % (assoc.getName(),
                        '%s'))
      
      newCode.append(ind + "  %sLink.append(\"</form>\")" % (assoc.getName()))
                     
      newCode.append(ind + "  %sLink = string.join(%sLink, \" \")" % (assoc.getName(),
                                                                    assoc.getName()))
      newCode.append(ind + "else:")
      newCode.append(ind + "  %sLink = \"\"" % (assoc.getName()))
      newCode.append("")
      newCode.append("")

    newCode = string.join(newCode, os.linesep)

    return re.sub('#--INSERT_LINK_FORMS--#', newCode, code)


  def insertLinkForm2(self, code, assocList, indent = 4):
    """
    Insert newCode into code to handle following foreign keys

    returns code
    """
    newCode = []

    ind = " " * indent
    print "assocList len(%s)" % (len(assocList))
    for assoc in assocList:
      newCode.append(ind + "####################################")
      newCode.append(ind + "# %s HTML Link Code           #" % (assoc.getContainingClassName()))
      newCode.append(ind + "####################################")
      newCode.append(ind + "if %s is not None:" % (assoc.getName()))
      newCode.append(ind + "  %sLink = []" % (assoc.getName()))
      
      newCode.append(ind + "  %sLink.append(\"<form action=\\\"./%s_web.py\\\" method=\\\"POST\\\""\
                     "enctype=\\\"multipart/form-data\\\">\")" % \
                     (assoc.getName(),
                      assoc.getTargetClassName()))
      
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"submit\\\" value=\\\"%s (%s)\\\">\" %% "\
                     "(%s))" % (assoc.getName(),
                                 assoc.getTargetClassName(),
                                 '%s',
                                 assoc.getName()))
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"hidden\\\"" \
                     "name=\\\"session\\\" value=\\\"%s\\\">\" %% (mysession.info['session']))"\
                     % (assoc.getName(), '%s'))
      
      newCode.append(ind + "  %sLink.append(\"<input type=\\\"hidden\\\" name=\\\"handler\\\""\
                     "value=\\\"viewLink\\\">\")" % (assoc.getName()))
      
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"hidden\\\" name=\\\"reqObj\\\""\
                     "value=\\\"%s\\\">\")" % (assoc.getName(), assoc.getContainingClassName()))
                     
      newCode.append(ind + "  %sLink.append(\"  <input type=\\\"hidden\\\""\
                     "name=\\\"selection\\\" value=\\\"%s\\\">\" %% (primaryKey))"\
                     % (assoc.getName(),
                        '%s'))
      
      newCode.append(ind + "  %sLink.append(\"</form>\")" % (assoc.getName()))
                     
      newCode.append(ind + "  %sLink = string.join(%sLink, \" \")" % (assoc.getName(),
                                                                    assoc.getName()))
      newCode.append(ind + "else:")
      newCode.append(ind + "  %sLink = \"\"" % (assoc.getName()))
      newCode.append("")
      newCode.append("")

    newCode = string.join(newCode, os.linesep)
    return re.sub('#--INSERT_LINK_FORMS2--#', newCode, code)

