﻿# -*- coding: utf-8 -*-
'''애는 뭐하는 얘나? 음 뭐냐면
'''
# start
class KlassInfoList:
	def __init__(self):
		self.klassList = []
	def setKlassList(self, klassList):
		self.klassList = klassList
	def getKlassList(self):
		return self.klassList

	def setDaoXmlFileName(self, daoXmlFileName):
		self.daoXmlFileName = daoXmlFileName
		
	def setPackagePath(self, packagePath):
		self.packagePath = packagePath
	def getPackagePath(self):
		return self.packagePath
