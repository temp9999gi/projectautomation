# -*- coding: utf-8 -*-
from domain.ServiceXmlInfo import *
##from domain.BizComp import *
from domain.ActivityClassInfo import *
from domain.TableInfo import *
##from domain.Process import *
import sys
class ActivityClassApp:
	def __init__(self, CONS, aFieldApp):
		self.ActivityClassList=[]
		self.CONS=CONS
		self.aFieldApp= aFieldApp
		
	def getKlassList(self, inRs):
		masterId = ''
		oldMasterId = ''
		oldda_Query_ID = ''
		oldTable_Eng=''
		for row  in inRs:
			try:
				process_Nm, processID, da_Query_ID, table_Kor, table_Eng, table_Cd, crud_Type = row[0:7]
						
				masterId = da_Query_ID
			except (ValueError):
				print 'Count Error'
				sys.exit(2)

			if processID == '': break
			if oldMasterId != masterId:
				aActivityClassInfo = ActivityClassInfo()
				aActivityClassInfo.setAttributes(da_Query_ID)
				self.ActivityClassList.append(aActivityClassInfo)
				oldTable_Eng=''
			oldMasterId = masterId
			if oldTable_Eng != table_Eng:
				aTableInfo = TableInfo()
				aTableInfo.setAttributes(table_Kor, table_Eng, table_Cd, crud_Type)
				aActivityClassInfo.addTableList(aTableInfo)
				#aFieldApp------------------------------------------------------
				#???????????
				aTableInfo.fieldList = self.aFieldApp.getFieldDictByTableId(aTableInfo.table_Cd)
				aTableInfo.pkColumnList = self.aFieldApp.getPkColumnsDictByTableId(aTableInfo.table_Cd)
				aTableInfo.nonPkColumnList = self.aFieldApp.getNonPkColumnDictByTableId(aTableInfo.table_Cd)
			oldTable_Eng = table_Eng
			self.createMethod(aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID)

		return self.ActivityClassList

	def createMethod(self, aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID):
		if crud_Type.find('C')>=0:
			crudGubun='add'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID, crudGubun)

		if crud_Type.find('D')>=0:
			crudGubun='delete'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID, crudGubun)
			
		if crud_Type.find('U')>=0:
			crudGubun='update'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID, crudGubun)
			
		if crud_Type.find('R')>=0:
			crudGubun='find'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID, crudGubun)

		if crud_Type.find('S')>=0:
			crudGubun='save'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID, crudGubun)


	def createMethodCore(self, aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID, crudGubun):
			aMethodInfo = MethodInfo()
			aMethodInfo.setAttributes(table_Kor, table_Eng, crudGubun, process_Nm, processID)
			self.setMethod(aTableInfo, aMethodInfo, crudGubun, table_Eng, table_Cd, processID)
			aMethodInfo.setTable(aTableInfo) #aMethod와 Table Info 관계 설정
			aMethodInfo.setMethodKor()
			aTableInfo.addMethodList(aMethodInfo)

	def setMethod(self, aTableInfo, aMethodInfo, crudGubun, table_Eng, table_Cd, processID):
		aMethodInfo.setMethod(aTableInfo, aMethodInfo, crudGubun, table_Eng, table_Cd, processID)



if __name__ == '__main__':
	pass
