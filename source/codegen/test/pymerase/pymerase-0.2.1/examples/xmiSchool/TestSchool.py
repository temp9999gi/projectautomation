#!/usr/bin/env python
from __future__ import nested_scopes
import copy
import sys
import os
import string
import unittest

# CHANGE TO HOST RUNNING POSTGRESQL
host='localhost'
database='school_d0'

# import components needed to build the sql & api
# FIXME: need to set path to pymerase code
#sys.path.append(os.path.abspath(".."))
import pymerase                
from pymerase.util import NameMangling

# import code to use api
from mx import DateTime

def getHouses(session):
  """Returns dictionary of houses indexed by house name
  """
  houses_list = session.getAllObjects(session.Houses)
  houses = {}
  for h in houses_list:
    houses[string.lower(h.getName())] = h
  return houses

def getFaculty(session):
  """Returns dictionary of houses indexed by professor
  """
  prof_list = session.getAllObjects(session.Faculty)
  faculty = {}
  for p in prof_list:
    faculty[string.lower(p.getGivenName())] = p
  return faculty

def getEmployee(session, givenName):
  givenNameQuery = "%s = '%s'" % (givenNameFieldName, givenName)
  employees = session.getObjectsWhere(session.Employees, givenNameQuery)
  return employees
      

class CreatePyGenexTestCases(unittest.TestCase):
  def setUp(self):
    """Perform setup
    """
    pass
  
  def tearDown(self):
    """Clean up after ourselves. 
    """
    pass

  def testCreate_underscore_API(self):
    """Test generating python api with the sql part using underscore_word.
    """
    # Figure out path information
    schema = os.path.abspath("./schema")
    api_output = os.path.abspath("./school")
    sql_output = os.path.abspath("./school.sql")

    # construct pymerase object
    translator = pymerase.Pymerase()
    translator.setDefaultPackage("school")
    
    # set mangler convetion
    #mangler = NameMangling.underscore_word()
    #translator.setNameMangler(mangler, 'CreateSQL')

    # do the translation 
    parsed_input = translator.read(schema, 'parseGenexSchemaXML')
    translator.write(parsed_input, api_output, 'CreateDBAPI')
    translator.write(parsed_input, sql_output, 'CreateSQL')

    # one of the later tests needs to know what the actual field name is
    global givenNameFieldName
    givenNameFieldName="given_name"
    global dataSourceName
    dataSourceName = "data.sql"

    
  def testCreateCapsAPI(self):
    """Test generating python api with the sql part using CapWord.
    """
    # Figure out path information
    schema = os.path.abspath("./schema")
    api_output = os.path.abspath("./school")
    sql_output = os.path.abspath("./school.sql")

    # construct pymerase object
    translator = pymerase.Pymerase()
    translator.setDefaultPackage("school")

    # set mangler convetion
    mangler = NameMangling.CapWord()
    translator.setNameMangler(mangler, 'CreateSQL')

    # do the translation 
    parsed_input = translator.read(schema, 'parseGenexSchemaXML')
    translator.write(parsed_input, api_output, 'CreateDBAPI')
    translator.write(parsed_input, sql_output, 'CreateSQL')

    # one of the later tests needs to know what the actual field name is
    global givenNameFieldName
    givenNameFieldName='"GivenName"'
    global dataSourceName
    dataSourceName = "dataCapWord.sql"

  def testCreateDB(self):
    """Construct the set of commands needed to tell postgresql to load data
    """
    createDBName = "createdb.sql"
    createdb = open(createDBName, "w")

    createDBText = []
    createDBText.append("drop database school_d0;")
    createDBText.append("create database school_d0;")
    createDBText.append("\c school_d0")
    createDBText.append("\i school.sql")
    createDBText.append("\i %s" % (dataSourceName))
    createdb.write(string.join(createDBText, os.linesep))
    createdb.close()
                   
    os.system("psql -h %s -f createdb.sql template1" % (host))

    #os.remove(createDBName)

  def testReadObject(self):
    import school
    s = school.DBSession(host, database)

    # grab by primary key and make sure it's our first example student
    ann = s.Students(4)
    self.failUnless(ann.getGivenName() == 'Ann')
    self.failUnless(ann.getFamilyName() == 'Arbor')
    self.failUnless(ann.getHousesFk() == 1)
    #self.failUnless(ann.getAdvisorFk() == 2)
    self.failUnless(ann.getPeopleFk() == 2)

    # try to read inherited object via class factory
    zaphod = s.Faculty(3)
    self.failUnless(zaphod.getGivenName() == 'Zaphod')
    self.failUnless(zaphod.getFamilyName() == 'Zim')
    self.failUnless(zaphod.getStatus() == 'Full')

    # The initial load of data installs 4 example students
    students = s.getAllObjects(school.Students.Students)
    self.failUnless(len(students) == 4)

  def testReadOneToOneLink(self):
    import school
    s = school.DBSession(host, database)

    daria = s.Students(7)

    # FIXME: this should read advisor
    advisors = daria.getAdvisor()
    house = daria.getHouse()

    self.failUnless(len(advisors) == 1)
    #self.failUnless(advisors[0].getUid() == 2)
    self.failUnless(advisors[0].getPeoplePk() == 2)
    self.failUnless(advisors[0].getGivenName() == 'Yolanda')
    self.failUnless(advisors[0].getFamilyName() == 'Yetti')
    self.failUnless(len(house) == 1)
    print house[0].getName()
    self.failUnless(house[0].getName() == 'Lloyd')

  def testReadManyToOneLink(self):
    import school
    s = school.DBSession(host, database)

    houses = getHouses(s)
    darbs = houses['dabney'].getStudents()

    self.failUnless(len(darbs) == 1)
    self.failUnless(darbs[0].getGivenName() == "Ben")
    self.failUnless(darbs[0].getFamilyName() == "Blartfast")

  def testReadManyToManyLink(self):
    pass
  
  def testOneToOneInsert(self):
    import school
    s = school.DBSession(host, database)
    houses = getHouses(s)
    faculty = getFaculty(s)
    
    #erin = Students(db_session=s)
    erin = s.Students()
    erin.setGivenName("Erin")
    erin.setFamilyName("Ericsson")
    erin.setHouse(houses['page'])
    # FIXME: we should be able to commit this and then add more information
    # FIXME: but that doesn't work
    # erin.commit()
    faculty['yolanda'].appendStudents(erin)
    faculty['yolanda'].commit()

    #erin_list = s.getObjectsWhere(s.Students, "\"GivenName\" = 'Erin'")
    givenNameQuery = "%s = 'Erin'" % ( givenNameFieldName )
    erin_list = s.getObjectsWhere(s.Students, givenNameQuery)
    self.failUnless(len(erin_list) == 1)
    erin_loaded = erin_list[0]

    print "erin: %s, %s" % (erin.id(), erin_loaded.id())
    self.failUnless(erin.id() == erin_loaded.id())
    self.failUnless(erin.getGivenName() == erin_loaded.getGivenName())
    self.failUnless(erin.getFamilyName() == erin_loaded.getFamilyName())
    self.failUnless(erin.getHousesFk() == erin_loaded.getHousesFk())
    #self.failUnless(erin.getAdvisorFk() == erin_loaded.getAdvisorFk())
    self.failUnless(erin.getPeopleFk() == erin_loaded.getPeopleFk())
    
    frederick = s.Students()
    frederick.setGivenName("Frederick")
    frederick.setFamilyName("Fergison")
    frederick.setHouse(houses['ricketts'])
    faculty['zaphod'].appendStudents(frederick)
    faculty['zaphod'].commit()

    #frederick_list = s.getObjectsWhere(s.Students,
    #                                     "\"GivenName\" = 'Frederick'")
    givenNameQuery = "%s = 'Frederick'" % (givenNameFieldName)
    frederick_list = s.getObjectsWhere(s.Students, givenNameQuery)
    self.failUnless(len(frederick_list) == 1)
    frederick_loaded = frederick_list[0]

    self.failUnless(frederick.id() == frederick_loaded.id(),
       "frederick primary key failure %s != %s" % (frederick.id(),
                                                   frederick_loaded.id()))
    self.failUnless(frederick.getGivenName() == frederick_loaded.getGivenName())
    self.failUnless(frederick.getFamilyName()==frederick_loaded.getFamilyName())
    self.failUnless(frederick.getHousesFk() == frederick_loaded.getHousesFk())
    #self.failUnless(frederick.getAdvisorFk() == frederick_loaded.getAdvisorFk())
    self.failUnless(frederick.getPeopleFk() == frederick_loaded.getPeopleFk())
    

  def testManyToOneInsert(self):
    import school
    s = school.DBSession(host, database)
    charles = s.Students(6)
    daria = s.Students(7)
    bi188 = s.Courses(2)

    classes = s.Classes()
    classes.setCourses(bi188)
    classes.setStudents(charles)
    classes.setTerm(DateTime.DateTime(2002,04,01))
    classes.commit()

    classes = s.Classes()
    classes.setCourses(bi188)
    classes.setStudents(daria)
    classes.setTerm(DateTime.DateTime(2002,04,01))
    classes.commit()


  def testTreeInsert(self):
    import school

    def checkEmployee(session, givenName):
      e = getEmployee(session, givenName)
      self.failUnless(len(e) == 1)
      return e[0]

    s = school.DBSession(host, database)
    diane = checkEmployee(s, "diane")
    kevin = checkEmployee(s, "kevin")
    jason = checkEmployee(s, "jason")
    amanda = checkEmployee(s, "amanda")
    yolanda = checkEmployee(s, "Yolanda")

    #yolanda.appendManaged(amanda)
    diane.setManager(yolanda)
    kevin.setManager(diane)
    amanda.setManager(yolanda)
 
    diane.commit()
    kevin.commit()
    
    jason.setManager(yolanda)
    jason.commit()
    amanda.commit()
    yolanda.commit()
    
  def testTreeRetrieval(self):
    import school
    s = school.DBSession(host, database)
    yolanda = getEmployee(s, "Yolanda")[0]
    managedList = yolanda.getManaged()
    self.failUnless(len(managedList) == 3)

    diane = filter(lambda x: x.getGivenName() == 'diane', managedList)[0]
    managedByDiane = diane.getManaged()
    self.failUnless(len(managedByDiane) == 1)
    kevin = managedByDiane[0]
    self.failUnless(kevin.getGivenName() == 'kevin')

    kevinManager = kevin.getManager()[0]
    self.failUnless(kevinManager.getGivenName() == diane.getGivenName())
    
    amanda = filter(lambda x: x.getGivenName() == 'amanda', managedList)[0]
    amandaDirect = getEmployee(s, "amanda")[0]
    self.failUnless(amanda.getGivenName() == amandaDirect.getGivenName())
    self.failUnless(amanda.getFamilyName() == amandaDirect.getFamilyName())
    
