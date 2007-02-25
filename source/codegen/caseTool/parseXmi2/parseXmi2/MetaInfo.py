# -*- coding: utf-8 -*-

from CommonUtil import *
aCommonUtil = CommonUtil()

class MetaInfo:
	def __init__(self):
		self.documentation = ''
		
	def setXmiId(self, xmiId):
		self.xmiId = xmiId
	def getXmiId(self):
		return self.xmiId		
	def setOwner(self, owner):
		self.owner = owner
	def getOwner(self):
		return self.owner			
	def setVisibility(self, visibility):
		self.visibility = visibility
	def getVisibility(self):
		return self.visibility	
	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
	
# 아래 예시와 같은 형태의 메소드를 동적으로 정의한다.
# --- 예시 ---
# 	def setBehavioralFeature(self, behavioralFeature):
# 		self.behavioralFeature = behavioralFeature
# 	def getBehavioralFeature(self):
# 		return self.behavioralFeature

	def defineMethod(self, methodName):
		defineMethodString = '''
def set%(MethodNameUpperIndex0)s(self,%(methodName)s):
	self.%(methodName)s = %(methodName)s
def get%(MethodNameUpperIndex0)s(self):
	return self.%(methodName)s

self.set%(MethodNameUpperIndex0)s=set%(MethodNameUpperIndex0)s
self.get%(MethodNameUpperIndex0)s=get%(MethodNameUpperIndex0)s
''' % {'methodName': methodName, \
		'MethodNameUpperIndex0': aCommonUtil.getUpperNameIndex0(methodName)}

		exec defineMethodString
		
	def setDocumentation(self, aModelInfo):
		# <UML:TaggedValue xmi.id="X.30" tag="documentation" value="insert_xxxxxxxxxxxxxxxxxxx" modelElement="UMLOperation.10"/>
		aTaggedValue = aModelInfo.getTaggedValueDictModelElementXmiId(self.xmiId)
		if aTaggedValue:
			self.documentation = aTaggedValue.value
		else:
			self.documentation = ''
	def getDocumentation(self):
		return self.documentation		
		