# -*- coding: utf-8 -*-
#import string
# start
from CommonUtil import *
from MetaInfo import *

class ClassInfo(MetaInfo):
	def __init__(self):
		self.attributeListOfClassInfo = []
		self.operationListOfClassInfo = []
		
	def setXmiId(self, xmiId):
		self.xmiId = xmiId		
	def getXmiId(self):
		return self.xmiId	
		
	def setClassName(self, className):
		self.className = className
		aCommonUtil = CommonUtil()
		self.lowerClassName = aCommonUtil.getLowerNameIndex0(className)		
	def getClassName(self):
		return self.className

	def setNamespace(self, namespace):
		self.namespace = namespace
	def getNamespace(self):
		return self.namespace		
		
	def setWriter(self, writer):
		self.writer = writer
	def setWriteDate(self, writeDate):
		self.writeDate = writeDate
	def setSubSystemName(self, subSystemName):
		self.subSystemName = subSystemName
		
	def addClassAttributeList(self, aClassAttribute):
		self.attributeListOfClassInfo.append(aClassAttribute)	
		
	def addClassOperation(self, aClassOperation):
		self.operationListOfClassInfo.append(aClassOperation)

	def getClassOperation(self):
		return self.operationListOfClassInfo
		
# 	def setClassDocumentation(self, aModelInfo):
		# <UML:TaggedValue xmi.id="X.30" tag="documentation" value="insert_xxxxxxxxxxxxxxxxxxx" modelElement="UMLOperation.10"/>
# 		aTaggedValue = aModelInfo.getTaggedValueDictModelElementXmiId(self.xmiId)
# 		if aTaggedValue:
# 			self.classDocumentation = aTaggedValue.value
# 		
# 	def getClassDocumentation(self):
# 		return self.classDocumentation		
