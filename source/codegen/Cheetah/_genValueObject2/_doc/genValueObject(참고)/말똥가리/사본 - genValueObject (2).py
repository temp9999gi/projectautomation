#*- coding: utf-8 -*-

from classDef import *

import sys
import string
import xml.dom.minidom

# uncomment the following line for validation using gen.dtd
from xml.parsers.xmlproc import xmlval

class Run :
	
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
	
#		col1 = Column(classAttributeName, classAttributeDesc, classAtributeType, tableColumnName, className, \
#			classDesc, primaryKey, insertCol,updateCol)
	
#	classInfo = ClassInfo(className, classDesc, primaryTable, primaryTableBase)
	
	aClassInfo = ClassInfo(className,aColumns)	
	
	from Cheetah.Template import Template
	aTemplate = Template(file="ValueObject.tmpl", searchList=[aClassInfo])
	
	# print aTemplate
	
	file_name = './output/' + aClassInfo.className + '.java'
	
	new_file = file(file_name, 'w+')
	#new_file.write('%s' % self.template)
	new_file.write('%s' % aTemplate)
	new_file.close()
	print '(NG) file %s created' % file_name


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python gen.py Class.xml"
		sys.exit()	

	Run()






