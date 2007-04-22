﻿# -*- coding: utf-8 -*-
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
		self.app = Dispatch("HWPFrame.HwpObject.1")

	def openWord(self, filename):
		try:
			#filename은 풀 패스를 가지고 있어야 함
			#self.doc = self.app.Documents.Open(filename)
			#self.hwpDocs = hwpApp.XHwpDocuments
			self.doc = self.app.XHwpDocuments
			
			self.app.HAction.GetDefault("FileOpen", self.app.HParameterSet.HFileOpenSave.HSet);
			self.app.HParameterSet.HFileOpenSave.OpenFlag = 0;
			self.app.HParameterSet.HFileOpenSave.FileName = filename;
			self.app.HParameterSet.HFileOpenSave.OpenReadOnly = 0;
			self.app.HAction.Execute("FileOpen", self.app.HParameterSet.HFileOpenSave.HSet);

			self.filename = filename
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
	def getActiveDoc(self):
		return self.app.ActiveDocument

	def getApp(self):
		return self.app

	def getDoc(self):
		return self.doc
	def setVisible(self, isVisible):
		pass
		#self.app.Visible = isVisible
	def moveTopLevelEnd(self):
		self.app.HAction.Run("MoveTopLevelEnd");
		#HAction.Run("MoveTopLevelBegin");
	def breakPage(self):
		self.app.HAction.Run("BreakPage");
	
	def insertRowOfTable(self, tb, row):
		tb.Rows(row).Select()
		self.app.Selection.InsertRowsBelow(1)

	def closeWord(self):
		try:
			del self.app
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)

	def closeActiveDocument(self,fileName):
		try:
			#self.app.ActiveDocument.Close()
			self.app.HAction.GetDefault("FileSaveAs", self.app.HParameterSet.HFileOpenSave.HSet);
			self.app.HParameterSet.HFileOpenSave.Attributes = 2048;
			self.app.HParameterSet.HFileOpenSave.FileName = fileName;
			self.app.HParameterSet.HFileOpenSave.Format = "HWP";
			self.app.HAction.Execute("FileSaveAs", self.app.HParameterSet.HFileOpenSave.HSet);
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)

