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
import re
from pymerase.util import xor_string

def makePackage(destination, webUtilPath):
    if os.path.isdir(destination):
        PATH = os.path.join(destination, 'myWebUtil')
        if not os.path.isdir(PATH):
            os.mkdir(PATH)
    else:
        print "Directory (%s) does not exist!" % (destination)
        sys.exit()

    if os.path.isdir(webUtilPath):
        fileList = os.listdir(webUtilPath)
    else:
        print "Directory (%s) does not exist!" % (webUtilPath)
        sys.exit()

    print ''

    templatePath = os.path.join(webUtilPath, 'templates')

    tempList = []
    ############################
    #Files to ignore during copy
    tempList.append('CodeUtil.py')
    ############################
    
    for x in fileList:
        #Remove self from list of files to copy
        if re.search('makePackage.py', x) is not None:
            tempList.append(x)
                
        #Remove all non python files from list
        if re.search('.py', x) is None:
            tempList.append(x)
                
        #Remove all .pyc files from list
        if re.search('.pyc', x) is not None:
            tempList.append(x)

        #Remove all .py~ files from list
        if re.search('.py~', x) is not None:
            tempList.append(x)

        #Remove anything with ~ in it
        if re.search('~', x) is not None:
            tempList.append(x)
        
    for z in tempList:
        for y in fileList:
            if z == y:
                fileList.remove(y)
                print y, 'removed.'

    print os.linesep + "Files to be copied:"
    for x in fileList:
        print x

    print 'Copying files...'
    for x in fileList:
        fileToCopy = os.path.join(webUtilPath, x)
        fileToSave = os.path.join(PATH, x)
        
        file = open(fileToCopy, 'r')
        newfile = open(fileToSave, 'w')

        newfile.write(file.read())

        file.close()
        newfile.close()

    #Coping xor_string util
    print "Copying xor_string..."
    xorStringName = xor_string.__file__
    xorFile = open(xorStringName, 'r')
    print "Copying from %s" % (os.path.abspath(xorStringName))
    xorFilePath, xorFileName = os.path.split(xorStringName)
    fileToSave = os.path.join(PATH, xorFileName)
    print "Saving to %s" % (os.path.abspath(fileToSave))
    destFile = open(fileToSave, 'w')
    destFile.write(xorFile.read())
    xorFile.close()
    destFile.close()
    print "Copy of xor_string complete."

    print "Copying login.html..."
    loginHtmlFile = getTemplate(templatePath, 'login.html')
    fileToSave = os.path.join(destination, 'login.html')
    htmlFile = open(fileToSave, 'w')
    htmlFile.write(loginHtmlFile)
    htmlFile.close()
    del loginHtmlFile
    print 'Copy of login.html complete.'
    
    print "Copying login.py..."
    loginPyFile = getTemplate(templatePath, 'login.py')
    fileToSave = os.path.join(destination, 'login.py')
    pyFile = open(fileToSave, 'w')
    pyFile.write(loginPyFile)
    pyFile.close()
    del loginPyFile
    print 'Copy of login.py complete.'

    print "Copying config.py..."
    configPyFile = getTemplate(templatePath, 'config.py')
    fileToSave = os.path.join(destination, 'config.py')
    pyFile = open(fileToSave, 'w')
    pyFile.write(configPyFile)
    pyFile.close()
    del configPyFile
    print 'Copy of config.py complete.'

    print "Copying setup.py..."
    setupFile = getTemplate(templatePath, 'setup.py')
    fileToSave = os.path.join(destination, 'setup.py')
    pyFile = open(fileToSave, 'w')
    pyFile.write(setupFile)
    pyFile.close()
    del setupFile
    os.chmod(fileToSave, 0755)
    print 'Copy of setup.sh complete.'

    print 'Done.' + os.linesep + os.linesep


def getTemplate(location, name):
    """
    retrives a template and returns it.
    """
    filepath = os.path.join(location, name)
    if os.path.isfile(filepath):
        
        file = open(filepath, 'r')
        template = file.read()
        file.close()

        return template
    
    else:
        return None
