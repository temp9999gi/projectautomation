# start
from CommonUtil import *
aCommonUtil = CommonUtil()


class ActivityClassInfo:
	def __init__(self):
		self.tableList = []

	def setAttributes(self, da_Query_ID):
		self.da_Query_ID = da_Query_ID
		self.classId = aCommonUtil.getClassName(da_Query_ID)
		self.packageId = string.lower(self.classId[0]) + self.classId[1:]
		self.lowerClassId = string.lower(self.classId[0]) + self.classId[1:]
		
	def addTableList(self, obj):
		self.tableList.append(obj)
		
		

