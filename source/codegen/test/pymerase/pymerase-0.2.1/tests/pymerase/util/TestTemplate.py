#!/usr/bin/env python
import string
import re
import unittest

from pymerase.util.Template import Template

class TestTemplate(Template):
  def __init__(self, namespace=None):
    # define modules we want access to
    self.string = string
    self.re = re
    self.testParameter = "class"
    self.listParameter = ['hello','earth']
    # call after we set up our namespace
    super(TestTemplate, self).__init__(namespace)
    
  def simple(self):
    return "simple"

  def parameter(self, x):
    return "%s" % (x)

testParameter = "global"

class TemplateTestCases(unittest.TestCase):
  def testKeys(self):
    tt = TestTemplate()
    keys = tt.keys()
    self.failUnless(len(keys) == 2)
    self.failUnless('simple' in keys)
    self.failUnless('parameter' in keys)
    
  def testSimple(self):
    tt = TestTemplate()
    result = "%(simple())s" % (tt)
    self.failUnless(result == "simple")

  def testParameterGlobal(self):
    tt = TestTemplate(globals())
    result = "%(parameter(testParameter))s" % (tt)
    self.failUnless(result == "global", result)

  def testParameterClass(self):
    tt = TestTemplate()
    result = "%(parameter(testParameter))s" % (tt)
    self.failUnless(result == "class")

  def testParameterOther(self):
    d = {'testParameter': 'local'}
    tt = TestTemplate(d)
    result = "%(parameter(testParameter))s" % (tt)
    self.failUnless(result == "local")

  def testExpression(self):
    """Test expression using manually constructed namespace
    """
    import string
    d = {'l': ['hello', 'world'],
         'string': string}
    tt = TestTemplate(d)
    result = "%(string.join(map(parameter,l)))s" % (tt)
    self.failUnless(result == "hello world", "result was %s" % (result))

  def testExpressionClass(self):
    """Test expression using namespace inherited from the Template class
    """
    tt = TestTemplate()
    result = "%(string.join(map(parameter,listParameter)))s" % (tt)
    self.failUnless(result == "hello earth", "result was %s" % (result))

def suite():
  return unittest.defaultTestLoader.loadTestsFromTestCase(TemplateTestCases)

if __name__ == "__main__":
  unittest.main(defaultTest="suite")
