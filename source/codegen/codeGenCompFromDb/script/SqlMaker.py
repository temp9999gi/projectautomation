# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
SPACE2='  '
SPACE6='      '
COLUMN_PAD_LEN=25
from CommonUtil import *
aCommonUtil = CommonUtil()
# start
#-------------------------------------------------------------------------------
class SqlMaker:
	def __init__(self):
		pass #Klass.__init__(self)
	
	def setTable(self, aTable):
		self.aTable = aTable

	# dos의 경우: cr(\r) + lf(\n)
	# \r ASCII Carriage Return (CR)
	# \n ASCII Linefeed (LF)
	#-------------------------------------------------------------------------------
	def setSelectSqlAction(self, inMaster, aTable):
		# SELECT CD_ID, CD_NM, CD_TP_ID, DEL_FG, to_char(UPDATE_DATE, 'YYYY/MM/DD HH24:MI:SS') UPDATE_DATE FROM CD
		# WHERE CD_TP_ID=#cdTpId# and CD_ID = #cdId#
		columnArg = self.array2comma(aTable)
		sqlWhere = self.getSqlWhere()
		sqlId = inMaster.processID + '_' +  inMaster.methodId
		sql = "SELECT /*" + sqlId + "*/\n" + columnArg + \
			  "\nFROM " + aTable.tableEng  \
			+ "\nWHERE " + sqlWhere
		padedSql = aCommonUtil.getLpadAtLeftSpaceNum(sql, 6)
		inMaster.setSql(padedSql)

	#-------------------------------------------------------------------------------
	def setDeleteSqlAction(self, inMaster, aTable):
		# DELETE FROM CD
		# WHERE  CD_ID= #cdId:VARCHAR#
		# AND    CD_TP_ID = #cdTpId:VARCHAR#
		sqlId = inMaster.processID + '_' +  inMaster.methodId
		sqlWhere = self.getSqlWhere()
		sql = "DELETE /*" + sqlId + "*/ " + "FROM " + aTable.tableEng  \
			+ "\nWHERE " + sqlWhere
		padedSql = aCommonUtil.getLpadAtLeftSpaceNum(sql, 6)
		inMaster.setSql(padedSql)

	#-------------------------------------------------------------------------------
	def setUpdateSqlAction(self, inMaster, aTable):
		# UPDATE CD
		# SET      CD_ID = ?
			 # , UPDATE_DATE = sysdate
		# WHERE  CD_ID = ?
		# AND    CD_TP_ID = ?
		updateColumnArg = self.getUpdateSetArg(aTable)
		sqlWhere = self.getSqlWhere()
		sqlId = inMaster.processID + '_' +  inMaster.methodId
		sql = "UPDATE /*" + sqlId + "*/ " + aTable.tableEng + "\nSET\n"  + updateColumnArg \
			+ "" + "\nWHERE " + sqlWhere
		padedSql = aCommonUtil.getLpadAtLeftSpaceNum(sql, 6)
		inMaster.setSql(padedSql)
	#-------------------------------------------------------------------------------
	def setInsertSqlAction(self, inMaster, aTable):
		columnArg = self.array2comma(aTable)
		rValueArg = self.getArray2ValueArg(aTable)
		sqlId = inMaster.processID + '_' +  inMaster.methodId
		sql = "INSERT /*" + sqlId + "*/ " + "INTO " + aTable.tableEng +" (\n" + columnArg + ") " + \
			  "\n" + "VALUES (\n" + rValueArg + ")"
		#inMaster.setInsertSql(sql)
		padedSql = aCommonUtil.getLpadAtLeftSpaceNum(sql, 6)
		inMaster.setSql(padedSql)
	#-------------------------------------------------------------------------------


	
	def getSqlWhere(self):
		s = ''
		pkColumnList = self.aTable.pkColumnList
		first = True
		for pkCol in pkColumnList:
			ce = pkCol.columnEng
			if first :
				s = s + ce.ljust(COLUMN_PAD_LEN,' ') +  ' = ? '
				first=False
			else:
				s = s + '\n'+ SPACE2 +'AND ' + ce.ljust(COLUMN_PAD_LEN,' ') + \
				  ' = ? '
		return s

   	#-------------------------------------------------------------------------------
   	#-------------------------------------------------------------------------------
	def array2comma(self, aTable):
		s = SPACE2+' '
		#print 'TypeError: 언제 에러나냐?', aTable.tableEng
		"""
		음 source_input에는 테일블이 있는데 columnInfo에 없으면 에러남다.
		"""
		for c in aTable.fieldList:
			s = s + c.columnEng.ljust(COLUMN_PAD_LEN,' ') + '  /*'+c.columnKor +'*/' +'\n' + SPACE2 +','

		out = s[0:len(s)-4]
		return out


	def array2CommaForTbAlias(self, aTable):
		s = SPACE2+' '
		for c in aTable.fieldList:
			s = s + 'T1.'+c.columnEng.ljust(COLUMN_PAD_LEN,' ') + '  /*'+c.columnKorName +'*/' +'\n' + SPACE2 +','

		out = s[0:len(s)-4]
		return out
	def getUpdateSetArg(self, aTable):
		s = SPACE2+' '
		for c in aTable.nonPkColumnList:
			s = s + c.columnEng.ljust(COLUMN_PAD_LEN,' ') +  ' = ?' + '\n' + SPACE2 + ','
		out = s[0:len(s)-4]
		return out

	def getArray2ValueArg(self, aTable):
	    sValueArg = SPACE2+' '
	    for c in aTable.fieldList:
	        sValueArg = sValueArg + '?' + '  /*'+c.columnEng +'*/'+ '\n' + SPACE2 +','

	    out = sValueArg[0:len(sValueArg)-2]
	    # print 'array2comma', out
	    return out



