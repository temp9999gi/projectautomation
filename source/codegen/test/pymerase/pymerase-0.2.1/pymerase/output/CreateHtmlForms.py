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

"""Creates HTML Forms of each Class/Table"""
#FIXME: HTML Generation needs more work to be really generic (I think)

#Imported System Packages.
import os
import sys
import re

sys.path.append("../pymerase")
from pymerase.output.webUtil import HTMLUtil
from pymerase.util import PymeraseType
from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociations

############################
# Globals

TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.split(HTMLUtil.__file__)[0], 'templates'))
WEB_NAME = "Generic Data Annotator"

TRANSLATOR_NAME='CreateHtmlForms'

############################
# Writer components


def isFKey(name):
    """
    Checks to see if a field is a foreign key or primary key.

    returns 1 if is fk or pk
    returns 0 if is not fk or pk
    """
    #FIXME: GeneX specific currently... needs to be more generic.
    #FIXME: Should make sure FK/PK are at end of string
    result = re.search('Fk', name)
    result2 = re.search('Pk', name)
    result3 = re.search('ID', name)
    if result != None or result2 != None or result3 != None:
        return 1
    else:
        return 0

def checkDestination(destination):
    """
    Checks to see if the destination path exists, if it doesn't it creates the directory and moves into it.
    """
    if os.path.exists(destination) == 0:
        os.mkdir(destination)
    elif os.path.isdir(destination) == 0:
        print "%s exists but is not a directory." % (destination)
        sys.exit(2)
        


###############################################
#HTML Form write function -- called by pymerase

def write(destination, tables):
    """
    Create HTML Forms in destination dirctory.

    HTML Froms can be reordered in any way as long as the form code doesn't change.
    """


    #Change directory to destination
    checkDestination(destination)

    #Get html helper util
    util = HTMLUtil.HTMLUtil()
    
    #Iterate through the tables/classes and process the data
    for tbl in tables:
        
        #Retrieve HTML Template
        html = util.getHtmlTemplate('table_template.html', TEMPLATE_PATH)

        #Set Web Page Title
        title = "%s - %s" % (WEB_NAME, tbl.getName(TRANSLATOR_NAME))
        #Set html filename
        filename = "%s.html" % (tbl.getName(TRANSLATOR_NAME))
        filePath = os.path.join(destination, filename)
        #Set scriptname to handle form
        scriptName = "%s_web.py" % (tbl.getName(TRANSLATOR_NAME))

        #Insert Title into html template
        html = util.insertTitle(html, title)
        #Insert Script name into html template
        html = util.insertScriptName(html, scriptName)

        #Process each attribute in a given table (class)
        for attribute in getAllAttributes(tables, tbl, TRANSLATOR_NAME):
            
            #get attribute type
            type = attribute.getType().getSQLType()

            print "Processing(%s:%s)" % (tbl.getName(TRANSLATOR_NAME), type)
            #Process Foriegn keys
            if isFKey(attribute.getName(TRANSLATOR_NAME)) or type == "serial":
                print "ACCESSING isFKey"
                comment = "INSERT_%s_HERE" % (attribute.getName(TRANSLATOR_NAME))
                if attribute.isRequired() == 0:
                    html = util.insertComment(html, comment)
                else:
                    html = util.insertComment(html, comment, 1)
                
            #Process Integers and Doubles
            elif type == "integer" or type == "double precision":
                html = util.insertInputBox(html,
                                           attribute.getFriendlyName(TRANSLATOR_NAME),
                                           attribute.getName(TRANSLATOR_NAME),
                                           "4",
                                           notNull=attribute.isRequired())
            elif type == "name":
                html = util.insertInputBox(html,
                                           attribute.getFriendlyName(TRANSLATOR_NAME),
                                           attribute.getName(TRANSLATOR_NAME),
                                           "31",
                                           "31",
                                           notNull=attribute.isRequired())
            #Process Text
            elif type == "text":
                html = util.insertTextBox(html,
                                          attribute.getFriendlyName(TRANSLATOR_NAME),
                                          attribute.getName(TRANSLATOR_NAME),
                                          notNull=attribute.isRequired())
            #Process Variable Characters
            elif PymeraseType.isVarchar(type):
                html = util.insertInputBox(html,
                                           attribute.getFriendlyName(TRANSLATOR_NAME),
                                           attribute.getName(TRANSLATOR_NAME),
                                           "30",
                                           PymeraseType.getVarcharLen(type),
                                           notNull=attribute.isRequired())
            #Process Characters
            elif PymeraseType.isChar(type):
                html = util.insertInputBox(html,
                                           attribute.getFriendlyName(TRANSLATOR_NAME),
                                           attribute.getName(TRANSLATOR_NAME),
                                           PymeraseType.getVarcharLen(type),
                                           PymeraseType.getVarcharLen(type),
                                           notNull=attribute.isRequired())
            #Process Boolean
            elif type == "boolean":
                html = util.insertBooleanRadio(html, attribute.getName(TRANSLATOR_NAME))
                                           
            #Process Time Stamps
            elif type == "timestamp with time zone":
                html = util.insertDatetime(html,
                                           attribute.getFriendlyName(TRANSLATOR_NAME),
                                           attribute.getName(TRANSLATOR_NAME),
                                           notNull=attribute.isRequired())
            #Write out what is not being handled.
            else:
                print "Table(%s), Type(%s), Attribute(%s) not processed." % \
                      (tbl.getName(TRANSLATOR_NAME),
                       type,
                       attribute.getName(TRANSLATOR_NAME))
                
        #Write html template to file
        util.saveHtml(html, filePath)

    print os.linesep \
          + "HTML Form Generation Complete... Good Bye." \
          + os.linesep
