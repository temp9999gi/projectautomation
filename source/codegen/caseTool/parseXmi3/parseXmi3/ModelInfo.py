# -*- coding: utf-8 -*-
# import sys
# from Constants import *
# start
# import handyxml
from smw.io import loadModel
from smw.metamodel import UML14
from smw.metamodel import UML13

import logging

log = logging.getLogger('ModelInfo')

#---------------------------------------------------------------------------
"""
ToDo:
    Interface/class가 분석모델인지, 설계모델인지 찾는다.

    Interface/class 객체에 패키지의 최상위 레벨을 찾아서 set한다.

    분석 모델과 설계모델을 분리하여 staruml파일을 만들도록 한다면
    이 작업은 필요없어진다.

    일단 개발자들에게 분리하여 모델을 만들도록 한다.
    왜냐? 지금 당장은 하기가 싫어니깐
	for aInterface in model.getAllParts():
		if isinstance(aInterface, UML13.Interface):
			# print 'aInterface.name[',aInterface.name,']'
			aMyTempVar=MyTempVar()
			getNamespace(aInterface,aMyTempVar)
			out = aMyTempVar.getRootNamespace()
			setRootNamespace(aInterface,out)"""
#---------------------------------------------------------------------------
class MyTempVar:
	def __init__(self):
		self.rootNamespace=''
	def setRootNamespace(self, rootNamespace):
		self.rootNamespace = rootNamespace
	def getRootNamespace(self):
		return self.rootNamespace

def getNamespace(aObject, aMyTempVar):
	ns=aObject.namespace
	#print ns.name
	if ns.name == 'Design Model':
		print 'ns.name[',ns.name,']'
		aMyTempVar.setRootNamespace('Design')
		return 'Design'
	elif ns.name == 'Analysis Model':
		print 'ns.name[',ns.name,']'
		aMyTempVar.setRootNamespace('Analysis')
		return 'Analysis'
	else:
		getNamespace(aObject.namespace, aMyTempVar)

def setRootNamespace(aObject,namespace):
	aObject.rootNamespace = namespace
def getRootNamespace(aObject):
	return aObject.rootNamespace

#---------------------------------------------------------------------------

class ModelInfo:
	global XMI
	
	def __init__(self):	
		#self.classDictByName = {}
		self.classInfoList = []
		self.packagePath=''
		
	def loadModel(self,inFile):
		aSmwModel= loadModel(inFile)
		model= aSmwModel.getModel()
		self.setModel(model)
		self.setStreamer(aSmwModel.getStreamer())
		self.loadClasses(model)

	def setModel(self, model):
		self.model = model
	def getModel(self):
		return self.model
	def setStreamer(self, streamer):
		self.streamer = streamer
	def getStreamer(self):
		return self.streamer
	
	def initPackagePath(self):
		self.packagePath=''
	def setPackagePath(self, aNamespace):
		#getNamespace(aObject, aMyTempVar):
		if aNamespace:
			 self.packagePath = aNamespace.name +'.'+ self.packagePath
		if aNamespace.namespace: #패키지가 존재한다면
			self.setPackagePath(aNamespace.namespace)
		else:
			self.packagePath = self.packagePath[:-1]
			return self.packagePath
		
