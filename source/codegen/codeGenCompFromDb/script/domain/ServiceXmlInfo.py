# -*- coding: utf-8 -*-
from CommonUtil import *
# start
#-------------------------------------------------------------------------------
aCommonUtil = CommonUtil()


class ServiceXmlInfo:
	def __init__(self):
		#self.processList = []
		self.tableInfoList = []
		self.bizCompList=[]
		self.bizCompDictByBizCompId={}
		
	def setAttributes(self, service_Xml_Nm, service_Xml_Id, processID):
		self.service_Xml_Nm, self.service_Xml_Id = service_Xml_Nm, service_Xml_Id
		self.processID = processID

		klassName = self.service_Xml_Id
		self.lowerKlassName	=""
		if klassName is not None:
			self.setLowerKlassNameIndex0(klassName)

	def setLowerKlassNameIndex0(self, klassName):
		self.lowerKlassName = aCommonUtil.getLowerNameIndex0(klassName)


	def addTableList(self, obj):
		self.tableInfoList.append(obj)
	#---------------------------------------------------------------------------
	# App Comp 생성시 사용
	def addBizComp(self, obj):
		self.bizCompList.append(obj)
		
	def setBizCompDictByBizCompId(self, key, item):
		self.bizCompDictByBizCompId[key] = item
	def getBizCompDictByBizCompId(self, key):
		try:
			out = self.bizCompDictByBizCompId[key]
			return out
		except KeyError:
			return None
		
	#---------------------------------------------------------------------------


