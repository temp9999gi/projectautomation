###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2003 by:                                                 #
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
#      Revision: $Revision: 1.1 $
#

"""Creates a cgi script for each Class/Table"""


#Imported System Packages.
import os
import string
import re

from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociationEnds

from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning
import warnings
from warnings import warn

############################
# Globals

TRANSLATOR_NAME='CreateDbTableBrowser'

def getTemplate():
  template = """#!/usr/bin/env python
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2003 by:                                                 #
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
#     Generator: Pymerase (CreateDbTableBrowser Output Module)
#       Authors: Brandon King
# Last Modified: $Date: 2006/12/18 15:54:02 $
#      Revision: $Revision: 1.1 $
#

import cgi
import os
import sys
import pickle
import re
import string
import time
import ConfigParser
import cgitb
cgitb.enable()

from %PACKAGE_NAME% import DBSession

#Automatic update of version by CVS
rev = "$Revision: 1.1 $"
rev = rev.replace('$Revision: ', '')
rev = rev.replace(' $', '')

VERSION = '0.%s' % (rev)

TITLE = '<a href=\"http://pymerase.sf.net/\">Pymerase</a> Generated Custom DB'

#CONFIG FILE PATH
CONFIG_FILE = os.path.abspath('./%PACKAGE_NAME%%CLASS_NAME%.cfg')

#DEFAULT DIRS
ROOTPATH = '/var/local/%PACKAGE_NAME%'


#PathAliasConveter
# Converts between strings (alias) passed in URL to web browser
# and the actual paths in which the file is located
#PathAliasConverter = {}
#PathAliasConverter[ROOTPATH] = LOC_BROWSER
#PathAliasConverter[TRASHPATH] = LOC_TRASH
#PathAliasConverter[DELETEPATH] = LOC_DELETE
#PathAliasConverter[TEMPDIR] = LOC_TMP
#PathAliasConverter[LOC_BROWSER] = ROOTPATH
#PathAliasConverter[LOC_TRASH] = TRASHPATH
#PathAliasConverter[LOC_DELETE] = DELETEPATH
#PathAliasConverter[LOC_TMP] = TEMPDIR

#Direction of Ordering
ASCENDING = 0
DESCENDING = 1

#SORTING
FLD_LIST = []


#DEFAULT URLS
ROOTURL = '/%PACKAGE_NAME%/'
SCRIPT = '/cgi-bin/%PACKAGE_NAME%%CLASS_NAME%.cgi'

#VIEWS
TABLEVIEW = 'tableView'
RECORDVIEW = 'recordView'

#DEFAULT COLORS
BROWSER_COLOR = '#CCCCFF'
TRASH_COLOR = '#FF0000'

#CONFIG FILE PROCESSING

if os.path.isfile(CONFIG_FILE):
  parser = ConfigParser.ConfigParser()
  parser.read(CONFIG_FILE)

  if parser.has_section('INFO'):
    if parser.has_option('INFO', 'TITLE'):
      TITLE = parser.get('INFO', 'TITLE')
    if parser.has_option('INFO', 'BROWSER_COLOR'):
      BROWSER_COLOR = parser.get('INFO', 'BROWSER_COLOR')
    #if parser.has_option('INFO', 'TRASH_COLOR'):
    #  TRASH_COLOR = parser.get('INFO', 'TRASH_COLOR')
  
  if parser.has_section('DIRS'):
    if parser.has_option('DIRS', 'ROOTPATH'):
      ROOTPATH = parser.get('DIRS', 'ROOTPATH')
    if parser.has_option('DIRS', 'TEMPDIR'):
      TEMPDIR = parser.get('DIRS', 'TEMPDIR')
      
  if parser.has_section('URLS'):
    if parser.has_option('URLS', 'ROOTURL'):
      ROOTURL = parser.get('URLS', 'ROOTURL')
    if parser.has_option('URLS', 'SCRIPT'):
      SCRIPT = parser.get('URLS', 'SCRIPT')


#def search(dataDict, field, query):
#  \"\"\"
#  search(dataDict, field, query)
#    --> 1 if search succesful
#    --> 0 if search failed
#
#  dataDict - provides meta data about a file
#  field    - determines which field should be search
#             if field == 'all', all fields searched
#  query    - regular expression search
#  \"\"\"
#  #FIXME: Try using filter() to speed up!
#  
#  #setup regular expression, ignore case.
#  engine = re.compile(query, re.IGNORECASE)
#
#  #check all fields or individual?
#  if field != "all":
#    result = engine.search(dataDict[field])
#    if result is not None:
#      return 1
#    else:
#      return 0
#  else:
#    for key in dataDict.keys():
#      result = engine.search(str(dataDict[key]))
#      if result is not None:
#        return 1
#    return 0


def getField(friendlyName):
  for fld in FLD_LIST:
    if fld.friendlyName == friendlyName:
      return fld.name
  return None

def getSortedRecords(sortField, direction, query=None, field=None):
  \"\"\"
  getSortedRecords(sortField, direction)
    --> All files (list), no sorting if sortFiled does not exist
    --> sortedFileList

  sortField - the field name you want to sort by
  direction - ASCENDING or DESCENDING vars
  \"\"\"
  #get all records from DB
  allRecords = getRecords(query, field, sortField, direction)

  sortRecList = []
  for rec in allRecords:
    sortRecList.append(getDataDict(rec))

  return sortRecList


def getRecords(query=None, field=None, sortField=None, direction=None):
  \"\"\"
  Downloads records from database.
  \"\"\"
  if direction == ASCENDING:
    sortDirect = ' ASC'
  elif direction == DESCENDING:
    sortDirect = ' DESC'
  else:
    sortDirect = ''

  #FIXME: Need to have some way of overriding these values!
  dbs = DBSession('localhost', 'tabdata', 'king')
  
  if query is not None and field is not None:
    if field != 'all':
      fldName = getField(field)
      if fldName is not None:
        if sortField is not None:
          objList = dbs.getObjectsWhere(dbs.%CLASS_NAME%, '%s LIKE \\\'%s%s%s\\\' ORDER BY %s%s' % \\
                                        (fldName, '%', query, '%', getField(sortField), sortDirect))
        else:
          objList = dbs.getObjectsWhere(dbs.%CLASS_NAME%, '%s LIKE \\\'%s%s%s\\\'' % (fldName, '%', query, '%'))
      else:
        raise ValueError, 'Invalid Field Name (%s)' % (field)
    else:
      sqlSearch = []
      for fld in FLD_LIST:
        tmp = '%s LIKE \\\'%s%s%s\\\'' % (fld.name, '%', query, '%')
        sqlSearch.append(tmp)
      sqlSearch = string.join(sqlSearch, ' OR ')
      if sortField is not None:
        sqlSearch += ' ORDER BY %s%s' % (getField(sortField), sortDirect)
      objList = dbs.getObjectsWhere(dbs.%CLASS_NAME%, '%s' % (sqlSearch))
  else:
    objList = dbs.getAllObjects(dbs.%CLASS_NAME%)
    #NOTE: Comment out the line above if number of objects is too large
    # Then uncomment the 4 lines below
    #tmpObj = dbs.%CLASS_NAME%()
    #objList = dbs.getObjectsWhere(dbs.%CLASS_NAME%,
    #                              '%s BETWEEN %s AND %s ORDER BY %s%s' % \\
    #                              (tmpObj.getPrimaryKeyName(), 1, 50, getField(sortField), sortDirect))
  return objList
  


def getDataDict(dbObj):
  \"\"\"
  getDataDict(filePath)
    --> link, dataDict
    
      link - URL to File for downloading
      dataDict - meta data about file
  \"\"\"
  dataDict = {}
  for field in dbObj.fields.values():
    dataDict[field.friendlyName] = field.value
    
  return dataDict



#def isSafe(fileName):
#  \"\"\"
#  isSafe(fileName)
#    --> 1 if fileName doesn't contain dir chars / or \
#    --> 0 if fileName does contain dir chars / or \
#  \"\"\"
#  if '\\' not in fileName or '/' not in fileName or fileName != 'viewer.cfg':
#    return 1
#  else:
#    return 0



def printTableViewHeader(direction, view, search=None, field=None):
  if search is not None and field is not None:
    memString = '&direction=%s&view=%s&search=%s&field=%s' % \\
                (direction, view, search, field)
  else:
    memString = '&direction=%s&view=%s' % \\
                (direction, view)
  
  print "<table border=\\\"2\\\">"
  print "  <tr bgcolor=\\\"%s\\\">" % (BROWSER_COLOR)
  for fld in FLD_LIST:
    print "    <td>"
    print "      <div align=\\\"center\\\">"
    print "      <a href=\\\"%s?sortField=%s%s\\\"><b>%s</b></a>" % \\
          (SCRIPT, fld.friendlyName, memString, fld.friendlyName)
    print "      </div>"
    print "    </td>"
  print "  </tr>"



def printTableViewRecord(dataDict):
  print "  <tr>"
  for fld in FLD_LIST:
    print "    <td>"
    print "      %s" % dataDict[fld.friendlyName]
    print "    </td>"
  print "  </tr>"


def printTableViewFooter():
  print "</table>"
  print "<br>"



def printRecord(dataDict, direction, view, search=None, field=None):
  if search is not None and field is not None:
    memString = '&direction=%s&view=%s&search=%s&field=%s' % \\
                (direction, view, search, field)
  else:
    memString = '&direction=%s&view=%s' % \\
                (direction, view)
  print "<table border=\\\"2\\\">"
  for fld in FLD_LIST:
    print "  <tr>"
    print "    <td bgcolor=\\\"%s\\\">" % (BROWSER_COLOR)
    print "      <div align=\\\"right\\\">"
    print "      <a href=\\\"%s?sortField=%s%s\\\"><b>%s</b></a>" % \\
          (SCRIPT, fld.friendlyName, memString, fld.friendlyName)
    print "    </div>"
    print "    </td>"
    print "    <td>"
    print "      %s" % (dataDict[fld.friendlyName])
    print "    </td>"
    print "  </tr>"
  print "</table>"
  print "<br>"



    
########################
# MAIN
if __name__ == '__main__':
  form = cgi.FieldStorage()
  
  #Default message
  msg = ""

  #Process Uploads and retrive message
  #if form.has_key('uploading'):
  #  msg += upload(form)

  #save view state
  if form.has_key('view'):
    view = form['view'].value
  else:
    view = TABLEVIEW
     
  #check if the user wants ASCENDING or DESCENDING data
  if form.has_key('direction'):
    direction = int(form['direction'].value)
  else:
    direction = DESCENDING

  #check if user wants to sort the data
  if form.has_key('sortField'):
    sortField = form['sortField'].value
  else:
    sortField = 'OligoName'

  #print html definition
  text = "Content-Type: text/html\\n\\n"
  print text

  #setup query string for saved states
  searchString = ""
  directionString = ""
  #search state
  if form.has_key('search') and form.has_key('field'):
    text = "&search=%s&field=%s" % (form['search'].value, form['field'].value)
    searchString += text
    directionString += text

  #direction state
  if form.has_key('direction'):
    searchString += "&direction=%s" % (direction)

  #sorting state
  if form.has_key('sortField'):
    text = "&sortField=%s" % (sortField)
    searchString += text
    directionString += text

  #view state
  if view is not None:
    text = '&view=%s' % (view)
    directionString += text

  
  ########################
  # HTML - Header and Menu
  header = \"\"\"<html>
<head>
<title>%s</title>
</head>
<body>
	<div align="center">
	<h1>%s</h1>
        Generator Version %s<br><br>
        [ <a href=\"\#search\">Search</a> |
        <a href=\"%s?view=%s\">View All</a> ]<br>
        [ <a href=\"%s?view=tableView%s\">Table View</a> |
        <a href=\"%s?view=recordView%s\">Record View</a> ]<br>
        [ <a href=\"%s?direction=0%s\">Ascending</a> |
        <a href=\"%s?direction=1%s\">Decending<a/> ]<br>
        <br>
\"\"\" % (TITLE, TITLE, VERSION, SCRIPT, view, SCRIPT, searchString, SCRIPT, searchString, SCRIPT, directionString, SCRIPT, directionString)


  ########################
  # HTML - Footer
  footer = \"\"\"</div>
</body>
</html>

\"\"\"


                        
  ########################
  # HTML - Search Form

  #remember users view choice in Search form
  if view == RECORDVIEW:
    tableViewSelected = ''
    recordViewSelected = 'selected'
  else:
    tableViewSelected = 'selected'
    recordViewSelected = ''

  #FIXME: UPDATE FIELD OPTIONS FOR CODE GENERATION
  searchForm = \"\"\"<form action="%s" method="POST" enctype="multipart/form-data">
<table>
	<tr>
		<td>
			<div align="right"><b>Search:</b></div>
		</td>
		<td>
			<input type="text" name="search" size="30">
		</td>
	</tr>
	<tr>
		<td>
			<div align="right"><b>Field:</b></div>
               </td>
               <td>
                 <select name="field" size="1">
                 <option value="all" label="all">All</option>
                 %s
                 </select>
			
		</td>
	</tr>
        <tr>
		<td>
			<div align="right"><b>View:</b></div>
               </td>
               <td>
                 <select name="view" size="1">
                 <option value="tableView" label="tableView" %s>Table View</option>
                 <option value="recordView" label="recordView" %s>Record View</option>
                 </select>
			
		</td>
	</tr>
	<tr>
		<td>
			<div align="right"></div>
		</td>
		<td>
			<div align="left">
                        <input type="hidden" name="direction" value="%s">
                        <input type="hidden" name="sortField" value="%s">
			<input name="Submit" value="Submit" type="submit">
			<input name="Reset" value="Reset" type="reset">
			</div>
		</td>
	</tr>
</table>
</form>
\"\"\" % (SCRIPT, '%OPTIONS%', tableViewSelected, recordViewSelected, direction, sortField)

    
                        
  ########################
  # Begin HTML Printing

  #print header - Title, version, menus
  print header
  
  #show if there is a search
  if form.has_key('search'):
    msg += '<b>Searching:</b> Query=%s, Field=%s<br><br>' % \\
          (form['search'].value, form['field'].value)

  #Create FLD_LIST
  #if len(recList) >= 1:
  dbs = DBSession('localhost', 'arab_oligo', 'king')
  rec = dbs.%CLASS_NAME%()
  try:
    f = open(os.path.abspath('./data/%PACKAGE_NAME%%CLASS_NAME%Fields.pickle'), 'r')
    FLD_LIST = pickle.load(f)
    f.close()
  except:
    FLD_LIST = rec.fields.values()
    f = open(os.path.abspath('./data/%PACKAGE_NAME%%CLASS_NAME%Fields.pickle'), 'w')
    pickle.dump(FLD_LIST, f)
    f.close()
  

  #get records from database.
  if form.has_key('search'):
    recList = getSortedRecords(sortField, direction, form['search'].value, form['field'].value)
  else:
    recList = getSortedRecords(sortField, direction)

  if msg != '':
    msg += 'Records returned is %s' % (len(recList))
  else:
    msg = 'Records returned is %s' % (len(recList))

  #print messages
  if msg != '':
    print '<table border=\"2\">'
    print '  <tr><td bgcolor="FF0000">'
    print '    <h3><div align=\"center\">MESSAGES</div></h3>'
    print '  </td></tr>'
    print '  <tr><td>'
    print msg
    print '  </tr></td>'
    print '</table>'
    print '<br>'
  

  #Update Search Options in Search HTML
  for fld in FLD_LIST:
    newHtml = "<option value=\\\"%s\\\" label=\\\"%s\\\">%s</option>\\n" % (fld.friendlyName, fld.friendlyName, fld.friendlyName)
    newHtml += "                 %OPTIONS%"
    searchForm = re.sub('%OPTIONS%', newHtml, searchForm)

  #print tableview header if needed
  if view == TABLEVIEW:
    if form.has_key('search') and form.has_key('field'):
      printTableViewHeader(direction, view,
                           form['search'].value, form['field'].value)
    else:    
      printTableViewHeader(direction, view)


  #process each file
  for dataDict in recList:
    #dataDict = getDataDict(rec)

    if view == RECORDVIEW:
      if form.has_key('search') and form.has_key('field'):
        printRecord(dataDict, direction, view, form['search'].value, form['field'].value)
      else:
        printRecord(dataDict, direction, view)
    else:
      printTableViewRecord(dataDict)

  #print table view footer if needed
  if view == TABLEVIEW:
    printTableViewFooter()

  print "<HR width=\\\"90%\\\" size=\\\"1\\\" noshade>"
  print "<a name=\\\"search\\\"></a>"
  print "<h2>Search</h2>"
  #display search form
  print searchForm
  #print "<HR width=\\\"90%\\\" size=\\\"1\\\" noshade>"
  #print "<a name=\\\"upload\\\"></a>"
  #print "<h2>Upload</h2>"
  #display upload form
  #print uploadForm
  print footer

  """
  return template

