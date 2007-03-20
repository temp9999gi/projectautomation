#!/usr/bin/env python
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
#



import os
import sys
import getopt
import re

from LinkAPI import DBSession

def parseCommandLine():
  """
  Processes Command Line Arguments

  return (groupName, fileName, dsn, database, user, password)
  """

  #Set default values for command line
  groupName = None
  fileName = None
  dsn = "localhost"
  database = "linkdb"
  try:
    user = os.environ["USERNAME"]
  except:
    user = None
  password = None
  
  try:
    #define command line args
    opts, args = getopt.getopt(sys.argv[1:], "h:d:u:p:g:f:",
                               ["host",
                                "database=",
                                "user=",
                                "password=",
                                "group=",
                                "file=",
                                "help"])
  except getopt.GetoptError:
    print "-------------------------------"
    print "- Invalid Command Line Option -"
    print "-------------------------------"
    printUseage()
    sys.exit(2)
  
  if len(sys.argv) <= 1:
    printUseage()
    sys.exit(2)

  for arg, val in opts:

    #Display Help
    if arg in ('--help', '--help'):
      printUseage()
      sys.exit()

    #Set the group name to use when accessing the database
    if arg in ('-g', '--group'):
      groupName = val

    #Set files name to use
    if arg in ('-f', '--file'):
      fileName = val

    #host to connect to. Default = localhost
    if arg in ('-h', '--host'):
      dsn = val

    #name of database. Default = linkdb
    if arg in ('-d', '--database'):
      database = val

    #user name. Default = $USERNAME environment var
    if arg in ('-u', '--user'):
      user = val

    #password. Default = None
    if arg in ('-p', '--password'):
      password = val

  msg = ""
  if groupName is None:
    msg += "Error: No group provided"
    msg += os.linesep
  if fileName is None:
    msg += "Error: No file provided"
    msg += os.linesep
  if msg != "":
    msg += "Suggestion: see \'linker.py --help\'"
    msg += os.linesep
    print msg
    sys.exit(2)


  return (groupName, fileName, dsn, database, user, password)

def printUseage():
  """
  Prints the useage information
  """
  useage = """
  Linker.py:
    Looks for names in an html file that matches the database
    and replaces them with a link.
  
  Useage:
    linker.py [options] -g group -f file
  
    linker.py [options] --group=group --file=file


  Options:
    -h, --host=foo       Name of host. Default: localhost
    -d, --database=foo   Name of database. Default: linkdb
    -u, --user=foo       User login for DB. Default: $USERNAME
    -p, --password=foo   User password for DB. Default: None
  
    -g, --group=foo      Name of group to use for processing
    -f, --file=foo       File to be processed

    -h, --help           Displays this help page

  """
  
  print useage

def getFileData(fileName):
  """
  opens file if exists
  returns data
  """
  
  if os.path.isfile(fileName):
    f = open(fileName, 'r')
    data = f.read()
    f.close()
    return data
  else:
    "Invalid file name \"%s\"" % (fileName)
    return None


if __name__ == '__main__':
  #retrive command line arguments if valid
  groupName, fileName, dsn, database, user, password = parseCommandLine()

  #set fileName to absolute path
  fileName = os.path.abspath(fileName)

  #Connects, or dies... Good luck!
  dbs = DBSession(dsn=dsn, database=database, user=user, password=password)

  #get the group object with a given name
  # this allows you to sort your links in groups
  groupList = dbs.getObjectsWhere(dbs.Group, 'name = \'%s\'' % (groupName))

  #If you entered a name that doesn't exist (CASE sensitive),
  # the program quits
  if len(groupList) == 0:
    print "Group \"%s\" not found" % (groupName)
    sys.exit()

  #If one group exists 
  if len(groupList) == 1:
    #get the group
    group = groupList.pop()
    #get all the links in the group
    linkerList = group.getNameLinkPair()

    #get the html file in string form for processing
    fileData = getFileData(fileName)

    #save a backup copy of the file as fileName.bak
    f = open(fileName + '.bak', 'w')
    f.write(fileData)
    f.close()

    
    print "Processing Links:"
    for nameLink in linkerList:
      name = nameLink.getName()
      url = nameLink.getUrl()

      print "%s\t%s" % (name, url)

      #replace keyword with link using regexp
      fileData = re.sub(name+"(?!</a>)", "<a href=\"%s\">%s</a>" % \
                        (url,name),
                        fileData)

    #save html file
    f = open(fileName, 'w')
    f.write(fileData)
    f.close()
    
  else:
    print "%s groups with name %s!" % (len(groupList), groupName)
    sys.exit()
