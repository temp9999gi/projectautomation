# -*- coding: utf-8 -*-
# start

from MetaInfo import *
'''
<UML:Operation xmi.id="UMLOperation.10" name="insert" visibility="public" 
isSpecification="false" ownerScope="instance" isQuery="false" concurrency="sequential" 
isRoot="false" isLeaf="false" isAbstract="false" specification="Specification" owner="UMLClass.6">
'''
class ClassOperation(MetaInfo):
	def __init__(self):	
		MetaInfo.__init__
		self.operationParameterList = []
		self.methodParameterString = ''
		self.operationReturnType = ''
		#self.operationDocumentation = ''
		
	def addOperationParameterList(self, aModelInfo, aMethodParameter):
		self.operationParameterList.append(aMethodParameter)
		if aMethodParameter.kind ==  'return':
			returnType = aModelInfo.getDataTypeByXmiId(aMethodParameter.type)
			self.setOperationReturnType(returnType)
		if aMethodParameter.kind ==  'in':
			typeName = aModelInfo.getDataTypeByXmiId(aMethodParameter.type)
			parameterString = '''%(typeName)s : %(parameterName)s ''' \
				% {'typeName': typeName, 'parameterName': aMethodParameter.name}
			self.setMethodParameterString(parameterString)			
	
	def setOperationReturnType(self, operationReturnType):
		self.operationReturnType = operationReturnType
	def getOperationReturnType(self):
		return self.operationReturnType		
		
	def setMethodParameterString(self, methodParameterString):
		if self.methodParameterString == '':
			self.methodParameterString = methodParameterString
		else:
			self.methodParameterString = self.methodParameterString + ', ' +methodParameterString
			
	def getMethodParameterString(self):
		return self.methodParameterString 		
	

	

'''
<UML:Parameter xmi.id="UMLParameter.11" name="" visibility="public" isSpecification="false" 
kind="return" behavioralFeature="UMLOperation.10" type="X.31"/>
'''
class MethodParameter(MetaInfo):
	def __init__(self):
		MetaInfo.__init__


	
	

