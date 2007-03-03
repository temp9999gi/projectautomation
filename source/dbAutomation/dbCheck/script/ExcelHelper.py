# -*- coding: utf-8 -*-
import sys
from win32com.client import Dispatch
import pythoncom
from CommonUtil import *
from Constants import *

ComUtil = CommonUtil()

CONS = Constants()


class ExcelHelper:
	def setVoList(self, voList):
		self.voList= voList
		
	def setCons(self, CONS):
		self.CONS = CONS	
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
			#xl.Sheets(cnt).Name = aClassInfo.className
			if sheetName == None:
				xl.Sheets(cnt).Name = cnt - 1
			else:
				xl.Sheets(cnt).Name = sheetName
			self.setVisible(True)

			return aTargetSheet

		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
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


