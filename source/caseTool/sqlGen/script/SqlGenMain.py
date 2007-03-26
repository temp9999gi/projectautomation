# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import sys;sys.path.append("C://_projectautomation/source/common")
import logging
import utils
# import shutil

import ExcelHelperClassList
from KlassInfoList import *
from ExcelReader import *
from Constants import *
from CommonUtil import *
import ReaderAppEnv

CONS = Constants()

class SqlWriterApp:  
	def writeSqlCore(self,aReaderAppEnv):

		inFile = CONS.INPUT_DATA_DIR / sys.argv[1]
		aExcelReader = ExcelReader(inFile, CONS)
		self.aKlassInfoList = KlassInfoList()

		xx = aExcelReader.getKlassListFromExcel()
		self.aKlassInfoList.setKlassList(xx)
		self.aKlassInfoList.setReaderAppEnv(aReaderAppEnv)

		aCommonUtil = CommonUtil()
		for aKlass in self.aKlassInfoList.getKlassList():
			aKlass.setInsertSqlAction(aKlass)
			aKlass.setUpdateSqlAction(aKlass)
			aKlass.setDeleteSqlAction(aKlass)
			aKlass.setSelectSqlAction(aKlass)
			aKlass.setSelectSqlTbAliasAction(aKlass)
##			print 'aKlass.getInsertSql\n', aKlass.getUpdateSql()
##			print 'aKlass.getInsertSql\n', aKlass.getInsertSql()
			
			outSource = aCommonUtil.generateCode(aKlass, str(CONS.SQL_TEMPLATE))
			fileName = CONS.OUT_DIR / aKlass.name + '.txt'
			aCommonUtil.writeFile(fileName, outSource)
			
		log.info('---def writeSqlCore---')
		log.info("(MSG) Ok: write Sql")
		print "(MSG)write Sql statement: Ok"


if __name__ == '__main__':
 	if len(sys.argv) < 2:
 		print "USAGE: SqlWriterApp.py input.xls"
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
	

	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)
	aSqlWriterApp = SqlWriterApp()
	aSqlWriterApp.writeSqlCore(aReaderAppEnv)

# 	if aReaderAppEnv.appEnvData["isUmlCaseInput"]=='True':
# 		#deliverableType = 'Class'
# 		aSqlWriterApp = SqlWriterApp()
# 		aSqlWriterApp.writeSqlCore(aReaderAppEnv)
		
