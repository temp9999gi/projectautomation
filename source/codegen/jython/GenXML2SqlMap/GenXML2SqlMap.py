#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import xmlHelper
from commonUtil import *
from commonClassDef import *

def getTable(xmlFile):
	c =  xmlHelper.getClassInfo(xmlFile, 'classInfo')
	aTable = Table(c.className)
	for p in xmlHelper.getProperty(xmlFile, 'property'):
		(propertyName, propertyType, pkYn) = (p.name ,p.type, p.pkYn)
		aColumn = Column(propertyName, propertyType)
		aColumn.setPkYn(pkYn)
		aTable.addColumnList(aColumn)
	aTable.setPkColumn()
	return aTable

def getInsertSqlBlock(aTable):
	setInsertSql1(aTable)
	return getTemplate(aTable,'insert')

def getUpdateSqlBlock(aTable):
	setUpdateSql1(aTable)
	return getTemplate(aTable,'update')

def getDeleteSqlBlock(aTable):
	setDeleteSql1(aTable)
	return getTemplate(aTable,'delete')

def getSelectSqlBlock(aTable):
	setSelectSql1(aTable)
	return getTemplate(aTable,'select')
 
def genMain():
	xmlFile = './input/Account.xml'
	aTable = getTable(xmlFile)
	# print getInsertSqlBlock(aTable)

	file_name = './output/output.xml'

	aTemplate = getInsertSqlBlock(aTable) + '\n' +\
		getUpdateSqlBlock(aTable) + '\n' +\
		getDeleteSqlBlock(aTable) + '\n' +\
		getSelectSqlBlock(aTable) + '\n'

	aTable.setCrudSql(aTemplate)


	inTemplateFile = "./input/sqlMapTmpl.xml"
	template = airspeed.getTemplateFile(inTemplateFile)
	t = airspeed.Template(template)

	ret = t.merge({"aTable": aTable})

	
	writeFile(file_name, ret)
	
if __name__ in ('__main__','main'):
	genMain()


