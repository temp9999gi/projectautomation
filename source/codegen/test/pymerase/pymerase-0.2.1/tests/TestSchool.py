#!/usr/bin/env python
from __future__ import nested_scopes
import copy
import os
import re
import string
import sys
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
    houses[string.lower(h.getHouseName())] = h
  return houses

def getFaculty(session):
  """Returns dictionary of houses indexed by professor
  """
  prof_list = session.getAllObjects(session.Faculty)
  faculty = {}
  for p in prof_list:
    faculty[string.lower(p.getGivenName())] = p
  return faculty

def getEmployees(session, givenName):
  givenNameQuery = "%s = '%s'" % (givenNameFieldName, givenName)
  employee = session.getObjectsWhere(session.Employees, givenNameQuery)
  return employee

def getStaff(session, givenName):
  givenNameQuery = "%s = '%s'" % (givenNameFieldName, givenName)
  staff = session.getObjectsWhere(session.Staff, givenNameQuery)
  return staff

  
class CreateSchoolTestCases(unittest.TestCase):
  def __init__(self, name):
    """Initialize
    """
    self.school_dir = os.path.normpath(os.path.join(os.getcwd(), "../examples/school"))

    unittest.TestCase.__init__(self, name)
    
  def setUp(self):
    """Perform setup
    """
    self.current_dir = os.getcwd()
    os.chdir(self.school_dir)
    self.current_python_path = copy.copy(sys.path)
    sys.path.append(self.school_dir)

  def tearDown(self):
    """Clean up after ourselves. 
    """
    os.chdir(self.current_dir)
    sys.path = copy.copy(self.current_python_path)
    
  def resetDirectory(self):
    """Reset the environemnt for testing a different API
    """
    # remove the generated API
    api_dir = os.path.join(self.school_dir, 'school')
    if os.path.isdir(api_dir):
      for file in os.listdir(api_dir):
        os.remove(os.path.join(api_dir,file))
      os.rmdir(api_dir)
      
    sql_file = os.path.join(self.school_dir, 'school.sql')
    if os.path.isfile(sql_file):
      os.remove(sql_file)

    #os.system("sleep 10")
              
  def testCreate_underscore_API(self):
    """Test generating python api with the sql part using underscore_word.
    """
    self.resetDirectory()
    
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
    classesInModel={}
    parsed_input = translator.read(schema, 'parseGenexSchemaXML', classesInModel)
    translator.write(parsed_input, api_output, 'CreateDBAPI')
    translator.write(parsed_input, sql_output, 'CreateSQL')

    # one of the later tests needs to know what the actual field name is
    global givenNameFieldName
    givenNameFieldName="given_name"

    
  def testCreateUML_underscore_API(self, schema):
    """Test generating python code from zargo file with the db using underscore_word
    """
    self.resetDirectory()

    # Figure out path information
    schema = os.path.abspath(schema)
    api_output = os.path.abspath("./school")
    sql_output = os.path.abspath("./school.sql")

    # construct pymerase object
    translator = pymerase.Pymerase()
    #translator.setDefaultPackage("school")
    
    # set mangler convetion
    #mangler = NameMangling.underscore_word()
    #translator.setNameMangler(mangler, 'CreateSQL')

    # do the translation
    classesInModel={}
    parsed_input = translator.read(schema, 'parseXMI', classesInModel)
    translator.write(parsed_input, api_output, 'CreateDBAPI')
    translator.write(parsed_input, sql_output, 'CreateSQL')

    # one of the later tests needs to know what the actual field name is
    global givenNameFieldName
    givenNameFieldName="given_name"


  def testSMWCreateUML_underscore_API(self):
    self.testCreateUML_underscore_API("school.smw")

  def testPoseidon161CreateUML_underscore_API(self):
    self.testCreateUML_underscore_API("schoolPoseidon161.xmi")
    
  def testPoseidon141CreateUML_underscore_API(self):
    self.testCreateUML_underscore_API("schoolPoseidon141.xmi")

  def testCreateCapsAPI(self):
    """Test generating python api with the sql part using CapWord.
    """
    self.resetDirectory()

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
    classesInModel={}
    parsed_input = translator.read(schema, 'parseGenexSchemaXML', classesInModel)
    translator.write(parsed_input, api_output, 'CreateDBAPI')
    translator.write(parsed_input, sql_output, 'CreateSQL')

    # one of the later tests needs to know what the actual field name is
    global givenNameFieldName
    givenNameFieldName='"GivenName"'


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
    createdb.write(string.join(createDBText, os.linesep))
    createdb.close()

    log_file = os.path.join(self.current_dir, "psql.log")
    exit = os.system("psql -h %s -f createdb.sql template1 >>  %s 2>&1 " % (host, log_file))

    self.failUnless(exit == 0)
    
    #os.remove(createDBName)


  def testSimpleInsert(self):
    """Insert objects with all attributes manual initialized
    """
    # also known as try to get rid of the using psql to load data
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      # define some faculty
      for faculty_values in [('0001', 'Xavier', 'Xal', 'Associate'),
                             ('0002', 'Yolanda', 'Yetti', 'Visiting'),
                             ('0003', 'Zaphod', 'Zim', 'Full')]:
        f = s.Faculty()
        f.setUid(faculty_values[0])
        f.setGivenName(faculty_values[1])
        f.setFamilyName(faculty_values[2])
        f.setStatus(faculty_values[3])
        f.commit()
  
      # define some houses
      for house_name in ('Blacker', 'Dabney', 'Flemming', 'Lloyd', 'Page', 
                         'Ricketts', 'Ruddock'):
        house = s.Houses()
        house.setHouseName(house_name)
        house.commit()
  
      for student_values in [('0004', 'Ann', 'Arbor', 1, 2),
                             ('0005', 'Ben', 'Blartfast', 2, 1),
                             ('0006', 'Charles', 'Cooper', 3, 3),
                             ('0007', 'Daria', 'Darwin', 4, 2),]:
        student = s.Students()
        student.setUid(student_values[0])
        student.setGivenName(student_values[1])
        student.setFamilyName(student_values[2])
        student.setHousesFk(student_values[3])
        # FIXME: set key link to advisor, this is a bad name
        # but does reflect the base class name
        student.setFacultyFk(student_values[4])
        student.commit()
  
      courses_list = [('Bi/CS 164', 'Lecture, discussion, and projects in bioinformatics. Students will create, extend, and integrate bioinformatic software tools. Topics include genome-scale mRNA expression analysis, signal transduction pathway modeling, genome database analysis tools, and modeling morphogenesis from gene expression patterns. Each project will link into a larger Web application framework.'),
                      ('Bi 188', 'Introduction to the genetics of humans. Subjects covered include human genome structure, genetic diseases and predispositions, the human genome project, forensic use of human genetic markers, human variability, and human evolution.')
                      ]
      for course_value in courses_list:
        course = s.Courses()
        course.setCourseCode(course_value[0])
        course.setDescription(course_value[1])
        course.commit()
  
      for class_values in [(1,1,'2002-04-01',3.3),
                           (2,1,'2002-04-01',3.0),
                           ]:
        c = s.Classes()
        # FIXME: need better way to declare what name the primary key should have
        #c.setUidFk(class_values[0])
        c.setStudentsFk(class_values[0])
        c.setCoursesFk(class_values[1])
        c.setTerm(class_values[2])
        c.setGrade(class_values[3])
        c.commit()
  
  
      for staff_value in [('0008', 'diane', 'trout', 'code monkey'),
                             ('0009', 'kevin', 'cooper', 'lab tech'),
                             ('0010', 'jason', 'stewart', 'software consultant'),
                             ('0011', 'amanda', 'jones', 'music')]:
        staff = s.Staff()
        staff.setUid(staff_value[0])
        staff.setGivenName(staff_value[1])
        staff.setFamilyName(staff_value[2])
        staff.setJobDescription(staff_value[3])
        staff.commit()
    finally:
      s.close()

  def testInsertClassAttribute(self):
    """Insert an element into a collection of class type coded as a collection

    Tests Bug #774006
      (well sort of, since the failure is that pymerase can't create such
      an attribute)
    """
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      xavier = s.People(1)
  
      home = s.Address()
      home.setName('Home')
      home.setStreetAddress('123 Anywhere')
      home.setCity('Pasadena')
      home.setRegion('California')
      home.setPostalCode('91125')
  
      # bug 774006 would fail here
      xavier.appendAddresses(home)
      xavier.commit()
  
      xavierLoaded = s.People(1)
      addresses = xavierLoaded.getAddresses()
      self.failUnless(len(addresses) == 1)
      self.failUnless(addresses[0].getStreetAddress() == home.getStreetAddress())
      self.failUnless(addresses[0].getCity() == home.getCity())
      self.failUnless(addresses[0].getRegion() == home.getRegion() )
      self.failUnless(addresses[0].getPostalCode() == home.getPostalCode() )
    finally:
      s.close()


  def testReadObject(self):
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      # grab by primary key and make sure it's our first example student
      ann = s.Students(4)
      self.failUnless(ann.getGivenName() == 'Ann')
      self.failUnless(ann.getFamilyName() == 'Arbor')
      self.failUnless(ann.getHousesFk() == 1)
      self.failUnless(ann.getFacultyFk() == 2)
  
      # try to read inherited object via class factory
      zaphod = s.Faculty(3)
      self.failUnless(zaphod.getGivenName() == 'Zaphod')
      self.failUnless(zaphod.getFamilyName() == 'Zim')
      self.failUnless(zaphod.getStatus() == 'Full')
  
      # The initial load of data installs 4 example students
      student_list = s.getAllObjects(school.Students.Students)
      self.failUnless(len(student_list) == 4, "students = %d" % (len(student_list)))
    finally:
      s.close()
    

  def testReadOneToOneLink(self):
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      daria = s.Students(7)
  
      # FIXME: this should read advisor
      advisors = daria.getAdvisor()
  
      self.failUnless(len(advisors) == 1)
      self.failUnless(advisors[0].getUid() == '0002')
      self.failUnless(advisors[0].getGivenName() == 'Yolanda')
      self.failUnless(advisors[0].getFamilyName() == 'Yetti')
    finally:
      s.close()
    

  def testReadManyToOneLink(self):
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      houses = getHouses(s)
      darbs = houses['dabney'].getStudents()
  
      self.failUnless(len(darbs) == 1, "darbs = %d" % (len(darbs)))
      self.failUnless(darbs[0].getGivenName() == "Ben")
      self.failUnless(darbs[0].getFamilyName() == "Blartfast")
    finally:
      s.close()
    

  def testReadManyToManyLink(self):
    pass
  
  def testOneToOneInsert(self):
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      houses = getHouses(s)
      faculty = getFaculty(s)
      
      #erin = Students(db_session=s)
      erin = s.Students()
      erin.setUid('0012')
      erin.setGivenName("Erin")
      erin.setFamilyName("Ericsson")
      erin.setHouse(houses['page'])
  
      faculty['yolanda'].appendStudents(erin)
      faculty['yolanda'].commit()
  
      #erin_list = s.getObjectsWhere(s.Students, "\"GivenName\" = 'Erin'")
      givenNameQuery = "%s = 'Erin'" % ( givenNameFieldName )
      erin_list = s.getObjectsWhere(s.Students, givenNameQuery)
      self.failUnless(len(erin_list) == 1, "erin = %d" % (len(erin_list)))
      erin_loaded = erin_list[0]
  
      self.failUnless(erin.id() == erin_loaded.id())
      self.failUnless(erin.getGivenName() == erin_loaded.getGivenName())
      self.failUnless(erin.getFamilyName() == erin_loaded.getFamilyName())
      self.failUnless(erin.getHousesFk() == erin_loaded.getHousesFk())
      self.failUnless(erin.getFacultyFk() == erin_loaded.getFacultyFk())
      
      frederick = s.Students()
      frederick.setUid('0013')
      frederick.setGivenName("Frederick")
      frederick.setFamilyName("Fergison")
      frederick.setHouse(houses['ricketts'])
      faculty['zaphod'].appendStudents(frederick)
      faculty['zaphod'].commit()
  
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
      self.failUnless(frederick.getFacultyFk() == frederick_loaded.getFacultyFk())
    finally:
      s.close()

  def testNewAttributeAccess(self):
    """test new-style python attribute access
    implementation by Luis Rodrigo Gallardo Cruz
    """
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    guiseppe = s.Staff()
    guiseppe.Uid = "0014"
    guiseppe.GivenName = "Guiseppe"
    guiseppe.FamilyName = "Gallard"
    guiseppe.JobDescription = "accountant"
    guiseppe.commit()
    
    givenNameQuery = "%s = 'Guiseppe'" % (givenNameFieldName)
    guiseppe_list = s.getObjectsWhere(s.Staff, givenNameQuery)
    self.failUnless(len(guiseppe_list) == 1)
    guiseppe_saved = guiseppe_list[0]

    self.failUnless(guiseppe.Uid == guiseppe_saved.getGivenName())
    self.failUnless(guiseppe.GivenName == guiseppe_saved.getGivenName())
    self.failUnless(guiseppe.FamilyName == guiseppe_saved.getFamilyName())
    self.failUnless(guiseppe.JobDescription == guiseppe_saved.getJobDescription())
      
  def testOneToOneUpdate(self):
    """Make sure that set replaces not appends with a one to one links

    Tests for Bug #693212 'set function for one2one links is appending
                           not setting'
    """
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      houses = getHouses(s)
      
      givenNameQuery = "%s = 'Frederick'" % (givenNameFieldName)
      frederick_list = s.getObjectsWhere(s.Students, givenNameQuery)
      self.failUnless(len(frederick_list) == 1)
      frederick = frederick_list[0]
  
      frederick.setHouse(houses['ricketts'])
      frederick.setHouse(houses['dabney'])
      frederick.commit()
    finally:
      s.close()
    
  def testManyToOneInsert(self):
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      charles = s.Students(6)
      daria = s.Students(7)
      bi188 = s.Courses(2)
  
      classes = s.Classes()
      classes.setCourses(bi188)
      classes.setStudents(charles)
      classes.setTerm(DateTime.DateTime(2002,04,01))
      classes.setGrade(3.3)
      classes.commit()
  
      classes = s.Classes()
      classes.setCourses(bi188)
      classes.setStudents(daria)
      classes.setTerm(DateTime.DateTime(2002,04,01))
      classes.setGrade(3.7)
      classes.commit()
    finally:
      s.close()
    

  def testTreeInsert(self):

    def checkEmployees(session, givenName):
      e = getEmployees(session, givenName)
      self.failUnless(len(e) == 1, "checking for %s" % (givenName))
      return e[0]

    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      diane = checkEmployees(s, "diane")
      kevin = checkEmployees(s, "kevin")
      jason = checkEmployees(s, "jason")
      amanda = checkEmployees(s, "amanda")
      yolanda = checkEmployees(s, "Yolanda")
  
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
    finally:
      s.close()
    
    
  def testTreeRetrieval(self):
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    try:
      yolanda_list = getEmployees(s, "Yolanda")
      self.failUnless(len(yolanda_list) == 1, (map(lambda x: x.getGivenName, yolanda_list)))
      yolanda = yolanda_list[0]
      managedList = yolanda.getManaged()
      self.failUnless(len(managedList) == 3)
  
      diane = filter(lambda x: x.getGivenName() == 'diane', managedList)[0]
      managedByDiane = diane.getManaged()
      self.failUnless(len(managedByDiane) == 1)
      kevin = managedByDiane[0]
      self.failUnless(kevin.getGivenName() == 'kevin')
  
      kevinManager = kevin.getManager()[0]
      self.failUnless(kevinManager.getGivenName() == diane.getGivenName())
      
      amanda_list = filter(lambda x: x.getGivenName() == 'amanda', managedList)
      self.failUnless(len(amanda_list) == 1, str(amanda_list))
      amanda = amanda_list[0]
      amandaDirect = getEmployees(s, "amanda")[0]
      self.failUnless(amanda.getGivenName() == amandaDirect.getGivenName())
      self.failUnless(amanda.getFamilyName() == amandaDirect.getFamilyName())
    finally:
      s.close()


  def testDoubleCommit(self):
    """Test committing one the same object twice

    Tests Bug 788408
    """
    import school
    school.moduleReload()
    s = school.DBSession(host, database)

    givenNameQuery = "%s = 'Erin'" % ( givenNameFieldName )
    erin_list = s.getObjectsWhere(s.Students, givenNameQuery)
    self.failUnless(len(erin_list) == 1, "%d erins" % (len(erin_list)))
    erin = erin_list[0]
    uid = erin.getUid()

    erin.setUid('test')
    erin.commit()
    erin.setUid(uid)
    erin.commit()

    erin_list = s.getObjectsWhere(s.Students, givenNameQuery)
    self.failUnless(len(erin_list) == 1, "%d erins" % (len(erin_list)))
    erin_loaded = erin_list[0]
    self.failUnless(erin_loaded.getUid() == uid, "Couldn't commit twice")
    
  def testFromImport(self):
    """Test using python's from x import y to import a subpackage

    Tests Bug ?
    """
    # move back to the test directory so relative imports don't work
    os.chdir(self.current_dir)
    # set the right path to point at the samples directory
    sys.path = copy.copy(self.current_python_path)
    sys.path.append(os.path.normpath(os.path.join(self.school_dir,'../')))
    # try the from import
    from school.school import DBSession, moduleReload
    moduleReload()
    s = DBSession(host, database)
    
    givenNameQuery = "%s = 'Erin'" % ( givenNameFieldName )
    erin_list = s.getObjectsWhere(s.Students, givenNameQuery)
    self.failUnless(len(erin_list) == 1, "%d erins" % (len(erin_list)))

  def testTransactionManager(self):
    """Test transaction support

    <a href="http://sourceforge.net/tracker/index.php?func=detail&aid=914529&group_id=63836&atid=505348">transaction support</a>
    """
    import school
    school.moduleReload()
    s1 = school.DBSession(host, database)
    transaction = school.TransactionManager(s1)    
    s2 = school.DBSession(host, database)
    
    def getErin(session):
      # get our object
      givenNameQuery = "%s = 'Erin'" % ( givenNameFieldName )
      erin_list = session.getObjectsWhere(session.Students, givenNameQuery)
      self.failUnless(len(erin_list) == 1, "%d erin1s" % (len(erin_list)))
      return erin_list[0]

    # get record and change it in the transaction manager
    erin1 = getErin(s1)
    uid1 = erin1.getUid()
    new_uid = 'test'
    erin1.setUid(new_uid)
    erin1.commit(transaction)
    del erin1
    
    # get a new copy off the disk and make sure it matches the original version
    erin2 = getErin(s2)
    self.failUnless(erin2.getUid() == uid1)
    del erin2
    
    # commit the transaction
    transaction.commit()
    erin2 = getErin(s2)
    self.failUnless(erin2.getUid() == new_uid)
    erin2.setUid(uid1)
    erin2.commit()

    # FIXME: need to add tests of transaction delete

