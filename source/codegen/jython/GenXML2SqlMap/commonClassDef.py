import string
from commonUtil import *

class Table :
	def __init__(self,tableEng):
		self.tableKor = ''
		self.lowNameIndex0 = ''
		self.columnList = []
		self.tableEng = tableEng
		self.setLowNameIndex0(tableEng)

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
		
	def setTableKor(self,tableKor):
		self.tableKor = tableKor

	def setCrudSql(self, crudSql):
		self.crudSql = crudSql
	def getCrudSql(self):
		return self.crudSql

	def setLowNameIndex0(self, attributeName):
		self.lowNameIndex0 = string.lower(attributeName[0]) + attributeName[1:]
		
	def addColumnList(self,aColumn):
		self.columnList.append(aColumn)
		aColumn.setTableEng(self.tableEng)
		#print '['+self.tableKor + ']' #, aColumn
	def setPkColumn(self):
		self.pkColumns = []
		tmp = []
		for c in self.columnList:
			if string.lower(c.pkYn) == 'y' :
				tmp.append(c.columnEng)
		self.pkColumns = tmp
		
	# WHERE  CD_ID = #cdId:VARCHAR#
	# AND    CD_TP_ID = #cdTpId:VARCHAR#		
	def getSqlWhere(self):
		s = ''
		pkColumns = self.pkColumns
		for i in range(len(pkColumns)):
			if i == 0 :
				s = s + pkColumns[i] +  ' = #' + pkColumns[i] + '# '
			if i > 0 :
				s = s + '\n\t\tAND ' + pkColumns[i] +  ' = #' + pkColumns[i] + '# '
		return s
		
class Column :
	def __init__(self,columnEng, propertyType):
		self.columnEng = columnEng
		self.propertyType = propertyType
		self.setUpperNameIndex0(columnEng)
	def setTableEng(self,tableEng):
		self.tableEng = tableEng
	def setPropertyType(self,propertyType):
		self.propertyType = propertyType
	def setUpperNameIndex0(self, attributeName):
		self.upperNameIndex0 = string.upper(attributeName[0]) + attributeName[1:]
	def setPkYn(self, pkYn):
		self.pkYn = pkYn

def setInsertSql1(aTable):
	#sql = "INSERT INTO ACCOUNT (" + "EMAIL, FIRSTNAME, LASTNAME" + ") VALUES (#email#, #firstName#, #lastName#)"
	columnArg = array2comma(aTable)
	rValueArg = getArray2ValueArg(aTable)
	sql = "INSERT INTO " + aTable.tableEng +" (" + columnArg + ") " + \
	      "\n\t\tVALUES (" + rValueArg + ")"
	aTable.setInsertSql(sql)

def setUpdateSql1(aTable):
	# UPDATE CD
	# SET      CD_ID = #cdId:VARCHAR# 
		 # , UPDATE_DATE = sysdate 
	# WHERE  CD_ID = #cdId:VARCHAR#
	# AND    CD_TP_ID = #cdTpId:VARCHAR#
	updateColumnArg = getUpdateSetArg(aTable)
	sqlWhere = aTable.getSqlWhere()
	sql = "UPDATE " + aTable.tableEng + " SET "  + updateColumnArg \
		+ "\n\t\tWHERE " + sqlWhere
	aTable.setUpdateSql(sql)
	
def setDeleteSql1(aTable):
	# DELETE FROM CD 
	# WHERE  CD_ID= #cdId:VARCHAR# 
	# AND    CD_TP_ID = #cdTpId:VARCHAR#
	sqlWhere = aTable.getSqlWhere()
	sql = "DELETE FROM " + aTable.tableEng  \
		+ " \n\t\tWHERE " + sqlWhere
	aTable.setDeleteSql(sql)
	
def setSelectSql1(aTable):	
	# SELECT CD_ID, CD_NM, CD_TP_ID, DEL_FG, to_char(UPDATE_DATE, 'YYYY/MM/DD HH24:MI:SS') UPDATE_DATE FROM CD 
	# WHERE CD_TP_ID=#cdTpId# and CD_ID = #cdId#
	columnArg = array2comma(aTable)
	sqlWhere = aTable.getSqlWhere()
	sql = "SELECT " + columnArg + \
	      " \n\t\tFROM " + aTable.tableEng  \
		+ " \n\t\tWHERE " + sqlWhere
	aTable.setSelectSql(sql)
	
