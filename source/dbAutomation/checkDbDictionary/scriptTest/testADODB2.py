# -*- coding: utf-8 -*-
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')

data_source ='C://_projectautomation/source/dbAutomation/checkDbDictionary/db/MyDB.mdb'

DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=%(data_source)s;' \
	% {'data_source': data_source}
conn.Open(DSN)

rs = win32com.client.Dispatch(r'ADODB.Recordset')
#rs_name = 'columnInfo'

sql = """SELECT
	elementWord.elementWordEng,
	IIf(IsNull([dataDictionary.nameKor]),"|" & [elementWord.elementWordEng], [dataDictionary.nameKor])
	AS nameKorAndNull,
	elementWord.columnEng,
	elementWord.seq, columnInfo.tableEng
	FROM columnInfo INNER JOIN (elementWord LEFT JOIN dataDictionary ON elementWord.elementWordEng=dataDictionary.nameEng) ON (columnInfo.columnEng=elementWord.columnEng) AND (columnInfo.tableEng=elementWord.tableEng)
	ORDER BY columnInfo.tableEng, elementWord.columnEng, elementWord.seq;
		"""

rs.Cursorlocation = 3 # don't use parenthesis here
rs.Open(sql, conn) # be sure conn is open
rs.RecordCount # no parenthesis here either

fldList=[]
flds_dict = {}
rs.MoveFirst()
while 1:
	if rs.EOF:
		break
	else:
		for x in range(rs.Fields.Count):
			#f1 = rs.Fields.Item(x).Name
			flds_dict[x] = rs.Fields.Item(x).Value
		#print flds_dict.values()
		#(u'END', u'\uc885\ub8cc', u'END_DT', u'1', u'TB_BTR_DOMESTIC_PURPOSE')
		xx = flds_dict.values()
		fldList.append(tuple(xx))
		rs.MoveNext()

print fldList

conn.Close()
