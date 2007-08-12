# -*- coding: utf-8 -*-
from domain.QueryXmlInfo import *
##from domain.BizComp import *
from domain.ActivityClassInfo import *
from domain.TableInfo import *
from SqlMaker import *

class QueryXmlApp:
	def __init__(self, CONS):
		self.queryXmlInfoList=[]
		self.CONS=CONS
		self.aFieldApp = None

	def getKlassList(self, inRs, aFieldApp):
		self.aFieldApp = aFieldApp
		masterId = ''
		oldMasterId = ''
		oldda_Query_ID = ''
		oldTable_Eng=''
		for row  in inRs:
			try:
				process_Nm, processID, da_Query_ID, \
				table_Kor, table_Eng, table_Cd,  crud_Type \
					= row[0:7]
				masterId = da_Query_ID
			except (ValueError):
				print 'Count Error'
				sys.exit(2)

			if processID == '': break
			if oldMasterId != masterId:
				aQueryXmlInfo = QueryXmlInfo()
				aQueryXmlInfo.setAttributes(da_Query_ID)
				self.queryXmlInfoList.append(aQueryXmlInfo)
				oldTable_Eng=''
			oldMasterId = masterId
			if oldTable_Eng != table_Eng:
				aTableInfo = TableInfo()
				aTableInfo.setAttributes(table_Kor, table_Eng, table_Cd, crud_Type)

				#aFieldApp------------------------------------------------------
				aTableInfo.fieldList = self.aFieldApp.getFieldDictByTableId(aTableInfo.table_Cd)
				aTableInfo.pkColumnList = self.aFieldApp.getPkColumnsDictByTableId(aTableInfo.table_Cd)
				aTableInfo.nonPkColumnList = self.aFieldApp.getNonPkColumnDictByTableId(aTableInfo.table_Cd)
				
				aQueryXmlInfo.addTableList(aTableInfo)
			oldTable_Eng = table_Eng
			
			self.createMethod(aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID)

		return self.queryXmlInfoList

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

	def createMethodCore(self, aTableInfo, table_Kor, table_Eng, table_Cd, crud_Type, process_Nm, processID, crudGubun):
			aMethodInfo = MethodInfo()
			aMethodInfo.setAttributes(table_Kor, table_Eng, crudGubun, process_Nm, processID)
			aMethodInfo.setMethod(aTableInfo, aMethodInfo, crudGubun, table_Eng, table_Cd, processID)
			self.createSql(aTableInfo, aMethodInfo)
			aTableInfo.addMethodList(aMethodInfo)

	def createSql(self, aTableInfo, aMethod):
		aSqlMaker = SqlMaker()
		aSqlMaker.setTable(aTableInfo)
		crud = aMethod.crudGubun
		if crud == 'add':
			aSqlMaker.setInsertSqlAction(aMethod, aTableInfo)
		if crud == 'update':
			aSqlMaker.setUpdateSqlAction(aMethod, aTableInfo)
		if crud == 'delete':
			aSqlMaker.setDeleteSqlAction(aMethod, aTableInfo)
		if crud == 'find':
			aSqlMaker.setSelectSqlAction(aMethod, aTableInfo)


if __name__ == '__main__':
	pass
