#*- coding: utf-8 -*-

import string
import sys
import xml.dom.minidom

class ClassInfo :
	def __init__(self, className, attributeList, pkList):
		self.className = className
		self.setLowerClassNameIndex0(className)
		
		self.attributeList = attributeList #[] 
		self.pkList = pkList #[] 		
		self.setPkString(pkList)
		
	def setLowerClassNameIndex0(self, className):
		self.lowerClassName = string.lower(className[0]) + className[1:]
		
	def setPkString(self, pkList):
		s = ''
		for x in pkList:
			 s = s + (x.attributeType + ' ' + x.attributeName) + ', '
			 
		self.pkString = s[:len(s)-2]
		
		# print self.pkString,'ssssssssss'

class PrimaryKey :
	def __init__(self, attributeName, attributeType):
		self.attributeName = attributeName
		self.attributeType  =  attributeType
		

class ClassAttribute :
	def __init__(self, attributeName, attributeType):
		self.attributeName = attributeName
		self.setUpperNameIndex0(attributeName)
		
		self.attributeType  =  attributeType
		
	def setUpperNameIndex0(self, attributeName):
		self.upperNameIndex0 = string.upper(attributeName[0]) + attributeName[1:]
