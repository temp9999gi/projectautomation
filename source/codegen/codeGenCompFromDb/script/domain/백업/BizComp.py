# -*- coding: utf-8 -*-
from CommonUtil import *
# start
#-------------------------------------------------------------------------------
##aCommonUtil = CommonUtil()
class BizComp:
	def __init__(self):
		self.processList = []
		self.ActivityClassInfoList = []
		
	def setAttributes(self, biz_Comp_Nm, biz_Comp_Id):
		self.biz_Comp_Nm, self.biz_Comp_Id = biz_Comp_Nm, biz_Comp_Id

		klassName = self.biz_Comp_Id
		self.lowerKlassName	=""
		if klassName is not None:
			self.setLowerKlassNameIndex0(klassName)

	def setLowerKlassNameIndex0(self, klassName):
		self.lowerKlassName = string.lower(klassName[0]) + klassName[1:]

	def addProcessList(self, aProcess):
		self.processList.append(aProcess)

	def addActivityClassInfoList(self, aActivityClassInfo):
		self.ActivityClassInfoList.append(aActivityClassInfo)






