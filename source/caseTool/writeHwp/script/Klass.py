# -*- coding: utf-8 -*-
from CommonUtil import *
import Field
# start
class Klass:
	def __init__(self):
		self.fieldList = []
		self.operationList=[]

	def setAttributes(self, klassEng):
		self.klassEng = klassEng
		self.name=self.klassEng
		#self.klassKor = klassKor
##		aCommonUtil = CommonUtil()
		#self.javaClassName = aCommonUtil.getClassName(klassEng)
		
		self.writer			=" "
		self.writeDate		=" "
		self.subSystemName	=" "

	def addFieldList(self, aField):
		self.fieldList.append(aField)

	def addOperationList(self, aOperation):
		self.operationList.append(aOperation)

	def setClassDoc(self, aClassDoc):
		self.classDoc = aClassDoc
	def getClassDoc(self):
		try:
			out = self.classDoc
			return out
		except AttributeError:
			#ClassDoc 객체가 만들어지지 않았다면 ''을 리턴한다.
			aClassDoc=Field.ClassDoc()
			aClassDoc.setAttributes('','')
			return aClassDoc
	
	def setWriter(self, writer):
		self.writer = writer
	def setWriteDate(self, writeDate):
		self.writeDate = writeDate
	def setSubSystemName(self, subSystemName):
		self.subSystemName = subSystemName


