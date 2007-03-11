# -*- coding: utf-8 -*-
from MyDao2 import MyDao2
# 

class Table:
	def __init__(self):
		self.columnList=[]
	def setAttributes(self, tableViewName):
		self.klassEng = tableViewName
		self.tableEng = tableViewName
	def addColumnList(self, aColumn):
		self.columnList.append(aColumn)

class Column:
	def __init__(self):
		self.elementWordList=[]
		self.checkColumn=''
	def setAttributes(self, columnEng):
		self.columnEng      = columnEng
	def addElementWordList(self, aElementWord):
		self.elementWordList.append(aElementWord)
		self.setCheckColumn(aElementWord)
	def setCheckColumn(self, aElementWord):
		self.checkColumn = self.checkColumn + aElementWord.nameKorAndNull
		
class ElementWord:
	def __init__(self):
		pass
	def setAttributes(self, elementWordEng, nameKorAndNull, seq):
		self.elementWordEng = elementWordEng
		self.nameKorAndNull = nameKorAndNull
		self.seq		    = seq

class MainApp:
	def __init__(self):
		self.klassList=[]		
	def doAction(self, rsList):
		tableEng = '';oldtableEng = '';oldColumnEng=''
		for row  in rsList:
			try:
				elementWordEng, nameKorAndNull, columnEng, seq, tableEng = row[0:5]
			except (ValueError):
				print '열의 개수가 너무 많습니다.'
				sys.exit(2)
			if oldtableEng != tableEng:
				aTable = Table()
				aTable.setAttributes(tableEng)
				self.klassList.append(aTable)
				#self.setTableDictByName(tableEng,aTable)
			oldtableEng = tableEng

			if oldColumnEng != columnEng:
				aColumn = Column()
				aColumn.setAttributes(columnEng)
				aTable.addColumnList(aColumn)
			oldColumnEng = columnEng

			if len(elementWordEng) > 0:
				aElementWord = ElementWord()
				aElementWord.setAttributes(elementWordEng, nameKorAndNull, seq)
				aColumn.addElementWordList(aElementWord)
				
		return self.klassList
		#-------------------------------------------------------------------
def insertTbCheckColumnAction():
	aMyDao2 = MyDao2()
	#sql=aMyDao2.selectAllTbNameKorAndNull()
	sql=aMyDao2.selectNameKorAndNull()
	
	rsList = aMyDao2.selectAction(sql)
	if  rsList == None:
		print 'Data not found'
		import sys
		sys.exit(2)

	aMainApp = MainApp()
	tl = aMainApp.doAction(rsList)

	from myDao import MyDao
	aDao = MyDao()

	voList=[]
	for tb  in tl:
		for cl  in tb.columnList:
			xx=(cl.checkColumn, cl.columnEng, tb.tableEng)
			voList.append(xx)
	aDao.deleteAllTbCheckColumnAction()
	aDao.insertTbCheckColumnAction(voList)
	print "(MSG): Ok"
if __name__ == '__main__':
    insertTbCheckColumnAction()


