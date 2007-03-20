#*- coding: utf-8 -*-
import re
import string

#-------------------------------------------------------------------------------

def generateCode(aSqlMaster, templateFileName):

	from Cheetah.Template import Template
	aTemplate = Template(file = templateFileName, searchList = [aSqlMaster])
	
	return aTemplate	

def writeFile(file_name, aTemplate):
	# print aTemplate
	new_file = file(file_name, 'w+')
	new_file.write('%s' % aTemplate)
	new_file.close()
	print '(NG) file %s created' % file_name

def getWhereInArg(inSqlText):
	reg1 = re.compile('WHERE.*')
	sqlText = string.replace(inSqlText,'\n',' ')
	whereStr = reg1.findall(sqlText, re.I | re.M)
	reg2 = re.compile('#(\w+)#')
	whereArg = reg2.findall(str(whereStr), re.I | re.M)
	
	return whereArg

def capitalize1(inText):
	return string.capitalize(inText)
