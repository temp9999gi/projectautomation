# start
from posdata.DbAndJavaTypeMapper import *
from CommonUtil import *

class Field:
	def __init__(self, CONS):
		#self.typeMapper= typeMapper
		self.typeMapper = DbAndJavaTypeMapper(CONS)
		self.javaType=""
	def setAttributes(self, fieldVisibility, fieldType, fieldName):
		self.fieldVisibility = fieldVisibility
		self.fieldType = fieldType
		self.fieldName = fieldName

		self.setJavaType(fieldType)
		aCommonUtil = CommonUtil()
		self.upperNameIndex0 = aCommonUtil.getUpperNameIndex0(fieldName)

	def setJavaType(self, colType):
		self.javaType = self.typeMapper.getJavaType(colType)
		
	def getMethodType(self):
		if self.fieldType =="boolean":
			return "is"
		else:
			return "get"
		
	def getMethodBoolean(self):
		ss = """public int get%(upperNameIndex0)sAsInt() { return %(fieldName)s ? 1 : 0; }""" % \
			{'upperNameIndex0': self.upperNameIndex0, 'fieldName': self.fieldName}
		if self.fieldType =="boolean":
			return ss + '\n'
		else:
			return ""