# -*- coding: utf-8 -*-
import adodb
#builds object layers on top of databases.

class MyDao:
	def __init__(self):
		self.conn = adodb.NewADOConnection('access') # mxodbc required
		self.connect()
		self.tableVoList=[]
		self.columnVoList=[]
		self.elementWordVoList=[]

	def connect(self):
		dbq = "C:\\_projectautomation\\source\\dbAutomation\\checkDbDictionary\\db\\MyDB.mdb;"
		dsn = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%(dbq)s" % {'dbq': dbq}
		self.conn.Connect(dsn)
		return self.conn
	
	def __del__(self):
		self.conn.Close()
		
	def setVo(self, tableList):
		for tl in tableList:
			self.tableVoList.append((tl.tableEng, tl.tableKor))
			i=0
			for col in tl.ColumnList:
				i=i+1;col.no1=i;
				self.columnVoList.append((col.no1,col.columnKor,col.columnEng,col.type1, \
					col.length,col.null1,col.key,col.remark,tl.tableKor,tl.tableEng))
				j=0
				for ew in col.elementWordList:
					j=j+1;seq=j;
					self.elementWordVoList.append( \
						(ew.elementWordEng, col.columnEng, seq, tl.tableKor, tl.tableEng))
					

	def deleteAllAction(self):
		# clean up existing data
		sql= 'DELETE FROM tableInfo'
		self.executeQuery(sql)
		sql= 'DELETE FROM columnInfo'
		cursor = self.executeQuery(sql)
		sql= 'DELETE FROM elementWord'
		cursor = self.executeQuery(sql)
		sql= 'DELETE FROM tbNameKorAndNull'
		cursor = self.executeQuery(sql)

		return cursor
	
	def deleteAllTbCheckColumnAction(self):
		sql= 'DELETE FROM tbCheckColumn'
		cursor = self.executeQuery(sql)

	def insertAction(self):
		self.insertTableAction()
		self.insertColumnAction()
		self.insertElementWordAction()

	def insertTableAction(self):
		statement = "INSERT INTO tableInfo (tableEng, tableKor) VALUES(?, ?)"
		self.insert1(self.conn, statement,self.tableVoList)
		

	def insertColumnAction(self):
		statement = "INSERT INTO columnInfo " \
				"(no1,columnKor,columnEng,type1,length,null1,key,remark,tableKR, tableEng) VALUES " + \
				"(  ?,        ?,        ?,    ?,     ?,    ?,  ?,     ?,      ?,        ?)"
		self.insert1(self.conn,statement,self.columnVoList)

	def insertElementWordAction(self):
		statement = "INSERT INTO elementWord (elementWordEng, columnEng, seq, tableKR, tableEng) VALUES " + \
											"(             ?,         ?,   ?,       ?,        ?)"
		self.insert1(self.conn, statement,self.elementWordVoList)

	def insertTbNameKorAndNullAction(self, voList):
		statement = """INSERT INTO tbNameKorAndNull (elementWordEng, nameKorAndNull, columnEng, seq, tableEng) VALUES
													(             ?,              ?,         ?,   ?,        ?)"""
		self.insert1(self.conn, statement,voList)

	def insertTbCheckColumnAction(self, voList):
		statement = """INSERT INTO tbCheckColumn (checkColumn, columnEng, tableEng) VALUES
		                                         (          ?,         ?,        ?)"""
		self.insert1(self.conn, statement,voList)


	def insert1(self, conn,statement,inData):
		sql = statement
		cursor = self.conn.Execute(sql, inData)
		return cursor

##	    cursor = conn.cursor()
##	    cursor.execute(statement, inData)  #all in one
##	    cursor.close()
##	    conn.commit()
	def executeQuery(self, sql):
		cursor = self.conn.Execute(sql)
		return cursor
	
	#010_3용어사전한글명_Null컬럼_낱단어한글명조회
	def selectNameKorAndNull(self):
		sql="""SELECT elementWord.elementWordEng, IIf(IsNull([dataDictionary.nameKor]),"|" & [elementWord.elementWordEng],[dataDictionary.nameKor]) AS nameKorAndNull, elementWord.columnEng, elementWord.seq, columnInfo.tableEng
FROM columnInfo INNER JOIN (elementWord LEFT JOIN dataDictionary ON elementWord.elementWordEng=dataDictionary.nameEng) ON (columnInfo.columnEng=elementWord.columnEng) AND (columnInfo.tableEng=elementWord.tableEng)
ORDER BY columnInfo.tableEng, elementWord.columnEng, elementWord.seq;
		"""
		return self.executeQuery(sql)
   
   
   
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


