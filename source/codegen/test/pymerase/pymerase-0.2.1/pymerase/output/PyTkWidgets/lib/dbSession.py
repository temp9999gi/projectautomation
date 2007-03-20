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
import tkMessageBox
import sys
import os
import ConfigParser

from %DBAPI% import DBSession

class dbConnect:
  """
  Class used to create a connection to the database (used by sessionObj)
  """
  def __init__(self,
               master,
               dsn=None,
               database=None,
               user=None,
               password=None):

    self.parent = master

    self.dbs = None

    self.dsn = dsn
    self.database = database
    self.user = user
    self.password = password

    self.__readConfigFile()

    if self.dsn is None and \
       self.database is None and \
       self.user is None and \
       self.password is None:
      self.display()
    else:
      try:
        self.dbs = DBSession(self.dsn, self.database, self.user, self.password)
      except:
        self.getDbs()

  def __readConfigFile(self):
    """
    Retrives the following config file from the dir that the program
    was run from.

    [Connect]
    dsn: localhost
    database: someDb
    user: guest
    password: guest
    """
    CONNECT = 'Connect'
    
    parser = ConfigParser.ConfigParser()
    filePath = os.path.abspath('./db.cfg')

    if os.path.isfile(filePath):
      parser.read(filePath)

      #[Connect] Section
      if parser.has_section(CONNECT):
        #dsn option
        if parser.has_option(CONNECT, 'dsn'):
          dsn = parser.get(CONNECT, 'dsn')
          if dsn != "":
            self.dsn = dsn

        #database option
        if parser.has_option(CONNECT, 'database'):
          database = parser.get(CONNECT, 'database')
          if database != "":
            self.database = database

        #user option
        if parser.has_option(CONNECT, 'user'):
          user = parser.get(CONNECT, 'user')
          if user != "":
            self.user = user

        #password option
        if parser.has_option(CONNECT, 'password'):
          password = parser.get(CONNECT, 'password')
          if password != "":
            self.password = password

  def display(self):

    self.top = Tkinter.Toplevel(self.parent)
    self.top.title("Database Connection")
    
    self.HeaderFrame = Tkinter.Frame(self.top)
    self.BodyFrame = Tkinter.Frame(self.top)
    self.FooterFrame = Tkinter.Frame(self.top)

    self.HeaderFrame.grid(row=0)
    self.BodyFrame.grid(row=1)
    self.FooterFrame.grid(row=2)
    
    self.dsnLabel = Tkinter.Label(self.BodyFrame, text="Host:")
    self.dsnLabel.grid(row=0, column=0, sticky=Tkinter.E)
    self.dsnEntry = Tkinter.Entry(self.BodyFrame)
    self.dsnEntry.grid(row=0, column=1, sticky=Tkinter.W)

    if self.dsn is not None:
      self.dsnEntry.insert(0, self.dsn)

    self.databaseLabel = Tkinter.Label(self.BodyFrame, text="Database:")
    self.databaseLabel.grid(row=1, column=0, sticky=Tkinter.E)
    self.databaseEntry = Tkinter.Entry(self.BodyFrame)
    self.databaseEntry.grid(row=1, column=1, sticky=Tkinter.W)

    if self.database is not None:
      self.databaseEntry.insert(0, self.database)

    self.userLabel = Tkinter.Label(self.BodyFrame, text="User:")
    self.userLabel.grid(row=2, column=0, sticky=Tkinter.E)
    self.userEntry = Tkinter.Entry(self.BodyFrame)
    self.userEntry.grid(row=2, column=1, sticky=Tkinter.W)

    if self.user is not None:
      self.userEntry.insert(0, self.user)

    self.passwordLabel = Tkinter.Label(self.BodyFrame, text="Password:")
    self.passwordLabel.grid(row=3, column=0, sticky=Tkinter.E)
    self.passwordEntry = Tkinter.Entry(self.BodyFrame, show="*")
    self.passwordEntry.grid(row=3, column=1, sticky=Tkinter.W)

    if self.password is not None:
      self.passwordEntry.insert(0, self.password)

    self.ConnectButton = Tkinter.Button(self.FooterFrame,
                                        text="Connect",
                                        bg='blue',
                                        fg='white',
                                        command=self.connect)
    self.ConnectButton.grid(row=1)

    self.parent.wait_window(self.top)
    
  def getDsn(self):
    return self.dsnEntry.get()

  def getDatabase(self):
    return self.databaseEntry.get()

  def getUser(self):
    return self.userEntry.get()

  def getPassword(self):
    return self.passwordEntry.get()

  def connect(self):
    dsn = self.getDsn()
    db = self.getDatabase()
    user = self.getUser()
    password = self.getPassword()

    if dsn == "":
      dsn = None

    if db == "":
      db = None

    if user == "":
      user = None

    if password == "":
      password = None

    try:
      self.dbs = DBSession(dsn, db, user, password)
      print "Connected"
      self.top.destroy()
    except:
      tkMessageBox.showwarning("Warning", "Unable to connect")

  def getDbs(self):
    while self.dbs is None:
      try:
        self.display()
      except:
        sys.exit()
    return self.dbs
    
    
class sessionObj:
  """
  Session Object for Database Connection
  """
  
  def __init__(self, master):
    self.dbs = None
    self.parent = master

  def getDbs(self):
    if self.dbs is None:
      self.connect()
    return self.dbs

  def connect(self,
              dsn=None,
              database=None,
              user=None,
              password=None):
    dbCon = dbConnect(self.parent)
    self.dbs = dbCon.getDbs()

if __name__ == '__main__':
  root = Tkinter.Tk()
  root.title('Database Connect')
  l = Tkinter.Label(root, text="Database Connection Test")
  l.pack()
  session = sessionObj(root)
  print session.getDbs()
  root.mainloop()
