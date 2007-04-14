# -*- coding: utf-8 -*-
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')

#dsn = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%(dbq)s" % {'dbq': dbq}

data_source ='C://_projectautomation/source/dbAutomation/checkDbDictionary/db/MyDB.mdb'

DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=%(data_source)s;' \
	% {'data_source': data_source}
conn.Open(DSN)

rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs_name = 'columnInfo'

rs.Open('[' + rs_name + ']', conn, 1, 3)

flds_dict = {}
for x in range(rs.Fields.Count):
	flds_dict[x] = rs.Fields.Item(x).Name

print rs.Fields.Item(1).Type
#202 # 202 is a text field
print rs.Fields.Item(1).DefinedSize

#50  # 50 Characters

conn.Close()
