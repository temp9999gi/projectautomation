# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
# -*- coding: utf-8 -*-
# start
from pyExcel.ReadExcel import *
class ExcelReader:
	def __init__(self, inFile, inSheetName, inColCount):
		self.listForListFromSheet=[]
		self.readExcelInfo(inFile, inSheetName, inColCount)
		
	def getListFromSheet(self):
		return self.listForListFromSheet
	
	def getTupleFromSheet(self):
		return self.listForTupleFromSheet
	
	def readExcelInfo(self, inFile, inSheetName, inColCount):
		xl = ReadExcel(inFile)
		sheetnames = xl.worksheets()
		# print sheetnames
		outList = []
		outTuple = []
		for sheet in sheetnames:
			#-------------------------------------------------------------------
			if sheet == inSheetName:
				i=0
				for row  in xl.getIter(sheet, True):
					i=i+1
					if i<>1: #첫줄은 타이틀이다.
						
						#print row[0]
						outList.append(row[0:inColCount])
						outTuple.append(tuple(row[0:inColCount]))
						#print row
			#-------------------------------------------------------------------

		self.listForListFromSheet = outList
		self.listForTupleFromSheet = outTuple
		#return self.outList
	
if __name__ == '__main__':
	inFile='C:/_projectautomation/source/analysisSupport/identifyComponent/input/inputData/input.xls'
	inSheetNam='input'
	inColCount = 3
	aExcelReader= ExcelReader(inFile, inSheetNam, inColCount)
	print aExcelReader.getListFromSheet()
	#print aExcelReader.getTupleFromSheet()
