# -*- coding: utf-8 -*-
from CommonUtil import *
# start
class Klass:
	def __init__(self):
		self.fieldList = []
		self.methodList = []
		

	def setAttributes(self, klassName):
		self.klassName = klassName
		self.writer			=" "
		self.writeDate		=" "
		self.subSystemName	=" "

	def addFieldList(self, aField):
		self.fieldList.append(aField)
		
	def addMethodList(self, aMethod):
		self.methodList.append(aMethod)
		aMethod.setMethodBody(self)
		
	def setWriter(self, writer):
		self.writer = writer
	def setWriteDate(self, writeDate):
		self.writeDate = writeDate
	def setSubSystemName(self, subSystemName):
		self.subSystemName = subSystemName


class Method:
	def __init__(self):
		pass
	def setAttributes(self, methodReturnType, methodName, methodArgument):
		self.methodReturnType = methodReturnType
		self.methodName       = methodName
		self.methodArgument   = methodArgument
		
	def setMethodBody(self, aKlass):
		xx="""return (%(in_klassName)s) getSqlMapClientTemplate().queryForObject("get%(in_klassName)s", username);""" % \
  			{'in_klassName': aKlass.klassName}
		self.methodBody = xx
		
	def getMethodBody(self):
		return self.methodBody


