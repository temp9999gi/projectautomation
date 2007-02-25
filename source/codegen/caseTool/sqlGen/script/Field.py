# start
from CommonUtil import *
aCommonUtil = CommonUtil()
class Field:
	def __init__(self, typeMapper):
		self.typeMapper= typeMapper
		self.javaType=""
	
	def setAttributes(self, columnName, columnDatatype, columnNullOption, \
							columnIsPK, columnIsFK, attributeName):
		self.name                   = columnName
		self.columnName				= columnName
		self.columnEng				= columnName
		self.columnKorName			= attributeName

		self.visibility             = 'private'
		self.columnDatatype			= columnDatatype
		self.columnIsPK = columnIsPK
		self.columnIsFK = columnIsFK
		
		self.setColTypeAndLength(columnDatatype)
		self.setJavaName(columnName)
		
	def setColTypeAndLength(self, columnDatatype):
		if '(' in columnDatatype:
			self.colType, self.length  =  columnDatatype.split('(')
			self.length = self.length.replace(')', '')
		else:
			self.colType = columnDatatype
			self.length = ''

		self.setJavaType(self.colType)
		
	def setJavaType(self, colType):
		self.javaType = self.typeMapper.getJavaType(colType)

	def setJavaName(self, inName):
		self.javaName = aCommonUtil.getJavaFieldName(inName)
	def getJavaName(self):
		return self.javaName		
		
