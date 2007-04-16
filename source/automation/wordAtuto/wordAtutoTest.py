# -*- coding: utf-8 -*-
# 
# generates xml files from Word
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import sys;sys.path.append("C://_projectautomation/source/common")
#import sys
from win32com.client import Dispatch
import pythoncom
#from commonUtil.CommonUtil import *
#from ReaderAppEnvXml import *
from commonUtil.Constants import *
import commonUtil.CommonUtil as comUtil

ComUtil = comUtil.CommonUtil()

import logging
#import utils

log = logging.getLogger('ExcelHelper')

def WordSaveHTML(self,out_dir):
	"""open the word document and save it as a html file"""
	self.out_path=os.path.join(out_dir,self.fname_new)
	self.out_dir=out_dir
	app = win32com.client.Dispatch("Word.Application")
	doc=app.Documents.Open(self.path)

	#get the document subject and category for possible later use
	self.subject=doc.BuiltInDocumentProperties('Subject').__str__()
	self.category=doc.BuiltInDocumentProperties('Category').__str__()

	try:
			doc.SaveAs(self.out_path, FileFormat=8, AddToRecentFiles=0)
	except:
			print 'MS Word failed to save', self.out_path
	doc.Close()
	self.__move_images()
	self.html=open(self.out_path,'r').read()
	
	
class WordHelper:
	def __init__(self):
		self.aModelInfo = None

	def openWord(self, filename):
		try:
			self.app = Dispatch("Word.Application")
			#filename은 풀 패스를 가지고 있어야 함
			self.doc = self.app.Documents.Open(filename)
			self.filename = filename
			#self.workFile = self.app.ActiveWorkbook.Name
			#return self.doc

		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)
			
	def getApp(self):
		return self.app

	def getDoc(self):
		return self.doc
	
	def setVisible(self, isVisible):
		#pass
		self.app.Visible = isVisible
		
	def closeWord(self):
		try:
			self.app.ActiveWorkbook.Close(1) #1이면 저장을 한다.
			del self.app
		except pythoncom.com_error, (hr, msg, exc, arg):
			ComUtil.printPythonComError(hr, msg, exc, arg)

#---------------------------------------------------------------------------


	def writXX(self, tb):
		#aReaderAppEnv=self.aModelInfo.getReaderAppEnv()
		# row, col
		tb.Cell(1, 1).Range.Text = '1'#aReaderAppEnv.appEnvData["writer"]	# 작성자
		tb.Cell(1, 2).Range.Text = '2'#aReaderAppEnv.appEnvData["writeDate"]# 작성일
		tb.Cell(1, 3).Range.Text = '3'#aReaderAppEnv.appEnvData["subSystemName"] # 서브시스템



xx='C://_python/wordAtuto/test.doc'
aWordHelper=WordHelper()
aWordHelper.openWord(xx)
app = aWordHelper.getApp()

aWordHelper.setVisible(True)

activeDoc=app.ActiveDocument

cells = activeDoc.Tables(1).Columns(1).Cells
for x in cells:
	x.Range.Text='1'


cells = app.ActiveDocument.Tables(2).Columns(2).Cells
for x in cells:
	x.Range.Text='2'


xx= activeDoc.Tables(1).Cell(1, 1)
xx.Range.Delete
xx.Range.InsertBefore("Sales")
xx.Column.Sort

tb = activeDoc.Tables(1)
aWordHelper.writXX(tb)
