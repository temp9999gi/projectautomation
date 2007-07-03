# -*- coding: utf-8 -*-
from CommonUtil import *
# start
#-------------------------------------------------------------------------------
class Klass:
	def __init__(self):
		self.fieldList = []

	def setAttributes(self, klassName):
		self.klassName = klassName
		self.writer			=" "
		self.writeDate		=" "
		self.subSystemName	=" "
		
		self.lowerKlassName	=""
		self.setLowerKlassNameIndex0(klassName)

	def setLowerKlassNameIndex0(self, klassName):
		self.lowerKlassName = string.lower(klassName[0]) + klassName[1:]

	def addFieldList(self, aField):
		self.fieldList.append(aField)
	#---------------------------------------------------------------------------
	def setWriter(self, writer):
		self.writer = writer
	def setWriteDate(self, writeDate):
		self.writeDate = writeDate
	def setSubSystemName(self, subSystemName):
		self.subSystemName = subSystemName


