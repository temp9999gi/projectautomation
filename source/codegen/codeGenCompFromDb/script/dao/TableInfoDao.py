# -*- coding: utf-8 -*-
import sys;sys.path.append("C://_projectautomation/source/common")

##from domain.BizComp import *
##from domain.Process import *
from domain.ActivityClassInfo import *
from domain.TableInfo import *


from dbLib.SuperDao import SuperDao
class TableInfoDao(SuperDao):
	def __init__(self, dataSource, CONS):
		SuperDao.__init__(self, dataSource)
		self.fldList=[]
		#self.bizCompList=[]
		self.CONS=CONS
		
	def setFldList(self, fldList):
		self.fldList = fldList
	def getFldList(self):
		return self.fldList

	#---------------------------------------------------------------------------
	#---------------------------------------------------------------------------
	# app Comp
	def getKlassListForServiceXmlInfoAction(self):
		return self.selectForServiceXmlInfoService()
	def selectForServiceXmlInfoService(self):
		sql=self.getSqlForServiceXmlInfo()
		return self.getTupleAction(sql)
	def getSqlForServiceXmlInfo(self):
		sql = """
			SELECT
				T1.processID, T1.process_Nm, T1.service_Xml_Nm, T1.service_Xml_Id,
				'XXXX' as biz_Comp_Nm, 'XXXX' as biz_Comp_Id, T1.table_Eng, T1.table_Cd, T1.table_Kor,
				T1.crud_Type
			FROM source_input AS T1
			ORDER BY T1.service_Xml_Id, T1.table_Eng, T1.processID;
			"""
		return sql

	#---------------------------------------------------------------------------
	#---------------------------------------------------------------------------
	# Biz Comp
	def getKlassListAction(self):
		return self.selectAction()

	def selectAction(self):
		sql=self.getSqlColumnInfo()
		return self.getTupleAction(sql)

	def getSqlColumnInfo(self):
		sql = """
			SELECT
				T1.process_Nm, T1.processID, T1.biz_Comp_Nm,
				T1.biz_Comp_Id, T1.da_Query_ID, T1.table_Kor,
				T1.table_Eng, T1.table_Cd,  T1.crud_Type
			FROM source_input AS T1
			ORDER BY T1.Biz_Comp_Id, T1.da_Query_ID, T1.table_Eng,T1.processID;
			"""
		return sql
	#---------------------------------------------------------------------------
	#---------------------------------------------------------------------------
	# dAO Comp
	def getKlassListForActivityClassAction(self):
		return self.selectForActivityClassService()
	def selectForActivityClassService(self):
		sql=self.getSqlForActivityClass()
		return self.getTupleAction(sql)
	def getSqlForActivityClass(self):
		sql = """
			SELECT
			T1.process_Nm, T1.processID, T1.da_Query_ID, T1.table_Kor,
			T1.table_Eng, T1.table_Cd, T1.crud_Type
			FROM source_input AS T1
			ORDER BY T1.da_Query_ID, T1.table_Eng, T1.processID;
			"""
		return sql

	#---------------------------------------------------------------------------
	#---------------------------------------------------------------------------

	def getKlassListForCreateFieldAction(self):
		return self.selectForCreateFieldService()
	def selectForCreateFieldService(self):
		sql=self.getSqlForCreateField()
		return self.getTupleAction(sql)
	def getSqlForCreateField(self):
		sql = """
			SELECT
			T1.tableKor, T1.tableEng, T1.columnEng, T1.columnDataTypeAndLength,
			T1.columnNullOption, T1.columnIsPK, T1.columnIsFk, T1.columnKor
			FROM columnInfo AS T1
			ORDER BY T1.tableEng, T1.seq;
			"""
		return sql


	#---------------------------------------------------------------------------
	#---------------------------------------------------------------------------
	def insertMethodInfoService(self, aMethodInfo):
		self.insertMethodInfo(aMethodInfo)

	def insertMethodInfo(self, aMethod):
		sql = """
			INSERT INTO MethodInfo
			(processID, methodEng,
			 methodKor, classId,
			 table_Cd, crud_Type)
			VALUES
			('%s', '%s',
			 '%s', '%s',
			 '%s', '%s')
			""" \
			% (aMethod.processID, aMethod.methodEng,
			   aMethod.methodKor, aMethod.classId,
			   aMethod.aTable.table_Cd, aMethod.crud_Type)
			   
		self.executeCudQuery(sql)
		

if __name__ == '__main__':
	dataSource='C://_projectautomation/source/dbAutomation/dbCheck/db/MyDB.mdb'
	#dataSource='C://_projectautomation/source/dbAutomation/checkDbDictionary2/db/MyDB.mdb'
	#dataSource = sys.argv[2]

	aTableInfoDao = TableInfoDao(dataSource)
	rs = aTableInfoDao.selectAction()
	aTableInfoDao.getKlassList(rs)
	print rs
