# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
# ActiveX Data Objects (ADO)를 사용한다.
import win32com.client

data_source ='C://_projectautomation/source/analysisSupport/identifyComponent/db/MyDB.mdb'

class CrudMatrixDao:
	def __init__(self):
		self.connect()

	def selectAction(self, sql):
		
		self.setRecordset()
		rs = self.executeQuery(sql)
		return self.getTuple(rs)
		
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

	def __del__(self):
		pass #self.conn.Close()
		
	def insert1(self, conn,sql,inData):
		#sql = statement
		
		cursor = self.conn.Execute(sql, inData)
		return cursor
	"""
	conn = win32com.client.Dispatch(r'ADODB.Connection')
	DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=C:/MyDB.mdb;'
	sql_statement = "INSERT INTO [Table_Name]
	                 ([Field_1], [Field_2]) VALUES ('data1', 'data2')"
	conn.Open(DSN)
	conn.Execute(sql_statement)
	conn.Close()

	"""
	def insertAction(self, voList):
		self.setRecordset()
		self.setRecordsetForMuliRowInsert()
		self.insertCrudMatrix(voList)

	def insertCrudMatrix(self, voList):

		sql="""
		select usecaseName, crudGubun, className, crudGubunOriginal, accessValue
		from crudMatrix where 1<>1
		"""

		xx = self.executeQuery(sql)
		
		for x in range(0,4):
			#Add New Row
			self.rs.AddNew()

			# Add new Column Data
			self.rs["usecaseName"] 		= "my New Value 0"
			self.rs["crudGubun"] 		= "my New Value 1"
			self.rs["className"] 		= "my New Value 2"
			self.rs["crudGubunOriginal"]= "my New Value 3"
			self.rs["accessValue"] 		= "my New Value 4"
			
		self.rs.UpdateBatch()
		#self.rs.Close()
		
		statement = """INSERT INTO crudMatrix 
		  (usecaseName, crudGubun, className, crudGubunOriginal, accessValue) VALUES 
		  (          ?,         ?,         ?,                 ?,           ?)"""
		#self.insert1(self.conn, statement, voList)

	#---------------------------------------------------------------------------
		
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
					flds_dict[x] = rs.Fields.Item(x).Value
				#(u'END', u'\uc885\ub8cc', u'END_DT', u'1', u'TB_BTR_DOMESTIC_PURPOSE')
				xx = flds_dict.values()
				fldList.append(tuple(xx))
				rs.MoveNext()
		return fldList
	
if __name__ == '__main__':
	aCrudMatrixDao = CrudMatrixDao()

# 	voList=[]
# 	for tb  in tl:
# 		for cl  in tb.columnList:
# 			xx=(cl.checkColumn, cl.columnEng, tb.tableEng)
# 			voList.append(xx)

	voList=[]
	usecaseName='1'; crudGubun='1'; className='1'; crudGubunOriginal='1'; accessValue='1'
	xx=(usecaseName, crudGubun, className, crudGubunOriginal, accessValue)
	voList.append(xx)
	usecaseName='2'; crudGubun='1'; className='1'; crudGubunOriginal='1'; accessValue='1'	
	xx=(usecaseName, crudGubun, className, crudGubunOriginal, accessValue)
	voList.append(xx)
	
	
	rs=aCrudMatrixDao.insertAction(voList)

	print rs
