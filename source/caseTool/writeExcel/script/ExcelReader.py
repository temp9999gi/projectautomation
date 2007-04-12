# -*- coding: utf-8 -*-
# start
from CommonUtil import *
import sys;sys.path.append("C://_projectautomation/source/common")
from pyExcel.ReadExcel import *
from Klass import *
from Field import *

class ExcelReader:
	def __init__(self, inFile):
		self.klassListFromExcel = []
		self.klassDictByName = {}
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
			if sheet == 'attribute':
				klassEng = ''
				oldKlassEng = ''
				for row  in xl.getIter(sheet, True):
					#ClassName	속성	가시성	타입	기본값	속성

					# Klass_Name, Field_Name, Field_Datatype, Field_Null_Option, Field_Is_PK, Field_Is_FK, Attribute_Name, Entity_Name, SEQ_NO
					try:
						klassEng, fieldName, visibility, typeName, initialValueBody, \
							documentation= row[0:6]
						
					except (ValueError):
						print '엑셀 파일에 문제가 있습니다. 열의 개수가 너무 많습니다.'
						sys.exit(2)

					if klassEng == 'Class': continue
					if fieldName == '': break
					if oldKlassEng != klassEng:
						aKlass = Klass()
						aKlass.setAttributes(klassEng)
						self.klassListFromExcel.append(aKlass)
						self.setKlassDictByName(klassEng,aKlass)

					oldKlassEng = klassEng

					if len(fieldName) > 0:
						aField = Field()
						aField.setAttributes(fieldName, visibility, typeName, initialValueBody, \
							documentation)
						aKlass.addFieldList(aField)
			#-------------------------------------------------------------------
			if sheet == 'operation':
				klassEng = ''
				oldKlassEng = ''
				for row  in xl.getIter(sheet, True):
					#Class	오퍼레이션	가시성	파라미터	반환타입	오퍼레이션 설명	사전조건	사후조건

					try:

						klassEng, operationName, visibility, parameterString, returnTypeName, \
							documentation= row[0:6]
					except (ValueError):
						print '엑셀 파일에 문제가 있습니다. 열의 개수가 너무 많습니다.'
						sys.exit(2)

					if klassEng == 'Class': continue
					if operationName == '': break
					if oldKlassEng != klassEng:
						aKlass = self.getKlassDictByName(klassEng)
						if not aKlass:
							aKlass = Klass()
							aKlass.setAttributes(klassEng)
							self.klassListFromExcel.append(aKlass)
							self.setKlassDictByName(klassEng,aKlass)

					oldKlassEng = klassEng

					if len(operationName) > 0:
						aOperation = Operation()
						aOperation.setAttributes(operationName, visibility, \
							parameterString, returnTypeName, \
							documentation)
						aKlass.addOperationList(aOperation)
						
			#-------------------------------------------------------------------
			if sheet == 'classDoc':
				klassEng = ''
				oldKlassEng = ''
				for row  in xl.getIter(sheet, True):
					#Class	패키지	설명

					try:

						klassEng, packagePath, documentation= row[0:3]
					except (ValueError):
						print '엑셀 파일에 문제가 있습니다. 열의 개수가 너무 많습니다.'
						sys.exit(2)

					if klassEng == 'Class': continue
					if klassEng == '': break
					if oldKlassEng != klassEng:
						aKlass = self.getKlassDictByName(klassEng)
						if not aKlass:
							aKlass = Klass()
							aKlass.setAttributes(klassEng)
							self.klassListFromExcel.append(aKlass)
							self.setKlassDictByName(klassEng,aKlass)

					oldKlassEng = klassEng

					if len(klassEng) > 0:
						aClassDoc = ClassDoc()
						aClassDoc.setAttributes(packagePath, documentation)
						aKlass.setClassDoc(aClassDoc)

			#-------------------------------------------------------------------
		return self.klassListFromExcel
	
