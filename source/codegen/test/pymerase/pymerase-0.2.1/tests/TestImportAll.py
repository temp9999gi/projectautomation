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
import unittest
try:
  import unittestgui
except:
  pass

class TestImportAll(unittest.TestCase):

  def testPymerase(self):
    import pymerase

  def testInput(self):
    import pymerase.input

  def testOutput(self):
    import pymerase.output

  def testInputParseGenexSchemaXML(self):
    from pymerase.input import parseGenexSchemaXML

  def testInputParseXMI(self):
    from pymerase.input import parseXMI
    
  def testOutputCreateDBAPI(self):
    from pymerase.output import CreateDBAPI

  #Abandoned code, fails
  #def testOutputCreateDBEditor(self):
  #  from pymerase.output import CreateDBEditor

  def testOutputCreateGraphvizUML(self):
    from pymerase.output import CreateGraphvizUML

  #Abandoned code, fails
  #def testOutputCreateHtmlForms(self):
  #  from pymerase.output import CreateHtmlForms

  def testOuputCreatePyTkDBWidgets(self):
    from pymerase.output import CreatePyTkDBWidgets

  def testOutputCreatePyTkWidgets(self):
    from pymerase.output import CreatePyTkWidgets

  def testOutputCreatePythonAPI(self):
    from pymerase.output import CreatePythonAPI

  def testOutputCreateReport(self):
    from pymerase.output import CreateReport

  def testOutputCreateSQL(self):
    from pymerase.output import CreateSQL

  def testOutputCreateTableXML(self):
    from pymerase.output import CreateTableXML

  def testOuputIPymerase(self):
    from pymerase.output import iPymerase

  def testUtil(self):
    import pymerase.util

  def testUtilSortMetaInfo(self):
    from pymerase.util import SortMetaInfo

  def testUtilNameMangling(self):
    from pymerase.util import NameMangling

  def testUtilPymeraseType(self):
    from pymerase.util import PymeraseType

  def testUtilWarnings(self):
    from pymerase.util import Warnings

  def testUtilBool(self):
    from pymerase.util import bool

  def testUtilFkUtil(self):
    from pymerase.util import fk_util

  def testUtilIPymeraseUtil(self):
    from pymerase.util import iPymeraseUtil

  def testUtilOutput(self):
    from pymerase.util import output

  def testUtilXorString(self):
    from pymerase.util import xor_string

  def testOutputDBAPI(self):
    import pymerase.output.dbAPI

  #bool.py gets copied to new location after generation, fail ok
  #def testOutputDBAPIdbAPI(self):
  #  from pymerase.output.dbAPI import dbAPI

  def testOutputDBAPIfkeyTypes(self):
    from pymerase.output.dbAPI import fkeyTypes

  #is template, fails like it should, fail ok
  #def testOutputDBAPIinit(self):
  #  from pymerase.output.dbAPI import init

  def testOutputPyTkWidgets(self):
    import pymerase.output.PyTkWidgets

  def testOutputPyTkWidgetsHelperUtil(self):
    from pymerase.output.PyTkWidgets import HelperUtil

  def testOutputPyTkWidgetsTemplates(self):
    from pymerase.output.PyTkWidgets import Templates

  def testOuputPythonAPI(self):
    import pymerase.output.PythonAPI

  def testOutputPythonAPIapi(self):
    from pymerase.output.PythonAPI import API

  def testOutputPythonAPIfkeyTypes(self):
    from pymerase.output.PythonAPI import fkeyTypes

  #Is template, fails like it should, fail ok
  #def testOutputPythonAPIinit(self):
  #  from pymerase.output.PythonAPI import init

def suite():
  suite = unittest.makeSuite(TestImportAll, 'test')
  return suite

if __name__ == '__main__':
  try:
    unittestgui.main(initialTestName='TestImportAll')
  except:
    unittest.main()
