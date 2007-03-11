# -*- coding: utf-8 -*-

from CommonUtil import *
import Field
from sqlHelper import *
# start
SPACE2='  '
SPACE4='    '
INDENT_SPC='    '
COLUMN_PAD_LEN=25
aCommonUtil = CommonUtil()
class Klass:
	def __init__(self):
		self.fieldList = []
		self.ColumnList = self.fieldList
		self.operationList=[]
		self.pkColumnList=[]
		self.nonPkColumnList=[]		

	def setAttributes(self, entityName,tableViewName):
		self.klassEng = tableViewName
		self.tableEng = tableViewName
		self.klassKor = entityName
		self.tableKor = entityName
		
		#self.javaClassName = entityName
		self.name=self.klassEng

		self.javaClassName = aCommonUtil.getClassName(self.tableEng)
		
		self.writer			=" "
		self.writeDate		=" "
		self.subSystemName	=" "

	def addFieldList(self, aField):
		self.fieldList.append(aField)
		self.setpkColumnList(aField)
		
	def setpkColumnList(self, aField):
		if aField.columnIsPK == 'Yes':
			self.pkColumnList.append(aField)			
# 			print 'aField: [',aField.name,']'
		else:
			self.nonPkColumnList.append(aField)
# 			print 'aField: [',aField.name,']'			

	def getpkColumnList(self):
		return self.pkColumnList
		
	def addOperationList(self, aOperation):
		self.operationList.append(aOperation)

	def setClassDoc(self, aClassDoc):
		self.classDoc = aClassDoc
	def getClassDoc(self):
		try:
			out = self.classDoc
			return out
		except AttributeError:
			#ClassDoc 객체가 만들어지지 않았다면 ''을 리턴한다.
			aClassDoc=Field.ClassDoc()
			aClassDoc.setAttributes('','')
			return aClassDoc
	
	def setWriter(self, writer):
		self.writer = writer
	def setWriteDate(self, writeDate):
		self.writeDate = writeDate
	def setSubSystemName(self, subSystemName):
		self.subSystemName = subSystemName

	#---------------------------------------------------------------------------
	def getSqlWhere(self):
		s = ''
		pkColumnList = self.pkColumnList
		first = True
		for pkCol in self.pkColumnList:
			ce = pkCol.columnEng
			if first :
				s = s + ce.ljust(COLUMN_PAD_LEN,' ') +  ' = #' + pkCol.javaName + '# '
				first=False
			else:
				s = s + '\n'+ SPACE2 +'AND ' + ce.ljust(COLUMN_PAD_LEN,' ') + \
				  ' = #' + pkCol.javaName + '# '
		return s
	
	def getSqlWhereTbAlias(self):
		s = ''
		pkColumnList = self.pkColumnList
		first = True
		for pkCol in self.pkColumnList:
			ce = pkCol.columnEng
			if first :
				s = s + 'T1.'+ce.ljust(COLUMN_PAD_LEN,' ') +  ' = #' + pkCol.javaName + '# '
				first=False
			else:
				s = s + '\n'+ SPACE2 +'AND ' + 'T1.'+ce.ljust(COLUMN_PAD_LEN,' ') + \
				  ' = #' + pkCol.javaName + '# '
		return s
	
	def setInsertSql(self, insertSql):
		self.insertSql = insertSql
	def getInsertSql(self):
		return self.insertSql

	def setUpdateSql(self, updateSql):
		self.updateSql = updateSql
	def getUpdateSql(self):
		return self.updateSql

	def setDeleteSql(self, deleteSql):
		self.deleteSql = deleteSql
	def getDeleteSql(self):
		return self.deleteSql

	def setSelectSql(self, selectSql):
		self.selectSql = selectSql
	def getSelectSql(self):
		return self.selectSql

	def setSelectSqlTbAlias(self, selectSqlTbAlias):
		self.selectSqlTbAlias = selectSqlTbAlias
	def getSelectSqlTbAlias(self):
		return self.selectSqlTbAlias
	
	def setInsertSqlAction(self, aTable):

		columnArg = array2comma(aTable)
		rValueArg = getArray2ValueArg(aTable)
		sql = "INSERT INTO " + aTable.tableEng +" (\n" + columnArg + ") " + \
			  "\n" + "VALUES (\n" + rValueArg + ")"
		aTable.setInsertSql(sql)
		

	def setUpdateSqlAction(self, aTable):
		# UPDATE CD
		# SET      CD_ID = #cdId:VARCHAR# 
			 # , UPDATE_DATE = sysdate 
		# WHERE  CD_ID = #cdId:VARCHAR#
		# AND    CD_TP_ID = #cdTpId:VARCHAR#
		updateColumnArg = getUpdateSetArg(aTable)
		sqlWhere = self.getSqlWhere()
		sql = "UPDATE " + aTable.tableEng + "\nSET\n"  + updateColumnArg \
			+ "" + "\nWHERE " + sqlWhere
		aTable.setUpdateSql(sql)
		
	def setDeleteSqlAction(self, aTable):
		# DELETE FROM CD 
		# WHERE  CD_ID= #cdId:VARCHAR# 
		# AND    CD_TP_ID = #cdTpId:VARCHAR#
		sqlWhere = aTable.getSqlWhere()
		sql = "DELETE FROM " + aTable.tableEng  \
			+ "\nWHERE " + sqlWhere
		aTable.setDeleteSql(sql)
		
	def setSelectSqlAction(self, aTable):	
		# SELECT CD_ID, CD_NM, CD_TP_ID, DEL_FG, to_char(UPDATE_DATE, 'YYYY/MM/DD HH24:MI:SS') UPDATE_DATE FROM CD 
		# WHERE CD_TP_ID=#cdTpId# and CD_ID = #cdId#
		columnArg = array2comma(aTable)
		sqlWhere = self.getSqlWhere()
		sql = "SELECT\n" + columnArg + \
			  "\nFROM " + aTable.tableEng  \
			+ "\nWHERE " + sqlWhere
		aTable.setSelectSql(sql)

	def setSelectSqlTbAliasAction(self, aTable):
		# SELECT CD_ID, CD_NM, CD_TP_ID, DEL_FG, to_char(UPDATE_DATE, 'YYYY/MM/DD HH24:MI:SS') UPDATE_DATE FROM CD
		# WHERE CD_TP_ID=#cdTpId# and CD_ID = #cdId#
		columnArg = array2CommaForTbAlias(aTable)
		sqlWhere = self.getSqlWhereTbAlias()
		sql = "SELECT\n" + columnArg + \
			  "\nFROM "  + aTable.tableEng +' T1' \
			+ "\nWHERE " + sqlWhere
		aTable.setSelectSqlTbAlias(sql)
		


		
