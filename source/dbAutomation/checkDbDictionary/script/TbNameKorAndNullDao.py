# -*- coding: utf-8 -*-
import win32com.client
from dbLib.SuperDao import SuperDao
class TbNameKorAndNullDao(SuperDao):
	def __init__(self,dataSource):
		SuperDao.__init__(self,dataSource)

	def selectNameKorAndNullAction(self):

		self.setRecordset()
		sql=self.selectNameKorAndNull()
		rs = self.executeQuery(sql)
		return self.getTuple(rs)
	def selectNameKorAndNull(self):
		sql = """
		  SELECT
			elementWord.elementWordEng,
			IIf(IsNull([dataDictionary.nameKor]),"|" & [elementWord.elementWordEng], [dataDictionary.nameKor])
			AS nameKorAndNull,
			elementWord.columnEng,
			elementWord.seq, columnInfo.tableEng
		  FROM columnInfo INNER JOIN (elementWord LEFT JOIN dataDictionary ON elementWord.elementWordEng=dataDictionary.nameEng) ON (columnInfo.columnEng=elementWord.columnEng) AND (columnInfo.tableEng=elementWord.tableEng)
		  ORDER BY columnInfo.tableEng, elementWord.columnEng, elementWord.seq;
				"""
		return sql

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
	def insertTbNameKorAndNullAction(self, voList):
		self.setRecordset()
		for vl in voList:
			sql = """INSERT INTO tbNameKorAndNull
				(elementWordEng, nameKorAndNull, columnEng,  seq, tableEng) VALUES
				(          '%s',           '%s',      '%s', '%s',     '%s')"""\
				% vl
			self.executeQuery(sql)

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
		return fldList
	
if __name__ == '__main__':
	aTbNameKorAndNullDao = TbNameKorAndNullDao()
	sql=aTbNameKorAndNullDao.selectNameKorAndNull()
	rs = aTbNameKorAndNullDao.selectAction(sql)
	print rs
