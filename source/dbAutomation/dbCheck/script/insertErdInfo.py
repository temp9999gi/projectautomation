# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import sys;sys.path.append("C://_projectautomation/source/common")
import logging
import log.utils as utils

import excelLib.ExcelHelperClassList as ExcelHelperClassList
from excelLib.ExcelReader import *
from excelLib.KlassInfoList import *
from excelLib.CommonUtil import *
from excelLib.ErdInfoDao import ErdInfoDao

from Constants import *

#import ReaderAppEnv


#from TbNameKorAndNullDao import TbNameKorAndNullDao

CONS = Constants()
def getList(cursor):
	voList = []
	for row in cursor:
		voList.append(row)
	return voList
class WriterApp:
	#def writeAction(self,aReaderAppEnv):
	def writeAction(self):

		inFile = path(sys.argv[1])
#		print inFile
		aExcelReader = ExcelReader(inFile, CONS)
		self.aKlassInfoList = KlassInfoList()

		cl = aExcelReader.getKlassListFromExcel()
		self.aKlassInfoList.setKlassList(cl)
		#self.aKlassInfoList.setReaderAppEnv(aReaderAppEnv)

		#-----------------------------------------------------------------------
		# db에 저장한다.
		xx = 'C:\_projectautomation\source\dbAutomation\dbCheck\db\MyDB.mdb'
		dataSource=xx.replace('\\', "/") # replace( old, new[, count])
		aErdInfoDao = ErdInfoDao(dataSource)
		
		tableList = self.aKlassInfoList.getKlassList()
		aErdInfoDao.deleteAllAction()
		aErdInfoDao.insertAction(tableList)

		log.info('---def writeAction---')
		log.info("(MSG)insert: Ok")
		print "(MSG)insert: Ok"


if __name__ == '__main__':
 	if len(sys.argv) < 2:
 		print "USAGE: WriterApp.py input.xls"
 		sys.exit()

	inPath = sys.argv[0]
	CONS.setConstant(inPath)

	utils.initLog(CONS.LOG_FILE)
	utils.addConsoleLogging()
	log = logging.getLogger('ExcelMain')

	#log.debug("argv0: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	log.debug("---input argument---")
	log.debug("sys.argv[0]: ['%s']",sys.argv[0])
	log.debug("sys.argv[1]: ['%s']",sys.argv[1])
	

##	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
##	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)
	aWriterApp = WriterApp()
	#aWriterApp.writeAction(aReaderAppEnv)
	aWriterApp.writeAction()
	print "(MSG) OK"

