# -*- coding: utf-8 -*-
import win32com.client

class MyDao2:
	def __init__(self):
		self.data_source ='C://_projectautomation/source/dbAutomation/checkDbDictionary/db/MyDB.mdb'
		self.connect()

	def selectAction(self, sql):
		
		self.setRecordset()
		rs = self.executeQuery(sql)
		return self.getTuple(rs)
		
	def connect(self):
		
		dsn = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=%(data_source)s;' \
			% {'data_source': self.data_source}
		self.conn = win32com.client.Dispatch(r'ADODB.Connection')
		self.conn.Open(dsn)
		return self.conn

	def setRecordset(self):
		self.rs = win32com.client.Dispatch(r'ADODB.Recordset')
	
	def executeQuery(self, sql):
		self.rs.Cursorlocation = 3 # don't use parenthesis here
		self.rs.Open(sql, self.conn) # be sure conn is open
		return self.rs
	
	def __del__(self):
		self.conn.Close()
		
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
					#f1 = rs.Fields.Item(x).Name
					flds_dict[x] = rs.Fields.Item(x).Value
				#(u'END', u'\uc885\ub8cc', u'END_DT', u'1', u'TB_BTR_DOMESTIC_PURPOSE')
				xx = flds_dict.values()
				fldList.append(tuple(xx))
				rs.MoveNext()
		return fldList
	
if __name__ == '__main__':
	aMyDao2 = MyDao2()
	sql=aMyDao2.selectNameKorAndNull()
	rs = aMyDao2.selectAction(sql)
	print rs
