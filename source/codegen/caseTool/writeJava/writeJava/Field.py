# start
#from DbAndJavaTypeMapper import *
from CommonUtil import *

class Field:		
	def setAttributes(self, fieldVisibility, fieldType, fieldName):
	    #fieldEng, fieldKor, fieldType, fieldVisibility, key, colSeq
	    self.fieldVisibility = fieldVisibility
	    self.fieldType = fieldType
	    self.fieldName = fieldName

##		self.setJavaFieldName(fieldEng)
		
##	def setJavaFieldName(self, fieldEng):
##		aCommonUtil = CommonUtil()
##		self.javaFieldName = aCommonUtil.getJavaFieldName(fieldEng)
##	def setJavaType(self, javaType):
##		self.javaType = javaType
##	def getJavaType(self):
##		return self.javaType
##	def setColTypeAndLength(self, fieldType):
##		if '(' in fieldType:
##			self.colType, self.length  =  fieldType.split('(')
##			self.length = self.length.replace(')', '')
##		else:
##			self.colType = fieldType
##			self.length = 0
##
##		self.setJavaType(self.colType)
##
##	def getLength(self):
##		return self.length

