# -*- coding: utf-8 -*-
from ExcelHelper import *
#-------------------------------------------------------------------------------

class ExcelHelperClassDefiniton(ExcelHelper):
	def __init__(self):
		ExcelHelper.__init__
		self.excelFileNo = 0

	def writeExcelCoreClassDef(self, aModelInfo, aExcelHelper):
		sheetCnt = 1

		#for aClassInfo in aModelInfo.classInfoList:
		outList = aModelInfo.getClassListOrInterfaceList()
		if not outList:
			log.debug("---def writeExcelCoreClassDef---")
			log.debug("data is none")
			if self.xl.ActiveWorkbook: #close되지 않은 경우
				self.closeFileForClassDef()
			sys.exit(0)

		for aClassInfo in outList:
			#엑셀에는 256개의 시트 개수 제한이 있다.
			#클래스 정의서는 250개씩 만들기로 한다.
			#그래서 sheetCnt=1일때 파일을 오픈한다.
			if sheetCnt==1:
				self.initExcelFileClassDef()

			remainder = sheetCnt % (self.CONS.EXCEL_MAX_SHEET_COUNT+1)

			#250으로 나누어서 나머지가 0 이면
			#새로운 엑셀파일에 write한다.
			#self.EXCEL_MAX_SHEET_COUNT = 5으로 설정해놓으면
			#5개시트씩 write한다.

			if sheetCnt<>1 and remainder==0:
				self.closeFileForClassDef()
				self.initExcelFileClassDef()

			aReaderAppEnvXml = ReaderAppEnvXml()
			aReaderAppEnvXml.saveWriterInfo(aClassInfo, self.CONS.INPUT_APP_ENV_XML)

			aTargetSheet = self.addSheet("templ", None)

			self.writeClassDefInfo(aTargetSheet, aClassInfo)
			self.writeAttribute(aTargetSheet, aClassInfo)

			self.copyMethodTitle(aTargetSheet, self.getCurrentRow())
			self.writeOperation(aTargetSheet, aClassInfo)

			sheetCnt = sheetCnt+1

		if self.xl.ActiveWorkbook: #close되지 않은 경우
			self.closeFileForClassDef()

	def setExcelFileNo(self):
		self.excelFileNo = self.excelFileNo+1
	def getExcelFileNo(self):
		return str(self.excelFileNo)

	def initExcelFileClassDef(self):
		self.setExcelFileNo()
		if self.aModelInfo.getDefinitionType()=='Interface':
			tmplFileName = self.CONS.INPUT_INTERFACE_XLS_TEMPLATE
			fileName = self.CONS.OUTPUT_INTERFACE_EXCEL
		if self.aModelInfo.getDefinitionType()=='Class':
			tmplFileName = self.CONS.INPUT_CLASS_EXCEL_TEMPLATE
			fileName = self.CONS.OUTPUT_CLASS_EXCEL

		outputfile = fileName + self.getExcelFileNo() + '.xls'
		ComUtil.copyTemplate(tmplFileName, outputfile)
		self.openExcelSheet(outputfile)
		
		


	def closeFileForClassDef(self):
		self.deleteSheet(['templ','method_templ']) #template 시트 삭제
		self.closeExcel()


	def writeClassDefInfo(self, sh, aClassInfo):
		self.writeHeadInfo(sh, aClassInfo)

		sh.Cells(6, 3).Value = aClassInfo.name				# 클래스명
		sh.Cells(7, 3).Value = self.aModelInfo.getDocumentation(aClassInfo.taggedValue)	# 설명


	def writeAttribute(self, sh, aClassInfo):

		attributes = self.aModelInfo.getAttributes(aClassInfo)
		i = self.CONS.ATTRIBUTE_LIST_START_POSITION

		for attr in attributes:
			# 번호	속성명		가시성	타입	기본값	설명
			visibility, name, typeName, initialValueBody = \
				self.aModelInfo.getAttributeInfo(attr)
   			documentation = self.aModelInfo.getDocumentation(attr.taggedValue)	# 설명

			self.writeAttributeRecord(sh, i, visibility, name, typeName, \
				initialValueBody, documentation)
			i = i + 1

		#속성정보가 없는 경우에 대한 처리
		if i == self.CONS.ATTRIBUTE_LIST_START_POSITION:
			visibility, name, typeName, initialValueBody, documentation = \
				"N/A", "N/A", "N/A", "N/A", "N/A"
			self.writeAttributeRecord(sh, i, visibility, name, typeName, \
				initialValueBody, documentation)
			i = i + 1

		self.setCurrentRow(i)

	def writeAttributeRecord(self, sh, row, visibility, name, typeName, \
			initialValueBody, documentation):

		sh.Cells(row, 1).Value = row - (self.CONS.ATTRIBUTE_LIST_START_POSITION-1)	# 번호
		sh.Cells(row, 2).Value = name			# 속성명
		sh.Cells(row, 3).Value = visibility	# 가시성
		sh.Cells(row, 4).Value = typeName		# 타입
		sh.Cells(row, 5).Value = initialValueBody			# 기본값 ????????????????????????????
		sh.Cells(row, 6).Value = documentation	# 설명

	def writeOperation(self, sh, aClassInfo):
		row = self.getCurrentRow()
		operations = self.aModelInfo.getOperations(aClassInfo)
		no = 1
		for x in operations:
			# 번호	오퍼레이션명		가시성	파라미터	반환타입	설명
			visibility, name, parameterString, returnTypeName = \
				self.aModelInfo.getBehavioralFeatureInfo(x)
			documentation = self.aModelInfo.getDocumentation(x.taggedValue)
			self.writeOperationRecord(sh,row,no,visibility, name, parameterString, \
				returnTypeName, documentation)
			row = row + 1
			no = no + 1

	def writeOperationRecord(self, sh, row, no, visibility, name, parameterString, \
	  returnTypeName, documentation):
		i=row
		sh.Cells(i, 1).Value = no						# 번호
		sh.Cells(i, 2).Value = name						# 명
		sh.Cells(i, 3).Value = visibility				# 가시성
		sh.Cells(i, 4).Value = parameterString			# 파라미터
		sh.Cells(i, 5).Value = returnTypeName			# 반환타입
		sh.Cells(i, 6).Value = documentation			# 설명
#-------------------------------------------------------------------------------
