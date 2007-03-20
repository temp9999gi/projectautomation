# -*- coding: utf-8 -*-
# start
from CommonUtil import *
from MetaInfo import *

class ClassAttribute(MetaInfo):
	def __init__(self):	
		MetaInfo.__init__	
	def setAttributeName(self, attributeName):
		self.attributeName = attributeName
		aCommonUtil = CommonUtil()
		self.upperNameIndex0 = aCommonUtil.getUpperNameIndex0(attributeName)		
	def getAttributeName(self):
		return self.attributeName
	
	def setTypeXmiId(self, typeXmiId):
		self.typeXmiId = typeXmiId
	def getTypeXmiId(self):
		return self.typeXmiId
	
	def setAttributeType(self, attributeType):
		self.attributeType = attributeType
	def getAttributeType(self):
		return self.attributeType
	
	def setTaggedValue(self, aTaggedValue):
		self.aTaggedValue = aTaggedValue
	def getTaggedValue(self):
		return self.aTaggedValue
	
	def setInitialValue(self, initialValue):
		self.initialValue = initialValue
	def getInitialValue(self):
		return self.initialValue
		
		
class AttributeInitialValue(MetaInfo):
	def __init__(self):
		MetaInfo.__init__
		self.xmiId=''
	def setXmiId(self, xmiId):
		self.xmiId = xmiId
	def getXmiId(self):
		return self.xmiId	

