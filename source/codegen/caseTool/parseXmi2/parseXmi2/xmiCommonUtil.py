# -*- coding: utf-8 -*-

from ClassInfo import *

from ClassAttribute import *
from ClassOperation import *
from XmiDataType import *

from ModelInfo import *
from TaggedValue import *

from Constants import *
CONS = Constants()

from CommonUtil import *
ComUtil = CommonUtil()

import logging

log = logging.getLogger('xmiCommonUtil')

def getClass(attrs):
	aClassInfo = ClassInfo()
	log.debug("-aClassInfo--------------------------------------------------")
	# attrs : AttributesImpl instance
	for attrName in attrs.getNames():	# 속성 정보를 출력한다 (속성 이름, 속성 값)
		if attrName == 'name':
			aClassInfo.setClassName(attrs.getValue(attrName))
		if attrName == 'xmi.id':
			aClassInfo.setXmiId(attrs.getValue(attrName))
		if attrName == 'namespace':
			aClassInfo.setNamespace(attrs.getValue(attrName))
		log.debug("attrName: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))

	return aClassInfo

def getAttribute(attrs):
	log.debug("-aClassAttribute--------------------------------------------------")
	aClassAttribute = ClassAttribute()
	for attrName in attrs.getNames():	# 속성 정보를 출력한다 (속성 이름, 속성 값)
		if attrName == 'name':
			attributeName=attrs.getValue(attrName)
			aClassAttribute.setAttributeName(attributeName)
		if attrName == 'type':
			aClassAttribute.setTypeXmiId(attrs.getValue(attrName))
		if attrName == 'visibility':
			aClassAttribute.setVisibility(attrs.getValue(attrName))
		if attrName == 'owner':
			aClassAttribute.setOwner(attrs.getValue(attrName))
		if attrName == 'xmi.id':
			aClassAttribute.setXmiId(attrs.getValue(attrName))
			
		objectName ='aClassAttribute'
		if attrName in ['xmi.uuid']:
			aClassAttribute.defineMethod('xmiUuid')
			exec getStringCallSetterMethod(objectName, 'xmiUuid')

		log.debug("attrName: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	return aClassAttribute

# <UML:Operation xmi.id="UMLOperation.14" name="update" visibility="public"
# isSpecification="false" ownerScope="instance" isQuery="false" concurrency="sequential"
# isRoot="false" isLeaf="false" isAbstract="false" specification="" owner="UMLClass.6"/>
def getOperation(attrs):
	aClassOperation = ClassOperation()
	log.debug("-aClassOperation--------------------------------------------------")
	for attrName in attrs.getNames():	# 속성 정보를 출력한다 (속성 이름, 속성 값)
		if attrName == 'xmi.id':
			aClassOperation.setXmiId(attrs.getValue(attrName))
		if attrName == 'name':
			aClassOperation.setName(attrs.getValue(attrName))
		if attrName == 'owner':
			aClassOperation.setOwner(attrs.getValue(attrName))
		if attrName == 'visibility':
			aClassOperation.setVisibility(attrs.getValue(attrName))
			
		objectName ='aClassOperation'
		if attrName in ['owner']:
			aClassOperation.defineMethod(attrName)
			exec getStringCallSetterMethod(objectName, attrName)

		log.debug("attrName: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	return aClassOperation

#<UML:Parameter xmi.id="UMLParameter.11" name="inID" visibility="public"
#isSpecification="false" kind="in" behavioralFeature="UMLOperation.10" type="X.31"/>
def getParameter(attrs):
	aMethodParameter = MethodParameter()
	log.debug("-aMethodParameter--------------------------------------------------")
	for attrName in attrs.getNames():	# 속성 정보를 출력한다 (속성 이름, 속성 값)
		if attrName == 'xmi.id':
			aMethodParameter.setXmiId(attrs.getValue(attrName))
		if attrName == 'name':
			aMethodParameter.setName(attrs.getValue(attrName))
		if attrName == 'visibility':
			aMethodParameter.setVisibility(attrs.getValue(attrName))
			
		if attrName in ['kind','behavioralFeature','type']:
			aMethodParameter.defineMethod(attrName)
			objectName='aMethodParameter'
			exec getStringCallSetterMethod(objectName, attrName)
			
			##aMethodParameter.setVisibility(attrs.getValue(attrName))

		log.debug("attrName: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	return aMethodParameter

def getStringCallSetterMethod(objectName, attrName):
	defineMethodString = '''%(objectName)s.set%(MethodNameUpperIndex0)s(%(objectName)s, attrs.getValue(attrName))''' \
	% {'MethodNameUpperIndex0': ComUtil.getUpperNameIndex0(attrName),\
	'objectName': objectName}
	return defineMethodString

#<UML:DataType xmi.id="X.30" name="String" visibility="public" isSpecification="false" isRoot="false" isLeaf="false" isAbstract="false"/>
def getDataType(attrs):
	aXmiDataType = XmiDataType()
	log.debug("-aClassOperation--------------------------------------------------")
	for attrName in attrs.getNames():	# 속성 정보를 출력한다 (속성 이름, 속성 값)
		if attrName == 'xmi.id':
			aXmiDataType.setXmiId(attrs.getValue(attrName))
		if attrName == 'name':
			aXmiDataType.setName(attrs.getValue(attrName))
	return aXmiDataType

def isDocumentationOfTag(attrs):
	for attrName in attrs.getNames():
		if attrName == 'tag':
			if attrs.getValue(attrName) == 'documentation':
				return True
			else:
				return False
'''
<UML:TaggedValue xmi.id="X.35" tag="documentation" value="�굹�씠" modelElement="UMLAttribute.9"/>
'''
def getTaggedValue(attrs):
	aTaggedValue = TaggedValue()
	log.debug("-aTaggedValue--------------------------------------------------")
	for attrName in attrs.getNames():	# 속성 정보를 출력한다 (속성 이름, 속성 값)
		if attrName == 'xmi.id':
			aTaggedValue.setXmiId(attrs.getValue(attrName))
		if attrName == 'tag':
			aTaggedValue.setTag(attrs.getValue(attrName))
		if attrName == 'value':
			aTaggedValue.setValue(attrs.getValue(attrName))
		if attrName == 'modelElement':
			aTaggedValue.setModelElement(attrs.getValue(attrName))
		log.debug("attrName: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	return aTaggedValue


#<UML:Attribute xmi.id="UMLAttribute.7" name="name" visibility="public" 
# isSpecification="false" ownerScope="instance" changeability="changeable" 
# targetScope="instance" type="X.32" owner="UMLClass.6">
#  <UML:Attribute.initialValue>
#	<UML:Expression xmi.id="X.35" body="'default1'"/>
#  </UML:Attribute.initialValue>
#</UML:Attribute>
def getAttributeInitialValue(attrs):
	aAttributeInitialValue = AttributeInitialValue()
	log.debug("-getAttributeInitialValue--------------------------------------------------")
	for attrName in attrs.getNames():	# 속성 정보를 출력한다 (속성 이름, 속성 값)
		objectName='aAttributeInitialValue'
		if attrName == 'xmi.id':
			aAttributeInitialValue.setXmiId(attrs.getValue(attrName))

		if attrName in ['body']:
			aAttributeInitialValue.defineMethod(attrName)
			exec getStringCallSetterMethod(objectName, attrName)
			
		objectName ='aAttributeInitialValue'
		if attrName in ['xmi.uuid']:
			aAttributeInitialValue.defineMethod('xmiUuid')
			exec getStringCallSetterMethod(objectName, 'xmiUuid')

		log.debug("attrName: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	return aAttributeInitialValue


from xml.dom import minidom	
from XMI import *
def getXMI(xschemaFileName):

	if xschemaFileName:
		doc = minidom.parse(xschemaFileName)
	else:
		doc = minidom.parseString(xschema)
		
	xmi = doc.getElementsByTagName('XMI')[0]
	xmiver = str(xmi.getAttribute('xmi.version'))
	log.debug("XMI version: %s", xmiver)
	if xmiver >= "1.2":
		log.debug("Using xmi 1.2+ parser.")
		# XMI = XMI1_2()
	elif xmiver >= "1.1":
		log.debug("Using xmi 1.1+ parser.")
		XMI = XMI1_1()
	else:
		log.debug("Using xmi 1.1+ parser.")
		XMI = XMI1_0()
		
	return XMI	

from smw.metamodel import UML14
from smw.metamodel import UML13
from smw.io import loadModel
def loadInitialValue(aModelInfo, inFile):
	model = loadModel(inFile)	
	aAttributes = filter(lambda c: isinstance(c, UML13.Attribute), model.getAllParts())

	for attr in aAttributes:
		#UML:Expression body를 가지고 온다.
		#print 'attr.initialValue.body', attr.initialValue.body
		aClassAttribute = aModelInfo.getClassAttributeByXmiUuid(attr.__XMIid__())
		#smw의 xmi id에 아래와 같은 값이들어 있다.
		# xmiid는 xmi파일의 uuid를 가지고 있음
##[Dbg]>>> attr.__XMIid__()
##u'DCE:0A7DDAD0-D00C-482E-A95B-6AF0A9C65A79'
		aInitialValue = aModelInfo.getAttributeInitialValueDictByXmiUuid(attr.initialValue.__XMIid__())
		if aInitialValue:
			aClassAttribute.setInitialValue(aInitialValue)	


