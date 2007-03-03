# -*- coding: utf-8 -*-
from ExcelHelper import *

class WriterExcelMain(ExcelHelper):
	def __init__(self):
		inPath = sys.argv[0] #메인프로그램
		CONS.setConstant(inPath)
		self.setCons(CONS)
		outputfile = CONS.OUTPUT_XLS_FILE		
		self.openExcelSheet(outputfile)
		
	def writeSheetAtion(self, voList, columnTitle, inSheetName):
		i = self.CONS.ATTRIBUTE_LIST_START_POSITION
		self.setCurrentRow(i)
		self.setVoList(voList)
		#??????????????????????????????????????
		self.setColumnTitle(columnTitle)

		self.deleteSheet([inSheetName]) #templ
		aTargetSheet = self.addSheet('templ', inSheetName)
		
		self.writeExcel(aTargetSheet)
		#self.closeExcel()

	def setColumnTitle(self, columnTitle):
		self.columnTitle = columnTitle

	def writeExcel(self, aTargetSheet):
		
		# columnTitle
		self.writeAttributeRecord(aTargetSheet, 1, self.columnTitle)
		
		i = self.getCurrentRow()
		for attr in self.voList:
			self.writeAttributeRecord(aTargetSheet, i, attr)
			i = i + 1
			
		self.setCurrentRow(i)

	def writeAttributeRecord(self, sh, row, attr):
		for colx in range(1,len(attr)):
			sh.Cells(row, colx).Value = attr[colx]
