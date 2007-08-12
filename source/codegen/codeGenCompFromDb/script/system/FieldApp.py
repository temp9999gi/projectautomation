# -*- coding: utf-8 -*-
from domain.QueryXmlInfo import *
from domain.Field import *

class FieldApp:
	def __init__(self, CONS):
		self.CONS=CONS
		self.tableList=[]
		self.fieldDictByTableId = {}
		self.pkColumnsDictByTableId={}
		self.nonPkColumnDictByTableId={}


	def setNonPkColumnDictByTableId(self, key, item):
		self.nonPkColumnDictByTableId[key] = item
	def getNonPkColumnDictByTableId(self, key):
		try:
			out = self.nonPkColumnDictByTableId[key]
			return out
		except KeyError:
			return None

	def setPkColumnsDictByTableId(self, key, item):
		self.pkColumnsDictByTableId[key] = item
	def getPkColumnsDictByTableId(self, key):
		try:
			out = self.pkColumnsDictByTableId[key]
			return out
		except KeyError:
			return None
		
	def setFieldDictByTableId(self, key, item):
		self.fieldDictByTableId[key] = item
	def getFieldDictByTableId(self, key):
		try:
			out = self.fieldDictByTableId[key]
			return out
		except KeyError:
			return None

	def getKlassList(self, inRs):
		masterId = ''
		oldMasterId = ''
		oldda_Query_ID = ''
		oldTable_Eng=''
		fieldList=[]
		pkColumnList=[];nonPkColumnList=[]
		for row  in inRs:
			try:
				tableKor, tableCd, columnEng, columnDataTypeAndLength, \
				columnNullOption, columnIsPK, columnIsFk, columnKor = row[0:8]
				masterId = tableCd
				child_Id = columnEng
			except (ValueError):
				print 'Count Error'
				sys.exit(2)

			if masterId == '': break
			if oldMasterId != masterId:
				self.tableList.append(tableCd)
				fieldList=[];pkColumnList=[];nonPkColumnList=[]
				oldChild_Id=''
			oldMasterId = masterId
			if oldChild_Id != child_Id:
				aField = Field(self.CONS)
				aField.setAttributes(columnEng, columnDataTypeAndLength, \
					columnNullOption, columnIsPK, columnIsFk, columnKor, tableKor, tableCd)

				fieldList.append(aField)
				if aField.columnIsPK == 'Yes': pkColumnList.append(aField)
				else: nonPkColumnList.append(aField)

				self.setFieldDictByTableId(tableCd, fieldList)
				self.setPkColumnsDictByTableId(tableCd, pkColumnList)
				self.setNonPkColumnDictByTableId(tableCd, nonPkColumnList)
			oldChild_Id = child_Id

		return self.tableList


if __name__ == '__main__':
	pass