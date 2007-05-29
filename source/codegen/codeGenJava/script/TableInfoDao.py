# -*- coding: utf-8 -*-
#import win32com.client
import sys;sys.path.append("C://_projectautomation/source/common")

from Klass import *
from Field import *

from dbLib.SuperDao import SuperDao
class TableInfoDao(SuperDao):
	def __init__(self,dataSource, CONS):
		SuperDao.__init__(self,dataSource)
		self.fldList=[]
		self.klassList=[]
		self.CONS=CONS
		
	def setFldList(self, fldList):
		self.fldList = fldList
	def getFldList(self):
		return self.fldList


	def getKlassListAction(self):
		self.selectAction()
		return self.getKlassList(self.fldList)


	#---------------------------------------------------------------------------
	#self.setMethod(klassName)

	#def setMethod(self, klassName):
		
	def setMethod(self, aKlass):
		self.setRecordset()
		sql=self.getSqlForMethod(aKlass.klassName)
		rs = self.executeQuery(sql)
		xx = self.getTuple(rs)
		self.setRelMethodAndClass(xx, aKlass)

	def getSqlForMethod(self, klassName):
		sql = """
			SELECT T1.methodReturnType, T1.methodName, T1.methodArgument
			FROM MethodInfo AS T1
			WHERE T1.klassName="%(in_klassName)s";
			"""% \
			{'in_klassName': klassName}
			
		return sql
	
	def setRelMethodAndClass(self, inRs, aKlass):
		for row  in inRs:
			try:
			    #
				col1, col2, col3 = row[0:3]
			except (ValueError):
				print 'ValueError'
				sys.exit(2)

			if len(col2) > 0:
				aMethod = Method()
				aMethod.setAttributes(col1, col2, col3)
				aKlass.addMethodList(aMethod)

		#return self.klassList
	
	#---------------------------------------------------------------------------
	def selectAction(self):
		self.setRecordset()
		sql=self.selectColumnInfo()
		rs = self.executeQuery(sql)
		return self.getTuple(rs)
	



	def selectColumnInfo(self):
		sql = """
			SELECT
			columnInfo.no1, columnInfo.javaClassEng, "private" as fieldVisibility,
			columnInfo.javaFieldType,
			columnInfo.javaFieldEng
			FROM columnInfo order by clng(columnInfo.no1);
			"""
		return sql

	def getTuple(self,rs):
		fldList=[]
		flds_dict = {}
		if rs.EOF: return None
		rs.MoveFirst()
		while 1:
			if rs.EOF:
				break
			else:
				for x in range(rs.Fields.Count):
					flds_dict[x] = rs.Fields.Item(x).Value
				xx = flds_dict.values()
				fldList.append(tuple(xx))
				rs.MoveNext()

		self.setFldList(fldList)
		return fldList
	
	def getKlassList(self, inRs):
		klassName = ''
		oldKlassEng = ''
		for row  in inRs:
			try:
			    #번호	클래스명	가시성	타입	속성명
				seqNo, klassName, fieldVisibility, fieldType, fieldName = row[0:5]
			except (ValueError):
				print 'excel input file is invalid'
				sys.exit(2)

			#if seqNo == 'NO': continue
			if fieldName == '': break
			if oldKlassEng != klassName:
				aKlass = Klass()
				aKlass.setAttributes(klassName)
				self.setMethod(aKlass)
				
				self.klassList.append(aKlass)

			oldKlassEng = klassName

			if len(fieldName) > 0:
				aField = Field(self.CONS)
				aField.setAttributes(fieldVisibility, fieldType, fieldName)
				aKlass.addFieldList(aField)

		return self.klassList
	
	
if __name__ == '__main__':
	dataSource='C://_projectautomation/source/dbAutomation/dbCheck/db/MyDB.mdb'
	#dataSource='C://_projectautomation/source/dbAutomation/checkDbDictionary2/db/MyDB.mdb'
	#dataSource = sys.argv[2]

	aTableInfoDao = TableInfoDao(dataSource)
	rs = aTableInfoDao.selectAction()
	aTableInfoDao.getKlassList(rs)
	print rs
