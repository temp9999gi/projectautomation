# start
from CommonUtil import *
class Field:
	def __init__(self, typeMapper):
		self.typeMapper= typeMapper

	def setAttributes(self, name, columnDatatype):
		self.name                   = name
		self.visibility             = 'private'
		self.columnDatatype			= columnDatatype
		self.setColTypeAndLength(columnDatatype)
		
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
