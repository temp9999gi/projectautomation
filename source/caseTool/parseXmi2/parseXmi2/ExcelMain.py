# -*- coding: utf-8 -*-
# start
import sys;sys.path.append("C://_projectautomation/source/common")
import logging
import utils
import xmiCommonUtil as xmiUtil
from ModelInfo import *

from WriterExcel import *
from ParseXmiMain import *

# ToDo: xmi파싱 부분을 공통화해라..
utils.initLog('ExcelMain.log')
utils.addConsoleLogging()
log = logging.getLogger('ExcelMain')

from Constants import *
CONS = Constants()

class ExcelMain:
	def writeExcelClassDefinition(self):
		aModelInfo = self.getModel()

		aWriterExcel = WriterExcel()
		aWriterExcel.writeExcelClassDefinition(aModelInfo)
		print "(MSG) Ok"
	def writeExcelClassList(self):
		aModelInfo = self.getModel()

		aWriterExcel = WriterExcel()
		aWriterExcel.writeExcelClassList(aModelInfo)
		print "(MSG) Ok"
		
	def getModel(self):
		inFile  = CONS.INPUT_DIR / sys.argv[1]
		inFile = str(inFile)
		
		CONS.setInputXmlFile(inFile)

		aModelInfo = ParseXmiMain().getModelInfo(inFile)
		return aModelInfo


if __name__ == '__main__':

# 	if len(sys.argv) < 2:
# 		print "USAGE: python ParseXmiMain.py input.xmi"
# 		sys.exit()

	ExcelMain().writeExcelClassDefinition()
	#ExcelMain().writeExcelClassList()



