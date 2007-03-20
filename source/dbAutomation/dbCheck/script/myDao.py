# -*- coding: utf-8 -*-
import adodb
#builds object layers on top of databases.
class MyDao:
	def __init__(self):
		self.conn = adodb.NewADOConnection('access') # mxodbc required
		self.connect()
		self.tableVoList=[]
		self.columnVoList=[]

	def connect(self):
		dataSource ='C://_projectautomation/source/dbAutomation/dbCheck/db/MyDB.mdb'
		#C:\\_kldp\\codegen\\dbAutomation\\dbCheck\\input\\mdb\\MyDB.mdb
		#dsn = "Driver={Microsoft Access Driver (*.mdb)};Dbq=C:\\_kldp\\codegen\\dbAutomation\\dbCheck\\input\\mdb\\MyDB.mdb;"
		dsn = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%(dataSource)s;" \
			% {'dataSource': dataSource}

		self.conn.Connect(dsn)
		return self.conn
	
	def __del__(self):
		self.conn.Close()
		
	def setVo(self, tableList):
		for vo in tableList:
			self.tableVoList.append((vo.tableEng, vo.tableKor))
			for vo1 in vo.ColumnList:
				self.columnVoList.append((vo1.no1,vo1.columnKor,vo1.columnEng,vo1.type1, \
					vo1.length,vo1.null1,vo1.key,vo1.remark,vo1.tableEng))

	def deleteAll(self):
		# clean up existing data
		cursor = self.conn.cursor()
		cursor.execute('DELETE FROM tableInfo')
		cursor.execute('DELETE FROM columnInfo')
		cursor.close()
		self.conn.commit()

	def insertTable(self):
		statement = "INSERT INTO tableInfo (tableEng, tableKor) VALUES(?, ?)"
		insert1(self.conn, statement,self.tableVoList)
		

	def insertColumn(self):
		statement = "INSERT INTO columnInfo (no1,columnKor,columnEng,type1,length,null1,key,remark,tableEng) VALUES " + \
										   "(  ?,		?,		?,	?,	 ?,	?,  ?,	 ?,	  ?)"
		insert1(self.conn,statement,self.columnVoList)
		
	def executeQuery(self, sql):
		cursor = self.conn.Execute(sql)
		return cursor
   
    #101한글명같고 타입다른것
	def selectTypeErrorAndColumnKorIsEqual(self):
		sql="""SELECT DISTINCT columnInfo.no1, columnInfo.columnKor, columnInfo.columnEng, columnInfo.type1 AS Type, columnInfo.tableEng, columnInfo.tableKR, columnInfo.remark AS bizName
FROM columnInfo INNER JOIN columnInfo AS columnInfo2 ON columnInfo.columnKor=columnInfo2.columnKor
WHERE (((columnInfo.type1)<>columnInfo2.type1))
ORDER BY columnInfo.columnKor, columnInfo.type1, columnInfo.remark;
		"""
		return self.executeQuery(sql)

    #102한글명같고 길이다른것
	def selectLengthErrorAndColumnKorIsEqual(self):
		sql="""SELECT DISTINCT columnInfo.no1, columnInfo.columnKor, columnInfo.columnEng, columnInfo.length, columnInfo.tableEng, columnInfo.tableKR, columnInfo.remark AS bizName
FROM columnInfo INNER JOIN columnInfo AS columnInfo2 ON columnInfo.columnKor=columnInfo2.columnKor
WHERE (((columnInfo.length)<>columnInfo2.length))
ORDER BY columnInfo.columnKor, columnInfo.length, columnInfo.remark;
		"""
		return self.executeQuery(sql)
	
    #103한글명같고 영문명다른것
	def selectColumnEngErrorAndColumnKorIsEqual(self):
		sql="""SELECT DISTINCT columnInfo.no1, columnInfo.columnKor, columnInfo.columnEng, columnInfo.tableEng, columnInfo.tableKR, columnInfo.remark AS bizName
FROM columnInfo INNER JOIN columnInfo AS columnInfo2 ON columnInfo.columnKor=columnInfo2.columnKor
WHERE (((columnInfo.columnEng)<>columnInfo2.columnEng))
ORDER BY columnInfo.columnKor, columnInfo.columnEng, columnInfo.remark;
		"""
		return self.executeQuery(sql)

    #201영문명같고 타입다른것
	def selectTypeErrorAndColumnEngIsEqual(self):
		sql="""SELECT DISTINCT columnInfo.no1, columnInfo.columnKor, columnInfo.columnEng, columnInfo.type1, columnInfo.tableEng, columnInfo.tableKR, columnInfo.remark AS bizName
FROM columnInfo INNER JOIN columnInfo AS columnInfo2 ON columnInfo.columnEng=columnInfo2.columnEng
WHERE (((columnInfo.type1)<>columnInfo2.type1))
ORDER BY columnInfo.columnEng, columnInfo.type1, columnInfo.remark;
		"""
		return self.executeQuery(sql)

    #202영문명같고 길이다른것
	def selectLengthErrorAndColumnEngIsEqual(self):
		sql="""SELECT DISTINCT columnInfo.no1, columnInfo.columnKor, columnInfo.columnEng, columnInfo.length, columnInfo.tableEng, columnInfo.tableKR, columnInfo.remark AS bizName
FROM columnInfo INNER JOIN columnInfo AS columnInfo2 ON columnInfo.columnEng=columnInfo2.columnEng
WHERE (((columnInfo.length)<>columnInfo2.length))
ORDER BY columnInfo.columnEng, columnInfo.length, columnInfo.remark;
		"""
		return self.executeQuery(sql)

    #203영문명같고 한글명다른것
	def selectColumnKorErrorAndColumnEngIsEqual(self):
		sql="""SELECT DISTINCT columnInfo.no1 AS [No], columnInfo.columnKor, columnInfo.columnEng, columnInfo.tableEng, columnInfo.tableKR, columnInfo.remark AS bizName
FROM columnInfo INNER JOIN columnInfo AS columnInfo2 ON columnInfo.columnEng=columnInfo2.columnEng
WHERE (((columnInfo.columnKor)<>columnInfo2.columnKor))
ORDER BY columnInfo.columnEng, columnInfo.columnKor, columnInfo.remark;
		"""
		return self.executeQuery(sql)
	
	def selectAll(self):
		cursor = self.conn.cursor()
		cursor.execute('SELECT * from tableInfo')
		rs = cursor.fetchall()
		return rs


