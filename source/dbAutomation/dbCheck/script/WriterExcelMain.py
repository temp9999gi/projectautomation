# -*- coding: utf-8 -*-
from ExcelHelper import *

class WriterExcelMain(ExcelHelper):
	def __init__(self):
		pass
	def run(self, voList):
		inPath = sys.argv[0]
		CONS.setConstant(inPath)
		#inFile = CONS.INPUT_DATA_DIR / sys.argv[1]
		#ExcelHelper1.__init__
		self.setCons(CONS)
		
		i = self.CONS.ATTRIBUTE_LIST_START_POSITION
		self.setCurrentRow(i)

		self.setVoList(voList)
		#??????????????????????????????????????
		fileName = CONS.INPUT_CLASS_ATTRIBUTE
		
		self.title = ('no1', 'columnKor', 'columnEng', 'colType', 'tableEng', 'tableKR', 'bizName')
		
		self.writeExcel(fileName)

	def initExcelSheet(self, outputfile):
		self.openExcelSheet(outputfile)
		self.deleteSheet(['input']) #templ
		aTargetSheet = self.addSheet('templ', 'input')
		return aTargetSheet

	def writeExcel(self, outputfile):
		aTargetSheet = self.initExcelSheet(outputfile)
		
		# title
		self.writeAttributeRecord(aTargetSheet, 1, self.title)
		
		i = self.getCurrentRow()
		for attr in self.voList:
			self.writeAttributeRecord(aTargetSheet, i, attr)
			i = i + 1
			
		self.setCurrentRow(i)

	def writeAttributeRecord(self, sh, row, attr):
		for colx in range(1,len(attr)):
			sh.Cells(row, colx).Value = attr[colx]
