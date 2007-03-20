# -*- coding: utf-8 -*- 
# gen.py
# usage:  python gen.py Class.xml

# generates JavaBean Class.java and database access ClassMgr.java files from XML

# Programming by KyungUk,Sung
#
# Copyright (c) 2002 KyungUk,Sung

# gen comes with Absolutely No Warranty.
# This is free software, and you are welcome to
# redistribute it under certain conditions
# (for details see:GNU General Public License,
# http://www.gnu.org/copyleft/gpl.html)

# version 0.1

from classDef import *
from javaBeanWriter import *
from mgrWriter import *

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
	
	classInfo = ClassInfo(className, classDesc, primaryTable, primaryTableBase)
	
	for field in fieldList:
		classAttributeName = field.getElementsByTagName("class-field")[0].firstChild.data.encode('cp949')
		classAtributeType  = field.getElementsByTagName("type")[0].firstChild.data.encode('cp949')
		tableColumnName    = field.getElementsByTagName("database-field")[0].firstChild.data.encode('cp949')
		classAttributeDesc = 'classAttributeDesc 작업필요'
		classDesc          = 'classDesc	작업필요'
		primaryKey         = field.getElementsByTagName("primary-key")
		insertCol          = field.getElementsByTagName("insert-col")
		updateCol          = field.getElementsByTagName("update-col")
	
		col1 = Column(classAttributeName, classAttributeDesc, classAtributeType, tableColumnName, className, \
			classDesc, primaryKey, insertCol,updateCol)

		#classInfo.__setitem__(classAttributeName,col1)
		
		classInfo.addColumnInClassInfo(col1)
		classInfo.addColumnsArray(col1)
	
	
	#join 문장 작성
	joinList = doc.getElementsByTagName("join-table")
	for table in joinList:
		joinName = table.getElementsByTagName("join-name")[0].firstChild.data
		joinClause = table.getElementsByTagName("clause")[0].firstChild.data
		leftOuter = table.getElementsByTagName("left-outer")

		joinTable = JoinTable(joinName, joinClause, leftOuter)
		classInfo.addJoinTableArray(joinTable)
	
	#--------------------------------------------------------#
	# generate JavaBean file
	#--------------------------------------------------------#
	javaBeanWriter = JavaBeanWriter(classInfo)
	i = javaBeanWriter.writeJavaBeanfile()

	
	#--------------------------------------------------------------------
	# generate Mgr database access file
	#--------------------------------------------------------------------
	mgrWriter = MgrWriter(classInfo)
	i = mgrWriter.writeMgrfile()



if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python gen.py Class.xml"
		sys.exit()	
	Run()