def suite():
  suite = unittest.TestSuite()
  #if 1:
  #  # Test with underscores for sql variables
  #  suite.addTest(CreatePyGenexTestCases("testCreate_underscore_API"))
  #else:
  #  # Test with CapsWord for sql variables
  #  suite.addTest(CreatePyGenexTestCases("testCreateCapsAPI"))
  #  
  global givenNameFieldName
  givenNameFieldName="given_name"
  global dataSourceName
  dataSourceName = "data.sql"

  suite.addTest(CreatePyGenexTestCases("testCreateDB"))
  suite.addTest(CreatePyGenexTestCases("testReadObject"))
  suite.addTest(CreatePyGenexTestCases("testReadOneToOneLink"))
  suite.addTest(CreatePyGenexTestCases("testReadManyToOneLink"))
  suite.addTest(CreatePyGenexTestCases("testReadManyToManyLink"))
  suite.addTest(CreatePyGenexTestCases("testOneToOneInsert"))
  suite.addTest(CreatePyGenexTestCases("testManyToOneInsert"))
#  ##suite.addTest(CreatePyGenexTestCases("testTreeInsert"))
#  ##suite.addTest(CreatePyGenexTestCases("testTreeRetrieval"))
  return suite

if __name__ == "__main__":
  unittest.main(defaultTest="suite")