def getConfigTemplate():
  template = """#%PACKAGE_NAME% %CLASS_NAME% Viewer Default Configuration File
[INFO]
TITLE=%PACKAGE_NAME% %CLASS_NAME%<br>\n<a href=\"http://pymerase.sf.net/\">Pymerase</a> Generated Custom DB
BROWSER_COLOR=#CCCCFF

[DIRS]
ROOTPATH=/var/local/%PACKAGE_NAME%
TEMPDIR=/tmp/%PACKAGE_NAME%

[URLS]
SCRIPT=/cgi-bin/%PACKAGE_NAME%%CLASS_NAME%.cgi
"""
  return template


############################
# Writer components

def write(destination, classList):
  """
  Create Table Search CGI in destination dirctory.
  """
  if os.path.exists(destination) and not os.path.isdir(destination):
    raise ValueError, '%s exists and is not a directory.' % (destination)

  if not os.path.exists(destination):
    os.mkdir(destination)

  #Iterate through the tables/classes and process the data
  for cls in classList:
    code = getTemplate()
    cfg = getConfigTemplate()
      
    #Provide class and package names for cgi code
    code = re.sub('%CLASS_NAME%', cls.getName(TRANSLATOR_NAME), code)
    code = re.sub('%PACKAGE_NAME%', cls.getPackage(), code)

    #Provide class and package names for config file
    cfg = re.sub('%CLASS_NAME%', cls.getName(TRANSLATOR_NAME), cfg)
    cfg = re.sub('%PACKAGE_NAME%', cls.getPackage(), cfg)

    #CGI file for Class
    classFile = cls.getPackage() + cls.getName(TRANSLATOR_NAME) + '.cgi'
    classFilePath = os.path.join(destination, classFile)

    #Config file for Class
    cfgFile = cls.getPackage() + cls.getName(TRANSLATOR_NAME) + '.cfg'
    cfgFilePath = os.path.join(destination, cfgFile)

    #Save CGI File
    f = open(classFilePath, 'w')
    f.write(code)
    f.close()

    #Save Conf File
    f = open(cfgFilePath, 'w')
    f.write(cfg)
    f.close()

  warn("CreateDbTableBrowser Generation Complete... Good Bye.", InfoWarning)
