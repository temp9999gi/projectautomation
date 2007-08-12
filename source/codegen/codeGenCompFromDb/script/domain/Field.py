# start
from posdata.DbAndJavaTypeMapper import *
from CommonUtil import *
aCommonUtil = CommonUtil()

class Field:
	def __init__(self, CONS):
		self.typeMapper = DbAndJavaTypeMapper(CONS)
		self.javaType = ''
		self.javaName = ''
		
	def setAttributes(self, columnEng, columnDataTypeAndLength, \
					columnNullOption, columnIsPK, columnIsFk, columnKor, tableKor, tableEng):
		self.columnDataTypeAndLength, self.columnNullOption, self.columnIsPK, \
		self.columnIsFk, self.columnKor, self.tableKor, self.tableEng \
		    = \
        	columnDataTypeAndLength, columnNullOption, columnIsPK, \
        	columnIsFk, columnKor, tableKor, tableEng

		self.columnEng = columnEng.upper()
		
		self.setColTypeAndLength(columnDataTypeAndLength)
		self.setJavaName(columnEng)

	def getPadedJavaName(self):
		return aCommonUtil.getRpadSpaceInTotalLen(self.javaName, 20)
		
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
		
	def setColTypeAndLength(self, columnDataType):
		if '(' in columnDataType:
			self.colType, self.length  =  columnDataType.split('(')
			self.length = self.length.replace(')', '')
		else:
			self.colType = columnDataType
			self.length = ''

		self.setJavaType(self.colType)

	def setJavaType(self, colType):
		self.javaType = self.typeMapper.getJavaType(colType)

	def setJavaName(self, inName):
		self.javaName = aCommonUtil.getJavaFieldName(inName)
	def getJavaName(self):
		return self.javaName
	