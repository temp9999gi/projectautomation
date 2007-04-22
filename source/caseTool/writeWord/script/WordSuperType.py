# -*- coding: utf-8 -*-
import sys
from win32com.client import Dispatch
import pythoncom
from CommonUtil import *
#from ReaderAppEnvXml import *
from Constants import *
import CommonUtil as comUtil

ComUtil = CommonUtil()

import logging
import utils

log = logging.getLogger('WordlHelper')

class WordSuperType:
	def __init__(self):
		self.app = Dispatch("Word.Application")
	
	def openWord(self, filename):
		try:
			#filename은 풀 패스를 가지고 있어야 함
			self.doc = self.app.Documents.Open(filename)
			self.filename = filename
			#self.workFile = self.app.ActiveWorkbook.Name
			#return self.doc
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
	def getActiveDoc(self):
		return self.app.ActiveDocument

	def getApp(self):
		return self.app

	def getDoc(self):
		return self.doc
	def setVisible(self, isVisible):
		#pass
		self.app.Visible = isVisible

	def insertRowOfTable(self, tb, row):
		tb.Rows(row).Select()
		self.app.Selection.InsertRowsBelow(1)

	def closeWord(self):
		try:
			del self.app
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)

	def closeActiveDocument(self):
		try:
			self.app.ActiveDocument.Close()
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)

