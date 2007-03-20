# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase, main
import string
#from airspeed import *
import airspeed

class Table :
    def __init__(self,tableEng):
        self.tableEng = tableEng
        self.tableKor = ''
        self.columnList = []
        #print '[',tableKor,']'

    def setTableKor(self,tableKor):
        self.tableKor = tableKor

    def addColumnList(self,aColumn):
        self.columnList.append(aColumn)
        aColumn.setTableEng(self.tableEng)
        #print '['+self.tableKor + ']' #, aColumn


class Column :
	def __init__(self,columnEng, propertyType):
		self.columnEng = columnEng
		self.propertyType = propertyType
		self.setUpperNameIndex0(columnEng)
	def setTableEng(self,tableEng):
		self.tableEng = tableEng
	def setpropertyType(self,propertyType):
		self.propertyType = propertyType
	def setUpperNameIndex0(self, attributeName):
		self.upperNameIndex0 = string.upper(attributeName[0]) + attributeName[1:]


def makeGetter((type,name)):
	return """
	public %s get%s(){
		return this.%s;
	}
""" % (type, name[0].upper() + name[1:], name,)


class TemplateTestCase(TestCase):
    def setUp(self):
        pass

    def runTest(self):
        print "runTest"


    def test_foreach(self):
        people = [{'name': 'Bill', 'age': 100}, {'name': 'Bob', 'age': 90}]

        t = airspeed.Template("""
Old people:
#foreach ($person in $people)
  #if($person.age > 95)
  $person.name
  #end
#end
""")
        expected ="""
Old people:


  Bill




"""
        expected1 ="\nOld people:\n\n  \n  Bill\n  \n\n  \n\n"
        # print '[[',expected,']]\n'
        # print '[[',t.merge(locals()),']]'

        self.assertEquals(expected, t.merge(locals()))

    def test_set(self):
        template = airspeed.Template('#set($values = [1..5])#foreach($value in $values)$value,#end')
        ret = template.merge({})
        print ret
        self.assertEquals('1,2,3,4,5,', ret)

        template = airspeed.Template('#set($values = [2..-2])#foreach($value in $values)$value,#end')
        self.assertEquals('2,1,0,-1,-2,', template.merge({}))

    def test_set2(self):
        template = airspeed.Template("#set ($value = 10)$value")
        self.assertEquals("10", template.merge({}))


    def test_can_return_value_from_an_attribute_of_a_context_object(self):
        template = airspeed.Template("Hello $name.first_name")
        class MyObj: pass
        o = MyObj()
        o.first_name = 'Chris'
        self.assertEquals("Hello Chris", template.merge({"name": o}))

    def test_can_return_value_from_a_method_of_a_context_object(self):
        template = airspeed.Template("Hello $name.first_name()")
        class MyObj:
            def first_name(self): return "Chris"
        self.assertEquals("Hello Chris", template.merge({"name": MyObj()}))

    def test_foreach_array(self):
		people = [{'name': 'cdId'  , 'propertyType': 'int'},
				  {'name': 'cdName', 'propertyType':  'String'}]

		t = airspeed.Template("""
//declare var
#foreach ($p in $people)
  private $p.propertyType $p.name;
#end
""")
		expected ='\n//declare var\n\n  private int cdId;\n\n  private String cdName;\n\n'
		ret = t.merge(locals())
		# print '[[',ret,']]'
		self.assertEquals(expected, ret)

    def test_foreach_objectArray(self):
		tabArr = []
		o1 = Column('cdId', 'int')
		tabArr.append(o1)
		o2 = Column('cdName', 'String')
		tabArr.append(o2)
		t = airspeed.Template("""
//declare var
#foreach ($t in $tabArr)
  private $t.propertyType $t.columnEng;
#end
""")

		expected ="""
//declare var

  private int cdId;

  private String cdName;

"""
		ret = t.merge(locals())
#		print '[[',ret,']]'
		self.assertEquals(expected, ret)

    def test_file(self):
		t1 = Table('Table_Name')
		o1 = Column('cdId', 'int')
		t1.addColumnList(o1)
		o2 = Column('cdName', 'String')
		t1.addColumnList(o1)

		inFile = "./input/inputTmpl.java"
		template = airspeed.getTemplateFile(inFile)
		t = airspeed.Template(template)
		expected ='package lfis.sample.cd.vo;\n\nimport lfis.framework.vo.BaseVO;\n\npublic class Table_Name extends BaseVO {\n\n    public Table_Name() {\n    }\n\t\n    private int cdId;\n    public int getCdId() {\n        return cdId;\n    }\n    public void setCdId(String cdId) {\n        this.cdId = cdId;\n    }\n\n    private int cdId;\n    public int getCdId() {\n        return cdId;\n    }\n    public void setCdId(String cdId) {\n        this.cdId = cdId;\n    }\n\n}'
		ret = t.merge({"aTable": t1})
		print '[[',ret,']]'
		#print '[[',expected,']]'
		self.assertEquals(expected, ret)


if __name__ == '__main__':
    #reload(airspeed)

    suite = unittest.TestSuite()
    #suite.addTest(TemplateTestCase())
    #suite.addTest(TemplateTestCase("test_foreach"))
    #suite.addTest(TemplateTestCase("test_set2"))
    #suite.addTest(TemplateTestCase("test_foreach_array"))
    #suite.addTest(TemplateTestCase("test_foreach_objectArray"))
    suite.addTest(TemplateTestCase("test_file"))


    runner = unittest.TextTestRunner()
    runner.run(suite)
