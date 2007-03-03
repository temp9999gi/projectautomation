# -*- coding: utf-8 -*-

import adodb
conn = adodb.NewADOConnection('access') # mxodbc required
#dsn = "Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\_kldp\\codegen\\dbAutomation\\dbCheck\\MyDB.mdb;"
dsn = "Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\_kldp\\codegen\\dbAutomation\\dbCheck\\MyDB.mdb;"
conn.Connect(dsn)


cursor = conn.Execute('select * from columnInfo')

while not cursor.EOF:
        print cursor.fields
        cursor.MoveNext()

cursor.Close()
conn.Close()

