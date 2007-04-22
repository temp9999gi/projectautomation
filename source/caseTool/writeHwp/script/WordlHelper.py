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


		ComUtil.rmPattern(self.CONS.OUT_DIR_TEMP,'*.hwp')
		for aClassInfo in outList:
			self.openWordService()

			self.writeHeadInfo()
			self.writeClassMasterInfo(aClassInfo)
			self.writeAttribute(aClassInfo)

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

	def writeClassMasterInfo(self, aClassInfo):
		#self.writeHeadInfo(tb, aClassInfo)
		#누름틀
		aClassDoc = aClassInfo.getClassDoc()
		self.app.PutFieldText("packagePath",	aClassDoc.packagePath)
		self.app.PutFieldText("klassEng",	aClassInfo.name)
		self.app.PutFieldText("classDoc",	aClassDoc.documentation) # 설명

 	#---------------------------------------------------------------------------
	def writeAttribute(self, aClassInfo):

		i = 1
		for attr in aClassInfo.fieldList:
			self.writeAttributeRecord( i, attr)
			i = i + 1

		self.setCurrentRow(i)
		
	def writeAttributeRecord(self, row, attr):
		self.app.PutFieldText("attrName" + str(row),	attr.name)
		self.app.PutFieldText("attrVisib"+ str(row),	attr.visibility)# 가시성
		self.app.PutFieldText("attrType"+ str(row),		attr.typeName)# 타입
		self.app.PutFieldText("initialValue"+ str(row),	attr.initialValueBody) # 기본값
		self.app.PutFieldText("attrDoc"+ str(row),		attr.documentation) # 설명

##		tb.Cell(row, 5).Range.Text = attr.documentation		# 설명
##		if row >= 6:
##			self.insertRowOfTable(tb, row)
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
