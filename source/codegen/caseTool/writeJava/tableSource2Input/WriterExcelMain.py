# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import sys
from KlassInfoList import *
from ExcelReader import *
from Constants import *
from CommonUtil import *
#from ExcelHelper import *
#from ReaderAppEnvXml import *

# start
import sys
import logging
import utils

import ReaderAppEnv

CONS = Constants()

import shutil

import ExcelHelperClassList

class WriterExcelMain:  
	def initWriteExcel(self,deliverableType,aReaderAppEnv):
		
		inFile = CONS.INPUT_DATA_DIR / sys.argv[1]
		aExcelReader = ExcelReader(inFile, CONS)
		self.aModelInfo = KlassInfoList()
		xx = aExcelReader.getKlassListFromExcel()
		self.aModelInfo.setKlassList(xx)
		self.aModelInfo.setReaderAppEnv(aReaderAppEnv)

		self.aModelInfo.setDefinitionType(deliverableType)

	def writeExcelClassList(self,deliverableType,aReaderAppEnv):
		aCommonUtil = CommonUtil()

		self.initWriteExcel(deliverableType,aReaderAppEnv)

		aExcelHelper = ExcelHelperClassList.ExcelHelperClassList(CONS)
		aExcelHelper.setModelInfo(self.aModelInfo)

##		if self.aModelInfo.getDefinitionType()=='Class':
##			fileName = CONS.OUTPUT_CLASS_LIST_EXCEL
##			aCommonUtil.copyTemplate(CONS.INPUT_CLASS_LIST_XLS_TEMPLATE , \
##				fileName)

		fileName = CONS.INPUT_CLASS_ATTRIBUTE
		aExcelHelper.writeExcelCoreClassList(aExcelHelper, fileName)
		
		log.info('---def writeExcelClassList---')
		log.info("(MSG) Ok: write Excel List(Class/IF): deliverableType['%s']",deliverableType)
		print "(MSG)write Excel List: Ok"


if __name__ == '__main__':
 	if len(sys.argv) < 2:
 		print "USAGE: WriterExcelMain.py input.xls"
 		sys.exit()

	inPath = sys.argv[0]
	CONS.setConstant(inPath)

	#CONS.LOG_FILE

	utils.initLog(CONS.LOG_FILE)
	utils.addConsoleLogging()
	log = logging.getLogger('ExcelMain')

	#log.debug("argv0: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	log.debug("---input argument---")
	log.debug("sys.argv[0]: ['%s']",sys.argv[0])
	log.debug("sys.argv[1]: ['%s']",sys.argv[1])
	

	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)

	if aReaderAppEnv.appEnvData["isUmlCaseInput"]=='True':
		deliverableType = 'Class'
		aWriterExcelMain = WriterExcelMain()
		aWriterExcelMain.writeExcelClassList(deliverableType,aReaderAppEnv)
