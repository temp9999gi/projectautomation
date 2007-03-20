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
#        Author: Brandon King
#           URL: http://pymerase.sourceforge.net
# Last Modified: $Date: 2006/12/18 15:54:02 $
#
import Tkinter
from dbSession import sessionObj

class NavBar(Tkinter.Frame):

  def __init__(self, root=None,
               EntryWidget=None,
               dbObj=None,
               session=None,
               buttonFG='white',
               buttonBG='blue',
               **kw):
    Tkinter.Frame.__init__(self, root, kw)

    self.parent = root

    self.can = Tkinter.Canvas(self, width=300, height=30)
    self.can.pack()

    self.entryWidget = EntryWidget
    self.dbObj = dbObj
    
    self.navList = []
    self.navIndex = None

    #First Record Button
    self.StartButton = Tkinter.Button(self,
                                      text="| <<",
                                      fg=buttonFG,
                                      bg=buttonBG,
                                      command=self.moveFirst)
    self.can.create_window(25,15,window=self.StartButton)

    #Previous Record Button
    self.PrevButton = Tkinter.Button(self,
                                     text="| <",
                                     fg=buttonFG,
                                     bg=buttonBG,
                                     command=self.movePrev)
    self.can.create_window(70,15,window=self.PrevButton)

    #Next Record Button
    self.NextButton = Tkinter.Button(self,
                                     text="> |",
                                     fg=buttonFG,
                                     bg=buttonBG,
                                     command=self.moveNext)
    self.can.create_window(190,15,window=self.NextButton)

    #Last Record Button
    self.EndButton = Tkinter.Button(self,
                                    text=">> |",
                                    fg=buttonFG,
                                    bg=buttonBG,
                                    command=self.moveLast)
    self.can.create_window(235,15,window=self.EndButton)

    #New record button
    self.NewButton = Tkinter.Button(self,
                                    text="> *",
                                    fg=buttonFG,
                                    bg=buttonBG,
                                    command=self.newRecord)
    self.can.create_window(280,15,window=self.NewButton)

    #Current Record
    self.recordIndicator = Tkinter.Message(self,
                                           text="0 of 0",
                                           relief=Tkinter.SUNKEN)
    self.can.create_window(130,15,window=self.recordIndicator)

    if session is None:
      self.session = sessionObj(self.parent)
    else:
      self.session = session
    self.updateNavListFromDB()

  def updateNavListFromDB(self):
    dbs = self.session.getDbs()
    self.navList = dbs.getAllObjects(self.dbObj)
    if len(self.navList) >= 1 and self.navIndex is None:
      self.moveFirst()
    elif len(self.navList) == 0:
      print "No records in database..."
      self.newRecord()

  def loadCurrentNav(self):
    self.entryWidget.load(self.navList[self.navIndex])

  def updateRecordIndicator(self):
    if self.navIndex is not None and \
       self.navList is not None and \
       len(self.navList) >= 1:
      newText = "%s of %s" % (self.navIndex + 1, len(self.navList))
      self.recordIndicator['text'] = newText

  def moveFirst(self):
    print "Moving to first record"
    if self.navList is not None and len(self.navList) >= 1:
      self.navIndex = 0
      self.loadCurrentNav()
      self.updateRecordIndicator()

  def moveLast(self):
    print "Moving to last record"
    if self.navList is not None and len(self.navList) >= 1:
      self.navIndex = len(self.navList) - 1
      self.loadCurrentNav()
      self.updateRecordIndicator()

  def moveNext(self):
    print "Moving to next record"
    if self.navList is not None and len(self.navList) >=1:
      if (self.navIndex + 1) < len(self.navList):
        self.navIndex += 1
      self.loadCurrentNav()
      self.updateRecordIndicator()

  def movePrev(self):
    print "Moving to prev record"
    if self.navList is not None and len(self.navList) >=1:
      if (self.navIndex + 1) <= len(self.navList) and \
         self.navIndex > 0:
        self.navIndex -= 1
      self.loadCurrentNav()
      self.updateRecordIndicator()

  def newRecord(self):
    if self.dbObj is not None:
      print "Creating new record"
      self.appendNavItem(self.dbObj())
      self.moveLast()
      self.updateRecordIndicator()
    else:
      print "No dbObj defined"

  def setNavList(self, list):
    self.navList = list

  def getNavList(self):
    return self.navList

  def appendNavItem(self, item):
    self.navList.append(item)

  def deleteNavItem(self, item):
    self.navList.remove(item)
