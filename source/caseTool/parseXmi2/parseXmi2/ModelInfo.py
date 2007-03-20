# -*- coding: utf-8 -*-
# import sys
# from Constants import *
# start
# import handyxml

import logging

log = logging.getLogger('ModelInfo')

class ModelInfo:
	global XMI
	
	def __init__(self):	
		#self.classDictByName = {}
		self.classDictXmiId = {}
		self.operationDictXmiId = {}
		
		self.taggedValueDictByModelElementXmiId = {}

		self.classInfoList = []		
		self.classAttributeList = []
		self.classAttributeDictByXmiUuid = {}
		
		self.classOperationList = []

		self.operationParameterList = []
		self.attributeInitialValueList = []
		self.attributeInitialValueDictByXmiUuid = {}
		
		self.taggedValueList = []		
		self.dataTypeList = []
		self.dataTypeDict = {}
		
	def setXMI(self, inXMI):
		ModelInfo.XMI = inXMI
	def getXMI(self):
		return ModelInfo.XMI 
		
	def setClassDict(self, aClassInfo):
		self.setClassDictXmiId(aClassInfo)
		self.addClassInfoList(aClassInfo)
		
	# 이름으로 찾는 것은 의미가 없다. 왜냐면
	# 클래스의 이름은 같은 것이 있을수 있다.	
# 	def setClassDictByName(self, aClassInfo):
# 		self.classDictByName[aClassInfo.className]=aClassInfo		
# 	def getClassByName(self,className):
# 		return self.classDictByName[className]
		
	def setClassDictXmiId(self, aClassInfo):
		self.classDictXmiId[aClassInfo.xmiId]=aClassInfo
	def getClassByXmiId(self, xmiId):
		return self.classDictXmiId[xmiId]

	def addClassInfoList(self, aClassInfo):
		self.classInfoList.append(aClassInfo)
		
	def addClassAttributeList(self, aClassAttribute):
		self.classAttributeList.append(aClassAttribute)
		self.setClassAttributeDictxmiUuid(aClassAttribute)		
	def setClassAttributeDictxmiUuid(self, aClassAttribute):
		self.classAttributeDictByXmiUuid[aClassAttribute.xmiUuid]=aClassAttribute
	def getClassAttributeByXmiUuid(self, xmiUuid):
		try:
			out = self.classAttributeDictByXmiUuid[xmiUuid]
		except KeyError:
			out = None
		return out		
	
	def getClassAttributeList(self):
		return self.classAttributeList
		
	def addDataType(self, aDataType):
		self.dataTypeList.append(aDataType)
		self.setDataTypeDict(aDataType)
		
	def setDataTypeDict(self, aDataType):
		self.dataTypeDict[aDataType.xmiId]=aDataType.name
		
	def getDataTypeByXmiId(self, xmiId):
		try:
			out = self.dataTypeDict[xmiId]
		except KeyError:
			out = None
		return out
	
	def getClassOperationList(self):
		return self.classOperationList		

	def addTaggedValueList(self, aTaggedValue):
		self.taggedValueList.append(aTaggedValue)
		self.setTaggedValueDictModelElementXmiId(aTaggedValue)
	def getTaggedValueList(self):
		return self.taggedValueList
		
	def setTaggedValueDictModelElementXmiId(self, aTaggedValue):
		self.taggedValueDictByModelElementXmiId[aTaggedValue.modelElement] = aTaggedValue
	def getTaggedValueDictModelElementXmiId(self, modelElementXmiId):
		try:
			out = self.taggedValueDictByModelElementXmiId[modelElementXmiId]
		except KeyError:
			out = None
		return out
	
	def makeRelationOfAttribute(self, aModelInfo):
		for aClassAttribute in aModelInfo.getClassAttributeList():
			self.makeRelationForClassAndAttribute(aModelInfo, aClassAttribute)
			self.makeRelationForAttributeAndTaggedValue(aModelInfo, aClassAttribute)
			self.setDataTypeOfAttribute(aModelInfo, aClassAttribute)
			aClassAttribute.setDocumentation(aModelInfo)
			#log.debug("aClassAttribute.attributeName: ['%s']", aClassAttribute.attributeName)

	def setDataTypeOfAttribute(self, aModelInfo, aClassAttribute):
		name = aModelInfo.getDataTypeByXmiId(aClassAttribute.typeXmiId)
		aClassAttribute.setAttributeType(name)

	def makeRelationForClassAndAttribute(self, aModelInfo, aClassAttribute):
		aClassInfo = self.getClassByXmiId(aClassAttribute.owner)
		aClassInfo.addClassAttributeList(aClassAttribute)


	def makeRelationForAttributeAndTaggedValue(self, aModelInfo, aClassAttribute):
		aTaggedValue = aModelInfo.getTaggedValueDictModelElementXmiId(aClassAttribute.xmiId)
		if aTaggedValue:
			aClassAttribute.setTaggedValue(aTaggedValue) # 속성 클래스과 TaggedValue의 릴레이션을 만든다.

	#---------------------------------------------------------------------------
	# setClassAndOperation
	def setClassAndOperation(self, aModelInfo):
		for aOperation in aModelInfo.getClassOperationList():
  			self.makeRelationForClassAndOperation(aModelInfo, aOperation)
			aOperation.setDocumentation(aModelInfo)

	def makeRelationForClassAndOperation(self, aModelInfo, aOperation):
			aClassInfo = aModelInfo.getClassByXmiId(aOperation.owner)
			aClassInfo.addClassOperation(aOperation)
			aClassInfo.setDocumentation(aModelInfo)
			
			#log.debug("aClassInfo.className: ['%s'], oper.name: ['%s']", aClassInfo.className, oper.name)
	#---------------------------------------------------------------------------
	
	#---------------------------------------------------------------------------
	# Parameter
	def addOperationParameter(self, aMethodParameter):
		self.operationParameterList.append(aMethodParameter)
		
	def makeRelationOfParameter(self, aModelInfo):
		for x in self.operationParameterList:
			self.makeRelationForOperationAndParameter(aModelInfo, x)
			
	def makeRelationForOperationAndParameter(self, aModelInfo, inParameter):
		aClassOperation = self.getOperationByXmiId(inParameter.behavioralFeature)
		aClassOperation.addOperationParameterList(aModelInfo, inParameter)
	#---------------------------------------------------------------------------
	
	#---------------------------------------------------------------------------
	# 
	def addAttributeInitialValue(self, aAttributeInitialValue):
		self.attributeInitialValueList.append(aAttributeInitialValue)
		self.setAttributeInitialValueDictByXmiUuid(aAttributeInitialValue)

	def setAttributeInitialValueDictByXmiUuid(self, aAttributeInitialValue):
		self.attributeInitialValueDictByXmiUuid[aAttributeInitialValue.xmiUuid]=aAttributeInitialValue
	def getAttributeInitialValueDictByXmiUuid(self, xmiUuid):
		try:
			out = self.attributeInitialValueDictByXmiUuid[xmiUuid]
		except KeyError:
			out = None
		return out		
		
	#---------------------------------------------------------------------------
	# addClassOperation
	def addClassOperation(self, aClassOperation):
		self.classOperationList.append(aClassOperation)
		self.setOperationDictXmiId(aClassOperation)
		
	def setOperationDictXmiId(self, aClassOperation):
		self.operationDictXmiId[aClassOperation.xmiId] = aClassOperation
	def getOperationByXmiId(self, xmiId):
		return self.operationDictXmiId[xmiId]
	#---------------------------------------------------------------------------
	
# if __name__ == "__main__":
# 	aModelInfo = ModelInfo()
# 	print aModelInfo.getJavaType('C')
