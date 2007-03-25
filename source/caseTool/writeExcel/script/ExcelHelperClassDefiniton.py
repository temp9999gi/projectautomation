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

			aTargetSheet = self.addSheet("templ", aClassInfo.name)
			#aTargetSheet = self.addSheet("templ", None)
			print 'aClassInfo.name:[', aClassInfo.name,']'

			self.writeClassMasterInfo(aTargetSheet, aClassInfo, sheetCnt)
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


	def writeClassMasterInfo(self, sh, aClassInfo,sheetCnt):
		self.writeHeadInfo(sh, aClassInfo)
		
		sh.Cells(1, 6).Value = sheetCnt #페이지번호
		sh.Cells(4, 3).Value = aClassInfo.name				# 클래스명
		sh.Cells(5, 3).Value = aClassInfo.getClassDoc().packagePath
		sh.Cells(6, 3).Value = aClassInfo.getClassDoc().documentation	# 설명
		#sh.Cells(7, 3).Value = self.aModelInfo.getDocumentation(aClassInfo.taggedValue)	# 설명


	def writeAttribute(self, sh, aClassInfo):

		#attributes = self.aModelInfo.getAttributes(aClassInfo)
		attributes = aClassInfo.fieldList
		i = self.CONS.ATTRIBUTE_LIST_START_POSITION

		for attr in attributes:
			self.writeAttributeRecord(sh, i, attr)
			i = i + 1

		#속성정보가 없는 경우에 대한 처리
		if i == self.CONS.ATTRIBUTE_LIST_START_POSITION:
			self.writeAttributeRecordBlank(sh, i)
			i = i + 1

		self.setCurrentRow(i)

	def writeAttributeRecord(self, sh, row, attr):

		sh.Cells(row, 1).Value = row - (self.CONS.ATTRIBUTE_LIST_START_POSITION-1)	# 번호
		sh.Cells(row, 2).Value = attr.name			# 속성명
##		sh.Cells(row, 3).Value = attr.visibility	# 가시성
##		sh.Cells(row, 4).Value = attr.typeName		# 타입
##		sh.Cells(row, 5).Value = attr.initialValueBody			# 기본값 ????????????????????????????
##		sh.Cells(row, 6).Value = attr.documentation	# 설명
	def writeAttributeRecordBlank(self, sh, row):
		sh.Cells(row, 1).Value = '1'	# 번호
		sh.Cells(row, 2).Value = 'N_A'	# 속성명
		sh.Cells(row, 3).Value = 'N_A'	# 가시성
		sh.Cells(row, 4).Value = 'N_A'	# 타입
		sh.Cells(row, 5).Value = 'N_A'	# 기본값 ????????????????????????????
		sh.Cells(row, 6).Value = 'N_A'	# 설명
		
	def writeOperation(self, sh, aClassInfo):
		row = self.getCurrentRow()
		
		operations = aClassInfo.operationList
		no = 1
		for aOper in operations:
			# 번호	오퍼레이션명		가시성	파라미터	반환타입	설명
##			visibility, name, parameterString, returnTypeName = \
##				self.aModelInfo.getBehavioralFeatureInfo(x)
			self.writeOperationRecord(sh,row,no,aOper)
			row = row + 1
			no = no + 1

	def writeOperationRecord(self, sh, row, no, aOper):
		i=row
		sh.Cells(i, 1).Value = no						# 번호
		sh.Cells(i, 2).Value = aOper.name						# 명
		sh.Cells(i, 3).Value = aOper.visibility				# 가시성
		sh.Cells(i, 4).Value = aOper.parameterString			# 파라미터
		sh.Cells(i, 5).Value = aOper.returnTypeName			# 반환타입
		sh.Cells(i, 6).Value = aOper.documentation			# 설명
#-------------------------------------------------------------------------------
