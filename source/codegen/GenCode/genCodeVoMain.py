#! /usr/bin/env python
# -*- coding: utf-8 -*-
import string
#from airspeed import *
import airspeed
import xmlHelper

class Table :
    def __init__(self,tableEng):
        self.tableEng = tableEng
        self.tableKor = ''
        self.columnList = []

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
	def setPropertyType(self,propertyType):
		self.propertyType = propertyType
	def setUpperNameIndex0(self, attributeName):
		self.upperNameIndex0 = string.upper(attributeName[0]) + attributeName[1:]

def getTable(xmlFile):
	c =  xmlHelper.getClassInfo(xmlFile, 'classInfo')
	aTable = Table(c.className)
	#print c.className

	for p in xmlHelper.getProperty(xmlFile, 'property'):
		(propertyName, propertyType) = (p.name ,p.type)
		aColumn = Column(propertyName, propertyType)
		aTable.addColumnList(aColumn)
		
	return aTable

def genMain():
	inTemplateFile = "./input/inputTmpl.java"
	template = airspeed.getTemplateFile(inTemplateFile)
	t = airspeed.Template(template)

	xmlFile = './input/Account.xml'	
	aTable = getTable(xmlFile)
	
	ret = t.merge({"aTable": aTable})

	print ret

if __name__ in ('__main__','main'):
	genMain()


