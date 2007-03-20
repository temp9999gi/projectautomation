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
"""
NOTE: Configure config.py before running this setup script
"""

import os
import re
import config

def main():
  #Get list of files in directory
  fileList = os.listdir('.')
  filteredList = []

  #Filter for only files with _web.py at the end of the name
  print 'Collecting files for processing:'
  for fileName in fileList:
    if fileName[-7:] == '_web.py':
      print fileName, 'added to list.'
      #Add to filtered list
      filteredList.append(fileName)

  #Configure each of the files in the filtered list
  for fileName in filteredList:
    print 'Processing %s now...' % (fileName)

    #setup script needs to be run in the same directory as the files
    filePath = os.path.join(os.path.abspath('.'), fileName)

    #Make the file executable
    os.chmod(filePath, 0755)

    #Open file for configuration
    f = open(filePath, 'r')
    file = f.read()
    f.close()

    #Substitue the DBAPI name given in the config.py file
    file = re.sub('#--DBAPI--#', config.DBAPI_NAME, file)

    #Write and close the file
    f = open(filePath, 'w')
    f.write(file)
    f.close()

  print 'Processing MainMenu.py...'
  mainMenuPath = os.path.join(os.path.abspath('.'), 'MainMenu.py')

  #Open and read MainMenu.py
  mainFile = open(mainMenuPath, 'r')
  mainMenu = mainFile.read()
  mainFile.close()

  #Replace string '#--DBAPI--# with the name of users DBAPI
  mainMenu = re.sub('#--DBAPI--#', config.DBAPI_NAME, mainMenu)

  #Save MainMenu.py with DBAPI change
  mainFile = open(mainMenuPath, 'w')
  mainFile.write(mainMenu)
  mainFile.close()
  del mainMenu
  
  #Make the following files executable
  os.chmod(os.path.join(os.path.abspath('.'), 'MainMenu.py'), 0755)
  os.chmod(os.path.join(os.path.abspath('.'), 'login.py'), 0755)


if __name__ == '__main__':
  main()
