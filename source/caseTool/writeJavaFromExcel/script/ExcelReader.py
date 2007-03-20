# -*- coding: utf-8 -*-
# start
from CommonUtil import *
from ReaderExcelCore import *
from Klass import *
from Field import *
import sys

class ExcelReader:
	def __init__(self, inFile):
		self.klassListFromExcel = []
		self.readExcelInfo(inFile)
	def getKlassListFromExcel(self):
		return self.klassListFromExcel
	def readExcelInfo(self, inFile):
		xl = ReaderExcelCore(inFile)
		sheetnames = xl.worksheets()
		# print sheetnames
		for sheet in sheetnames:
			if sheet == 'input':
				klassName = ''
				oldKlassEng = ''
				for row  in xl.getIter(sheet, True):
					# Klass_Name, Field_Name, Field_Datatype, Field_Null_Option, Field_Is_PK, Field_Is_FK, Attribute_Name, Entity_Name, SEQ_NO
					try:
					    #번호	클래스명	가시성	타입	속성명
						seqNo, klassName, fieldVisibility, fieldType, fieldName = row[0:5]
					except (ValueError):
						print 'excel input file is invalid'
						print '엑셀 파일에 문제가 있습니다. 열의 개수가 너무 많습니다.'
						sys.exit(2)

					if seqNo == 'NO': continue
					if fieldName == '': break
					if oldKlassEng != klassName:
						aKlass = Klass()
						aKlass.setAttributes(klassName)
						self.klassListFromExcel.append(aKlass)

					oldKlassEng = klassName

					if len(fieldName) > 0:
						aField = Field()
						aField.setAttributes(fieldVisibility, fieldType, fieldName)
						aKlass.addFieldList(aField)
						
		return self.klassListFromExcel