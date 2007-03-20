#!/usr/bin/env python2.2

from __future__ import nested_scopes
import copy
import os
import re
import string
import sys
import types
import unittest

import pymerase
from  pymerase import ClassMembers
import pymerase.util.PymeraseType
import pymerase.util.NameMangling


#from pymerase.util import NameMangling
TRANSLATOR=None
class ClassMemberTestCases(unittest.TestCase):

  def setUp(self):
    self.config = pymerase.PymeraseConfig()
    nullMangler = pymerase.util.NameMangling.nullMangler()
    self.config.setNameMangler(nullMangler)

  def tearDown(self):
    self.config = None
    
  def testModelElement(self):
    """Test all the various functions of the ModelElement class
    """
    # can we be named
    me = ClassMembers.ModelElement(self.config, "testModelElement")
    self.failUnless(me.getName(TRANSLATOR) == "testModelElement")
    
    # does the friendly name default properly?
    self.failUnless(me.getFriendlyName() == "testModelElement")
    me.setFriendlyName("test the model")
    self.failUnless(me.getFriendlyName() == "test the model")

    # get description
    me.setDescription("this is a description")
    self.failUnless(me.getDescription() == "this is a description")

    # also get a minor test of PymeraseType
    me.setType(pymerase.util.PymeraseType.PymeraseType('integer'))
    self.failUnless(me.getType().getPythonTypeStr() == 'types.IntType')

    # cannot set a uuid to none
    try:
      me.setUUID(None)
    except RuntimeError, e:
      pass
    else:
      self.fail("me.setUUID(None) didn't fail")

    # get uuid
    me.setUUID('12345')
    self.failUnless(me.getUUID()=='12345')

    # make sure location list is maintained correctly
    self.failUnless(len(me.getLocations())==0)
    me.appendLocation('testCaseMembers: line 1234')
    self.failUnless(me.getLocations()[0] == 'testCaseMembers: line 1234')

    # does isDefined have the correct default?
    self.failUnless(not me.getDefined())
    me.setDefined(1)
    self.failUnless(me.getDefined())

    # test naming utilities
    self.failUnless(me.getGetterName(TRANSLATOR) == 'gettestModelElement')
    self.failUnless(me.getSetterName(TRANSLATOR) == 'settestModelElement')
    self.failUnless(me.getAppenderName(TRANSLATOR) == 'appendtestModelElement')


  def testClassAttribute(self):
    """I bet you guessed this function tests the capabilities of ClassAttribute
    """
    ca = ClassMembers.ClassAttribute(self.config, "testClassAttribute")

    # isRequired test
    self.failUnless(not ca.isRequired())
    ca.setRequired(1)
    self.failUnless(ca.isRequired())

    # isUnique
    self.failUnless(not ca.isUnique())
    ca.setUnique(1)
    self.failUnless(ca.isUnique())

    # is indexed?
    self.failUnless(not ca.isIndexed())
    ca.setIndexed(1)
    self.failUnless(ca.isIndexed())

    # does isKey start as false?
    self.failUnless(not ca.isKey())

    # try setting as primary key
    self.failUnless(not ca.isPrimaryKey())
    ca.setPrimaryKey(1)
    self.failUnless(ca.isPrimaryKey())
    self.failUnless(ca.isKey())

    # can't be both primary and foreign key? (I don't know if that should be
    # true, but I decided to code that)
    try:
      ca.setForeignKey(1)
    except ValueError, e:
      pass
    else:
      self.fail("a key cannot be both a primary and foreign key")

    # reset primary key to false to test foreign key
    ca.setPrimaryKey(0)
    self.failUnless(not ca.isPrimaryKey())
    
    # test foreign key
    self.failUnless(not ca.isForeignKey())
    ca.setForeignKey(1)
    self.failUnless(ca.isKey())

    try:
      ca.setPrimaryKey(1)
    except ValueError, e:
      pass
    else:
      self.fail("a key cannot be both a primary and foreign key")

    # test accessors
    # default is public access
    self.failUnless(ca.isPublicAccess() and not ca.isProtectedAccess() and not ca.isPrivateAccess(), "default is public")
    ca.setProtectedAccess()
    self.failUnless(not ca.isPublicAccess() and ca.isProtectedAccess() and not ca.isPrivateAccess(), "should've been protected")
    ca.setPrivateAccess()
    self.failUnless(not ca.isPublicAccess() and not ca.isProtectedAccess() and ca.isPrivateAccess(), "should've been private")
    ca.setPublicAccess()
    self.failUnless(ca.isPublicAccess() and not ca.isProtectedAccess() and not ca.isPrivateAccess(), "should've been public")

    

  def testAssociationEnd(self):
    """Test parts of an AssociationEnd that doesn't depend on being in an Association
    """
    ae = ClassMembers.AssociationEnd(self.config, "testAssociationEnd")

    ae.setAttributeName('attribute')
    self.failUnless(ae.getAttributeName(TRANSLATOR) == 'attribute')

    cmi = ClassMembers.ClassMetaInfo(self.config, 'ClassMetaInfo')
    ae.setType(cmi)
    self.failUnless(ae.getType() == cmi)
    self.failUnless(ae.getClassName(TRANSLATOR) == 'ClassMetaInfo')

    self.failUnless(ae.getMultiplicity() is None)
    ae.setMultiplicity(1)
    self.failUnless(ae.getMultiplicity() == 1)

    self.failUnless(not ae.isNavigable())
    ae.setNavigable(1)
    self.failUnless(ae.isNavigable())

    self.failUnless(ae.getGetterName(TRANSLATOR) == 'gettestAssociationEnd')
    self.failUnless(ae.getSetterName(TRANSLATOR) == 'settestAssociationEnd')
    self.failUnless(ae.getAppenderName(TRANSLATOR) == 'appendtestAssociationEnd')


  def testAssociation(self):
    """Test Association and AssociationEnd components that work in an association
    """

    leftAE = ClassMembers.AssociationEnd(self.config, 'leftAssociationEnd')
    rightAE = ClassMembers.AssociationEnd(self.config, 'rightAssociationEnd')
    leftAE.setAttributeName('left')
    rightAE.setAttributeName('right')
    leftCMI = ClassMembers.ClassMetaInfo(self.config, 'leftCMI')
    rightCMI = ClassMembers.ClassMetaInfo(self.config, 'rightCMI')
    leftAE.setType(leftCMI)
    rightAE.setType(rightCMI)

    A = ClassMembers.createAssociation(self.config, leftAE, rightAE, "ends")

    self.failUnless(A.getName(TRANSLATOR) == "ends")
    self.failUnless(len(A) == 2)
    self.failUnless(leftAE.getAssociation() == A)
    self.failUnless(rightAE.getAssociation() == A)
    self.failUnless(leftAE.getOppositeEnd() == rightAE)
    self.failUnless(rightAE.getOppositeEnd() == leftAE)

    A.removeAssociationEnd(leftAE)
    A.removeAssociationEnd(rightAE)

    self.failUnless(len(A) == 0)
    self.failUnless(leftAE.getAssociation() is None)
    self.failUnless(rightAE.getAssociation() is None)

    # test name construction
    A = ClassMembers.createAssociation(self.config, leftAE, rightAE)

    self.failUnless(A.getName(TRANSLATOR) == 'leftAssociationEndrightAssociationEnd')

  def testClassMetaInfo(self):
    root1 = ClassMembers.ClassMetaInfo(self.config, "root1")
    root1Attrib = ClassMembers.ClassAttribute(self.config, 'root1Attrib')
    
    root2 = ClassMembers.ClassMetaInfo(self.config, "root2")
    root2Attrib = ClassMembers.ClassAttribute(self.config, 'root2Attrib')
    
    cmi = ClassMembers.ClassMetaInfo(self.config, "testClassMetaInfo")

    testPathname = "/a/b/c/d"
    testPath, testFilename = os.path.split(testPathname)
    cmi.setFilename(testPathname)

    self.failUnless(cmi.getFilename() == testFilename, "%s was not %s" % (cmi.getFilename(), testFilename) )

    self.failUnless(not cmi.isAbstract())
    cmi.setAbstract(1)
    self.failUnless(cmi.isAbstract())

    # FIXME: test adding an association end?
    
    attrib1 = ClassMembers.ClassAttribute(self.config, 'attrib1')
    attrib2 = ClassMembers.ClassAttribute(self.config, 'attrib2')

    self.failUnless(len(cmi.getAttributes()) == 0)
    cmi.addAttribute(attrib1)
    cmi.addAttribute(attrib2)
    self.failUnless(len(cmi.getAttributes()) == 2)
    self.failUnless(cmi.getAttributeByName('attrib1', TRANSLATOR) == attrib1)
    self.failUnless(len(cmi.getAttributeNames(TRANSLATOR)) == 2)
    self.failUnless('attrib1' in cmi.getAttributeNames(TRANSLATOR))
    
    cmi.appendBaseClass(root1)
    cmi.appendBaseClass(root2)
    self.failUnless(root1 in cmi.getBaseClasses())
    self.failUnless('root1' in cmi.getBaseClassNames(TRANSLATOR))
    self.failUnless(root2 in cmi.getBaseClasses())
    self.failUnless('root2' in cmi.getBaseClassNames(TRANSLATOR))
    self.failUnless(len(cmi.getBaseClasses()) == 2)
    self.failUnless(len(cmi.getBaseClassNames(TRANSLATOR)) == 2)

    self.failUnless(not cmi.isRootClass())
    self.failUnless(root1.isRootClass())
    self.failUnless(root2.isRootClass())
    self.failUnless(cmi.getRootClass() == root1)

    self.failUnless(cmi.getBasePrimaryKeyName(TRANSLATOR) == 'root1_pk')
    self.failUnless(cmi.getForeignKeyName(TRANSLATOR) == 'testClassMetaInfo_fk')
    
def suite():
  return unittest.defaultTestLoader.loadTestsFromTestCase(ClassMemberTestCases)

if __name__ == "__main__":
  unittest.main(defaultTest="suite")
