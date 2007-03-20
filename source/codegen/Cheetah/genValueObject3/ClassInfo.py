# -*- coding: utf-8 -*-
#import string
# start
from CommonUtil import *

class ClassInfo :
	def __init__(self):
		self.classAttributeList = []
	def setAttributes(self, className, packagePath):
		self.className = className
		self.packagePath = packagePath
		aCommonUtil = CommonUtil()
		self.lowerClassName = aCommonUtil.getLowerNameIndex0(className)
	def addClassAttributeList(self, aClassAttribute):
		self.classAttributeList.append(aClassAttribute)		

