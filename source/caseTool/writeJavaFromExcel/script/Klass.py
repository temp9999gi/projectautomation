# -*- coding: utf-8 -*-
from CommonUtil import *
# start
class Klass:
	def __init__(self):
		self.fieldList = []

	def setAttributes(self, klassName):
		self.klassName = klassName
		self.writer			=" "
		self.writeDate		=" "
		self.subSystemName	=" "

	def addFieldList(self, aField):
		self.fieldList.append(aField)
		
	def setWriter(self, writer):
		self.writer = writer
	def setWriteDate(self, writeDate):
		self.writeDate = writeDate
	def setSubSystemName(self, subSystemName):
		self.subSystemName = subSystemName


