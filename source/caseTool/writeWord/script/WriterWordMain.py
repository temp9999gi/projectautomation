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
import CommonUtil as ComUtil
#from WordlHelper import *
#from ReaderAppEnvXml import *

# start
import sys
import logging
import utils

import ReaderAppEnv

CONS = Constants()

import shutil

import WordlHelper


class WriteWordMain:
	def initWriteAction(self,deliverableType,aReaderAppEnv):
		
		inFile = CONS.INPUT_DATA_DIR / sys.argv[1]
		aExcelReader = ExcelReader(inFile)
		self.aModelInfo = KlassInfoList()
		self.aModelInfo.setKlassList(aExcelReader.getKlassListFromExcel())
		#self.aModelInfo = aKlassInfoList
		#self.aModelInfo = self.getModel()
		self.aModelInfo.setReaderAppEnv(aReaderAppEnv)

		self.aModelInfo.setDefinitionType(deliverableType)

		
	def writeAction(self,deliverableType,aReaderAppEnv):
		log.info('---def writeAction---')
		self.initWriteAction(deliverableType,aReaderAppEnv)
		
		aWordlHelper = WordlHelper.WordlHelper()
		aWordlHelper.setModelInfo(self.aModelInfo, CONS)

		aWordlHelper.writeAction()

		log.info('(MSG)write ClassDefinition: Ok')



if __name__ == '__main__':
 	if len(sys.argv) < 2:
 		print "USAGE: WriteWordMain.py input.xls"
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

	if aReaderAppEnv.appEnvData["isClassDefinition"]=='True':
		deliverableType = 'Class'
		aWriteWordMain = WriteWordMain()
		aWriteWordMain.writeAction(deliverableType, aReaderAppEnv)


	if aReaderAppEnv.appEnvData["isInterfaceDefinition"]=='True':
		deliverableType = 'Interface'
		aWriteWordMain = WriteWordMain()
		aWriteWordMain.writeAction(deliverableType, aReaderAppEnv)

