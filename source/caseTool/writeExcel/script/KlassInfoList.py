# -*- coding: utf-8 -*-
'''애는 뭐하는 얘나? 음 뭐냐면
일단은 말야.....
액셀을 읽어서 테이블의 리스트를 만드는애다.
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
		return self.klassList
##		if self.deliverableType=='Class':
##			return self.classInfoList
##		if self.deliverableType=='Interface':
##			return self.interfaceList
