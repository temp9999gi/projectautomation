# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import win32com.client

data_source ='C://_projectautomation/source/analysisSupport/identifyComponent/db/Component.mdb'

class SuperDao:
	def __init__(self):
		self.connect()
	def connect(self):
		dsn = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=%(data_source)s;' \
			% {'data_source': data_source}
		self.conn = win32com.client.Dispatch(r'ADODB.Connection')
		self.conn.Open(dsn)
		return self.conn

	def setRecordset(self):
		self.rs = win32com.client.Dispatch(r'ADODB.Recordset')

	def setRecordsetForMuliRowInsert(self):
		self.rs.CursorType=2 		# Dynamic Curor
		self.rs.CursorLocation = 3 	# Uses a client-side cursor supplied by a local cursor library
		self.rs.LockType = 4 		# Batch Optimistic

	def executeQuery(self, sql):
		self.rs.Cursorlocation = 3 # don't use parenthesis here
		self.rs.Open(sql, self.conn) # be sure conn is open
		return self.rs
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
				#(u'END', u'\uc885\ub8cc', u'END_DT', u'1', u'TB_BTR_DOMESTIC_PURPOSE')
				xx = flds_dict.values()
				fldList.append(tuple(xx))
				rs.MoveNext()
		return fldList
	def __del__(self):
		self.conn.Close()
