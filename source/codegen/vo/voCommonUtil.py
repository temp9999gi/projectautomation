# -*- coding: utf-8 -*-
import xml.dom.minidom
from Cheetah.Template import Template

def generateCode(objectArray, templateFileName):
	
	aTemplate = Template(file = templateFileName, searchList = [objectArray])
	
	return aTemplate	

def writeFile(fileName, aTemplate):
	# print aTemplate
	new_file = file(fileName, 'w+')
	new_file.write('%s' % aTemplate)
	new_file.close()
	print '(NG) file %s created' % fileName
	
def parseXml(aClassInfo, inXmlFile):
	doc             = xml.dom.minidom.parse(inXmlFile)
	className       = doc.getElementsByTagName("classInfo")[0].getAttribute('className')
	packagePath     = doc.getElementsByTagName("classInfo")[0].getAttribute('packagePath')
	
	aClassInfo.setAttributes(className,packagePath)
	
	return aClassInfo	