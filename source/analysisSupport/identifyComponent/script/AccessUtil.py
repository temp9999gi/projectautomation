# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
from win32com.client import Dispatch
import pythoncom

from CommonUtil import CommonUtil

ComUtil = CommonUtil()

class AccessUtil:
	def __init__(self, inDataSource):
		self.dataSource =inDataSource
		try:
			self.accessApp=Dispatch("Access.Application")
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)

		self.accessApp.Visible=1
  		self.accessApp.OpenCurrentDatabase(self.dataSource)
  		self.aDoCmd = self.accessApp.DoCmd
  		self.aDoCmd.Maximize()
  		
	def __del__(self):
		print "__del__(self): self.accessApp.CloseCurrentDatabase ()"
		#del(self.accessApp)


	"""
		queryName='q_findComponent3'
		view = 0

		View   선택 요소로서 AcView 형식입니다.

		AcView는 다음 AcView 상수 중 하나를 사용할 수 있습니다.

		acViewDesign 1
		acViewNormal  0 기본값입니다.
		acViewPivotChart 4
		acViewPivotTable 3
		acViewPreview 2

	"""
	def openAccessQueryAction(self, queryName, view):
		
		x = self.aDoCmd.OpenQuery(queryName, view)

	def openAccessFormAction(self, formName, view):
		#aDoCmd = self.accessApp.DoCmd
		x = self.aDoCmd.OpenForm(formName, view)

