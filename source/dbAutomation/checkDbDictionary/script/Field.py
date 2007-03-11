# start
from CommonUtil import *
aCommonUtil = CommonUtil()
class ElementWord:
	def setElementWordEng(self, inName):
		self.elementWordEng = inName

class Field:
	def __init__(self, typeMapper):
		self.typeMapper= typeMapper
		self.javaType=""
		self.elementWordList = []
		
	
	def setAttributes(self, columnName, columnDatatype, columnNullOption, \
							columnIsPK, columnIsFK, attributeName):
		self.no1=""
		self.name                   = columnName
		self.columnName				= columnName
		self.columnEng				= columnName
		self.columnKorName			= attributeName
		self.columnKor = self.columnKorName

		self.visibility             = 'private'
		
		self.columnDatatype			= columnDatatype
		
		self.columnIsPK = columnIsPK
		self.key = self.columnIsPK
		self.columnIsFK = columnIsFK
		
		self.null1 = columnNullOption
		self.remark="bizName"
		self.tableEng=""
		
		
		self.setColTypeAndLength(columnDatatype)
		self.setJavaName(columnName)
		self.setElementWord(columnName)
		
	def setElementWord(self, inName):
		for ew in inName.split('_'):
			aElementWord = ElementWord()
			aElementWord.setElementWordEng(ew)
			self.elementWordList.append(aElementWord)

	def setColTypeAndLength(self, columnDatatype):
		if '(' in columnDatatype:
			self.colType, self.length  =  columnDatatype.split('(')
			self.length = self.length.replace(')', '')
		else:
			self.colType = columnDatatype
			self.length = ''
		self.type1 = self.colType
		self.setJavaType(self.colType)
		
	def setJavaType(self, colType):
		self.javaType = self.typeMapper.getJavaType(colType)

	def setJavaName(self, inName):
		self.javaName = aCommonUtil.getJavaFieldName(inName)
	def getJavaName(self):
		return self.javaName		
		

	