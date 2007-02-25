# -*- coding: utf-8 -*-
'''애는 뭐하는 얘나? 음 뭐냐면
'''
# start
class KlassInfoList:
	def __init__(self):
		self.klassList = []
		self.classInfoList = []
		self.packagePath=''

	def setKlassList(self, klassList):
		self.klassList = klassList
	def getKlassList(self):
		return self.klassList

	def setClassInfoList(self, classInfoList):
		self.classInfoList= classInfoList

	def setInterfaceList(self, interfaceList):
		self.interfaceList= interfaceList

	def setDefinitionType(self, deliverableType):
		self.deliverableType = deliverableType
	def getDefinitionType(self):
		return self.deliverableType
	
	def setReaderAppEnv(self, aReaderAppEnv):
		self.aReaderAppEnv = aReaderAppEnv
	def getReaderAppEnv(self):
		return self.aReaderAppEnv
	
	def getClassListOrInterfaceList(self):
		return self.klassList
