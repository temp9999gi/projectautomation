# -*- coding: utf-8 -*-
import sys
from win32com.client import Dispatch
import pythoncom
from CommonUtil import *
from ReaderAppEnvXml import *
from Constants import *

CONS = Constants()
ComUtil = CommonUtil()

class ExcelHelper:
	def __init__(self):
		pass
	
	def openExcelSheet(self, filename):
		try:
			self.xl = Dispatch("Excel.Application")
			#filename은 풀 패스를 가지고 있어야 함
			self.xl.Workbooks.Open(filename)
			self.filename = filename
			self.workFile = self.xl.ActiveWorkbook.Name
			
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
			
	def addSheet(self, sheetName):
		try:
			xl = self.xl; workFile = self.workFile
			
			self.setVisible(False)
			cnt = xl.Workbooks(workFile).Sheets.Count
			aSheet = xl.Workbooks(workFile).Sheets(cnt)
			xl.Workbooks(workFile).Sheets("templ").Copy(aSheet)
			
			aTargetSheet = xl.Workbooks(workFile).Sheets(cnt) # 복사된 시트
			#xl.Sheets(cnt).Name = aClassInfo.className
			xl.Sheets(cnt).Name = cnt - 1
			return aTargetSheet
			
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
			
			
	def writeExcelCoreClassList(self, aModelInfo, aExcelHelper, outputfile):

		aExcelHelper.openExcelSheet(outputfile)
		
		aTargetSheet = aExcelHelper.addSheet('sheetName')
		i = 3
		for aClassInfo in aModelInfo.classInfoList:
			aReaderAppEnvXml = ReaderAppEnvXml()
			aReaderAppEnvXml.saveWriterInfo(aClassInfo, CONS.INPUT_APP_ENV_XML)
			self.writeClassInfo(aTargetSheet, aClassInfo)
			i = i + 1
			self.writeColumn(aTargetSheet, aClassInfo, i)
			
##########		aExcelHelper.deleteSheet(['templ','method_templ']) #templ 시트 삭제
		aExcelHelper.closeExcel()
		
	def deleteSheet(self, inSheetNameList):
		try:
			xl = self.xl
			xl.DisplayAlerts = False
			self.setVisible(True)
			
			for ws in xl.Worksheets:
				#inSheetName = ['templ','method_templ']
				if ws.Name in inSheetNameList:
					xl.Worksheets(ws.Index).Delete() #Sheets(strSheetName).Index
			xl.DisplayAlerts = True
			
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
			
	def setCurrentRow(self, curRow):
		self.currentRow = curRow

	def getCurrentRow(self):
		return self.currentRow

	def setVisible(self, isVisible):
		#pass
		self.xl.Visible = isVisible

	#ToDo 로우에 대한 Fit기능을 사용한다.
	def setRowAutoFit(self, isVisible):
		pass
##    Rows("6:12").Select
##    Rows("6:12").EntireRow.AutoFit
		
	def closeExcel(self):
		try:
			self.xl.ActiveWorkbook.Close(1) #1이면 저장을 한다.
			del self.xl
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
			
	def writeExcelCoreClassDef(self, aModelInfo, aExcelHelper, outputfile):

		aExcelHelper.openExcelSheet(outputfile)

		for aClassInfo in aModelInfo.classInfoList:
			aReaderAppEnvXml = ReaderAppEnvXml()
			aReaderAppEnvXml.saveWriterInfo(aClassInfo, CONS.INPUT_APP_ENV_XML)
			aTargetSheet = aExcelHelper.addSheet(aClassInfo)
			self.writeClassInfo(aTargetSheet, aClassInfo)
			self.writeColumn(aTargetSheet, aClassInfo)
			
			self.copyMethodTitle(aTargetSheet, self.getCurrentRow())
			self.writeOperation(aTargetSheet, aClassInfo)
			#????????

		aExcelHelper.deleteSheet(['templ','method_templ']) #template 시트 삭제
		aExcelHelper.closeExcel()


	def copyMethodTitle(self, aTargetSheet, inTargetRow):
		try:
			xl = self.xl
			targetSheetName = aTargetSheet.Name
			# targetRow ="7:7"
			targetRow = str(inTargetRow) + ":" + str(inTargetRow)

			self.xl.Visible = True
			methodTemplSheet='method_templ'
			xl.Workbooks(self.workFile).Sheets(methodTemplSheet).Select()	##    Sheets("templ").Select
			xl.Worksheets(methodTemplSheet).Activate()
			xl.Worksheets(methodTemplSheet).Rows("1:1").Select() ##    Rows("1:1").Select

			xl.Selection.Copy()	##    Selection.Copy
			xl.Workbooks(self.workFile).Sheets(targetSheetName).Select()	##    Sheets("templ").Select
			xl.Worksheets(targetSheetName).Rows(targetRow).Select()	##    Rows("7:7").Select

			xl.Worksheets(targetSheetName).Paste()	##    ActiveSheet.Paste
			
			self.setCurrentRow(self.getCurrentRow()+1)

		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)

			

