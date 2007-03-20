# -*- coding: utf-8 -*-
# start
import string
from Cheetah.Template import Template

class CommonUtil :
	def generateCode(self, objectArray, templateFileName):
		aTemplate = Template(file = templateFileName, searchList = [objectArray])
		return aTemplate	
	
	def writeFile(self, fileName, aTemplate):
		new_file = file(fileName, 'w+')
		new_file.write('%s' % aTemplate)
		new_file.close()
		
	def getUpperNameIndex0(self, inString):
		return string.upper(inString[0]) + inString[1:]		
		
	def getLowerNameIndex0(self, inString):
		return string.lower(inString[0]) + inString[1:]		

		