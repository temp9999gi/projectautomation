# -*- coding: utf-8 -*-
from domain.ServiceXmlInfo import *
from domain.BizComp import *
from domain.ServiceXmlInfo import *
from domain.TableInfo import *
from domain.Process import *

class ServiceXmlApp:
	def __init__(self, CONS):
		self.ActivityClassList=[]
		self.CONS=CONS
		
	def getKlassList(self, inRs):
		masterId = ''
		oldMasterId = ''
		oldda_Query_ID = ''
		oldTable_Eng=''
		for row  in inRs:
			try:
				process_Nm, processID, da_Query_ID, table_Kor, table_Eng, crud_Type = row[0:6]
				masterId = da_Query_ID
			except (ValueError):
				print 'Count Error'
				sys.exit(2)

			if processID == '': break
			if oldMasterId != masterId:
				aServiceXmlInfo = ServiceXmlInfo()
				aServiceXmlInfo.setAttributes(da_Query_ID)
				self.ActivityClassList.append(aServiceXmlInfo)
				oldTable_Eng=''
			oldMasterId = masterId
			if oldTable_Eng != table_Eng:
				aTableInfo = TableInfo()
				aTableInfo.setAttributes(table_Kor, table_Eng, crud_Type)
				aServiceXmlInfo.addTableList(aTableInfo)
			oldTable_Eng = table_Eng
			self.createMethod(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID)

		return self.ActivityClassList

	def createMethod(self, aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID):
		if crud_Type.find('C')>=0:
			crudGubun='add'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)

		if crud_Type.find('D')>=0:
			crudGubun='delete'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)
			
		if crud_Type.find('U')>=0:
			crudGubun='update'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)
			
		if crud_Type.find('R')>=0:
			crudGubun='find'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)

	def createMethodCore(self, aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun):
			aMethodInfo = MethodInfo()
			aMethodInfo.setAttributes(table_Kor, table_Eng, crudGubun, process_Nm, processID)
			self.setMethod(aTableInfo, aMethodInfo, crudGubun, table_Eng, processID)
			aTableInfo.addMethodList(aMethodInfo)

	def setMethod(self, aTableInfo, aMethodInfo, crudGubun, table_Eng, processID):
		tableIdCapWord = aCommonUtil.getCapWord(table_Eng)
		tmpMethodId = crudGubun + tableIdCapWord
		#R이 두개인 경우 처리
		if aTableInfo.getMethodDictByMethodId(tmpMethodId) is None:
			aMethodInfo.setMethodId(tmpMethodId)
			aTableInfo.setMethodDictByMethodId(aMethodInfo.methodId, aMethodInfo)
		else:
			aMethodInfo.setMethodId(crudGubun + tableIdCapWord + '__' + processID + '_XXX')



if __name__ == '__main__':
	pass
