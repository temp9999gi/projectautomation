# -*- coding: utf-8 -*-

# start
##from posdata.DbAndJavaTypeMapper import *
from CommonUtil import *
aCommonUtil = CommonUtil()

from domain.MethodInfo import *

class TableInfo:
	def __init__(self):
		self.methodList = []
		self.methodDictByMethodId = {}
		self.fieldList = []
		self.pkColumnList=[]
		self.nonPkColumnList=[]

	def setAttributes(self, table_Kor, table_Eng, table_Cd, crud_Type):
		self.table_Kor, self.table_Eng, self.crud_Type =  table_Kor, table_Eng, crud_Type
		self.table_Cd = table_Cd
		self.tableEng = table_Cd
		self.tableIdCapWord = aCommonUtil.getCapWord(table_Eng)
		#self.voId = aCommonUtil.getCapWord(table_Eng)+'Vo'
		#self.lowerVoId = string.lower(self.voId[0]) + self.voId[1:]
		#####?????self.classId = aCommonUtil.getCapWord(table_Eng)

	def addMethodList(self, obj):
		self.methodList.append(obj)

	def setMethodDictByMethodId(self, key, item):
		self.methodDictByMethodId[key] = item
	def getMethodDictByMethodId(self, key):
		try:
			out = self.methodDictByMethodId[key]
			return out
		except KeyError:
			return None

		
	def addFieldList(self, aField):
		self.fieldList.append(aField)
		self.setpkColumnList(aField)

	def setPkColumnList(self, aField):
		if aField.columnIsPK == 'Yes':
			self.pkColumnList.append(aField)
# 			print 'aField: [',aField.name,']'
		else:
			self.nonPkColumnList.append(aField)
# 			print 'aField: [',aField.name,']'


