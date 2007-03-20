#*- coding: utf-8 -*-
# iBatisXMLParser.py
import string
import sys
import xml.dom.minidom

class IBatisXMLParser :

	def __init__(self):
		pass	
	
	def doParse(self):

		from xml.parsers.xmlproc import xmlval
		
		xmlFile = './input/'+sys.argv[1]		
		doc = xml.dom.minidom.parse(xmlFile)
		
		# getElementsByTagName("name")[0].firstChild.data 의 리턴은 유니코드임
		# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc0 in position 0: ordinal not in range(128)
		# str(className)

		temp = doc.getElementsByTagName("sqlMap")[0].firstChild.data
		print temp,'11111'
		
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