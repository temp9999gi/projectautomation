# -*- coding: utf-8 -*-
# start
from CommonUtil import *

class ClassAttribute :
	def setClassAttribute(self, attributeName, attributeType):
		self.attributeName = attributeName
		self.attributeType  =  attributeType
		aCommonUtil = CommonUtil()
		self.upperNameIndex0 = aCommonUtil.getUpperNameIndex0(attributeName)
		

