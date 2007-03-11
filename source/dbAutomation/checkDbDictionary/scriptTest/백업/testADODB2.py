# -*- coding: utf-8 -*-
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')

#dsn = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%(dbq)s" % {'dbq': dbq}

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


##rs.MoveFirst()
##count = 0
##while 1:
##	if rs.EOF:
##		break
##	else:
##		count = count + 1
##		x = rs('elementWordEng').Value
##		rs.MoveNext()


flds_dict = {}
rs.MoveFirst()
while 1:
	if rs.EOF:
		break
	else:
##		f1 = rs.Fields["elementWordEng"].Value
##		f2 = rs.Fields["nameKorAndNull"].Value
		for x in range(rs.Fields.Count):
			f1 = rs.Fields.Item(x).Name
			flds_dict[x] = rs.Fields.Item(x).Value
		print flds_dict
		rs.MoveNext

for x in rs.Fields:
	xx = x.Name
	y = x.Value
	rs.MoveNext()
	print x

flds_dict = {}
for x in range(rs.Fields.Count):
	flds_dict[x] = rs.Fields.Item(x).Name
	y = rs.Fields.Item(x).Value
	print x

print rs.Fields.Item(1).Type
#202 # 202 is a text field
print rs.Fields.Item(1).DefinedSize

#50  # 50 Characters

conn.Close()