##		if aNamespace.name =='Project' or aNamespace.name =='':
##			self.packagePath = self.packagePath[:-1]
##			return self.packagePath
##		else:
##			self.setPackagePath(aNamespace.namespace)

	def getPackagePath(self):
		return self.packagePath
	
	def setClassInfoList(self, classInfoList):
		self.classInfoList= classInfoList
		
	def setInterfaceList(self, interfaceList):
		self.interfaceList= interfaceList

	def setClassInfoList(self, classInfoList):
		self.classInfoList= classInfoList

	def setUseCaseList(self, UseCaseList):
		self.UseCaseList = UseCaseList
	def getUseCaseList(self):
		return self.UseCaseList

	#DefinitionType = 'Class' #클래스정의서, 인터페이이스정의서
	def setDefinitionType(self, deliverableType):
		self.deliverableType = deliverableType
	def getDefinitionType(self):
		return self.deliverableType

	def setReaderAppEnv(self, aReaderAppEnv):
		self.aReaderAppEnv = aReaderAppEnv
	def getReaderAppEnv(self):
		return self.aReaderAppEnv

	def getClassListOrInterfaceList(self):
		if self.deliverableType=='Class':
			return self.classInfoList
		if self.deliverableType=='Interface':
			return self.interfaceList

	def loadClasses(self, model):
		#aModelInfo.loadClasses

		"""Convert external UML model to pymerase's model classes.
		"""
		if isinstance(model, UML13.Model):
			umlClass = UML13.Class
			umlAttribute= UML13.Attribute
			umlOperation= UML13.Operation
			umlInterface= UML13.Interface
			umlUseCase= UML13.UseCase
		elif isinstance(model, UML14.Model):
			umlClass = UML14.Class
			umlAttribute= UML14.Attribute
			umlOperation= UML14.Operation
			umlInterface= UML14.Interface
			umlUseCase  = UML14.UseCase
		else:
			raise ValueError("This program only supports UML 1.3 and 1.4 metamodel")

		self.setUmlClass(umlClass)
		self.setUmlAttribute(umlAttribute)
		self.setUmlOperation(umlOperation)
		self.setUmlInterface(umlInterface)
		self.setUmlUseCase(umlUseCase)
		
		classes = filter(lambda c: isinstance(c, umlClass), model.getAllParts())
		self.setClassInfoList(classes)
		
		interfaces = filter(lambda c: isinstance(c, umlInterface), model.getAllParts())
		self.setInterfaceList(interfaces)

		useCases = filter(lambda c: isinstance(c, umlUseCase), model.getAllParts())
		self.setUseCaseList(useCases)

	def setUmlClass(self, umlClass):
		self.umlClass = umlClass
	def getUmlClass(self):
		return self.umlClass
	
	def setUmlAttribute(self, umlAttribute):
		self.umlAttribute = umlAttribute
	def getUmlAttribute(self):
		return self.umlAttribute
	
	def setUmlOperation(self, umlOperation):
		self.umlOperation = umlOperation
	def getUmlOperation(self):
		return self.umlOperation

	def setUmlInterface(self, umlInterface):
		self.umlInterface = umlInterface
	def getUmlInterface(self):
		return self.umlInterface

	def setUmlUseCase(self, umlUseCase):
		self.umlUseCase = umlUseCase
	def getUmlUseCase(self):
		return self.umlUseCase
	
	def getDocumentation(self,inTaggedValues):
		for aTaggedValue in inTaggedValues:
			if aTaggedValue.tag =='documentation':
#				print 'documentation', aTaggedValue.value
				return aTaggedValue.value
	#UML13.Actor
	def getActor(self,aUseCase):
		for ae in aUseCase.associationEnd:
			#print 'ae.association'
			for cnn in ae.association.connection:
				if isinstance(cnn.type, UML13.Actor):
					#print 'ae.association.connection.type.name', cnn.type.name
					return cnn.type.name
	#---------------------------------------------------------------------------
	def getAttributes(self,aClassInfo):
		#attributes = self.aModelInfo.getAttributes(aClassInfo)

		return filter(lambda c: isinstance(c, self.getUmlAttribute()), \
			aClassInfo.allFeatures())
	
	def getOperations(self,aClassInfo):
		#operations = self.aModelInfo.getOperations(aClassInfo)
		return filter(lambda c: isinstance(c, self.getUmlOperation()), \
			aClassInfo.allFeatures())
	#---------------------------------------------------------------------------
	def getBehavioralFeatureInfo(self,inOperation):
		return UML14.getBehavioralFeatureInfo(inOperation)
	
	def getAttributeInfo(self,inAttribute):
		return UML14.getAttributeInfo(inAttribute)


#---------------------------------------------------------------------------
# if __name__ == "__main__":
# 	aModelInfo = ModelInfo()
# 	print aModelInfo.getJavaType('C')
