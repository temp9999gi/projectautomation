# -*- coding: utf-8 -*-
from WordSuperType import *

class WordlHelper(WordSuperType):
	def __init__(self):
		WordSuperType.__init__(self)
		self.aModelInfo = None
		self.wordFileNo= 0

	def setModelInfo(self, aModelInfo, CONS):
		self.aModelInfo = aModelInfo
		self.CONS = CONS
	def getModelInfo(self):
		return self.aModelInfo
	
	def writeAction(self):
		classCnt = 1

		outList = self.aModelInfo.getClassListOrInterfaceList()
		if not outList:
			log.debug("---def writeWordCoreClassDef---")
			log.debug("data is none")
			sys.exit(0)

		#print self.CONS.OUT_DIR_TEMP
		ComUtil.rmTreeDir(self.CONS.OUT_DIR_TEMP)
		ComUtil.mkDir(self.CONS.OUT_DIR_TEMP)
		for aClassInfo in outList:
			self.openWordService()
			
##			activeDoc = self.getActiveDoc()
##			tb = activeDoc.Tables(1)
			self.writeHeadInfo()
			#self.writeClassMasterInfo(tb, aClassInfo)

			self.closeActiveDocument(self.filename)

			classCnt = classCnt+1
		self.closeWord()

	def openWordService(self):
		self.addWordFileNo()
		if self.aModelInfo.getDefinitionType()=='Interface':
			tmplFileName = self.CONS.INPUT_INTERFACE_WRD_TEMPLATE
			fileName = self.CONS.OUTPUT_INTERFACE_WRD
		if self.aModelInfo.getDefinitionType()=='Class':
			tmplFileName = self.CONS.INPUT_CLASS_WRD_TEMPLATE
			fileName = self.CONS.OUTPUT_CLASS_WRD

		outputfile = fileName + self.getWordFileNo() + self.CONS.OUTPUT_DOC_TYPE #'.hwp'
		ComUtil.copyTemplate(tmplFileName, outputfile)
		self.openWord(outputfile)
		

	def setCurrentRow(self, curRow):
		self.currentRow = curRow

	def getCurrentRow(self):
		return self.currentRow

	def addWordFileNo(self):
		self.wordFileNo = self.wordFileNo+1
	def getWordFileNo(self):
		return str(self.wordFileNo)
		
	#---------------------------------------------------------------------------
	def writeHeadInfo(self):
		aReaderAppEnv=self.aModelInfo.getReaderAppEnv()
		# row, col
		subSystemName = aReaderAppEnv.appEnvData["subSystemName"] # 서브시스템
		writer = aReaderAppEnv.appEnvData["writer"]	# 작성자
		writeDate = aReaderAppEnv.appEnvData["writeDate"]# 작성일
		
		self.app.PutFieldText("bizName",	subSystemName)
		self.app.PutFieldText("writer",		writer)
		self.app.PutFieldText("writeDate",	writeDate)

	def writeClassMasterInfo(self, tb, aClassInfo):
		#self.writeHeadInfo(tb, aClassInfo)

		tb.Cell(3, 2).Range.Text = aClassInfo.getClassDoc().packagePath
		tb.Cell(4, 2).Range.Text = aClassInfo.name				# 클래스명
		tb.Cell(5, 2).Range.Text = aClassInfo.getClassDoc().documentation	# 설명

	#---------------------------------------------------------------------------
	def writeAttribute(self, tb, aClassInfo):

		i = 2 #self.CONS.ATTRIBUTE_LIST_START_POSITION
		for attr in aClassInfo.fieldList:
			self.writeAttributeRecord(tb, i, attr)
			i = i + 1

		self.setCurrentRow(i)
		
	def writeAttributeRecord(self, tb, row, attr):

		#tb.Cell(row, 1).Range.Text = row - (self.CONS.ATTRIBUTE_LIST_START_POSITION-1)	# 번호

		tb.Cell(row, 1).Range.Text = attr.name				# 속성명
		tb.Cell(row, 2).Range.Text = attr.visibility		# 가시성
		tb.Cell(row, 3).Range.Text = attr.typeName			# 타입
		tb.Cell(row, 4).Range.Text = attr.initialValueBody	# 기본값
		tb.Cell(row, 5).Range.Text = attr.documentation		# 설명
		if row >= 6:
			self.insertRowOfTable(tb, row)
	#---------------------------------------------------------------------------
	def writeOperation(self, tb, aClassInfo):
		operations = aClassInfo.operationList
		no = 1
		row = 2
		for aOper in operations:
			self.writeOperationRecord(tb,row,aOper)
			row = row + 1
			no = no + 1

	def writeOperationRecord(self, tb, row, aOper):
		i=row
		tb.Cell(i, 1).Range.Text = aOper.name					# 명
		tb.Cell(i, 2).Range.Text = aOper.visibility				# 가시성
		tb.Cell(i, 3).Range.Text = aOper.parameterString		# 파라미터
		tb.Cell(i, 4).Range.Text = aOper.returnTypeName			# 반환타입
		tb.Cell(i, 5).Range.Text = aOper.documentation			# 설명
		if row >= 6:
			self.insertRowOfTable(tb, row)

	#---------------------------------------------------------------------------
