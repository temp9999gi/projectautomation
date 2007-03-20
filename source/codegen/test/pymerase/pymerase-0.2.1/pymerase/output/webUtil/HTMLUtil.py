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

#FIXME: Clean up code and document better

import re
import string
import os
import time


class HTMLUtil:
    """
    HTML Utilities for retrieving different html code elements.
    """

    def __init__(self):
        """
        Sets default input information.
        """
        self.DEFAULT_IB_SIZE = "30"
        self.DEFAULT_TB_ROWS = "6"
        self.DEFAULT_TB_COLS = "72"

        

    def getHeader(self):
        """
        Get the content type header for html
        """
        return "Content-type: text/html" + os.linesep



    def getHtmlTemplate(self, filename, template_loc):
        """
        Given Template file name, returns html
        """
               
        filePath = os.path.join(template_loc, filename)
        if os.path.isfile(filePath):
            template = open(filePath, 'r')
            html = template.read()
            template.close()
        else:
            msg = "%s is not valid." % (filePath)
            raise ValueError, msg

        return html


    def getDateTimeStr(self, mxDatetime):
        """
        Given a datetime object.

        return string formated 'YYYY-MM-DD HH:MM:SS.SS'
        """
        year, month, day, hour, minute, second, temp, temp, temp = mxDatetime.tuple()
        del temp
        if len(str(month)) == 1:
            month = "0" + str(month)
        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(hour)) == 1:
            hour = "0" + str(hour)
        if len(str(minute)) == 1:
            minute = "0" + str(minute)
            
        if str(second)[1] == '.':
            timeText = str(year) + "-" \
                   + str(month) + "-" \
                   + str(day) + " " \
                   + str(hour) + ":" \
                   + str(minute) + ":" \
                   + str(second)[:4]
        else:
            timeText = str(year) + "-" \
                   + str(month) + "-" \
                   + str(day) + " " \
                   + str(hour) + ":" \
                   + str(minute) + ":" \
                   + str(second)[:5]
            
        return timeText
        


    def insertTitle(self, html, title):
        """
        Given a title and html template to insert into... insert title.
        """
        try:
            html = re.sub('<!--TITLE-->', title, html)
            return html
        except:
            #FIXME: Need better error handling
            print "Error! Title Insert Failed"

    def insertHandler(self, html, handler):
        """
        Inserts handler into form
        """
        try:
            html = re.sub('<!--INSERT_HANDLER-->', handler, html)
            return html
        except:
            #FIXME: Need better error handling
            print "Error! Handler Insert Failed"

    def insertScriptName(self, html, scriptName):
        """
        Given a title and html template to insert into... insert title.
        """
        try:
            html = re.sub('<!--SCRIPTNAME-->', scriptName, html)
            return html
        except:
            #FIXME: Need better error handling
            print "Error! Script Name Insert Failed"


    def insertInputBox(self,
                       html,
                       text,
                       name,
                       size = None,
                       maxlength = None,
                       value = None,
                       notNull = 0):
        """
        Inserts InputBox into html and returns html

        Looks like:
        Input Box:<input type=\"text\" name=\"name\" size=\"25\" maxlength=\"25\"><br>
        """
        if notNull == 0:
            iBoxHtml = "%s:" % (text)
        else:
            iBoxHtml = "<font color=\"#FF0000\">%s:</font>" % (text)
        iBoxHtml += "<input type=\"text\" "
        iBoxHtml += "name=\"%s\" " % (name)

        if value != None:
            iBoxHtml += "value=\"%s\" " % (value)
        else:
            iBoxHtml += "value=\"\" "
        
        if size != None:
            iBoxHtml += "size=\"%s\" " % (size)
        else:
            iBoxHtml += "size=\"%s\" " % (self.DEFAULT_IB_SIZE)

        if maxlength != None:
            iBoxHtml += "maxlength=\"%s\" " % (maxlength)

        iBoxHtml = string.rstrip(iBoxHtml)

        iBoxHtml += "><br>" + os.linesep
        iBoxHtml += "<!--INSERT_FORM_HERE-->"

        html = re.sub("<!--INSERT_FORM_HERE-->", iBoxHtml, html)

        return html


    def getHiddenInputBox(self, text, name, value, notNull = 0):
        """
        Inserts InputBox into html and returns html

        Looks like:
        Input Box:<input type=\"hidden\" name=\"name\" value=\"foo\"><br>
        """
        if notNull == 0:
            iBoxHtml = "%s" % (text)
        else:
            iBoxHtml = "<font color=\"#FF0000\">%s:</font>" % (text)
        iBoxHtml += "<input type=\"hidden\" "
        iBoxHtml += "name=\"%s\" " % (name)
        iBoxHtml += "value=\"%s\" " % (value)
        iBoxHtml += ">"
        iBoxHtml += os.linesep

        return iBoxHtml


    def insertTextBox(self,
                      html,
                      text,
                      name,
                      rows = None,
                      cols = None,
                      notNull = 0):
        """
        Inserts TextBox into html and returns html

        Looks like:
        Text:<br>
        <textarea name=\"textArea\" rows=\"6\" cols=\"72\"></textarea><br>
        """
        if notNull == 0:
            tBoxHtml = "%s:<br>" % (text)
            tBoxHtml += os.linesep
        else:
            tBoxHtml = "<font color=\"#FF0000\">%s:</font><br>" % (text)
            tBoxHtml += os.linesep

        tBoxHtml += "<textarea name=\"%s\" " % (name)

        if rows != None:
            tBoxHtml += "rows=\"%s\" " % (rows)
        else:
            tBoxHtml += "rows=\"%s\" " % (self.DEFAULT_TB_ROWS)
            
        
        if cols != None:
            tBoxHtml += "cols=\"%s\" " % (cols)
        else:
            tBoxHtml += "cols=\"%s\" " % (self.DEFAULT_TB_COLS)

        tBoxHtml = string.rstrip(tBoxHtml)

        tBoxHtml += ">"

        tBoxHtml += "</textarea><br>"
        tBoxHtml += os.linesep
        tBoxHtml += "<!--INSERT_FORM_HERE-->"

        html = re.sub("<!--INSERT_FORM_HERE-->", tBoxHtml, html)

        return html


    def insertComment(self, html, comment, notNull = 0):
        """
        Inserts <!--Comment--> into html

        returns html
        """
        if notNull == 0:
            commentHtml = "<!--%s-->" % (comment)
            commentHtml += os.linesep
            commentHtml += "<!--INSERT_FORM_HERE-->"
        else:
            commentHtml = "<font color=\"#FF0000\"><!--%s--></font>" \
                          % (comment)
            commentHtml += os.linesep
            commentHtml += "<!--INSERT_FORM_HERE-->"
            
        html = re.sub("<!--INSERT_FORM_HERE-->", commentHtml, html)

        return html


    def insertMenuList(self, html,
                       text, name,
                       nameList, labelList,
                       valueList, selected = None,
                       notNull = 0):
        
        if len(nameList) == len(labelList) and len(nameList) == len(valueList):
            length = len(nameList)

            if notNull == 0:
                menuHtml = "%s:<select name=\"%s\" size=\"1\">" %\
                           (text, name)
                menuHtml += os.linesep
            else:
                menuHtml = "<font color=\"#FF0000\">%s:</font>"\
                           "<select name=\"%s\" size=\"1\">" % (text, name)
                menuHtml += os.linesep

            for x in range(0,length):
                if str(labelList[x]) == str(selected):
                    menuHtml += "<option value=\"%s\" label=\"%s\" selected>%s</option>" % (str(valueList[x]), str(labelList[x]), str(nameList[x]))
                    menuHtml += os.linesep
                else:
                    menuHtml += "<option value=\"%s\" label=\"%s\">%s</option>" % (str(valueList[x]), str(labelList[x]), str(nameList[x]))
                    menuHtml += os.linesep
            menuHtml += "</select><br>"
            menuHtml += os.linesep
            menuHtml += "<!--INSERT_FORM_HERE-->"

            html = re.sub("<!--INSERT_FORM_HERE-->", menuHtml, html)
            
            return html
        else:
            raise ValueError, "Mismatch List Lengths"


    def insertBooleanRadio(self, html, name):
        """
        Inserts boolean radio buttons into html and returns html
        """
        boolHtml = "%s:  True:<input type=\"radio\" name=\"%s\" value=\"1\">  "\
                   "False:<input type=\"radio\" name=\"%s\" value=\"0\"><br>" \
                   % (name, name, name)
        boolHtml += os.linesep
        boolHtml += "<!--INSERT_FORM_HERE-->"

        return re.sub("<!--INSERT_FORM_HERE-->", boolHtml, html)
        

    def insertDatetimeList(self, html, text, name):
        """
        Inserts pull down list for date and time and returns html
        """
        MONTH = range(1,13)
        DAY = range(1,32)
        YEAR = range(1950, 2010)

        #Reverse the order of the list of years
        YEAR.reverse()
        
        #TEMPTIME = time.localtime()
        #curYear = TEMPTIME[0]

        #Add drop down list for month
        dtHtml = "%s:<select name=\"%s_month\" size=\"1\">" % (text, name)
        dtHtml += os.linesep
        dtHtml += "<option value=\"MM\" label=\"MM\" selected>MM</option>"
        dtHtml += os.linesep
        for mm in MONTH:
            dtHtml += "<option value=\"%s\" label=\"%s\">%s</option>" % (str(mm), str(mm), str(mm))
            dtHtml += os.linesep
        dtHtml += "</select>"
        dtHtml += os.linesep

        #Add drop down list for day
        dtHtml += "/<select name=\"%s_day\" size=\"1\">" % (name)
        dtHtml += os.linesep
        dtHtml += "<option value=\"DD\" label=\"DD\" selected>DD</option>"
        dtHtml += os.linesep
        for dd in DAY:
            dtHtml += "<option value=\"%s\" label=\"%s\">%s</option>" \
                      % (str(dd), str(dd), str(dd))
            dtHtml += os.linesep
        dtHtml += "</select>"
        dtHtml += os.linesep

        #Add drop down list for day
        dtHtml += "/<select name=\"%s_year\" size=\"1\">" % (name)
        dtHtml += os.linesep
        dtHtml += "<option value=\"YYYY\" label=\"YYYY\" selected>YYYY</option>"
        dtHtml += os.linesep
        for yyyy in YEAR:
            #if str(yyyy) == str(curYear):
            #    dtHtml += "<option value=\"%s\" label=\"%s\" selected>%s</option>" % (str(yyyy), str(yyyy), str(yyyy))
            #    dtHtml += os.linesep
            #else:
            dtHtml += "<option value=\"%s\" label=\"%s\">%s</option>" % (str(yyyy), str(yyyy), str(yyyy))
            dtHtml += os.linesep
        dtHtml += "</select><br>"
        dtHtml += os.linesep
        dtHtml += "<!--INSERT_FORM_HERE-->"
        
        html = re.sub("<!--INSERT_FORM_HERE-->", dtHtml, html)

        return html


    def insertDatetime(self, html, text, name, value = None, notNull=0):
        """
        Inserts pull down list for date and time and returns html
        """
        if notNull == 0:
            iBoxHtml = "%s:" % (text)
        else:
            iBoxHtml = "<font color=\"#FF0000\">%s</font>" % (text)
        iBoxHtml += "<input type=\"text\" "
        iBoxHtml += "name=\"%s\" " % (name)

        if value != None:
            iBoxHtml += "value=\"%s\" " % (value)
        else:
            iBoxHtml += "value=\"\" "
        
        iBoxHtml += "size=\"28\" "
        #iBoxHtml += "maxlength=\"28\" "

        iBoxHtml = string.rstrip(iBoxHtml)

        iBoxHtml += "> (YYYY-MM-DD HH:MM:SS.ss+08:00)<br>"
        iBoxHtml += os.linesep
        iBoxHtml += "<!--INSERT_FORM_HERE-->"

        html = re.sub("<!--INSERT_FORM_HERE-->", iBoxHtml, html)

        return html



    def DateErrorCheck(self, month, day):
        """
        Returns 1 if the day is valid for a particular month.
        Returns 0 if the day is invalid for a particular month.
        """

        validDays = [ None, range(1,32), range(1,29), range(1,32),
                  range(1,31), range(1,32), range(1,31),
                  range(1,32), range(1,32), range(1,31),
                  range(1,32), range(1,31), range(1,32)]

        if day in validDays[month]:
            return 1
        else:
            return 0


    def saveHtml(self, html, filename):
        """
        Save html to file
        """
        try:
            file = open(filename, 'w')
            file.write(html)
            file.close()
            return 1
        
        except:
            return 0


    def insertTableTitle(self, html, title):
        """
        Inserts Table Title into HTML template and returns HTML
        """
        return re.sub('<!--INSERT_TABLE_TITLE-->', title, html)


    def insertTableAttrib(self, html, field, link = None):
        """
        Inserts Attributes of Field in to HTML template and returns HTML.
        """

        if link is None:
            pyType = field.getType()
            insert = "%s ---  %s<br>" % (field.getName(), pyType.getSQLType())
            insert += os.linesep
            insert += "<!--INSERT_TABLE_ATTRIB-->"
        else:
            insert = "<a href=\"%s\">%s</a><br>" % (link, field.getName())
            insert += os.linesep
            insert += "<!--INSERT_TABLE_ATTRIB-->"

        return re.sub('<!--INSERT_TABLE_ATTRIB-->', insert, html)
    
    
    def getMenuInsert(self, tableName, mysession):
        """
        Inserts Button into Main Menu

        returns menuInsertHtml
        """
        menuInsert = ""
        menuInsert += "<form action=\"./%s_web.py\" method=\"POST\" enctype=\"multipart/form-data\">" \
                      % (tableName)
        menuInsert += "<input value=\"%s\" type=\"submit\" width=\"200\">" % (tableName)
        menuInsert += "<input type=\"hidden\" name=\"session\" value=\"%s\">" % (mysession.info['session'])
        menuInsert += "</form>"

        return menuInsert


    def printHeader(self):
        """
        Prints HTML Header.
        """
        print 'Content-type: text/html' + os.linesep + os.linesep


    def printReturnMainMenu(self, mysession):
        """
        Prints HTML to return to main menu
        """
        html = """
<form action=\"./MainMenu.py\" method=\"POST\">
  <input value=\"Return to Main Menu\" type=\"submit\">
  <input type=\"hidden\" name=\"session\" value=\"%s\">
</form>
        """ % (mysession.info['session'])
        print html

    def insertHtmlTitle(self, html, title):
        """
        Inserts title into html

        returns html
        """
        return re.sub('<!--TITLE-->', title, html)
