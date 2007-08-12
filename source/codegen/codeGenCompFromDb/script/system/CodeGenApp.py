# -*- coding: utf-8 -*-
from domain.BizComp import *
from domain.Process import *
from domain.ActivityClassInfo import *
from domain.TableInfo import *

class CodeGenApp:
	def __init__(self, CONS):
		self.bizCompList=[]
		self.CONS=CONS
		
	def getKlassList(self, inRs):
		masterId = ''
		oldMasterId = ''
		oldda_Query_ID = ''
		oldTable_Eng=''
		for row  in inRs:
			try:
				process_Nm, processID, biz_Comp_Nm, biz_Comp_Id, da_Query_ID, table_Kor, table_Eng, crud_Type = row[0:8]
				masterId = biz_Comp_Id
			except (ValueError):
				print 'ValueError'
				sys.exit(2)

			if processID == '': break
			if oldMasterId != masterId:
				aBizComp = BizComp()
				aBizComp.setAttributes(biz_Comp_Nm, biz_Comp_Id)
				self.bizCompList.append(aBizComp)
				oldda_Query_ID=''
				oldTable_Eng=''
			oldMasterId = masterId

			if da_Query_ID is not None:
				if oldda_Query_ID != da_Query_ID:
					aActivityClassInfo = ActivityClassInfo()
					aActivityClassInfo.setAttributes(da_Query_ID)
					aBizComp.addActivityClassInfoList(aActivityClassInfo)
					oldTable_Eng=''
				oldda_Query_ID = da_Query_ID

				if oldTable_Eng != table_Eng:
					aTableInfo = TableInfo()
					aTableInfo.setAttributes(table_Kor, table_Eng, crud_Type)
					aActivityClassInfo.addTableList(aTableInfo)
				oldTable_Eng = table_Eng
				self.createMethod(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID)
				
		return self.bizCompList

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
			self.setMethodId(aTableInfo, aMethodInfo, crudGubun, table_Eng, processID)
			aTableInfo.addMethodList(aMethodInfo)

	def setMethodId(self, aTableInfo, aMethodInfo, crudGubun, table_Eng, processID):
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
