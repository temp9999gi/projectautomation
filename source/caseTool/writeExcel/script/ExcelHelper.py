# -*- coding: utf-8 -*-
import sys
from win32com.client import Dispatch
import pythoncom
from CommonUtil import *

from Constants import *
import CommonUtil as comUtil

ComUtil = CommonUtil()

import logging
import utils

log = logging.getLogger('ExcelHelper')

class ExcelHelper:
	def __init__(self):
		self.aModelInfo = None

	def setModelInfo(self, aModelInfo, CONS):
		self.aModelInfo = aModelInfo
		self.CONS = CONS
	def getModelInfo(self):
		return self.aModelInfo
		
	def openExcelSheet(self, filename):
		try:
			self.xl = Dispatch("Excel.Application")
			#filename은 풀 패스를 가지고 있어야 함
			self.xl.Workbooks.Open(filename)
			self.filename = filename
			self.workFile = self.xl.ActiveWorkbook.Name
			
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
			
	def addSheet(self, templName="templ", sheetName=None):
		try:
			xl = self.xl; workFile = self.workFile
			
			self.setVisible(False)
			cnt = xl.Workbooks(workFile).Sheets.Count
			aSheet = xl.Workbooks(workFile).Sheets(cnt)
			xl.Workbooks(workFile).Sheets(templName).Copy(aSheet)
			
			aTargetSheet = xl.Workbooks(workFile).Sheets(cnt) # 복사된 시트
			if sheetName == None:
				xl.Sheets(cnt).Name = cnt - 1
			else:
				xl.Sheets(cnt).Name = str(cnt - 1)+ self.getSheetName(sheetName)
				
			return aTargetSheet
			
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
			
	def getSheetName(self, inName):
		#엑셀에서 SheetName은 31자리까지 가능하다.
		#순번에 3자리, 나머지 시트 이름 28
		outSheetName = inName[0:28]
		return outSheetName
		
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
			
	def copyMethodTitle(self, aTargetSheet, inTargetRow):
		try:
			xl = self.xl
			targetSheetName = aTargetSheet.Name
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
			
	def writeHeadInfo(self, sh, aClassInfo):
		# row, col
		aReaderAppEnv=self.aModelInfo.getReaderAppEnv()
		rowWriter    = aReaderAppEnv.classTemplateEnv["rowWriter"] #        ='2'
		colWriter    = aReaderAppEnv.classTemplateEnv["colWriter"] #        ='4'
		rowWriteDate = aReaderAppEnv.classTemplateEnv["rowWriteDate"] #        ='2'
		colWriteDate = aReaderAppEnv.classTemplateEnv["colWriteDate"] #        ='6'
		rowSubSystemName = aReaderAppEnv.classTemplateEnv["rowSubSystemName"] #        ='3'
		colSubSystemName = aReaderAppEnv.classTemplateEnv["colSubSystemName"] #        ='6'

		sh.Cells(rowWriter,        colWriter).Value        = aReaderAppEnv.appEnvData["writer"]	# 작성자
		sh.Cells(rowWriteDate,     colWriteDate).Value     = aReaderAppEnv.appEnvData["writeDate"]# 작성일
		sh.Cells(rowSubSystemName, colSubSystemName).Value = aReaderAppEnv.appEnvData["subSystemName"] # 서브시스템



			

