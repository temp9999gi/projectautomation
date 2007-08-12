# -*- coding: utf-8 -*-
from domain.QueryXmlInfo import *
from domain.BizComp import *
from domain.ActivityClassInfo import *
from domain.TableInfo import *
from domain.Process import *

class QueryXmlApp:
	def __init__(self, CONS):
		self.QueryXmlInfoList=[]
		self.CONS=CONS
		
	def getKlassList(self, inRs):
		masterId = ''
		oldMasterId = ''
		oldda_Query_ID = ''
		oldTable_Eng=''
		for row  in inRs:
			try:
				processID, process_Nm, service_Xml_Nm, service_Xml_Id, \
				biz_Comp_Nm, biz_Comp_Id, table_Eng, table_Kor, crud_Type = row[0:9]
				masterId = service_Xml_Id
			except (ValueError):
				print 'Count Error'
				sys.exit(2)

			if processID == '': break
			if oldMasterId != masterId:
				aQueryXmlInfo = QueryXmlInfo()
				aQueryXmlInfo.setAttributes(service_Xml_Nm, service_Xml_Id)
				self.QueryXmlInfoList.append(aQueryXmlInfo)
				oldTable_Eng=''
			oldMasterId = masterId

			if table_Eng is not None:
				if oldTable_Eng != table_Eng:
					aTableInfo = TableInfo()
					aTableInfo.setAttributes(table_Kor, table_Eng, crud_Type)
					aQueryXmlInfo.addTableList(aTableInfo)
				oldTable_Eng = table_Eng
				self.createMethod(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID)
				
		return self.QueryXmlInfoList

	def createMethod(self, aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID):
		if crud_Type.find('R')>=0:
			crudGubun='find'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)

		if crud_Type.find('U')>=0:
			crudGubun='update'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)

		if crud_Type.find('D')>=0:
			crudGubun='delete'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)

		if crud_Type.find('C')>=0:
			crudGubun='add'
			self.createMethodCore(aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun)

	def createMethodCore(self, aTableInfo, table_Kor, table_Eng, crud_Type, process_Nm, processID, crudGubun):
			aMethodInfo = MethodInfo()
			aMethodInfo.setAttributes(table_Kor, table_Eng, crudGubun, process_Nm, processID)
			self.setMethod(aTableInfo, aMethodInfo, crudGubun, table_Eng, processID)
			aTableInfo.addMethodList(aMethodInfo)

	def setMethod(self, aTableInfo, aMethodInfo, crudGubun, table_Eng, processID):
		tableIdCapWord = aCommonUtil.getCapWord(table_Eng)
		tmpMethodId = crudGubun + tableIdCapWord
		#예, R이 두개인 경우 처리
		if aTableInfo.getMethodDictByMethodId(tmpMethodId) is None:
			aMethodInfo.setMethodId(tmpMethodId)
			aTableInfo.setMethodDictByMethodId(aMethodInfo.methodId, aMethodInfo)
		else:
			aMethodInfo.setMethodId(crudGubun + tableIdCapWord + '__' + processID + '_XXX')


if __name__ == '__main__':
	pass
