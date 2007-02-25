# -*- coding: utf-8 -*-
from ExcelHelper import *

class ExcelHelperClassExport(ExcelHelper):
	def __init__(self):
		ExcelHelper.__init__
		self.excelFileNo = 0
		
	def setExcelFileNo(self):
		self.excelFileNo = self.excelFileNo+1
	def getExcelFileNo(self):
		return str(self.excelFileNo)		
	def setCurrentRowOfClassDocSh(self, currentRowOfClassDocSh):
		self.currentRowOfClassDocSh = currentRowOfClassDocSh
	def getCurrentRowOfClassDocSh(self):
		return self.currentRowOfClassDocSh
	
	def setCurrentRowOfOperationSh(self, currentRowOfOperationSh):
		self.currentRowOfOperationSh = currentRowOfOperationSh
	def getCurrentRowOfOperationSh(self):
		return self.currentRowOfOperationSh
	
	def setCurrentRowOfAttributeSh(self, currentRowOfAttributeSh):
		self.currentRowOfAttributeSh = currentRowOfAttributeSh
	def getCurrentRowOfAttributeSh(self):
		return self.currentRowOfAttributeSh
#-------------------------------------------------------------------------------	
	def writeExcelClassExport(self, aModelInfo, aExcelHelper):
		sheetCnt = 1

		#for aClassInfo in aModelInfo.classInfoList:
		outList = aModelInfo.getClassListOrInterfaceList()
		if not outList:
			log.debug("---def writeExcelCoreClassExport---")
			log.debug("data is none")
			self.closeFileForClassExport()
			sys.exit(0)

		self.initExcelFileClassExport()
		aTargetShAttribute = self.addSheet("attributeTmpl",'attribute')
		aTargetShOperation = self.addSheet("operationTmpl",'operation')
		aTargetShClassDocumentation = self.addSheet("classDocTmpl",'classDoc')
		
		#출력 레코드 위치를 설정
		self.setCurrentRowOfAttributeSh(2)
		self.setCurrentRowOfOperationSh(2)
		self.setCurrentRowOfClassDocSh(2)
		
		for aClassInfo in outList:
			aReaderAppEnvXml = ReaderAppEnvXml()
			aReaderAppEnvXml.saveWriterInfo(aClassInfo, self.CONS.INPUT_APP_ENV_XML)

			self.writeClassDocumentation(aTargetShClassDocumentation, aClassInfo)
			self.writeAttribute(aTargetShAttribute, aClassInfo)

			#self.copyMethodTitle(aTargetShAttribute, self.getCurrentRowOfAttributeSh())
			self.writeOperation(aTargetShOperation, aClassInfo)

		if self.xl.ActiveWorkbook: #close되지 않은 경우
			self.closeFileForClassExport()

	def initExcelFileClassExport(self):
		self.setExcelFileNo()
		if self.aModelInfo.getDefinitionType()=='Interface':
			fileName = self.CONS.OUTPUT_INTERFACE_EXCEL
		if self.aModelInfo.getDefinitionType()=='Class':
			fileName = self.CONS.OUTPUT_CLASS_EXCEL

		#outputfile = fileName + self.getExcelFileNo() + '.xls'
		outputfile=self.CONS.OUTPUT_CLASS_EXPORT_XLS
		
		ComUtil.copyTemplate(self.CONS.INPUT_CLASS_XLS_TMPL_FOR_EXPORT , outputfile)
		self.openExcelSheet(outputfile)


	def closeFileForClassExport(self):
		self.deleteSheet(['attributeTmpl','operationTmpl','classDocTmpl']) #template 시트 삭제
		self.closeExcel()


	def writeClassDocumentation(self, sh, aClassInfo):
		#self.writeHeadInfo(sh, aClassInfo)
		#row,col
		row=self.getCurrentRowOfClassDocSh()
		sh.Cells(row, 1).Value = aClassInfo.name				# 클래스명
		
		self.aModelInfo.initPackagePath()
		self.aModelInfo.setPackagePath(aClassInfo.namespace)
		sh.Cells(row, 2).Value = self.aModelInfo.getPackagePath()
		
		sh.Cells(row, 3).Value = self.aModelInfo.getDocumentation(aClassInfo.taggedValue)	# 설명
		
		row = row +1
		self.setCurrentRowOfClassDocSh(row)

	def writeAttribute(self, sh, aClassInfo):

		attributes = self.aModelInfo.getAttributes(aClassInfo)
		i=self.getCurrentRowOfAttributeSh()
		
		for attr in attributes:
			
			# 번호	속성명		가시성	타입	기본값	설명
			visibility, name, typeName, initialValueBody = \
				self.aModelInfo.getAttributeInfo(attr)
   			documentation = self.aModelInfo.getDocumentation(attr.taggedValue)	# 설명
   			className=attr.owner.name
			self.writeAttributeRecord(sh, i, className,visibility, name, typeName, \
				initialValueBody, documentation)
			i = i + 1

		#속성정보가 없는 경우에 대한 처리
		if i == self.CONS.ATTRIBUTE_LIST_START_POSITION:
			className, visibility, name, typeName, initialValueBody, documentation = \
				"N/A", "N/A", "N/A", "N/A", "N/A", "N/A"
			self.writeAttributeRecord(sh, i, className,visibility, name, typeName, \
				initialValueBody, documentation)
			i = i + 1

		self.setCurrentRowOfAttributeSh(i)

	def writeAttributeRecord(self, sh, row, className, visibility, name, typeName, \
			initialValueBody, documentation):
		#sh.Cells(row, 2).Value = row - (self.CONS.ATTRIBUTE_LIST_START_POSITION-1)	# 번호
		sh.Cells(row, 1).Value = className
		sh.Cells(row, 2).Value = name			# 속성명
		sh.Cells(row, 3).Value = visibility	# 가시성
		sh.Cells(row, 4).Value = typeName		# 타입
		sh.Cells(row, 5).Value = initialValueBody	# 기본값 ????????????????????????????
		sh.Cells(row, 6).Value = documentation	# 설명

	def writeOperation(self, sh, aClassInfo):
		row = self.getCurrentRowOfOperationSh()
		operations = self.aModelInfo.getOperations(aClassInfo)
		no = 1
		for x in operations:
			# 번호	오퍼레이션명		가시성	파라미터	반환타입	설명
			visibility, name, parameterString, returnTypeName = \
				self.aModelInfo.getBehavioralFeatureInfo(x)
			documentation = self.aModelInfo.getDocumentation(x.taggedValue)
			className=x.owner.name
			self.writeOperationRecord(sh,row,no,className,visibility, name, parameterString, \
				returnTypeName, documentation)
			row = row + 1
			no = no + 1
		self.setCurrentRowOfOperationSh(row)

	def writeOperationRecord(self, sh, row, no, className,visibility, name, parameterString, \
	  returnTypeName, documentation):
		i=row
		sh.Cells(i, 1).Value = className				# 클래스명
		sh.Cells(i, 2).Value = name						# 오퍼레이션명
		sh.Cells(i, 3).Value = visibility				# 가시성
		sh.Cells(i, 4).Value = parameterString			# 파라미터
		sh.Cells(i, 5).Value = returnTypeName			# 반환타입
		sh.Cells(i, 6).Value = documentation			# 설명
		
	#-------------------------------------------------------------------------------
