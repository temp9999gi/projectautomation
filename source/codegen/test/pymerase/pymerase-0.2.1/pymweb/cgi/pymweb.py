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

import pymerase
import os
import tempfile
import re
import glob
import cgi
import cgitb
cgitb.enable()

rev = "$Revision: 1.1 $"
rev = rev.replace('$Revision: ', '')
rev = rev.replace(' $', '')

VERSION = '0.%s' % (rev)

def getCompressionScript(dest, compress):
  if compress == 'Tar&Gzip':
    text = """#!/bin/bash
cd %s
if [ -e %s ] ; then
  tar cvzf %s.tar.gz %s > /dev/null
else
  cat %s.bs
fi
""" % (DIRPATH, dest, dest, dest, dest)
    
  elif compress == 'Zip':
    text = """#!/bin/bash
cd %s
if [ -e %s ] ; then
  zip -r %s.zip %s > /dev/null
else
  cat %s.bs
fi
""" % (DIRPATH, dest, dest, dest, dest)

  elif compress == 'None':
    return None
  
  else:
    raise ValueError, 'Compression type of %s is invalid.' % (compress)
    
  return text


def launchPymerase(input, output, schema, dest):
  import sys
  import os
  
  import pymerase
  
  schema = os.path.abspath(os.path.join(DIRPATH, schema))
  outputPath = os.path.abspath(os.path.join(DIRPATH, dest))
    
  pymerase.run(schema,
               input,
               outputPath,
               output)

  return 0


def getDecompress(fileName):
  text = """#!/bin/bash
tar xzf %s
""" % (fileName)

  return text


ROOTPATH = '/tmp/pymweb'
if not os.path.exists(ROOTPATH):
  os.mkdir(ROOTPATH)
  f = open(os.path.join(ROOTPATH, 'index.html'), 'w')
  f.write("Pymweb")
  f.close()

  f = open(os.path.abspath('table.dtd'), 'r')
  dtd = f.read()
  f.close()

  f = open(os.path.join(ROOTPATH, 'table.dtd'), 'w')
  f.write(dtd)
  f.close()
  
tempfile.tempdir = ROOTPATH
DIRPATH = tempfile.mktemp()
mydir, sessionDir = os.path.split(DIRPATH)
os.mkdir(DIRPATH)
os.chmod(DIRPATH, 0775)


def processSchemaXML(schemaPath):
  obj = re.compile('SYSTEM \".*\"')

  xmlSearch = os.path.join(schemaPath[:-7], '*.xml')
  fileList = glob.glob(xmlSearch)

  for file in fileList:
    f = open(file, 'r')
    xmlFile = f.read()
    f.close()

    xmlFile = obj.sub('SYSTEM \"http://localhost/table.dtd\"', xmlFile)

    f = open(file, 'w')
    f.write(xmlFile)
    f.close()
  

def saveFile(fileName, file):

  filePath = os.path.join(DIRPATH, fileName)

  f = open(filePath, 'w')
  f.write(file)
  f.close()

  if fileName[-7:] == '.tar.gz':
    curPath = os.getcwd()
    os.chdir(DIRPATH)
    
    untarPath = os.path.join(DIRPATH, 'untar.sh')

    f = open(untarPath, 'w')
    f.write(getDecompress(fileName))
    f.close()

    os.chmod(untarPath, 0755)

    errCode = os.spawnl(os.P_WAIT, 'untar.sh', 'untar.sh')
    #print 'Decompress Exit Code: %s<br><br>' % \
    #      (errCode)
    if str(errCode) == '0':
      processSchemaXML(filePath)

    os.chdir(curPath)
  return filePath

def debug():
  print "---DEBUG---<br>"
  try:
    print "login: %s <br>" % (os.getlogin())
  except:
    pass
  print "CLASSPATH: %s <br>" % (os.getenv('CLASSPATH'))
  print "UID: %s <br>" % (os.geteuid())
  print "GID: %s <br>" % (os.getegid())
  print "---DEBUG---<br>"
  

def checkFileName(fileName):
  #Change windows linesep to linux linesep
  text = re.sub('\\\\', '/', fileName)
  path, file = os.path.split(text)

  return file


def checkSchema(fileName):
  if fileName[-7:] == '.tar.gz':
    fileName = fileName[:-7]
  
  if fileName == 'cmp.sh' \
     or fileName == 'index.html' \
     or fileName == 'untar.sh':
    return 0

  return 1

def checkDest(dest):
  block = ['\\', '/']

  for item in block:
    if item in dest:
      return 0

  if dest == 'cmp.sh' \
     or dest == 'index.html' \
     or dest == 'untar.sh':
    return 0

  return 1
  

