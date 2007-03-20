#*- coding: utf-8 -*-

import string
import sys
import xml.dom.minidom
from ClassInfo import *

class XMLParser :

	def __init__(self):
		pass	
	
	def doParse(self, xmlFile):
		# uncomment the following line for validation using gen.dtd
		from xml.parsers.xmlproc import xmlval
		
		# uncomment the following two lines for validation using gen.dtd
		xv = xmlval.XMLValidator()
		xv.parse_resource(xmlFile)
		
		doc = xml.dom.minidom.parse(xmlFile)
		
		# getElementsByTagName("name")[0].firstChild.data �� ������ �����ڵ���
		# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc0 in position 0: ordinal not in range(128)
		# str(className)
		temp = doc.getElementsByTagName("name")[0].firstChild.data
		className = temp.encode('cp949') #Korean
		
		classDesc = 'classDesc �۾��ʿ�'
			
		primaryTable = doc.getElementsByTagName("primary-table")[0].firstChild.data.encode('cp949')
		primaryTableBase = string.split(primaryTable)[0]
		
		fieldList = doc.getElementsByTagName("field")
		
		aClassAttributes = []
		aPrimaryKey = []
		for field in fieldList:
			classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data.encode('cp949')
			classAtributeType  = field.getElementsByTagName("type")[0].firstChild.data.encode('cp949')
			tableColumnName    = field.getElementsByTagName("database-field")[0].firstChild.data.encode('cp949')
			classAttributeDesc = 'classAttributeDesc �۾��ʿ�'
			classDesc          = 'classDesc	�۾��ʿ�'
			primaryKey         = field.getElementsByTagName("primary-key")
			insertCol          = field.getElementsByTagName("insert-col")
			updateCol          = field.getElementsByTagName("update-col")
	
			aClassAttributes.append(ClassAttribute(classAttributeName, classAtributeType))
			if len(primaryKey) > 0:
				aPrimaryKey.append(PrimaryKey(classAttributeName, classAtributeType))

		aClassInfo = ClassInfo(className,aClassAttributes,aPrimaryKey)	
		
		return aClassInfo