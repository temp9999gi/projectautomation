#*- coding: utf-8 -*-

from classDef import *
from iBaitsXMLParser import *

import sys

def getTemplate(aClassInfo, templateFileName):

	from Cheetah.Template import Template
	aTemplate = Template(file = templateFileName, searchList = [aClassInfo])
	
	return aTemplate	

def writeFile(file_name, aTemplate):
	# print aTemplate
	
	new_file = file(file_name, 'w+')
	new_file.write('%s' % aTemplate)
	new_file.close()
	print '(NG) file %s created' % file_name


class Run :
	
	aIBatisXMLParser = IBatisXMLParser()

	aClassInfo = aIBatisXMLParser.doParse()
		
	# interface AccountDao
	file_name = './output/' + aClassInfo.className + 'Dao.java'	
	templateFileName = "./input/InterfaceDao.tmpl"
	aTemplate = getTemplate(aClassInfo, templateFileName)

	
	writeFile(file_name, aTemplate)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python gen.py Class.xml"
		sys.exit()	

	Run()






