# -*- coding: utf-8 -*-
# start
from CommonUtil import *
from MetaInfo import *

class TaggedValue(MetaInfo):
	def __init__(self):	
		MetaInfo.__init__
		self.value = ''
		
	def setModelElement(self, modelElement):
		self.modelElement = modelElement
	def getModelElement(self):
		return self.modelElement
	def setTag(self, tag):
		self.tag = tag
	def getTag(self):
		return self.tag
	def setValue(self, value):
		self.value = value
	def getValue(self):
		return self.value