def suite():
  suite = unittest.TestSuite()

  # run through test twice once for underscore_api and once for CapsAPI
  api_tests = [
#               CreateSchoolTestCases("testCreate_underscore_API"),
#               CreateSchoolTestCases("testCreateCapsAPI"),
#               CreateSchoolTestCases("testPoseidon141CreateUML_underscore_API"),
               CreateSchoolTestCases("testPoseidon161CreateUML_underscore_API"),
               # bizarre, if SMW attempts to parse this first
               # it causes the XMI readers to fail
#               CreateSchoolTestCases("testSMWCreateUML_underscore_API"),
              ]
  for api in api_tests:
    suite.addTest(api)
    suite.addTest(CreateSchoolTestCases("testCreateDB"))
    suite.addTest(CreateSchoolTestCases("testSimpleInsert"))
    suite.addTest(CreateSchoolTestCases("testInsertClassAttribute"))
    suite.addTest(CreateSchoolTestCases("testReadObject"))
    suite.addTest(CreateSchoolTestCases("testReadOneToOneLink"))
    suite.addTest(CreateSchoolTestCases("testReadManyToOneLink"))
    suite.addTest(CreateSchoolTestCases("testReadManyToManyLink"))
    suite.addTest(CreateSchoolTestCases("testOneToOneInsert"))
    suite.addTest(CreateSchoolTestCases("testNewAttributeAccess"))
    suite.addTest(CreateSchoolTestCases("testOneToOneUpdate"))
    suite.addTest(CreateSchoolTestCases("testManyToOneInsert"))
    suite.addTest(CreateSchoolTestCases("testTreeInsert"))
    suite.addTest(CreateSchoolTestCases("testTreeRetrieval"))
    suite.addTest(CreateSchoolTestCases("testDoubleCommit"))
    suite.addTest(CreateSchoolTestCases("testFromImport"))
    suite.addTest(CreateSchoolTestCases("testTransactionManager"))
  return suite

if __name__ == "__main__":
  unittest.main(defaultTest="suite")

# NOTES:
# need to change data
#
# Limitations:
#   Need to use SQL types in UML model
#     String isn't specific enough for defining column sizes
#   Associations
#     do you always want to link to the classes primary key?
#     can you link by some other attribute?
