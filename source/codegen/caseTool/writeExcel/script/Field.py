# start
#from DbAndJavaTypeMapper import *
from CommonUtil import *

class Field:		
	def setAttributes(self, name, visibility, typeName, initialValueBody, \
							documentation):
		self.name                   =name
		self.visibility             =visibility
		self.typeName               =typeName
		self.initialValueBody       =initialValueBody
		self.documentation          =documentation	

class Operation:
	def setAttributes(self, name, visibility, parameterString, returnTypeName, \
							documentation):
		self.name                   =name
		self.visibility             =visibility
		self.parameterString        =parameterString
		self.returnTypeName       	=returnTypeName
		self.documentation          =documentation

class ClassDoc:
	def setAttributes(self, packagePath, documentation):
		self.packagePath =packagePath
		self.documentation =documentation
