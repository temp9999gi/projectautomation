#*- coding: utf-8 -*-
from Cheetah.Template import Template

def getTemplate(aClassInfo, templateFileName):
	aTemplate =  Template(file = templateFileName, searchList = [aClassInfo])
	return aTemplate	

def writeFile(file_name, aTemplate):
	new_file = file(file_name, 'w+')
	new_file.write('%s' % aTemplate)
	new_file.close()
	print '(NG) file %s created' % file_name
	
	