class ExcelHelperClassDefiniton(ExcelHelper):
	def __init__(self):
		ExcelHelper.__init__
		
	def writeClassInfo(self, sh, aClassInfo):
		# row, col
		sh.Cells(2, 3).Value = aClassInfo.subSystemName 	# 서브시스템명
		sh.Cells(2, 7).Value = aClassInfo.writer			# 작성자

		sh.Cells(3, 7).Value = aClassInfo.writeDate			# 작성일

		sh.Cells(3, 3).Value = aClassInfo.className			# 클래스명
		sh.Cells(4, 3).Value = aClassInfo.getDocumentation() # 클래스설명
		

	def writeColumn(self, sh, aClassInfo):
		i = 6
		for attr in aClassInfo.attributeListOfClassInfo:
			sh.Cells(i, 1).Value = i - 5						# 번호
			sh.Cells(i, 2).Value = attr.attributeName			# 속성명
			sh.Cells(i, 4).Value = attr.visibility				# 가시성
			sh.Cells(i, 5).Value = attr.attributeType			# 타입
			
			try:
				body = attr.initialValue.body
				print 'body', body
			except AttributeError:
				body = None
			
			sh.Cells(i, 6).Value = body			# 기본값 ????????????????????????????
			sh.Cells(i, 7).Value = attr.getDocumentation()		#'desc?????'# 설명
			i = i + 1
			
		self.setCurrentRow(i)
		
	def writeOperation(self, sh, aClassInfo):
		i = self.getCurrentRow()
		j = 1
		for x in aClassInfo.getClassOperation():
			# 번호	오퍼레이션명		가시성	파라미터	반환타입	설명

			sh.Cells(i, 1).Value = j						# 번호
			sh.Cells(i, 2).Value = x.name					# 명
			sh.Cells(i, 4).Value = x.visibility				# 가시성
			sh.Cells(i, 5).Value = x.methodParameterString				# 	파라미터
			sh.Cells(i, 6).Value = x.operationReturnType				# 반환타입
			sh.Cells(i, 7).Value = x.getDocumentation()		# 설명
			i = i + 1
			j = j + 1

			
			
			
class ExcelHelperClassList(ExcelHelper):
	def __init__(self):
		ExcelHelper.__init__

	def writeClassInfo(self, sh, aClassInfo):
		# row, col
		sh.Cells(2, 3).Value = aClassInfo.subSystemName 	# 업무명
		sh.Cells(2, 6).Value = aClassInfo.writer			# 작성자

	def writeColumn(self, sh, aClassInfo, row):
		#for attr in aClassInfo.attributeListOfClassInfo:
		i = row
		sh.Cells(i, 1).Value = i - 3							# 번호
		sh.Cells(i, 2).Value = aClassInfo.className				# 클래스명
		sh.Cells(i, 4).Value = aClassInfo.namespace				# 패키지명
		sh.Cells(i, 5).Value = 'desc????'							# 설명