if __name__ == '__main__':
  html = ""
  text = "Content-Type: text/html\n\n"
  print text
  #html += text

  text = "<img src=\"/images/pymerase-title.jpg\" alt=\"Pymerase\"><br>\n"
  print text
  html += text

  text = "Pymerase %s<br>\n" % (pymerase.VERSION)
  text += "Pymweb v%s<br><br>\n\n" % (VERSION)
  print text
  html += text

  text = "<b>Report Bug:</b> <a href=\"http://sourceforge.net/tracker/?atid=505345&group_id=63836&func=browse\">click here</a><br>\n"
  print text
  html += text

  text = "<b>Support Request:</b> <a href=\"http://sourceforge.net/tracker/?group_id=63836&atid=505346\">click here</a><br>\n"
  print text
  html += text

  text = "<b>Feature Request:</b> <a href=\"http://sourceforge.net/tracker/?group_id=63836&atid=505348\">click here</a><br>\n"
  print text
  html += text

  text = "<b>Patches:</b> <a href=\"http://sourceforge.net/tracker/?group_id=63836&atid=505347\">click here</a><br>\n"
  print text
  html += text

  text = "<b>Mailing Lists:</b> <a href=\"http://sourceforge.net/mail/?group_id=63836\">click here</a><br><br>\n\n"
  print text
  html += text
  
  form = cgi.FieldStorage()
  
  #for item in form.keys():
  #  print form[item], "<br>"

  if form.has_key('schema'):
    file = form['schema']
    #print 'File:', file.filename, '<br>'

    fileName = file.filename
    fileName = checkFileName(fileName)

    if checkSchema(fileName) != 1:
      text = 'File name %s invalid! File already exists.<br>\n' % (fileName)
      print text
      raise ValueError, text
    
    saved = saveFile(fileName, file.file.read())  

    #print 'File %s saved.<br><br>' % (saved)

    text = '<b>Session:</b> <a href="/pymweb/%s/">%s</a><br>\n' % \
           (sessionDir, sessionDir)
    print text
    html += text

    input = form['input'].value
    output = form['output'].value
    dest = form['dest'].value
    compression = form['compression'].value

    text = '<b>Input:</b> %s<br>\n' % (input)
    print text
    html += text

    text = '<b>Output:</b> %s<br>\n' % (output)
    print text
    html += text

    text = '<b>Schema:</b> %s<br>\n' % (fileName)
    print text
    html += text

    if fileName[-7:] == '.tar.gz':
      uploadedFile = fileName
      fileName = fileName[:-7]

      if os.path.isdir(os.path.join(DIRPATH, fileName)):
        #tar xvzf fileName worked
        pass
      else:
        text = "Error: %s does not exist, is %s a valid file?<br>" % \
               (fileName, uploadedFile)
        print text
        raise ValueError, text

    text = '<b>Destination:</b> %s<br>\n' % (dest)
    print text
    html += text

    if checkDest(dest) == 1:
      pass
    else:
      text = "<b>Error: Destination %s Invalid!</b><br>" % (dest)
      print text
      raise ValueError, text

    text = '<b>Compression:</b> %s<br>\n' % (compression)
    print text
    html += text

    text = '<br>\n'
    print text
    html += text

    ##############################
    # Launch Pymerase
    ##############################
    rv = launchPymerase(input, output, fileName, dest)

    if rv != 0:
      raise ValueError, 'Pymweb broke badly'

    ##############################
    # Compress Output if Requested
    ##############################
    compressScript = getCompressionScript(dest, compression)

    if compressScript is not None:
      cmpScriptPath = saveFile('cmp.sh', compressScript)
      fullCmpPath = os.path.join(DIRPATH, cmpScriptPath)
      os.chmod(fullCmpPath, 0755)
      text = os.spawnl(os.P_WAIT, fullCmpPath, fullCmpPath)
    else:
      #compress type is None, don't compress
      text = 0
    
    if str(text) != '0':
      text = 'ERROR, exit code %s<br>\n' % (text)
      print text
      html += text

      text = 'E-mail pymerase-devel at lists.sourceforge.net for help.<br>'
      print text
      html += text
    else:
      text = '<b>Generation Complete</b><br>'
      print text
      html += text

      if compression == 'Tar&Gzip':
        text = 'Download: <a href="/pymweb/%s/%s.tar.gz">%s.tar.gz</a>' % \
               (sessionDir, dest, dest)
        print text
        html += text
        
      elif compression == 'Zip':
        text = 'Download: <a href="/pymweb/%s/%s.zip">%s.zip</a>' % \
               (sessionDir, dest, dest)
        print text
        html += text
      elif compression == 'None':
        text = 'Download: <a href="/pymweb/%s/%s">%s</a>' % \
               (sessionDir, dest, dest)
        print text
        html += text
      else:
        raise ValueError, '%s invalid compression type!' % (compression)
    htmlFile = open(os.path.join(DIRPATH, 'index.html'), 'w')
    htmlFile.write(html)
    htmlFile.close()
