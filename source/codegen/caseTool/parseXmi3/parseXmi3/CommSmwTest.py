# -*- coding: utf-8 -*-
###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2002 by:																								 #
																											 #
###########################################################################
#
#			 Authors: kusung
# Last Modified: $Date: 2007/01/21 15:16:39 $
#
"""Attempts to load a model defined in an xmi file into pymerase.

Currently requires the novosoft uml reader, which implies the need for jython.
It was currently tested with 0.4.19 downloaded from the argo cvs.
"""
# import system packages
from __future__ import nested_scopes

from smw.metamodel import UML14
from smw.metamodel import UML13
from smw.io import loadModel
from smw.io import ModelInfo

import sys
import logging
# import utils
##import xmiCommonUtil as xmiUtil

##def parseXMI_test(model):
##
##	aAttributes = filter(lambda c: isinstance(c, UML13.Attribute), model.getAllParts())
##
##	for attr in aAttributes:
##		#UML:Expression body를 가지고 온다.
##		print 'attr.initialValue.body', attr.initialValue.body
####		aClassAttribute = getAttributeByXmiId(attr.__XMIid__)
####		aInitialValue = getInitialValueByXmiId( attr.initialValue.__XMIid__)
####		aClassAttribute.setInitialValue(aInitialValue)

def classTest(model):
	"""Convert external UML model to pymerase's model classes.
	"""
	if isinstance(model, UML13.Model):
		umlClass = UML13.Class
##		umlParser = uml13Parser(pymeraseConfig)
	elif isinstance(model, UML14.Model):
		umlClass = UML14.Class
##		umlParser = uml14Parser(pymeraseConfig)
	else:
		raise ValueError("Pymerase only supports UML 1.3 and 1.4 metamodel")

	#원본 classes = filter(lambda c: isinstance(c, umlClass), model.ownedElement)
	classes = filter(lambda c: isinstance(c, umlClass), model.getAllParts())
	
	#tags = filter(lambda c: isinstance(c, umlClass), model.getAllParts())
	
	for xmiClass in classes:
		attributeTest(xmiClass)
		##writeOperationTest(xmiClass)
		#print xmiClass
		#xmiClass.name
		
def attributeTest(xmiClass):
	
	attributes = filter(lambda c: isinstance(c, UML13.Attribute), xmiClass.feature)
	for attr in attributes:
		# 번호	속성명		가시성	타입	기본값	설명
		bb = UML14.getAttributeInfo(attr)
		print '------------UML14.getAttributeInfo(attr)', bb
		visibility, name, typeName, initialValueBody = UML14.getAttributeInfo(attr)
		getDocumentation(attr.taggedValue)
##		for x in attr.taggedValue.items:
##			print '44444attr.taggedValue.items', x


		
		#print 'visibility', visibility
		
##		aa = UML14.fromAttributeToString(attr)
##		print 'UML14.fromAttributeToString(attr)', aa

def getDocumentation(inTaggedValues):
	for aTaggedValue in inTaggedValues:
		if aTaggedValue.tag =='documentation':
			print 'documentation', aTaggedValue.value
			return aTaggedValue.value


		
def writeOperationTest(xmiClass):
	operations = filter(lambda c: isinstance(c, UML13.Operation), xmiClass.feature)
	for x in operations:
		# 번호	오퍼레이션명		가시성	파라미터	반환타입	설명
##		aa = UML14.fromBehavioralFeatureToString(x)
##		print '22222---------fromBehavioralFeatureToString(x)', aa
		bb = UML14.getBehavioralFeatureInfo(x)
		print '33333---------getBehavioralFeatureInfo(x)', bb

		#?????parameterStr = getParameter(x.parameter)
		
##		print 'operations name: [',x.name,']'
##		print 'operations visibility: [',x.visibility,']'
##		print 'operations parameterStr: [',parameterStr,']'

def getParameter(inParameters):
	parameterStr=''
	for aParameter in inParameters:
		if aParameter.name:
			parameterStr = parameterStr + aParameter.name + ':' + aParameter.type.name + ', '
			print 'parameterStr', parameterStr

		aa = UML14.fromParameterToString(aParameter)
		print 'UML14.fromParameterToString(aParameter):', aa
		
##		print '-start-----------'
##		print 'aParameter.name', aParameter.name
##		print 'aParameter.kind', aParameter.kind
##		print 'aParameter.type.name', aParameter.type.name
##		print '-end-----------'
	return parameterStr

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

def namespaceTest(model):
		#classes = filter(lambda c: isinstance(c, umlClass), model.getAllParts())
	for xx in model.getAllParts():
		if isinstance(xx, UML13.UseCase):
			# print 'xx.name[',xx.name,']'
			aMyTempVar=MyTempVar()
			getNamespace(xx,aMyTempVar)
			out = aMyTempVar.getRootNamespace()
			setRootNamespace(xx,out)
			print 'getRootNamespace(xx)[',getRootNamespace(xx),']'
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
def useCaseTest(model):
	for xx in model.getAllParts():
		if isinstance(xx, UML13.UseCase):
			print 'xx[',xx.name,']'

if __name__ == "__main__":
	from Constants import *
	CONS = Constants()
	inFile  = CONS.INPUT_DIR / sys.argv[1]
	inFile = str(inFile)

	#model = loadModel(inFile)
	aModelInfo= loadModel(inFile)
	model = aModelInfo.getModel()
	useCaseTest(model)
	
##	for xx in model.getAllParts():
##		print 'xx.name[',xx.name,']'

	#UML:UseCase
	
##	myTaggedValues = filter(lambda c: isinstance(c, aModelInfo.streamer.metamodel.TaggedValue), \
##		aModelInfo.streamer.objectById.values())
	#getTaggedValue(myTaggedValues)
	#print 'myTaggedValues', myTaggedValues

	#parseXMI_test(model)
	#classTest(aModelInfo.getModel())
	#attributeTest(model)
	#writeOperationTest(model)
	
	#namespaceTest(aModelInfo.getModel())
	