#!/usr/bin/env python
from __future__ import nested_scopes
import copy
import os
import re
import string
import sys
import unittest

import pymerase                
from pymerase.util import NameMangling

# import code to use api
from mx import DateTime

class CreatePubMedTestCases(unittest.TestCase):
  def __init__(self, name):
    """Initialize
    """
    self.pubmed_dir = os.path.join(os.getcwd(), "../examples/ncbi")

    unittest.TestCase.__init__(self, name)
    
  def setUp(self):
    """Perform setup
    """
    self.current_dir = os.getcwd()
    os.chdir(self.pubmed_dir)
    self.current_python_path = sys.path
    sys.path.append(self.pubmed_dir)

  def tearDown(self):
    """Clean up after ourselves. 
    """
    os.chdir(self.current_dir)
    sys.path = self.current_python_path
    
  def testParseUML(self):
    """Test generating python code from xmi file
    """
    # Figure out path information
    schema = os.path.abspath("pubmed.xmi")

    # construct pymerase object
    translator = pymerase.Pymerase()

    # do the translation
    self.classesInModel = {}
    parsed_input = translator.read(schema, 'parseXMI', self.classesInModel)

    #Test construction of classes from association names.

    #association names were being used to do lookups in classesInModel instead of
    #the name of the class pointed to be the associations. 

    #tests bug #749853
    self.failUnless(len(self.classesInModel) == 2)
    
def suite():
  suite = unittest.TestSuite()

  # run through test twice once for underscore_api and once for CapsAPI
  suite.addTest(CreatePubMedTestCases("testParseUML"))

  return suite

if __name__ == "__main__":
  unittest.main(defaultTest="suite")
