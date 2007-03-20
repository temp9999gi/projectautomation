# -*- coding: utf-8 -*-
###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2002 by: kusung																								 #
																											 #
###########################################################################
#
#			 Authors: kusung
# Last Modified: $Date: 2007/02/13 22:24:48 $
#
"""Attempts to load a model defined in an xmi file into pymerase.

Currently requires the novosoft uml reader, which implies the need for jython.
It was currently tested with 0.4.19 downloaded from the argo cvs.
"""
# start
import sys
import logging
import utils
##import xmiCommonUtil as xmiUtil
from ModelInfo import *

from WriterExcel import *
#from ParseXmiMain import *

# import system packages
#from __future__ import nested_scopes

from smw.metamodel import UML14
from smw.metamodel import UML13
from smw.io import loadModel

# ToDo:

from ModelInfo import *
from Constants import *
import CommonUtil as comUtil
#from CommonUtil import *
import ExcelHelper
import ExcelHelperClassList
import ExcelHelperUseCaseList 
import ExcelHelperClassDefiniton
import ExcelHelperClassExport
import ReaderAppEnv

CONS = Constants()
class ExcelMainSuper:
	def __init__(self):
		pass
	def initWriteExcel(self,deliverableType,aReaderAppEnv):
		self.aModelInfo = self.getModel()
		self.aModelInfo.setDefinitionType(deliverableType)
		self.aModelInfo.setReaderAppEnv(aReaderAppEnv)
		
		self.aWriterExcel = WriterExcel()


class ExcelMain(ExcelMainSuper):
	def __init__(self):
		ExcelMainSuper.__init__(self)
		
	def writeExcelClassDefinition(self,deliverableType,aReaderAppEnv):
		log.info('---def writeExcelClassDefinition---')
		self.initWriteExcel(deliverableType,aReaderAppEnv)
		aExcelHelper = ExcelHelperClassDefiniton.ExcelHelperClassDefiniton()
		aExcelHelper.setModelInfo(self.aModelInfo, CONS)

		aExcelHelper.writeExcelCoreClassDef(self.aModelInfo, aExcelHelper)

		log.info('(MSG)write ClassDefinition: Ok')

	def writeExcelClassExport(self,deliverableType,aReaderAppEnv):
		log.info('---def writeExcelClassExport---')
		self.initWriteExcel(deliverableType,aReaderAppEnv)
		aExcelHelper = ExcelHelperClassExport.ExcelHelperClassExport()
		aExcelHelper.setModelInfo(self.aModelInfo, CONS)

		aExcelHelper.writeExcelClassExport(self.aModelInfo, aExcelHelper)

		log.info('(MSG)write ClassExport: Ok')

	def writeExcelClassList(self,deliverableType,aReaderAppEnv):
		aCommonUtil = comUtil.CommonUtil()

		self.initWriteExcel(deliverableType,aReaderAppEnv)
		
		aExcelHelper = ExcelHelperClassList.ExcelHelperClassList()
		aExcelHelper.setModelInfo(self.aModelInfo, CONS)

		if self.aModelInfo.getDefinitionType()=='Interface':
			fileName = CONS.OUTPUT_INTERFACE_LIST_EXCEL
			aCommonUtil.copyTemplate(CONS.INPUT_INTERFACE_LIST_XLS_TEMPLATE , \
				fileName)

		if self.aModelInfo.getDefinitionType()=='Class':
			fileName = CONS.OUTPUT_CLASS_LIST_EXCEL
			aCommonUtil.copyTemplate(CONS.INPUT_CLASS_LIST_XLS_TEMPLATE , \
				fileName)
			
		aExcelHelper.writeExcelCoreClassList(aExcelHelper, fileName)
		log.info('---def writeExcelClassList---')
		log.info("(MSG) Ok: write Excel List(Class/IF): deliverableType['%s']",deliverableType)
		print "(MSG)write Excel List: Ok"
		
	def writeUseCaseList(self,aReaderAppEnv):
		aCommonUtil = comUtil.CommonUtil()
		aCommonUtil.copyTemplate(CONS.INPUT_USECASE_LIST_TEMPLATE , \
			CONS.OUTPUT_USECASE_LIST_EXCEL)

		self.initWriteExcel(None,aReaderAppEnv)
		
		#???????
		#aExcelHelper = ExcelHelper.ExcelHelperUseCaseList()
		aExcelHelper = ExcelHelperUseCaseList.ExcelHelperUseCaseList()
		aExcelHelper.setModelInfo(self.aModelInfo, CONS)

		aExcelHelper.writeExcelCoreUseCaseList(aExcelHelper, \
			CONS.OUTPUT_USECASE_LIST_EXCEL)
		print "(MSG) UseCaseList generated"
		
	def getModel(self):
		inFile  = CONS.INPUT_DATA_DIR / sys.argv[1]
		inFile = str(inFile)
		
		CONS.setInputXmlFile(inFile)

		aModelInfo = ModelInfo()
		aModelInfo.loadModel(inFile)
		return aModelInfo


if __name__ == '__main__':

 	if len(sys.argv) < 2:
 		print "USAGE: ExcelMain.py input.xmi"
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
	
	#deliverableType = sys.argv[2]
	#deliverableType = 'Interface' #클래스, 인터페이스
	
	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)
	#deliverableType=aReaderAppEnv.AppEnvData["deliverableType"]

	if aReaderAppEnv.AppEnvData["isClassList"]=='True':
		deliverableType = 'Class'
		ExcelMain().writeExcelClassList(deliverableType,aReaderAppEnv)
	if aReaderAppEnv.AppEnvData["isClassDefinition"]=='True':
		deliverableType = 'Class'		
		ExcelMain().writeExcelClassDefinition(deliverableType,aReaderAppEnv)

	if aReaderAppEnv.AppEnvData["isInterfaceList"]=='True':
		deliverableType = 'Interface'
		ExcelMain().writeExcelClassList(deliverableType,aReaderAppEnv)
	if aReaderAppEnv.AppEnvData["isInterfaceDefinition"]=='True':
		deliverableType = 'Interface'		
		ExcelMain().writeExcelClassDefinition(deliverableType,aReaderAppEnv)
		
	if aReaderAppEnv.AppEnvData["isUseCaseList"]=='True':
		ExcelMain().writeUseCaseList(aReaderAppEnv)

	if aReaderAppEnv.AppEnvData["isClassExport"]=='True':
		deliverableType = 'Class'
		ExcelMain().writeExcelClassExport(deliverableType,aReaderAppEnv)
	if aReaderAppEnv.AppEnvData["isInterfaceExport"]=='True':
		deliverableType = 'Interface'
		ExcelMain().writeExcelClassExport(deliverableType,aReaderAppEnv)

	#ExcelMain().writeExcelClassList(deliverableType)
	
	#sys.exit(1)

	#



