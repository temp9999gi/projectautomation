# -*- coding: utf-8 -*-
# start
from CommonUtil import *
from pyExcel.ReadExcel import *
from Klass import *
from Field import *
from DbAndJavaTypeMapper import *

class ExcelReader:
	def __init__(self, inFile, CONS):
		self.klassListFromExcel = []
		self.klassDictByName = {}
		#self.CONS = CONS
		self.typeMapper = DbAndJavaTypeMapper(CONS)
		self.readExcelInfo(inFile)

		
	def setKlassDictByName(self, key, item):
		self.klassDictByName[key] = item
	def getKlassDictByName(self, key):
		try:
			out = self.klassDictByName[key]
			return out
		except KeyError:
			return None
	
	def getKlassListFromExcel(self):
		return self.klassListFromExcel
	def readExcelInfo(self, inFile):
		xl = ReadExcel(inFile)
		sheetnames = xl.worksheets()
		# print sheetnames
		for sheet in sheetnames:
			#-------------------------------------------------------------------
			if sheet == 'TABLE_Source':
				entityName = ''
				oldentityName = ''
				for row  in xl.getIter(sheet, True):
					#ClassName	속성	가시성	타입	기본값	속성

					try:
						tableViewName, columnName, columnDatatype, columnNullOption, \
							columnIsPK, columnIsFK, attributeName, entityName = row[0:8]
					except (ValueError):
						print '엑셀 파일에 문제가 있습니다. 열의 개수가 너무 많습니다.'
						sys.exit(2)

					if entityName == 'EntityName': continue
					if attributeName == '': break
					if oldentityName != entityName:
						aKlass = Klass()
						aKlass.setAttributes(entityName)
						self.klassListFromExcel.append(aKlass)
						self.setKlassDictByName(entityName,aKlass)

					oldentityName = entityName

					if len(attributeName) > 0:
						aField = Field(self.typeMapper)
						#ClassName	가시성	타입	속성명

						aField.setAttributes(attributeName, columnDatatype)
						aKlass.addFieldList(aField)
			#-------------------------------------------------------------------
		return self.klassListFromExcel
	