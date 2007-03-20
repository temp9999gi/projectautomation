#*- coding: utf-8 -*-

import string
import sys
import xml.dom.minidom

class ClassInfo :
	def __init__(self, className, attributeList, pkList):
		self.className = className
		self.setLowerClassNameIndex0(className)
		
		self.attributeList = attributeList #[] 
		self.pkList = pkList #[] 		
		self.setPkString(pkList)
		
	def setLowerClassNameIndex0(self, className):
		self.lowerClassName = string.lower(className[0]) + className[1:]
		
	def setPkString(self, pkList):
		s = ''
		for x in pkList:
			 s = s + (x.attributeType + ' ' + x.attributeName) + ', '
			 
		self.pkString = s[:len(s)-2]
		
		# print self.pkString,'ssssssssss'


class PrimaryKey :
	def __init__(self, attributeName, attributeType):
		self.attributeName = attributeName
		self.attributeType  =  attributeType
		

class Column :
	def __init__(self, attributeName, attributeType):
		self.attributeName = attributeName
		self.setUpperNameIndex0(attributeName)
		
		self.attributeType  =  attributeType
		
	def setUpperNameIndex0(self, attributeName):
		self.upperNameIndex0 = string.upper(attributeName[0]) + attributeName[1:]


		
class XMLParser :

	def __init__(self):
		pass	
	
	def doParse(self):
		# uncomment the following line for validation using gen.dtd
		from xml.parsers.xmlproc import xmlval
		
		# uncomment the following two lines for validation using gen.dtd
		xv = xmlval.XMLValidator()
		xmlFile = './input/'+sys.argv[1]
		xv.parse_resource(xmlFile)
		
		doc = xml.dom.minidom.parse(xmlFile)
		
		# getElementsByTagName("name")[0].firstChild.data 의 리턴은 유니코드임
		# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc0 in position 0: ordinal not in range(128)
		# str(className)
		temp = doc.getElementsByTagName("name")[0].firstChild.data
		className = temp.encode('cp949') #Korean
		
		classDesc = 'classDesc 작업필요'
			
		primaryTable = doc.getElementsByTagName("primary-table")[0].firstChild.data.encode('cp949')
		primaryTableBase = string.split(primaryTable)[0]
		
		fieldList = doc.getElementsByTagName("field")
		
		aColumns = []
		aPrimaryKey = []
		for field in fieldList:
			classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data.encode('cp949')
			classAtributeType  = field.getElementsByTagName("type")[0].firstChild.data.encode('cp949')
			tableColumnName    = field.getElementsByTagName("database-field")[0].firstChild.data.encode('cp949')
			classAttributeDesc = 'classAttributeDesc 작업필요'
			classDesc          = 'classDesc	작업필요'
			primaryKey         = field.getElementsByTagName("primary-key")
			insertCol          = field.getElementsByTagName("insert-col")
			updateCol          = field.getElementsByTagName("update-col")
	
			aColumns.append(Column(classAttributeName, classAtributeType))
			if len(primaryKey) > 0:
				aPrimaryKey.append(PrimaryKey(classAttributeName, classAtributeType))
			

		
		aClassInfo = ClassInfo(className,aColumns,aPrimaryKey)	
		
		return aClassInfo