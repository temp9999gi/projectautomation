# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
# ActiveX Data Objects (ADO)를 사용한다.

from dbLib.SuperDao import SuperDao

class CheckDbDictionaryDao(SuperDao):
	def __init__(self,dataSource):
		SuperDao.__init__(self,dataSource)

	#---------------------------------------------------------------------------
	def insertTblAndColAction(self, tableList):
		self.setRecordset()
		for tl in tableList:
			self.insertTable(tl)
			i=0;j=0
			for col in tl.ColumnList:
				i=i+1;col.no1=i;
				self.insertColumn(col, tl)

	def insertTblAndColAndElWordAction(self, tableList):
		self.setRecordset()
		self.insertTblAndColAndElWord(tableList)

	def insertTblAndColAndElWord(self,tableList):
		for tl in tableList:
			self.insertTable(tl)
			i=0;j=0
			for col in tl.ColumnList:
				i=i+1;col.no1=i;
				self.insertColumn(col, tl)
				for ew in col.elementWordList:
					j=j+1;seq=j;
					self.insertElementWord(ew,col,tl,seq)

	def insertTable(self, tl):
			sql = "INSERT INTO tableInfo (tableEng, tableKor) VALUES('%s', '%s')" % (tl.tableEng, tl.tableKor)
			self.executeQuery(sql)

	def insertColumn(self, col, tl):
		#for cl in col:
		sql = "INSERT INTO columnInfo " \
				"(no1 ,columnKor,columnEng,type1,length,null1,  key1,remark,tableKR, tableEng) VALUES " + \
				"('%s',     '%s',     '%s', '%s',  '%s', '%s', '%s',  '%s',   '%s',     '%s')" % \
				(col.no1,col.columnKor,col.columnEng,col.type1, col.length,col.null1,col.key,col.remark,tl.tableKor,tl.tableEng)
		#print sql
		self.executeQuery(sql)

	def insertElementWord(self,ew,col,tl,seq):
		sql = "INSERT INTO elementWord (elementWordEng, columnEng,  seq, tableKR, tableEng) VALUES " + \
								      "(          '%s',      '%s', '%s',    '%s',     '%s')" % \
  				(ew.elementWordEng, col.columnEng, seq, tl.tableKor, tl.tableEng)

		self.executeQuery(sql)


	#---------------------------------------------------------------------------
	def deleteTblAndColAction(self):
		self.setRecordset()
		# clean up existing data
		self.deleteTableInfo()
		self.deleteColumnInfo()

	def deleteAllAction(self):
		self.setRecordset()
		# clean up existing data
		self.deleteTableInfo()
		self.deleteColumnInfo()
		
		sql= 'DELETE FROM elementWord'
		cursor = self.executeQuery(sql)
		sql= 'DELETE FROM tbNameKorAndNull'
		cursor = self.executeQuery(sql)

		return cursor

	def deleteTableInfo(self):
		sql= 'DELETE FROM tableInfo'
		self.executeQuery(sql)
	def deleteColumnInfo(self):
		sql= 'DELETE FROM columnInfo'
		cursor = self.executeQuery(sql)

	def selectAllTbNameKorAndNull(self):
		sql = """
		SELECT tbNameKorAndNull.elementWordEng,
		  tbNameKorAndNull.nameKorAndNull,
		  tbNameKorAndNull.columnEng, tbNameKorAndNull.seq,
		  tbNameKorAndNull.tableEng
	    FROM tbNameKorAndNull;
				"""
		return sql
	#---------------------------------------------------------------------------



if __name__ == '__main__':
	pass
